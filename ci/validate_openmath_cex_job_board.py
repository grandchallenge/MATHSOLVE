#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
BOARD = "handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"
ENTRYPOINT = "handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md"
BASE_URL = "https://github.com/grandchallenge/MATHSOLVE"
ENTRYPOINT_URL = BASE_URL + "/blob/main/" + ENTRYPOINT
REGISTRY_URL = "https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/" + REGISTRY
H1 = {
    "assignment": "OM26-H1-H1-12",
    "dispatch": "OM26-H1-H1-12-IA-001",
    "agent": "INDEPENDENT-AGENT-001",
    "issue": 498,
}
INTRO = "3c835aaf6173176b64efca5f03ffdc27b20af965"
EXPECTED = {
    f"OM26-H{i}-WP01": {
        "hill": f"OM26-H{i}",
        "dispatch": f"OM26-H{i}-WP01-IA-001",
        "agent": f"INDEPENDENT-AGENT-00{i}",
        "issue": 503 + i,
    }
    for i in range(2, 8)
}
H2_WP02 = {
    "assignment": "OM26-H2-WP02",
    "hill": "OM26-H2",
    "dispatch": "OM26-H2-WP02-IA-001",
    "agent": "INDEPENDENT-AGENT-008",
    "issue": 526,
}


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def absolute_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and bool(parsed.path)


def git_blob_sha1(path: str) -> str:
    data = (ROOT / path).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    registry = load(REGISTRY)
    if registry.get("record_type") != "GCL_CEX_ASSIGNMENT_REGISTRY":
        errors.append("registry record_type mismatch")

    discovery = registry.get("discovery", {})
    if discovery.get("entrypoint_url") != ENTRYPOINT_URL or not absolute_https(discovery.get("entrypoint_url")):
        errors.append("entrypoint discovery mismatch")
    if discovery.get("machine_registry_url") != REGISTRY_URL or not absolute_https(discovery.get("machine_registry_url")):
        errors.append("machine registry discovery mismatch")
    if registry.get("lease_policy", {}).get("external_self_claim_allowed") is not False:
        errors.append("external self-claim enabled")

    math = [x for x in registry.get("assignments", []) if x.get("class") == "MATHEMATICAL_RESEARCH"]
    h1 = [x for x in math if x.get("assignment_id") == H1["assignment"]]
    if len(h1) != 1:
        errors.append("H1 assignment missing")
    else:
        item = h1[0]
        lease = item.get("lease", {})
        if item.get("state") not in {"CAPTURED", "ACCEPTED"} or lease.get("state") != "CLOSED_AFTER_RETURN":
            errors.append("H1 lifecycle must be CAPTURED or ACCEPTED with CLOSED_AFTER_RETURN")
        if item.get("state") == "CAPTURED" and item.get("lifecycle", {}).get("adjudication") != "PENDING":
            errors.append("captured H1 result must remain pending adjudication")
        if item.get("state") == "ACCEPTED" and item.get("lifecycle", {}).get("adjudication") != "ACCEPTED_SOURCE_CONDITIONAL_REDUCTION":
            errors.append("accepted H1 adjudication state mismatch")
        if lease.get("execution_authorized") is not False:
            errors.append("H1 returned lease must not remain executable")
        if (
            lease.get("dispatch_id") != H1["dispatch"]
            or lease.get("agent_ref") != H1["agent"]
            or lease.get("dispatch_issue_number") != H1["issue"]
        ):
            errors.append("H1 lease identity mismatch")

    seen_agents: set[str] = set()
    seen_issues: set[int] = set()
    seen_dispatches: set[str] = set()
    for aid, expected in EXPECTED.items():
        items = [x for x in math if x.get("assignment_id") == aid]
        if len(items) != 1:
            errors.append(f"{aid}: expected exactly one assignment")
            continue
        item = items[0]
        lease = item.get("lease", {})
        if item.get("hill") != expected["hill"] or item.get("slot_binding") != expected["hill"]:
            errors.append(f"{aid}: hill binding mismatch")
        if aid == "OM26-H2-WP01":
            if item.get("state") != "ACCEPTED" or lease.get("state") != "CLOSED_AFTER_RETURN":
                errors.append(f"{aid}: not ACCEPTED with CLOSED_AFTER_RETURN")
            if item.get("lifecycle", {}).get("launched") is not True:
                errors.append(f"{aid}: accepted return must record execution")
            if item.get("lifecycle", {}).get("adjudication") != "ACCEPTED_SCORER_CONCORDANCE_WITH_SEARCH_NARROWING":
                errors.append(f"{aid}: adjudication mismatch")
            if lease.get("execution_authorized") is not False:
                errors.append(f"{aid}: closed returned lease remains executable")
        else:
            if item.get("state") != "LEASED_NOT_LAUNCHED" or lease.get("state") != "LEASED":
                errors.append(f"{aid}: not LEASED_NOT_LAUNCHED with protected lease")
            if item.get("lifecycle", {}).get("launched") is not False:
                errors.append(f"{aid}: launch evidence must remain absent")
        if (
            lease.get("dispatch_id") != expected["dispatch"]
            or lease.get("agent_ref") != expected["agent"]
            or lease.get("dispatch_issue_number") != expected["issue"]
        ):
            errors.append(f"{aid}: lease identity mismatch")
        if lease.get("protected_lease_commit") != INTRO:
            errors.append(f"{aid}: introducing commit mismatch")
        url = BASE_URL + f"/issues/{expected['issue']}"
        if lease.get("dispatch_url") != url or lease.get("return_url") != url:
            errors.append(f"{aid}: return URL mismatch")
        if expected["agent"] in seen_agents:
            errors.append(f"{aid}: duplicate agent_ref")
        if expected["issue"] in seen_issues:
            errors.append(f"{aid}: duplicate issue")
        if expected["dispatch"] in seen_dispatches:
            errors.append(f"{aid}: duplicate dispatch")
        seen_agents.add(expected["agent"])
        seen_issues.add(expected["issue"])
        seen_dispatches.add(expected["dispatch"])

        expected_wp = f"handoffs/OPENMATH-2026/jobs/{expected['dispatch']}.md"
        if item.get("work_package") != expected_wp or item.get("work_package_url") != BASE_URL + "/blob/main/" + expected_wp:
            errors.append(f"{aid}: work-package locator mismatch")
        dispatch_path = item.get("dispatch_record")
        operation_path = item.get("operation_contract")
        if not dispatch_path or not (ROOT / dispatch_path).is_file():
            errors.append(f"{aid}: dispatch record missing")
            continue
        if not operation_path or not (ROOT / operation_path).is_file():
            errors.append(f"{aid}: operation contract missing")
            continue
        dispatch = load(dispatch_path)
        operation = load(operation_path)
        if dispatch.get("dispatch_id") != expected["dispatch"] or dispatch.get("agent_ref") != expected["agent"] or dispatch.get("assignment_id") != aid:
            errors.append(f"{aid}: dispatch record identity mismatch")
        if dispatch.get("github_issue_number") != expected["issue"] or dispatch.get("github_issue_url") != url:
            errors.append(f"{aid}: dispatch issue mismatch")
        if dispatch.get("bootstrap_path") != expected_wp:
            errors.append(f"{aid}: bootstrap path mismatch")
        if dispatch.get("bootstrap_blob_sha1") != git_blob_sha1(expected_wp):
            errors.append(f"{aid}: bootstrap blob mismatch")
        if operation.get("dispatch_id") != expected["dispatch"] or operation.get("agent_ref") != expected["agent"] or operation.get("assignment_id") != aid:
            errors.append(f"{aid}: operation identity mismatch")
        if not isinstance(operation.get("acceptable_dispositions"), list) or not operation["acceptable_dispositions"]:
            errors.append(f"{aid}: no acceptable dispositions")

    wp02_items = [x for x in math if x.get("assignment_id") == H2_WP02["assignment"]]
    if len(wp02_items) != 1:
        errors.append("OM26-H2-WP02: expected exactly one assignment")
    else:
        item = wp02_items[0]
        lease = item.get("lease", {})
        url = BASE_URL + f"/issues/{H2_WP02['issue']}"
        if item.get("hill") != H2_WP02["hill"] or item.get("slot_binding") != H2_WP02["hill"]:
            errors.append("OM26-H2-WP02: hill binding mismatch")
        if item.get("state") != "LEASED_NOT_LAUNCHED" or lease.get("state") != "LEASED":
            errors.append("OM26-H2-WP02: must be LEASED_NOT_LAUNCHED with protected lease")
        if item.get("lifecycle", {}).get("launched") is not False:
            errors.append("OM26-H2-WP02: launch evidence must remain absent")
        if lease.get("dispatch_id") != H2_WP02["dispatch"] or lease.get("agent_ref") != H2_WP02["agent"] or lease.get("dispatch_issue_number") != H2_WP02["issue"]:
            errors.append("OM26-H2-WP02: lease identity mismatch")
        if lease.get("dispatch_url") != url or lease.get("return_url") != url:
            errors.append("OM26-H2-WP02: return URL mismatch")
        if lease.get("protected_lease_commit") not in {"PENDING_PROTECTED_MERGE", lease.get("protected_lease_merge")}:
            errors.append("OM26-H2-WP02: protected lease commit state mismatch")
        expected_wp = f"handoffs/OPENMATH-2026/jobs/{H2_WP02['dispatch']}.md"
        if item.get("work_package") != expected_wp or item.get("work_package_url") != BASE_URL + "/blob/main/" + expected_wp:
            errors.append("OM26-H2-WP02: work-package locator mismatch")
        dispatch = load(item["dispatch_record"])
        operation = load(item["operation_contract"])
        if dispatch.get("dispatch_id") != H2_WP02["dispatch"] or dispatch.get("agent_ref") != H2_WP02["agent"] or dispatch.get("assignment_id") != H2_WP02["assignment"]:
            errors.append("OM26-H2-WP02: dispatch identity mismatch")
        if dispatch.get("github_issue_number") != H2_WP02["issue"] or dispatch.get("github_issue_url") != url:
            errors.append("OM26-H2-WP02: dispatch issue mismatch")
        if dispatch.get("bootstrap_path") != expected_wp or dispatch.get("bootstrap_blob_sha1") != git_blob_sha1(expected_wp):
            errors.append("OM26-H2-WP02: bootstrap binding mismatch")
        if operation.get("dispatch_id") != H2_WP02["dispatch"] or operation.get("agent_ref") != H2_WP02["agent"] or operation.get("assignment_id") != H2_WP02["assignment"]:
            errors.append("OM26-H2-WP02: operation identity mismatch")
        if set(operation.get("acceptable_dispositions", [])) != {"EXACT_SEARCH_DESIGN_VALIDATED", "EXACT_PRUNING_COUNTEREXAMPLE", "BOUNDED_CANDIDATE_FOUND", "EXACT_BLOCKER"}:
            errors.append("OM26-H2-WP02: acceptable dispositions mismatch")

    topology = registry.get("current_topology", {})
    if topology.get("lane_model") != "SEVEN_FIRST_CLASS_HILLS":
        errors.append("current assignment topology is not seven first-class hills")
    if topology.get("hills") != [f"OM26-H{i}" for i in range(1, 8)]:
        errors.append("current assignment hill roster mismatch")
    policy = registry.get("mathematics_release_policy", {})
    per_hill = policy.get("per_hill", {})
    if set(per_hill) != {f"OM26-H{i}" for i in range(1, 8)}:
        errors.append("per-hill release policy roster mismatch")
    if per_hill.get("OM26-H1", {}).get("agent_state") != "ACCEPTED":
        errors.append("H1 per-hill agent state mismatch")
    if per_hill.get("OM26-H2", {}).get("agent_state") != "LEASED_NOT_LAUNCHED" or per_hill.get("OM26-H2", {}).get("assignment") != "OM26-H2-WP02":
        errors.append("H2 per-hill active WP02 state mismatch")
    predecessor = per_hill.get("OM26-H2", {}).get("predecessor", {})
    if predecessor.get("assignment") != "OM26-H2-WP01" or predecessor.get("agent_state") != "ACCEPTED":
        errors.append("H2 per-hill predecessor state mismatch")
    for i in range(3, 8):
        if per_hill.get(f"OM26-H{i}", {}).get("agent_state") != "LEASED_NOT_LAUNCHED":
            errors.append(f"OM26-H{i} per-hill agent state mismatch")
    summary = policy.get("summary", {})
    if summary != {
        "released_hills": 7,
        "accepted_agents": 2,
        "leased_not_launched_agents": 6,
        "launched_agents": 0,
        "returned_unadjudicated_agents": 0,
    }:
        errors.append("seven-hill release summary mismatch")
    historical = policy.get("historical_tranche_metrics", {})
    if historical.get("deprecated_for_current_state") is not True:
        errors.append("historical H2-H7 metrics are not deprecated for current state")
    if registry.get("wp01_leases", {}).get("lease_introducing_commit") != INTRO:
        errors.append("historical lease introducing commit mismatch")

    board = (ROOT / BOARD).read_text(encoding="utf-8")
    for expected in [*EXPECTED.values(), H2_WP02]:
        for marker in (expected["dispatch"], expected["agent"], f"#{expected['issue']}"):
            if marker not in board:
                errors.append(f"board missing {marker}")
    entry = (ROOT / ENTRYPOINT).read_text(encoding="utf-8")
    for marker in (ENTRYPOINT_URL, REGISTRY_URL, "DISPATCH_ID:", "AGENT_REF:", "work_package_url"):
        if marker not in entry:
            errors.append(f"entrypoint missing {marker}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: OPENMATH CEX exposes seven first-class hill lanes with exact per-hill lifecycle state")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

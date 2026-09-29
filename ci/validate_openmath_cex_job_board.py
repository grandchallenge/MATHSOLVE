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
        if item.get("state") != "CAPTURED" or lease.get("state") != "CLOSED_AFTER_RETURN":
            errors.append("H1 lifecycle must be CAPTURED/CLOSED_AFTER_RETURN")
        if item.get("lifecycle", {}).get("adjudication") != "PENDING":
            errors.append("H1 recovered result must remain pending adjudication")
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

    policy = registry.get("mathematics_release_policy", {})
    if policy.get("h2_h7_available_math_jobs") != 0 or policy.get("h2_h7_leased_math_jobs") != 6:
        errors.append("H2-H7 lease counters mismatch")
    if (
        policy.get("h2_h7_launched_math_jobs") != 0
        or policy.get("h2_h7_returned_math_jobs") != 0
        or policy.get("h2_h7_captured_math_jobs") != 0
    ):
        errors.append("H2-H7 lifecycle counters must remain zero beyond lease")
    if registry.get("wp01_leases", {}).get("lease_introducing_commit") != INTRO:
        errors.append("aggregate lease introducing commit mismatch")

    board = (ROOT / BOARD).read_text(encoding="utf-8")
    for expected in EXPECTED.values():
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
    print("PASS: OPENMATH CEX exposes CAPTURED H1 evidence and six H2-H7 LEASED_NOT_LAUNCHED assignments")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

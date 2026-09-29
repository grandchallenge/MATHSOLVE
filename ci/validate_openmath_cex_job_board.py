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
INTRO = "3c835aaf6173176b64efca5f03ffdc27b20af965"
H1 = {"assignment":"OM26-H1-H1-12","dispatch":"OM26-H1-H1-12-IA-001","agent":"INDEPENDENT-AGENT-001","issue":498}
H2_WP01 = {"assignment":"OM26-H2-WP01","dispatch":"OM26-H2-WP01-IA-001","agent":"INDEPENDENT-AGENT-002","issue":505}
H2_WP02 = {"assignment":"OM26-H2-WP02","dispatch":"OM26-H2-WP02-IA-001","agent":"INDEPENDENT-AGENT-008","issue":526}
H2_WP03 = {"assignment":"OM26-H2-WP03","dispatch":"OM26-H2-WP03-IA-001","agent":"INDEPENDENT-AGENT-009","issue":537}
EXPECTED = {
    f"OM26-H{i}-WP01": {
        "hill": f"OM26-H{i}",
        "dispatch": f"OM26-H{i}-WP01-IA-001",
        "agent": f"INDEPENDENT-AGENT-00{i}",
        "issue": 503 + i,
    }
    for i in range(3, 8)
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
    assignments = {x["assignment_id"]: x for x in registry.get("assignments", [])}

    if registry.get("record_type") != "GCL_CEX_ASSIGNMENT_REGISTRY":
        errors.append("registry record_type mismatch")
    if registry.get("current_topology", {}).get("hills") != [f"OM26-H{i}" for i in range(1, 8)]:
        errors.append("current hill roster mismatch")
    if registry.get("current_topology", {}).get("grouped_current_lanes") != []:
        errors.append("grouped current lanes must be empty")

    def closed(item_id: str, disposition: str):
        item = assignments.get(item_id, {})
        if item.get("state") != "ACCEPTED":
            errors.append(f"{item_id}: not ACCEPTED")
        if item.get("lease", {}).get("state") != "CLOSED_AFTER_RETURN":
            errors.append(f"{item_id}: lease not CLOSED_AFTER_RETURN")
        if item.get("lease", {}).get("execution_authorized") is not False:
            errors.append(f"{item_id}: closed lease executable")
        if item.get("lifecycle", {}).get("adjudication") != disposition:
            errors.append(f"{item_id}: adjudication mismatch")
        if item.get("lifecycle", {}).get("closed") is not True:
            errors.append(f"{item_id}: lifecycle not closed")

    closed(H1["assignment"], "ACCEPTED_SOURCE_CONDITIONAL_REDUCTION")
    closed(H2_WP01["assignment"], "ACCEPTED_SCORER_CONCORDANCE_WITH_SEARCH_NARROWING")
    closed(H2_WP02["assignment"], "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED")

    wp03 = assignments.get(H2_WP03["assignment"], {})
    lease = wp03.get("lease", {})
    if wp03.get("state") != "LEASED_NOT_LAUNCHED" or lease.get("state") != "LEASED":
        errors.append("OM26-H2-WP03: not LEASED_NOT_LAUNCHED")
    if (lease.get("dispatch_id"), lease.get("agent_ref"), lease.get("dispatch_issue_number")) != (
        H2_WP03["dispatch"], H2_WP03["agent"], H2_WP03["issue"]
    ):
        errors.append("OM26-H2-WP03: lease identity mismatch")
    if lease.get("protected_lease_merge") != "208fa322f52d06eb7f9b6affff0f359217a5118e" or lease.get("readback_verified") is not True:
        errors.append("OM26-H2-WP03: protected readback mismatch")
    if lease.get("execution_authorized") is not True or wp03.get("lifecycle", {}).get("launched") is not False:
        errors.append("OM26-H2-WP03: execution/launch state mismatch")
    if wp03.get("dispatch_record") != "contributions/OPENMATH-2026/OM26-H2/WP03/dispatches/OM26-H2-WP03-IA-001.json":
        errors.append("OM26-H2-WP03: dispatch locator mismatch")
    if git_blob_sha1(wp03["work_package"]) != load(wp03["dispatch_record"])["bootstrap_blob_sha1"]:
        errors.append("OM26-H2-WP03: bootstrap binding mismatch")

    seen_agents={H2_WP03["agent"]}
    seen_issues={H2_WP03["issue"]}
    seen_dispatches={H2_WP03["dispatch"]}
    for aid, expected in EXPECTED.items():
        item = assignments.get(aid, {})
        lease = item.get("lease", {})
        if item.get("state") != "LEASED_NOT_LAUNCHED" or lease.get("state") != "LEASED":
            errors.append(f"{aid}: not LEASED_NOT_LAUNCHED")
        if item.get("lifecycle", {}).get("launched") is not False:
            errors.append(f"{aid}: unexpectedly launched")
        if lease.get("protected_lease_commit") != INTRO:
            errors.append(f"{aid}: lease introducing commit mismatch")
        if (lease.get("dispatch_id"), lease.get("agent_ref"), lease.get("dispatch_issue_number")) != (
            expected["dispatch"], expected["agent"], expected["issue"]
        ):
            errors.append(f"{aid}: lease identity mismatch")
        if expected["agent"] in seen_agents or expected["issue"] in seen_issues or expected["dispatch"] in seen_dispatches:
            errors.append(f"{aid}: duplicate current lease identity")
        seen_agents.add(expected["agent"]); seen_issues.add(expected["issue"]); seen_dispatches.add(expected["dispatch"])

    policy = registry.get("mathematics_release_policy", {})
    h2 = policy.get("per_hill", {}).get("OM26-H2", {})
    if h2.get("assignment") != "OM26-H2-WP03" or h2.get("agent_state") != "LEASED_NOT_LAUNCHED":
        errors.append("H2 release policy not on WP03")
    pred = h2.get("predecessor", {})
    if pred.get("assignment") != "OM26-H2-WP02" or pred.get("agent_state") != "ACCEPTED":
        errors.append("H2 predecessor policy mismatch")
    if policy.get("summary") != {
        "released_hills": 7,
        "accepted_agents": 3,
        "leased_not_launched_agents": 6,
        "launched_agents": 0,
        "returned_unadjudicated_agents": 0,
    }:
        errors.append("release summary mismatch")

    board=(ROOT/BOARD).read_text(encoding="utf-8")
    for marker in (
        "| `OM26-H2-WP02` | `OM26-H2` | `ACCEPTED` |",
        "| `OM26-H2-WP03` | `OM26-H2` | `LEASED_NOT_LAUNCHED` |",
        "Agent 009",
        "#537",
    ):
        if marker not in board:
            errors.append(f"board missing {marker}")

    entry=(ROOT/ENTRYPOINT).read_text(encoding="utf-8")
    for marker in ("LINK_IN_RELAY_OUT","<TASK_URL>","GCL-RETURN-RELAY/1","Authenticated GCL infrastructure"):
        if marker not in entry:
            errors.append(f"entrypoint missing {marker}")

    launch=registry.get("launch_contract", {})
    if launch.get("mode") != "LINK_IN_RELAY_OUT":
        errors.append("launch mode mismatch")
    scripts=launch.get("current_scripts", {})
    h2s=scripts.get("OM26-H2", {})
    if h2s.get("assignment_id") != "OM26-H2-WP03" or h2s.get("agent_ref") != "INDEPENDENT-AGENT-009":
        errors.append("H2 launch contract not rebound to WP03")
    for i in range(2,8):
        row=scripts.get(f"OM26-H{i}",{})
        if row.get("executable") is not True or not absolute_https(row.get("task_url")):
            errors.append(f"OM26-H{i}: current immutable task unavailable")
    return errors


def main() -> int:
    errors=validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: OPENMATH job board and machine registry expose H2 WP03 plus peer active leases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

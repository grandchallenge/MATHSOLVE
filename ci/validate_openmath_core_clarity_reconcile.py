#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

try:
    from ci.validate_openmath_cex_job_board import validate as validate_job_board
except ModuleNotFoundError:
    from validate_openmath_cex_job_board import validate as validate_job_board

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
LANES = ROOT / "work_packages/OPENMATH_2026/HILL_LANES.json"
CONTRACT = ROOT / ".gcl/campaigns/OPENMATH-2026/LIFECYCLE_CONTRACT.json"
HILLS = [f"OM26-H{i}" for i in range(1, 8)]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate() -> list[str]:
    errors = list(validate_job_board())
    registry = load(REGISTRY)
    lanes = load(LANES)
    contract = load(CONTRACT)

    if contract.get("status") != "FROZEN":
        errors.append("OPENMATH lifecycle contract is not frozen")
    if contract.get("lifecycle") != [
        "READY","LAUNCHED","RETURNED","CAPTURED","REPLAYED","ADJUDICATED","ADVANCED"
    ]:
        errors.append("OPENMATH lifecycle contract drift")

    lane_rows = {x["hill_slot"]: x for x in lanes.get("hills", [])}
    if set(lane_rows) != set(HILLS):
        errors.append("HILL_LANES roster mismatch")

    assignments = {
        x["assignment_id"]: x
        for x in registry.get("assignments", [])
        if isinstance(x, dict) and x.get("assignment_id")
    }
    policy = registry["mathematics_release_policy"]["per_hill"]
    for hill in HILLS:
        aid = policy[hill]["assignment"]
        item = assignments.get(aid, {})
        lane = lane_rows.get(hill, {})
        active = lane.get("active_lease")
        if item.get("state") == "LEASED_NOT_LAUNCHED":
            if not active:
                errors.append(f"{hill}: no active lane lease")
            else:
                if active.get("assignment_id") != aid:
                    errors.append(f"{hill}: lane/registry assignment drift")
                if active.get("dispatch_id") != item.get("lease", {}).get("dispatch_id"):
                    errors.append(f"{hill}: lane/registry dispatch drift")
                if active.get("agent_ref") != item.get("lease", {}).get("agent_ref"):
                    errors.append(f"{hill}: lane/registry agent drift")
                if active.get("lifecycle_state") != "LEASED_NOT_LAUNCHED":
                    errors.append(f"{hill}: lane lifecycle drift")
        predecessor = policy[hill].get("predecessor")
        if predecessor:
            prev = assignments.get(predecessor.get("assignment"), {})
            if prev.get("state") != "ACCEPTED" or not prev.get("lifecycle", {}).get("closed"):
                errors.append(f"{hill}: protected predecessor not accepted/closed")

    # Durable historical anchors must remain available while current state advances.
    h1 = assignments.get("OM26-H1-H1-12", {})
    if h1.get("state") != "ACCEPTED":
        errors.append("H1 Agent001 accepted history lost")
    wp01 = assignments.get("OM26-H2-WP01", {})
    if wp01.get("state") != "ACCEPTED":
        errors.append("H2 WP01 accepted history lost")
    wp02 = assignments.get("OM26-H2-WP02", {})
    if wp02.get("state") != "ACCEPTED":
        errors.append("H2 WP02 accepted history lost")
    elif wp02.get("lifecycle", {}).get("adjudication") != "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED":
        errors.append("H2 WP02 bounded adjudication drift")

    current = registry.get("current_topology", {})
    if current.get("hills") != HILLS:
        errors.append("current seven-hill topology drift")
    if current.get("grouped_current_lanes") not in (None, []):
        errors.append("deprecated grouped current topology returned")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: OPENMATH Core Clarity follows the state-derived seven-hill lifecycle")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

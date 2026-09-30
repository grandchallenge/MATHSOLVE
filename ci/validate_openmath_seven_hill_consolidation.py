#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from ci.validate_openmath_cex_job_board import validate as validate_job_board

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
LANES = ROOT / "work_packages/OPENMATH_2026/HILL_LANES.json"
HISTORY = ROOT / "work_packages/OPENMATH_2026/HISTORICAL_TRANCHE_REGISTRY.json"
HILLS = [f"OM26-H{i}" for i in range(1, 8)]
DEPRECATED = "H2-H7"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate() -> list[str]:
    errors = list(validate_job_board())
    registry = load(REGISTRY)
    lanes = load(LANES)
    history = load(HISTORY)

    topology = registry.get("current_topology", {})
    if topology.get("lane_model") != "SEVEN_FIRST_CLASS_HILLS":
        errors.append("current lane model drift")
    if topology.get("hills") != HILLS:
        errors.append("current hill roster drift")
    if topology.get("grouped_current_lanes") not in (None, []):
        errors.append("current topology exposes grouped lanes")

    lane_rows = lanes.get("hills", [])
    if [x.get("hill_slot") for x in lane_rows] != HILLS:
        errors.append("HILL_LANES order/roster drift")

    policy = registry.get("mathematics_release_policy", {}).get("per_hill", {})
    if set(policy) != set(HILLS):
        errors.append("release policy is not seven peer hills")

    # Deprecated aggregate syntax may survive only in explicit historical provenance.
    active = {
        "current_topology": topology,
        "release_policy": policy,
        "hills": [
            {
                "hill_slot": row.get("hill_slot"),
                "status": row.get("status"),
                "next_action": row.get("next_action"),
                "active_lease": row.get("active_lease"),
                "competition_state": row.get("competition_state"),
            }
            for row in lane_rows
        ],
    }
    if DEPRECATED in json.dumps(active, sort_keys=True):
        errors.append("deprecated H2-H7 grouping leaked into current operational state")

    if history.get("campaign") != "OPENMATH-2026":
        errors.append("historical tranche registry campaign drift")
    history_text = json.dumps(history, sort_keys=True)
    if DEPRECATED not in history_text:
        errors.append("historical provenance no longer records the deprecated tranche identity")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: OPENMATH current topology remains seven first-class peer hills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

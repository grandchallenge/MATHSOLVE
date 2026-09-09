#!/usr/bin/env python3
"""Fail-closed checks for the staged PNP-BRIDGE-001 package."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "work_packages/PNP_BRIDGE_001/bridge_status.json"
LEAN = ROOT / "MathSolve/PNP/CarrierBridge.lean"

EXPECTED = {
    "PNP-BRIDGE-CARRIER-001": "kernel_checked",
    "PNP-BRIDGE-MODEL-001": "blocked_missing_formal_target",
    "PNP-BRIDGE-POLYBOUND-001": "blocked_missing_formal_target",
    "PNP-BRIDGE-NP-001": "blocked_by_prerequisites",
    "PNP-BRIDGE-ENDPOINT-001": "endpoint_specific_open",
}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        record = json.loads((root / STATUS.relative_to(ROOT)).read_text(encoding="utf-8"))
        lean = (root / LEAN.relative_to(ROOT)).read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        return [f"PNP bridge package load failed: {exc}"]

    if record.get("package_id") != "PNP-BRIDGE-001" or record.get("campaign_id") != "PNP-001":
        errors.append("PNP bridge identity drift")
    if record.get("governance_issue") != "https://github.com/grandchallenge/MATHSOLVE/issues/148":
        errors.append("PNP bridge governance issue drift")

    bridges = record.get("bridges", [])
    by_id = {item.get("bridge_id"): item for item in bridges if isinstance(item, dict)}
    if len(by_id) != len(bridges) or set(by_id) != set(EXPECTED):
        errors.append("PNP bridge coverage drift")
    for bridge_id, status in EXPECTED.items():
        if by_id.get(bridge_id, {}).get("status") != status:
            errors.append(f"{bridge_id}: status drift")

    if record.get("closed_bridge_ids") != ["PNP-BRIDGE-CARRIER-001"]:
        errors.append("only the carrier bridge may be closed")
    if set(record.get("open_bridge_ids", [])) != set(EXPECTED) - {"PNP-BRIDGE-CARRIER-001"}:
        errors.append("PNP open bridge set drift")
    if by_id.get("PNP-BRIDGE-NP-001", {}).get("depends_on") != [
        "PNP-BRIDGE-MODEL-001",
        "PNP-BRIDGE-POLYBOUND-001",
    ]:
        errors.append("NP prerequisite ordering drift")

    for theorem in (
        "theorem languageOf_injective",
        "theorem languageClassOf_eq_iff",
        "theorem languageClassOf_ne_iff",
    ):
        if theorem not in lean:
            errors.append(f"carrier theorem missing: {theorem}")

    if record.get("certification_effect") != "none" or record.get("promotion_eligible") is not False:
        errors.append("PNP bridge package cannot certify or promote")
    boundary = str(record.get("claim_boundary", ""))
    if "does not prove P equals NP" not in boundary or "P differs from NP" not in boundary:
        errors.append("PNP claim boundary is incomplete")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PNP-BRIDGE-001 validated: carrier bridge closed, four obligations open, no certification or promotion effect.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

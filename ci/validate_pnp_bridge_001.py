#!/usr/bin/env python3
"""Fail-closed checks for PNP-BRIDGE-001."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "work_packages/PNP_BRIDGE_001/bridge_status.json"
CARRIER = ROOT / "MathSolve/PNP/CarrierBridge.lean"
POLYBOUND = ROOT / "MathSolve/PNP/PolyBoundBridge.lean"

EXPECTED = {
    "PNP-BRIDGE-CARRIER-001": "kernel_checked",
    "PNP-BRIDGE-MODEL-001": "blocked_missing_formal_target",
    "PNP-BRIDGE-POLYBOUND-001": "kernel_checked",
    "PNP-BRIDGE-NP-001": "blocked_by_prerequisites",
    "PNP-BRIDGE-ENDPOINT-001": "endpoint_specific_open",
}
CLOSED = ["PNP-BRIDGE-CARRIER-001", "PNP-BRIDGE-POLYBOUND-001"]
POLY_THEOREMS = [
    "polynomial_eval_le_eval_one_mul_pow_natDegree",
    "importedPolynomialBound_to_programmePolynomialBound",
    "programmePolynomialBound_to_importedPolynomialBound",
    "importedPolynomialBound_iff_programmePolynomialBound",
]


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        record = json.loads((root / STATUS.relative_to(ROOT)).read_text(encoding="utf-8"))
        carrier = (root / CARRIER.relative_to(ROOT)).read_text(encoding="utf-8")
        poly = (root / POLYBOUND.relative_to(ROOT)).read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        return [f"PNP bridge package load failed: {exc}"]

    if record.get("package_id") != "PNP-BRIDGE-001" or record.get("campaign_id") != "PNP-001":
        errors.append("PNP bridge identity drift")
    if record.get("governance_issue") != "https://github.com/grandchallenge/MATHSOLVE/issues/148":
        errors.append("PNP bridge governance issue drift")

    bridges = record.get("bridges", [])
    by_id = {x.get("bridge_id"): x for x in bridges if isinstance(x, dict)}
    if len(by_id) != len(bridges) or set(by_id) != set(EXPECTED):
        errors.append("PNP bridge coverage drift")
    for bridge_id, status in EXPECTED.items():
        if by_id.get(bridge_id, {}).get("status") != status:
            errors.append(f"{bridge_id}: status drift")
    if record.get("closed_bridge_ids") != CLOSED:
        errors.append("only carrier and polynomial-bound bridges may be closed")
    if set(record.get("open_bridge_ids", [])) != set(EXPECTED) - set(CLOSED):
        errors.append("PNP open bridge set drift")
    if by_id.get("PNP-BRIDGE-NP-001", {}).get("depends_on") != [
        "PNP-BRIDGE-MODEL-001", "PNP-BRIDGE-POLYBOUND-001"
    ]:
        errors.append("NP prerequisite ordering drift")

    for name in ("languageOf_injective", "languageClassOf_eq_iff", "languageClassOf_ne_iff"):
        if f"theorem {name}" not in carrier:
            errors.append(f"carrier theorem missing: {name}")

    compact = " ".join(poly.split())
    required = [
        "abbrev BinaryRuntimeCost := List Bool → Nat",
        "∃ p : Polynomial Nat, ∀ input, cost input ≤ p.eval input.length",
        "∃ constant exponent threshold lowCap : Nat,",
        "∀ input, input.length < threshold → cost input ≤ lowCap",
        "∀ input, threshold ≤ input.length → cost input ≤ constant * input.length ^ exponent",
    ]
    required += [f"theorem {name}" for name in POLY_THEOREMS]
    required += [f"#print axioms {name}" for name in POLY_THEOREMS]
    for snippet in required:
        if snippet not in compact:
            errors.append(f"polynomial-bound contract/theorem drift: {snippet}")

    for forbidden in (
        "sorry", "admit", "Polynomial Int", "Polynomial ℤ", "TM2Runtime",
        "TM2Computable", "importedPEqProgrammeP", "importedNPEqProgrammeNP",
    ):
        if forbidden in poly:
            errors.append(f"forbidden polynomial-bound inflation/placeholder: {forbidden}")

    poly_status = by_id.get("PNP-BRIDGE-POLYBOUND-001", {})
    if poly_status.get("artifact") != "MathSolve/PNP/PolyBoundBridge.lean":
        errors.append("polynomial-bound artifact identity drift")
    if poly_status.get("theorems") != [f"MathSolve.PNP.{name}" for name in POLY_THEOREMS]:
        errors.append("polynomial-bound theorem identity drift")

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
    print("PNP-BRIDGE-001 validated: carrier and polynomial-bound bridges closed; three obligations remain open.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

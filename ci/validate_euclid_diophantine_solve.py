#!/usr/bin/env python3
"""Fail-closed validator for the EUCLID-DIOPHANTINE-E2E-002 Solve package."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE_PATH = ROOT / "certificates" / "EUCLID-DIOPHANTINE-E2E-002.json"
SCHEMA_PATH = ROOT / "schemas" / "euclid_diophantine_candidate.schema.json"
SOLVER_PATH = ROOT / "solve" / "euclid_diophantine.py"

EXPECTED = {
    "forge_commit": "af5398a05f17789a061ab0d23c2b47f0cc952fff",
    "forge_package": "e89d5b7c611aaa4a7fdea716742e993eaa283da1",
    "forge_manifest": "de9dae12cd578ee98b58e6fc1b39365f8c1e7109",
    "stage1_solve_commit": "3a8493aa322f0e640c921b8824c4d7f88a8c057d",
    "stage1_candidate": "af54ae9b9a047a36767b2599ebc649fb6fdaaa52",
    "stage1_cert_commit": "78b69e6a3461a83f4893d61c421b1570c08a9ba6",
    "stage1_cert_output": "36c62434dbd19719d990e71ddc23729f0614ace7",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_solver():
    spec = importlib.util.spec_from_file_location("euclid_diophantine", SOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load deterministic producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def semantic_errors(candidate: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(candidate, dict):
        return ["candidate must be an object"]

    forge = candidate.get("forge_input", {})
    if forge.get("commit_sha") != EXPECTED["forge_commit"]:
        errors.append("protected Forge merge identity drifted")
    if forge.get("package", {}).get("digest") != EXPECTED["forge_package"]:
        errors.append("Forge package identity drifted")
    if forge.get("provider_manifest", {}).get("digest") != EXPECTED["forge_manifest"]:
        errors.append("Forge provider-manifest identity drifted")

    stage1 = candidate.get("protected_stage1", {})
    if stage1.get("solve_merge_commit") != EXPECTED["stage1_solve_commit"]:
        errors.append("protected Stage 1 Solve merge drifted")
    if stage1.get("solve_candidate", {}).get("digest") != EXPECTED["stage1_candidate"]:
        errors.append("protected Stage 1 candidate identity drifted")
    if stage1.get("cert_merge_commit") != EXPECTED["stage1_cert_commit"]:
        errors.append("protected Stage 1 Cert merge drifted")
    if stage1.get("certification_output", {}).get("digest") != EXPECTED["stage1_cert_output"]:
        errors.append("protected Stage 1 certification output identity drifted")
    if stage1.get("normalized_gcd") != 21 or stage1.get("positive_bezout") != {"x": -2, "y": 5}:
        errors.append("protected gcd or Bezout values drifted")

    cases = candidate.get("cases", [])
    by_id = {item.get("case_id"): item for item in cases if isinstance(item, dict)}
    if set(by_id) != {"DIO-POS-252-105-84", "DIO-NEG-252-105-20"}:
        errors.append("canonical case set drifted")
        return errors

    positive = by_id["DIO-POS-252-105-84"]
    if positive.get("inputs") != {"a": 252, "b": 105, "c": 84}:
        errors.append("positive inputs drifted")
    if positive.get("evidence_type") != "constructive_solution":
        errors.append("positive case must be constructive")
    solution = positive.get("constructive_solution")
    if not isinstance(solution, dict):
        errors.append("positive constructive solution is missing")
    else:
        if solution.get("base_bezout") != {"x": -2, "y": 5, "equation_value": 21}:
            errors.append("positive protected Bezout reference drifted")
        if solution.get("scale_factor") != 4:
            errors.append("positive scale factor drifted")
        if (solution.get("x"), solution.get("y"), solution.get("equation_value")) != (-8, 20, 84):
            errors.append("positive candidate witness drifted")
        if solution.get("x") * 252 + solution.get("y") * 105 != 84:
            errors.append("positive candidate equation is false")
        if solution.get("x") != 4 * -2 or solution.get("y") != 4 * 5:
            errors.append("positive witness is not the recorded protected scaling")
    if positive.get("divisibility_obstruction") is not None:
        errors.append("positive case cannot carry an obstruction")

    negative = by_id["DIO-NEG-252-105-20"]
    if negative.get("inputs") != {"a": 252, "b": 105, "c": 20}:
        errors.append("negative inputs drifted")
    if negative.get("evidence_type") != "divisibility_obstruction":
        errors.append("negative case must carry an obstruction")
    obstruction = negative.get("divisibility_obstruction")
    if not isinstance(obstruction, dict):
        errors.append("negative obstruction is missing")
    else:
        q, r = obstruction.get("quotient"), obstruction.get("remainder")
        if not isinstance(q, int) or not isinstance(r, int) or 20 != q * 21 + r:
            errors.append("negative quotient-remainder equation is false")
        if not isinstance(r, int) or not 0 < r < 21:
            errors.append("negative remainder must satisfy 0 < r < 21")
        if obstruction.get("absolute_target") != 20 or obstruction.get("equation_value") != 20:
            errors.append("negative absolute-target record drifted")
        if obstruction.get("strict_nonzero_remainder") is not True:
            errors.append("negative obstruction must record a strict nonzero remainder")
    if negative.get("constructive_solution") is not None:
        errors.append("negative case cannot carry a constructive witness")

    solver = candidate.get("solver", {})
    for field in ("network_used", "randomness_used", "timeout_or_failed_search_used_as_unsat", "recomputes_gcd"):
        if solver.get(field) is not False:
            errors.append(f"solver boundary {field} must remain false")

    scope = candidate.get("candidate_scope", {})
    if scope.get("arbitrary_diophantine_completeness_claimed") is not False:
        errors.append("bounded producer cannot claim arbitrary Diophantine completeness")

    boundary = candidate.get("claim_boundary", {})
    for field in (
        "constructive_witness_accepted",
        "unsatisfiable_obstruction_accepted",
        "theorem_certified",
        "arbitrary_diophantine_completeness_claimed",
        "novelty_claimed",
        "priority_claimed",
        "historical_verbatim_equivalence_claimed",
    ):
        if boundary.get(field) is not False:
            errors.append(f"claim boundary {field} must remain false")

    return errors


def validate_candidate(candidate: Any, schema: Any) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(candidate), key=lambda item: list(item.path))
    ]
    errors.extend(semantic_errors(candidate))
    return errors


def main() -> int:
    candidate = load_json(CERTIFICATE_PATH)
    errors = validate_candidate(candidate, load_json(SCHEMA_PATH))
    if not errors:
        produced = load_solver().build_candidate()
        if produced != candidate:
            errors.append("committed candidate is not the deterministic producer output")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"EUCLID-DIOPHANTINE-E2E-002 Solve validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("EUCLID-DIOPHANTINE-E2E-002 deterministic constructive and obstruction candidates are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate deterministic EUCLID-GCD-E2E-001 Solve evidence."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "certificates" / "EUCLID-GCD-E2E-001.json"
SCHEMA_PATH = ROOT / "schemas" / "euclid_gcd_candidate.schema.json"
SOLVER_PATH = ROOT / "solve" / "euclid_gcd.py"

EXPECTED_FORGE_COMMIT = "3622bac82a39cdb9e82ec463919d9e6927c1ec0e"
EXPECTED_PACKAGE_BLOB = "079b68fb5651e0d2eee0a7b2002454d34673d84c"
EXPECTED_MANIFEST_BLOB = "a103b2c85dbd67973da43656fed5af567c5b7074"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_solver():
    spec = importlib.util.spec_from_file_location("euclid_gcd_solver", SOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def semantic_errors(candidate: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(candidate, dict):
        return ["candidate must be an object"]
    forge = candidate.get("forge_input", {})
    if forge.get("commit_sha") != EXPECTED_FORGE_COMMIT:
        errors.append("protected Forge commit drift")
    if forge.get("package", {}).get("digest") != EXPECTED_PACKAGE_BLOB:
        errors.append("Forge package Git blob drift")
    if forge.get("provider_manifest", {}).get("digest") != EXPECTED_MANIFEST_BLOB:
        errors.append("Forge provider manifest Git blob drift")

    inputs = candidate.get("inputs", {})
    a, b = inputs.get("a"), inputs.get("b")
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        errors.append("inputs must be natural numbers")
        return errors
    if a == 0 and b == 0:
        errors.append("(0,0) is excluded")

    trace = candidate.get("euclidean_trace", [])
    if not isinstance(trace, list) or not trace:
        errors.append("trace must be nonempty")
        return errors
    current_a, current_b = a, b
    last_positive = None
    for index, step in enumerate(trace):
        if not isinstance(step, dict):
            errors.append(f"trace step {index} is not an object")
            continue
        dividend, divisor = step.get("dividend"), step.get("divisor")
        quotient, remainder = step.get("quotient"), step.get("remainder")
        if (dividend, divisor) != (current_a, current_b):
            errors.append(f"trace step {index} linkage failure")
        if not all(isinstance(v, int) for v in (dividend, divisor, quotient, remainder)):
            errors.append(f"trace step {index} fields must be integers")
            continue
        if divisor <= 0:
            errors.append(f"trace step {index} divisor must be positive")
            continue
        if dividend != quotient * divisor + remainder:
            errors.append(f"trace step {index} equation failure")
        if remainder < 0 or remainder >= divisor:
            errors.append(f"trace step {index} remainder bound failure")
        last_positive = divisor
        current_a, current_b = divisor, remainder
        if remainder == 0 and index != len(trace) - 1:
            errors.append("trace continues after terminal zero")
    if trace[-1].get("remainder") != 0:
        errors.append("trace does not terminate in zero")
    d = candidate.get("result", {}).get("d")
    if not isinstance(d, int) or d <= 0:
        errors.append("reported d must be positive")
    if d != last_positive:
        errors.append("reported d is not terminal positive divisor")
    if isinstance(d, int) and d > 0 and (a % d != 0 or b % d != 0):
        errors.append("reported d does not divide both inputs")

    witness = candidate.get("bezout_witness", {})
    x, y, equation = witness.get("x"), witness.get("y"), witness.get("equation_value")
    if not isinstance(x, int) or not isinstance(y, int):
        errors.append("Bézout coefficients must be integers")
    elif x * a + y * b != d or equation != d:
        errors.append("Bézout equality failure")

    solver = load_solver()
    regenerated = solver.build_candidate(a, b)
    if regenerated != candidate:
        errors.append("committed candidate does not equal deterministic solver replay")

    if candidate.get("authority_state") != "candidate_only":
        errors.append("Solve evidence must remain candidate_only")
    boundary = candidate.get("claim_boundary", {})
    for field in ("certificate_accepted", "theorem_certified", "novelty_claimed", "priority_claimed", "historical_verbatim_equivalence_claimed"):
        if boundary.get(field) is not False:
            errors.append(f"claim boundary {field} must remain false")
    return errors


def validate_candidate(candidate: Any, schema: Any) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [f"{error.json_path}: {error.message}" for error in sorted(validator.iter_errors(candidate), key=lambda item: list(item.path))]
    errors.extend(semantic_errors(candidate))
    return errors


def main() -> int:
    candidate = load_json(CERT_PATH)
    schema = load_json(SCHEMA_PATH)
    errors = validate_candidate(candidate, schema)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"EUCLID-GCD-E2E-001 Solve validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("EUCLID-GCD-E2E-001 deterministic candidate, Forge binding, arithmetic trace, and authority boundary are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

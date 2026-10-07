#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

try:
    from ci.erdos_open_cohort_closure import PROBLEMS, ROOT, validate_closure
except ModuleNotFoundError:
    from erdos_open_cohort_closure import PROBLEMS, ROOT, validate_closure

BASE = ROOT / "contributions" / "ERDOS-OPEN-001" / "RECON_TRANCHE_001"
ADJUDICATIONS = BASE / "adjudications"
CLOSURES = BASE / "closures"


def validate() -> list[str]:
    errors: list[str] = []
    if not ADJUDICATIONS.exists():
        return errors

    for path in sorted(ADJUDICATIONS.glob("*.json")):
        try:
            adjudication = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append(f"{path.name}: invalid adjudication JSON")
            continue

        problem_raw = adjudication.get("problem_id")
        problem = str(problem_raw) if isinstance(problem_raw, (int, str)) else ""
        if problem not in PROBLEMS:
            errors.append(f"{path.name}: unregistered ERDOS problem_id")
            continue

        closure_path = CLOSURES / f"ERDOS-{problem}-BLIND-COHORT-001.json"
        if not closure_path.is_file():
            errors.append(
                f"{path.name}: adjudication has no protected cohort closure"
            )
            continue

        try:
            closure = json.loads(closure_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append(f"{path.name}: protected closure JSON is invalid")
            continue

        closure_errors = validate_closure(problem, closure)
        errors.extend(
            f"{path.name}: closure gate: {message}"
            for message in closure_errors
        )
        if closure.get("synthesis_allowed") is not True:
            errors.append(f"{path.name}: closure does not allow synthesis")
        if closure.get("semantic_gate_required", False):
            if closure.get("semantic_gate_satisfied_at_closure") is not True:
                errors.append(f"{path.name}: semantic source gate is not satisfied")
            if closure.get("semantic_source_audit_obligation_discharged") is not True:
                errors.append(
                    f"{path.name}: semantic source-audit obligation is not discharged"
                )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    count = len(list(ADJUDICATIONS.glob("*.json"))) if ADJUDICATIONS.exists() else 0
    print(
        "PASS: ERDOS adjudications are downstream of satisfied protected closure "
        f"and semantic source gates ({count} adjudication record(s))"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

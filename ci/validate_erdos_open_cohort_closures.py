#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

try:
    from ci.erdos_open_cohort_closure import PROBLEMS, ROOT, validate_closure
except ModuleNotFoundError:
    from erdos_open_cohort_closure import PROBLEMS, ROOT, validate_closure

BASE = ROOT / "contributions" / "ERDOS-OPEN-001" / "RECON_TRANCHE_001"
CLOSURES = BASE / "closures"


def validate() -> list[str]:
    errors: list[str] = []
    if not CLOSURES.exists():
        return errors
    expected_names = {f"ERDOS-{p}-BLIND-COHORT-001.json" for p in PROBLEMS}
    for path in sorted(CLOSURES.glob("*.json")):
        if path.name not in expected_names:
            errors.append(f"unexpected ERDOS closure file: {path.name}")
            continue
        problem = path.name.split("-")[1]
        try:
            closure = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append(f"{path.name}: invalid JSON")
            continue
        for error in validate_closure(problem, closure):
            errors.append(f"ERDOS-{problem}: {error}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    count = len(list(CLOSURES.glob("*.json"))) if CLOSURES.exists() else 0
    print(f"PASS: ERDOS cohort closure overlays valid ({count} protected closure record(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

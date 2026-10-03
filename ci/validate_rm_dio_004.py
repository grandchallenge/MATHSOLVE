#!/usr/bin/env python3
"""Validate the RM-DIO-004 bounded exact screen and intake binding."""
from __future__ import annotations
import json
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "domains" / "researchmath" / "RM-DIO-004"
EXPECTED_FORGE_COMMIT = "bab7ae57f54601b49ad9fc870051095ad487c64a"
EXPECTED_DATASET_COMMIT = "f22d0f28b55e6e777acf82e722d97ae982dff02e"
EXPECTED_LFS_SHA256 = "3f6c96d18925a47ac223555717226c5408cc9c75e07a1e96bddcffde8a06f029"
EXPECTED_QUESTION_SHA256 = "9211447a6d6e4187668551a896ad9ce1750519d7d3952fb461fdaadffb324491"
EXPECTED_MIN = -1_000_000
EXPECTED_MAX = 1_000_000

def enumerate_solutions(lower: int, upper: int) -> list[list[int]]:
    solutions: set[tuple[int, int]] = set()
    for y in range(lower, upper + 1):
        discriminant = 1 + 4 * (y**5 - y)
        if discriminant < 0:
            continue
        root = isqrt(discriminant)
        if root * root != discriminant:
            continue
        for signed_root in {root, -root}:
            numerator = 1 + signed_root
            if numerator % 2 == 0:
                x = numerator // 2
                if x * x - x == y**5 - y:
                    solutions.add((x, y))
    return [list(pair) for pair in sorted(solutions)]

def validation_errors(binding: dict, screen: dict, handoff: dict) -> list[str]:
    forge, dataset, domain = binding.get("mathforge", {}), binding.get("dataset", {}), screen.get("domain", {})
    checks = {
        "wrong source id": binding.get("source_id") == "RM-AMPHORA-001",
        "wrong fixture id": binding.get("fixture_id") == "RM-DIO-004",
        "MATHFORGE protected commit drift": forge.get("protected_commit") == EXPECTED_FORGE_COMMIT,
        "dataset commit drift": dataset.get("commit") == EXPECTED_DATASET_COMMIT,
        "dataset LFS identity drift": dataset.get("git_lfs_sha256") == EXPECTED_LFS_SHA256,
        "question identity drift": dataset.get("question_sha256") == EXPECTED_QUESTION_SHA256,
        "lower bound drift": domain.get("minimum") == EXPECTED_MIN,
        "upper bound drift": domain.get("maximum") == EXPECTED_MAX,
        "domain must be inclusive": domain.get("inclusive") is True,
        "solution count drift": screen.get("solution_count") == len(screen.get("solutions", [])),
        "handoff level inflation": handoff.get("requested_level") == 2,
    }
    errors = [message for message, ok in checks.items() if not ok]
    if "does not prove" not in screen.get("claim_boundary", ""):
        errors.append("bounded claim boundary missing")
    if len(handoff.get("excluded_claims", [])) < 3:
        errors.append("handoff exclusions missing")
    if not errors and screen.get("solutions") != enumerate_solutions(EXPECTED_MIN, EXPECTED_MAX):
        errors.append("recorded solution list differs from exact replay")
    return errors

def load_package() -> tuple[dict, dict, dict]:
    values = [json.loads((PACKAGE / name).read_text(encoding="utf-8")) for name in ("source_binding.json", "exact_screen.json", "mathcert_handoff.json")]
    return values[0], values[1], values[2]

def main() -> int:
    errors = validation_errors(*load_package())
    if errors:
        print("\n".join(errors))
        return 1
    print("RM-DIO-004 exact screen validated for -1000000 <= y <= 1000000; global completeness remains withheld")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

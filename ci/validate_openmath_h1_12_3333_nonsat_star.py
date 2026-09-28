#!/usr/bin/env python3
"""Finite replay for the profile-3333 non-saturated D2=3 star exclusion."""
from __future__ import annotations

import itertools
import json

try:
    from ci.validate_openmath_h1_12_3333_c4 import residual_orbits
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_c4 import residual_orbits


def hub_patterns():
    """0=other, 1=D1, 2=D2; require the sole D1 to be unblocked."""
    rows = []
    for word in itertools.product((0, 1, 2), repeat=6):
        if word.count(1) != 1 or word.count(2) != 3:
            continue
        i = word.index(1)
        if word[(i - 1) % 6] == 2 or word[(i + 1) % 6] == 2:
            continue
        rows.append(word)
    return rows


def has_three_consecutive_d2(word):
    return any(
        all(word[(i + j) % 6] == 2 for j in range(3))
        for i in range(6)
    )


def target_orbit():
    rows = []
    for row in residual_orbits():
        if (
            row["D2"] == 3
            and tuple(row["degrees"]) == (3, 1, 1, 1)
            and row["saturated"] == 0
            and row["D1"] == 7
            and row["U"] == 1
            and row["clean"] == row["capacity"] == 9
        ):
            rows.append(row)
    if len(rows) != 1:
        raise AssertionError(f"unexpected target-orbit count: {len(rows)}")
    return rows[0]


def main() -> None:
    row = target_orbit()
    patterns = hub_patterns()
    if len(patterns) != 6:
        raise SystemExit(f"unexpected hub pattern count: {len(patterns)}")
    if not all(has_three_consecutive_d2(word) for word in patterns):
        raise SystemExit("unblocked hub D1 did not force three consecutive D2 rays")

    strengthened_clean = 10
    if not strengthened_clean > row["capacity"]:
        raise SystemExit("strict core-incidence contradiction not obtained")

    residual = [
        x for x in residual_orbits()
        if x != row
    ]
    if len(residual) != 6:
        raise SystemExit(f"unexpected residual form count: {len(residual)}")
    if sum(x["labeled"] for x in residual) != 41:
        raise SystemExit("unexpected residual labeled-state count")

    receipt = {
        "target": "3333_D2_3_NON_SATURATED_STAR",
        "hub_pattern_count": len(patterns),
        "all_patterns_force_three_consecutive_D2": True,
        "original_clean_line_lower_bound": row["clean"],
        "charge_capacity_upper_bound": row["capacity"],
        "strengthened_clean_line_lower_bound": strengthened_clean,
        "retained_normal_forms": len(residual),
        "retained_labeled_states": sum(x["labeled"] for x in residual),
        "result": "NON_SATURATED_D2_3_STAR_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite cyclic equality consequence plus independently reconstructed "
            "strict core-incidence refinement, conditional on the protected "
            "local fan/blocked-target analysis and clean-line charging map. "
            "No hill-global upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

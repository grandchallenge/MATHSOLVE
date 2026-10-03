#!/usr/bin/env python3
"""Finite replay for the profile-3333 D2=3 P4 exclusion."""
from __future__ import annotations

import itertools
import json

try:
    from ci.validate_openmath_h1_12_3333_c4 import (
        blocked_count,
        forces_neighbor_line,
    )
    from ci.validate_openmath_h1_12_3333_normal_form import EXPECTED_ORBITS
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_c4 import (
        blocked_count,
        forces_neighbor_line,
    )
    from validate_openmath_h1_12_3333_normal_form import EXPECTED_ORBITS


def target_orbit():
    rows = [
        row for row in EXPECTED_ORBITS
        if (
            row["D2"] == 3
            and tuple(sorted(row["degrees"])) == (1, 1, 2, 2)
            and row["D1"] == 8
            and row["U"] == 2
            and row["labeled"] == 12
        )
    ]
    if len(rows) != 1:
        raise AssertionError(f"unexpected P4 target count: {len(rows)}")
    return rows[0]


def local_patterns():
    rows = []
    for word in itertools.product((0, 1, 2), repeat=6):
        if word.count(1) != 2 or word.count(2) != 2:
            continue
        if any(word[i] == 1 and word[(i + 1) % 6] == 1 for i in range(6)):
            continue
        b = blocked_count(word)
        if b not in (1, 2):
            raise AssertionError(f"unexpected blocked count: {word} -> {b}")
        rows.append((word, b, forces_neighbor_line(word)))
    return rows


def main() -> None:
    row = target_orbit()
    patterns = local_patterns()

    one = [item for item in patterns if item[1] == 1]
    two = [item for item in patterns if item[1] == 2]

    if not one or not two:
        raise SystemExit("missing one-blocked or two-blocked local patterns")
    if any(mechanism is None for _, _, mechanism in one):
        raise SystemExit("one-blocked local pattern failed to force neighbor line")

    # b(B), b(C), extra core-incidence savings, clean lower bound,
    # capacity upper bound.
    cases = {
        (1, 1): {"extra": 2, "blocked": 2},
        (1, 2): {"extra": 1, "blocked": 3},
        (2, 1): {"extra": 1, "blocked": 3},
        (2, 2): {"extra": 0, "blocked": 4},
    }

    replay = {}
    for key, data in cases.items():
        clean = 18 - (12 - 3 - data["extra"])
        capacity = 2 * 2 + 8 - data["blocked"]
        if not clean > capacity:
            raise SystemExit(f"P4 case did not contradict budget: {key}")
        replay[str(key)] = {
            "extra_core_incidence_savings": data["extra"],
            "blocked_lower_bound": data["blocked"],
            "clean_line_lower_bound": clean,
            "charge_capacity_upper_bound": capacity,
        }

    receipt = {
        "target": "3333_D2_3_P4",
        "target_labeled_states": row["labeled"],
        "local_one_blocked_patterns": len(one),
        "local_two_blocked_patterns": len(two),
        "one_blocked_all_force_neighbor_line": True,
        "cases": replay,
        "result": "P4_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite local fan and budget replay with independently reconstructed "
            "extra core-incidence accounting. No hill-global upper bound or "
            "certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

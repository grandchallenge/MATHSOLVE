#!/usr/bin/env python3
"""Replay the profile-3333 D2=3 non-saturated star exclusion."""
from __future__ import annotations

import itertools
import json

try:
    from ci.validate_openmath_h1_12_3333_c4 import residual_orbits
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_c4 import residual_orbits


def blocked_count(word):
    n = len(word)
    return sum(
        value == 1
        and (word[(i - 1) % n] == 2 or word[(i + 1) % n] == 2)
        for i, value in enumerate(word)
    )


def hub_equality_patterns():
    out = []
    for word in itertools.product((0, 1, 2), repeat=6):
        if word.count(1) != 1 or word.count(2) != 3:
            continue
        if blocked_count(word) != 0:
            continue
        out.append(word)
    return out


def has_three_consecutive_d2(word):
    n = len(word)
    return any(
        all(word[(i + j) % n] == 2 for j in range(3))
        for i in range(n)
    )


def remaining_orbits():
    out = []
    for row in residual_orbits():
        is_target = (
            row["D2"] == 3
            and tuple(row["degrees"]) == (3, 1, 1, 1)
            and tuple(row["d1"]) == (1, 2, 2, 2)
            and row["saturated"] == 0
        )
        if not is_target:
            out.append(row)
    return out


def main() -> None:
    source = residual_orbits()
    target = [
        row for row in source
        if row["D2"] == 3
        and tuple(row["degrees"]) == (3, 1, 1, 1)
        and tuple(row["d1"]) == (1, 2, 2, 2)
        and row["saturated"] == 0
    ]
    if len(target) != 1:
        raise SystemExit(f"unexpected target count: {len(target)}")
    row = target[0]
    if (row["clean"], row["capacity"], row["blocked"]) != (9, 9, 0):
        raise SystemExit(f"unexpected star equality tuple: {row}")

    patterns = hub_equality_patterns()
    if len(patterns) != 6:
        raise SystemExit(f"unexpected hub pattern count: {len(patterns)}")
    if not all(has_three_consecutive_d2(word) for word in patterns):
        raise SystemExit("zero-block hub pattern without a three-D2 run")

    strengthened_clean = 11
    if not strengthened_clean > row["capacity"]:
        raise SystemExit("star incidence contradiction not obtained")

    rows = remaining_orbits()
    if len(rows) != 6:
        raise SystemExit(f"unexpected residual orbit count: {len(rows)}")
    if sum(x["labeled"] for x in rows) != 41:
        raise SystemExit("unexpected residual labeled-state count")

    receipt = {
        "hub_equality_pattern_count": len(patterns),
        "forced_extra_core_incidence_savings": 2,
        "strengthened_h_upper_bound": 7,
        "strengthened_clean_line_lower_bound": strengthened_clean,
        "charge_capacity_upper_bound": row["capacity"],
        "retained_normal_forms": len(rows),
        "retained_labeled_states": sum(x["labeled"] for x in rows),
        "result": "D2_3_NONSATURATED_STAR_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite hub equality classification and independently "
            "reconstructed incidence refinement using the protected "
            "clean-line charging map. No hill-global upper bound or "
            "certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

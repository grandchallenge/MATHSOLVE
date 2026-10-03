#!/usr/bin/env python3
"""Finite replay for the OM26-H1 H1-12 profile-3334 D2=4 reduction."""
from __future__ import annotations

import itertools
import json


N = 18
I = 13
D2 = 4


def cyclic_symbol_patterns(length, d1_count, d2_count, forbidden_d1_run):
    """Enumerate cyclic words: 1=D1, 2=D2, 0=other."""
    out = []
    symbols = [1] * d1_count + [2] * d2_count + [0] * (
        length - d1_count - d2_count
    )
    for word in set(itertools.permutations(symbols)):
        if any(
            all(word[(i + j) % length] == 1 for j in range(forbidden_d1_run))
            for i in range(length)
        ):
            continue
        out.append(word)
    return out


def d1_touching_d2(word):
    n = len(word)
    return sum(
        value == 1
        and (word[(i - 1) % n] == 2 or word[(i + 1) % n] == 2)
        for i, value in enumerate(word)
    )


def min_touching(length, d1_count, d2_count, forbidden_d1_run):
    rows = cyclic_symbol_patterns(
        length, d1_count, d2_count, forbidden_d1_run
    )
    return min(d1_touching_d2(row) for row in rows), len(rows)


def main() -> None:
    triple_min, triple_patterns = min_touching(6, 2, 2, 2)
    quad_min, quad_patterns = min_touching(8, 4, 2, 3)
    if triple_min != 1:
        raise SystemExit(f"unexpected triple-core minimum: {triple_min}")
    if quad_min != 1:
        raise SystemExit(f"unexpected quadruple-core minimum: {quad_min}")

    # Four-cycle: four cores each lose at least one D1 target.
    cycle_clean = N - (I - D2)
    cycle_capacity = 10 - 4
    if not cycle_clean > cycle_capacity:
        raise SystemExit("four-cycle charge contradiction not obtained")

    # Saturated Q hub loses five D1 targets.
    q_capacities = {
        "10,0": (10 - 5) + 2 * 0,
        "11,1": (11 - 5) + 2 * 1,
    }
    if not all(cycle_clean > cap for cap in q_capacities.values()):
        raise SystemExit("Q-hub charge contradiction not obtained")

    # Saturated T hub forces all three leaf-pair lines, so h<=8.
    t_clean = N - (I - 5)
    t_capacity_u0 = (10 - 3) + 2 * 0
    # In the U=1 state an outer-edge triple leaf loses another D1 target.
    t_capacity_u1 = (11 - 4) + 2 * 1
    if not t_clean > t_capacity_u0:
        raise SystemExit("T-hub U=0 charge contradiction not obtained")
    if not t_clean > t_capacity_u1:
        raise SystemExit("T-hub U=1 charge contradiction not obtained")

    receipt = {
        "profile": [3, 3, 3, 4],
        "D2": D2,
        "local_cyclic_minimums": {
            "triple_d1_2_d2_2": {
                "minimum_D1_touching_D2": triple_min,
                "pattern_count": triple_patterns,
            },
            "quadruple_d1_4_d2_2": {
                "minimum_D1_touching_D2": quad_min,
                "pattern_count": quad_patterns,
            },
        },
        "cycle": {
            "clean_line_lower_bound": cycle_clean,
            "available_charge_capacity_upper_bound": cycle_capacity,
        },
        "Q_hub": {
            "clean_line_lower_bound": cycle_clean,
            "capacity_by_D1_U": q_capacities,
        },
        "T_hub": {
            "clean_line_lower_bound": t_clean,
            "capacity_D1_10_U_0": t_capacity_u0,
            "capacity_D1_11_U_1": t_capacity_u1,
        },
        "result": "D2=4_ROLE_TYPES_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite cyclic and capacity consequence of the named local fan "
            "and clean-line charging premises; no hill-global upper bound "
            "or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

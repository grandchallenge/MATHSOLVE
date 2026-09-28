#!/usr/bin/env python3
"""Finite replay for the OM26-H1 H1-12 profile-3334 D2=5 reduction."""
from __future__ import annotations

import itertools
import json


N = 18
I = 13
D1 = 10
D2 = 5
U = 1


def cyclic_patterns(length: int, d1_count: int, forbidden_run: int):
    out = []
    for bits in itertools.product((0, 1), repeat=length):
        # 1=D1, 0=D2 for saturated hubs in this tranche.
        if sum(bits) != d1_count:
            continue
        if any(
            all(bits[(i + j) % length] == 1 for j in range(forbidden_run))
            for i in range(length)
        ):
            continue
        out.append(bits)
    return out


def every_d1_touches_d2(bits):
    n = len(bits)
    return all(
        bit == 0 or bits[(i - 1) % n] == 0 or bits[(i + 1) % n] == 0
        for i, bit in enumerate(bits)
    )


def main() -> None:
    triple = cyclic_patterns(6, 3, 2)
    quad = cyclic_patterns(8, 5, 3)

    if set(triple) != {
        (0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0),
    }:
        raise SystemExit(f"unexpected triple-hub patterns: {triple}")
    if not all(every_d1_touches_d2(row) for row in triple):
        raise SystemExit("triple-hub D1 without adjacent D2")

    if len(quad) != 8:
        raise SystemExit(f"unexpected quadruple-hub pattern count: {len(quad)}")
    if not all(every_d1_touches_d2(row) for row in quad):
        raise SystemExit("quadruple-hub D1 without adjacent D2")

    clean_lower = N - (I - D2)
    t_capacity = (D1 - 3) + 2 * U
    q_capacity = (D1 - 5) + 2 * U

    if (clean_lower, t_capacity, q_capacity) != (10, 9, 7):
        raise SystemExit(
            "unexpected D2=5 capacity tuple: "
            f"{clean_lower,t_capacity,q_capacity}"
        )
    if not clean_lower > t_capacity:
        raise SystemExit("triple-hub contradiction not obtained")
    if not clean_lower > q_capacity:
        raise SystemExit("quadruple-hub contradiction not obtained")

    receipt = {
        "profile": [3, 3, 3, 4],
        "D2": D2,
        "D1": D1,
        "U": U,
        "clean_line_lower_bound": clean_lower,
        "triple_hub_available_capacity_upper_bound": t_capacity,
        "quadruple_hub_available_capacity_upper_bound": q_capacity,
        "result": "PROFILE_3334_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite cyclic and charge-capacity consequence of the named local "
            "fan and clean-line charging premises; no hill-global upper bound "
            "or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

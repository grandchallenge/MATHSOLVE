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


def binary_patterns(length: int, d1_count: int, forbidden_run: int):
    out = []
    for bits in itertools.product((0, 1), repeat=length):
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
        bit == 0
        or bits[(i - 1) % n] == 0
        or bits[(i + 1) % n] == 0
        for i, bit in enumerate(bits)
    )


def main() -> None:
    triple = binary_patterns(6, 3, 2)
    quad = binary_patterns(8, 5, 3)

    expected_triple = {
        (0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0),
    }
    if set(triple) != expected_triple:
        raise SystemExit(f"unexpected triple-hub patterns: {triple}")
    if len(quad) != 8:
        raise SystemExit(f"unexpected quadruple-hub pattern count: {len(quad)}")
    if not all(every_d1_touches_d2(bits) for bits in quad):
        raise SystemExit("quadruple-hub D1 ray without adjacent D2 spoke")

    clean_lower = N - (I - D2)
    if clean_lower != 10:
        raise SystemExit(f"unexpected clean-line lower bound: {clean_lower}")

    triple_capacity = (D1 - 3) + 2 * U
    quad_capacity = (D1 - 5) + 2 * U

    if not clean_lower > triple_capacity:
        raise SystemExit("triple-hub charge contradiction not obtained")
    if not clean_lower > quad_capacity:
        raise SystemExit("quadruple-hub charge contradiction not obtained")

    receipt = {
        "profile": [3, 3, 3, 4],
        "D2": D2,
        "D1": D1,
        "U": U,
        "clean_line_lower_bound": clean_lower,
        "triple_hub": {
            "cyclic_pattern_count": len(triple),
            "available_charge_capacity_upper_bound": triple_capacity,
        },
        "quadruple_hub": {
            "cyclic_pattern_count": len(quad),
            "available_charge_capacity_upper_bound": quad_capacity,
        },
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

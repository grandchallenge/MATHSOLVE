#!/usr/bin/env python3
"""Finite replay for the OM26-H1 H1-12 profile-3334 D2=3 reduction.

This checks the cyclic ray consequences and charge-capacity arithmetic used in
the companion proof note. The local no-long-run fan premise and clean-line
charging map remain explicitly source-scoped.
"""
from __future__ import annotations

import itertools
import json


N = 18
I = 13
D1 = 11
D2 = 3
U = 0


def cyclic_patterns(length: int, d1_count: int, forbidden_run: int):
    out = []
    for bits in itertools.product((0, 1), repeat=length):
        # 1 = D1 ray, 0 = D2 ray.
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


def every_d1_between_two_d2(bits):
    n = len(bits)
    return all(
        bit == 0
        or (bits[(i - 1) % n] == 0 and bits[(i + 1) % n] == 0)
        for i, bit in enumerate(bits)
    )


def main() -> None:
    triple = cyclic_patterns(length=6, d1_count=3, forbidden_run=2)
    quad = cyclic_patterns(length=8, d1_count=5, forbidden_run=3)

    expected_triple = {
        (0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0),
    }
    if set(triple) != expected_triple:
        raise SystemExit(f"unexpected triple-hub patterns: {triple}")
    if not all(every_d1_between_two_d2(bits) for bits in triple):
        raise SystemExit("triple-hub D1 ray not bracketed by D2 spokes")

    if len(quad) != 8:
        raise SystemExit(f"unexpected quadruple-hub pattern count: {len(quad)}")
    if not all(every_d1_touches_d2(bits) for bits in quad):
        raise SystemExit("quadruple-hub D1 ray without adjacent D2 spoke")

    # Q-hub: h <= I-D2 = 10, so clean >= 8. Five hub D1 targets
    # are unavailable, leaving at most six chargeable D1 targets.
    q_clean_lower = N - (I - D2)
    q_charge_capacity = D1 - 5
    if not q_clean_lower > q_charge_capacity:
        raise SystemExit("quadruple-hub charge contradiction not obtained")

    # T-hub: alternation forces all three leaf-pair arrangement lines.
    # Beyond the three spoke-line incidence identifications this contributes
    # at least two more, so h <= I-5 = 8 and clean >= 10.
    t_h_upper = I - 5
    t_clean_lower = N - t_h_upper
    t_charge_capacity = D1 - 3
    if not t_clean_lower > t_charge_capacity:
        raise SystemExit("triple-hub charge contradiction not obtained")

    receipt = {
        "profile": [3, 3, 3, 4],
        "D2": D2,
        "D1": D1,
        "U": U,
        "triple_hub_patterns": len(triple),
        "quadruple_hub_patterns": len(quad),
        "quadruple_hub": {
            "clean_line_lower_bound": q_clean_lower,
            "available_D1_charge_targets_upper_bound": q_charge_capacity,
        },
        "triple_hub": {
            "core_line_upper_bound": t_h_upper,
            "clean_line_lower_bound": t_clean_lower,
            "available_D1_charge_targets_upper_bound": t_charge_capacity,
        },
        "result": "D2=3_STAR_ROLE_TYPES_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite consequence of the named local fan and clean-line charging "
            "premises plus independently reconstructed transverse-line and "
            "core-line counting arguments; no hill-global upper bound or "
            "certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

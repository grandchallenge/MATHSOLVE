#!/usr/bin/env python3
"""Saturation/extreme-core replay for the q=5 H1-12 residual."""
from __future__ import annotations

import itertools
import json
from collections import Counter

try:
    from ci.validate_openmath_h1_12_q5_profiles import (
        COARSE_PROFILES,
        GRAPHS,
        N,
        DELTA,
        local_options,
    )
except ModuleNotFoundError:
    from validate_openmath_h1_12_q5_profiles import (
        COARSE_PROFILES,
        GRAPHS,
        N,
        DELTA,
        local_options,
    )


TARGET_PROFILES = (
    (3, 3, 3, 3, 3),
    (3, 3, 3, 3, 4),
    (3, 3, 4, 4, 4),
)

EXPECTED_MIN_SATURATION = {
    (3, 3, 3, 3, 3): {
        3: 0, 4: 1, 5: 1, 6: 2, 7: 2, 8: 3, 9: 4, 10: 5,
    },
    (3, 3, 3, 3, 4): {
        5: 2, 6: 2, 7: 3, 8: 4, 9: 5,
    },
    (3, 3, 4, 4, 4): {
        6: 4, 7: 4,
    },
}

EXPECTED_RETAINED = {
    (3, 3, 3, 3, 3): {
        "state_count": 595,
        "D2_values": [3, 4, 5, 6, 7],
    },
    (3, 3, 3, 3, 4): {
        "state_count": 300,
        "D2_values": [5, 6],
    },
    (3, 3, 4, 4, 4): {
        "state_count": 0,
        "D2_values": [],
    },
}


def local_options_with_saturation(r, d2):
    return tuple(
        (d1, blocked, int(d1 + d2 == 2 * r))
        for d1, blocked in local_options(r, d2)
    )


def total_options(rs, degrees):
    totals = {(0, 0, 0)}
    for r, d2 in zip(rs, degrees):
        local = local_options_with_saturation(r, d2)
        if not local:
            return set()
        totals = {
            (
                D1 + d1,
                B + blocked,
                saturated + sat,
            )
            for D1, B, saturated in totals
            for d1, blocked, sat in local
        }
    return totals


def surviving_state(rs, D2, degrees, max_saturated=None):
    I = sum(rs)
    S = sum(r * (r - 2) for r in rs)

    found = []
    for D1, blocked, saturated in total_options(rs, degrees):
        if max_saturated is not None and saturated > max_saturated:
            continue

        U = DELTA - S + D1 + D2
        if U < 0:
            continue

        clean = N - (I - D2)
        capacity = 2 * U + D1 - blocked
        if clean <= capacity:
            found.append((D1, blocked, saturated, U, clean, capacity))
    return found


def saturation_summary(profile):
    minimum = {}

    for rs in sorted(set(itertools.permutations(profile))):
        for D2, degrees in GRAPHS:
            rows = surviving_state(rs, D2, degrees)
            if not rows:
                continue
            value = min(row[2] for row in rows)
            minimum[D2] = min(minimum.get(D2, 99), value)

    return dict(sorted(minimum.items()))


def retained_summary(profile):
    state_count = 0
    d2_histogram = Counter()

    for rs in sorted(set(itertools.permutations(profile))):
        for D2, degrees in GRAPHS:
            rows = surviving_state(rs, D2, degrees)
            if not rows:
                continue

            # D2<=4 can be collinear, so do not use the five-point
            # noncollinear extreme-core cap there.
            max_saturated = 2 if D2 >= 5 else None
            filtered = surviving_state(
                rs, D2, degrees, max_saturated=max_saturated
            )
            if not filtered:
                continue

            state_count += 1
            d2_histogram[D2] += 1

    return {
        "state_count": state_count,
        "D2_values": sorted(d2_histogram),
        "D2_histogram": dict(sorted(d2_histogram.items())),
    }


def main() -> None:
    for profile, expected in EXPECTED_MIN_SATURATION.items():
        observed = saturation_summary(profile)
        if observed != expected:
            raise SystemExit(
                f"unexpected saturation table for {profile}: {observed}"
            )

    retained = {
        profile: retained_summary(profile)
        for profile in TARGET_PROFILES
    }

    for profile, expected in EXPECTED_RETAINED.items():
        observed = retained[profile]
        if observed["state_count"] != expected["state_count"]:
            raise SystemExit(
                f"unexpected retained state count for {profile}: "
                f"{observed['state_count']}"
            )
        if observed["D2_values"] != expected["D2_values"]:
            raise SystemExit(
                f"unexpected retained D2 range for {profile}: "
                f"{observed['D2_values']}"
            )

    receipt = {
        "minimum_saturated_cores": {
            str(profile): table
            for profile, table in EXPECTED_MIN_SATURATION.items()
        },
        "retained": {
            str(profile): retained[profile]
            for profile in TARGET_PROFILES
        },
        "result": "Q5_REDUCED_TO_33333_D2_3_7_AND_33334_D2_5_6",
        "claim_boundary": (
            "Finite saturation replay. At-most-two saturated cores is applied "
            "only for D2>=5, where five collinear cores are impossible. "
            "Saturated-core non-extremality remains source-conditional. No "
            "hill-global upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

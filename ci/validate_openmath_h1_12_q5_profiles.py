#!/usr/bin/env python3
"""Finite q=5 profile/core-graph replay for OM26-H1 H1-12."""
from __future__ import annotations

import itertools
import json
from collections import Counter
from functools import lru_cache


N = 18
T = 95
DELTA = N * (N - 2) - 3 * T
Q = 5
assert DELTA == 3

COARSE_PROFILES = [
    (3, 3, 3, 3, 3),
    (3, 3, 3, 3, 4),
    (3, 3, 3, 3, 5),
    (3, 3, 3, 4, 4),
    (3, 3, 3, 4, 5),
    (3, 3, 4, 4, 4),
    (3, 4, 4, 4, 4),
]

EXPECTED = {
    (3, 3, 3, 3, 3): {
        "state_count": 671,
        "D2": list(range(3, 11)),
    },
    (3, 3, 3, 3, 4): {
        "state_count": 1270,
        "D2": [5, 6, 7, 8, 9],
    },
    (3, 3, 3, 4, 4): {
        "state_count": 140,
        "D2": [6, 7],
    },
}


def coarse_profiles():
    out = []
    for rs in itertools.combinations_with_replacement(range(3, N + 1), Q):
        if sum(r * (r - 4) for r in rs) <= -2:
            out.append(rs)
    return out


@lru_cache(maxsize=None)
def local_options(r: int, d2: int):
    """Return sector-consistent (d1,blocked) options at one r-fold core."""
    length = 2 * r
    options = set()

    for sectors in itertools.product((0, 1), repeat=length):
        shared = tuple(
            sectors[(i - 1) % length] & sectors[i]
            for i in range(length)
        )
        positions = [i for i, value in enumerate(shared) if value]
        if len(positions) < d2:
            continue

        for d2_positions in itertools.combinations(positions, d2):
            d2_set = set(d2_positions)
            word = tuple(
                2 if i in d2_set
                else 1 if shared[i]
                else 0
                for i in range(length)
            )

            if any(
                all(word[(i + j) % length] == 1 for j in range(r - 1))
                for i in range(length)
            ):
                continue

            d1 = word.count(1)
            blocked = sum(
                word[i] == 1
                and (
                    word[(i - 1) % length] == 2
                    or word[(i + 1) % length] == 2
                )
                for i in range(length)
            )
            options.add((d1, blocked))

    return tuple(sorted(options))


def core_graphs():
    all_edges = list(itertools.combinations(range(Q), 2))
    for mask in range(1 << len(all_edges)):
        edges = tuple(
            all_edges[i]
            for i in range(len(all_edges))
            if (mask >> i) & 1
        )
        degree = [0] * Q
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
        yield len(edges), tuple(degree)


GRAPHS = tuple(core_graphs())


def total_options(rs, degrees):
    totals = {(0, 0)}
    for r, d2 in zip(rs, degrees):
        local = local_options(r, d2)
        if not local:
            return set()
        totals = {
            (D1 + d1, B + blocked)
            for D1, B in totals
            for d1, blocked in local
        }
    return totals


def profile_summary(profile):
    graph_state_count = 0
    d2_histogram = Counter()
    placement_count = 0

    for rs in sorted(set(itertools.permutations(profile))):
        I = sum(rs)
        S = sum(r * (r - 2) for r in rs)
        placement_survives = False

        for D2, degrees in GRAPHS:
            survives = False
            for D1, blocked in total_options(rs, degrees):
                U = DELTA - S + D1 + D2
                if U < 0:
                    continue
                clean = N - (I - D2)
                capacity = 2 * U + D1 - blocked
                if clean <= capacity:
                    survives = True
                    break

            if survives:
                graph_state_count += 1
                d2_histogram[D2] += 1
                placement_survives = True

        if placement_survives:
            placement_count += 1

    return {
        "state_count": graph_state_count,
        "D2_values": sorted(d2_histogram),
        "D2_histogram": dict(sorted(d2_histogram.items())),
        "surviving_multiplicity_placements": placement_count,
    }


def main() -> None:
    coarse = coarse_profiles()
    if coarse != COARSE_PROFILES:
        raise SystemExit(
            "unexpected coarse q=5 profile set:\n"
            + json.dumps([list(x) for x in coarse], indent=2)
        )

    summaries = {
        profile: profile_summary(profile)
        for profile in COARSE_PROFILES
    }

    survivors = {
        profile: summary
        for profile, summary in summaries.items()
        if summary["state_count"] > 0
    }

    if set(survivors) != set(EXPECTED):
        raise SystemExit(
            "unexpected surviving q=5 profiles:\n"
            + json.dumps(
                {str(k): v for k, v in survivors.items()},
                indent=2,
            )
        )

    for profile, expected in EXPECTED.items():
        observed = survivors[profile]
        if observed["state_count"] != expected["state_count"]:
            raise SystemExit(
                f"unexpected state count for {profile}: "
                f"{observed['state_count']}"
            )
        if observed["D2_values"] != expected["D2"]:
            raise SystemExit(
                f"unexpected D2 range for {profile}: "
                f"{observed['D2_values']}"
            )

    excluded = [
        profile for profile, summary in summaries.items()
        if summary["state_count"] == 0
    ]

    receipt = {
        "q": Q,
        "coarse_profiles": [list(x) for x in COARSE_PROFILES],
        "surviving_profiles": {
            str(profile): survivors[profile]
            for profile in EXPECTED
        },
        "excluded_profiles": [list(x) for x in excluded],
        "result": "Q5_REDUCED_TO_33333_33334_33344",
        "claim_boundary": (
            "Finite graph/sector/charge replay under the named local fan and "
            "clean-line charging premises. No hill-global upper bound or "
            "certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

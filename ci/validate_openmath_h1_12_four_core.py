#!/usr/bin/env python3
"""Independent finite replay for the OM26-H1 H1-12 q=4 residual.

The program treats the named clean-line/fan statements as explicit necessary
conditions. It does not prove those geometric premises.
"""
from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict

N = 18
T = 95
DELTA = N * (N - 2) - 3 * T
assert DELTA == 3

EXPECTED_PROFILES = [
    (3, 3, 3, 3),
    (3, 3, 3, 4),
    (3, 3, 3, 5),
    (3, 3, 4, 4),
    (3, 4, 4, 4),
]

EXPECTED_MIN_D2 = {
    (3, 3, 3, 3): 1,
    (3, 3, 3, 4): 3,
    (3, 3, 3, 5): 6,
    (3, 3, 4, 4): 5,
    (3, 4, 4, 4): 6,
}


def profile_candidates():
    result = []
    for rs in itertools.combinations_with_replacement(range(3, N + 1), 4):
        if sum(r * (r - 4) for r in rs) <= -3:
            result.append(rs)
    return result


def core_graphs():
    vertices = range(4)
    edges = list(itertools.combinations(vertices, 2))
    for mask in range(1 << len(edges)):
        chosen = tuple(
            edges[i] for i in range(len(edges)) if (mask >> i) & 1
        )
        degree = [0, 0, 0, 0]
        for a, b in chosen:
            degree[a] += 1
            degree[b] += 1
        yield chosen, tuple(degree)


def d1_cap(r: int, d2: int) -> int:
    # Source-scoped local premises.
    if r == 3:
        return 3 if d2 >= 3 else 2
    if d2 <= 1:
        return 2 * r - 4
    return 2 * r - 3


def shared_count_allowed(r: int, shared: int) -> bool:
    # Pure cyclic-sector necessity: exactly 2r-1 shared rays is impossible.
    return 0 <= shared <= 2 * r and shared != 2 * r - 1


def enumerate_states():
    states = []
    for rs in profile_candidates():
        I = sum(rs)
        S = sum(r * (r - 2) for r in rs)

        for edges, degrees in core_graphs():
            D2 = len(edges)
            caps = [d1_cap(r, d2) for r, d2 in zip(rs, degrees)]

            for local_d1 in itertools.product(
                *[range(cap + 1) for cap in caps]
            ):
                if any(
                    not shared_count_allowed(r, d1 + d2)
                    for r, d1, d2 in zip(rs, local_d1, degrees)
                ):
                    continue

                D1 = sum(local_d1)
                U = DELTA - S + D1 + D2
                if U < 0:
                    continue

                # h <= I-D2, hence clean lines >= N-(I-D2).
                min_clean = N - (I - D2)
                if min_clean > 2 * U + D1:
                    continue

                states.append(
                    {
                        "multiplicities": list(rs),
                        "core_edges": [list(e) for e in edges],
                        "core_degrees": list(degrees),
                        "local_d1": list(local_d1),
                        "D1": D1,
                        "D2": D2,
                        "U": U,
                        "I": I,
                        "S": S,
                        "min_clean": min_clean,
                    }
                )
    return states


def summarize(states):
    by_profile = defaultdict(list)
    for state in states:
        by_profile[tuple(state["multiplicities"])].append(state)

    result = {}
    for profile in EXPECTED_PROFILES:
        rows = by_profile[profile]
        result[str(profile)] = {
            "state_count": len(rows),
            "min_D2": min(row["D2"] for row in rows),
            "D2_histogram": dict(
                sorted(Counter(row["D2"] for row in rows).items())
            ),
        }
    return result


def main() -> None:
    profiles = profile_candidates()
    if profiles != EXPECTED_PROFILES:
        raise SystemExit(
            "unexpected q=4 profile set:\n" + json.dumps(profiles, indent=2)
        )

    states = enumerate_states()
    observed_min = {}
    for profile in EXPECTED_PROFILES:
        rows = [
            row
            for row in states
            if tuple(row["multiplicities"]) == profile
        ]
        if not rows:
            raise SystemExit(f"no surviving states for {profile}")
        observed_min[profile] = min(row["D2"] for row in rows)

    if observed_min != EXPECTED_MIN_D2:
        raise SystemExit(
            "unexpected minimum D2 table:\n"
            + json.dumps(
                {str(k): v for k, v in observed_min.items()}, indent=2
            )
        )

    receipt = {
        "n": N,
        "triangles": T,
        "defect": DELTA,
        "q": 4,
        "multiplicity_profiles": [list(x) for x in EXPECTED_PROFILES],
        "minimum_D2": {
            str(k): v for k, v in EXPECTED_MIN_D2.items()
        },
        "summary": summarize(states),
        "claim_boundary": (
            "Finite arithmetic/combinatorial replay under explicitly named "
            "source-scoped clean-line/fan premises; no hill-global upper "
            "bound, optimality, or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

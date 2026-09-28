#!/usr/bin/env python3
"""Independent arithmetic replay for the OM26-H1 H1-12 q=3 residual.

This program does NOT prove the geometric clean-line or fan premises. It treats
those premises as explicit inequalities and exhaustively checks their n=18,
T=95 integer consequences.
"""
from __future__ import annotations

import itertools
import json


N = 18
T = 95
DELTA = N * (N - 2) - 3 * T
assert DELTA == 3


def core_graphs():
    vertices = range(3)
    edges = list(itertools.combinations(vertices, 2))
    for size in range(4):
        for chosen in itertools.combinations(edges, size):
            degree = [0, 0, 0]
            for a, b in chosen:
                degree[a] += 1
                degree[b] += 1
            yield chosen, tuple(degree)


def d1_cap(r: int, d2: int) -> int:
    # Source-scoped local premises:
    # - at a triple point d1=3 would force d2>=3; q=3 gives d2<=2;
    # - when d2<=1, d1<=2r-4;
    # - universally, d1<=2r-3.
    if r == 3:
        return 2
    if d2 <= 1:
        return 2 * r - 4
    return 2 * r - 3


def shared_ray_count_not_forbidden(r: int, shared: int) -> bool:
    """Necessary cyclic-sector condition used by the classification proof.

    A radial ray is shared iff both adjacent sectors are triangular. If all
    2r sectors are triangular, all 2r rays are shared. Otherwise any
    nontriangular sector makes both of its boundary rays nonshared. Therefore
    exactly 2r-1 shared rays is impossible.

    We deliberately use only this necessary condition in the global
    enumeration. This makes the search more permissive, so uniqueness of the
    surviving template does not depend on silently importing a stronger
    sector-classification theorem.
    """
    return 0 <= shared <= 2 * r and shared != 2 * r - 1


def enumerate_feasible():
    feasible = []
    for rs in itertools.combinations_with_replacement(range(3, N + 1), 3):
        I = sum(rs)
        S = sum(r * (r - 2) for r in rs)
        for edges, degrees in core_graphs():
            D2 = len(edges)
            caps = [d1_cap(r, d2) for r, d2 in zip(rs, degrees)]
            for local_d1 in itertools.product(
                *[range(cap + 1) for cap in caps]
            ):
                if any(
                    not shared_ray_count_not_forbidden(r, d1 + d2)
                    for r, d1, d2 in zip(rs, local_d1, degrees)
                ):
                    continue

                D1 = sum(local_d1)
                # delta = S + U - D1 - D2.
                U = DELTA - S + D1 + D2
                if U < 0:
                    continue

                # h <= I-D2, so the number of clean lines is at least
                # N-(I-D2). Requiring charging even at that most-permissive h
                # is a necessary condition.
                min_clean = N - (I - D2)
                if min_clean > 2 * U + D1:
                    continue

                feasible.append(
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
    return feasible


def sector_patterns(r: int, shared: int):
    result = []
    for sectors in itertools.product((0, 1), repeat=2 * r):
        count = sum(
            sectors[i] and sectors[(i + 1) % (2 * r)]
            for i in range(2 * r)
        )
        if count == shared:
            result.append(sectors)
    return result


def main() -> None:
    feasible = enumerate_feasible()
    expected = [
        {
            "multiplicities": [3, 3, 3],
            "core_edges": [[0, 1], [0, 2], [1, 2]],
            "core_degrees": [2, 2, 2],
            "local_d1": [2, 2, 2],
            "D1": 6,
            "D2": 3,
            "U": 3,
            "I": 9,
            "S": 9,
            "min_clean": 12,
        }
    ]
    if feasible != expected:
        raise SystemExit(
            "unexpected q=3 feasible set:\n" + json.dumps(feasible, indent=2)
        )

    patterns = sector_patterns(3, 4)
    if not patterns:
        raise SystemExit("no six-sector realization with four shared rays")
    if any(sum(1 - bit for bit in pattern) != 1 for pattern in patterns):
        raise SystemExit(
            "four shared rays on a six-sector cycle did not force one "
            "nontriangular sector"
        )

    # In the surviving case charging also forces h=6:
    # h<=I-D2=6, while 18-h<=2U+D1=12 gives h>=6.
    h = 6
    receipt = {
        "n": N,
        "triangles": T,
        "defect": DELTA,
        "q": 3,
        "surviving_templates": feasible,
        "forced_h": h,
        "triangular_sectors_per_core": 5,
        "claim_boundary": (
            "Arithmetic/sector consequence of explicit source-scoped "
            "clean-line and fan premises; not an unconditional Kobon upper "
            "bound and not certification."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

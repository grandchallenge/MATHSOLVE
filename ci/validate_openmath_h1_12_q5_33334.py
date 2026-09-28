#!/usr/bin/env python3
"""Finite graph quotient for the OM26-H1 q=5 profile 33334 closure."""
from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict

try:
    from ci.validate_openmath_h1_12_q5_profiles import (
        DELTA,
        N,
        local_options,
    )
except ModuleNotFoundError:
    from validate_openmath_h1_12_q5_profiles import (
        DELTA,
        N,
        local_options,
    )


PROFILE = (3, 3, 3, 3, 4)
Q = 5
QUAD = 4
ALL_EDGES = tuple(itertools.combinations(range(Q), 2))
TRIPLE_PERMS = tuple(itertools.permutations(range(4)))

EXPECTED_ORBITS = [
    {
        "D2": 5,
        "edges": ((0,1),(0,2),(0,3),(1,2),(1,3)),
        "degrees": (3,3,2,2,0),
        "orbit_size": 6,
        "saturated": (0,1),
        "separator_ok": False,
    },
    {
        "D2": 5,
        "edges": ((0,1),(0,2),(0,4),(1,2),(1,4)),
        "degrees": (3,3,2,0,2),
        "orbit_size": 12,
        "saturated": (0,1),
        "separator_ok": False,
    },
    {
        "D2": 6,
        "edges": ((0,1),(0,2),(0,3),(1,2),(1,4),(3,4)),
        "degrees": (3,3,2,2,2),
        "orbit_size": 24,
        "saturated": (0,1),
        "separator_ok": False,
    },
    {
        "D2": 6,
        "edges": ((0,1),(0,2),(0,4),(1,3),(1,4),(2,3)),
        "degrees": (3,3,2,2,2),
        "orbit_size": 12,
        "saturated": (0,1),
        "separator_ok": False,
    },
    {
        "D2": 6,
        "edges": ((0,1),(0,2),(0,4),(1,3),(2,3),(3,4)),
        "degrees": (3,2,2,3,2),
        "orbit_size": 6,
        "saturated": (0,3),
        "separator_ok": True,
    },
]


def graphs():
    for mask in range(1 << len(ALL_EDGES)):
        edges = tuple(
            ALL_EDGES[i]
            for i in range(len(ALL_EDGES))
            if (mask >> i) & 1
        )
        degree = [0] * Q
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
        yield edges, tuple(degree)


def local_options_with_saturation(r, d2):
    return tuple(
        (d1, blocked, int(d1 + d2 == 2 * r))
        for d1, blocked in local_options(r, d2)
    )


def state_options(degrees, D2):
    S = sum(r * (r - 2) for r in PROFILE)
    I = sum(PROFILE)
    local = [
        local_options_with_saturation(r, d2)
        for r, d2 in zip(PROFILE, degrees)
    ]
    if any(not x for x in local):
        return []

    out = []
    for choice in itertools.product(*local):
        D1 = sum(x[0] for x in choice)
        blocked = sum(x[1] for x in choice)
        saturated = tuple(i for i, x in enumerate(choice) if x[2])
        if len(saturated) > 2:
            continue

        U = DELTA - S + D1 + D2
        if U < 0:
            continue

        clean = N - (I - D2)
        capacity = 2 * U + D1 - blocked
        if clean <= capacity:
            out.append({
                "D1": D1,
                "blocked": blocked,
                "saturated": saturated,
                "U": U,
                "clean": clean,
                "capacity": capacity,
            })
    return out


def canonical_edges(edges):
    candidates = []
    for perm in TRIPLE_PERMS:
        mapping = {i: perm[i] for i in range(4)}
        mapping[QUAD] = QUAD
        candidates.append(tuple(sorted(
            tuple(sorted((mapping[a], mapping[b])))
            for a, b in edges
        )))
    return min(candidates)


def saturated_role(states):
    roles = {row["saturated"] for row in states}
    if len(roles) != 1:
        raise AssertionError(f"non-unique saturated role: {roles}")
    role = next(iter(roles))
    if len(role) != 2:
        raise AssertionError(f"expected exactly two saturated cores: {role}")
    if QUAD in role:
        raise AssertionError(f"quadruple core unexpectedly saturated: {role}")
    return role


def neighbor_set(edges, vertex):
    out = []
    for a, b in edges:
        if a == vertex:
            out.append(b)
        elif b == vertex:
            out.append(a)
    return tuple(sorted(out))


def separator_ok(edges, saturated):
    edge_set = set(edges)
    for hub in saturated:
        neighbors = neighbor_set(edges, hub)
        if len(neighbors) != 3:
            return False
        if any(
            tuple(sorted(pair)) in edge_set
            for pair in itertools.combinations(neighbors, 2)
        ):
            return False
    return True


def quotient():
    retained = []
    for edges, degrees in graphs():
        D2 = len(edges)
        if D2 not in (5, 6):
            continue
        states = state_options(degrees, D2)
        if states:
            retained.append((edges, degrees, states))

    groups = defaultdict(list)
    for row in retained:
        groups[(len(row[0]), canonical_edges(row[0]))].append(row)

    summary = []
    for (D2, canon), members in groups.items():
        representative = next(
            (row for row in members if row[0] == canon),
            min(members, key=lambda row: row[0]),
        )
        edges, degrees, states = representative
        role = saturated_role(states)
        summary.append({
            "D2": D2,
            "edges": edges,
            "degrees": degrees,
            "orbit_size": len(members),
            "saturated": role,
            "separator_ok": separator_ok(edges, role),
        })
    return retained, sorted(summary, key=lambda x: (x["D2"], x["edges"]))


def main() -> None:
    retained, orbits = quotient()

    histogram = Counter(len(edges) for edges, _, _ in retained)
    if dict(sorted(histogram.items())) != {5: 18, 6: 42}:
        raise SystemExit(f"unexpected labeled graph histogram: {histogram}")

    observed = [
        {
            "D2": row["D2"],
            "edges": row["edges"],
            "degrees": row["degrees"],
            "orbit_size": row["orbit_size"],
            "saturated": row["saturated"],
            "separator_ok": row["separator_ok"],
        }
        for row in orbits
    ]
    if observed != EXPECTED_ORBITS:
        raise SystemExit(
            "unexpected 33334 graph quotient:\n"
            + json.dumps(observed, indent=2)
        )

    survivors = [row for row in orbits if row["separator_ok"]]
    if len(survivors) != 1:
        raise SystemExit(f"unexpected separator survivor count: {len(survivors)}")

    survivor = survivors[0]
    expected_k23 = {
        (0,1),(0,2),(0,4),
        (3,1),(3,2),(3,4),
    }
    if set(survivor["edges"]) != expected_k23:
        raise SystemExit(f"separator survivor is not K2,3: {survivor}")

    if tuple(sorted(survivor["saturated"])) != (0, 3):
        raise SystemExit("K2,3 degree-3 side is not exactly the saturated pair")

    receipt = {
        "profile": list(PROFILE),
        "retained_labeled_graphs": len(retained),
        "D2_histogram": dict(sorted(histogram.items())),
        "orbit_count": len(orbits),
        "orbit_sizes": [row["orbit_size"] for row in orbits],
        "separator_survivors": 1,
        "separator_survivor_graph": "K2,3",
        "separator_survivor_saturated_side": list(survivor["saturated"]),
        "result": "33334_REDUCED_TO_K23_THEN_GEOMETRICALLY_EXCLUDED",
        "claim_boundary": (
            "Finite graph/saturation quotient plus saturated-neighbor "
            "independence replay. The final two-interior-hub straight-line "
            "crossing contradiction is proved in the companion Solve note. "
            "No hill-global upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

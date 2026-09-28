#!/usr/bin/env python3
"""Finite S5 quotient for the OM26-H1 q=5 profile 33333 reduction."""
from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict

try:
    from ci.validate_openmath_h1_12_q5_profiles import DELTA, N, local_options
except ModuleNotFoundError:
    from validate_openmath_h1_12_q5_profiles import DELTA, N, local_options


PROFILE = (3, 3, 3, 3, 3)
Q = 5
ALL_EDGES = tuple(itertools.combinations(range(Q), 2))
PERMS = tuple(itertools.permutations(range(Q)))

EXPECTED_HISTOGRAM = {3:30, 4:60, 5:210, 6:195, 7:100}
EXPECTED_ORBIT_COUNTS = {3:2, 4:1, 5:4, 6:5, 7:3}
EXPECTED_ORBIT_SIZES = [20,10,60,30,60,60,60,60,5,60,60,10,10,60,30]

EXPECTED_SEPARATOR_CASES = [
    {
        "D2":3,
        "edges":((0,1),(0,2),(0,3)),
        "degrees":(3,1,1,1,0),
        "orbit_size":20,
        "saturated":(0,),
        "kind":"STAR_PLUS_ISOLATED",
    },
    {
        "D2":3,
        "edges":((0,1),(0,2),(1,2)),
        "degrees":(2,2,2,0,0),
        "orbit_size":10,
        "saturated":(),
        "kind":"TRIANGLE_PLUS_TWO_ISOLATED",
    },
    {
        "D2":5,
        "edges":((0,1),(0,2),(0,3),(1,4),(2,4)),
        "degrees":(3,2,2,1,2),
        "orbit_size":60,
        "saturated":(0,),
        "kind":"STAR_PLUS_TWO_ATTACHMENTS",
    },
    {
        "D2":6,
        "edges":((0,1),(0,2),(0,3),(1,4),(2,4),(3,4)),
        "degrees":(3,2,2,2,3),
        "orbit_size":10,
        "saturated":(0,4),
        "kind":"K2_3",
    },
]


def graphs():
    for mask in range(1 << len(ALL_EDGES)):
        edges = tuple(
            ALL_EDGES[i] for i in range(len(ALL_EDGES))
            if (mask >> i) & 1
        )
        degree = [0] * Q
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
        yield edges, tuple(degree)


def local_with_saturation(r, d2):
    return tuple(
        (d1, blocked, int(d1 + d2 == 2 * r))
        for d1, blocked in local_options(r, d2)
    )


def state_options(degrees, D2):
    S = sum(r * (r - 2) for r in PROFILE)
    I = sum(PROFILE)
    local = [
        local_with_saturation(r, d2)
        for r, d2 in zip(PROFILE, degrees)
    ]
    if any(not x for x in local):
        return []

    max_saturated = 2 if D2 >= 5 else None
    out = []
    for choice in itertools.product(*local):
        D1 = sum(x[0] for x in choice)
        blocked = sum(x[1] for x in choice)
        saturated = tuple(i for i, x in enumerate(choice) if x[2])
        if max_saturated is not None and len(saturated) > max_saturated:
            continue

        U = DELTA - S + D1 + D2
        if U < 0:
            continue

        clean = N - (I - D2)
        capacity = 2 * U + D1 - blocked
        if clean <= capacity:
            out.append({
                "D1":D1,
                "blocked":blocked,
                "saturated":saturated,
                "U":U,
                "clean":clean,
                "capacity":capacity,
                "local":choice,
            })
    return out


def canonical_edges(edges):
    return min(
        tuple(sorted(
            tuple(sorted((perm[a], perm[b])))
            for a, b in edges
        ))
        for perm in PERMS
    )


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
        if D2 not in range(3, 8):
            continue
        states = state_options(degrees, D2)
        if states:
            retained.append((edges, degrees, states))

    groups = defaultdict(list)
    for row in retained:
        groups[(len(row[0]), canonical_edges(row[0]))].append(row)

    orbits = []
    for (D2, canon), members in groups.items():
        representative = next(
            (row for row in members if row[0] == canon),
            min(members, key=lambda row: row[0]),
        )
        edges, degrees, states = representative
        satsets = sorted({row["saturated"] for row in states})
        compatible = [
            satset for satset in satsets
            if separator_ok(edges, satset)
        ]
        orbits.append({
            "D2":D2,
            "edges":edges,
            "degrees":degrees,
            "orbit_size":len(members),
            "saturated_sets":satsets,
            "separator_compatible":compatible,
            "states":states,
        })
    return retained, sorted(orbits, key=lambda x:(x["D2"],x["edges"]))


def case_kind(edges, compatible):
    edge_set = set(edges)
    if edge_set == {(0,1),(0,2),(0,3)} and compatible == [(0,)]:
        return "STAR_PLUS_ISOLATED"
    if edge_set == {(0,1),(0,2),(1,2)} and compatible == [()]:
        return "TRIANGLE_PLUS_TWO_ISOLATED"
    if edge_set == {(0,1),(0,2),(0,3),(1,4),(2,4)} and compatible == [(0,)]:
        return "STAR_PLUS_TWO_ATTACHMENTS"
    if edge_set == {(0,1),(0,2),(0,3),(1,4),(2,4),(3,4)} and compatible == [(0,4)]:
        return "K2_3"
    return None


def separator_cases(orbits):
    out = []
    for row in orbits:
        if not row["separator_compatible"]:
            continue
        kind = case_kind(row["edges"], row["separator_compatible"])
        if kind is None:
            raise AssertionError(f"unclassified separator case: {row}")
        out.append({
            "D2":row["D2"],
            "edges":row["edges"],
            "degrees":row["degrees"],
            "orbit_size":row["orbit_size"],
            "saturated":row["separator_compatible"][0],
            "kind":kind,
        })
    return out


def main() -> None:
    retained, orbits = quotient()

    histogram = Counter(len(edges) for edges, _, _ in retained)
    if dict(sorted(histogram.items())) != EXPECTED_HISTOGRAM:
        raise SystemExit(f"unexpected 33333 histogram: {histogram}")

    orbit_counts = Counter(row["D2"] for row in orbits)
    if dict(sorted(orbit_counts.items())) != EXPECTED_ORBIT_COUNTS:
        raise SystemExit(f"unexpected orbit counts: {orbit_counts}")

    if [row["orbit_size"] for row in orbits] != EXPECTED_ORBIT_SIZES:
        raise SystemExit(
            f"unexpected orbit sizes: {[row['orbit_size'] for row in orbits]}"
        )

    cases = separator_cases(orbits)
    if cases != EXPECTED_SEPARATOR_CASES:
        raise SystemExit(
            "unexpected separator-compatible cases:\n"
            + json.dumps(cases, indent=2)
        )

    star = next(x for x in orbits if case_kind(x["edges"], x["separator_compatible"]) == "STAR_PLUS_ISOLATED")
    star_capacity = max(row["capacity"] for row in star["states"] if row["saturated"] == (0,))
    if star_capacity != 6:
        raise SystemExit(f"unexpected star capacity: {star_capacity}")
    strengthened_star_clean = 9
    if not strengthened_star_clean > star_capacity:
        raise SystemExit("star-plus-isolated clean-line contradiction not obtained")

    triangle = next(x for x in orbits if case_kind(x["edges"], x["separator_compatible"]) == "TRIANGLE_PLUS_TWO_ISOLATED")
    triangle_states = [row for row in triangle["states"] if row["saturated"] == ()]
    equality = {
        (row["D1"], row["U"], row["blocked"], row["clean"], row["capacity"])
        for row in triangle_states
    }
    if equality != {(10,1,6,6,6)}:
        raise SystemExit(f"unexpected triangle equality data: {equality}")

    receipt = {
        "profile":list(PROFILE),
        "retained_labeled_graphs":len(retained),
        "D2_histogram":dict(sorted(histogram.items())),
        "orbit_count":len(orbits),
        "orbit_counts_by_D2":dict(sorted(orbit_counts.items())),
        "separator_compatible_cases":cases,
        "post_geometry_survivor":"K3_PLUS_TWO_ISOLATED",
        "survivor_equality":{
            "D2":3,
            "D1":10,
            "U":1,
            "blocked":6,
            "clean":6,
            "capacity":6,
        },
        "result":"33333_REDUCED_TO_K3_PLUS_TWO_ISOLATED_EQUALITY",
        "claim_boundary":(
            "Finite S5 graph/saturation quotient and separator-role replay. "
            "The star-plus-two-attachments incidence exhaustion and K2,3 "
            "crossing contradictions are proved in the companion Solve note. "
            "No hill-global upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

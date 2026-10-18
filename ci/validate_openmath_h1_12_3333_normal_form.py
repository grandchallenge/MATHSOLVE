#!/usr/bin/env python3
"""Finite normal-form replay for OM26-H1 H1-12 profile 3333.

The replay imports the protected q=4 saturated-core-filtered state set, applies
the transverse-line blocked-target consequence of the named local fan premise,
then quotients the survivors by S4 permutation of the four triple cores.
"""
from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict
from functools import lru_cache

try:
    from ci.validate_openmath_h1_12_saturated_core import (
        reduced_states,
        saturated_count,
    )
except ModuleNotFoundError:
    from validate_openmath_h1_12_saturated_core import (
        reduced_states,
        saturated_count,
    )


N = 18
PROFILE = (3, 3, 3, 3)

EXPECTED_D2_HISTOGRAM = {1: 6, 2: 15, 3: 36, 4: 39, 5: 12}

EXPECTED_ORBITS = [
    {"D2":1,"edges":[[0,1]],"degrees":[1,1,0,0],"d1":[2,2,2,2],"D1":8,"U":0,"saturated":0,"blocked":0,"clean":7,"capacity":8,"labeled":6},
    {"D2":2,"edges":[[0,1],[0,2]],"degrees":[2,1,1,0],"d1":[2,2,2,2],"D1":8,"U":1,"saturated":0,"blocked":1,"clean":8,"capacity":9,"labeled":12},
    {"D2":2,"edges":[[0,1],[2,3]],"degrees":[1,1,1,1],"d1":[2,2,2,2],"D1":8,"U":1,"saturated":0,"blocked":0,"clean":8,"capacity":10,"labeled":3},
    {"D2":3,"edges":[[0,1],[0,2],[0,3]],"degrees":[3,1,1,1],"d1":[1,2,2,2],"D1":7,"U":1,"saturated":0,"blocked":0,"clean":9,"capacity":9,"labeled":4},
    {"D2":3,"edges":[[0,1],[0,2],[0,3]],"degrees":[3,1,1,1],"d1":[3,1,2,2],"D1":8,"U":2,"saturated":1,"blocked":3,"clean":9,"capacity":9,"labeled":12},
    {"D2":3,"edges":[[0,1],[0,2],[0,3]],"degrees":[3,1,1,1],"d1":[3,2,2,2],"D1":9,"U":3,"saturated":1,"blocked":3,"clean":9,"capacity":12,"labeled":4},
    {"D2":3,"edges":[[0,1],[0,2],[1,2]],"degrees":[2,2,2,0],"d1":[2,2,2,2],"D1":8,"U":2,"saturated":0,"blocked":3,"clean":9,"capacity":9,"labeled":4},
    {"D2":3,"edges":[[0,1],[0,2],[1,3]],"degrees":[2,2,1,1],"d1":[2,2,2,2],"D1":8,"U":2,"saturated":0,"blocked":2,"clean":9,"capacity":10,"labeled":12},
    {"D2":4,"edges":[[0,1],[0,2],[0,3],[1,2]],"degrees":[3,2,2,1],"d1":[3,1,2,2],"D1":8,"U":3,"saturated":1,"blocked":4,"clean":10,"capacity":10,"labeled":24},
    {"D2":4,"edges":[[0,1],[0,2],[0,3],[1,2]],"degrees":[3,2,2,1],"d1":[3,2,2,2],"D1":9,"U":4,"saturated":1,"blocked":5,"clean":10,"capacity":12,"labeled":12},
    {"D2":4,"edges":[[0,1],[0,2],[1,3],[2,3]],"degrees":[2,2,2,2],"d1":[2,2,2,2],"D1":8,"U":3,"saturated":0,"blocked":4,"clean":10,"capacity":10,"labeled":3},
    {"D2":5,"edges":[[0,1],[0,2],[0,3],[1,2],[1,3]],"degrees":[3,3,2,2],"d1":[1,3,2,2],"D1":8,"U":4,"saturated":1,"blocked":5,"clean":11,"capacity":11,"labeled":12},
]


def profile_states() -> list[dict]:
    return [
        row for row in reduced_states()
        if tuple(row["multiplicities"]) == PROFILE
    ]


@lru_cache(maxsize=None)
def local_blocked_minimum(d1: int, d2: int) -> int:
    """Minimum D1 rays adjacent to D2 in a six-ray triple-point fan.

    Symbols: 0=other, 1=D1, 2=D2. The named local fan premise for r=3
    forbids two cyclically consecutive D1 rays.
    """
    if d1 < 0 or d2 < 0 or d1 + d2 > 6:
        raise ValueError((d1, d2))

    minima = []
    for word in itertools.product((0, 1, 2), repeat=6):
        if word.count(1) != d1 or word.count(2) != d2:
            continue
        if any(word[i] == 1 and word[(i + 1) % 6] == 1 for i in range(6)):
            continue
        blocked = sum(
            word[i] == 1
            and (word[(i - 1) % 6] == 2 or word[(i + 1) % 6] == 2)
            for i in range(6)
        )
        minima.append(blocked)

    if not minima:
        raise ValueError(f"no cyclic realization for d1={d1}, d2={d2}")
    return min(minima)


def blocked_lower_bound(state: dict) -> int:
    return sum(
        local_blocked_minimum(d1, d2)
        for d1, d2 in zip(state["local_d1"], state["core_degrees"])
    )


def refined_states() -> list[dict]:
    out = []
    for row in profile_states():
        blocked = blocked_lower_bound(row)
        capacity = 2 * row["U"] + row["D1"] - blocked
        clean = N - (row["I"] - row["D2"])
        if clean > capacity:
            continue
        item = dict(row)
        item["blocked"] = blocked
        item["clean"] = clean
        item["capacity"] = capacity
        item["saturated"] = saturated_count(row)
        out.append(item)
    return out


def canonical_key(state: dict):
    keys = []
    for perm in itertools.permutations(range(4)):
        # perm maps old vertex -> new vertex.
        edges = tuple(sorted(
            tuple(sorted((perm[a], perm[b])))
            for a, b in state["core_edges"]
        ))
        degrees = [None] * 4
        d1 = [None] * 4
        for old, new in enumerate(perm):
            degrees[new] = state["core_degrees"][old]
            d1[new] = state["local_d1"][old]
        keys.append((
            edges,
            tuple(degrees),
            tuple(d1),
            state["D1"],
            state["D2"],
            state["U"],
            state["saturated"],
            state["blocked"],
            state["clean"],
            state["capacity"],
        ))
    return min(keys)


def orbit_summary(states: list[dict]) -> list[dict]:
    groups = defaultdict(list)
    for row in states:
        groups[canonical_key(row)].append(row)

    result = []
    for key, members in groups.items():
        edges, degrees, d1, D1, D2, U, saturated, blocked, clean, capacity = key
        result.append({
            "D2": D2,
            "edges": [list(e) for e in edges],
            "degrees": list(degrees),
            "d1": list(d1),
            "D1": D1,
            "U": U,
            "saturated": saturated,
            "blocked": blocked,
            "clean": clean,
            "capacity": capacity,
            "labeled": len(members),
        })
    return sorted(
        result,
        key=lambda row: (
            row["D2"],
            row["edges"],
            row["degrees"],
            row["d1"],
            row["D1"],
            row["U"],
        ),
    )


def main() -> None:
    source = profile_states()
    if len(source) != 344:
        raise SystemExit(f"unexpected protected 3333 state count: {len(source)}")

    refined = refined_states()
    if len(refined) != 108:
        raise SystemExit(f"unexpected refined 3333 state count: {len(refined)}")

    histogram = dict(sorted(Counter(row["D2"] for row in refined).items()))
    if histogram != EXPECTED_D2_HISTOGRAM:
        raise SystemExit(f"unexpected D2 histogram: {histogram}")
    if any(row["D2"] == 6 for row in refined):
        raise SystemExit("D2=6 survived blocked-target refinement")

    orbits = orbit_summary(refined)
    if orbits != EXPECTED_ORBITS:
        raise SystemExit(
            "unexpected 3333 orbit quotient:\n" + json.dumps(orbits, indent=2)
        )

    equality = [row for row in orbits if row["clean"] == row["capacity"]]
    if len(equality) != 6:
        raise SystemExit(f"unexpected equality-orbit count: {len(equality)}")

    local_table = {
        f"{d1},{d2}": local_blocked_minimum(d1, d2)
        for d1, d2 in sorted({
            (d1, d2)
            for row in source
            for d1, d2 in zip(row["local_d1"], row["core_degrees"])
        })
    }

    receipt = {
        "profile": list(PROFILE),
        "input_labeled_states": len(source),
        "retained_labeled_states": len(refined),
        "D2_histogram": histogram,
        "normal_form_count": len(orbits),
        "equality_normal_form_count": len(equality),
        "local_blocked_minimums": local_table,
        "normal_forms": orbits,
        "claim_boundary": (
            "Finite consequence of the protected source-conditional q=4 "
            "state set, the named triple-point local fan premise, and the "
            "clean-line charging map, using the independently reconstructed "
            "transverse-line blocked-target lemma. No hill-global upper bound "
            "or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

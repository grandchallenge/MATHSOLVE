#!/usr/bin/env python3
"""Finite replay for the 3333 K3+isolated equality normal form."""
from __future__ import annotations

import itertools
import json

try:
    from ci.validate_openmath_h1_12_3333_c4 import residual_orbits
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_c4 import residual_orbits


def target_orbit():
    rows = [
        row for row in residual_orbits()
        if (
            row["D2"] == 3
            and tuple(row["degrees"]) == (2, 2, 2, 0)
            and row["saturated"] == 0
            and row["D1"] == 8
            and row["U"] == 2
            and row["blocked"] == 3
            and row["clean"] == row["capacity"] == 9
        )
    ]
    if len(rows) != 1:
        raise AssertionError(f"unexpected target count: {len(rows)}")
    return rows[0]


def adjacent_d2_local_words():
    """Fix D2 at positions 0,1; 1=D1, 2=D2, 0=other."""
    rows = []
    for word in itertools.product((0, 1, 2), repeat=6):
        if word[0:2] != (2, 2):
            continue
        if word.count(1) != 2 or word.count(2) != 2:
            continue
        if any(word[i] == 1 and word[(i + 1) % 6] == 1 for i in range(6)):
            continue
        blocked = sum(
            word[i] == 1
            and (word[(i - 1) % 6] == 2 or word[(i + 1) % 6] == 2)
            for i in range(6)
        )
        if blocked == 1:
            rows.append(word)
    return rows


def assignments():
    """Each vertex chooses one of its two incident edges in K3."""
    vertices = range(3)
    neighbors = {
        0: (1, 2),
        1: (0, 2),
        2: (0, 1),
    }
    rows = []
    for choices in itertools.product((0, 1), repeat=3):
        selected = []
        for v, bit in zip(vertices, choices):
            w = neighbors[v][bit]
            selected.append(tuple(sorted((v, w))))
        rows.append(tuple(selected))
    return rows


def selection_multiplicities(assignment):
    edges = ((0, 1), (0, 2), (1, 2))
    return tuple(sorted((assignment.count(edge) for edge in edges), reverse=True))


def main() -> None:
    row = target_orbit()
    if row["labeled"] != 4:
        raise SystemExit(f"unexpected arithmetic labeled count: {row['labeled']}")

    local = adjacent_d2_local_words()
    expected_local = {
        (2, 2, 0, 1, 0, 1),
        (2, 2, 1, 0, 1, 0),
    }
    if set(local) != expected_local:
        raise SystemExit(f"unexpected adjacent-D2 equality words: {local}")

    rows = assignments()
    if len(rows) != 8:
        raise SystemExit(f"unexpected assignment count: {len(rows)}")

    hist = {}
    for assignment in rows:
        key = selection_multiplicities(assignment)
        hist[key] = hist.get(key, 0) + 1

    expected_hist = {
        (1, 1, 1): 2,
        (2, 1, 0): 6,
    }
    if hist != expected_hist:
        raise SystemExit(f"unexpected symmetry-type histogram: {hist}")

    receipt = {
        "target": "3333_D2_3_K3_PLUS_ISOLATED_EQUALITY",
        "arithmetic_labeled_states": row["labeled"],
        "adjacent_D2_local_words": [list(x) for x in sorted(local)],
        "edge_choice_assignments_per_labeled_core_graph": len(rows),
        "orientation_type_histogram": {
            "cyclic_1_1_1": hist[(1, 1, 1)],
            "doubled_2_1_0": hist[(2, 1, 0)],
        },
        "result": "TWO_GEOMETRIC_ORIENTATION_TYPES_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite local equality and symmetry quotient after the independently "
            "reconstructed elementary-segment exclusion of the between-D2 "
            "mechanism. No hill-global upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

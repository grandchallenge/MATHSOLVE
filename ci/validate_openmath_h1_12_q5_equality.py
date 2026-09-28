#!/usr/bin/env python3
"""Finite local/equality replay for the sole q=5 H1-12 residual."""
from __future__ import annotations

import itertools
import json

try:
    from ci.validate_openmath_h1_12_q5_33333 import quotient
except ModuleNotFoundError:
    from validate_openmath_h1_12_q5_33333 import quotient


def triangle_local_words():
    """Fix adjacent D2 rays at positions 0,1. Return sector-consistent words."""
    out = []
    for sectors in itertools.product((0,1), repeat=6):
        shared = tuple(
            sectors[(i-1) % 6] & sectors[i]
            for i in range(6)
        )
        if not (shared[0] and shared[1]):
            continue

        word = tuple(
            2 if i in (0,1)
            else 1 if shared[i]
            else 0
            for i in range(6)
        )
        if word.count(1) != 2:
            continue
        if any(
            word[i] == 1 and word[(i+1) % 6] == 1
            for i in range(6)
        ):
            continue

        blocked = sum(
            word[i] == 1
            and (
                word[(i-1) % 6] == 2
                or word[(i+1) % 6] == 2
            )
            for i in range(6)
        )
        if blocked != 2:
            continue
        out.append((sectors, word))
    return out


def isolated_local_words():
    """Sector-consistent d2=0,d1=2 triple-core words."""
    out = []
    for sectors in itertools.product((0,1), repeat=6):
        shared = tuple(
            sectors[(i-1) % 6] & sectors[i]
            for i in range(6)
        )
        word = tuple(1 if shared[i] else 0 for i in range(6))
        if word.count(1) != 2:
            continue
        if any(
            word[i] == 1 and word[(i+1) % 6] == 1
            for i in range(6)
        ):
            continue
        out.append((sectors, word))
    return out


def d1_positions(word):
    return tuple(i for i, value in enumerate(word) if value == 1)


def sole_q5_case():
    _, orbits = quotient()
    rows = [
        row for row in orbits
        if (
            row["D2"] == 3
            and set(row["edges"]) == {(0,1),(0,2),(1,2)}
            and row["separator_compatible"] == [()]
        )
    ]
    if len(rows) != 1:
        raise AssertionError(f"unexpected sole-case count: {len(rows)}")
    return rows[0]


def main() -> None:
    row = sole_q5_case()

    equality = {
        (
            state["D1"],
            state["U"],
            state["blocked"],
            state["clean"],
            state["capacity"],
        )
        for state in row["states"]
        if state["saturated"] == ()
    }
    if equality != {(10,1,6,6,6)}:
        raise SystemExit(f"unexpected q5 equality tuple: {equality}")

    triangle = triangle_local_words()
    expected_triangle = [
        ((1,1,1,0,1,1), (2,2,1,0,0,1)),
    ]
    if triangle != expected_triangle:
        raise SystemExit(f"unexpected triangle local words: {triangle}")

    isolated = isolated_local_words()
    if len(isolated) != 3:
        raise SystemExit(f"unexpected isolated local word count: {len(isolated)}")
    for _, word in isolated:
        a, b = d1_positions(word)
        if (b - a) % 6 != 3:
            raise SystemExit(f"isolated D1 rays not antipodal: {word}")

    # Equality bookkeeping: 10 D1 - 6 blocked = 4 one-charge slots,
    # plus U=1 with two endpoint slots = exactly 6 clean-line charges.
    d1_charge_slots = 10 - 6
    u_charge_slots = 2 * 1
    clean = 6
    if d1_charge_slots + u_charge_slots != clean:
        raise SystemExit("q5 equality charge partition does not close")

    receipt = {
        "graph":"K3_PLUS_TWO_ISOLATED",
        "equality":{
            "D2":3,
            "D1":10,
            "U":1,
            "blocked":6,
            "clean":6,
            "capacity":6,
            "h":12,
        },
        "triangle_local_word":list(expected_triangle[0][1]),
        "triangle_D1_positions":list(d1_positions(expected_triangle[0][1])),
        "isolated_local_word_count":len(isolated),
        "isolated_D1_relation":"ANTIPODAL",
        "clean_charge_partition":{
            "isolated_core_D1_slots":d1_charge_slots,
            "U_endpoint_slots":u_charge_slots,
            "total":clean,
        },
        "result":"Q5_EQUALITY_NESTED_TRIANGLE_AND_4_PLUS_2_CHARGE_NORMAL_FORM",
        "claim_boundary":(
            "Finite local sector/equality replay for the sole q=5 residual. "
            "The nested outer-triangle incidence consequence is proved in "
            "the companion Solve note. No hill-global upper bound or "
            "certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Sector-consistency replay closing the remaining q=4 low-D2 forms."""
from __future__ import annotations

import itertools
import json


def sector_consistent_words(d1_count: int, d2_count: int):
    """Enumerate actual six-sector fans.

    Sector bit t_i is triangular/nontriangular. Ray i is shared iff both
    adjacent sectors are triangular. Shared rays are then labeled D1 or D2,
    with the named triple-point rule forbidding consecutive D1 rays.
    """
    words = set()
    for sectors in itertools.product((0, 1), repeat=6):
        shared = tuple(
            sectors[(i - 1) % 6] & sectors[i]
            for i in range(6)
        )
        positions = [i for i, value in enumerate(shared) if value]
        if len(positions) != d1_count + d2_count:
            continue

        for d1_positions in itertools.combinations(positions, d1_count):
            d1_positions = set(d1_positions)
            word = tuple(
                1 if i in d1_positions
                else 2 if shared[i]
                else 0
                for i in range(6)
            )
            if word.count(2) != d2_count:
                continue
            if any(
                word[i] == 1 and word[(i + 1) % 6] == 1
                for i in range(6)
            ):
                continue
            words.add(word)
    return sorted(words)


def blocked_count(word):
    return sum(
        value == 1
        and (
            word[(i - 1) % 6] == 2
            or word[(i + 1) % 6] == 2
        )
        for i, value in enumerate(word)
    )


def blocked_minimum(d1_count, d2_count):
    rows = sector_consistent_words(d1_count, d2_count)
    if not rows:
        raise AssertionError((d1_count, d2_count))
    return min(blocked_count(word) for word in rows), rows


def budget(D2, U, blocked):
    clean = 18 - (12 - D2)
    capacity = 2 * U + 8 - blocked
    return clean, capacity


def main() -> None:
    b21, words21 = blocked_minimum(2, 1)
    b22, words22 = blocked_minimum(2, 2)
    b20, words20 = blocked_minimum(2, 0)

    if b21 != 2:
        raise SystemExit(f"unexpected (2,1) blocked minimum: {b21}")
    if b22 != 2:
        raise SystemExit(f"unexpected (2,2) blocked minimum: {b22}")
    if b20 != 0:
        raise SystemExit(f"unexpected (2,0) blocked minimum: {b20}")

    forms = {
        "single_edge": {
            "D2": 1,
            "U": 0,
            "blocked": 2 + 2,
            "labeled": 6,
        },
        "P3_plus_isolated": {
            "D2": 2,
            "U": 1,
            "blocked": 2 + 2 + 2,
            "labeled": 12,
        },
        "two_disjoint_edges": {
            "D2": 2,
            "U": 1,
            "blocked": 2 + 2 + 2 + 2,
            "labeled": 3,
        },
        "P4_crosscheck": {
            "D2": 3,
            "U": 2,
            "blocked": 2 + 2 + 2 + 2,
            "labeled": 12,
        },
    }

    replay = {}
    for name, item in forms.items():
        clean, capacity = budget(item["D2"], item["U"], item["blocked"])
        if not clean > capacity:
            raise SystemExit(f"{name} did not violate budget")
        replay[name] = {
            **item,
            "clean_line_lower_bound": clean,
            "charge_capacity_upper_bound": capacity,
        }

    receipt = {
        "local": {
            "d1_2_d2_1": {
                "word_count": len(words21),
                "blocked_minimum": b21,
            },
            "d1_2_d2_2": {
                "word_count": len(words22),
                "blocked_minimum": b22,
            },
            "d1_2_d2_0": {
                "word_count": len(words20),
                "blocked_minimum": b20,
            },
        },
        "forms": replay,
        "newly_excluded_labeled_states": 21,
        "result": "Q4_PROFILE_3333_CLOSED__Q_GE_5_RESIDUAL",
        "claim_boundary": (
            "Sector-consistency is independently reconstructed. Global closure "
            "remains conditional on the named triple-point local fan premise "
            "and clean-line charging map. No hill-global upper bound or "
            "certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

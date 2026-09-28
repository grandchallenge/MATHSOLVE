#!/usr/bin/env python3
"""Finite quotient of the OM26-H1 H1-12 q=4 profile 3334.

This replay imports the protected saturated-core-filtered q=4 states and
quotients the 3334 states by permutation of the three triple cores. It checks
finite graph/count facts only. The geometric conclusion that a saturated core
is non-extreme retains the source scope stated in the companion proof note.
"""
from __future__ import annotations

import json
from collections import Counter

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


PROFILE = (3, 3, 3, 4)

EXPECTED_ROLE_COUNTS = {
    "D2=3|star|hub=T": 3,
    "D2=3|star|hub=Q": 1,
    "D2=4|cycle|hub=none": 3,
    "D2=4|star+outer=TT|hub=T": 12,
    "D2=4|star+outer=TQ|hub=T": 24,
    "D2=4|star+outer=TT|hub=Q": 12,
    "D2=5|K4-e|missing=TQ|hub=T": 6,
    "D2=5|K4-e|missing=TT|hub=T": 3,
    "D2=5|K4-e|missing=TT|hub=Q": 3,
}


def profile_states() -> list[dict]:
    return [
        state
        for state in reduced_states()
        if tuple(state["multiplicities"]) == PROFILE
    ]


def saturated_vertices(state: dict) -> list[int]:
    return [
        i
        for i, (r, d1, d2) in enumerate(
            zip(
                state["multiplicities"],
                state["local_d1"],
                state["core_degrees"],
            )
        )
        if d1 + d2 == 2 * r
    ]


def edge_role(edge: tuple[int, int] | list[int]) -> str:
    a, b = edge
    return "TQ" if 3 in (a, b) else "TT"


def descriptor(state: dict) -> str:
    d2 = state["D2"]
    edges = {tuple(edge) for edge in state["core_edges"]}
    sats = saturated_vertices(state)

    if d2 == 3:
        if len(sats) != 1:
            raise AssertionError("D2=3 state must have one saturated hub")
        hub = sats[0]
        if state["core_degrees"][hub] != 3:
            raise AssertionError("D2=3 saturated vertex is not the star hub")
        return f"D2=3|star|hub={'Q' if hub == 3 else 'T'}"

    if d2 == 4:
        if not sats:
            if tuple(sorted(state["core_degrees"])) != (2, 2, 2, 2):
                raise AssertionError("non-saturated D2=4 state is not a cycle")
            return "D2=4|cycle|hub=none"

        if len(sats) != 1:
            raise AssertionError("D2=4 state has unexpected saturation count")
        hub = sats[0]
        if state["core_degrees"][hub] != 3:
            raise AssertionError("D2=4 saturated vertex is not degree 3")
        spokes = {
            tuple(sorted((hub, j))) for j in range(4) if j != hub
        }
        extras = sorted(edges - spokes)
        if len(extras) != 1:
            raise AssertionError("D2=4 hub state is not star plus one edge")
        return (
            f"D2=4|star+outer={edge_role(extras[0])}|"
            f"hub={'Q' if hub == 3 else 'T'}"
        )

    if d2 == 5:
        if len(sats) != 1:
            raise AssertionError("D2=5 state must have one saturated hub")
        hub = sats[0]
        if state["core_degrees"][hub] != 3:
            raise AssertionError("D2=5 saturated vertex is not degree 3")
        all_edges = {
            (a, b) for a in range(4) for b in range(a + 1, 4)
        }
        missing = sorted(all_edges - edges)
        if len(missing) != 1:
            raise AssertionError("D2=5 graph is not K4 minus one edge")
        if hub in missing[0]:
            raise AssertionError("missing K4 edge is incident to saturated hub")
        return (
            f"D2=5|K4-e|missing={edge_role(missing[0])}|"
            f"hub={'Q' if hub == 3 else 'T'}"
        )

    raise AssertionError(f"unexpected D2={d2}")


def main() -> None:
    rows = profile_states()
    if len(rows) != 67:
        raise SystemExit(f"unexpected 3334 state count: {len(rows)}")

    d2_hist = Counter(row["D2"] for row in rows)
    if d2_hist != Counter({3: 4, 4: 51, 5: 12}):
        raise SystemExit(f"unexpected D2 histogram: {dict(d2_hist)}")

    roles = Counter(descriptor(row) for row in rows)
    if dict(roles) != EXPECTED_ROLE_COUNTS:
        raise SystemExit(
            "unexpected role quotient:\n"
            + json.dumps(dict(sorted(roles.items())), indent=2)
        )

    by_d2 = {}
    for d2 in (3, 4, 5):
        subset = [row for row in rows if row["D2"] == d2]
        by_d2[str(d2)] = {
            "state_count": len(subset),
            "D1_U": sorted(
                {f"{row['D1']},{row['U']}" for row in subset}
            ),
            "saturation_counts": sorted(
                {saturated_count(row) for row in subset}
            ),
        }

    if by_d2["3"]["D1_U"] != ["11,0"]:
        raise SystemExit(f"unexpected D2=3 D1/U: {by_d2['3']}")
    if by_d2["4"]["D1_U"] != ["10,0", "11,1"]:
        raise SystemExit(f"unexpected D2=4 D1/U: {by_d2['4']}")
    if by_d2["5"]["D1_U"] != ["10,1"]:
        raise SystemExit(f"unexpected D2=5 D1/U: {by_d2['5']}")

    receipt = {
        "profile": list(PROFILE),
        "state_count": len(rows),
        "D2_histogram": dict(sorted(d2_hist.items())),
        "role_counts": dict(sorted(roles.items())),
        "by_D2": by_d2,
        "claim_boundary": (
            "Finite quotient of the protected source-conditional 3334 "
            "state set. No hill-global upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Replay the saturated-core consequence for OM26-H1 H1-12 q=4.

This imports the protected four-core arithmetic enumerator. The geometric
statement "at most one saturated core when D2>=5" is proved in the companion
Solve note from the explicitly named local fan premise; this script checks
only the finite state consequences.
"""
from __future__ import annotations

import json

try:
    from ci.validate_openmath_h1_12_four_core import enumerate_states
except ModuleNotFoundError:
    from validate_openmath_h1_12_four_core import enumerate_states


def saturated_count(state: dict) -> int:
    return sum(
        d1 + d2 == 2 * r
        for r, d1, d2 in zip(
            state["multiplicities"],
            state["local_d1"],
            state["core_degrees"],
        )
    )


def reduced_states():
    return [
        state
        for state in enumerate_states()
        if state["D2"] < 5 or saturated_count(state) <= 1
    ]


def summarize(states):
    out = {}
    profiles = sorted({tuple(s["multiplicities"]) for s in states})
    for profile in profiles:
        rows = [s for s in states if tuple(s["multiplicities"]) == profile]
        out[str(profile)] = {
            "state_count": len(rows),
            "D2_values": sorted({s["D2"] for s in rows}),
            "max_saturated_cores": max(saturated_count(s) for s in rows),
        }
    return out


def main() -> None:
    original = enumerate_states()

    dense_profiles = {
        (3, 3, 3, 5),
        (3, 3, 4, 4),
        (3, 4, 4, 4),
    }
    for profile in dense_profiles:
        rows = [
            s for s in original
            if tuple(s["multiplicities"]) == profile
        ]
        if not rows:
            raise SystemExit(f"missing protected q=4 profile {profile}")
        if any(s["D2"] < 5 for s in rows):
            raise SystemExit(f"unexpected low-D2 state for {profile}")
        if any(saturated_count(s) < 2 for s in rows):
            raise SystemExit(
                f"profile {profile} has a state with fewer than two "
                "saturated cores"
            )

    reduced = reduced_states()
    profiles = sorted({tuple(s["multiplicities"]) for s in reduced})
    expected_profiles = [(3, 3, 3, 3), (3, 3, 3, 4)]
    if profiles != expected_profiles:
        raise SystemExit(
            "unexpected residual profiles:\n"
            + json.dumps([list(p) for p in profiles], indent=2)
        )

    d2_3333 = sorted({
        s["D2"] for s in reduced
        if tuple(s["multiplicities"]) == (3, 3, 3, 3)
    })
    d2_3334 = sorted({
        s["D2"] for s in reduced
        if tuple(s["multiplicities"]) == (3, 3, 3, 4)
    })

    if d2_3333 != [1, 2, 3, 4, 5, 6]:
        raise SystemExit(f"unexpected 3333 D2 set: {d2_3333}")
    if d2_3334 != [3, 4, 5]:
        raise SystemExit(f"unexpected 3334 D2 set: {d2_3334}")

    receipt = {
        "q": 4,
        "input_state_count": len(original),
        "residual_state_count": len(reduced),
        "residual_profiles": [list(p) for p in profiles],
        "summary": summarize(reduced),
        "excluded_profiles": [
            [3, 3, 3, 5],
            [3, 3, 4, 4],
            [3, 4, 4, 4],
        ],
        "claim_boundary": (
            "Finite consequence of the q=4 enumerator plus the companion "
            "source-conditional saturated-core hull lemma; no hill-global "
            "upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

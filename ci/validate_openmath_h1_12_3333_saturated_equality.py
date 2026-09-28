#!/usr/bin/env python3
"""Finite replay for the higher-count saturated 3333 D2=3 star exclusion."""
from __future__ import annotations

import itertools
import json

try:
    from ci.validate_openmath_h1_12_3333_nonsat_star import target_orbit as _unused_target
    from ci.validate_openmath_h1_12_3333_c4 import residual_orbits
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_nonsat_star import target_orbit as _unused_target
    from validate_openmath_h1_12_3333_c4 import residual_orbits


def saturated_equality_orbit():
    rows = []
    for row in residual_orbits():
        if (
            row["D2"] == 3
            and tuple(row["degrees"]) == (3, 1, 1, 1)
            and row["saturated"] == 1
            and row["D1"] == 9
            and row["U"] == 3
            and row["clean"] == row["capacity"] == 12
        ):
            rows.append(row)
    if len(rows) != 1:
        raise AssertionError(f"unexpected saturated equality orbit count: {len(rows)}")
    return rows[0]


def leaf_d1_choices():
    """Leaf ray positions:
    0=AB_in, 1=AH_in(D2), 2=AC_in, 3=AB_out, 4=AH_out, 5=AC_out.
    Equality forbids D1 adjacent to position 1; local fan forbids consecutive D1.
    """
    allowed = []
    for chosen in itertools.combinations(range(6), 2):
        chosen = set(chosen)
        if 0 in chosen or 2 in chosen:
            continue
        if any(
            i in chosen and (i + 1) % 6 in chosen
            for i in range(6)
        ):
            continue
        allowed.append(tuple(sorted(chosen)))
    return allowed


def main() -> None:
    row = saturated_equality_orbit()
    choices = leaf_d1_choices()
    if choices != [(3, 5)]:
        raise SystemExit(f"unexpected leaf D1 choices: {choices}")

    # Both forced D1 rays flank AH_out (position 4), so the elementary segment
    # on AH_out is adjacent to triangular sectors on both sides and is shared.
    left, right = choices[0]
    if not (left == 3 and right == 5):
        raise SystemExit("outward side-ray pair not forced")
    forced_third_d1_position = 4

    if row["labeled"] != 4:
        raise SystemExit(f"unexpected labeled multiplicity: {row['labeled']}")

    residual = [
        x for x in residual_orbits()
        if x != row
        and not (
            x["D2"] == 3
            and tuple(x["degrees"]) == (3, 1, 1, 1)
            and x["saturated"] == 0
            and x["D1"] == 7
            and x["U"] == 1
            and x["clean"] == x["capacity"] == 9
        )
    ]
    if len(residual) != 5:
        raise SystemExit(f"unexpected residual form count: {len(residual)}")
    if sum(x["labeled"] for x in residual) != 37:
        raise SystemExit("unexpected residual labeled-state count")

    receipt = {
        "target": "3333_D2_3_HIGHER_COUNT_SATURATED_STAR",
        "leaf_D1_choices_under_equality": [list(x) for x in choices],
        "forced_third_D1_ray_position": forced_third_d1_position,
        "target_labeled_states": row["labeled"],
        "retained_normal_forms": len(residual),
        "retained_labeled_states": sum(x["labeled"] for x in residual),
        "result": "HIGHER_COUNT_SATURATED_D2_3_STAR_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite leaf-ray consequence of the protected saturated-hub "
            "separator geometry plus the named local fan and clean-line "
            "charging equality; no hill-global upper bound or certification "
            "effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

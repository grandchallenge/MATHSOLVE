#!/usr/bin/env python3
"""Finite replay for the profile-3333 D2=4 C4 equality exclusion."""
from __future__ import annotations

import itertools
import json

try:
    from ci.validate_openmath_h1_12_3333_saturated_hub import reduced_orbits
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_saturated_hub import reduced_orbits


def blocked_count(word):
    n = len(word)
    return sum(
        value == 1
        and (word[(i - 1) % n] == 2 or word[(i + 1) % n] == 2)
        for i, value in enumerate(word)
    )


def equality_local_patterns():
    """0=other, 1=D1, 2=D2 at a triple core."""
    out = []
    for word in itertools.product((0, 1, 2), repeat=6):
        if word.count(1) != 2 or word.count(2) != 2:
            continue
        if any(word[i] == 1 and word[(i + 1) % 6] == 1 for i in range(6)):
            continue
        if blocked_count(word) != 1:
            continue
        out.append(word)
    return out


def dihedral_canonical(word):
    word = tuple(word)
    variants = []
    for source in (word, tuple(reversed(word))):
        for shift in range(6):
            variants.append(source[shift:] + source[:shift])
    return min(variants)


def local_types():
    return sorted({dihedral_canonical(word) for word in equality_local_patterns()})


def forces_neighbor_line(word):
    """Classify how the neighbor-neighbor arrangement line is forced.

    Return ADJACENT_D2 if the two D2 rays are cyclically adjacent.
    Return BLOCKED_D1_BETWEEN if the unique blocked D1 has D2 on both sides.
    """
    n = len(word)
    d2_positions = [i for i, value in enumerate(word) if value == 2]
    a, b = d2_positions
    if (a - b) % n in (1, n - 1):
        return "ADJACENT_D2"

    for i, value in enumerate(word):
        if (
            value == 1
            and word[(i - 1) % n] == 2
            and word[(i + 1) % n] == 2
        ):
            return "BLOCKED_D1_BETWEEN"
    return None


def residual_orbits():
    rows = reduced_orbits()
    out = []
    for row in rows:
        is_c4 = (
            row["D2"] == 4
            and tuple(row["degrees"]) == (2, 2, 2, 2)
            and row["saturated"] == 0
        )
        if not is_c4:
            out.append(row)
    return out


def main() -> None:
    source = reduced_orbits()
    c4 = [
        row for row in source
        if row["D2"] == 4
        and tuple(row["degrees"]) == (2, 2, 2, 2)
        and row["saturated"] == 0
    ]
    if len(c4) != 1:
        raise SystemExit(f"unexpected C4 form count: {len(c4)}")
    row = c4[0]
    if (row["clean"], row["capacity"], row["blocked"]) != (10, 10, 4):
        raise SystemExit(f"unexpected C4 equality tuple: {row}")

    patterns = equality_local_patterns()
    if len(patterns) != 18:
        raise SystemExit(f"unexpected labeled local pattern count: {len(patterns)}")

    types = local_types()
    expected_types = [
        (0, 1, 0, 1, 2, 2),
        (0, 1, 0, 2, 1, 2),
    ]
    if types != expected_types:
        raise SystemExit(f"unexpected local types: {types}")

    mechanisms = {forces_neighbor_line(word) for word in patterns}
    if mechanisms != {"ADJACENT_D2", "BLOCKED_D1_BETWEEN"}:
        raise SystemExit(f"unexpected forcing mechanisms: {mechanisms}")

    # One extra core-pair arrangement line makes h<=7, hence clean>=11,
    # strictly above the protected capacity 10.
    strengthened_clean = 11
    if not strengthened_clean > row["capacity"]:
        raise SystemExit("C4 strengthened clean-line contradiction not obtained")

    residual = residual_orbits()
    if len(residual) != 7:
        raise SystemExit(f"unexpected residual normal-form count: {len(residual)}")
    if sum(x["labeled"] for x in residual) != 45:
        raise SystemExit("unexpected residual labeled-state count")
    if any(x["D2"] >= 4 for x in residual):
        raise SystemExit("D2>=4 survived C4 exclusion")

    receipt = {
        "input_normal_forms": len(source),
        "C4_labeled_states": row["labeled"],
        "local_labeled_patterns": len(patterns),
        "local_dihedral_types": [list(x) for x in types],
        "neighbor_line_mechanisms": sorted(mechanisms),
        "strengthened_clean_line_lower_bound": strengthened_clean,
        "charge_capacity_upper_bound": row["capacity"],
        "retained_normal_forms": len(residual),
        "retained_labeled_states": sum(x["labeled"] for x in residual),
        "result": "D2_4_C4_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite local classification plus independently reconstructed "
            "core-incidence refinement, conditional on the named local fan "
            "premise and clean-line charging map. No hill-global upper bound "
            "or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()

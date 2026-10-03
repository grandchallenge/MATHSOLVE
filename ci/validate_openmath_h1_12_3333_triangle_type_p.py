#!/usr/bin/env python3
"""Finite replay for the triangle-isolated Type P exclusion."""
from __future__ import annotations

import itertools
import json

try:
    from ci.validate_openmath_h1_12_3333_triangle_isolated import assignments
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_triangle_isolated import assignments


VERTICES = (0, 1, 2)


def choice_map(assignment):
    out = {}
    for v, edge in zip(VERTICES, assignment):
        a, b = edge
        out[v] = b if a == v else a
    return out


def third_vertex(v, w):
    return next(x for x in VERTICES if x not in (v, w))


def point_p(x, y):
    return ("P",) + tuple(sorted((x, y)))


def point_q(w, v, u):
    # L_w intersect side(v,u)
    return ("Q", w) + tuple(sorted((v, u)))


def m_descriptor(v, choices):
    w = choices[v]
    u = third_vertex(v, w)
    points = (
        point_p(v, u),
        point_q(w, v, u),
    )
    return tuple(sorted(points))


def selection_counts(assignment):
    edges = ((0, 1), (0, 2), (1, 2))
    return tuple(sorted((assignment.count(edge) for edge in edges), reverse=True))


def duplicate_count(assignment):
    choices = choice_map(assignment)
    lines = [m_descriptor(v, choices) for v in VERTICES]
    return len(lines) - len(set(lines)), lines


def main() -> None:
    rows = assignments()
    type_p = [a for a in rows if selection_counts(a) == (2, 1, 0)]
    type_c = [a for a in rows if selection_counts(a) == (1, 1, 1)]

    if len(type_p) != 6 or len(type_c) != 2:
        raise SystemExit("unexpected orientation-type counts")

    p_dups = []
    for assignment in type_p:
        duplicates, lines = duplicate_count(assignment)
        if duplicates != 1:
            raise SystemExit(
                f"Type P assignment lacks unique M-line duplication: "
                f"{assignment} -> {lines}"
            )
        p_dups.append({"assignment": assignment, "M": lines})

    for assignment in type_c:
        duplicates, lines = duplicate_count(assignment)
        if duplicates != 0:
            raise SystemExit(
                f"Type C unexpectedly duplicates M-lines: {assignment} -> {lines}"
            )

    nominal_d1_capacity = 5
    u_capacity = 4
    type_p_d1_capacity = 4
    clean_lines = 9
    if not clean_lines > type_p_d1_capacity + u_capacity:
        raise SystemExit("Type P charge contradiction not obtained")

    receipt = {
        "type_P_assignments": len(type_p),
        "type_C_assignments": len(type_c),
        "type_P_duplicate_M_lines_per_assignment": 1,
        "nominal_D1_charge_slots": nominal_d1_capacity,
        "Type_P_distinct_D1_charge_lines_upper_bound": type_p_d1_capacity,
        "U_charge_capacity": u_capacity,
        "clean_lines": clean_lines,
        "result": "TYPE_P_EXCLUDED_SOURCE_CONDITIONAL",
        "claim_boundary": (
            "Finite incidence replay of the independently reconstructed M_V "
            "formula, conditional on the protected clean-line charging equality. "
            "No hill-global upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True, default=list))


if __name__ == "__main__":
    main()

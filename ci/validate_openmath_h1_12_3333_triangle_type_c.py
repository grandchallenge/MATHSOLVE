#!/usr/bin/env python3
"""Finite incidence replay for the triangle-isolated Type C exclusion."""
from __future__ import annotations

import json

try:
    from ci.validate_openmath_h1_12_3333_triangle_isolated import assignments
    from ci.validate_openmath_h1_12_3333_triangle_type_p import (
        choice_map,
        selection_counts,
        third_vertex,
    )
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_triangle_isolated import assignments
    from validate_openmath_h1_12_3333_triangle_type_p import (
        choice_map,
        selection_counts,
        third_vertex,
    )


VERTICES = (0, 1, 2)


def forced_multiple_descriptor(v, choices):
    w = choices[v]
    u = third_vertex(v, w)

    # Q_v is already the intersection of L_w and side(v,u).
    existing_lines = {
        ("third", w),
        ("side",) + tuple(sorted((v, u))),
    }

    # The triangular sector adjacent to the selected outward D1 introduces
    # a third side M_v through the same Q_v. It is distinct from both:
    # its other point X lies on side(v,w), away from v and w.
    forced_line = ("M", v)

    return {
        "vertex": v,
        "selected_neighbor": w,
        "other_vertex": u,
        "Q": ("Q", w) + tuple(sorted((v, u))),
        "existing_lines": tuple(sorted(existing_lines)),
        "forced_line": forced_line,
        "distinct_line_count": 3,
    }


def main() -> None:
    type_c = [
        assignment for assignment in assignments()
        if selection_counts(assignment) == (1, 1, 1)
    ]
    if len(type_c) != 2:
        raise SystemExit(f"unexpected Type C assignment count: {len(type_c)}")

    records = []
    for assignment in type_c:
        choices = choice_map(assignment)
        local = [forced_multiple_descriptor(v, choices) for v in VERTICES]
        if any(item["distinct_line_count"] != 3 for item in local):
            raise SystemExit("selected vertex failed to force three-line concurrence")
        if len({item["Q"] for item in local}) != 3:
            raise SystemExit("unexpected repeated Q descriptor inside Type C")
        records.append({
            "assignment": assignment,
            "forced_new_multiple_points": [item["Q"] for item in local],
        })

    receipt = {
        "Type_C_assignments": len(type_c),
        "selected_vertices_per_assignment": 3,
        "forced_new_multiple_points_per_assignment": 3,
        "minimum_needed_for_contradiction": 1,
        "result": "TYPE_C_EXCLUDED__K3_ISOLATED_EQUALITY_FORM_CLOSED",
        "claim_boundary": (
            "Finite incidence replay of the independently reconstructed "
            "selected-vertex geometry. Reaching Type C remains conditional on "
            "the protected local fan and clean-line equality premises. No "
            "hill-global upper bound or certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True, default=list))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Replicate the algebraic core of Galashin, Example B.1/B.3.

This script uses only the Python standard library. It:
1. verifies the five bounded regions of the projectivized arrangement;
2. solves the saturated degree-five critical-point equation for a regular
   hexagonal kami boundary;
3. reconstructs the five projective pairs (lambda, lambda_tilde);
4. checks denominator exclusion, critical residuals, orthogonality, adjacent
   minor signs, and winding numbers.

It does not reconstruct an explicit weighted planar bipartite graph, internal
face coordinates, a rigid-folding path, finite-thickness geometry, or a
manufacturable product.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Sequence

SQRT3 = math.sqrt(3.0)
TWO_PI = 2.0 * math.pi

C_MATRIX = (
    (1, 1, 0, -6, 0, 3),
    (0, 1, 1, 7, 0, -2),
    (0, 0, 0, 2, 1, 3),
)

# Projectivized lines Abar_C in the form A*x + B*y + D = 0.
LINES = (
    (Fraction(1), Fraction(0), Fraction(1)),   # x = -1
    (Fraction(1), Fraction(0), Fraction(0)),   # x = 0
    (Fraction(7), Fraction(2), Fraction(-6)),  # 7x + 2y = 6
    (Fraction(0), Fraction(1), Fraction(0)),   # y = 0
    (Fraction(-2), Fraction(3), Fraction(3)),  # -2x + 3y = -3
)

# Saturated resultant after removing the denominator-supported factor 25*x-24.
# Coefficients are descending powers of x.
QUINTIC = (
    350 * SQRT3 + 350j,
    -686 * SQRT3 + 4086j,
    -4908 * SQRT3 - 1710j,
    1923 * SQRT3 - 8073j,
    2610 * SQRT3 + 1422j,
    864j,
)


@dataclass(frozen=True)
class CriticalPoint:
    x: complex
    y: complex


def complex_record(z: complex) -> dict[str, float]:
    return {"re": float(z.real), "im": float(z.imag)}


def poly_eval(coefficients: Sequence[complex], z: complex) -> complex:
    value = 0j
    for coefficient in coefficients:
        value = value * z + coefficient
    return value


def durand_kerner(
    coefficients: Sequence[complex], *, tolerance: float = 1e-13, max_iterations: int = 500
) -> list[complex]:
    degree = len(coefficients) - 1
    if degree < 1 or coefficients[0] == 0:
        raise ValueError("A nonconstant polynomial with nonzero leading coefficient is required.")
    monic = [coefficient / coefficients[0] for coefficient in coefficients]
    radius = 1.0 + max(abs(coefficient) for coefficient in monic[1:])
    roots = [
        0.5 * radius * cmath.exp(2j * math.pi * (index + 0.2) / degree)
        for index in range(degree)
    ]
    for _ in range(max_iterations):
        updated: list[complex] = []
        maximum_step = 0.0
        for index, root in enumerate(roots):
            denominator = 1 + 0j
            for other_index, other_root in enumerate(roots):
                if other_index != index:
                    denominator *= root - other_root
            if abs(denominator) < 1e-30:
                raise RuntimeError("Durand-Kerner roots collided.")
            step = poly_eval(monic, root) / denominator
            updated_root = root - step
            updated.append(updated_root)
            maximum_step = max(maximum_step, abs(step))
        roots = updated
        if maximum_step < tolerance:
            return roots
    raise RuntimeError("Durand-Kerner iteration did not converge.")


def intersection(
    first: tuple[Fraction, Fraction, Fraction],
    second: tuple[Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction] | None:
    a1, b1, d1 = first
    a2, b2, d2 = second
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    x = (b1 * d2 - b2 * d1) / determinant
    y = (d1 * a2 - d2 * a1) / determinant
    return x, y


def bounded_region_count(lines: Sequence[tuple[Fraction, Fraction, Fraction]]) -> tuple[int, int]:
    incidences: dict[tuple[Fraction, Fraction], int] = {}
    for left in range(len(lines)):
        for right in range(left + 1, len(lines)):
            point = intersection(lines[left], lines[right])
            if point is not None:
                incidences[point] = incidences.get(point, 0) + 1
    # A point incident to m lines contributes m-1. Pair incidence count is C(m,2),
    # so recover m exactly from the small integer pair count.
    contribution = 0
    for pair_count in incidences.values():
        multiplicity = int((1 + math.isqrt(1 + 8 * pair_count)) // 2)
        if multiplicity * (multiplicity - 1) // 2 != pair_count:
            raise AssertionError("Intersection multiplicity is inconsistent.")
        contribution += multiplicity - 1
    beta = 1 - len(lines) + contribution
    return beta, len(incidences)


def regular_hexagon_edges() -> tuple[complex, ...]:
    omega = 0.5 + 0.5j * SQRT3
    vertices = tuple(omega**index for index in range(6))
    return tuple(vertices[index] - vertices[index - 1] for index in range(6))


def alpha_values(x: complex, y: complex) -> tuple[complex, ...]:
    return (
        1 + 0j,
        1 + x,
        x,
        -6 + 7 * x + 2 * y,
        y,
        3 - 2 * x + 3 * y,
    )


def equation_f2(x: complex, y: complex) -> complex:
    return (
        28 * x**3
        - 80 * x**2 * y
        - 4j * SQRT3 * x**2 * y
        - 82 * x**2
        + 26j * SQRT3 * x**2
        - 18 * x * y**2
        + 6j * SQRT3 * x * y**2
        - 27 * x * y
        - 33j * SQRT3 * x * y
        - 9 * x
        - 39j * SQRT3 * x
        - 12 * y**2
        + 24 * y
        + 36
    )


def equation_f3(x: complex, y: complex) -> complex:
    return (
        (-12 * SQRT3 - 12j) * y**2
        + (-13 * SQRT3 * x - 63j * x + 6 * SQRT3 + 54j) * y
        + (14 * SQRT3 * x**2 + 14j * x**2 - 33 * SQRT3 * x - 33j * x + 18 * SQRT3 + 18j)
    )


def solve_y(x: complex) -> complex:
    coefficient_a = -12 * SQRT3 - 12j
    coefficient_b = -13 * SQRT3 * x - 63j * x + 6 * SQRT3 + 54j
    coefficient_c = 14 * SQRT3 * x**2 + 14j * x**2 - 33 * SQRT3 * x - 33j * x + 18 * SQRT3 + 18j
    discriminant = coefficient_b**2 - 4 * coefficient_a * coefficient_c
    candidates = (
        (-coefficient_b + cmath.sqrt(discriminant)) / (2 * coefficient_a),
        (-coefficient_b - cmath.sqrt(discriminant)) / (2 * coefficient_a),
    )
    return min(candidates, key=lambda candidate: abs(equation_f2(x, candidate)) + abs(equation_f3(x, candidate)))


def adjacent_minors(values: Sequence[complex]) -> list[float]:
    return [
        float((values[index].conjugate() * values[(index + 1) % len(values)]).imag)
        for index in range(len(values))
    ]


def positive_winding(values: Sequence[complex]) -> float:
    total = 0.0
    for index in range(len(values)):
        angle = cmath.phase(values[(index + 1) % len(values)] / values[index])
        if angle <= 0:
            angle += TWO_PI
        total += angle
    return total


def orthogonality_residual(lambda_values: Sequence[complex], tilde_values: Sequence[complex]) -> float:
    rows_lambda = ([value.real for value in lambda_values], [value.imag for value in lambda_values])
    rows_tilde = ([value.real for value in tilde_values], [value.imag for value in tilde_values])
    return max(
        abs(sum(left * right for left, right in zip(row_left, row_right)))
        for row_left in rows_lambda
        for row_right in rows_tilde
    )


def critical_points() -> list[CriticalPoint]:
    roots = durand_kerner(QUINTIC)
    points = [CriticalPoint(x=root, y=solve_y(root)) for root in roots]
    return sorted(points, key=lambda point: (round(point.x.real, 12), round(point.x.imag, 12)))


def build_report() -> dict[str, object]:
    beta, intersection_count = bounded_region_count(LINES)
    edges = regular_hexagon_edges()
    solutions = []
    for index, point in enumerate(critical_points(), start=1):
        alphas = alpha_values(point.x, point.y)
        minimum_denominator = min(abs(value) for value in alphas)
        if minimum_denominator <= 1e-10:
            raise AssertionError("A retained root lies on the arrangement divisor.")
        # Conjugation reverses the orientation of the two-row real presentation;
        # it selects the positive orientation of the same real 2-plane lambda.
        lambda_values = tuple(value.conjugate() for value in alphas)
        tilde_values = tuple(edge / value for edge, value in zip(edges, alphas))
        lambda_minors = adjacent_minors(lambda_values)
        tilde_minors = adjacent_minors(tilde_values)
        solution = {
            "id": f"B3-{index:02d}",
            "projective_chart": {"a1": 1, "a2": complex_record(point.x), "a3": complex_record(point.y)},
            "quintic_residual": abs(poly_eval(QUINTIC, point.x)),
            "critical_residual_f2": abs(equation_f2(point.x, point.y)),
            "critical_residual_f3": abs(equation_f3(point.x, point.y)),
            "minimum_arrangement_denominator": minimum_denominator,
            "orthogonality_residual": orthogonality_residual(lambda_values, tilde_values),
            "lambda_adjacent_minors": lambda_minors,
            "tilde_lambda_adjacent_minors": tilde_minors,
            "lambda_winding_over_pi": positive_winding(lambda_values) / math.pi,
            "tilde_lambda_winding_over_pi": positive_winding(tilde_values) / math.pi,
            "pair_status": "M_PLUS_SIGN_AND_ORTHOGONALITY_CHECKED_NUMERICALLY",
            "internal_t_embedding_reconstruction": "NOT_PERFORMED",
            "rigid_deployment_status": "NOT_ASSESSED",
            "manufacturability_status": "NOT_ASSESSED",
        }
        solutions.append(solution)
    return {
        "schema_version": "1.0.0",
        "replication_id": "VGSE-B3-REGULAR-HEXAGON-001",
        "source": {
            "title": "Amplituhedra and Origami, I: Tree Level",
            "author": "Pavel Galashin",
            "author_pdf_date": "2026-06-03",
            "author_pdf_sha256": "e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de",
            "target": "Appendix B, Example B.1, Proposition B.2, Example B.3, Figure 16",
        },
        "fixture": {
            "k": 3,
            "n": 6,
            "C": C_MATRIX,
            "kami_boundary": "regular_hexagon_unit_circumradius",
            "projectivized_lines": [
                "x=-1", "x=0", "7x+2y=6", "y=0", "-2x+3y=-3"
            ],
        },
        "arrangement": {
            "distinct_finite_intersections": intersection_count,
            "bounded_region_count_beta": beta,
            "expected_beta": 5,
        },
        "algebraic_solution_count": len(solutions),
        "solutions": solutions,
        "claim_boundary": {
            "algebraic_branch_count_replicated": len(solutions) == beta == 5,
            "real_t_embedding_geometry_rendered": False,
            "continuous_rigid_foldability_established": False,
            "finite_thickness_structure_established": False,
            "manufacturable_product_established": False,
            "commercial_claim_authorized": False,
        },
    }


def validate_report(report: dict[str, object]) -> None:
    arrangement = report["arrangement"]
    assert isinstance(arrangement, dict)
    assert arrangement["bounded_region_count_beta"] == 5
    assert report["algebraic_solution_count"] == 5
    for solution in report["solutions"]:
        assert solution["quintic_residual"] < 5e-10
        assert solution["critical_residual_f2"] < 5e-10
        assert solution["critical_residual_f3"] < 5e-10
        assert solution["minimum_arrangement_denominator"] > 1e-6
        assert solution["orthogonality_residual"] < 5e-10
        assert min(solution["lambda_adjacent_minors"]) > 1e-8
        assert min(solution["tilde_lambda_adjacent_minors"]) > 1e-8
        assert abs(solution["lambda_winding_over_pi"] - 2.0) < 1e-10
        assert abs(solution["tilde_lambda_winding_over_pi"] - 4.0) < 1e-10


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    arguments = parser.parse_args()
    report = build_report()
    if arguments.check:
        validate_report(report)
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

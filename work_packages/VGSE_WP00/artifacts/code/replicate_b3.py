#!/usr/bin/env python3
"""Replicate the algebraic boundary data for Galashin Figure 16.

The source-vector boundary is extracted from the pinned 2026-06-03 PDF. The
boundary is rounded to one micro-point and traversed counterclockwise from the
source anchor. The critical equations and divisor-filtered quintic were derived
with exact rational/Gaussian-integer elimination and are replayed here with only
the Python standard library.

This script produces algebraic witnesses and pair-level sign checks. It does
not reconstruct the five internal planar drawings from the witnesses.
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

TWO_PI = 2 * math.pi
C_MATRIX = (
    (1, 1, 0, -6, 0, 3),
    (0, 1, 1, 7, 0, -2),
    (0, 0, 0, 2, 1, 3),
)
LINES = (
    (Fraction(1), Fraction(0), Fraction(1)),
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(7), Fraction(2), Fraction(-6)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(-2), Fraction(3), Fraction(3)),
)

# Figure 16 source-vector boundary in right-handed coordinates. Source order is
# clockwise. The canonical algebraic labeling keeps the first point fixed and
# traverses the same polygon counterclockwise.
SOURCE_BOUNDARY_CLOCKWISE = (
    (0.0, 0.0),
    (34.129578, 20.239700),
    (68.854401, 0.992180),
    (69.251343, -38.693344),
    (34.923126, -39.288589),
    (0.595245, -39.685532),
)
BOUNDARY = (
    (0.0, 0.0),
    (0.595245, -39.685532),
    (34.923126, -39.288589),
    (69.251343, -38.693344),
    (68.854401, 0.992180),
    (34.129578, 20.239700),
)

# Primitive Gaussian-integer coefficients, descending powers of x.
QUINTIC = (
    complex(483540693892620000, -264313923428829400),
    complex(1828863333844625820, 2216795100985993022),
    complex(-4290971821226241732, 3605280657884124497),
    complex(-2698133932258548966, -5029360426989542682),
    complex(2775911427357818274, -629469832931420958),
    complex(-11773047226564512, 509002207288521984),
)

# Gaussian-integer coefficients for the two cleared chart equations.
F2_COEFF = {
    (3, 1): complex(483371280, -272241536),
    (2, 2): complex(-1453484991, 732395948),
    (2, 1): complex(-981619989, 1336408964),
    (1, 3): complex(-209538756, 235731534),
    (1, 2): complex(-1024288314, -413721164),
    (1, 1): complex(-808398486, -963764106),
    (0, 3): complex(-205967286, -2381658),
    (0, 2): complex(411934572, 4763316),
    (0, 1): complex(617901858, 7144974),
}
F3_COEFF = {
    (4, 0): complex(1852396, -185199112),
    (3, 1): complex(-291094055, 358823616),
    (3, 0): complex(-2513966, 251341652),
    (2, 2): complex(-1587096, 119056578),
    (2, 1): complex(-12500915, 85786890),
    (2, 0): complex(-1984710, 198427620),
    (1, 2): complex(-1587096, 119056578),
    (1, 1): complex(278593140, -273036726),
    (1, 0): complex(2381652, -238113144),
}
DIVISOR_FACTORS = {
    "x^3": {"factor": "x", "arrangement_forms": ["alpha_3"]},
    "(x+1)^3": {"factor": "x+1", "arrangement_forms": ["alpha_2"]},
    "2x-3": {
        "factor": "2*x-3",
        "companion_y": "0",
        "arrangement_forms": ["alpha_5", "alpha_6"],
    },
    "7x-6": {
        "factor": "7*x-6",
        "companion_y": "0",
        "arrangement_forms": ["alpha_4", "alpha_5"],
    },
    "25x-24": {
        "factor": "25*x-24",
        "companion_y": "-9/25",
        "arrangement_forms": ["alpha_4", "alpha_6"],
    },
}


@dataclass(frozen=True)
class Point:
    x: complex
    y: complex


def complex_record(value: complex) -> dict[str, float]:
    return {"re": float(value.real), "im": float(value.imag)}


def poly_eval(coefficients: Sequence[complex], value: complex) -> complex:
    result = 0j
    for coefficient in coefficients:
        result = result * value + coefficient
    return result


def bivariate_eval(
    coefficients: dict[tuple[int, int], complex], x_value: complex, y_value: complex
) -> complex:
    return sum(
        coefficient * x_value**x_degree * y_value**y_degree
        for (x_degree, y_degree), coefficient in coefficients.items()
    )


def durand_kerner(
    coefficients: Sequence[complex], tolerance: float = 1e-13, max_iterations: int = 600
) -> list[complex]:
    degree = len(coefficients) - 1
    monic = [coefficient / coefficients[0] for coefficient in coefficients]
    radius = 1 + max(abs(coefficient) for coefficient in monic[1:])
    roots = [
        0.45 * radius * cmath.exp(2j * math.pi * (index + 0.173) / degree)
        for index in range(degree)
    ]
    for _ in range(max_iterations):
        updated = []
        maximum_step = 0.0
        for index, root in enumerate(roots):
            denominator = 1 + 0j
            for other_index, other_root in enumerate(roots):
                if index != other_index:
                    denominator *= root - other_root
            if abs(denominator) < 1e-30:
                raise RuntimeError("Durand-Kerner roots collided.")
            step = poly_eval(monic, root) / denominator
            updated.append(root - step)
            maximum_step = max(maximum_step, abs(step))
        roots = updated
        if maximum_step < tolerance:
            return roots
    raise RuntimeError("Durand-Kerner did not converge.")


def intersection(
    first: tuple[Fraction, Fraction, Fraction],
    second: tuple[Fraction, Fraction, Fraction],
) -> tuple[Fraction, Fraction] | None:
    a, b, d = first
    other_a, other_b, other_d = second
    determinant = a * other_b - other_a * b
    if determinant == 0:
        return None
    return (
        (b * other_d - other_b * d) / determinant,
        (d * other_a - other_d * a) / determinant,
    )


def bounded_region_count(
    lines: Sequence[tuple[Fraction, Fraction, Fraction]],
) -> tuple[int, int]:
    incidences: dict[tuple[Fraction, Fraction], int] = {}
    for left in range(len(lines)):
        for right in range(left + 1, len(lines)):
            point = intersection(lines[left], lines[right])
            if point is not None:
                incidences[point] = incidences.get(point, 0) + 1
    contribution = 0
    for pair_count in incidences.values():
        multiplicity = (1 + math.isqrt(1 + 8 * pair_count)) // 2
        if multiplicity * (multiplicity - 1) // 2 != pair_count:
            raise AssertionError("Intersection multiplicity is inconsistent.")
        contribution += multiplicity - 1
    return 1 - len(lines) + contribution, len(incidences)


def boundary_edges(boundary: Sequence[tuple[float, float]]) -> tuple[complex, ...]:
    return tuple(
        complex(
            boundary[index][0] - boundary[index - 1][0],
            boundary[index][1] - boundary[index - 1][1],
        )
        for index in range(len(boundary))
    )


def alpha_values(x_value: complex, y_value: complex) -> tuple[complex, ...]:
    return (
        1 + 0j,
        1 + x_value,
        x_value,
        -6 + 7 * x_value + 2 * y_value,
        y_value,
        3 - 2 * x_value + 3 * y_value,
    )


def solve_y(x_value: complex) -> complex:
    # F3/x = A*y^2+B*y+C for retained roots, all of which have x != 0.
    coefficient_a = F3_COEFF[(2, 2)] * x_value + F3_COEFF[(1, 2)]
    coefficient_b = (
        F3_COEFF[(3, 1)] * x_value**2
        + F3_COEFF[(2, 1)] * x_value
        + F3_COEFF[(1, 1)]
    )
    coefficient_c = (
        F3_COEFF[(4, 0)] * x_value**3
        + F3_COEFF[(3, 0)] * x_value**2
        + F3_COEFF[(2, 0)] * x_value
        + F3_COEFF[(1, 0)]
    )
    discriminant = coefficient_b**2 - 4 * coefficient_a * coefficient_c
    candidates = (
        (-coefficient_b + cmath.sqrt(discriminant)) / (2 * coefficient_a),
        (-coefficient_b - cmath.sqrt(discriminant)) / (2 * coefficient_a),
    )
    return min(
        candidates,
        key=lambda candidate: abs(bivariate_eval(F2_COEFF, x_value, candidate))
        + abs(bivariate_eval(F3_COEFF, x_value, candidate)),
    )


def adjacent_minors(values: Sequence[complex]) -> list[float]:
    return [
        float((values[index].conjugate() * values[(index + 1) % len(values)]).imag)
        for index in range(len(values))
    ]


def positive_winding(values: Sequence[complex]) -> float:
    total = 0.0
    for index, value in enumerate(values):
        angle = cmath.phase(values[(index + 1) % len(values)] / value)
        if angle <= 0:
            angle += TWO_PI
        total += angle
    return total


def orthogonality_residual(
    lambda_values: Sequence[complex], tilde_values: Sequence[complex]
) -> float:
    rows = (
        [value.real for value in lambda_values],
        [value.imag for value in lambda_values],
    )
    tilde_rows = (
        [value.real for value in tilde_values],
        [value.imag for value in tilde_values],
    )
    return max(
        abs(sum(left * right for left, right in zip(row, tilde_row)))
        for row in rows
        for tilde_row in tilde_rows
    )


def critical_points() -> list[Point]:
    points = [Point(x=root, y=solve_y(root)) for root in durand_kerner(QUINTIC)]
    return sorted(points, key=lambda point: (round(point.x.real, 12), round(point.x.imag, 12)))


def build_report() -> dict[str, object]:
    beta, intersection_count = bounded_region_count(LINES)
    edges = boundary_edges(BOUNDARY)
    solutions = []
    for index, point in enumerate(critical_points(), start=1):
        alphas = alpha_values(point.x, point.y)
        minimum_denominator = min(abs(value) for value in alphas)
        if minimum_denominator <= 1e-10:
            raise AssertionError("A retained witness lies on the arrangement divisor.")
        lambda_values = tuple(value.conjugate() for value in alphas)
        tilde_values = tuple(edge / value for edge, value in zip(edges, alphas))
        solutions.append(
            {
                "id": f"FIG16-B3-{index:02d}",
                "projective_chart": {
                    "a1": 1,
                    "a2": complex_record(point.x),
                    "a3": complex_record(point.y),
                },
                "quintic_residual": abs(poly_eval(QUINTIC, point.x))
                / max(abs(coefficient) for coefficient in QUINTIC),
                "critical_residual_f2_scaled": abs(
                    bivariate_eval(F2_COEFF, point.x, point.y)
                )
                / max(abs(coefficient) for coefficient in F2_COEFF.values()),
                "critical_residual_f3_scaled": abs(
                    bivariate_eval(F3_COEFF, point.x, point.y)
                )
                / max(abs(coefficient) for coefficient in F3_COEFF.values()),
                "minimum_arrangement_denominator": minimum_denominator,
                "orthogonality_residual": orthogonality_residual(
                    lambda_values, tilde_values
                ),
                "lambda_adjacent_minors": adjacent_minors(lambda_values),
                "tilde_lambda_adjacent_minors": adjacent_minors(tilde_values),
                "lambda_winding_over_pi": positive_winding(lambda_values) / math.pi,
                "tilde_lambda_winding_over_pi": positive_winding(tilde_values) / math.pi,
                "pair_status": "M_PLUS_SIGN_AND_ORTHOGONALITY_CHECKED_NUMERICALLY",
                "pattern_correspondence": "NOT_RECONSTRUCTED",
                "rigid_deployment_status": "NOT_ASSESSED",
                "manufacturability_status": "NOT_ASSESSED",
            }
        )
    return {
        "schema_version": "1.1.0",
        "replication_id": "VGSE-B3-FIGURE16-BOUNDARY-001",
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
            "kami_boundary_source": "Figure 16 PDF vector paths rounded to 1e-6 PDF point after translation and y-axis inversion",
            "source_boundary_clockwise": SOURCE_BOUNDARY_CLOCKWISE,
            "canonical_boundary_labeling": {
                "anchor": "source boundary vertex 0",
                "orientation": "counterclockwise",
                "vertices": BOUNDARY,
            },
            "projectivized_lines": [
                "x=-1",
                "x=0",
                "7x+2y=6",
                "y=0",
                "-2x+3y=-3",
            ],
        },
        "elimination": {
            "unsaturated_resultant_factor_degrees": [1, 1, 1, 3, 3, 5],
            "excluded_divisor_factors": DIVISOR_FACTORS,
            "retained_factor_degree": 5,
        },
        "arrangement": {
            "distinct_finite_intersections": intersection_count,
            "bounded_region_count_beta": beta,
            "expected_beta": 5,
        },
        "algebraic_witness_count": len(solutions),
        "solutions": solutions,
        "claim_boundary": {
            "exact_arrangement_count_replicated": beta == 5,
            "source_boundary_algebraic_witness_replay_complete": len(solutions) == 5,
            "source_vector_five_pattern_geometry_replicated_in_separate_artifact": True,
            "algebraic_witness_to_pattern_correspondence_reconstructed": False,
            "continuous_rigid_foldability_established": False,
            "collision_free_deployment_established": False,
            "finite_thickness_structure_established": False,
            "manufacturable_product_established": False,
            "commercial_claim_authorized": False,
        },
    }


def validate_report(report: dict[str, object]) -> None:
    arrangement = report["arrangement"]
    assert isinstance(arrangement, dict)
    assert arrangement["bounded_region_count_beta"] == 5
    assert report["algebraic_witness_count"] == 5
    for solution in report["solutions"]:
        assert solution["quintic_residual"] < 2e-12
        assert solution["critical_residual_f2_scaled"] < 2e-12
        assert solution["critical_residual_f3_scaled"] < 2e-12
        assert solution["minimum_arrangement_denominator"] > 1e-6
        assert solution["orthogonality_residual"] < 5e-10
        assert min(solution["lambda_adjacent_minors"]) > 1e-8
        assert min(solution["tilde_lambda_adjacent_minors"]) > 1e-8
        assert abs(solution["lambda_winding_over_pi"] - 2.0) < 1e-10
        assert abs(solution["tilde_lambda_winding_over_pi"] - 4.0) < 1e-10
    claim_boundary = report["claim_boundary"]
    assert not claim_boundary["algebraic_witness_to_pattern_correspondence_reconstructed"]
    assert not claim_boundary["commercial_claim_authorized"]


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

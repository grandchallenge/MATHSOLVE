from __future__ import annotations

from typing import Sequence

Point = tuple[float, float]
ComplexMatrix = list[list[complex]]
C_MATRIX = (
    (1.0, 1.0, 0.0, -6.0, 0.0, 3.0),
    (0.0, 1.0, 1.0, 7.0, 0.0, -2.0),
    (0.0, 0.0, 0.0, 2.0, 1.0, 3.0),
)
CANONICAL_SOURCE_BOUNDARY_INDICES = (0, 5, 4, 3, 2, 1)
POINT_DIGITS = 4


def complex_record(value: complex) -> dict[str, float]:
    return {"re": float(value.real), "im": float(value.imag)}


def point_key(point: Sequence[float]) -> Point:
    return round(float(point[0]), POINT_DIGITS), round(float(point[1]), POINT_DIGITS)


def edge_key(left: Sequence[float], right: Sequence[float]) -> tuple[Point, Point]:
    return tuple(sorted((point_key(left), point_key(right))))  # type: ignore[return-value]


def polygon_area(points: Sequence[complex]) -> float:
    return 0.5 * sum(
        (points[index].conjugate() * points[(index + 1) % len(points)]).imag
        for index in range(len(points))
    )


def determinant_3(columns: tuple[int, int, int]) -> float:
    a, b, c = columns
    matrix = [[C_MATRIX[row][column] for column in (a, b, c)] for row in range(3)]
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )

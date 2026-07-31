from __future__ import annotations

import math
from collections import defaultdict, deque
from typing import Any, Sequence

from b3_common import ComplexMatrix, Point


def solve_linear(matrix: ComplexMatrix, rhs: Sequence[complex]) -> tuple[list[complex], float]:
    """Solve an overdetermined full-column-rank system through normal equations."""
    row_count = len(matrix)
    column_count = len(matrix[0])
    normal = [[0j for _ in range(column_count)] for _ in range(column_count)]
    target = [0j for _ in range(column_count)]
    for row in range(row_count):
        for left in range(column_count):
            conjugate = matrix[row][left].conjugate()
            target[left] += conjugate * rhs[row]
            for right in range(column_count):
                normal[left][right] += conjugate * matrix[row][right]
    augmented = [normal[row][:] + [target[row]] for row in range(column_count)]
    for column in range(column_count):
        pivot = max(range(column, column_count), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-18:
            raise AssertionError("Discrete holomorphic system is rank deficient.")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(column_count):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(augmented[row], augmented[column])
            ]
    solution = [augmented[row][-1] for row in range(column_count)]
    residual = math.sqrt(sum(
        abs(sum(coefficient * value for coefficient, value in zip(row, solution)) - expected) ** 2
        for row, expected in zip(matrix, rhs)
    ))
    return solution, residual


def extensions(
    colors: dict[str, str], edges: list[dict[str, Any]], zeta: Sequence[complex],
    zeta_tilde: Sequence[complex],
) -> tuple[dict[str, complex], dict[str, complex], float, float]:
    white_vertices = sorted(vertex for vertex, color in colors.items() if color == "white")
    black_vertices = sorted(vertex for vertex, color in colors.items() if color == "black")
    white_index = {vertex: index for index, vertex in enumerate(white_vertices)}
    black_index = {vertex: index for index, vertex in enumerate(black_vertices)}
    partial_f = [(-1) ** index * zeta[index] for index in range(6)]
    partial_tilde = [(-1) ** index * zeta_tilde[index] for index in range(6)]
    boundary_edges = {edge["index"]: edge for edge in edges if edge["boundary"]}

    matrix: ComplexMatrix = []
    rhs: list[complex] = []
    for black in sorted(vertex for vertex in black_vertices if not vertex.startswith("U")):
        row = [0j] * len(white_vertices)
        for edge in edges:
            if edge["black"] == black:
                row[white_index[edge["white"]]] += edge["sign"] * edge["weight"]
        matrix.append(row)
        rhs.append(0j)
    for index in range(1, 7):
        edge = boundary_edges[index]
        row = [0j] * len(white_vertices)
        boundary_vertex = f"U{index}"
        kasteleyn = edge["sign"] * edge["weight"]
        if colors[boundary_vertex] == "white":
            row[white_index[boundary_vertex]] = -1
        else:
            row[white_index[edge["owner"]]] = -kasteleyn
        matrix.append(row)
        rhs.append(partial_f[index - 1])
    values, f_residual = solve_linear(matrix, rhs)
    f_values = {vertex: values[index] for vertex, index in white_index.items()}

    matrix = []
    rhs = []
    for white in sorted(vertex for vertex in white_vertices if not vertex.startswith("U")):
        row = [0j] * len(black_vertices)
        for edge in edges:
            if edge["white"] == white:
                row[black_index[edge["black"]]] += edge["sign"] * edge["weight"]
        matrix.append(row)
        rhs.append(0j)
    for index in range(1, 7):
        edge = boundary_edges[index]
        row = [0j] * len(black_vertices)
        boundary_vertex = f"U{index}"
        kasteleyn = edge["sign"] * edge["weight"]
        if colors[boundary_vertex] == "black":
            row[black_index[boundary_vertex]] = 1
        else:
            row[black_index[edge["owner"]]] = -kasteleyn
        matrix.append(row)
        rhs.append(partial_tilde[index - 1])
    values, tilde_residual = solve_linear(matrix, rhs)
    tilde_values = {vertex: values[index] for vertex, index in black_index.items()}
    return f_values, tilde_values, f_residual, tilde_residual


def primitive(
    edges: list[dict[str, Any]], f_values: dict[str, complex], tilde_values: dict[str, complex],
) -> tuple[dict[Point, complex], float]:
    adjacency: dict[Point, list[tuple[Point, complex]]] = defaultdict(list)
    for edge in edges:
        start, end = edge["oriented_dual"]
        increment = (
            f_values[edge["white"]] * edge["sign"] * edge["weight"]
            * tilde_values[edge["black"]]
        )
        adjacency[start].append((end, increment))
        adjacency[end].append((start, -increment))
    root = next(iter(adjacency))
    positions = {root: 0j}
    queue = deque([root])
    closure_residuals: list[float] = []
    while queue:
        current = queue.popleft()
        for neighbor, increment in adjacency[current]:
            candidate = positions[current] + increment
            if neighbor not in positions:
                positions[neighbor] = candidate
                queue.append(neighbor)
            else:
                closure_residuals.append(abs(positions[neighbor] - candidate))
    return positions, max(closure_residuals or [0.0])

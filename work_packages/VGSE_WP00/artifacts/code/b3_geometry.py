from __future__ import annotations

import math
from collections import defaultdict
from typing import Any, Sequence

from b3_common import Point, complex_record, point_key, polygon_area


def convex(points: Sequence[complex], tolerance: float = 1e-9) -> bool:
    signs: list[int] = []
    for index in range(len(points)):
        first = points[index] - points[index - 1]
        second = points[(index + 1) % len(points)] - points[index]
        cross = (first.conjugate() * second).imag
        if abs(cross) <= tolerance:
            return False
        signs.append(1 if cross > 0 else -1)
    return all(sign == signs[0] for sign in signs)


def interior_angle(points: Sequence[complex], index: int) -> float:
    vertex = points[index]
    left = points[index - 1] - vertex
    right = points[(index + 1) % len(points)] - vertex
    cosine = (left.real * right.real + left.imag * right.imag) / (abs(left) * abs(right))
    return math.acos(max(-1.0, min(1.0, cosine)))


def validate_geometry(
    source: dict[str, Any], boundary: Sequence[complex], positions: dict[Point, complex],
) -> tuple[list[dict[str, Any]], dict[str, float]]:
    pattern = source["patterns"][0]
    boundary_keys = {point_key((point.real, point.imag)) for point in boundary}
    angle_sums: dict[Point, dict[str, float]] = defaultdict(
        lambda: {"black": 0.0, "white": 0.0}
    )
    generated_faces = []
    face_area = 0.0
    minimum_edge = math.inf
    for face in pattern["faces"]:
        points = [positions[point_key(point)] for point in face["vertices"]]
        if not convex(points):
            raise AssertionError(f"Generated face {face['face_id']} is not strictly convex.")
        face_area += abs(polygon_area(points))
        for index, point in enumerate(points):
            minimum_edge = min(minimum_edge, abs(points[(index + 1) % len(points)] - point))
            angle_sums[point_key((point.real, point.imag))][face["color"]] += interior_angle(points, index)
        generated_faces.append({
            "face_id": face["face_id"], "color": face["color"],
            "vertices": [complex_record(point) for point in points],
        })
    interior_vertices = set(angle_sums) - boundary_keys
    kawasaki = max(
        abs(angle_sums[vertex][color] - math.pi)
        for vertex in interior_vertices for color in ("black", "white")
    )
    boundary_margin = min(
        min(angle_sums[vertex][color], math.pi - angle_sums[vertex][color])
        for vertex in boundary_keys for color in ("black", "white")
    )
    boundary_area = abs(polygon_area(boundary))
    return generated_faces, {
        "face_count": float(len(generated_faces)),
        "minimum_edge_length": minimum_edge,
        "maximum_kawasaki_residual": kawasaki,
        "minimum_boundary_angle_margin": boundary_margin,
        "area_partition_residual": abs(face_area - boundary_area),
    }


def svg_document(pattern: dict[str, Any], width: int = 420, height: int = 300) -> str:
    faces = pattern["faces"]
    points = [complex(vertex["re"], vertex["im"]) for face in faces for vertex in face["vertices"]]
    minimum_x = min(point.real for point in points)
    maximum_x = max(point.real for point in points)
    minimum_y = min(point.imag for point in points)
    maximum_y = max(point.imag for point in points)
    margin = 20.0
    scale = min(
        (width - 2 * margin) / (maximum_x - minimum_x),
        (height - 2 * margin) / (maximum_y - minimum_y),
    )

    def transform(point: complex) -> tuple[float, float]:
        return (
            margin + (point.real - minimum_x) * scale,
            height - margin - (point.imag - minimum_y) * scale,
        )

    polygons = []
    for face in faces:
        vertices = [complex(vertex["re"], vertex["im"]) for vertex in face["vertices"]]
        serialized = " ".join(f"{x:.3f},{y:.3f}" for x, y in map(transform, vertices))
        fill = "#242424" if face["color"] == "black" else "#e6e6e6"
        polygons.append(
            f'<polygon points="{serialized}" fill="{fill}" stroke="#4c4c4c" stroke-width="1.2"/>'
        )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
        '<rect width="100%" height="100%" fill="white"/>\n'
        + "\n".join(polygons)
        + f'\n<text x="20" y="24" font-family="sans-serif" font-size="16">{pattern["pattern_id"]}</text>\n'
        + '</svg>\n'
    )

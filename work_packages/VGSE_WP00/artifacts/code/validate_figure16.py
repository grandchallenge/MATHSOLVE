#!/usr/bin/env python3
"""Validate and render the source-vector replication of Galashin Figure 16.

The fixture reproduces vector paths embedded in the pinned PDF. The checks
cover the planar drawings and the weighted planar graph reconstructed from each
drawing. They do not reconstruct the drawings from the master-function roots,
verify that the reconstructed graph has boundary measurement C, prove a rigid
folding motion, or establish a product.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any, Sequence

Point = tuple[float, float]
ANGLE_TOLERANCE = 4e-2
GEOMETRY_TOLERANCE = 2e-3


def as_points(values: Sequence[Sequence[float]]) -> list[Point]:
    return [(float(value[0]), float(value[1])) for value in values]


def signed_area(points: Sequence[Point]) -> float:
    return 0.5 * sum(
        points[index][0] * points[(index + 1) % len(points)][1]
        - points[(index + 1) % len(points)][0] * points[index][1]
        for index in range(len(points))
    )


def cross(left: Point, middle: Point, right: Point) -> float:
    return (middle[0] - left[0]) * (right[1] - middle[1]) - (
        middle[1] - left[1]
    ) * (right[0] - middle[0])


def strictly_convex(points: Sequence[Point], tolerance: float = 1e-7) -> bool:
    signs = []
    for index in range(len(points)):
        value = cross(points[index - 1], points[index], points[(index + 1) % len(points)])
        if abs(value) <= tolerance:
            return False
        signs.append(math.copysign(1.0, value))
    return all(sign == signs[0] for sign in signs)


def point_key(point: Point) -> tuple[float, float]:
    return round(point[0], 4), round(point[1], 4)


def edge_key(left: Point, right: Point) -> tuple[tuple[float, float], tuple[float, float]]:
    return tuple(sorted((point_key(left), point_key(right))))  # type: ignore[return-value]


def interior_angle(points: Sequence[Point], index: int) -> float:
    vertex = points[index]
    previous = points[index - 1]
    following = points[(index + 1) % len(points)]
    first = (previous[0] - vertex[0], previous[1] - vertex[1])
    second = (following[0] - vertex[0], following[1] - vertex[1])
    norm = math.hypot(*first) * math.hypot(*second)
    if norm == 0:
        raise AssertionError("Zero-length polygon edge.")
    cosine = max(
        -1.0,
        min(1.0, (first[0] * second[0] + first[1] * second[1]) / norm),
    )
    return math.acos(cosine)


def cyclic_distance(first: Sequence[Point], second: Sequence[Point]) -> float:
    if len(first) != len(second):
        return math.inf
    candidates = []
    for reverse in (False, True):
        sequence = list(reversed(second)) if reverse else list(second)
        for shift in range(len(sequence)):
            rotated = sequence[shift:] + sequence[:shift]
            dx = first[0][0] - rotated[0][0]
            dy = first[0][1] - rotated[0][1]
            candidates.append(
                max(
                    math.dist(left, (right[0] + dx, right[1] + dy))
                    for left, right in zip(first, rotated)
                )
            )
    return min(candidates)


def graph_signature(
    faces: Sequence[dict[str, Any]],
    edge_owners: dict[tuple[tuple[float, float], tuple[float, float]], list[str]],
    boundary_edges: set[tuple[tuple[float, float], tuple[float, float]]],
) -> dict[str, Any]:
    colors = {face["face_id"]: face["color"] for face in faces}
    internal_edges = sorted(
        tuple(sorted(owners))
        for edge, owners in edge_owners.items()
        if len(owners) == 2
    )
    boundary_owners = sorted(
        owners[0] for edge, owners in edge_owners.items() if edge in boundary_edges
    )
    colored_internal_edges = sorted(
        f"{colors[left][0]}:{left}|{colors[right][0]}:{right}"
        for left, right in internal_edges
    )
    return {
        "interior_vertex_count": len(faces),
        "boundary_vertex_count": len(boundary_edges),
        "primal_edge_count": len(internal_edges) + len(boundary_edges),
        "internal_edge_count": len(internal_edges),
        "boundary_edge_count": len(boundary_edges),
        "colored_internal_edges": colored_internal_edges,
        "boundary_edge_owner_multiset": boundary_owners,
    }


def validate_pattern(pattern: dict[str, Any]) -> dict[str, Any]:
    boundary = as_points(pattern["boundary"])
    faces = pattern["faces"]
    if len(boundary) != 6:
        raise AssertionError("The prescribed boundary must have six vertices.")
    if len(faces) != 8:
        raise AssertionError("Each source-vector pattern must have eight faces.")
    colors = [face["color"] for face in faces]
    if colors.count("black") != 4 or colors.count("white") != 4:
        raise AssertionError("Expected four black and four white faces.")
    if not strictly_convex(boundary):
        raise AssertionError("Boundary polygon is not strictly convex.")

    edge_counts: dict[
        tuple[tuple[float, float], tuple[float, float]], int
    ] = defaultdict(int)
    edge_owners: dict[
        tuple[tuple[float, float], tuple[float, float]], list[str]
    ] = defaultdict(list)
    angle_sums: dict[tuple[float, float], dict[str, float]] = defaultdict(
        lambda: {"black": 0.0, "white": 0.0}
    )
    face_area = 0.0
    minimum_edge = math.inf
    face_colors = {face["face_id"]: face["color"] for face in faces}
    for face in faces:
        points = as_points(face["vertices"])
        if len(points) < 3 or not strictly_convex(points):
            raise AssertionError(f"Nonconvex or degenerate face: {face['face_id']}")
        face_area += abs(signed_area(points))
        for index, left in enumerate(points):
            right = points[(index + 1) % len(points)]
            minimum_edge = min(minimum_edge, math.dist(left, right))
            edge = edge_key(left, right)
            edge_counts[edge] += 1
            edge_owners[edge].append(face["face_id"])
            angle_sums[point_key(left)][face["color"]] += interior_angle(points, index)

    boundary_edges = {
        edge_key(boundary[index], boundary[(index + 1) % len(boundary)])
        for index in range(6)
    }
    observed_boundary_edges = {edge for edge, count in edge_counts.items() if count == 1}
    if observed_boundary_edges != boundary_edges:
        raise AssertionError("Face union does not induce the recorded boundary.")
    if any(count not in (1, 2) for count in edge_counts.values()):
        raise AssertionError("An edge has invalid face incidence.")
    for owners in edge_owners.values():
        if len(owners) == 2 and {face_colors[owner] for owner in owners} != {
            "black",
            "white",
        }:
            raise AssertionError("An internal primal edge is not bipartite.")

    boundary_area = abs(signed_area(boundary))
    area_residual = abs(face_area - boundary_area)
    if area_residual > GEOMETRY_TOLERANCE:
        raise AssertionError(f"Face areas do not partition the boundary: {area_residual}")

    boundary_vertices = {point_key(point) for point in boundary}
    interior_vertices = sorted(set(angle_sums) - boundary_vertices)
    if len(interior_vertices) != 3:
        raise AssertionError(
            f"Expected three interior dual vertices, found {len(interior_vertices)}."
        )
    kawasaki_residual = 0.0
    for vertex in interior_vertices:
        for color in ("black", "white"):
            kawasaki_residual = max(
                kawasaki_residual, abs(angle_sums[vertex][color] - math.pi)
            )
    if kawasaki_residual > ANGLE_TOLERANCE:
        raise AssertionError(f"Kawasaki residual too large: {kawasaki_residual}")

    boundary_angle_margin = math.inf
    for vertex in boundary_vertices:
        for color in ("black", "white"):
            value = angle_sums[vertex][color]
            boundary_angle_margin = min(boundary_angle_margin, value, math.pi - value)
            if not (0.0 < value < math.pi):
                raise AssertionError("Boundary angle condition failed.")

    signature = graph_signature(faces, edge_owners, boundary_edges)
    return {
        "pattern_id": pattern["pattern_id"],
        "face_count": len(faces),
        "dual_vertex_count": len(angle_sums),
        "interior_dual_vertex_count": len(interior_vertices),
        "dual_edge_count": len(edge_counts),
        "minimum_edge_length": minimum_edge,
        "boundary_area": boundary_area,
        "face_area_sum": face_area,
        "area_partition_residual": area_residual,
        "maximum_kawasaki_color_sum_residual": kawasaki_residual,
        "minimum_boundary_angle_margin": boundary_angle_margin,
        "reconstructed_weighted_primal_graph": signature,
        "te1_nonzero_straight_edges": True,
        "te2_convex_oriented_faces": True,
        "te3_identity_gauge_for_reconstructed_geometric_weights": True,
        "te4_kawasaki_checked_at_pdf_precision": True,
        "te5_boundary_angles_checked": True,
        "injectivity_checked_by_simple_boundary_and_face_partition": True,
    }


def svg_document(pattern: dict[str, Any], width: int = 420, height: int = 300) -> str:
    boundary = as_points(pattern["boundary"])
    all_points = [
        point for face in pattern["faces"] for point in as_points(face["vertices"])
    ]
    min_x = min(point[0] for point in all_points)
    max_x = max(point[0] for point in all_points)
    min_y = min(point[1] for point in all_points)
    max_y = max(point[1] for point in all_points)
    margin = 20.0
    scale = min(
        (width - 2 * margin) / (max_x - min_x),
        (height - 2 * margin) / (max_y - min_y),
    )

    def transform(point: Point) -> tuple[float, float]:
        return (
            margin + (point[0] - min_x) * scale,
            height - margin - (point[1] - min_y) * scale,
        )

    polygons = []
    for face in pattern["faces"]:
        points = " ".join(
            f"{x:.3f},{y:.3f}"
            for x, y in map(transform, as_points(face["vertices"]))
        )
        fill = "#242424" if face["color"] == "black" else "#e6e6e6"
        polygons.append(
            f'<polygon points="{points}" fill="{fill}" stroke="#4c4c4c" stroke-width="1.2"/>'
        )
    boundary_points = " ".join(
        f"{x:.3f},{y:.3f}" for x, y in map(transform, boundary)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
        '<rect width="100%" height="100%" fill="white"/>\n'
        + "\n".join(polygons)
        + f'\n<polygon points="{boundary_points}" fill="none" stroke="#111" stroke-width="2"/>\n'
        + f'<text x="20" y="24" font-family="sans-serif" font-size="16">{pattern["pattern_id"]}</text>\n'
        + '</svg>\n'
    )


def build_report(fixture: dict[str, Any]) -> dict[str, Any]:
    patterns = fixture["patterns"]
    if len(patterns) != 5:
        raise AssertionError("Expected five Figure 16 patterns.")
    metrics = [validate_pattern(pattern) for pattern in patterns]
    reference_boundary = as_points(patterns[0]["boundary"])
    boundary_residual = max(
        cyclic_distance(reference_boundary, as_points(pattern["boundary"]))
        for pattern in patterns[1:]
    )
    if boundary_residual > GEOMETRY_TOLERANCE:
        raise AssertionError(f"Prescribed boundaries differ: {boundary_residual}")
    signatures = [metric["reconstructed_weighted_primal_graph"] for metric in metrics]
    topology_keys = [
        (signature["colored_internal_edges"], signature["boundary_edge_owner_multiset"])
        for signature in signatures
    ]
    if any(key != topology_keys[0] for key in topology_keys[1:]):
        raise AssertionError(
            "The five source drawings do not have the same reconstructed graph topology."
        )
    return {
        "schema_version": "1.1.0",
        "validation_id": "VGSE-FIG16-GEOMETRY-VALIDATION-001",
        "fixture_id": fixture["fixture_id"],
        "source": fixture["source"],
        "pattern_count": len(patterns),
        "maximum_common_boundary_residual": boundary_residual,
        "common_reconstructed_graph_topology": True,
        "patterns": metrics,
        "claim_boundary": {
            "source_vector_five_pattern_geometry_replicated": True,
            "source_vector_planar_geometry_checks_passed": True,
            "literature_identifies_drawings_as_t_embeddings": True,
            "full_t_embedding_correspondence_to_pinned_C_independently_verified": False,
            "algebraic_witness_to_pattern_correspondence_reconstructed": False,
            "continuous_rigid_foldability_established": False,
            "collision_free_deployment_established": False,
            "finite_thickness_structure_established": False,
            "manufacturable_product_established": False,
            "commercial_claim_authorized": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--svg-dir", type=Path)
    arguments = parser.parse_args()
    fixture = json.loads(arguments.fixture.read_text(encoding="utf-8"))
    report = build_report(fixture)
    if arguments.report:
        arguments.report.parent.mkdir(parents=True, exist_ok=True)
        arguments.report.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    if arguments.svg_dir:
        arguments.svg_dir.mkdir(parents=True, exist_ok=True)
        for pattern in fixture["patterns"]:
            (arguments.svg_dir / f"{pattern['pattern_id'].lower()}.svg").write_text(
                svg_document(pattern), encoding="utf-8"
            )
    if not arguments.report:
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

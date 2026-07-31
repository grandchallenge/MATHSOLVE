from __future__ import annotations

import itertools
import math
from collections import defaultdict
from typing import Any

from b3_common import (
    CANONICAL_SOURCE_BOUNDARY_INDICES, Point, determinant_3, edge_key, point_key, polygon_area
)


def load_graph(source: dict[str, Any], weights: dict[str, Any]) -> tuple[list[complex], dict[str, str], list[dict[str, Any]], dict[Point, str]]:
    pattern = source["patterns"][0]
    faces = {face["face_id"]: face for face in pattern["faces"]}
    colors = {face_id: face["color"] for face_id, face in faces.items()}
    source_boundary = [complex(*point) for point in pattern["boundary"]]
    boundary = [source_boundary[index] for index in CANONICAL_SOURCE_BOUNDARY_INDICES]

    edge_owners: dict[tuple[Point, Point], list[str]] = defaultdict(list)
    for face in pattern["faces"]:
        vertices = face["vertices"]
        for index, left in enumerate(vertices):
            right = vertices[(index + 1) % len(vertices)]
            edge_owners[edge_key(left, right)].append(face["face_id"])

    internal_fixture = weights["internal_edges"]
    edges: list[dict[str, Any]] = []
    for pair_name, record in internal_fixture.items():
        first, second = pair_name.split("|")
        shared = [edge for edge, owners in edge_owners.items() if set(owners) == {first, second}]
        if len(shared) != 1:
            raise AssertionError(f"Could not identify internal edge {pair_name}.")
        white = first if colors[first] == "white" else second
        black = second if white == first else first
        white_polygon = [complex(*point) for point in faces[white]["vertices"]]
        shared_key = shared[0]
        oriented: tuple[Point, Point] | None = None
        for index, left in enumerate(white_polygon):
            right = white_polygon[(index + 1) % len(white_polygon)]
            if edge_key((left.real, left.imag), (right.real, right.imag)) == shared_key:
                if polygon_area(white_polygon) > 0:
                    oriented = (point_key((right.real, right.imag)), point_key((left.real, left.imag)))
                else:
                    oriented = (point_key((left.real, left.imag)), point_key((right.real, right.imag)))
                break
        if oriented is None:
            raise AssertionError(f"Could not orient internal edge {pair_name}.")
        edges.append({
            "id": pair_name, "white": white, "black": black, "dual": shared_key,
            "oriented_dual": oriented, "weight": float(record["weight"]),
            "sign": int(record["kasteleyn_sign"]), "boundary": False,
        })

    boundary_fixture = weights["boundary_edges"]
    for index in range(1, 7):
        previous = boundary[index - 2]
        current = boundary[index - 1]
        shared_key = edge_key((previous.real, previous.imag), (current.real, current.imag))
        owners = edge_owners[shared_key]
        if len(owners) != 1:
            raise AssertionError(f"Boundary edge B{index} has invalid incidence.")
        owner = owners[0]
        record = boundary_fixture[f"B{index}"]
        if owner != record["owner"]:
            raise AssertionError(f"Boundary owner mismatch for B{index}.")
        boundary_vertex = f"U{index}"
        colors[boundary_vertex] = "black" if colors[owner] == "white" else "white"
        white = owner if colors[owner] == "white" else boundary_vertex
        black = boundary_vertex if colors[owner] == "white" else owner
        oriented = (
            (point_key((current.real, current.imag)), point_key((previous.real, previous.imag)))
            if colors[boundary_vertex] == "black"
            else (point_key((previous.real, previous.imag)), point_key((current.real, current.imag)))
        )
        edges.append({
            "id": f"B{index}", "index": index, "owner": owner, "white": white,
            "black": black, "dual": shared_key, "oriented_dual": oriented,
            "weight": float(record["weight"]), "sign": int(record["kasteleyn_sign"]),
            "boundary": True,
        })

    incident_faces: dict[Point, set[str]] = defaultdict(set)
    for face in pattern["faces"]:
        for point in face["vertices"]:
            incident_faces[point_key(point)].add(face["face_id"])
    labels: dict[Point, str] = {}
    boundary_keys = {point_key((point.real, point.imag)) for point in boundary}
    for index, point in enumerate(boundary, start=1):
        labels[point_key((point.real, point.imag))] = f"B{index}"
    for point_id, owners in incident_faces.items():
        if point_id not in boundary_keys:
            labels[point_id] = "I:" + "+".join(sorted(owners))
    return boundary, colors, edges, labels


def enumerate_matchings(colors: dict[str, str], edges: list[dict[str, Any]]) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    interior = sorted(vertex for vertex in colors if not vertex.startswith("U"))
    incident = {
        vertex: [index for index, edge in enumerate(edges) if vertex in (edge["white"], edge["black"])]
        for vertex in colors
    }
    selected: list[tuple[int, ...]] = []

    def recurse(covered: set[str], chosen: list[int], used_boundary: set[str]) -> None:
        if len(covered) == len(interior):
            selected.append(tuple(chosen))
            return
        vertex = next(item for item in interior if item not in covered)
        for edge_index in incident[vertex]:
            edge = edges[edge_index]
            other = edge["black"] if vertex == edge["white"] else edge["white"]
            if other in interior and other in covered:
                continue
            if other.startswith("U") and other in used_boundary:
                continue
            next_covered = set(covered)
            next_covered.add(vertex)
            next_boundary = set(used_boundary)
            if other in interior:
                next_covered.add(other)
            else:
                next_boundary.add(other)
            recurse(next_covered, chosen + [edge_index], next_boundary)

    recurse(set(), [], set())
    records = []
    for matching in selected:
        used = {
            vertex for edge_index in matching
            for vertex in (edges[edge_index]["white"], edges[edge_index]["black"])
            if vertex.startswith("U")
        }
        boundary_set = []
        for index in range(1, 7):
            vertex = f"U{index}"
            if (colors[vertex] == "black" and vertex in used) or (
                colors[vertex] == "white" and vertex not in used
            ):
                boundary_set.append(index)
        records.append((tuple(boundary_set), matching))
    return records


def boundary_measurement(colors: dict[str, str], edges: list[dict[str, Any]]) -> dict[str, Any]:
    records = enumerate_matchings(colors, edges)
    minors: dict[tuple[int, ...], float] = defaultdict(float)
    multiplicities: dict[tuple[int, ...], int] = defaultdict(int)
    for boundary_set, matching in records:
        minors[boundary_set] += math.prod(edges[index]["weight"] for index in matching)
        multiplicities[boundary_set] += 1
    target = {
        tuple(index + 1 for index in columns): abs(determinant_3(columns))
        for columns in itertools.combinations(range(6), 3)
        if abs(determinant_3(columns)) > 1e-12
    }
    if set(minors) != set(target):
        raise AssertionError("Reconstructed graph has the wrong positroid support.")
    reference = (1, 2, 4)
    scale = minors[reference] / target[reference]
    normalized = {boundary_set: value / scale for boundary_set, value in minors.items()}
    maximum_residual = max(abs(normalized[key] - target[key]) for key in target)
    maximum_relative = max(abs(normalized[key] / target[key] - 1.0) for key in target)
    return {
        "almost_perfect_matching_count": len(records),
        "nonzero_minor_count": len(minors),
        "normalization_reference": list(reference),
        "common_scale": scale,
        "maximum_absolute_minor_residual": maximum_residual,
        "maximum_relative_minor_residual": maximum_relative,
        "matching_multiplicities": {"".join(map(str, key)): multiplicities[key] for key in sorted(multiplicities)},
        "normalized_minors": {"".join(map(str, key)): normalized[key] for key in sorted(normalized)},
    }


def check_kasteleyn(colors: dict[str, str], edges: list[dict[str, Any]]) -> float:
    dual_vertices = sorted({point for edge in edges for point in edge["dual"]})
    maximum = 0.0
    for dual_vertex in dual_vertices:
        incident = [edge for edge in edges if dual_vertex in edge["dual"]]
        white_corners = len({edge["white"] for edge in incident})
        boundary_face = any(edge["boundary"] for edge in incident)
        expected = (-1) ** (white_corners if boundary_face else white_corners + 1)
        observed = math.prod(edge["sign"] for edge in incident)
        maximum = max(maximum, abs(observed - expected))
    return maximum

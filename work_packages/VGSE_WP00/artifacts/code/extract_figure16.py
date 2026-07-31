#!/usr/bin/env python3
"""Extract the five Figure 16 t-embedding drawings from the pinned Galashin PDF.

This is a source-provenance utility. It requires PyMuPDF 1.26.7 and the exact
PDF identified by SOURCE_SHA256. The CI replay consumes the committed JSON
fixture and does not download or parse the paper.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import fitz

SOURCE_SHA256 = "e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de"
PDF_PAGE_INDEX = 74
ROUND_DIGITS = 6


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def polygon_area(points: list[tuple[float, float]]) -> float:
    return 0.5 * sum(
        points[index][0] * points[(index + 1) % len(points)][1]
        - points[(index + 1) % len(points)][0] * points[index][1]
        for index in range(len(points))
    )


def drawing_points(drawing: dict[str, Any]) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for item in drawing["items"]:
        if item[0] != "l":
            return []
        left, right = item[1], item[2]
        left_pair = (float(left.x), float(left.y))
        right_pair = (float(right.x), float(right.y))
        if not points:
            points.append(left_pair)
        elif math.dist(points[-1], left_pair) > 1e-4:
            points.append(left_pair)
        points.append(right_pair)
    clean: list[tuple[float, float]] = []
    for point in points:
        if not clean or math.dist(clean[-1], point) > 1e-4:
            clean.append(point)
    if len(clean) > 1 and math.dist(clean[0], clean[-1]) < 1e-4:
        clean.pop()
    return clean


def point_key(point: tuple[float, float]) -> tuple[float, float]:
    return round(point[0], 3), round(point[1], 3)


def undirected_edge(
    left: tuple[float, float], right: tuple[float, float]
) -> tuple[tuple[float, float], tuple[float, float]]:
    return tuple(sorted((point_key(left), point_key(right))))  # type: ignore[return-value]


def boundary_cycle(faces: list[dict[str, Any]]) -> list[tuple[float, float]]:
    counts: dict[tuple[tuple[float, float], tuple[float, float]], int] = defaultdict(int)
    representatives: dict[tuple[float, float], tuple[float, float]] = {}
    for face in faces:
        points = face["points"]
        for index, left in enumerate(points):
            right = points[(index + 1) % len(points)]
            counts[undirected_edge(left, right)] += 1
            representatives[point_key(left)] = left
            representatives[point_key(right)] = right
    graph: dict[tuple[float, float], list[tuple[float, float]]] = defaultdict(list)
    for edge, count in counts.items():
        if count == 1:
            left, right = edge
            graph[left].append(right)
            graph[right].append(left)
    if len(graph) != 6 or any(len(neighbors) != 2 for neighbors in graph.values()):
        raise AssertionError("Expected a six-vertex simple boundary cycle.")
    start = min(graph, key=lambda point: (point[0], point[1]))
    cycle = [start]
    previous = None
    current = start
    while True:
        candidates = graph[current]
        next_point = candidates[0] if candidates[0] != previous else candidates[1]
        if next_point == start:
            break
        cycle.append(next_point)
        previous, current = current, next_point
    coordinates = [representatives[key] for key in cycle]
    # Select the orientation whose next edge points toward the upper apex in PDF coordinates.
    if coordinates[1][1] > coordinates[-1][1]:
        coordinates = [coordinates[0], *reversed(coordinates[1:])]
    return coordinates


def extract(pdf_path: Path) -> dict[str, Any]:
    observed_hash = sha256(pdf_path)
    if observed_hash != SOURCE_SHA256:
        raise ValueError(f"Unexpected PDF SHA-256: {observed_hash}")
    document = fitz.open(pdf_path)
    page = document[PDF_PAGE_INDEX]
    faces: list[dict[str, Any]] = []
    for drawing_index, drawing in enumerate(page.get_drawings()):
        rectangle = drawing["rect"]
        fill = drawing.get("fill")
        if fill is None:
            continue
        if not (rectangle.x0 > 270 and rectangle.y0 < 210 and rectangle.y1 > 60):
            continue
        if max(fill) - min(fill) > 0.01:
            continue
        gray = sum(fill) / 3
        if not (gray < 0.2 or 0.8 < gray < 0.95):
            continue
        points = drawing_points(drawing)
        if len(points) < 3 or abs(polygon_area(points)) < 1.0:
            continue
        faces.append(
            {
                "source_drawing_index": drawing_index,
                "color": "black" if gray < 0.2 else "white",
                "points": points,
            }
        )
    vertex_to_faces: dict[tuple[float, float], list[int]] = defaultdict(list)
    for face_index, face in enumerate(faces):
        for point in face["points"]:
            vertex_to_faces[point_key(point)].append(face_index)
    adjacency = [set() for _ in faces]
    for incident in vertex_to_faces.values():
        for face_index in incident:
            adjacency[face_index].update(set(incident) - {face_index})
    components: list[list[int]] = []
    seen: set[int] = set()
    for face_index in range(len(faces)):
        if face_index in seen:
            continue
        stack = [face_index]
        seen.add(face_index)
        component: list[int] = []
        while stack:
            current = stack.pop()
            component.append(current)
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        components.append(component)
    if len(components) != 5 or any(len(component) != 8 for component in components):
        raise AssertionError("Expected five components with eight nondegenerate faces each.")
    components.sort(
        key=lambda component: (
            min(point[1] for index in component for point in faces[index]["points"]),
            min(point[0] for index in component for point in faces[index]["points"]),
        )
    )
    patterns = []
    for pattern_index, component in enumerate(components, start=1):
        component_faces = [faces[index] for index in sorted(component)]
        boundary = boundary_cycle(component_faces)
        origin_x, origin_y = boundary[0]

        def normalize(point: tuple[float, float]) -> list[float]:
            return [
                round(point[0] - origin_x, ROUND_DIGITS),
                round(origin_y - point[1], ROUND_DIGITS),
            ]

        patterns.append(
            {
                "pattern_id": f"FIG16-{pattern_index:02d}",
                "source_component_order": pattern_index,
                "source_origin_pdf_points": [round(origin_x, 6), round(origin_y, 6)],
                "boundary": [normalize(point) for point in boundary],
                "faces": [
                    {
                        "face_id": f"F{face_number:02d}",
                        "color": face["color"],
                        "source_drawing_index": face["source_drawing_index"],
                        "vertices": [normalize(point) for point in face["points"]],
                    }
                    for face_number, face in enumerate(component_faces, start=1)
                ],
            }
        )
    return {
        "schema_version": "1.0.0",
        "fixture_id": "VGSE-FIG16-SOURCE-VECTOR-001",
        "source": {
            "title": "Amplituhedra and Origami, I: Tree Level",
            "author": "Pavel Galashin",
            "pdf_date": "2026-06-03",
            "pdf_sha256": SOURCE_SHA256,
            "pdf_page_index_zero_based": PDF_PAGE_INDEX,
            "printed_page": 75,
            "figure": 16,
            "extraction_method": "PyMuPDF page.get_drawings vector-path extraction",
            "extractor_version": "PyMuPDF 1.26.7 / MuPDF 1.26.12",
        },
        "semantics": {
            "evidence_class": "SOURCE_VECTOR_GEOMETRY_REPLICATION",
            "not_an_independent_algebraic_to_geometry_reconstruction": True,
            "not_a_rigid_foldability_result": True,
            "not_a_manufacturability_result": True,
            "commercial_claim_authorized": False,
        },
        "patterns": patterns,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    result = extract(arguments.pdf)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

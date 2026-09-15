#!/usr/bin/env python3
"""Audit the Figure 16 source-vector reconstruction against pinned Example B.1 C.

This audit is intentionally narrower than a claim about the paper's undisclosed
source graph. It asks whether the *committed reconstructed visible graph* from
VGSE-FIG16-SOURCE-VECTOR-001, equipped with the Euclidean geometric edge
weights of each extracted drawing, has boundary measurement equal to the
pinned Example B.1 point C.

The comparison is strengthened against labeling ambiguity by exhausting all
6! boundary relabelings and a global color/complement swap. Source coordinates
are rounded to 1e-6 PDF point; the final lower bound accounts conservatively
for +/-0.5e-6 rounding in each coordinate.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence

Point = tuple[float, float]
EdgeKey = tuple[tuple[float, float], tuple[float, float]]
CANONICAL_SOURCE_BOUNDARY_INDICES = (0, 5, 4, 3, 2, 1)
COORDINATE_HALF_QUANTUM = 0.5e-6
TARGET_C = (
    (1, 1, 0, -6, 0, 3),
    (0, 1, 1, 7, 0, -2),
    (0, 0, 0, 2, 1, 3),
)


def determinant_3(columns: Sequence[int]) -> int:
    a, b, c = columns
    return (
        TARGET_C[0][a] * (TARGET_C[1][b] * TARGET_C[2][c] - TARGET_C[1][c] * TARGET_C[2][b])
        - TARGET_C[0][b] * (TARGET_C[1][a] * TARGET_C[2][c] - TARGET_C[1][c] * TARGET_C[2][a])
        + TARGET_C[0][c] * (TARGET_C[1][a] * TARGET_C[2][b] - TARGET_C[1][b] * TARGET_C[2][a])
    )


def target_minors() -> dict[tuple[int, ...], float]:
    return {
        tuple(index + 1 for index in columns): float(abs(determinant_3(columns)))
        for columns in itertools.combinations(range(6), 3)
        if determinant_3(columns) != 0
    }


def as_point(value: Sequence[float]) -> Point:
    return float(value[0]), float(value[1])


def point_key(point: Point) -> tuple[float, float]:
    return round(point[0], 4), round(point[1], 4)


def edge_key(left: Point, right: Point) -> EdgeKey:
    return tuple(sorted((point_key(left), point_key(right))))  # type: ignore[return-value]


def reconstruct_pattern_graph(pattern: dict[str, Any]) -> tuple[dict[str, str], list[dict[str, Any]]]:
    faces = {face["face_id"]: face for face in pattern["faces"]}
    colors = {face_id: face["color"] for face_id, face in faces.items()}
    owners: dict[EdgeKey, list[str]] = defaultdict(list)
    representatives: dict[EdgeKey, tuple[Point, Point]] = {}
    for face in faces.values():
        vertices = [as_point(value) for value in face["vertices"]]
        for index, left in enumerate(vertices):
            right = vertices[(index + 1) % len(vertices)]
            key = edge_key(left, right)
            owners[key].append(face["face_id"])
            representatives.setdefault(key, (left, right))

    boundary_source = [as_point(value) for value in pattern["boundary"]]
    boundary = [boundary_source[index] for index in CANONICAL_SOURCE_BOUNDARY_INDICES]
    boundary_keys = {
        edge_key(boundary[index - 1], boundary[index])
        for index in range(6)
    }
    observed_boundary = {key for key, value in owners.items() if len(value) == 1}
    if boundary_keys != observed_boundary:
        raise AssertionError("Reconstructed face union does not induce the canonical six-edge boundary.")

    edges: list[dict[str, Any]] = []
    for key, incident in sorted(owners.items()):
        left, right = representatives[key]
        weight = math.dist(left, right)
        if weight <= 0:
            raise AssertionError("Zero geometric edge weight.")
        if len(incident) == 2:
            first, second = incident
            if colors[first] == colors[second]:
                raise AssertionError("Internal edge is not bipartite.")
            white = first if colors[first] == "white" else second
            black = second if white == first else first
            edges.append({"white": white, "black": black, "weight": weight, "boundary": False})
        elif len(incident) != 1:
            raise AssertionError("Invalid reconstructed dual-edge incidence.")

    # Boundary edge B_i crosses the primal boundary vertex u_i and therefore
    # lies between canonical dual boundary faces f_{i-1} and f_i.
    for index in range(1, 7):
        previous = boundary[index - 2]
        current = boundary[index - 1]
        key = edge_key(previous, current)
        incident = owners[key]
        if len(incident) != 1:
            raise AssertionError(f"Boundary edge B{index} has invalid incidence.")
        owner = incident[0]
        boundary_vertex = f"U{index}"
        colors[boundary_vertex] = "black" if colors[owner] == "white" else "white"
        white = owner if colors[owner] == "white" else boundary_vertex
        black = boundary_vertex if colors[owner] == "white" else owner
        left, right = representatives[key]
        edges.append({
            "white": white,
            "black": black,
            "weight": math.dist(left, right),
            "boundary": True,
            "boundary_index": index,
        })

    if len(edges) != 16:
        raise AssertionError(f"Expected 16 reconstructed primal edges, found {len(edges)}.")
    return colors, edges


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
        vertex = next(value for value in interior if value not in covered)
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
    records: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    for matching in selected:
        used = {
            vertex
            for edge_index in matching
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


def boundary_measurement(colors: dict[str, str], edges: list[dict[str, Any]]) -> tuple[dict[tuple[int, ...], float], int, int]:
    records = enumerate_matchings(colors, edges)
    minors: dict[tuple[int, ...], float] = defaultdict(float)
    for boundary_set, matching in records:
        minors[boundary_set] += math.prod(edges[index]["weight"] for index in matching)
    return dict(minors), len(records), max(len(matching) for _, matching in records)


def permute_minors(
    minors: dict[tuple[int, ...], float], permutation: Sequence[int], complement: bool
) -> dict[tuple[int, ...], float]:
    labels = set(range(1, 7))
    result: dict[tuple[int, ...], float] = {}
    for key, value in minors.items():
        mapped = tuple(sorted(permutation[index - 1] for index in key))
        if complement:
            mapped = tuple(sorted(labels - set(mapped)))
        result[mapped] = value
    return result


def projective_distortion(
    measured: dict[tuple[int, ...], float], target: dict[tuple[int, ...], float]
) -> float:
    if set(measured) != set(target):
        return math.inf
    logs = [math.log(measured[key] / target[key]) for key in sorted(target)]
    # Minimize the worst multiplicative error over a free common Pluecker scale.
    radius = 0.5 * (max(logs) - min(logs))
    return math.exp(radius)


def best_relabelled_distortion(
    minors: dict[tuple[int, ...], float], target: dict[tuple[int, ...], float]
) -> tuple[float, tuple[int, ...], bool]:
    best = (math.inf, tuple(range(1, 7)), False)
    for permutation in itertools.permutations(range(1, 7)):
        for complement in (False, True):
            candidate = permute_minors(minors, permutation, complement)
            distortion = projective_distortion(candidate, target)
            if distortion < best[0]:
                best = (distortion, permutation, complement)
    return best


def build_audit(fixture: dict[str, Any]) -> dict[str, Any]:
    target = target_minors()
    reports = []
    global_minimum_edge = math.inf
    global_max_matching_size = 0
    for pattern in fixture["patterns"]:
        colors, edges = reconstruct_pattern_graph(pattern)
        minors, matching_count, max_matching_size = boundary_measurement(colors, edges)
        if matching_count != 31:
            raise AssertionError(f"Unexpected APM count for {pattern['pattern_id']}: {matching_count}")
        if set(minors) != set(target):
            raise AssertionError(f"Unexpected positroid support for {pattern['pattern_id']}")
        canonical = projective_distortion(minors, target)
        best, permutation, complement = best_relabelled_distortion(minors, target)
        minimum_edge = min(edge["weight"] for edge in edges)
        global_minimum_edge = min(global_minimum_edge, minimum_edge)
        global_max_matching_size = max(global_max_matching_size, max_matching_size)
        reports.append({
            "pattern_id": pattern["pattern_id"],
            "almost_perfect_matching_count": matching_count,
            "nonzero_plucker_count": len(minors),
            "minimum_geometric_edge_length_pdf_point": minimum_edge,
            "canonical_projective_distortion_factor": canonical,
            "best_projective_distortion_factor_after_all_boundary_relabelings": best,
            "best_boundary_permutation_old_to_new": list(permutation),
            "best_uses_global_color_complement": complement,
        })

    # Each extracted coordinate is rounded to 1e-6 PDF point. A segment vector
    # therefore changes by at most sqrt(2)*1e-6 in Euclidean norm when both
    # endpoints vary over their rounding cells. Bound every matching product
    # by the worst relative edge perturbation and propagate to every minor.
    segment_error = math.sqrt(2.0) * 1e-6
    relative_edge_error = segment_error / global_minimum_edge
    if not (0.0 < relative_edge_error < 1.0):
        raise AssertionError("Invalid source-coordinate rounding bound.")
    plucker_log_error_bound = global_max_matching_size * (-math.log(1.0 - relative_edge_error))
    rounding_distortion_factor = math.exp(plucker_log_error_bound)
    observed_best = min(report["best_projective_distortion_factor_after_all_boundary_relabelings"] for report in reports)
    certified_lower = observed_best / rounding_distortion_factor
    if certified_lower <= 100.0:
        raise AssertionError(
            "Source/C mismatch is not separated from the conservative rounding bound by the required factor 100."
        )

    return {
        "schema_version": "1.0.0",
        "audit_id": "VGSE-FIG16-PINNED-C-MEASUREMENT-AUDIT-001",
        "campaign_id": "VGSE-001",
        "fixture_id": fixture["fixture_id"],
        "target": {
            "source_locus": "Galashin Example B.1 / Figure 16",
            "matrix_C": [list(row) for row in TARGET_C],
            "nonzero_plucker_count": len(target),
        },
        "method": {
            "graph": "committed reconstructed visible eight-face Figure 16 graph",
            "weights": "Euclidean geometric dual-edge lengths from each source-vector drawing",
            "boundary_measurement": "direct almost-perfect-matching enumeration",
            "label_robustness": "exhaust all 6! boundary relabelings and both global color/complement conventions",
            "projective_metric": "minimum worst multiplicative Pluecker error after free common scale",
            "source_coordinate_rounding_half_quantum_pdf_point": COORDINATE_HALF_QUANTUM,
            "rounding_bound": "endpoint rounding propagated through edge lengths, matching products, and Pluecker sums",
        },
        "patterns": reports,
        "rounding_robustness": {
            "global_minimum_geometric_edge_length_pdf_point": global_minimum_edge,
            "maximum_matching_size": global_max_matching_size,
            "relative_edge_error_upper": relative_edge_error,
            "plucker_rounding_distortion_factor_upper": rounding_distortion_factor,
            "minimum_observed_best_relabelled_projective_distortion_factor": observed_best,
            "certified_best_relabelled_projective_distortion_factor_lower": certified_lower,
            "required_lower_threshold": 100.0,
        },
        "conclusion": {
            "visible_reconstructed_geometric_weight_class_measures_pinned_C": False,
            "all_five_source_vector_patterns_fail_pinned_C_under_visible_graph": True,
            "failure_survives_all_boundary_relabelings_and_global_color_complement": True,
            "current_pdf_vector_reconstruction_sufficient_for_VGSE_C06": False,
            "required_repair": "Obtain the exact source graph/weight or generation data, or define a separately governed source-authorized correspondence; do not infer an equivalence relation from the failed output.",
        },
        "claim_boundary": {
            "paper_claim_refuted": False,
            "exact_underlying_source_graph_identified": False,
            "current_reconstructed_visible_graph_bridge_to_pinned_C_rejected": True,
            "mathcert_adjudication_effect": "none",
            "rigid_deployment_authorized": False,
            "manufacturing_authorized": False,
            "commercial_claim_authorized": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    fixture = json.loads(arguments.fixture.read_text(encoding="utf-8"))
    audit = build_audit(fixture)
    text = json.dumps(audit, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(text, encoding="utf-8")
    if arguments.check and arguments.check.read_text(encoding="utf-8") != text:
        print("Figure 16 pinned-C measurement audit does not match replay.")
        return 1
    if not arguments.output and not arguments.check:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

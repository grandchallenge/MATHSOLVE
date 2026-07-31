#!/usr/bin/env python3
"""Independently reconstruct the five Galashin B.3 t-embeddings.

This numerical, standard-library replay verifies the reduced graph boundary
measurement, extends five master-function witnesses, integrates five
Kenyon-Smirnov primitives, and checks the resulting planar t-embeddings. It
does not establish rigid deployment, finite thickness, manufacture, or a
commercial claim.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

from b3_common import complex_record, point_key
from b3_geometry import svg_document, validate_geometry
from b3_graph import boundary_measurement, check_kasteleyn, load_graph
from b3_holomorphic import extensions, primitive


def build_report(source: dict[str, Any], replay: dict[str, Any], weights: dict[str, Any]) -> dict[str, Any]:
    boundary, colors, edges, labels = load_graph(source, weights)
    measurement = boundary_measurement(colors, edges)
    kasteleyn_residual = check_kasteleyn(colors, edges)
    boundary_increments = [boundary[index] - boundary[index - 1] for index in range(6)]
    generated = []
    coordinate_maps: list[dict[str, complex]] = []
    for solution in replay["solutions"]:
        chart = solution["projective_chart"]
        x = complex(chart["a2"]["re"], chart["a2"]["im"])
        y = complex(chart["a3"]["re"], chart["a3"]["im"])
        zeta = [1 + 0j, 1 + x, x, -6 + 7 * x + 2 * y, y, 3 - 2 * x + 3 * y]
        zeta_tilde = [boundary_increments[index] / zeta[index] for index in range(6)]
        f_values, tilde_values, f_residual, tilde_residual = extensions(
            colors, edges, zeta, zeta_tilde
        )
        positions, closure_residual = primitive(edges, f_values, tilde_values)
        anchor_key = point_key((boundary[0].real, boundary[0].imag))
        shift = boundary[0] - positions[anchor_key]
        positions = {key: value + shift for key, value in positions.items()}
        boundary_residual = max(
            abs(positions[point_key((point.real, point.imag))] - point) for point in boundary
        )
        faces, metrics = validate_geometry(source, boundary, positions)
        coordinates = {labels[key]: value for key, value in positions.items()}
        coordinate_maps.append(coordinates)
        generated.append(
            {
                "pattern_id": solution["id"],
                "algebraic_witness": chart,
                "dual_vertices": {
                    label: complex_record(value) for label, value in sorted(coordinates.items())
                },
                "faces": faces,
                "metrics": {
                    **metrics,
                    "f_extension_residual": f_residual,
                    "tilde_extension_residual": tilde_residual,
                    "primitive_closure_residual": closure_residual,
                    "prescribed_boundary_residual": boundary_residual,
                },
                "status": "NUMERICALLY_RECONSTRUCTED_T_EMBEDDING_NEEDS_AUDIT",
            }
        )
    pairwise = []
    minimum_distinctness = math.inf
    for left in range(len(coordinate_maps)):
        row = []
        for right in range(len(coordinate_maps)):
            distance = max(
                abs(coordinate_maps[left][label] - coordinate_maps[right][label])
                for label in coordinate_maps[left]
            )
            row.append(distance)
            if left < right:
                minimum_distinctness = min(minimum_distinctness, distance)
        pairwise.append(row)
    return {
        "schema_version": "1.0.0",
        "reconstruction_id": "VGSE-B3-KENYON-SMIRNOV-001",
        "source_fixture": source["fixture_id"],
        "algebraic_fixture": replay["replication_id"],
        "graph_weight_fixture": weights["fixture_id"],
        "boundary_measurement": measurement,
        "kasteleyn_sign_residual": kasteleyn_residual,
        "generated_pattern_count": len(generated),
        "minimum_pairwise_internal_coordinate_distance": minimum_distinctness,
        "pairwise_maximum_coordinate_distance": pairwise,
        "patterns": generated,
        "claim_boundary": {
            "five_algebraic_witnesses_extended": True,
            "five_kenyon_smirnov_primitives_integrated": True,
            "five_distinct_planar_t_embeddings_reconstructed_numerically": True,
            "exact_root_isolation_certified": False,
            "exact_symbolic_weight_recovery_certified": False,
            "continuous_rigid_foldability_established": False,
            "collision_free_deployment_established": False,
            "finite_thickness_structure_established": False,
            "manufacturable_product_established": False,
            "commercial_claim_authorized": False,
        },
    }


def validate_report(report: dict[str, Any]) -> None:
    measurement = report["boundary_measurement"]
    assert measurement["almost_perfect_matching_count"] == 31
    assert measurement["nonzero_minor_count"] == 19
    assert measurement["maximum_relative_minor_residual"] < 1e-12
    assert report["kasteleyn_sign_residual"] == 0.0
    assert report["generated_pattern_count"] == 5
    assert report["minimum_pairwise_internal_coordinate_distance"] > 1.0
    for pattern in report["patterns"]:
        metrics = pattern["metrics"]
        assert metrics["face_count"] == 8.0
        assert metrics["minimum_edge_length"] > 1e-6
        assert metrics["maximum_kawasaki_residual"] < 1e-9
        assert metrics["minimum_boundary_angle_margin"] > 1e-3
        assert metrics["area_partition_residual"] < 1e-8
        assert metrics["f_extension_residual"] < 1e-9
        assert metrics["tilde_extension_residual"] < 1e-8
        assert metrics["primitive_closure_residual"] < 1e-8
        assert metrics["prescribed_boundary_residual"] < 1e-8
    boundary = report["claim_boundary"]
    assert boundary["five_distinct_planar_t_embeddings_reconstructed_numerically"]
    assert not boundary["continuous_rigid_foldability_established"]
    assert not boundary["manufacturable_product_established"]
    assert not boundary["commercial_claim_authorized"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_vectors", type=Path)
    parser.add_argument("algebraic_replay", type=Path)
    parser.add_argument("graph_weights", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--svg-dir", type=Path)
    parser.add_argument("--check", action="store_true")
    arguments = parser.parse_args()
    source = json.loads(arguments.source_vectors.read_text(encoding="utf-8"))
    replay = json.loads(arguments.algebraic_replay.read_text(encoding="utf-8"))
    weights = json.loads(arguments.graph_weights.read_text(encoding="utf-8"))
    report = build_report(source, replay, weights)
    if arguments.check:
        validate_report(report)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    if arguments.svg_dir:
        arguments.svg_dir.mkdir(parents=True, exist_ok=True)
        for pattern in report["patterns"]:
            (arguments.svg_dir / f"{pattern['pattern_id'].lower()}.svg").write_text(
                svg_document(pattern), encoding="utf-8"
            )
    if not arguments.output:
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

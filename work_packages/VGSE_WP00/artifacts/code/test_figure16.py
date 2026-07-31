#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import validate_figure16 as MODULE


class Figure16Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = pathlib.Path(__file__).parents[1]
        cls.fixture = json.loads(
            (cls.root / "data" / "figure16_source_vectors.json").read_text(encoding="utf-8")
        )
        cls.report = MODULE.build_report(cls.fixture)

    def test_five_common_boundary_patterns(self) -> None:
        self.assertEqual(self.report["pattern_count"], 5)
        self.assertLess(
            self.report["maximum_common_boundary_residual"], MODULE.GEOMETRY_TOLERANCE
        )
        self.assertTrue(self.report["common_reconstructed_graph_topology"])

    def test_planar_conditions(self) -> None:
        for pattern in self.report["patterns"]:
            self.assertEqual(pattern["face_count"], 8)
            self.assertEqual(pattern["interior_dual_vertex_count"], 3)
            self.assertEqual(
                pattern["reconstructed_weighted_primal_graph"]["primal_edge_count"], 16
            )
            self.assertLess(
                pattern["maximum_kawasaki_color_sum_residual"], MODULE.ANGLE_TOLERANCE
            )
            self.assertTrue(
                pattern["injectivity_checked_by_simple_boundary_and_face_partition"]
            )

    def test_claim_boundary_fails_closed(self) -> None:
        boundary = self.report["claim_boundary"]
        self.assertTrue(boundary["source_vector_five_pattern_geometry_replicated"])
        self.assertFalse(
            boundary["full_t_embedding_correspondence_to_pinned_C_independently_verified"]
        )
        self.assertFalse(
            boundary["algebraic_witness_to_pattern_correspondence_reconstructed"]
        )
        self.assertFalse(boundary["continuous_rigid_foldability_established"])
        self.assertFalse(boundary["manufacturable_product_established"])
        self.assertFalse(boundary["commercial_claim_authorized"])

    def test_expected_report_and_svg_render(self) -> None:
        expected = json.loads(
            (self.root / "data" / "figure16_validation.json").read_text(encoding="utf-8")
        )
        self.assertEqual(expected, self.report)
        with tempfile.TemporaryDirectory() as directory:
            for pattern in self.fixture["patterns"]:
                svg = MODULE.svg_document(pattern)
                self.assertIn("<svg", svg)
                self.assertEqual(svg.count("<polygon"), 9)
                (pathlib.Path(directory) / f"{pattern['pattern_id']}.svg").write_text(svg)


if __name__ == "__main__":
    unittest.main(verbosity=2)

#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import reconstruct_b3 as MODULE


class ReconstructB3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = pathlib.Path(__file__).parents[1]
        cls.source = json.loads((cls.root / "data" / "figure16_source_vectors.json").read_text())
        cls.replay = json.loads((cls.root / "data" / "expected_replay.json").read_text())
        cls.weights = json.loads((cls.root / "data" / "graph_weight_fixture.json").read_text())
        cls.report = MODULE.build_report(cls.source, cls.replay, cls.weights)

    def test_boundary_measurement_replays_C(self) -> None:
        measurement = self.report["boundary_measurement"]
        self.assertEqual(measurement["almost_perfect_matching_count"], 31)
        self.assertEqual(measurement["nonzero_minor_count"], 19)
        self.assertLess(measurement["maximum_relative_minor_residual"], 1e-12)

    def test_five_distinct_t_embeddings(self) -> None:
        MODULE.validate_report(self.report)
        self.assertEqual(self.report["generated_pattern_count"], 5)
        self.assertGreater(self.report["minimum_pairwise_internal_coordinate_distance"], 1.0)

    def test_expected_reconstruction_matches_fresh_replay(self) -> None:
        expected = json.loads((self.root / "data" / "reconstruction_summary.json").read_text())
        fresh = {key: self.report[key] for key in (
            "schema_version", "reconstruction_id", "source_fixture", "algebraic_fixture",
            "graph_weight_fixture", "boundary_measurement", "kasteleyn_sign_residual",
            "generated_pattern_count", "minimum_pairwise_internal_coordinate_distance",
            "claim_boundary"
        )}
        fresh["patterns"] = [
            {
                "pattern_id": pattern["pattern_id"],
                "algebraic_witness": pattern["algebraic_witness"],
                "interior_dual_vertices": {
                    label: value for label, value in pattern["dual_vertices"].items()
                    if label.startswith("I:")
                },
                "metrics": pattern["metrics"],
                "status": pattern["status"],
            }
            for pattern in self.report["patterns"]
        ]
        self.assertEqual(expected, fresh)

    def test_svg_render_and_claim_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = pathlib.Path(directory)
            for pattern in self.report["patterns"]:
                svg = MODULE.svg_document(pattern)
                self.assertIn("<svg", svg)
                self.assertEqual(svg.count("<polygon"), 8)
                (output / f"{pattern['pattern_id']}.svg").write_text(svg)
            self.assertEqual(len(list(output.glob("*.svg"))), 5)
        boundary = self.report["claim_boundary"]
        self.assertTrue(boundary["five_distinct_planar_t_embeddings_reconstructed_numerically"])
        self.assertFalse(boundary["continuous_rigid_foldability_established"])
        self.assertFalse(boundary["manufacturable_product_established"])
        self.assertFalse(boundary["commercial_claim_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

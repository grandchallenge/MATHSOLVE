#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import replicate_b3 as MODULE


class GalashinB3ReplicationTests(unittest.TestCase):
    def test_bounded_region_count_is_five(self) -> None:
        beta, intersections = MODULE.bounded_region_count(MODULE.LINES)
        self.assertEqual(beta, 5)
        self.assertEqual(intersections, 9)

    def test_source_boundary_solver_returns_five_valid_pairs(self) -> None:
        report = MODULE.report()
        MODULE.validate(report)
        self.assertEqual(report["algebraic_witness_count"], 5)
        self.assertEqual(report["replication_id"], "VGSE-B3-FIGURE16-BOUNDARY-001")
        self.assertEqual(report["source"]["provenance_state"], "unverified_candidate")
        self.assertIsNone(report["source"]["provider_manifest"])

    def test_all_unsaturated_extra_factors_are_divisor_supported(self) -> None:
        report = MODULE.report()
        excluded = report["elimination"]["excluded_divisor_factors"]
        self.assertEqual(set(excluded), {"x^3", "(x+1)^3", "2x-3", "7x-6", "25x-24"})
        self.assertTrue(all(item["arrangement_forms"] for item in excluded.values()))

    def test_claim_boundary_fails_closed(self) -> None:
        boundary = MODULE.report()["claim_boundary"]
        self.assertTrue(boundary["exact_arrangement_count_replicated"])
        self.assertTrue(boundary["source_boundary_algebraic_witness_replay_complete"])
        self.assertTrue(boundary["source_vector_five_pattern_geometry_replicated_in_separate_artifact"])
        self.assertFalse(boundary["algebraic_witness_to_pattern_correspondence_reconstructed"])
        self.assertFalse(boundary["continuous_rigid_foldability_established"])
        self.assertFalse(boundary["finite_thickness_structure_established"])
        self.assertFalse(boundary["manufacturable_product_established"])
        self.assertFalse(boundary["commercial_claim_authorized"])

    def test_expected_fixture_matches_fresh_replay(self) -> None:
        expected_path = pathlib.Path(__file__).parents[1] / "data" / "expected_replay.json"
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        fresh = MODULE.report()
        self.assertEqual(expected["arrangement"], fresh["arrangement"])
        self.assertEqual(expected["elimination"], fresh["elimination"])
        self.assertEqual(expected["algebraic_witness_count"], fresh["algebraic_witness_count"])
        self.assertEqual(
            expected["source"]["author_pdf_sha256"],
            fresh["source"]["candidate_pdf_sha256"],
        )
        expected_points = [
            (item["projective_chart"]["a2"], item["projective_chart"]["a3"])
            for item in expected["solutions"]
        ]
        fresh_points = [
            (item["projective_chart"]["a2"], item["projective_chart"]["a3"])
            for item in fresh["solutions"]
        ]
        for (expected_x, expected_y), (fresh_x, fresh_y) in zip(expected_points, fresh_points):
            for key in ("re", "im"):
                self.assertAlmostEqual(expected_x[key], fresh_x[key], places=11)
                self.assertAlmostEqual(expected_y[key], fresh_y[key], places=11)


if __name__ == "__main__":
    unittest.main(verbosity=2)

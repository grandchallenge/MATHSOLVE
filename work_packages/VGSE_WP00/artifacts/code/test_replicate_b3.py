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

    def test_saturated_solver_returns_five_valid_pairs(self) -> None:
        report = MODULE.build_report()
        MODULE.validate_report(report)
        self.assertEqual(report["algebraic_solution_count"], 5)

    def test_claim_boundary_fails_closed(self) -> None:
        report = MODULE.build_report()
        boundary = report["claim_boundary"]
        self.assertTrue(boundary["algebraic_branch_count_replicated"])
        self.assertFalse(boundary["real_t_embedding_geometry_rendered"])
        self.assertFalse(boundary["continuous_rigid_foldability_established"])
        self.assertFalse(boundary["finite_thickness_structure_established"])
        self.assertFalse(boundary["manufacturable_product_established"])
        self.assertFalse(boundary["commercial_claim_authorized"])

    def test_expected_fixture_matches_fresh_replay(self) -> None:
        expected_path = pathlib.Path(__file__).parents[1] / "data" / "expected_replay.json"
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        fresh = MODULE.build_report()
        self.assertEqual(expected["arrangement"], fresh["arrangement"])
        self.assertEqual(expected["algebraic_solution_count"], fresh["algebraic_solution_count"])
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

import unittest
from unittest.mock import patch

import ci.erdos_open_cohort_closure as closure_module
from ci.erdos_open_cohort_closure import build_closure, validate_closure


class ErdosOpenCohortClosureTests(unittest.TestCase):
    def test_live_241_r_plus_a_builds_bounded_closure(self):
        closure = build_closure("241", "b" * 40, "2026-10-06")
        self.assertEqual(
            closure["required_synthesis_lanes"],
            ["R1", "A1"],
        )
        self.assertTrue(closure["minimum_synthesis_evidence_satisfied"])
        self.assertTrue(closure["blind_cohort_closed"])
        self.assertTrue(closure["synthesis_allowed"])
        self.assertFalse(closure["mathematical_correctness_adjudicated"])
        self.assertFalse(closure["canonical_claim_effect"])
        self.assertEqual(
            {item["lane"] for item in closure["evidence"]},
            {"R1", "A1"},
        )
        self.assertEqual(validate_closure("241", closure), [])

    def test_closure_does_not_require_source_lane_for_synthesis(self):
        live_lane_receipt = closure_module.lane_receipt

        def without_source(problem, lane):
            if lane == "S1":
                return None
            return live_lane_receipt(problem, lane)

        with patch.object(closure_module, "lane_receipt", side_effect=without_source):
            closure = build_closure("241", "c" * 40, "2026-10-06")
        self.assertFalse(closure["source_lane"]["protected_at_closure"])
        self.assertFalse(
            closure["literature_dependent_promotion_source_gate_satisfied_at_closure"]
        )
        self.assertTrue(closure["synthesis_allowed"])

    def test_authority_inflation_is_rejected(self):
        closure = build_closure("241", "d" * 40, "2026-10-06")
        closure["canonical_claim_effect"] = True
        errors = validate_closure("241", closure)
        self.assertIn("authority inflation: canonical_claim_effect", errors)


if __name__ == "__main__":
    unittest.main()

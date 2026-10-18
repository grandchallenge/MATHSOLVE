import unittest
from unittest.mock import patch

import ci.erdos_open_cohort_closure as closure_module
from ci.erdos_open_cohort_closure import build_closure, validate_closure
from ci.erdos_open_semantic_gate import policy_blockers


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

    def test_registered_erdos_138_policy_retroactively_gates_counterexample(self):
        blockers = policy_blockers(
            "ERDOS-138-A1-IA-001",
            "COUNTEREXAMPLE",
            closure_module.ROOT,
        )
        self.assertEqual(len(blockers), 1)
        self.assertEqual(
            blockers[0]["requires_dispatch_id"],
            "ERDOS-138-S1-IA-001",
        )

    def test_semantic_blocker_prevents_closure_without_source_return(self):
        live_lane_receipt = closure_module.lane_receipt

        def with_blocker_without_source(problem, lane):
            if lane == "S1":
                return None
            receipt = live_lane_receipt(problem, lane)
            if lane == "A1" and receipt is not None:
                receipt = dict(receipt)
                receipt["semantic_blockers"] = [
                    {
                        "blocker_id": "ERDOS-241-TEST-SOURCE-FORMAL-001",
                        "kind": "SOURCE_FORMAL_CONFLICT",
                        "requires_dispatch_id": "ERDOS-241-S1-IA-001",
                    }
                ]
            return receipt

        with patch.object(
            closure_module,
            "lane_receipt",
            side_effect=with_blocker_without_source,
        ):
            with self.assertRaisesRegex(ValueError, "semantic source gate requires protected return"):
                build_closure("241", "e" * 40, "2026-10-06")

    def test_semantic_blocker_requires_s1_before_synthesis(self):
        live_lane_receipt = closure_module.lane_receipt

        def with_blocker_and_source(problem, lane):
            if lane == "S1":
                return {
                    "lane": "S1",
                    "dispatch_id": "ERDOS-241-S1-IA-001",
                    "disposition_declared": "SOURCE_INTERFACE_FOUND",
                    "semantic_blockers": [],
                }
            receipt = live_lane_receipt(problem, lane)
            if lane == "A1" and receipt is not None:
                receipt = dict(receipt)
                receipt["semantic_blockers"] = [
                    {
                        "blocker_id": "ERDOS-241-TEST-SOURCE-FORMAL-001",
                        "kind": "SOURCE_FORMAL_CONFLICT",
                        "requires_dispatch_id": "ERDOS-241-S1-IA-001",
                    }
                ]
            return receipt

        with patch.object(
            closure_module,
            "lane_receipt",
            side_effect=with_blocker_and_source,
        ):
            closure = build_closure("241", "f" * 40, "2026-10-06")
            self.assertEqual(
                closure["required_synthesis_lanes"],
                ["R1", "A1", "S1"],
            )
            self.assertTrue(closure["semantic_gate_required"])
            self.assertTrue(closure["semantic_source_audit_obligation_discharged"])
            self.assertTrue(closure["semantic_gate_satisfied_at_closure"])
            self.assertTrue(closure["synthesis_allowed"])
            self.assertEqual(validate_closure("241", closure), [])

    def test_semantic_source_exact_blocker_does_not_discharge_gate(self):
        live_lane_receipt = closure_module.lane_receipt

        def with_blocked_source(problem, lane):
            if lane == "S1":
                return {
                    "lane": "S1",
                    "dispatch_id": "ERDOS-241-S1-IA-001",
                    "disposition_declared": "EXACT_BLOCKER",
                    "semantic_blockers": [],
                }
            receipt = live_lane_receipt(problem, lane)
            if lane == "A1" and receipt is not None:
                receipt = dict(receipt)
                receipt["semantic_blockers"] = [
                    {
                        "blocker_id": "ERDOS-241-TEST-SOURCE-FORMAL-001",
                        "kind": "SOURCE_FORMAL_CONFLICT",
                        "requires_dispatch_id": "ERDOS-241-S1-IA-001",
                    }
                ]
            return receipt

        with patch.object(
            closure_module,
            "lane_receipt",
            side_effect=with_blocked_source,
        ):
            with self.assertRaisesRegex(ValueError, "source-audit return is itself blocked"):
                build_closure("241", "1" * 40, "2026-10-06")

    def test_authority_inflation_is_rejected(self):
        closure = build_closure("241", "d" * 40, "2026-10-06")
        closure["canonical_claim_effect"] = True
        errors = validate_closure("241", closure)
        self.assertIn("authority inflation: canonical_claim_effect", errors)


if __name__ == "__main__":
    unittest.main()

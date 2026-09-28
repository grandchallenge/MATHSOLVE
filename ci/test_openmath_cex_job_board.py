import unittest

from ci.validate_openmath_cex_job_board import EXPECTED_ASSIGNMENTS, EXPECTED_SLOTS, load, validate


class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_exact_source_acquisition_assignment_set(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        self.assertEqual([x["assignment_id"] for x in registry["assignments"]], EXPECTED_ASSIGNMENTS)
        self.assertEqual([x["slot"] for x in registry["assignments"]], EXPECTED_SLOTS)

    def test_no_external_self_claim(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        self.assertFalse(registry["lease_policy"]["external_self_claim_allowed"])
        self.assertTrue(all(x["state"] == "AVAILABLE_FOR_LEASE" for x in registry["assignments"]))
        self.assertTrue(all(x["lease"]["state"] == "UNCLAIMED" for x in registry["assignments"]))

    def test_no_early_math_release(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        self.assertEqual(registry["mathematics_release_policy"]["current_math_jobs"], 0)
        for item in registry["assignments"]:
            self.assertFalse(item["permissions"]["hill_specific_mathematics"])
            self.assertIsNone(item["prerequisites"]["source_lock"])


if __name__ == "__main__":
    unittest.main()

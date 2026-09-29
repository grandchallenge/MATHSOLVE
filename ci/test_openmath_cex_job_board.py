import unittest

from ci.validate_openmath_cex_job_board import EXPECTED, H1, INTRO, load, validate


class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_six_h2_h7_leases_are_one_to_one_and_not_launched(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        jobs = {
            x["assignment_id"]: x
            for x in registry["assignments"]
            if x.get("assignment_id") in EXPECTED
        }
        self.assertEqual(set(jobs), set(EXPECTED))
        self.assertEqual(
            {jobs[a]["lease"]["agent_ref"] for a in jobs},
            {v["agent"] for v in EXPECTED.values()},
        )
        self.assertEqual(
            {jobs[a]["lease"]["dispatch_issue_number"] for a in jobs},
            {v["issue"] for v in EXPECTED.values()},
        )
        self.assertTrue(
            all(
                jobs[a]["state"] == "LEASED_NOT_LAUNCHED"
                and jobs[a]["lease"]["state"] == "LEASED"
                for a in jobs
            )
        )
        self.assertTrue(all(jobs[a]["lifecycle"]["launched"] is False for a in jobs))
        self.assertTrue(
            all(jobs[a]["lease"]["protected_lease_commit"] == INTRO for a in jobs)
        )

    def test_h1_result_is_adjudicated_and_closed(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        job = next(
            x for x in registry["assignments"]
            if x.get("assignment_id") == H1["assignment"]
        )
        self.assertEqual(job["lease"]["dispatch_id"], H1["dispatch"])
        self.assertEqual(job["lease"]["agent_ref"], H1["agent"])
        self.assertEqual(job["lease"]["dispatch_issue_number"], H1["issue"])
        self.assertEqual(job["state"], "ACCEPTED")
        self.assertEqual(job["lease"]["state"], "CLOSED_AFTER_RETURN")
        self.assertFalse(job["lease"]["execution_authorized"])
        self.assertEqual(job["lifecycle"]["adjudication"], "ACCEPTED_SOURCE_CONDITIONAL_REDUCTION")
        self.assertTrue(job["lifecycle"]["closed"])

    def test_lifecycle_counters(self):
        policy = load(
            ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
        )["mathematics_release_policy"]
        self.assertEqual(policy["h2_h7_available_math_jobs"], 0)
        self.assertEqual(policy["h2_h7_leased_math_jobs"], 6)
        self.assertEqual(policy["h2_h7_launched_math_jobs"], 0)
        self.assertEqual(policy["h2_h7_returned_math_jobs"], 0)
        self.assertEqual(policy["h2_h7_captured_math_jobs"], 0)


if __name__ == "__main__":
    unittest.main()

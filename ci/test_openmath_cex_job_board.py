import unittest

from ci.validate_openmath_cex_job_board import EXPECTED, H1, INTRO, load, validate


class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_h2_through_h7_bindings_remain_one_to_one(self):
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
        h2 = jobs["OM26-H2-WP01"]
        self.assertEqual(h2["state"], "ACCEPTED")
        self.assertEqual(h2["lease"]["state"], "CLOSED_AFTER_RETURN")
        self.assertFalse(h2["lease"]["execution_authorized"])
        self.assertTrue(h2["lifecycle"]["launched"])
        self.assertTrue(h2["lifecycle"]["closed"])
        for aid in sorted(a for a in jobs if a != "OM26-H2-WP01"):
            self.assertEqual(jobs[aid]["state"], "LEASED_NOT_LAUNCHED")
            self.assertEqual(jobs[aid]["lease"]["state"], "LEASED")
            self.assertFalse(jobs[aid]["lifecycle"]["launched"])
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

    def test_seven_hill_release_projection(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        self.assertEqual(
            registry["current_topology"]["hills"],
            [f"OM26-H{i}" for i in range(1, 8)],
        )
        policy = registry["mathematics_release_policy"]
        self.assertEqual(set(policy["per_hill"]), {f"OM26-H{i}" for i in range(1, 8)})
        self.assertEqual(policy["per_hill"]["OM26-H1"]["agent_state"], "ACCEPTED")
        self.assertEqual(policy["per_hill"]["OM26-H2"]["agent_state"], "ACCEPTED")
        for i in range(3, 8):
            self.assertEqual(
                policy["per_hill"][f"OM26-H{i}"]["agent_state"],
                "LEASED_NOT_LAUNCHED",
            )
        self.assertEqual(policy["summary"]["released_hills"], 7)
        self.assertEqual(policy["summary"]["accepted_agents"], 2)
        self.assertEqual(policy["summary"]["leased_not_launched_agents"], 5)
        self.assertTrue(policy["historical_tranche_metrics"]["deprecated_for_current_state"])


if __name__ == "__main__":
    unittest.main()

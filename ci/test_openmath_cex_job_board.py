import unittest

from ci.validate_openmath_cex_job_board import (
    H1, H2_WP01, H2_WP02, H2_WP03, EXPECTED, load, validate
)


class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_h2_lifecycle_progression(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        jobs = {x["assignment_id"]: x for x in registry["assignments"]}
        self.assertEqual(jobs[H2_WP01["assignment"]]["state"], "ACCEPTED")
        self.assertEqual(jobs[H2_WP02["assignment"]]["state"], "ACCEPTED")
        self.assertEqual(
            jobs[H2_WP02["assignment"]]["lifecycle"]["adjudication"],
            "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED",
        )
        wp03 = jobs[H2_WP03["assignment"]]
        self.assertEqual(wp03["state"], "LEASED_NOT_LAUNCHED")
        self.assertEqual(wp03["lease"]["state"], "LEASED")
        self.assertEqual(wp03["lease"]["agent_ref"], "INDEPENDENT-AGENT-009")
        self.assertFalse(wp03["lifecycle"]["launched"])

    def test_peer_hills_remain_leased_and_unlaunched(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        jobs = {x["assignment_id"]: x for x in registry["assignments"]}
        for aid in EXPECTED:
            self.assertEqual(jobs[aid]["state"], "LEASED_NOT_LAUNCHED")
            self.assertEqual(jobs[aid]["lease"]["state"], "LEASED")
            self.assertFalse(jobs[aid]["lifecycle"]["launched"])

    def test_h1_remains_adjudicated_and_closed(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        job = next(x for x in registry["assignments"] if x["assignment_id"] == H1["assignment"])
        self.assertEqual(job["state"], "ACCEPTED")
        self.assertEqual(job["lease"]["state"], "CLOSED_AFTER_RETURN")
        self.assertFalse(job["lease"]["execution_authorized"])

    def test_seven_hill_release_projection(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        self.assertEqual(registry["current_topology"]["hills"], [f"OM26-H{i}" for i in range(1, 8)])
        policy = registry["mathematics_release_policy"]
        self.assertEqual(policy["per_hill"]["OM26-H2"]["assignment"], "OM26-H2-WP03")
        self.assertEqual(policy["per_hill"]["OM26-H2"]["predecessor"]["assignment"], "OM26-H2-WP02")
        self.assertEqual(policy["summary"]["accepted_agents"], 3)
        self.assertEqual(policy["summary"]["leased_not_launched_agents"], 6)


if __name__ == "__main__":
    unittest.main()

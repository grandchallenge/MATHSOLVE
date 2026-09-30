import unittest

from ci.validate_openmath_cex_job_board import HILLS, load, validate


class OpenMathCEXJobBoardTest(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_every_hill_has_one_current_assignment(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        assignments = {x["assignment_id"]: x for x in registry["assignments"] if x.get("assignment_id")}
        policy = registry["mathematics_release_policy"]["per_hill"]
        self.assertEqual(set(policy), set(HILLS))
        for hill in HILLS:
            aid = policy[hill]["assignment"]
            self.assertIn(aid, assignments)
            self.assertEqual(assignments[aid]["hill"], hill)
            self.assertEqual(assignments[aid]["state"], policy[hill]["agent_state"])

    def test_closed_predecessors_are_not_executable(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        assignments = {x["assignment_id"]: x for x in registry["assignments"] if x.get("assignment_id")}
        for item in assignments.values():
            if item.get("class") != "MATHEMATICAL_RESEARCH":
                continue
            if item.get("state") == "ACCEPTED":
                self.assertTrue(item["lifecycle"]["closed"])
                self.assertFalse(item["lease"].get("execution_authorized", False))

    def test_current_leases_are_ready_not_launched(self):
        registry = load(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
        assignments = {x["assignment_id"]: x for x in registry["assignments"] if x.get("assignment_id")}
        policy = registry["mathematics_release_policy"]["per_hill"]
        scripts = registry["launch_contract"]["current_scripts"]
        for hill in HILLS:
            item = assignments[policy[hill]["assignment"]]
            if item["state"] != "LEASED_NOT_LAUNCHED":
                continue
            self.assertEqual(item["lease"]["state"], "LEASED")
            self.assertTrue(item["lease"]["execution_authorized"])
            self.assertFalse(item["lifecycle"]["launched"])
            self.assertTrue(scripts[hill]["executable"])
            self.assertEqual(scripts[hill]["assignment_id"], item["assignment_id"])


if __name__ == "__main__":
    unittest.main()

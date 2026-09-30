import copy
import json
import unittest
from pathlib import Path

from ci.openmath_lifecycle_candidate import refresh_summary

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"


class OpenMathLifecycleCandidateStateTest(unittest.TestCase):
    def load_registry(self):
        return json.loads(REGISTRY.read_text(encoding="utf-8"))

    def test_current_summary_is_state_derived(self):
        registry = self.load_registry()
        expected = copy.deepcopy(registry["mathematics_release_policy"]["summary"])
        self.assertEqual(refresh_summary(registry), expected)

    def test_launched_return_to_successor_recomputes_counts(self):
        registry = self.load_registry()
        assignments = {
            x["assignment_id"]: x
            for x in registry["assignments"]
            if x.get("assignment_id")
        }
        predecessor = assignments["OM26-H3-WP01"]
        predecessor["state"] = "LAUNCHED"

        launched = refresh_summary(registry)
        self.assertEqual(launched["launched_agents"], 1)
        self.assertEqual(launched["leased_not_launched_agents"], 5)

        predecessor["state"] = "ACCEPTED"
        successor = {
            "assignment_id": "OM26-H3-WP02",
            "class": "MATHEMATICAL_RESEARCH",
            "hill": "OM26-H3",
            "state": "LEASED_NOT_LAUNCHED",
        }
        registry["assignments"].append(successor)
        registry["mathematics_release_policy"]["per_hill"]["OM26-H3"]["assignment"] = successor["assignment_id"]
        registry["mathematics_release_policy"]["per_hill"]["OM26-H3"]["agent_state"] = successor["state"]

        advanced = refresh_summary(registry)
        self.assertEqual(advanced["launched_agents"], 0)
        self.assertEqual(advanced["leased_not_launched_agents"], 6)
        self.assertEqual(advanced["returned_unadjudicated_agents"], 0)
        self.assertEqual(advanced["accepted_agents"], launched["accepted_agents"] + 1)


if __name__ == "__main__":
    unittest.main()

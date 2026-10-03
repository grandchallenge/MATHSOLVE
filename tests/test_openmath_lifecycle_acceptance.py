import copy
import json
import unittest
from pathlib import Path

from ci.openmath_lifecycle_acceptance import AcceptanceError, run_acceptance, validate_successor_progress


class OpenMathLifecycleAcceptanceTest(unittest.TestCase):
    def test_protected_lifecycle_merge_wakes_programme_without_manual_poll(self):
        workflow=(Path(__file__).resolve().parents[1]/".github/workflows/openmath-cex-independent-contribution-intake.yml").read_text()
        self.assertIn('branches: [main]',workflow)
        self.assertIn('"contributions/OPENMATH-2026/**/lifecycle/**/MANIFEST.json"',workflow)
        self.assertIn("github.event_name == 'push'",workflow)
        self.assertIn('event_type=openmath-return-ready',workflow)
        self.assertNotIn('github.event.client_payload',workflow)

    def test_historical_successor_requires_closed_protected_chain(self):
        registry=json.loads((Path(__file__).resolve().parents[1]/".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json").read_text())
        validate_successor_progress(registry, "OM26-H2-WP03")
        for field, value in (("closed", False), ("pipeline_state", "READY")):
            broken=copy.deepcopy(registry)
            predecessor=next(x for x in broken["assignments"] if x["assignment_id"]=="OM26-H2-WP03")
            predecessor["lifecycle"][field]=value
            with self.assertRaises(AcceptanceError):
                validate_successor_progress(broken, "OM26-H2-WP03")
        broken=copy.deepcopy(registry)
        current_id=broken["mathematics_release_policy"]["per_hill"]["OM26-H2"]["assignment"]
        current=next(x for x in broken["assignments"] if x["assignment_id"]==current_id)
        current["prerequisites"]["predecessor_assignment"]="OM26-H3-WP02"
        with self.assertRaises(AcceptanceError):
            validate_successor_progress(broken, "OM26-H2-WP03")

    def test_h2_wp02_returned_to_advanced_unattended(self):
        report = run_acceptance()
        self.assertEqual(
            report["pipeline"],
            ["RETURNED", "CAPTURED", "REPLAYED", "ADJUDICATED", "ADVANCED"],
        )
        self.assertEqual(report["result"], "PASS")
        self.assertFalse(report["manual_transport_required"])
        self.assertFalse(report["manual_controller_wake_required"])
        self.assertFalse(report["conversational_reconciliation_required"])
        self.assertEqual(
            report["adjudication"],
            "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED",
        )
        self.assertEqual(report["successor"]["assignment_id"], "OM26-H2-WP03")


if __name__ == "__main__":
    unittest.main()

import unittest
from pathlib import Path

from ci.openmath_lifecycle_acceptance import run_acceptance


class OpenMathLifecycleAcceptanceTest(unittest.TestCase):
    def test_protected_lifecycle_merge_wakes_programme_without_manual_poll(self):
        workflow=(Path(__file__).resolve().parents[1]/".github/workflows/openmath-cex-independent-contribution-intake.yml").read_text()
        self.assertIn('branches: [main]',workflow)
        self.assertIn('"contributions/OPENMATH-2026/**/lifecycle/**/MANIFEST.json"',workflow)
        self.assertIn("github.event_name == 'push'",workflow)
        self.assertIn('event_type=openmath-return-ready',workflow)
        self.assertNotIn('github.event.client_payload',workflow)

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

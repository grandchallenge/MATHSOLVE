import unittest

from ci.openmath_lifecycle_acceptance import run_acceptance


class OpenMathLifecycleAcceptanceTest(unittest.TestCase):
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

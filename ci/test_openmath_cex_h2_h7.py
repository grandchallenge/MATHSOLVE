import unittest

from ci.validate_openmath_cex_h2_h7 import EXPECTED_SLOTS, OPERATION, load, validate


class OpenMathCEXH2H7Test(unittest.TestCase):
    def test_preflight(self):
        self.assertEqual(validate(), [])

    def test_exact_lane_set(self):
        prep = load("work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json")
        self.assertEqual([lane["slot"] for lane in prep["lanes"]], EXPECTED_SLOTS)

    def test_no_early_solve_release(self):
        prep = load("work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json")
        self.assertTrue(all(lane["solve_release"] is False for lane in prep["lanes"]))
        self.assertTrue(all(lane["exact_hill_id"] is None for lane in prep["lanes"]))

    def test_routing_registration(self):
        routing = load(".ghos-routing/workflows.json")
        path = ".github/workflows/openmath-h2-h7-cex-source-acq.yml"
        entries = [entry for entry in routing["workflows"] if entry["path"] == path]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["observed_features"], ["OPAQUE_EXECUTION"])
        self.assertEqual(entries[0]["topology"], "PERSISTENT_CONTROLLER_REQUIRED")
        self.assertEqual(entries[0]["controller_id"], "GITHUB_ACTIONS")

    def test_operation_firewall(self):
        op = load(f".gcl/operations/{OPERATION}/OPERATION.json")
        self.assertFalse(op["scope"]["may_author_hill_mathematics"])
        self.assertFalse(op["scope"]["may_certify"])
        self.assertFalse(op["scope"]["may_submit_competition_entry"])


if __name__ == "__main__":
    unittest.main()

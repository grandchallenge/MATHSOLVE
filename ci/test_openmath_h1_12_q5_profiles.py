import unittest

from ci.validate_openmath_h1_12_q5_profiles import (
    COARSE_PROFILES,
    EXPECTED,
    coarse_profiles,
    local_options,
    profile_summary,
)


class H112Q5ProfilesTest(unittest.TestCase):
    def test_coarse_profile_set(self):
        self.assertEqual(coarse_profiles(), COARSE_PROFILES)

    def test_sector_local_options_exist(self):
        for r in (3, 4, 5):
            for d2 in range(5):
                self.assertTrue(local_options(r, d2))

    def test_expected_survivor_ranges(self):
        for profile, expected in EXPECTED.items():
            observed = profile_summary(profile)
            self.assertEqual(observed["state_count"], expected["state_count"])
            self.assertEqual(observed["D2_values"], expected["D2"])

    def test_excluded_profiles_have_no_state(self):
        for profile in COARSE_PROFILES:
            if profile in EXPECTED:
                continue
            self.assertEqual(profile_summary(profile)["state_count"], 0)


class H1Q6ReplayClosureTest(unittest.TestCase):
    def test_full_graph_replay_matches_durable_receipt(self):
        import json
        from pathlib import Path
        from ci.validate_openmath_h1_q6_replay import replay
        receipt = Path(__file__).resolve().parents[1] / "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/H1_Q6_INTERNAL_REPLAY_RECEIPT.json"
        self.assertEqual(json.loads(json.dumps(replay())), json.loads(receipt.read_text()))


class H1GeometricPremiseAuditTest(unittest.TestCase):
    def test_six_core_geometry_and_charge_certificates(self):
        import json
        from pathlib import Path
        from ci.validate_openmath_h1_geometric_premises import replay
        receipt = Path(__file__).resolve().parents[1] / "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/H1_SIX_CORE_PREMISE_AUDIT_RECEIPT.json"
        self.assertEqual(json.loads(json.dumps(replay())), json.loads(receipt.read_text()))


class H1PrismObstructionTest(unittest.TestCase):
    def test_saturated_words_and_all_prism_triangle_certificates(self):
        import json
        from pathlib import Path
        from ci.validate_openmath_h1_prism_obstruction import replay
        receipt = Path(__file__).resolve().parents[1] / "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/H1_SATURATED_PRISM_OBSTRUCTION_RECEIPT.json"
        self.assertEqual(replay(), json.loads(receipt.read_text()))


if __name__ == "__main__":
    unittest.main()

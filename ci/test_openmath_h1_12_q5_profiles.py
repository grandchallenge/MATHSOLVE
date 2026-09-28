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


if __name__ == "__main__":
    unittest.main()

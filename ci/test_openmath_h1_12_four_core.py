import unittest

from ci.validate_openmath_h1_12_four_core import (
    EXPECTED_MIN_D2,
    EXPECTED_PROFILES,
    enumerate_states,
    profile_candidates,
)


class H112FourCoreReplayTest(unittest.TestCase):
    def test_exact_profile_set(self):
        self.assertEqual(profile_candidates(), EXPECTED_PROFILES)

    def test_minimum_core_sharing(self):
        states = enumerate_states()
        observed = {}
        for profile in EXPECTED_PROFILES:
            rows = [
                row
                for row in states
                if tuple(row["multiplicities"]) == profile
            ]
            self.assertTrue(rows)
            observed[profile] = min(row["D2"] for row in rows)
        self.assertEqual(observed, EXPECTED_MIN_D2)

    def test_dense_profiles_force_complete_core_graph(self):
        states = enumerate_states()
        for profile in ((3, 3, 3, 5), (3, 4, 4, 4)):
            rows = [
                row
                for row in states
                if tuple(row["multiplicities"]) == profile
            ]
            self.assertTrue(rows)
            self.assertTrue(all(row["D2"] == 6 for row in rows))

    def test_3344_requires_at_least_five_core_edges(self):
        rows = [
            row
            for row in enumerate_states()
            if tuple(row["multiplicities"]) == (3, 3, 4, 4)
        ]
        self.assertTrue(rows)
        self.assertGreaterEqual(min(row["D2"] for row in rows), 5)


if __name__ == "__main__":
    unittest.main()

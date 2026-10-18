import unittest

from ci.validate_openmath_h1_12_saturated_core import (
    reduced_states,
    saturated_count,
)
from ci.validate_openmath_h1_12_four_core import enumerate_states


class H112SaturatedCoreReductionTest(unittest.TestCase):
    def test_dense_profiles_require_multiple_saturated_cores(self):
        original = enumerate_states()
        for profile in (
            (3, 3, 3, 5),
            (3, 3, 4, 4),
            (3, 4, 4, 4),
        ):
            rows = [
                s for s in original
                if tuple(s["multiplicities"]) == profile
            ]
            self.assertTrue(rows)
            self.assertTrue(all(s["D2"] >= 5 for s in rows))
            self.assertTrue(all(saturated_count(s) >= 2 for s in rows))

    def test_reduced_profiles(self):
        rows = reduced_states()
        profiles = sorted({tuple(s["multiplicities"]) for s in rows})
        self.assertEqual(profiles, [(3, 3, 3, 3), (3, 3, 3, 4)])

    def test_3334_complete_core_is_removed(self):
        rows = [
            s for s in reduced_states()
            if tuple(s["multiplicities"]) == (3, 3, 3, 4)
        ]
        self.assertTrue(rows)
        self.assertEqual(sorted({s["D2"] for s in rows}), [3, 4, 5])

    def test_3333_retains_all_d2_levels(self):
        rows = [
            s for s in reduced_states()
            if tuple(s["multiplicities"]) == (3, 3, 3, 3)
        ]
        self.assertTrue(rows)
        self.assertEqual(
            sorted({s["D2"] for s in rows}),
            [1, 2, 3, 4, 5, 6],
        )
        self.assertLessEqual(max(saturated_count(s) for s in rows), 1)


if __name__ == "__main__":
    unittest.main()

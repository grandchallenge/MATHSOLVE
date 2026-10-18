import unittest
from collections import Counter

from ci.validate_openmath_h1_12_3333_normal_form import (
    EXPECTED_D2_HISTOGRAM,
    EXPECTED_ORBITS,
    local_blocked_minimum,
    orbit_summary,
    profile_states,
    refined_states,
)


class H112Profile3333NormalFormTest(unittest.TestCase):
    def test_protected_input_and_refined_count(self):
        self.assertEqual(len(profile_states()), 344)
        self.assertEqual(len(refined_states()), 108)

    def test_local_positive_blocked_minima(self):
        self.assertEqual(local_blocked_minimum(2, 2), 1)
        self.assertEqual(local_blocked_minimum(3, 3), 3)

    def test_d2_histogram_and_d2_six_elimination(self):
        rows = refined_states()
        hist = dict(sorted(Counter(row["D2"] for row in rows).items()))
        self.assertEqual(hist, EXPECTED_D2_HISTOGRAM)
        self.assertNotIn(6, hist)

    def test_exact_symmetry_quotient(self):
        self.assertEqual(orbit_summary(refined_states()), EXPECTED_ORBITS)

    def test_six_charge_equality_normal_forms(self):
        rows = orbit_summary(refined_states())
        equality = [row for row in rows if row["clean"] == row["capacity"]]
        self.assertEqual(len(equality), 6)


if __name__ == "__main__":
    unittest.main()

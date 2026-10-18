import unittest

from ci.validate_openmath_h1_12_3333_nonsat_star import (
    has_three_consecutive_d2,
    hub_patterns,
    target_orbit,
)


class H112Profile3333NonSatStarTest(unittest.TestCase):
    def test_target_equality_form(self):
        row = target_orbit()
        self.assertEqual((row["D2"], row["D1"], row["U"]), (3, 7, 1))
        self.assertEqual((row["clean"], row["capacity"]), (9, 9))

    def test_unblocked_hub_d1_forces_d2_block(self):
        rows = hub_patterns()
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(has_three_consecutive_d2(row) for row in rows))

    def test_strict_incidence_breaks_equality(self):
        row = target_orbit()
        self.assertGreater(10, row["capacity"])


if __name__ == "__main__":
    unittest.main()

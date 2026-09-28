import unittest

from ci.validate_openmath_h1_12_3333_d2_3_star import (
    has_three_consecutive_d2,
    hub_equality_patterns,
    remaining_orbits,
)


class H112Profile3333D23StarTest(unittest.TestCase):
    def test_six_zero_block_hub_patterns(self):
        rows = hub_equality_patterns()
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(has_three_consecutive_d2(row) for row in rows))

    def test_residual_size(self):
        rows = remaining_orbits()
        self.assertEqual(len(rows), 6)
        self.assertEqual(sum(row["labeled"] for row in rows), 41)

    def test_target_star_removed(self):
        self.assertFalse(any(
            row["D2"] == 3
            and tuple(row["degrees"]) == (3, 1, 1, 1)
            and tuple(row["d1"]) == (1, 2, 2, 2)
            and row["saturated"] == 0
            for row in remaining_orbits()
        ))


if __name__ == "__main__":
    unittest.main()

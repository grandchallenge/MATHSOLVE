import unittest

from ci.validate_openmath_h1_12_3333_saturated_equality import (
    leaf_d1_choices,
    saturated_equality_orbit,
)


class H112Profile3333SaturatedEqualityTest(unittest.TestCase):
    def test_target_form(self):
        row = saturated_equality_orbit()
        self.assertEqual((row["D2"], row["D1"], row["U"]), (3, 9, 3))
        self.assertEqual((row["clean"], row["capacity"]), (12, 12))
        self.assertEqual(row["labeled"], 4)

    def test_leaf_equality_forces_outward_side_rays(self):
        self.assertEqual(leaf_d1_choices(), [(3, 5)])


if __name__ == "__main__":
    unittest.main()

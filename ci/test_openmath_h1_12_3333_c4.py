import unittest

from ci.validate_openmath_h1_12_3333_c4 import (
    equality_local_patterns,
    forces_neighbor_line,
    local_types,
    residual_orbits,
)


class H112Profile3333C4Test(unittest.TestCase):
    def test_eighteen_equality_local_patterns(self):
        self.assertEqual(len(equality_local_patterns()), 18)

    def test_two_dihedral_local_types(self):
        self.assertEqual(
            local_types(),
            [
                (0, 1, 0, 1, 2, 2),
                (0, 1, 0, 2, 1, 2),
            ],
        )

    def test_every_local_type_forces_neighbor_line(self):
        mechanisms = {
            forces_neighbor_line(word) for word in equality_local_patterns()
        }
        self.assertEqual(
            mechanisms,
            {"ADJACENT_D2", "BLOCKED_D1_BETWEEN"},
        )
        self.assertNotIn(None, mechanisms)

    def test_residual_is_seven_forms_without_d2_four(self):
        rows = residual_orbits()
        self.assertEqual(len(rows), 7)
        self.assertEqual(sum(row["labeled"] for row in rows), 45)
        self.assertTrue(all(row["D2"] <= 3 for row in rows))


if __name__ == "__main__":
    unittest.main()

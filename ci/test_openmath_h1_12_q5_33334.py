import unittest

from ci.validate_openmath_h1_12_q5_33334 import (
    EXPECTED_ORBITS,
    quotient,
)


class H112Q533334Test(unittest.TestCase):
    def test_exact_five_orbits(self):
        retained, orbits = quotient()
        self.assertEqual(len(retained), 60)
        self.assertEqual(len(orbits), 5)
        self.assertEqual(
            [row["orbit_size"] for row in orbits],
            [6, 12, 24, 12, 6],
        )

    def test_every_orbit_has_two_saturated_triples(self):
        _, orbits = quotient()
        for row in orbits:
            self.assertEqual(len(row["saturated"]), 2)
            self.assertNotIn(4, row["saturated"])

    def test_separator_filter_leaves_only_k23(self):
        _, orbits = quotient()
        survivors = [row for row in orbits if row["separator_ok"]]
        self.assertEqual(len(survivors), 1)
        row = survivors[0]
        self.assertEqual(row["D2"], 6)
        self.assertEqual(
            set(row["edges"]),
            {
                (0,1),(0,2),(0,4),
                (1,3),(2,3),(3,4),
            },
        )
        self.assertEqual(tuple(sorted(row["saturated"])), (0,3))


if __name__ == "__main__":
    unittest.main()

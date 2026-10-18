import unittest

from ci.validate_openmath_h1_12_3334_d2_3 import (
    D1,
    D2,
    I,
    N,
    cyclic_patterns,
    every_d1_between_two_d2,
    every_d1_touches_d2,
)


class H112Profile3334D23Test(unittest.TestCase):
    def test_triple_hub_alternates(self):
        rows = cyclic_patterns(length=6, d1_count=3, forbidden_run=2)
        self.assertEqual(
            set(rows),
            {
                (0, 1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1, 0),
            },
        )
        self.assertTrue(all(every_d1_between_two_d2(row) for row in rows))

    def test_quadruple_hub_every_d1_touches_d2(self):
        rows = cyclic_patterns(length=8, d1_count=5, forbidden_run=3)
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(every_d1_touches_d2(row) for row in rows))

    def test_quadruple_hub_charge_capacity_fails(self):
        clean_lower = N - (I - D2)
        charge_capacity = D1 - 5
        self.assertEqual((clean_lower, charge_capacity), (8, 6))
        self.assertGreater(clean_lower, charge_capacity)

    def test_triple_hub_strengthened_line_count_fails_capacity(self):
        h_upper = I - 5
        clean_lower = N - h_upper
        charge_capacity = D1 - 3
        self.assertEqual((h_upper, clean_lower, charge_capacity), (8, 10, 8))
        self.assertGreater(clean_lower, charge_capacity)


if __name__ == "__main__":
    unittest.main()

import unittest

from ci.validate_openmath_h1_12_3334_d2_5 import (
    D1,
    D2,
    I,
    N,
    U,
    binary_patterns,
    every_d1_touches_d2,
)


class H112Profile3334D25Test(unittest.TestCase):
    def test_triple_hub_alternates(self):
        rows = binary_patterns(6, 3, 2)
        self.assertEqual(
            set(rows),
            {
                (0, 1, 0, 1, 0, 1),
                (1, 0, 1, 0, 1, 0),
            },
        )

    def test_quadruple_hub_every_d1_touches_d2(self):
        rows = binary_patterns(8, 5, 3)
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(every_d1_touches_d2(row) for row in rows))

    def test_clean_line_lower_bound(self):
        self.assertEqual(N - (I - D2), 10)

    def test_triple_hub_capacity(self):
        self.assertGreater(N - (I - D2), (D1 - 3) + 2 * U)

    def test_quadruple_hub_capacity(self):
        self.assertGreater(N - (I - D2), (D1 - 5) + 2 * U)


if __name__ == "__main__":
    unittest.main()

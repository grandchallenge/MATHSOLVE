import unittest

from ci.validate_openmath_h1_12_3334_d2_5 import (
    D1,
    D2,
    I,
    N,
    U,
    cyclic_patterns,
    every_d1_touches_d2,
)


class H112Profile3334D25Test(unittest.TestCase):
    def test_triple_hub_alternates(self):
        rows = cyclic_patterns(6, 3, 2)
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(every_d1_touches_d2(row) for row in rows))

    def test_quadruple_hub_every_d1_touches_d2(self):
        rows = cyclic_patterns(8, 5, 3)
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(every_d1_touches_d2(row) for row in rows))

    def test_capacity_contradictions(self):
        clean = N - (I - D2)
        self.assertEqual(clean, 10)
        self.assertGreater(clean, (D1 - 3) + 2 * U)
        self.assertGreater(clean, (D1 - 5) + 2 * U)


if __name__ == "__main__":
    unittest.main()

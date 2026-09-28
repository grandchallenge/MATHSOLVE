import unittest

from ci.validate_openmath_h1_12_3334_d2_4 import (
    D2,
    I,
    N,
    min_touching,
)


class H112Profile3334D24Test(unittest.TestCase):
    def test_local_cyclic_minimums(self):
        self.assertEqual(min_touching(6, 2, 2, 2)[0], 1)
        self.assertEqual(min_touching(8, 4, 2, 3)[0], 1)

    def test_cycle_capacity(self):
        clean = N - (I - D2)
        self.assertEqual(clean, 9)
        self.assertGreater(clean, 10 - 4)

    def test_q_hub_capacities(self):
        clean = N - (I - D2)
        self.assertGreater(clean, (10 - 5) + 2 * 0)
        self.assertGreater(clean, (11 - 5) + 2 * 1)

    def test_t_hub_capacities(self):
        clean = N - (I - 5)
        self.assertEqual(clean, 10)
        self.assertGreater(clean, (10 - 3) + 2 * 0)
        self.assertGreater(clean, (11 - 4) + 2 * 1)


if __name__ == "__main__":
    unittest.main()

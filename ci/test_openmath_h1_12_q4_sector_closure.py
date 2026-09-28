import unittest

from ci.validate_openmath_h1_12_q4_sector_closure import (
    blocked_minimum,
    budget,
)


class H112Q4SectorClosureTest(unittest.TestCase):
    def test_local_blocked_minima(self):
        self.assertEqual(blocked_minimum(2, 1)[0], 2)
        self.assertEqual(blocked_minimum(2, 2)[0], 2)
        self.assertEqual(blocked_minimum(2, 0)[0], 0)

    def test_single_edge_fails(self):
        clean, capacity = budget(1, 0, 4)
        self.assertEqual((clean, capacity), (7, 4))
        self.assertGreater(clean, capacity)

    def test_p3_isolated_fails(self):
        clean, capacity = budget(2, 1, 6)
        self.assertEqual((clean, capacity), (8, 4))
        self.assertGreater(clean, capacity)

    def test_two_disjoint_edges_fails(self):
        clean, capacity = budget(2, 1, 8)
        self.assertEqual((clean, capacity), (8, 2))
        self.assertGreater(clean, capacity)

    def test_p4_crosscheck(self):
        clean, capacity = budget(3, 2, 8)
        self.assertEqual((clean, capacity), (9, 4))
        self.assertGreater(clean, capacity)


if __name__ == "__main__":
    unittest.main()

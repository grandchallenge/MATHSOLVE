import unittest

from ci.validate_openmath_h1_12_3333_p4 import (
    local_patterns,
    target_orbit,
)


class H112Profile3333P4Test(unittest.TestCase):
    def test_target_form(self):
        row = target_orbit()
        self.assertEqual((row["D2"], row["D1"], row["U"]), (3, 8, 2))
        self.assertEqual(row["labeled"], 12)

    def test_one_blocked_patterns_force_neighbor_line(self):
        rows = [item for item in local_patterns() if item[1] == 1]
        self.assertTrue(rows)
        self.assertTrue(all(item[2] is not None for item in rows))

    def test_three_budget_regimes_fail(self):
        # (blocked lower bound, extra incidence savings)
        for blocked, extra in ((2, 2), (3, 1), (4, 0)):
            clean = 18 - (12 - 3 - extra)
            capacity = 4 + 8 - blocked
            self.assertGreater(clean, capacity)


if __name__ == "__main__":
    unittest.main()

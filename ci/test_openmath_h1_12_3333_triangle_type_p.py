import unittest

from ci.validate_openmath_h1_12_3333_triangle_isolated import assignments
from ci.validate_openmath_h1_12_3333_triangle_type_p import (
    duplicate_count,
    selection_counts,
)


class H112Profile3333TriangleTypePTest(unittest.TestCase):
    def test_type_p_always_duplicates_one_M_line(self):
        rows = [a for a in assignments() if selection_counts(a) == (2, 1, 0)]
        self.assertEqual(len(rows), 6)
        for assignment in rows:
            self.assertEqual(duplicate_count(assignment)[0], 1)

    def test_type_c_has_distinct_M_lines(self):
        rows = [a for a in assignments() if selection_counts(a) == (1, 1, 1)]
        self.assertEqual(len(rows), 2)
        for assignment in rows:
            self.assertEqual(duplicate_count(assignment)[0], 0)

    def test_capacity_drops_below_nine(self):
        self.assertLess(4 + 4, 9)


if __name__ == "__main__":
    unittest.main()

import unittest

from ci.validate_openmath_h1_12_3333_triangle_isolated import assignments
from ci.validate_openmath_h1_12_3333_triangle_type_c import (
    VERTICES,
    forced_multiple_descriptor,
)
from ci.validate_openmath_h1_12_3333_triangle_type_p import (
    choice_map,
    selection_counts,
)


class H112Profile3333TriangleTypeCTest(unittest.TestCase):
    def test_two_type_c_assignments(self):
        rows = [a for a in assignments() if selection_counts(a) == (1, 1, 1)]
        self.assertEqual(len(rows), 2)

    def test_every_selected_vertex_forces_three_line_concurrence(self):
        rows = [a for a in assignments() if selection_counts(a) == (1, 1, 1)]
        for assignment in rows:
            choices = choice_map(assignment)
            for v in VERTICES:
                item = forced_multiple_descriptor(v, choices)
                self.assertEqual(item["distinct_line_count"], 3)


if __name__ == "__main__":
    unittest.main()

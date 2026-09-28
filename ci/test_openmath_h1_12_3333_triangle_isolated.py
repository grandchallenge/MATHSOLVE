import unittest

from ci.validate_openmath_h1_12_3333_triangle_isolated import (
    adjacent_d2_local_words,
    assignments,
    selection_multiplicities,
    target_orbit,
)


class H112Profile3333TriangleIsolatedTest(unittest.TestCase):
    def test_target_equality_form(self):
        row = target_orbit()
        self.assertEqual((row["D2"], row["D1"], row["U"]), (3, 8, 2))
        self.assertEqual((row["clean"], row["capacity"]), (9, 9))
        self.assertEqual(row["labeled"], 4)

    def test_adjacent_d2_has_two_reflected_words(self):
        self.assertEqual(
            set(adjacent_d2_local_words()),
            {
                (2, 2, 0, 1, 0, 1),
                (2, 2, 1, 0, 1, 0),
            },
        )

    def test_two_orientation_types(self):
        hist = {}
        for assignment in assignments():
            key = selection_multiplicities(assignment)
            hist[key] = hist.get(key, 0) + 1
        self.assertEqual(hist, {(1, 1, 1): 2, (2, 1, 0): 6})


if __name__ == "__main__":
    unittest.main()

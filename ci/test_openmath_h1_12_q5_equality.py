import unittest

from ci.validate_openmath_h1_12_q5_equality import (
    d1_positions,
    isolated_local_words,
    sole_q5_case,
    triangle_local_words,
)


class H112Q5EqualityTest(unittest.TestCase):
    def test_exact_equality_case(self):
        row = sole_q5_case()
        equality = {
            (
                state["D1"],
                state["U"],
                state["blocked"],
                state["clean"],
                state["capacity"],
            )
            for state in row["states"]
            if state["saturated"] == ()
        }
        self.assertEqual(equality, {(10,1,6,6,6)})

    def test_triangle_word_is_unique(self):
        rows = triangle_local_words()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], (2,2,1,0,0,1))
        self.assertEqual(d1_positions(rows[0][1]), (2,5))

    def test_isolated_D1_rays_are_antipodal(self):
        rows = isolated_local_words()
        self.assertEqual(len(rows), 3)
        for _, word in rows:
            a, b = d1_positions(word)
            self.assertEqual((b-a) % 6, 3)


if __name__ == "__main__":
    unittest.main()

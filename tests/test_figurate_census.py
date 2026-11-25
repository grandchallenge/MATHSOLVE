"""FIGURATE census independent bounded brute-force regressions."""
import itertools
import unittest
from math import isqrt
from research.figurate_census import census, polygonal, polygonal_index, verify_tuple


class FigurateTests(unittest.TestCase):
    def test_polygonal_roundtrip(self):
        for k in range(3, 13):
            for t in range(1, 100):
                self.assertEqual(polygonal_index(k, polygonal(k, t)), t)

    def test_nonmembers(self):
        self.assertIsNone(polygonal_index(3, 2))
        self.assertIsNone(polygonal_index(4, 3))
        self.assertIsNone(polygonal_index(5, 2))
        self.assertIsNone(polygonal_index(3, -1))

    def test_known_classical_quadruple(self):
        self.assertEqual(len(verify_tuple((1, 3, 8, 120), "B", 4, 1)), 6)

    def test_triangular_output_example(self):
        self.assertEqual(verify_tuple((1, 2, 27), "B", 3, 1),
                         {"1,2": 2, "1,27": 7, "2,27": 10})

    def test_distinct_positive(self):
        self.assertIsNone(verify_tuple((1, 1, 2), "B", 3, 1))
        self.assertIsNone(verify_tuple((0, 1), "B", 3, 1))

    def test_bruteforce_independent(self):
        for kind, k, offset, limit, size in [
            ("A", 3, 1, 40, 2), ("A", 3, 1, 40, 3),
            ("B", 3, 1, 35, 3), ("B", 5, -1, 30, 2),
            ("C", 4, 1, 40, 2),
        ]:
            fig = {polygonal(k, t) for t in range(1, limit + 1)}
            candidates = range(1, limit + 1) if kind == "B" else sorted(
                a for a in fig if a <= limit)
            expected = set()
            for values in itertools.combinations(candidates, size):
                valid = True
                for a, b in itertools.combinations(values, 2):
                    z = a * b + offset
                    if kind == "A":
                        valid &= z >= 0 and isqrt(max(0, z)) ** 2 == z
                    else:
                        valid &= z in {polygonal(k, t) for t in range(1, z + 1)} if z > 0 else False
                    if not valid:
                        break
                if valid:
                    expected.add(values)
            actual = census(kind, k, offset, limit, size)
            self.assertEqual({tuple(item["values"]) for item in actual}, expected)
            for item in actual:
                self.assertEqual(item["witnesses"], verify_tuple(
                    tuple(item["values"]), kind, k, offset))


if __name__ == "__main__":
    unittest.main()

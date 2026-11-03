"""FIGURATE L60 archive regression: source-to-data replay and independent spot check."""
import itertools
import unittest
from math import isqrt

from research.figurate_census import census
from research.figurate_census_replay import replay


class FIGURATEArchiveTests(unittest.TestCase):
    def test_full_archive_replay(self):
        self.assertEqual(replay(), {"A": 112, "B": 1490, "C": 138})

    def test_bruteforce_independent_selected(self):
        for kind, k, c, size, limit in (
            ("A", 3, 1, 3, 40), ("A", 4, 0, 4, 30),
            ("B", 3, 1, 3, 35), ("B", 5, -1, 3, 60),
            ("C", 3, 0, 3, 30), ("C", 4, 0, 4, 30),
        ):
            def poly(t):
                return ((k - 2) * t * t - (k - 4) * t) // 2
            polygonal = {poly(t) for t in range(1, limit * limit + 2)}
            domain = range(1, limit + 1) if kind == "B" else sorted(
                z for z in polygonal if 1 <= z <= limit
            )
            count = 0
            for values in itertools.combinations(domain, size):
                good = True
                for a, b in itertools.combinations(values, 2):
                    z = a * b + c
                    if kind == "A":
                        good = z >= 0 and isqrt(max(z, 0)) ** 2 == z
                    else:
                        good = z in polygonal
                    if not good:
                        break
                count += good
            self.assertEqual(len(census(kind, k, c, limit, size)), count)


if __name__ == "__main__":
    unittest.main()

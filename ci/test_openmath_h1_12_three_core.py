import unittest

from ci.validate_openmath_h1_12_three_core import (
    enumerate_feasible,
    sector_patterns,
)


class H112ThreeCoreArithmeticTest(unittest.TestCase):
    def test_unique_surviving_template(self):
        self.assertEqual(
            enumerate_feasible(),
            [
                {
                    "multiplicities": [3, 3, 3],
                    "core_edges": [[0, 1], [0, 2], [1, 2]],
                    "core_degrees": [2, 2, 2],
                    "local_d1": [2, 2, 2],
                    "D1": 6,
                    "D2": 3,
                    "U": 3,
                    "I": 9,
                    "S": 9,
                    "min_clean": 12,
                }
            ],
        )

    def test_four_shared_rays_force_one_nontriangular_sector(self):
        patterns = sector_patterns(3, 4)
        self.assertTrue(patterns)
        self.assertTrue(
            all(sum(1 - bit for bit in pattern) == 1 for pattern in patterns)
        )

    def test_seven_of_eight_shared_rays_is_impossible(self):
        self.assertEqual(sector_patterns(4, 7), [])


if __name__ == "__main__":
    unittest.main()

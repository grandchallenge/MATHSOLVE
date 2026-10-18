import unittest

from ci.validate_openmath_h1_12_q5_33333 import (
    EXPECTED_HISTOGRAM,
    EXPECTED_ORBIT_COUNTS,
    quotient,
    separator_cases,
)


class H112Q533333Test(unittest.TestCase):
    def test_exact_state_and_orbit_counts(self):
        retained, orbits = quotient()
        self.assertEqual(len(retained), 595)
        self.assertEqual(len(orbits), 15)

    def test_separator_filter_leaves_four_cases(self):
        _, orbits = quotient()
        cases = separator_cases(orbits)
        self.assertEqual(
            [row["kind"] for row in cases],
            [
                "STAR_PLUS_ISOLATED",
                "TRIANGLE_PLUS_TWO_ISOLATED",
                "STAR_PLUS_TWO_ATTACHMENTS",
                "K2_3",
            ],
        )

    def test_triangle_is_unique_post_geometry_survivor(self):
        _, orbits = quotient()
        cases = separator_cases(orbits)
        triangle = [x for x in cases if x["kind"] == "TRIANGLE_PLUS_TWO_ISOLATED"]
        self.assertEqual(len(triangle), 1)
        self.assertEqual(triangle[0]["D2"], 3)
        self.assertEqual(triangle[0]["saturated"], ())


if __name__ == "__main__":
    unittest.main()

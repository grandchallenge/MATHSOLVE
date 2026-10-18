import unittest

from ci.validate_openmath_h1_12_q5_saturation import (
    EXPECTED_MIN_SATURATION,
    EXPECTED_RETAINED,
    retained_summary,
    saturation_summary,
)


class H112Q5SaturationTest(unittest.TestCase):
    def test_minimum_saturation_tables(self):
        for profile, expected in EXPECTED_MIN_SATURATION.items():
            self.assertEqual(saturation_summary(profile), expected)

    def test_retained_ranges(self):
        for profile, expected in EXPECTED_RETAINED.items():
            observed = retained_summary(profile)
            self.assertEqual(observed["state_count"], expected["state_count"])
            self.assertEqual(observed["D2_values"], expected["D2_values"])

    def test_33344_is_eliminated(self):
        self.assertEqual(
            retained_summary((3, 3, 3, 4, 4))["state_count"],
            0,
        )


if __name__ == "__main__":
    unittest.main()

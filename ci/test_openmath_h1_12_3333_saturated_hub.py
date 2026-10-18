import unittest

from ci.validate_openmath_h1_12_3333_saturated_hub import (
    has_saturated_triple_hub,
    reduced_orbits,
)
from ci.validate_openmath_h1_12_3333_normal_form import EXPECTED_ORBITS


class H112Profile3333SaturatedHubTest(unittest.TestCase):
    def test_five_input_saturated_forms(self):
        self.assertEqual(
            sum(has_saturated_triple_hub(row) for row in EXPECTED_ORBITS),
            5,
        )

    def test_residual_size(self):
        rows = reduced_orbits()
        self.assertEqual(len(rows), 8)
        self.assertEqual(sum(row["labeled"] for row in rows), 48)

    def test_d2_histogram(self):
        rows = reduced_orbits()
        hist = {
            d2: sum(row["labeled"] for row in rows if row["D2"] == d2)
            for d2 in sorted({row["D2"] for row in rows})
        }
        self.assertEqual(hist, {1: 6, 2: 15, 3: 24, 4: 3})

    def test_only_saturated_residual_is_d2_three_equality(self):
        rows = [
            row for row in reduced_orbits()
            if has_saturated_triple_hub(row)
        ]
        self.assertEqual(len(rows), 1)
        self.assertEqual(
            (rows[0]["D2"], rows[0]["clean"], rows[0]["capacity"]),
            (3, 12, 12),
        )

    def test_d2_four_is_only_nonsaturated_cycle(self):
        rows = [row for row in reduced_orbits() if row["D2"] == 4]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["saturated"], 0)
        self.assertEqual(tuple(rows[0]["degrees"]), (2, 2, 2, 2))

    def test_four_equality_forms_remain(self):
        rows = reduced_orbits()
        self.assertEqual(
            sum(row["clean"] == row["capacity"] for row in rows),
            4,
        )


if __name__ == "__main__":
    unittest.main()

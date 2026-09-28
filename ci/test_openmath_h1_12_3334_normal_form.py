import unittest
from collections import Counter

from ci.validate_openmath_h1_12_3334_normal_form import (
    EXPECTED_ROLE_COUNTS,
    descriptor,
    profile_states,
    saturated_vertices,
)


class H112Profile3334NormalFormTest(unittest.TestCase):
    def test_state_and_role_counts(self):
        rows = profile_states()
        self.assertEqual(len(rows), 67)
        self.assertEqual(
            Counter(row["D2"] for row in rows),
            Counter({3: 4, 4: 51, 5: 12}),
        )
        self.assertEqual(
            Counter(descriptor(row) for row in rows),
            Counter(EXPECTED_ROLE_COUNTS),
        )

    def test_d2_three_is_star_with_one_saturated_hub(self):
        rows = [row for row in profile_states() if row["D2"] == 3]
        self.assertTrue(rows)
        for row in rows:
            sats = saturated_vertices(row)
            self.assertEqual(len(sats), 1)
            self.assertEqual(row["core_degrees"][sats[0]], 3)
            self.assertEqual((row["D1"], row["U"]), (11, 0))

    def test_d2_four_cycle_or_star_plus_edge(self):
        rows = [row for row in profile_states() if row["D2"] == 4]
        self.assertTrue(rows)
        for row in rows:
            sats = saturated_vertices(row)
            if not sats:
                self.assertEqual(
                    tuple(sorted(row["core_degrees"])),
                    (2, 2, 2, 2),
                )
                self.assertEqual((row["D1"], row["U"]), (10, 0))
            else:
                self.assertEqual(len(sats), 1)
                self.assertEqual(row["core_degrees"][sats[0]], 3)
                self.assertIn((row["D1"], row["U"]), ((10, 0), (11, 1)))

    def test_d2_five_is_k4_minus_outer_pair(self):
        rows = [row for row in profile_states() if row["D2"] == 5]
        self.assertTrue(rows)
        all_edges = {
            (a, b) for a in range(4) for b in range(a + 1, 4)
        }
        for row in rows:
            sats = saturated_vertices(row)
            self.assertEqual(len(sats), 1)
            hub = sats[0]
            self.assertEqual(row["core_degrees"][hub], 3)
            missing = all_edges - {tuple(edge) for edge in row["core_edges"]}
            self.assertEqual(len(missing), 1)
            self.assertNotIn(hub, next(iter(missing)))
            self.assertEqual((row["D1"], row["U"]), (10, 1))


if __name__ == "__main__":
    unittest.main()

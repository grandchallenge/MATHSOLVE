"""WP08 exact 2-adic square-normal-form arithmetic and Type B checks."""
import itertools
import unittest

from research.figurate_census import polygonal, verify_tuple
from research.figurate_wp08_square_normal_form import (
    normal_form, square_mod_power_two, polygonal_local_possible,
    polynomial_local_possible, triple_local_possible, obstruction_witness,
)
from research.figurate_wp08_2adic import local_first_triple


class FigurateSquareNormalForm(unittest.TestCase):
    def test_completed_square_integer_identity(self):
        for k in range(4, 85, 4):
            A, q = normal_form(k)
            self.assertEqual(A % 2, 1)
            for t in range(1, 301):
                self.assertEqual(
                    A * polygonal(k, t) + q * q,
                    (A * t - q) ** 2,
                )

    def test_square_predicate_against_all_square_residues(self):
        for n in range(1, 11):
            m = 1 << n
            expected = {x*x % m for x in range(m)}
            self.assertEqual(
                {x for x in range(m) if square_mod_power_two(x, n)},
                expected,
            )
        for n in (1, 2, 7):
            with self.assertRaises(ValueError):
                square_mod_power_two(5, 0)

    def test_exact_all_power_two_polygonal_images(self):
        for n in range(1, 10):
            m = 1 << n
            for k in range(4, 65, 4):
                direct = {polygonal(k, t) % m
                          for t in range(1, 2*m + 1)}
                predicted = {z for z in range(m)
                             if polygonal_local_possible(k, z, n)}
                self.assertEqual(predicted, direct, (k, n))
                self.assertEqual(
                    predicted,
                    {z for z in range(m)
                     if polynomial_local_possible(k, z, n)},
                ) if m <= 32 else None

    def test_triple_exact_local_relation_and_repeated_classes(self):
        for k in (4, 8, 12, 16, 20, 24, 32):
            for n in range(1, 7):
                m = 1 << n
                for c in (-13, -5, 0, 2, 5, 9):
                    image = {polygonal(k, t) % m
                             for t in range(1, 2*m + 1)}
                    for a, b, d in itertools.combinations_with_replacement(
                            range(min(m, 7)), 3):
                        expected = all(
                            (x*y+c) % m in image
                            for x, y in ((a, b), (a, d), (b, d)))
                        self.assertEqual(
                            triple_local_possible(k, c, (a, b, d), n),
                            expected, (k, n, c, a, b, d))

    def test_mod64_first_local_witness_matches_prior_independent(self):
        for k in (4, 8, 12, 16, 24, 28, 32, 40, 44, 48, 60, 64):
            for c in range(64):
                self.assertEqual(
                    obstruction_witness(k, c, 6),
                    local_first_triple(k, c, 64), (k, c))

    def test_new_global_cases_and_pair_nonvacuity(self):
        for k, c in ((64, 9), (80, 25), (72, 13), (76, 4),
                     (16, 5), (8, 9), (12, 2)):
            self.assertIsNone(obstruction_witness(k, c, 6))
            for t in (4, 7, 13):
                b = polygonal(k, t) - c
                if b > 1:
                    self.assertEqual(
                        verify_tuple((1, b), "B", k, c),
                        {f"1,{b}": t},
                    )

    def test_invalid_order_and_input(self):
        for k in (3, 5, 6, 7, 9):
            with self.assertRaises(ValueError):
                normal_form(k)
        with self.assertRaises(ValueError):
            triple_local_possible(8, 1, (1, 2), 4)


if __name__ == "__main__":
    unittest.main()

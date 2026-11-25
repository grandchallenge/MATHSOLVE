"""WP08: independent density, negative 2-adic squares and coherent triples."""
import itertools
import unittest

from research.figurate_census import polygonal, verify_tuple
from research.figurate_wp08_2adic_density import (
    fixed_coherent_triple, offset_immune_to_all_two_power_tests,
    polygonal_residue_count, square_residue_count, triple_passes_precision,
    two_adic_square, valuation_two,
)
from research.figurate_wp08_square_normal_form import normal_form


def independent_square_residue_set(n):
    m = 1 << n
    return {x*x % m for x in range(m)}


def independent_polygonal_image(k, n):
    m = 1 << n
    return {polygonal(k, t) % m for t in range(1, 2*m+1)}


class TwoAdicDensityCoherence(unittest.TestCase):
    def test_exact_square_and_polygonal_image_counts(self):
        for n in range(1, 13):
            squares = independent_square_residue_set(n)
            self.assertEqual(len(squares), square_residue_count(n))
            m = 1 << n
            self.assertLessEqual(abs(len(squares)/m - 1/6),
                                 10/(6*m)+1e-12)
            for k in (4,8,12,16,20,24,32,44,64):
                self.assertEqual(
                    len(independent_polygonal_image(k,n)),
                    polygonal_residue_count(k,n))

    def test_integer_2adic_square_predicate_independent_moduli(self):
        for D in range(-150,151):
            expected = all(D % (1 << n) in
                           independent_square_residue_set(n)
                           for n in range(1,11))
            # Small finite compatibility is a necessary condition, not
            # sufficient when v2(D)≥10, so check only |D|<150 and v2<8.
            if D and valuation_two(D) >= 8:
                continue
            self.assertEqual(two_adic_square(D), expected, D)
        self.assertTrue(two_adic_square(0))
        self.assertTrue(two_adic_square(-7))
        self.assertFalse(two_adic_square(-1))

    def test_fixed_coherent_witness_every_precision(self):
        for k in range(4,65,4):
            for c in range(-75,76):
                if not offset_immune_to_all_two_power_tests(k,c):
                    with self.assertRaises(ValueError):
                        fixed_coherent_triple(k,c)
                    continue
                triple = fixed_coherent_triple(k,c)
                self.assertEqual(len(set(triple)),3)
                self.assertTrue(all(x>0 for x in triple))
                for n in range(1,17):
                    self.assertTrue(triple_passes_precision(k,c,triple,n),
                                    (k,c,n,triple))
                # Large exponent checks transcend the previous mod64 table.
                self.assertTrue(triple_passes_precision(k,c,triple,32))
                self.assertTrue(triple_passes_precision(k,c,triple,64))

    def test_integer_zero_case_and_actual_positive_square_triple(self):
        self.assertEqual(fixed_coherent_triple(4,0),(1,4,16))
        self.assertIsNotNone(verify_tuple((1,4,16),"B",4,0))
        for k in range(8,165,4):
            a,q=normal_form(k)
            for c in range(-200,201):
                self.assertNotEqual(a*c+q*q,0)

    def test_immune_versus_all_previous_global_exclusions(self):
        from research.figurate_wp08_2adic import exclusions
        table=exclusions(64)
        for k in range(64,128):
            for c in table[k%64]:
                self.assertFalse(offset_immune_to_all_two_power_tests(k,c),
                                 (k,c))

    def test_negative_offset_and_surviving_multiple_k_families(self):
        for k,c in ((8,-8),(4,-7),(12,1),(16,0),(20,0),
                    (8,21),(12,12)):
            if offset_immune_to_all_two_power_tests(k,c):
                t=fixed_coherent_triple(k,c)
                self.assertTrue(triple_passes_precision(k,c,t,32))

    def test_reject_invalid_exponents_and_unsupported_orders(self):
        with self.assertRaises(ValueError):
            square_residue_count(0)
        with self.assertRaises(ValueError):
            polygonal_residue_count(6,4)
        with self.assertRaises(ValueError):
            valuation_two(0)


if __name__ == "__main__":
    unittest.main()

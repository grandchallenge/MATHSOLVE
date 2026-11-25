"""Independent regression for WP09 infinite odd-prime separation family."""
import unittest

from research.figurate_census import polygonal, polygonal_index, verify_tuple
from research.figurate_wp09_odd_prime_separation import (
    ENTRIES, ORDER, OFFSET_PERIOD, offset_at, pair_outputs,
    transformed_outputs, full_binary_certificate, odd_prime_obstruction,
    complete_certificate,
)


def independent_square_mod(value, modulus):
    return value % modulus in {j*j % modulus for j in range(modulus)}


def independent_polygonal_mod(k, value, modulus):
    image = {(((k-2)*t*t-(k-4)*t)//2) % modulus
             for t in range(1, 2*modulus+1)}
    return value % modulus in image


def signed_v2(z):
    if z == 0:
        return None
    v = 0
    while z % 2 == 0:
        z //= 2
        v += 1
    return v, z % 8


class WP09OddPrimeSeparation(unittest.TestCase):
    def test_exact_first_certificate(self):
        d=complete_certificate(0)
        self.assertEqual(tuple(d["binary"]["outputs"]), (244,377,90752))
        self.assertEqual(tuple(d["binary"]["transformed_outputs"]),
                         (2212,3409,816784))
        self.assertEqual(tuple(d["odd_prime"]["image"]), (0,1,2))
        self.assertEqual(tuple(d["odd_prime"]["output_residues"]), (4,2,2))
        self.assertEqual(tuple(d["odd_prime"]["valid_edges"]),
                         (False,True,True))
        self.assertTrue(d["local_to_global_failure_for_this_fixed_triple"])
        self.assertFalse(d["global_nonexistence_for_all_triples_claimed"])

    def test_infinite_family_signed_valuation_proof(self):
        # Adding 640*m changes transformed outputs by 5760*m,
        # divisible by 2^7. Base v2 values (2,0,4) remain stable.
        self.assertEqual(9*OFFSET_PERIOD % 128,0)
        self.assertEqual(tuple(signed_v2(x) for x in
                         transformed_outputs(2)), ((2,1),(0,1),(4,1)))
        for m in list(range(-400,401))+[-10**30,10**30]:
            data=full_binary_certificate(m)
            self.assertTrue(data["all_powers_binary_compatible"],m)
            self.assertEqual(tuple(signed_v2(x) for x in
                             transformed_outputs(offset_at(m))),
                             ((2,1),(0,1),(4,1)),m)
            odd=odd_prime_obstruction(m)
            self.assertEqual(odd["output_residues"], (4,2,2))
            self.assertTrue(odd["first_edge_excluded"])

    def test_direct_independent_modular_replay(self):
        for m in (-128,-19,-1,0,1,7,128,10**9):
            for output, transform in zip(pair_outputs(offset_at(m)),
                                         transformed_outputs(offset_at(m))):
                for exponent in range(1,11):
                    mod=1<<exponent
                    self.assertTrue(independent_square_mod(transform,mod))
                    self.assertTrue(independent_polygonal_mod(
                        ORDER,output,mod))
                self.assertEqual(output%5 in
                    {(((ORDER-2)*t*t-(ORDER-4)*t)//2)%5
                     for t in range(1,11)},output%5 !=4)

    def test_no_exact_integer_membership_for_any_offset(self):
        # 20-gonal first shifted product is 4 mod5: not an exact integer.
        for m in (-100,-1,0,1,100,10**9):
            c=offset_at(m)
            z=pair_outputs(c)[0]
            self.assertEqual(z%5,4)
            self.assertIsNone(polygonal_index(20,z))
            self.assertIsNone(verify_tuple(ENTRIES,"B",20,c))

    def test_even_binary_congruence_not_actual_triple(self):
        for m in (-9,0,13):
            self.assertEqual(tuple(pair_outputs(offset_at(m))),
                             tuple(x*y+offset_at(m) for x,y in
                                   ((1,242),(1,375),(242,375))))
        self.assertEqual(ENTRIES,(1,242,375))
        self.assertEqual(OFFSET_PERIOD%5,0)


if __name__ == "__main__":
    unittest.main()

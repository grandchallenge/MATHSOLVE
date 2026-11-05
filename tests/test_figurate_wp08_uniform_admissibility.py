"""WP08: independent tests for uniform all-offset 2-adic Type B triple admission."""
import itertools
import unittest

from research.figurate_census import polygonal, verify_tuple
from research.figurate_wp08_uniform_admissibility import (
    constructive_witness, counterexample_offset, local_triple_holds,
    order_is_uniformly_admissible,
)
from research.figurate_wp08_mod16_classification import local_certificate


def direct_residue_image(k, exponent):
    m = 1 << exponent
    return {(((k-2)*t*t-(k-4)*t)//2) % m
            for t in range(1, 2*m+1)}


def direct_triple(k, c, entries, exponent):
    m = 1 << exponent
    image = direct_residue_image(k, exponent)
    a, b, d = entries
    return all((x*y+c) % m in image
               for x, y in ((a,b),(a,d),(b,d)))


def independent_two_adic_square(D):
    if D == 0:
        return True
    n = abs(D)
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v % 2 == 0 and (D // (1 << v)) % 8 == 1


class FigurateUniformTwoAdicAdmissibility(unittest.TestCase):
    def test_complete_order_classification_against_mod16_obstructions(self):
        for k in range(3, 194):
            target = k % 4 != 0 or k % 16 == 4
            self.assertEqual(order_is_uniformly_admissible(k), target)
            if not target:
                self.assertEqual(counterexample_offset(k), 2)
                self.assertTrue(local_certificate(k, 2)[
                    "global_exclusion_by_mod16"], k)
            else:
                self.assertIsNone(counterexample_offset(k))
        for bad in (0,1,2):
            with self.assertRaises(ValueError):
                order_is_uniformly_admissible(bad)

    def test_fixed_witness_complement_to_prior_one_sixth_class(self):
        from research.figurate_wp08_2adic_density import (
            offset_immune_to_all_two_power_tests)
        count = 0
        for k in range(4, 149, 16):
            for c in range(-128, 129):
                if offset_immune_to_all_two_power_tests(k,c):
                    continue
                w = constructive_witness(k,c)
                a,b,d = w["entries"]
                self.assertEqual(a,1)
                self.assertTrue(1 < b < d)
                for exponent in (1,2,3,4,5,6,7,8,16,32,64,128):
                    self.assertTrue(local_triple_holds(k,c,(a,b,d),exponent),
                                    (k,c,exponent,w))
                count += 1
        self.assertGreater(count, 1900)

    def test_independent_direct_polynomial_all_power2_images(self):
        for k in (3,5,6,7,8,12,16,20,36,52,68,84):
            if not order_is_uniformly_admissible(k):
                with self.assertRaises(ValueError):
                    constructive_witness(k,7)
                continue
            for c in (-31,-7,-2,0,1,2,3,6,7,17,45):
                w=constructive_witness(k,c)
                entries=tuple(w["entries"])
                self.assertEqual(len(set(entries)),3)
                for n in range(1,9):
                    self.assertTrue(direct_triple(k,c,entries,n),
                                    (k,c,n,entries))

    def test_independent_2adic_split_proof_lemmas(self):
        for k in range(4,149,16):
            A=k//2-1
            q=k//4-1
            self.assertEqual(A % 8,1)
            for c in (-115,-37,-1,0,2,6,11,17,44,105):
                w=constructive_witness(k,c)
                t=w["seed_index"]
                N=w["precision"]
                m=1<<N
                D=A*c+q*q
                self.assertTrue(t in (2,3))
                self.assertNotEqual(A*(t*t+t)-D,0)
                C=(D*pow(A,-1,m))%m
                a,b,d=w["entries"]
                self.assertEqual(a,1)
                self.assertEqual((b+C)%m, t*t%m)
                self.assertEqual((d+C)%m, (t+1)**2%m)
                self.assertEqual((b*d+C)%m, (b+t)**2%m)
                roots=(t,t+1,t*t+t-C)
                for root in roots:
                    self.assertNotEqual(root,0)
                    v=0
                    rr=abs(root)
                    while rr%2==0:
                        rr//=2
                        v+=1
                    self.assertGreaterEqual(N,2*v+3)
                # At any precision, direct affine forms are Z2 squares.
                for x,y in ((a,b),(a,d),(b,d)):
                    self.assertTrue(independent_two_adic_square(
                        A*(x*y+c)+q*q),(k,c,x,y))

    def test_seed_degeneracy_and_large_negative_offsets(self):
        # For square order, c=6 gives D=6 A and triggers alternative t=3.
        for k in (4,20,36,52,68):
            A=k//2-1;q=k//4-1
            numer=6*A-q*q
            if numer%A==0:
                c=numer//A
                w=constructive_witness(k,c)
                self.assertEqual(w["seed_index"],3)
                self.assertTrue(local_triple_holds(
                    k,c,tuple(w["entries"]),256))
        for k,c in ((4,-10**20),(20,10**25),(36,-10**27),(52,10**36)):
            w=constructive_witness(k,c)
            self.assertTrue(local_triple_holds(
                k,c,tuple(w["entries"]),256))

    def test_nonlocal_not_claimed_as_integer_tuple(self):
        # Actual square-output example exists for c=2, but our
        # positive integer witness is only locally compatible.
        w=constructive_witness(4,2)
        self.assertEqual(w["entries"],(1,130,263))
        self.assertIsNone(verify_tuple(tuple(w["entries"]),"B",4,2))
        self.assertTrue(direct_triple(4,2,tuple(w["entries"]),8))
        # A different exact square-output tuple is genuinely valid.
        self.assertIsNotNone(verify_tuple((1,2,7),"B",4,2))

    def test_precise_validation(self):
        for k in (8,12,16,24,28):
            with self.assertRaises(ValueError):
                constructive_witness(k,2)
        with self.assertRaises(ValueError):
            local_triple_holds(4,0,(1,1,2),4)
        with self.assertRaises(ValueError):
            local_triple_holds(4,0,(1,2,3),0)


if __name__ == "__main__":
    unittest.main()

"""Independent HNF lattice, exact norm, and oriented ray tests (WP09-028)."""
from __future__ import annotations

import unittest
from math import gcd, isqrt

from research.figurate_wp09_ideal_ray_enumeration_028 import (
    IdealHNF, is_stable_ideal, enumerate_norm_ideals,
    principal_ideal_from_generator, classify_norm_ideal_ray,
)
from research.figurate_wp09_odd_ray_lattice_025 import (
    normalized_decide, construct_exact_seed,
)
from research.figurate_wp09_linear_ray_026 import linear_gcd_decide
from research.figurate_wp09_ray_class_conductor_027 import (
    order_data, ideal_norm_locally_permitted,
)


def brute_hnf(D, n):
    result = []
    for c in range(1, isqrt(n) + 1):
        for h in range(1, n + 1):
            if c*c*h != n:
                continue
            for j in range(h):
                # Independently verify closure on BOTH lattice generators
                # under multiplication by sqrt(D).
                i = IdealHNF(c, h, j)
                if (i.contains(0, c*h) and
                        i.contains(D*c, c*j)):
                    result.append(i)
    return result


def brute_norm_generators(D, N, limit):
    result = []
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            if x*x - D*y*y == N:
                result.append((x,y))
    return result


class IdealRayTests(unittest.TestCase):
    def test_hnf_complete_small_independent_basis_oracle(self):
        for D in (2, 10, 18, 26, 34):
            for n in range(1, 110):
                enumerated = enumerate_norm_ideals(
                    D, n, max_root_checks=30000
                )
                self.assertEqual(enumerated, brute_hnf(D,n),(D,n))
                self.assertEqual(len(enumerated),len(set(enumerated)))
                for i in enumerated:
                    self.assertEqual(i.norm,n)
                    self.assertTrue(is_stable_ideal(i,D))

    def test_exact_principal_ideal_from_small_norm_generators(self):
        for D in (2, 10, 18):
            for x in range(1, 21):
                for y in range(1, 21):
                    n = abs(x*x - D*y*y)
                    if n == 0 or n > 500:
                        continue
                    ideals = enumerate_norm_ideals(
                        D,n,max_root_checks=20000
                    )
                    i = principal_ideal_from_generator(
                        D,x,y,ideals
                    )
                    self.assertTrue(i.contains(x,y))
                    self.assertEqual(i.norm,n)

    def test_complete_ray_classification_and_positive_controls(self):
        expected = {
            0:(1,1,True),
            1:(3,3,True),
            2:(4,1,True),
            3:(6,6,True),
            4:(0,0,False),
            5:(10,6,True),
            6:(4,2,True),
        }
        for m,(count,hits,exists) in expected.items():
            z=classify_norm_ideal_ray(m)
            self.assertEqual((z["candidate_ideal_count"],
                              z["ray_match_count"],z["exists"]),
                             (count,hits,exists),m)
            self.assertFalse(z["full_ray_class_group_computed"])
            self.assertFalse(z["global_parameter_classification_proved"])
            self.assertEqual(z["order_conductor"],order_data(m)["f"])
            self.assertEqual(exists,linear_gcd_decide(16*m+4)["exists"])
            self.assertEqual(exists,normalized_decide(16*m+4)["exists"])
            self.assertEqual(bool(count),ideal_norm_locally_permitted(m))
            for entry in z["ideal_classes"]:
                if entry["status"]=="ray_match":
                    self.assertIsNotNone(entry["witness"]["ray_hit"])
                else:
                    self.assertIsNone(entry["witness"])

    def test_independent_bruteforce_ideal_and_ray_membership(self):
        for m in range(4):
            z=classify_norm_ideal_ray(m)
            D,A,N=z["D"],z["A"],z["N"]
            ideals=enumerate_norm_ideals(D,abs(N))
            indexed={tuple(i):i for i in (
                e["hnf"] for e in z["ideal_classes"])}
            ray={}
            for x,y in brute_norm_generators(D,N,350):
                ideal=principal_ideal_from_generator(D,x,y,ideals)
                if (2*x-1)%A==0 and (2*y-1)%A==0:
                    ray[(ideal.c,ideal.h,ideal.j)]=True
            for e in z["ideal_classes"]:
                if e["hnf"] in ray:
                    self.assertEqual(e["status"],"ray_match")

    def test_known_witness_exact_anchor(self):
        for m in (0,1,2,3,5,6):
            z=classify_norm_ideal_ray(m)
            self.assertTrue(z["exists"])
            result=normalized_decide(16*m+4)
            w=construct_exact_seed(result)
            a,b,d=w["entries"];r,s,t=w["indices"]
            k=16*m+4
            def P(n): return n+(k-2)*n*(n-1)//2
            self.assertEqual((a,b,r),(1,k-2,2))
            self.assertEqual((a*b+2,a*d+2,b*d+2),
                             (P(r),P(s),P(t)))

    def test_guard_is_not_a_negative(self):
        with self.assertRaises(ValueError):
            classify_norm_ideal_ray(5,max_ideal_checks=1)
        with self.assertRaises(ValueError):
            classify_norm_ideal_ray(5,max_representative_bound=1)
        with self.assertRaises(ValueError):
            enumerate_norm_ideals(18,100,max_root_checks=1)
        with self.assertRaises(ValueError):
            enumerate_norm_ideals(0,2)
        with self.assertRaises(ValueError):
            enumerate_norm_ideals(18,-1)
        with self.assertRaises(ValueError):
            enumerate_norm_ideals(18,1,max_root_checks=-1)


if __name__=="__main__":
    unittest.main()

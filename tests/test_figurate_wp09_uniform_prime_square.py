"""Independent direct-polynomial tests for FIGURATE WP09-005."""
import unittest
from research.figurate_wp09_uniform_prime_square import (
    full_audit, uniform_obstruction, local_witness, theorem_count,
    legendre, polygonal,
)


def direct_polygonal(k, t):
    return ((k - 2) * t * t - (k - 4) * t) // 2


def independent_witness(k, c, p):
    q = p * p
    image = {direct_polygonal(k, t) % q for t in range(1, 2*q+1)}
    for a in range(q):
        for b in range(q):
            if (a*b+c) % q not in image:
                continue
            for d in range(q):
                if (a*d+c) % q in image and (b*d+c) % q in image:
                    return a, b, d
    return None


class UniformPrimeSquareTests(unittest.TestCase):
    def test_full_small_prime_classifications(self):
        for p, n in ((3, 6), (5, 40), (7, 126)):
            with self.subTest(p=p):
                result = full_audit(p)
                self.assertEqual(result["predicted"], n)
                self.assertEqual(result["locally_excluded"], n)
                self.assertEqual(result["additional_exclusions"], 0)
                self.assertEqual(theorem_count(p), n)

    def test_independent_obstruction_oracle(self):
        for p in (3, 5, 7):
            for k in range(3, p*p+3):
                for c in range(p*p):
                    if uniform_obstruction(k, c, p):
                        self.assertIsNone(independent_witness(k, c, p), (p, k, c))

    def test_larger_primes(self):
        for p in (11, 13):
            q = p*p
            for k in range(3, p+3):
                if (k-2) % p == 0:
                    continue
                A = (k-2)*pow(2, -1, p) % p
                if legendre(A, p) != -1:
                    continue
                B = (-(k-4)**2 * pow(8*(k-2), -1, q)) % q
                for j in (1, p-1):
                    c = (B + p*j) % q
                    self.assertTrue(uniform_obstruction(k, c, p))
                    self.assertIsNone(local_witness(k, c, q), (p, k, c))

    def test_signed_offsets_and_lifting(self):
        for p in (3, 5, 7, 11):
            q = p*p
            for k in (3, 5, 7, 11, 20, 31):
                for c in (-10**13, -73, -9, 0, 3, 8, 31, 10**13):
                    self.assertEqual(uniform_obstruction(k, c, p),
                                     uniform_obstruction(k+q, c, p))
                    self.assertEqual(uniform_obstruction(k, c, p),
                                     uniform_obstruction(k, c+q, p))

    def test_integer_controls_and_formula(self):
        for k in range(3, 30):
            for t in range(1, 35):
                self.assertEqual(polygonal(k, t), direct_polygonal(k, t))
        triangular = {n*(n+1)//2 for n in range(1, 5000)}
        for a, b, d in ((1, 3, 15), (1, 3, 210), (1, 3, 2926)):
            self.assertTrue({a*b, a*d, b*d}.issubset(triangular))
            for p in (3, 5, 7, 11, 13):
                self.assertFalse(uniform_obstruction(3, 0, p))

    def test_repeated_residue_classes(self):
        for p in (3, 5, 7):
            self.assertIsNotNone(local_witness(3, 0, p*p))

    def test_reject_nonprime_and_bad_order(self):
        for p in (1, 2, 4, 9):
            with self.assertRaises(ValueError):
                uniform_obstruction(3, 0, p)
        with self.assertRaises(ValueError):
            uniform_obstruction(2, 0, 3)


if __name__ == "__main__":
    unittest.main()

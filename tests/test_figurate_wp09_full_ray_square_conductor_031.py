"""Independent exact arithmetic tests for FIGURATE WP09-031."""
import unittest
from math import gcd, prod

from research.figurate_wp09_full_ray_square_conductor_031 import (
    full_ray_square_conductor, local_components, mul, power, inverse,
    sqrt_two_hensel, cyclic_quotient_invariants,
)
from research.figurate_wp09_square_conductor_picard_030 import (
    narrow_picard_square_conductor,
)
from research.figurate_wp09_ray_kernel_029 import ray_kernel


def independent_finite_quotient(f):
    """Directly enumerate all ring units and the principal ray subgroup.

    This oracle NEVER calls local coordinates, local roots, torsion
    presentation, or the candidate invariant-factor routine.
    """
    modulus = f**3
    positive = (3,2)
    positive_powers = []
    z = (1,0)
    while z not in positive_powers:
        positive_powers.append(z)
        z = ((3*z[0]+4*z[1])%modulus,
             (2*z[0]+3*z[1])%modulus)
    subgroup = set()
    for x,y in positive_powers:
        for j in range(f):
            s = 1+f*f*j
            subgroup.add((s*x%modulus,s*y%modulus))
    # Coprimality with the conductor is equivalent to a unit in O_K/f^3.
    units = [(a,b) for a in range(modulus) for b in range(modulus)
             if gcd(a*a-2*b*b,f)==1]
    if not units or len(units)%len(subgroup):
        raise AssertionError("invalid residue quotient")
    order = len(units)//len(subgroup)
    torsion = {}
    x = order
    p = 2
    while p*p <= x:
        if x%p:
            p += 1
            continue
        e = 0
        while x%p == 0:
            x//=p
            e+=1
        torsion[p] = e
    if x>1:
        torsion[x] = 1
    counts = {}
    for p,e in torsion.items():
        counts[p] = []
        for j in range(1,e+1):
            killed = sum(power(z,p**j,modulus) in subgroup for z in units)
            if killed%len(subgroup):
                raise AssertionError("coset torsion divisibility failure")
            counts[p].append(killed//len(subgroup))
    return order,counts


class FullRaySquareConductorTests(unittest.TestCase):
    def test_three_direct_full_group_oracles(self):
        expected = {
            3: (6,[6]),
            5: (20,[20]),
            7: (84,[2,42]),
        }
        for f,(order,invariants) in expected.items():
            direct_order,torsion = independent_finite_quotient(f)
            actual = full_ray_square_conductor(f)
            self.assertEqual(actual["full_oriented_ray_group_order"],direct_order)
            self.assertEqual(actual["full_oriented_ray_group_order"],order)
            self.assertEqual(actual["full_oriented_ray_invariant_factors"],invariants)
            for p,counts in torsion.items():
                for j,count in enumerate(counts,1):
                    expected_count = prod(gcd(z,p**j) for z in invariants)
                    self.assertEqual(count,expected_count,(f,p,j))

    def test_full_quotient_against_prior_ray_kernel_and_picard(self):
        # Old result determined ORDER only, not full structure.
        expected = {
            1:(1,[]), 3:(6,[6]), 5:(20,[20]), 7:(84,[2,42]),
            9:(54,[54]), 11:(110,[110]), 13:(2028,[13,156]),
            15:(720,[6,120]), 17:(544,[2,272]),
            19:(342,[342]), 21:(1512,[6,6,42]),
        }
        for f,(order,inv) in expected.items():
            got = full_ray_square_conductor(f)
            self.assertEqual(got["full_oriented_ray_group_order"],order)
            self.assertEqual(got["full_oriented_ray_invariant_factors"],inv)
            old = narrow_picard_square_conductor(f)
            kernel = ray_kernel((f*f-1)//8)
            self.assertEqual(order,old["narrow_picard_order"]*
                             kernel["kernel_order"])
            self.assertEqual(prod(inv),order)

    def test_composite_and_prime_power_crt(self):
        expected = {
            25:[500], 27:[486], 33:[6,1320],
            35:[2,6,420], 45:[6,1080], 49:[2,2058],
            63:[6,6,378],
        }
        for f,inv in expected.items():
            result = full_ray_square_conductor(f)
            self.assertEqual(result["full_oriented_ray_invariant_factors"], inv)
            self.assertEqual(result["full_oriented_ray_group_order"],prod(inv))

    def test_local_teichmueller_principal_decomposition(self):
        for p,e in ((3,1),(5,1),(7,1),(11,1),(17,1),(3,2),(7,2)):
            coords = local_components(p,e)
            for n,a in coords:
                self.assertGreater(n,0)
                self.assertGreaterEqual(a,0)
                self.assertLess(a,n)
            if p%8 in (1,7):
                r = sqrt_two_hensel(p,3*e)
                self.assertEqual(r*r%(p**(3*e)),2)
            z=(3,2)
            mod=p**(3*e)
            self.assertEqual(mul(z,inverse(z,mod),mod),(1,0))
        # A direct group presentation should be invariant under adding
        # any multiple of a cyclic factor to the relation coordinate.
        presentation=[(8,3),(9,6),(25,2)]
        inv1,order1,_=cyclic_quotient_invariants(presentation)
        inv2,order2,_=cyclic_quotient_invariants(
            [(n,a+7*n) for n,a in presentation])
        self.assertEqual((inv1,order1),(inv2,order2))

    def test_fail_closed_resource_and_argument_guards(self):
        for f in (-1,0,2,4):
            with self.assertRaises(ValueError):
                full_ray_square_conductor(f)
        with self.assertRaises(ValueError):
            full_ray_square_conductor(101,max_prime=97)
        with self.assertRaises(ValueError):
            full_ray_square_conductor(27,max_modulus=1000)
        with self.assertRaises(ValueError):
            power((1,1),-1,7)
        with self.assertRaises(ValueError):
            cyclic_quotient_invariants([(0,0)])
        with self.assertRaises(ValueError):
            sqrt_two_hensel(3,3)


if __name__=="__main__":
    unittest.main()

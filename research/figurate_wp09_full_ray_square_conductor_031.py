"""FIGURATE WP09-031: full oriented ray-class group for odd square conductors.

For f odd, O_f=Z[f sqrt(2)], ray modulus f^2 O_f.
The full ray group (not just its cardinality) has the finite presentation
  ((O_K/f^3 O_K)^x)/(<3+2 sqrt(2)> * {1+f^2 j:j mod f}),
with O_K=Z[sqrt(2)]. This file computes exact invariant factors via local
cyclic coordinates and one global unit relation. No class-group or
Diophantine existence claim outside this subfamily is made.
"""
from __future__ import annotations
from math import gcd, lcm


def factor(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("positive integer required")
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mul(z: tuple[int, int], w: tuple[int, int], modulus: int):
    return ((z[0]*w[0] + 2*z[1]*w[1]) % modulus,
            (z[0]*w[1] + z[1]*w[0]) % modulus)


def power(z: tuple[int, int], exponent: int, modulus: int):
    if exponent < 0 or modulus < 1:
        raise ValueError("nonnegative exponent and positive modulus required")
    result = (1 % modulus, 0)
    while exponent:
        if exponent & 1:
            result = mul(result, z, modulus)
        z = mul(z, z, modulus)
        exponent >>= 1
    return result


def inverse(z: tuple[int, int], modulus: int):
    norm = (z[0]*z[0] - 2*z[1]*z[1]) % modulus
    t = pow(norm, -1, modulus)
    return (z[0]*t % modulus, -z[1]*t % modulus)


def primitive_root_prime(p: int) -> int:
    if p < 3:
        raise ValueError("odd prime required")
    factors = factor(p-1)
    for g in range(2, p):
        if all(pow(g, (p-1)//q, p) != 1 for q in factors):
            return g
    raise ArithmeticError("primitive root not found")


def sqrt_two_hensel(p: int, n: int) -> int:
    root = next((r for r in range(p) if r*r % p == 2), None)
    if root is None:
        raise ValueError("two is not a square at this prime")
    pp = p
    for _ in range(1, n):
        digit = (-((root*root-2)//pp)*pow(2*root, -1, p)) % p
        root += digit*pp
        pp *= p
    if root*root % pp != 2:
        raise ArithmeticError("Hensel lift failed")
    return root


def local_torsion(p: int, n: int):
    """Finite-field Teichmueller generators and coordinates of 3+2sqrt2."""
    modulus = p**n
    lift_power = p**(n-1)
    if p % 8 in (1, 7):  # split: two cyclic torsion factors of order p-1
        r = sqrt_two_hensel(p, n)
        g = primitive_root_prime(p)
        tau = pow(g, lift_power*pow(lift_power, -1, p-1), modulus)
        if pow(tau, p-1, modulus) != 1 or tau % p != g:
            raise ArithmeticError("split Teichmueller lift failed")
        half, ir = pow(2, -1, modulus), pow(2*r, -1, modulus)

        def from_crt(a, b):
            return ((a+b)*half % modulus, (a-b)*ir % modulus)

        g1, g2 = from_crt(tau, 1), from_crt(1, tau)
        pos, neg = (3+2*r) % p, (3-2*r) % p
        i = next((i for i in range(p-1) if pow(g, i, p) == pos), None)
        j = next((i for i in range(p-1) if pow(g, i, p) == neg), None)
        if i is None or j is None:
            raise ArithmeticError("split finite-field logarithm failed")
        torsion = mul(power(g1, i, modulus),
                      power(g2, j, modulus), modulus)
        return [(p-1, i), (p-1, j)], torsion

    # Inert: cyclic residue field of order p^2-1.
    order = p*p-1
    prime_divisors = factor(order)
    root = next(((x,y) for x in range(p) for y in range(p)
                 if gcd(x*x-2*y*y, p) == 1
                 and all(power((x,y), order//q, p) != (1,0)
                         for q in prime_divisors)), None)
    if root is None:
        raise ArithmeticError("inert finite-field generator not found")
    generator = power(root, lift_power*pow(lift_power, -1, order),
                      modulus)
    if power(generator, order, modulus) != (1,0):
        raise ArithmeticError("inert Teichmueller lift failed")
    value, digit = (1,0), None
    for i in range(order):
        if value == (3 % p, 2 % p):
            digit = i
            break
        value = mul(value, root, p)
    if digit is None:
        raise ArithmeticError("inert finite-field logarithm failed")
    return [(order, digit)], power(generator, digit, modulus)


def local_components(p: int, e: int):
    """Presentation of (O_K/p^(3e))^x / (1+p^(2e) Z), with unit coords.

    Since p is odd and the extension is unramified, 1+p and
    1+p sqrt(2) generate the two principal-unit factors, each of
    exponent p^(3e-1). The scalar ray relation truncates only
    the first factor to exponent p^(2e-1).
    """
    n, modulus = 3*e, p**(3*e)
    torsion_coords, torsion_part = local_torsion(p, n)
    residue = mul((3 % modulus, 2 % modulus),
                  inverse(torsion_part, modulus), modulus)
    if residue[0] % p != 1 or residue[1] % p != 0:
        raise ArithmeticError("torsion extraction failed")
    scalar = (1+p, 0)
    radical = (1, p)
    a = b = 0
    digit_base = 1
    for level in range(n-1):
        pp = p**(level+1)
        if (residue[0]-1) % pp or residue[1] % pp:
            raise ArithmeticError("principal-unit layer mismatch")
        da = ((residue[0]-1)//pp) % p
        db = (residue[1]//pp) % p
        a += da*digit_base
        b += db*digit_base
        correction = mul(power(scalar, da*digit_base, modulus),
                         power(radical, db*digit_base, modulus), modulus)
        residue = mul(residue, inverse(correction, modulus), modulus)
        digit_base *= p
    if residue != (1,0):
        raise ArithmeticError("principal-unit decomposition incomplete")
    presentation = torsion_coords + [
        (p**(2*e-1), a % p**(2*e-1)),
        (p**(3*e-1), b)
    ]
    return presentation


def valuation(n: int, p: int) -> int:
    if n == 0:
        return 10**30
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count


def cyclic_quotient_invariants(components: list[tuple[int, int]]):
    """Invariant factors of (direct sum Z/n_i) / <(a_i)>.

    For the quotient G=B/<u>, |G[p^j]|=|B[p^j]| /
    ord(u mod p^j B). The differences of these p-adic exponents
    recover the complete elementary divisors, without a Smith library.
    """
    primes = set()
    ambient_order = 1
    unit_order = 1
    for n, a in components:
        if n < 1:
            raise ArithmeticError("bad cyclic factor")
        primes.update(factor(n))
        ambient_order *= n
        unit_order = lcm(unit_order, n//gcd(n,a))
    prime_powers = {}
    for p in sorted(primes):
        maximum = max(valuation(n,p) for n,_ in components)
        previous = 0
        ranks = []
        for j in range(1, maximum+1):
            ambient = sum(min(valuation(n,p),j) for n,_ in components)
            relation = max(
                max(0,min(valuation(n,p),j)-valuation(a,p))
                for n,a in components
            )
            torsion_log = ambient-relation
            ranks.append(torsion_log-previous)
            previous = torsion_log
        ranks.append(0)
        if ranks != sorted(ranks, reverse=True):
            raise ArithmeticError("inconsistent p-power torsion")
        prime_powers[p] = [
            j+1 for j in range(maximum)
            for _ in range(ranks[j]-ranks[j+1])
        ]
    width = max(map(len,prime_powers.values()), default=0)
    factors = [1]*width
    for p, exponents in prime_powers.items():
        for i, exponent in enumerate(exponents,
                                     start=width-len(exponents)):
            factors[i] *= p**exponent
    expected = ambient_order//unit_order
    product = 1
    for x in factors:
        product *= x
    if product != expected or any(b % a for a,b in zip(factors,factors[1:])):
        raise ArithmeticError("quotient order/invariants mismatch")
    return factors, expected, unit_order


def full_ray_square_conductor(f: int, *, max_prime: int = 97,
                               max_modulus: int = 10**20):
    """Complete full ray-group invariants for odd positive conductor f.

    Explicit resource bounds raise ValueError, never assert nonexistence.
    This is exact finite arithmetic; running time need not be polynomial.
    """
    if f < 1 or f % 2 == 0:
        raise ValueError("f must be positive odd")
    components = []
    for p, exponent in factor(f).items():
        if p > max_prime or p**(3*exponent) > max_modulus:
            raise ValueError("complete local arithmetic exceeds guard")
        components.extend(local_components(p, exponent))
    invariants, order, positive_unit_order = cyclic_quotient_invariants(components)
    return {
        "f": f, "A": f*f, "m": (f*f-1)//8,
        "conductor_ray_modulus_in_maximal_order": f**3,
        "local_cyclic_presentation": components,
        "positive_unit_image_order": positive_unit_order,
        "full_oriented_ray_invariant_factors": invariants,
        "full_oriented_ray_group_order": order,
        "full_oriented_ray_group_complete": True,
        "extension_law_computed": True,
    }

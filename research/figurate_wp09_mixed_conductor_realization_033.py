"""WP09-033: all mixed 3/5/7-power conductors realize the anchor target ray.

Proof: work_packages/FIGURATE_WP09_MIXED_CONDUCTOR_REALIZATION_033.md.
Strict guards mean NOT COMPUTED, never mathematical NONEXISTENCE.
This bounded research implementation does not confer independent MATHCERT review.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from research.figurate_wp09_power3_global_seeds_032 import (
    multiply, norm, polygonal, power,
)

# For u=3+2*sqrt(2), each u**t is 1 modulo p,
# and its radical coefficient has p-adic valuation exactly one.
BASE_PERIODS = {3: 4, 5: 6, 7: 3}


class UnsupportedConductor(ValueError):
    """Not in the proved sufficient family; does NOT mean nonexistence."""


class ResourceGuard(RuntimeError):
    """The exact computation was deliberately not attempted or not completed."""


@dataclass(frozen=True)
class RayCertificate:
    conductor: int
    factorization: tuple[tuple[int, int], ...]
    A: int
    H: int
    N: int
    lift_exponent: int
    lift_coefficient: int
    correction_index: int
    unit_exponent: int
    ray_period: int
    alpha: tuple[int, int]
    beta_mod_f_cubed: tuple[int, int]


@dataclass(frozen=True)
class PositiveTriple:
    conductor: int
    order: int
    offset: int
    entries: tuple[int, int, int]
    indices: tuple[int, int, int]


def supported_factors(f: int) -> tuple[tuple[int, int], ...]:
    if type(f) is not int or f < 3 or f % 2 == 0:
        raise UnsupportedConductor("conductor must be an odd integer >= 3")
    remaining = f
    result = []
    for p in BASE_PERIODS:
        e = 0
        while remaining % p == 0:
            remaining //= p
            e += 1
        if e:
            result.append((p, e))
    if remaining != 1:
        raise UnsupportedConductor(
            "unproved conductor prime: no nonexistence conclusion"
        )
    return tuple(result)


def ray_certificate(f: int, *, max_conductor_bits: int = 12000) -> RayCertificate:
    """Explicit finite 3/5/7-power target ray witness, with no Pell scan.

    The certificate is a proof-backed modular construction valid for all
    supported f, including mixed products; a guard raises rather than NO.
    """
    # Apply the bit-size guard before potentially expensive repeated factor removal.
    if type(f) is int and f > 0 and f.bit_length() > max_conductor_bits:
        raise ResourceGuard("conductor size guard; mathematical theorem still holds")
    factors = supported_factors(f)
    A, modulus = f*f, f**3
    H = (A*A + 6*A + 1)//8
    N = -2*(2*A - 1)*H

    # For each p^e || f: t_p*p^(2e-1) lifts its radical coefficient to
    # valuation 2e. The lcm has exactly that valuation at every p|f.
    L = lcm(*(BASE_PERIODS[p]*p**(2*e-1) for p, e in factors))
    unit_scalar, unit_radical = power((3, 2), L, modulus)
    if unit_scalar != 1 or unit_radical % A:
        raise ArithmeticError("primitive principal-unit lift congruence failed")
    b = (unit_radical // A) % f
    if gcd(b, f) != 1:
        raise ArithmeticError("lift derivative not invertible")

    j = (2*pow(b, -1, f)) % f
    if not (1 <= j < f):
        raise ArithmeticError("invalid correction index")
    E = L*j - 1
    period = L*f

    alpha = ((A+4*f+3)//2, (f**3+3*f+2)//2)
    if norm(alpha) != N:
        raise ArithmeticError("closed norm identity failed")

    beta = multiply(alpha, power((3, 2), E, modulus), modulus)
    r = (A+1)//2
    # Stronger congruence than just ray membership: the scalar difference
    # is exactly f^2 modulo f^3 and radical difference is zero modulo f^3.
    if beta != ((r + A) % modulus, f*r % modulus):
        raise ArithmeticError("target conductor-order ray not attained")
    if power((3, 2), period, modulus) != (1, 0):
        raise ArithmeticError("claimed ray-preserving unit period failed")

    return RayCertificate(f, factors, A, H, N, L, b, j, E,
                          period, alpha, beta)


def positive_triple(f: int, *, max_unit_exponent: int = 8000) -> PositiveTriple:
    """Build a full positive Type B witness for supported small conductors.

    Returns actual three entry values and *positive integer* polygonal indices.
    Very large witnesses may exceed the explicit guard without invalidating
    the global theorem or yielding a false mathematical NO.
    """
    cert = ray_certificate(f)
    if cert.unit_exponent > max_unit_exponent:
        raise ResourceGuard("witness-size guard; existence theorem is unchanged")
    x, y_k = multiply(cert.alpha, power((3, 2), cert.unit_exponent))
    if y_k % f or norm((x, y_k)) != cert.N:
        raise ArithmeticError("constructed element not in the correct order/norm")
    y = y_k//f
    A = cert.A
    r, offset = (A+1)//2, (A-1)//2
    if x % A != r % A or y % A != r % A:
        raise ArithmeticError("ray condition lost in full-integer construction")
    if (x+offset) % A or (y+offset) % A:
        raise ArithmeticError("polygonal index lattice failed")

    s = (y+offset)//A
    t = (x+offset)//A
    d = polygonal(A, s)-2
    k, b = 2*A+2, 2*A
    if not (s>0 and t>0 and d>0 and d not in (1,b)):
        raise ArithmeticError("invalid positive or distinct Type B entries")
    if polygonal(A,2) != b+2 or polygonal(A,s) != d+2:
        raise ArithmeticError("first/second pair equalities failed")
    if polygonal(A,t) != b*d+2:
        raise ArithmeticError("third pair equality failed")
    return PositiveTriple(f, k, 2, (1,b,d), (2,s,t))


if __name__ == "__main__":
    for f in (3, 5, 7, 9, 15, 21, 35, 45, 49, 75, 105, 315):
        c = ray_certificate(f)
        print(f"f={f} k={2*f*f+2} L={c.lift_exponent} "
              f"E={c.unit_exponent} target_ray=PASS")
    for f in (3, 5, 7, 15, 21):
        w = positive_triple(f)
        print(f"f={f} exact_positive_indices=PASS d_bits={w.entries[2].bit_length()}")

"""FIGURATE WP09-034: prime-general exact alpha-unit-orbit target-ray criterion.

A positive result proves infinitely many exact Type B anchor triples.
An obstruction is scoped ONLY to the particular alpha*u**E orbit of
WP09-033; it says nothing about other norm representatives or first pairs.
See work_packages/FIGURATE_WP09_PRIME_GENERAL_CRT_034.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from research.figurate_wp09_power3_global_seeds_032 import (
    multiply, norm, polygonal, power,
)


class ResourceGuard(RuntimeError):
    """Capacity exhaustion. Never interpret it as mathematical nonexistence."""


@dataclass(frozen=True)
class PrimeCondition:
    prime: int
    exponent: int
    unit_order: int
    unit_slope_valuation: int
    base_exponent: int
    slope_mod_prime_power: int
    exponent_residue: int
    exponent_modulus: int


@dataclass(frozen=True)
class OrbitObstruction:
    conductor: int
    reason: str
    detail: str
    conditions: tuple[PrimeCondition, ...]


@dataclass(frozen=True)
class RaySuccess:
    conductor: int
    A: int
    N: int
    alpha: tuple[int, int]
    unit_exponent: int
    unit_period: int
    beta_mod_f_cubed: tuple[int, int]
    conditions: tuple[PrimeCondition, ...]


@dataclass(frozen=True)
class PositiveTriple:
    conductor: int
    order: int
    entries: tuple[int, int, int]
    indices: tuple[int, int, int]


def factor(n: int, *, max_trial_divisor: int = 100_000) -> tuple[tuple[int, int], ...]:
    """Exact trial factorization, with an honest guard for an untested cofactor."""
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")
    if max_trial_divisor < 3:
        raise ValueError("invalid trial divisor limit")
    out: list[tuple[int, int]] = []
    remainder = n
    for p in (2,):
        e = 0
        while remainder % p == 0:
            remainder //= p
            e += 1
        if e:
            out.append((p, e))
    p = 3
    while p * p <= remainder:
        if p > max_trial_divisor:
            raise ResourceGuard("factorization guard; no mathematical verdict")
        e = 0
        while remainder % p == 0:
            remainder //= p
            e += 1
        if e:
            out.append((p, e))
        p += 2
    if remainder > 1:
        out.append((remainder, 1))
    return tuple(out)


def unit_order_mod_prime(p: int, *, max_trial_divisor: int = 100_000) -> int:
    """Exact order of 3+2sqrt(2) in the norm-one subgroup modulo odd prime p.

    Requires p to be certified prime by the caller's exact factorization.
    """
    if p < 3 or p % 2 == 0:
        raise ValueError("odd prime required")
    legendre_2 = pow(2, (p - 1)//2, p)
    if legendre_2 not in (1, p - 1):
        raise ArithmeticError("not an odd prime")
    upper = p-1 if legendre_2 == 1 else p+1
    order = upper
    for q, _ in factor(upper, max_trial_divisor=max_trial_divisor):
        while order % q == 0 and power((3, 2), order//q, p) == (1, 0):
            order //= q
    if power((3, 2), order, p) != (1, 0) or (order > 1 and p % order == 0):
        raise ArithmeticError("unit order derivation failed")
    return order


def valuation_up_to(y: int, p: int, limit: int) -> int:
    """Exact v_p(y) when <= limit; return limit+1 if divisible by p^(limit+1)."""
    v = 0
    while v <= limit and y % p == 0:
        y //= p
        v += 1
    return v


def _crt_step(a: int, m: int, b: int, n: int) -> tuple[int, int] | None:
    g = gcd(m, n)
    if (b-a) % g:
        return None
    quotient = n//g
    z = ((b-a)//g * pow(m//g, -1, quotient)) % quotient if quotient > 1 else 0
    new_modulus = lcm(m, n)
    return (a + m*z) % new_modulus, new_modulus


def decide_alpha_orbit(
    f: int, *, max_conductor_bits: int = 4096, max_trial_divisor: int = 100_000
) -> RaySuccess | OrbitObstruction:
    """Necessary and sufficient ray decision for alpha*(3+2sqrt2)^E, E>=0.

    SUCCESS proves real Type B anchor existence; orbit obstruction does not
    rule out other norm ideals (or other Type B first pairs).
    """
    if type(f) is not int or f < 3 or f % 2 == 0:
        raise ValueError("conductor must be an odd integer >=3")
    if f.bit_length() > max_conductor_bits:
        raise ResourceGuard("conductor bit limit; not a mathematical NO")
    primes = factor(f, max_trial_divisor=max_trial_divisor)
    records: list[PrimeCondition] = []
    alpha = ((f*f + 4*f + 3)//2, (f**3 + 3*f + 2)//2)
    A = f*f
    H = (A*A + 6*A + 1)//8
    N = -2*(2*A-1)*H
    if norm(alpha) != N:
        raise ArithmeticError("explicit norm identity failed")

    for p, e in primes:
        t = unit_order_mod_prime(p, max_trial_divisor=max_trial_divisor)
        # We only need to decide whether the exact valuation is <= 2e.
        y = power((3, 2), t, p**(2*e+1))[1]
        lam = valuation_up_to(y, p, 2*e)
        if lam < 1:
            raise ArithmeticError("unit not congruent to 1 modulo p")
        if lam > 2*e:
            return OrbitObstruction(
                f, "local-valuation",
                f"p={p}: v_p(radical(u^t)) > 2e={2*e}, so this unit orbit cannot hit the target",
                tuple(records),
            )

        base_exponent = t*p**(2*e-lam)
        modulus = p**(3*e)
        x0, y0 = power((3, 2), base_exponent, modulus)
        if x0 != 1 or y0 % p**(2*e):
            raise ArithmeticError("prime-local base unit not in required slope layer")
        B = (y0//p**(2*e)) % p**e
        if gcd(B, p) != 1:
            raise ArithmeticError("slope is not a p-adic unit")
        cofactor = f//p**e
        h = (2*cofactor*cofactor*pow(B, -1, p**e)) % p**e
        residue = base_exponent*h
        period = t*p**(3*e-lam)
        if power((3, 2), residue, modulus) != (1, 2*f*f % modulus):
            raise ArithmeticError("prime-local ray comparison failed")
        if power((3, 2), period, modulus) != (1, 0):
            raise ArithmeticError("prime-local period failed")
        records.append(PrimeCondition(p, e, t, lam, base_exponent,
                                      B, residue, period))

    n, M = 0, 1
    for item in records:
        next_result = _crt_step(n, M, item.exponent_residue, item.exponent_modulus)
        if next_result is None:
            g = gcd(M, item.exponent_modulus)
            return OrbitObstruction(
                f, "crt-incompatible",
                f"prior n={n} (mod {M}) differs from "
                f"n={item.exponent_residue} (mod {item.exponent_modulus}) "
                f"modulo gcd={g}",
                tuple(records),
            )
        n, M = next_result
    if n <= 0:
        raise ArithmeticError("target is nontrivial, so n=0 cannot be a hit")
    if power((3, 2), n, f**3) != (1, 2*f*f % f**3):
        raise ArithmeticError("CRT did not produce global target unit")
    E = n-1
    beta = multiply(alpha, power((3, 2), E, f**3), f**3)
    rho_scalar = (A+1)//2
    if beta != ((rho_scalar+A) % f**3, (f*rho_scalar) % f**3):
        raise ArithmeticError("full conductor-order ray congruence failed")
    if power((3, 2), M, f**3) != (1, 0):
        raise ArithmeticError("CRT unit period invalid")
    return RaySuccess(f, A, N, alpha, E, M, beta, tuple(records))


def positive_triple(f: int, *, max_unit_exponent: int = 10000) -> PositiveTriple:
    """Actual three positive distinct Type B entries and positive polygonal indices."""
    result = decide_alpha_orbit(f)
    if isinstance(result, OrbitObstruction):
        raise ValueError("specified alpha unit orbit blocked; other solutions NOT ruled out")
    if result.unit_exponent > max_unit_exponent:
        raise ResourceGuard("witness size guard; existence theorem remains established")
    x, yk = multiply(result.alpha, power((3, 2), result.unit_exponent))
    if yk % f or norm((x, yk)) != result.N:
        raise ArithmeticError("constructed generator not in correct order/norm")
    y = yk//f
    r, A = (result.A+1)//2, result.A
    if x % A != r % A or y % A != r % A:
        raise ArithmeticError("full ray congruence lost")
    offset = (A-1)//2
    if (x+offset)%A or (y+offset)%A:
        raise ArithmeticError("polygonal index integrality failed")
    s, t = (y+offset)//A, (x+offset)//A
    d = polygonal(A, s)-2
    k, b = 2*A+2, 2*A
    if not (s>0 and t>0 and d>0 and d not in (1,b)):
        raise ArithmeticError("invalid positive distinct Type B triple")
    if polygonal(A,2) != b+2 or polygonal(A,s) != d+2:
        raise ArithmeticError("first and second Type B equations failed")
    if polygonal(A,t) != b*d+2:
        raise ArithmeticError("third Type B equation failed")
    return PositiveTriple(f,k,(1,b,d),(2,s,t))


if __name__=="__main__":
    for f in (3,5,7,11,13,17,19,23,31,33,39,65,93,155,219,365,403):
        z=decide_alpha_orbit(f)
        if isinstance(z, RaySuccess):
            print(f"f={f} k={2*f*f+2} ray=YES E={z.unit_exponent} period={z.unit_period}")
        else:
            print(f"f={f} alpha-orbit={z.reason} (NOT global nonexistence)")

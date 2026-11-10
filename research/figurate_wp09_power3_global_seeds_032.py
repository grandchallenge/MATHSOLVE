"""WP09-032: explicit Type B anchor seeds for the infinite 3-power square-conductor family.

Mathematical proof: work_packages/FIGURATE_WP09_POWER3_GLOBAL_SEEDS_032.md.
All arithmetic is exact. A resource guard raises rather than declaring nonexistence.
This is a producer implementation, not an independent MATHCERT certification.
"""

from __future__ import annotations

from dataclasses import dataclass

Pair = tuple[int, int]


def multiply(a: Pair, b: Pair, modulus: int | None = None) -> Pair:
    """Multiply coefficients in Z[sqrt(2)], optionally reducing both modulo modulus."""
    x, y = a[0] * b[0] + 2 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]
    return (x % modulus, y % modulus) if modulus is not None else (x, y)


def power(a: Pair, n: int, modulus: int | None = None) -> Pair:
    """Binary powering in Z[sqrt(2)] or in its finite coefficient quotient."""
    if n < 0:
        raise ValueError("negative exponent not accepted")
    result = (1, 0)
    while n:
        if n & 1:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        n //= 2
    return result


def norm(a: Pair) -> int:
    return a[0] * a[0] - 2 * a[1] * a[1]


def polygonal(a: int, t: int) -> int:
    """Order k=2a+2 polygonal polynomial P_k(t)."""
    return a * t * (t - 1) + t


@dataclass(frozen=True)
class Certificate:
    e: int
    conductor: int
    A: int
    H: int
    N: int
    modulus: int
    unit_lift_exponent: int
    unit_period: int
    lift_coefficient: int
    correction_index: int
    constructive_exponent: int
    alpha: Pair


def certificate(e: int, *, max_exponent_bits: int = 8192) -> Certificate:
    """Construct a parameter-uniform 3-adic ray certificate for f=3**e.

    Does not build enormous Pell/Type B witnesses. Never returns a negative
    existence verdict on resource exhaustion.
    """
    if not isinstance(e, int) or e < 1:
        raise ValueError("e must be a positive integer")
    if e.bit_length() > max_exponent_bits:
        raise RuntimeError("exponent-size guard; no mathematical NO inferred")

    f = 3**e
    A = f*f
    H = (A*A + 6*A + 1)//8
    N = -2*(2*A-1)*H
    modulus = f**3
    L = 4*3**(2*e-1)
    period = f*L
    alpha = ((f*f+4*f+3)//2, (f**3+3*f+2)//2)

    if norm(alpha) != N:
        raise ArithmeticError("explicit norm identity failed")

    # u**L = 1 + f**2*b*sqrt(2) (mod f**3), b a 3-adic unit.
    a_lift, y_lift = power((3, 2), L, modulus)
    if a_lift != 1 or y_lift % A:
        raise ArithmeticError("3-adic unit lift congruence failed")
    b = (y_lift//A) % f
    if b % 3 == 0:
        raise ArithmeticError("unit-lift coefficient is not a 3-adic unit")

    j = (-2 * pow(b, -1, f)) % f
    exponent = period - (1+L*j)
    if not (0 <= exponent < period):
        raise ArithmeticError("computed exponent is outside a period")

    r = (A+1)//2
    reduced = multiply(alpha, power((3, 2), exponent, modulus), modulus)
    # x ≡ r mod f**2; y_K ≡ f*r mod f**3.
    if reduced[0] % A != r % A or reduced[1] != (f*r) % modulus:
        raise ArithmeticError("target oriented ray congruence failed")
    if power((3, 2), period, modulus) != (1, 0):
        raise ArithmeticError("claimed unit period does not close")

    return Certificate(e, f, A, H, N, modulus, L, period, b, j, exponent, alpha)


def positive_seed(e: int, *, max_unit_exponent: int = 2500) -> tuple[int, int, int, int, int]:
    """Return (k, c, a, b, d) with a=1, b=k-2 and all Type B indices positive.

    The constructive exponent can grow exponentially in e, so use an explicit
    guard. A guard failure means NOT COMPUTED, never NONEXISTENCE.
    """
    cert = certificate(e)
    if cert.constructive_exponent > max_unit_exponent:
        raise RuntimeError("witness-size guard; mathematical existence remains proved")

    x, y_k = multiply(cert.alpha, power((3, 2), cert.constructive_exponent))
    f, A = cert.conductor, cert.A
    if y_k % f:
        raise ArithmeticError("constructed element does not lie in the conductor order")
    y = y_k // f
    r = (A+1)//2
    if x % A != r % A or y % A != r % A or norm((x, y_k)) != cert.N:
        raise ArithmeticError("norm/ray certificate mismatch")

    offset = (A-1)//2
    s_numerator, t_numerator = y+offset, x+offset
    if s_numerator % A or t_numerator % A:
        raise ArithmeticError("polygonal index lattice not met")
    s, t = s_numerator//A, t_numerator//A
    d = polygonal(A, s)-2
    k, b = 2*A+2, 2*A
    if not (s > 0 and t > 0 and d > 0 and d not in (1, b)):
        raise ArithmeticError("invalid Type B positivity/distinctness")
    if polygonal(A, 2) != b+2 or polygonal(A, s) != d+2:
        raise ArithmeticError("first/second Type B pair identities failed")
    if polygonal(A, t) != b*d+2:
        raise ArithmeticError("third exact Type B pair identity failed")
    return k, 2, 1, b, d


if __name__ == "__main__":
    for e in range(1, 7):
        v = certificate(e)
        print(f"e={e} f={v.conductor} A={v.A} exponent={v.constructive_exponent} ray=PASS")
    for e in (1, 2):
        k, c, a, b, d = positive_seed(e)
        print(f"order={k} c={c} witness={a},{b},d_bit_length={d.bit_length()}")

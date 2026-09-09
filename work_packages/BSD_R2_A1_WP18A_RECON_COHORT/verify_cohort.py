#!/usr/bin/env python3
"""Exact local verifier for the BSD-R2-A1 WP18A reconnaissance cohort.

This script uses only integer arithmetic and the pinned curve records listed in
00_README.md. It does not evaluate L-functions, compute Selmer groups, or
assume BSD.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Curve:
    label: str
    conductor: int
    ainvs: tuple[int, int, int, int, int]
    algebraic_rank: int
    analytic_rank: int
    torsion_order: int
    expected_regime: str
    expected_residual_conductor: int


def discriminant(a: tuple[int, int, int, int, int]) -> int:
    a1, a2, a3, a4, a6 = a
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    return -b2 * b2 * b8 - 8 * b4**3 - 27 * b6**2 + 9 * b2 * b4 * b6


def factor(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def count_points_f2(a: tuple[int, int, int, int, int]) -> int:
    a1, a2, a3, a4, a6 = a
    count = 1  # point at infinity
    for x in (0, 1):
        for y in (0, 1):
            lhs = (y * y + a1 * x * y + a3 * y) % 2
            rhs = (x**3 + a2 * x * x + a4 * x + a6) % 2
            count += int(lhs == rhs)
    return count


def is_squarefree(n: int) -> bool:
    return all(e == 1 for e in factor(n).values())


def verify(curve: Curve) -> dict[str, object]:
    assert curve.conductor % 2 == 1, f"{curve.label}: conductor must be odd"
    # For elliptic curves over Q, squarefree conductor means every bad
    # conductor exponent is one, hence every bad reduction is multiplicative.
    assert is_squarefree(curve.conductor), f"{curve.label}: conductor must be squarefree"
    assert curve.algebraic_rank == 1
    assert curve.analytic_rank == 1
    assert curve.torsion_order % 2 == 1

    delta = discriminant(curve.ainvs)
    d_fac = factor(delta)
    n_fac = factor(curve.conductor)
    assert set(d_fac) == set(n_fac), (curve.label, d_fac, n_fac)

    points_f2 = count_points_f2(curve.ainvs)
    trace2 = 3 - points_f2
    assert trace2 % 2 == 1, f"{curve.label}: not ordinary at 2; a_2={trace2}"

    # Protected WP13: residual conductor is the product of bad primes for
    # which n_l = ord_l(Delta_min) is odd; even n_l are exactly the
    # even-Tamagawa support.
    residual_conductor = 1
    even_tamagawa_support: list[int] = []
    tamagawa_v2: dict[int, int] = {}
    for p in sorted(n_fac):
        depth = d_fac[p]
        if depth % 2:
            residual_conductor *= p
            tamagawa_v2[p] = 0
        else:
            even_tamagawa_support.append(p)
            # For depth 2 the WP13 split and nonsplit formulas both give 1.
            if depth == 2:
                tamagawa_v2[p] = 1
            else:
                tamagawa_v2[p] = -1  # parity known; splitness needed for exact value > 1

    regime = "A" if not even_tamagawa_support else "B"
    assert regime == curve.expected_regime
    assert residual_conductor == curve.expected_residual_conductor

    # Over F_2 a reducible two-dimensional representation has an invariant
    # one-dimensional line; its unique nonzero vector is fixed. Thus odd
    # rational torsion excludes rational 2-torsion and gives irreducible E[2].
    mod2_irreducible = curve.torsion_order % 2 == 1
    assert mod2_irreducible

    return {
        "label": curve.label,
        "conductor": curve.conductor,
        "delta_min": delta,
        "delta_factorization": d_fac,
        "points_F2": points_f2,
        "a_2": trace2,
        "good_ordinary_at_2": True,
        "mod2_irreducible": True,
        "even_tamagawa_support": even_tamagawa_support,
        "tamagawa_v2": tamagawa_v2,
        "residual_conductor": residual_conductor,
        "wp13_regime": regime,
    }


def main() -> None:
    cohort = (
        Curve(
            label="53a1",
            conductor=53,
            ainvs=(1, -1, 1, 0, 0),
            algebraic_rank=1,
            analytic_rank=1,
            torsion_order=1,
            expected_regime="A",
            expected_residual_conductor=53,
        ),
        Curve(
            label="203b1",
            conductor=203,
            ainvs=(1, 1, 1, 0, -2),
            algebraic_rank=1,
            analytic_rank=1,
            torsion_order=1,
            expected_regime="B",
            expected_residual_conductor=29,
        ),
    )

    for curve in cohort:
        print(verify(curve))


if __name__ == "__main__":
    main()

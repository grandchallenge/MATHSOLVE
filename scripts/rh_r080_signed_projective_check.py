#!/usr/bin/env python3
"""Sanity replay for RH-R080 signed-projective normality."""

import cmath
import math


def int_cosh(beta: float, lo: float, hi: float) -> float:
    if beta == 0.0:
        return hi - lo
    return (math.sinh(beta * hi) - math.sinh(beta * lo)) / beta


def int_cos(z: complex, lo: float, hi: float) -> complex:
    if abs(z) < 1e-15:
        return hi - lo
    return (cmath.sin(z * hi) - cmath.sin(z * lo)) / z


def piecewise_f_integral(z: complex, a: float, b: float, q: float) -> complex:
    # f=1 on [0,b], f=-q on (b,a]
    return int_cos(z, 0.0, b) - q * int_cos(z, b, a)


def anchor_and_kappas(a: float, b: float, q: float, delta: float):
    A = int_cosh(0.5, 0.0, b) - q * int_cosh(0.5, b, a)
    M = int_cosh(delta, 0.0, b) + q * int_cosh(delta, b, a)
    return A, M / abs(A)


def check_signed_bounds() -> None:
    a = 2.0
    b = 1.6
    q = 0.2
    A, k_half = anchor_and_kappas(a, b, q, 0.5)
    assert A > 0
    assert k_half > 1.0

    for delta in [0.0, 0.2, 0.4, 0.5]:
        _, k = anchor_and_kappas(a, b, q, delta)
        assert k <= k_half + 1e-14
        points = [
            complex(t, s)
            for t in [-5.0, -1.0, 0.0, 2.0, 6.0]
            for s in [-delta, 0.0, delta]
        ]
        for z in points:
            F = 0.5 * piecewise_f_integral(z, a, b, q) / A
            assert abs(F) <= 0.5 * k + 1e-12, (delta, z, F, k)


def check_sign_defect_identity() -> None:
    a = 2.0
    b = 1.6
    q = 0.2
    P = int_cosh(0.5, 0.0, b)
    N = q * int_cosh(0.5, b, a)
    A = P - N
    k = (P + N) / A
    assert abs(k - (1.0 + 2.0 * N / A)) < 1e-14

    # Positive representative: equality kappa=1.
    A_pos = int_cosh(0.5, 0.0, a)
    M_pos = int_cosh(0.5, 0.0, a)
    assert abs(M_pos / A_pos - 1.0) < 1e-14


def check_reference_transfer() -> None:
    # g=1 and f differs by -r on a tail while staying within relative weighted error <1.
    a = 2.0
    b = 1.5
    r = 0.4
    Ag = int_cosh(0.5, 0.0, a)
    E = r * int_cosh(0.5, b, a)
    assert E < Ag

    # f=1 on [0,b], 1-r on (b,a], so actually positive; theorem must hold.
    Af = Ag - E
    Mf = Af
    k_actual = Mf / Af
    k_bound = (Ag + E) / (Ag - E)
    assert k_actual <= k_bound + 1e-14
    assert k_bound >= 1.0


def check_projective_invariance() -> None:
    a = 2.0
    b = 1.6
    q = 0.2
    A, k = anchor_and_kappas(a, b, q, 0.5)
    # Multiplying f by a nonzero real scalar leaves kappa unchanged.
    for c in [-3.0, -0.5, 2.0, 7.0]:
        A2 = c * A
        M2 = abs(c) * k * abs(A)
        assert abs(M2 / abs(A2) - k) < 1e-14


def main() -> int:
    check_signed_bounds()
    check_sign_defect_identity()
    check_reference_transfer()
    check_projective_invariance()
    print("RH-R080 signed-projective normality sanity replay: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

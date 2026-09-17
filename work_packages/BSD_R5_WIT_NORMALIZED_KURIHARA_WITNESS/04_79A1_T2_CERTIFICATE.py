#!/usr/bin/env python3
from __future__ import annotations

A = (1, 1, 1, -2, 0)  # 79a1

F4 = [2, 5, -15, 10, -10, -2, 2]
F8_EXACT = [
    2, 20, -179, 286, -2233, -12628, -20258, 2516, 129778,
    -53740, -402579, 203910, 737583, -733572, -265664, 793848,
    -631968, 405604, -278299, 160286, -63385, 16188, -2570, 228, -8,
]


def peval(c, x, m=None):
    y = 0
    for a in c:
        y = y*x + a
        if m is not None:
            y %= m
    return y


def pderiv(c):
    n = len(c) - 1
    return [a*(n-i) for i, a in enumerate(c[:-1])]


def v2(n):
    assert n != 0
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def invariants(a):
    a1, a2, a3, a4, a6 = a
    b2 = a1*a1 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    disc = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    return b2, b4, b6, b8, disc


def discr_y(a, x):
    a1, a2, a3, a4, a6 = a
    return (a1*x+a3)**2 + 4*(x**3+a2*x*x+a4*x+a6)


def count_f2(a):
    a1, a2, a3, a4, a6 = a
    affine = 0
    for x in range(2):
        for y in range(2):
            lhs = y*y + a1*x*y + a3*y
            rhs = x**3 + a2*x*x + a4*x + a6
            affine += (lhs-rhs) % 2 == 0
    return affine + 1


def main():
    b2, b4, b6, b8, disc = invariants(A)
    assert (b2, b4, b6, b8) == (5, -3, 1, -1)
    assert disc == 79
    assert disc % 8 == 7  # nonsquare unit in Q_2

    q2 = count_f2(A)
    assert q2 == 4
    assert 3-q2 == -1

    # Exact order-four existence. F4 has a simple Hensel root through x=9.
    f49 = peval(F4, 9)
    df49 = peval(pderiv(F4), 9)
    assert v2(f49) == 9
    assert df49 % 2 == 1
    assert discr_y(A, 9) % 32 == 4
    # Any lift x == 9 mod 16 retains D(x) == 4 mod 32.
    assert {discr_y(A, 9+16*k) % 32 for k in range(2)} == {4}

    # Exact-order-eight obstruction. A Q_2 rational order-eight point is
    # nonformal (the protected formal torsion has order two), hence integral,
    # and its x-coordinate must solve the exact-order-eight factor F8_EXACT.
    roots16 = [x for x in range(16) if peval(F8_EXACT, x, 16) == 0]
    assert roots16 == [], roots16

    print("79a1: Delta=79 (nonsquare in Q_2), q2=4, a2=-1")
    print("79a1: F4 has a simple Hensel root x=9 mod 512 and D=4 mod 32")
    print("79a1: exact-order-eight factor has no root mod 16")
    print("PASS: E_79a1(Q_2)[2^infinity] is cyclic of order 4; t_2=2")
    print("PASS: protected R5-RECIP therefore forces Delta_n^(2)=0 mod 2 on 79a1")


if __name__ == "__main__":
    main()

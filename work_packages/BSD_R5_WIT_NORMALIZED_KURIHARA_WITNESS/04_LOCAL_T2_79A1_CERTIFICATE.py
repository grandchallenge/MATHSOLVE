#!/usr/bin/env python3
from __future__ import annotations

A = (1, 1, 1, -2, 0)


def inv(a):
    a1, a2, a3, a4, a6 = a
    return (
        a1*a1 + 4*a2,
        2*a4 + a1*a3,
        a3*a3 + 4*a6,
        a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4,
    )


def trim(p):
    i = 0
    while i < len(p)-1 and p[i] == 0:
        i += 1
    return p[i:]


def padd(a, b):
    n = max(len(a), len(b))
    aa = [0]*(n-len(a)) + a
    bb = [0]*(n-len(b)) + b
    return trim([x+y for x, y in zip(aa, bb)])


def pneg(a):
    return [-x for x in a]


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def ppow(a, n):
    out = [1]
    base = a[:]
    while n:
        if n & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        n >>= 1
    return out


def peval(c, x, m=None):
    y = 0
    for aa in c:
        y = y*x + aa
        if m is not None:
            y %= m
    return y


def pder(c):
    n = len(c)-1
    return [c[i]*(n-i) for i in range(n)]


def roots_mod(c, m):
    return [x for x in range(m) if peval(c, x, m) == 0]


def discr_y(a, x):
    a1, a2, a3, a4, a6 = a
    return (a1*x + a3)**2 + 4*(x**3 + a2*x*x + a4*x + a6)


def count_mod2(a):
    a1, a2, a3, a4, a6 = a
    pts = []
    for x in range(2):
        for y in range(2):
            lhs = y*y + a1*x*y + a3*y
            rhs = x**3 + a2*x*x + a4*x + a6
            if (lhs-rhs) % 2 == 0:
                pts.append((x, y))
    return 1 + len(pts)


def main():
    b2, b4, b6, b8 = inv(A)
    assert (b2, b4, b6, b8) == (5, -3, 1, -1)

    f2 = [4, b2, 2*b4, b6]
    f4 = [
        2, b2, 5*b4, 10*b6, 10*b8,
        b2*b8 - b4*b6,
        b4*b8 - b6*b6,
    ]
    assert f2 == [4, 5, -6, 1]
    assert f4 == [2, 5, -15, 10, -10, -2, 2]

    q2 = count_mod2(A)
    assert q2 == 4
    a2_frob = 3 - q2
    assert a2_frob == -1 and a2_frob % 2 == 1

    # No second nonformal Q_2-rational order-two point.
    assert roots_mod(f2, 16) == []

    # Exact order four: simple Hensel root and square y-discriminant.
    assert roots_mod(f4, 16) == [9]
    assert peval(pder(f4), 9, 2) == 1
    assert roots_mod(f4, 32) == [9]
    assert discr_y(A, 9) % 32 == 4

    # Build the exact-order-eight x-factor from standard division recurrences.
    p3 = [3, b2, 3*b4, 3*b6, b8]
    p5 = psub(pmul(f4, ppow(f2, 2)), ppow(p3, 3))
    p6base = pmul(p3, psub(p5, ppow(f4, 2)))
    g8 = psub(pmul(p6base, ppow(p3, 2)), ppow(p5, 2))

    expected_g8 = [
        2, 20, -179, 286, -2233, -12628, -20258, 2516, 129778,
        -53740, -402579, 203910, 737583, -733572, -265664, 793848,
        -631968, 405604, -278299, 160286, -63385, 16188, -2570, 228, -8,
    ]
    assert g8 == expected_g8
    assert roots_mod(g8, 16) == []

    print("79a1: q2=4, a2=-1 ordinary")
    print("79a1: no second integral order-2 x-coordinate mod 16")
    print("79a1: simple F4 root x=9 mod 16; D=4 mod 32 => Q_2 order-4 point")
    print("79a1: exact-order-8 factor has no root mod 16")
    print("PASS: E_79a1(Q_2)[2^infinity] ~= Z/4Z, so t_2=2")


if __name__ == "__main__":
    main()

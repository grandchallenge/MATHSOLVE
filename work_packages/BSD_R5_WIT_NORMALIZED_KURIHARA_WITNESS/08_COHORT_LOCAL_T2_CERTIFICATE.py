#!/usr/bin/env python3
from __future__ import annotations

CURVES = {
    "61a1": (1, 0, 0, -2, 1),
    "83a1": (1, 1, 1, 1, 0),
    "89a1": (1, 1, 1, -1, 0),
    "201b1": (1, 0, 0, -1, 2),
}


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
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] += u*v
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
    for a in c:
        y = y*x + a
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
    count = 1
    for x in range(2):
        for y in range(2):
            lhs = y*y + a1*x*y + a3*y
            rhs = x**3 + a2*x*x + a4*x + a6
            if (lhs-rhs) % 2 == 0:
                count += 1
    return count


def v2(n):
    assert n != 0
    n = abs(n)
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e


def division_data(a):
    b2, b4, b6, b8 = inv(a)
    f2 = [4, b2, 2*b4, b6]
    f4 = [
        2, b2, 5*b4, 10*b6, 10*b8,
        b2*b8 - b4*b6,
        b4*b8 - b6*b6,
    ]
    p3 = [3, b2, 3*b4, 3*b6, b8]
    p5 = psub(pmul(f4, ppow(f2, 2)), ppow(p3, 3))
    p6base = pmul(p3, psub(p5, ppow(f4, 2)))
    g8 = psub(pmul(p6base, ppow(p3, 2)), ppow(p5, 2))
    return f2, f4, g8


def assert_good_ordinary_q2_4(name, a):
    q2 = count_mod2(a)
    assert q2 == 4, (name, q2)
    assert 3-q2 == -1


def main():
    for name, a in CURVES.items():
        assert_good_ordinary_q2_4(name, a)

    f2, f4, g8 = division_data(CURVES["61a1"])
    assert roots_mod(f2, 16) == []
    assert roots_mod(f4, 16) == [4]
    assert [discr_y(CURVES["61a1"], r) % 32 for r in (4, 20)] == [20, 20]
    print("61a1: no extra order-2 point; F4 y-discriminant nonsquare => t2=1")

    f2, f4, g8 = division_data(CURVES["83a1"])
    assert roots_mod(f2, 32) == []
    assert roots_mod(f4, 16) == [11]
    assert [discr_y(CURVES["83a1"], r) % 32 for r in (11, 27)] == [12, 12]
    print("83a1: no Z_2 order-2 lift; F4 y-discriminant nonsquare => t2=1")

    f2, f4, g8 = division_data(CURVES["201b1"])
    assert roots_mod(f2, 16) == []
    assert roots_mod(f4, 16) == [10]
    assert peval(pder(f4), 10, 2) == 1
    assert [discr_y(CURVES["201b1"], r) % 32 for r in (10, 26)] == [4, 4]
    assert roots_mod(g8, 16) == []
    print("201b1: simple F4 lift with square y-discriminant; no G8 root mod16 => t2=2")

    f2, f4, g8 = division_data(CURVES["89a1"])
    assert roots_mod(f2, 16) == []
    assert roots_mod(f4, 16) == [15]
    assert peval(pder(f4), 15, 2) == 1
    assert [discr_y(CURVES["89a1"], r) % 32 for r in (15, 31)] == [4, 4]
    # Generalized Hensel for the exact-order-eight factor at x=4:
    # v2(G8(4)) > 2*v2(G8'(4)) gives a Q_2 root congruent to 4 mod 16.
    vg = v2(peval(g8, 4))
    vgp = v2(peval(pder(g8), 4))
    assert (vg, vgp) == (6, 2)
    assert vg > 2*vgp
    assert discr_y(CURVES["89a1"], 4) % 8 == 1
    print("89a1: generalized Hensel G8 root with square y-discriminant => exact order 8, t2=3")

    print("PASS: cohort local exponents 61a1=1, 83a1=1, 89a1=3, 201b1=2")


if __name__ == "__main__":
    main()

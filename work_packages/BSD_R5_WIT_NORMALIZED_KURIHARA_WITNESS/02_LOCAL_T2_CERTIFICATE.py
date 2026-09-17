#!/usr/bin/env python3
from __future__ import annotations

CURVES = {
    "53a1": (1, -1, 1, 0, 0),
    "203b1": (1, 1, 1, 0, -2),
}


def inv(a):
    a1, a2, a3, a4, a6 = a
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    return b2, b4, b6, b8


def f4_coeffs(a):
    b2, b4, b6, b8 = inv(a)
    return [
        2,
        b2,
        5*b4,
        10*b6,
        10*b8,
        b2*b8 - b4*b6,
        b4*b8 - b6*b6,
    ]


def peval(c, x, m=None):
    y = 0
    for a in c:
        y = y*x + a
        if m is not None:
            y %= m
    return y


def discr_y(a, x):
    a1, a2, a3, a4, a6 = a
    return (a1*x + a3)**2 + 4*(x**3 + a2*x*x + a4*x + a6)


def roots_mod(c, m):
    return [x for x in range(m) if peval(c, x, m) == 0]


def main():
    expected = {"53a1": 13, "203b1": 5}
    for name, a in CURVES.items():
        c = f4_coeffs(a)
        roots = roots_mod(c, 16)
        assert roots == [expected[name]], (name, roots)
        x = roots[0]
        d32 = discr_y(a, x) % 32
        assert d32 == 20, (name, d32)
        # Any 2-adic square of valuation exactly 2 is 4 mod 32:
        # write s=2u with u odd; then s^2=4u^2 and u^2=1 mod 8.
        assert d32 != 4
        print(f"{name}: F4 root x={x} mod 16; D={d32} mod 32; no Q_2 point of order 4; t_2=1")

    print("PASS: protected A/B controls have exact local 2-primary torsion order 2")


if __name__ == "__main__":
    main()

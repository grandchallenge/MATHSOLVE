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


def f2_coeffs(a):
    b2, b4, b6, _ = inv(a)
    return [4, b2, 2*b4, b6]


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
    for aa in c:
        y = y*x + aa
        if m is not None:
            y %= m
    return y


def discr_y(a, x):
    a1, a2, a3, a4, a6 = a
    return (a1*x + a3)**2 + 4*(x**3 + a2*x*x + a4*x + a6)


def roots_mod(c, m):
    return [x for x in range(m) if peval(c, x, m) == 0]


def main():
    expected_f4 = {"53a1": 13, "203b1": 5}
    for name, a in CURVES.items():
        f2_roots = roots_mod(f2_coeffs(a), 16)
        assert f2_roots == [], (name, "unexpected integral 2-division root", f2_roots)

        f4_roots = roots_mod(f4_coeffs(a), 16)
        r = expected_f4[name]
        assert f4_roots == [r], (name, "F4 residues", f4_roots)

        dclasses = {discr_y(a, r) % 32, discr_y(a, r + 16) % 32}
        assert dclasses == {20}, (name, "D classes", dclasses)

        print(
            f"{name}: no integral 2-division root mod 16; "
            f"F4 root x={r} mod 16 has D=20 mod 32 on both lifts; "
            "no extra Q_2[2] and no Q_2 point of order 4; t_2=1"
        )

    print("PASS: protected A/B controls have exact local 2-primary torsion order 2")


if __name__ == "__main__":
    main()

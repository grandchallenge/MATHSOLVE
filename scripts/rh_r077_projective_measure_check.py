#!/usr/bin/env python3
"""Sanity replay for RH-R077 projective-measure integrity repair."""

import cmath
import math


def kernel(z: complex, x: float) -> complex:
    return cmath.cos(z * x) / math.cosh(x / 2.0)


def check_kernel_bound() -> None:
    for x in [0.0, 0.25, 1.0, 3.0, 8.0, 20.0]:
        for t in [-7.0, -1.0, 0.0, 2.5, 9.0]:
            for s in [-0.5, -0.4, 0.0, 0.4, 0.5]:
                v = abs(kernel(complex(t, s), x))
                assert v <= 1.0 + 1e-12, (x, t, s, v)


def check_boundary_anchor_escape() -> None:
    for n in [1, 3, 10, 30]:
        anchor = 0.5 * kernel(0.5j, float(n))
        assert abs(anchor - 0.5) < 1e-12

    points = [
        complex(t, s)
        for t in [-4.0, -1.0, 0.0, 2.0, 5.0]
        for s in [-0.4, -0.2, 0.0, 0.2, 0.4]
    ]
    vals = []
    for n in [5, 10, 20, 40]:
        vals.append(max(abs(0.5 * kernel(z, float(n))) for z in points))
    assert all(vals[i + 1] < vals[i] for i in range(len(vals) - 1)), vals
    assert vals[-1] < 1e-2, vals


def check_tv_contraction() -> None:
    xs = [0.0, 1.0, 3.0, 7.0]
    p = [0.1, 0.2, 0.4, 0.3]
    q = [0.15, 0.15, 0.5, 0.2]
    tv_norm = sum(abs(a - b) for a, b in zip(p, q))

    for z in [
        0.0,
        2.0,
        0.4j,
        complex(3.0, 0.49),
        complex(-1.5, -0.5),
    ]:
        fp = 0.5 * sum(w * kernel(z, x) for w, x in zip(p, xs))
        fq = 0.5 * sum(w * kernel(z, x) for w, x in zip(q, xs))
        assert abs(fp - fq) <= 0.5 * tv_norm + 1e-12


def check_fourier_counterexample() -> None:
    a = 1.7

    def coeff_abs(j: int) -> float:
        return math.sqrt(2.0) * a ** 1.5 / (math.pi * abs(j))

    scaled = [j * coeff_abs(j) for j in [1, 2, 5, 10, 50, 100]]
    target = scaled[0]
    assert max(abs(v - target) for v in scaled) < 1e-12

    rho = 0.5
    ratios = [
        coeff_abs(j) / math.exp(-math.pi * j * rho / a)
        for j in [5, 10, 20, 40]
    ]
    assert all(ratios[i + 1] > ratios[i] for i in range(len(ratios) - 1))
    assert ratios[-1] > 1e10

    # Even entire counterexample f(x)=x^2: coefficients are O(1/j^2),
    # still not exponential.
    def even_coeff_abs(j: int) -> float:
        return 2.0 * math.sqrt(2.0) * a ** 2.5 / (math.pi ** 2 * j ** 2)

    even_scaled = [j * j * even_coeff_abs(j) for j in [1, 2, 5, 10, 50]]
    even_target = even_scaled[0]
    assert max(abs(v - even_target) for v in even_scaled) < 1e-12


def main() -> int:
    check_kernel_bound()
    check_boundary_anchor_escape()
    check_tv_contraction()
    check_fourier_counterexample()
    print("RH-R077 projective-measure repair sanity replay: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

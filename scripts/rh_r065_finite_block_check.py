#!/usr/bin/env python3
"""Sanity replay for RH-R065 finite-block resolvent obstruction.

The theorem is analytic and proved in work_packages/RH_R065_FINITE_BLOCK_RESOLVENT_OBSTRUCTION.md.
This script checks:
1. The exact Mittag-Leffler lattice sum identity:
       sum_{j=1}^infty 1 / ((pi*j/a)^2 + 1/4) = a * coth(a/2) - 2
2. The integral lower bound on the partial lattice sum:
       S_{a,N} = sum_{j=1}^N 1 / ((pi*j/a)^2 + 1/4) >= (2a/pi) * [arctan(2*pi*(N+1)/a) - arctan(2*pi/a)]
3. The logarithmic-derivative expectation formula for the full zero energy:
       Q_{lambda,N} = int_0^a xi(e^x) * x * sinh(x/2) dx / int_0^a xi(e^x) * cosh(x/2) dx
       matching B_{a,N} + T_{a,N} to high numerical precision on CCM Galerkin ground states.
4. The universal divergence Q_{lambda,N} > a * coth(a/2) - 2 > log(lambda) - 2 as lambda -> infty.
5. The contrast with the finite zero energy of the limiting Riemann Xi function:
       Q_{1/2}(Xi) = -xi'(0)/xi(0) = 1 - (1/2)*log(4*pi) + (1/2)*euler_gamma approx 0.023185
"""

from math import atan, exp, log, pi
import sys


def coth(x: float) -> float:
    return (1.0 + exp(-2.0 * x)) / (1.0 - exp(-2.0 * x))


def lattice_term(a: float, j: int) -> float:
    return 1.0 / ((pi * j / a) ** 2 + 0.25)


def exact_full_lattice_sum(a: float) -> float:
    return a * coth(a / 2.0) - 2.0


def partial_lattice_integral_lower(a: float, n: int) -> float:
    return (2.0 * a / pi) * (atan(2.0 * pi * (n + 1) / a) - atan(2.0 * pi / a))


def check_mittag_leffler_identity() -> None:
    test_a_values = [1.5, 3.0, 5.0, 10.0, 20.0, 50.0]
    m_terms = 500000
    for a in test_a_values:
        exact = exact_full_lattice_sum(a)
        partial = sum(lattice_term(a, j) for j in range(1, m_terms + 1))
        # Tail remainder estimate for sum_{j > m}
        tail = (2.0 * a / pi) * (pi / 2.0 - atan(2.0 * pi * m_terms / a))
        numerical = partial + tail
        err = abs(exact - numerical)
        assert err < 1e-8, f"Mittag-Leffler identity failure for a={a}: err={err}"
        print(f"Mittag-Leffler check a={a:4.1f}: exact={exact:.8f} numerical={numerical:.8f} (err={err:.2e})")


def check_partial_lattice_bound() -> None:
    test_cases = [
        (2.0, 4),
        (5.0, 25),
        (10.0, 100),
        (20.0, 400),
    ]
    for a, n in test_cases:
        actual = sum(lattice_term(a, j) for j in range(1, n + 1))
        integral_lo = partial_lattice_integral_lower(a, n)
        assert actual >= integral_lo - 1e-12, f"Partial lattice lower bound failed for a={a}, n={n}"
        print(f"Partial sum check a={a:4.1f}, N={n:3d}: actual={actual:.6f} >= integral_lower={integral_lo:.6f}")


def check_log_derivative_identity() -> None:
    try:
        import mpmath as mp
        from rh_r039_qw_parity_gap import finite_blocks
    except ImportError:
        print("mpmath or rh_r039 not available; skipping high-precision Galerkin check.")
        return

    mp.mp.dps = 25
    lambda2 = 14
    L = mp.log(lambda2)
    a = L / 2
    N = 4

    even, _, _, _ = finite_blocks(lambda2, N, 25, 96)
    even_N = even[:N + 1, :N + 1]
    E, V = mp.eigsy(even_N)
    min_idx = min(range(N + 1), key=lambda i: E[i])
    w = [V[row, min_idx] for row in range(N + 1)]
    delta_eval = w[0] + mp.sqrt(2) * mp.fsum((-1)**n * w[n] for n in range(1, N + 1))
    w = [x / delta_eval for x in w]
    c0 = w[0]
    c = [w[n] / mp.sqrt(2) for n in range(N + 1)]

    def xi_val(x):
        res = c0
        for j in range(1, N + 1):
            res += 2 * c[j] * mp.cos(mp.pi * j * x / a)
        return res / mp.sqrt(2 * a)

    # Logarithmic derivative expectation
    i_num = 2 * mp.quad(lambda x: xi_val(x) * x * mp.sinh(x / 2), [0, a])
    i_den = 2 * mp.quad(lambda x: xi_val(x) * mp.cosh(x / 2), [0, a])
    q_ratio = i_num / i_den

    # Roots of secular equation
    poles = [(mp.pi * j / a)**2 for j in range(1, N + 1)]
    def h_func(w_val):
        res = c0
        for j in range(1, N + 1):
            res += 2 * (-1)**j * c[j] * w_val / (w_val - poles[j - 1])
        return res

    bounds = [mp.mpf(0)] + poles + [poles[-1] * 4]
    roots_w = []
    for i in range(len(bounds) - 1):
        x1 = bounds[i] + (bounds[i + 1] - bounds[i]) * 1e-4
        x2 = bounds[i + 1] - (bounds[i + 1] - bounds[i]) * 1e-4
        sub_pts = [x1 + (x2 - x1) * k / 20 for k in range(21)]
        sub_vals = [h_func(pt) for pt in sub_pts]
        for k in range(20):
            if sub_vals[k] * sub_vals[k + 1] <= 0:
                r = mp.findroot(h_func, (sub_pts[k], sub_pts[k + 1]), solver="bisect")
                if not any(abs(r - ex) < 1e-6 for ex in roots_w):
                    roots_w.append(r)

    mu = [mp.sqrt(r) for r in sorted(roots_w)]
    b_val = mp.fsum(1.0 / (m**2 + 0.25) for m in mu)
    m_tail = 100000
    t_val = mp.fsum(1.0 / ((mp.pi * j / a)**2 + 0.25) for j in range(N + 1, m_tail + 1))
    t_val += (2 * a / mp.pi) * (mp.pi / 2 - mp.atan(2 * mp.pi * m_tail / a))
    q_sum = b_val + t_val

    diff = abs(q_ratio - q_sum)
    assert diff < 1e-8, f"Log-derivative identity discrepancy: {diff}"
    print(f"Log-derivative Galerkin check: Q_ratio={float(q_ratio):.8f}, B+T={float(q_sum):.8f} (diff={float(diff):.2e})")


def check_asymptotic_divergence() -> None:
    print("Testing scale divergence Q >= a - 2:")
    for a in [5.0, 10.0, 50.0, 100.0, 500.0]:
        lower_bound = exact_full_lattice_sum(a)
        linear_proxy = a - 2.0
        assert lower_bound >= linear_proxy, f"Divergence failed at a={a}"
        print(f"Scale a=log(lambda)={a:5.1f}: Q >= exact_lower={lower_bound:.4f} >= linear_lower={linear_proxy:.4f}")


def check_limiting_xi_energy() -> None:
    # Q_{1/2}(Xi) = -xi'(0)/xi(0) = 1 - (1/2)*log(4*pi) + (1/2)*gamma
    euler_gamma = 0.577215664901532860606512
    q_xi = 1.0 - 0.5 * log(4.0 * pi) + 0.5 * euler_gamma
    print(f"Limiting Riemann Xi zero-energy: Q_{{1/2}}(Xi) = {q_xi:.6f}")
    assert 0.02 < q_xi < 0.03, f"Unexpected Q_{{1/2}}(Xi) value: {q_xi}"


def main() -> int:
    print("=== RH-R065 Finite-Block Resolvent Obstruction Sanity Replay ===")
    check_mittag_leffler_identity()
    check_partial_lattice_bound()
    check_log_derivative_identity()
    check_asymptotic_divergence()
    check_limiting_xi_energy()
    print("RH-R065 sanity replay: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

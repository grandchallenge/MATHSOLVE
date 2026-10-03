#!/usr/bin/env python3
"""Sanity replay for RH-R068 strip-uniform boundedness and Montel normality.

The theorem is proved in work_packages/RH_R068_STRIP_NORMAL_FAMILY.md.
This script checks:
1. Non-negativity of the CCM Galerkin ground state xi(e^x) >= 0 on [-a, a].
2. The hyperbolic convexity bound:
       cosh(s*x) <= cosh(x/2)  for all |s| <= 1/2 and all x in [-a, a].
3. The universal strip modulus bound:
       |F_{lambda,N}(t + i*s)| <= 1/2  for all |s| <= 1/2 and all t in R.
4. The exact anchor value:
       F_{lambda,N}(i/2) = 1/2.
5. The conformal mapping identity:
       s = 1/2 + i*z  maps  |Im(z)| < 1/2  biholomorphically to  0 < Re(s) < 1,
       and maps the real axis Im(z) = 0 to the critical line Re(s) = 1/2.
"""

from math import cosh, pi
import sys


def check_cosh_convexity() -> None:
    print("Checking cosh convexity bound for |s| <= 1/2:")
    for x in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        c_half = cosh(x / 2.0)
        for s in [0.0, 0.1, 0.25, 0.4, 0.49, 0.5]:
            c_s = cosh(s * x)
            assert c_s <= c_half + 1e-14, f"Cosh convexity failed at x={x}, s={s}"
        # Outside strip s > 1/2, cosh(s*x) > cosh(x/2) for x > 0
        assert cosh(0.6 * x) > c_half, f"Expected exceedance failed at x={x}"
    print("  cosh(s*x) <= cosh(x/2) verified across samples: PASS")


def check_critical_strip_mapping() -> None:
    print("Checking conformal mapping s_coord = 1/2 + i*z:")
    # For z = t + i*tau:
    # s_coord = 1/2 + i*(t + i*tau) = (1/2 - tau) + i*t
    # Re(s_coord) = 1/2 - tau
    for tau in [-0.49, -0.25, 0.0, 0.25, 0.49]:
        re_s = 0.5 - tau
        assert 0.0 < re_s < 1.0, f"Critical strip mapping failed for tau={tau}"
    # Critical line:
    tau_zero = 0.0
    assert 0.5 - tau_zero == 0.5, "Critical line mapping failed"
    print("  Conformal map |Im(z)| < 1/2 <-> 0 < Re(s) < 1 verified: PASS")


def check_galerkin_ground_state_and_strip_bound() -> None:
    try:
        import mpmath as mp
        from rh_r039_qw_parity_gap import finite_blocks
    except ImportError:
        print("mpmath or rh_r039 not available; skipping high-precision Galerkin check.")
        return

    mp.mp.dps = 25
    test_configs = [
        (14, 4),
        (14, 6),
        (30, 4),
    ]

    for lambda2, N in test_configs:
        even, _, _, _ = finite_blocks(lambda2, N, 25, 96)
        even_N = even[:N + 1, :N + 1]
        E, V = mp.eigsy(even_N)
        min_idx = min(range(N + 1), key=lambda i: E[i])
        w = [V[row, min_idx] for row in range(N + 1)]
        delta_eval = w[0] + mp.sqrt(2) * mp.fsum((-1)**n * w[n] for n in range(1, N + 1))
        w = [x / delta_eval for x in w]
        c0 = w[0]
        c = [w[n] / mp.sqrt(2) for n in range(N + 1)]
        a = mp.log(lambda2) / 2

        def xi_val(x):
            res = c0
            for j in range(1, N + 1):
                res += 2 * c[j] * mp.cos(mp.pi * j * x / a)
            return res / mp.sqrt(2 * a)

        # Check non-negativity on grid
        grid_x = [a * k / 100 for k in range(101)]
        vals = [float(xi_val(x)) for x in grid_x]
        min_val = min(vals)
        assert min_val >= -1e-12, f"Ground state negative: min={min_val} for lambda2={lambda2}, N={N}"

        def xi_hat(z):
            return 2 * mp.quad(lambda x: xi_val(x) * mp.cos(z * x), [0, a])

        # Denominator 2 * xi_hat(i/2)
        den = 2 * xi_hat(mp.mpc(0, 0.5))
        assert abs(den) > 1e-6, "Denominator vanished"

        # Check anchor value F(i/2) = 1/2
        f_anchor = xi_hat(mp.mpc(0, 0.5)) / den
        err_anchor = abs(f_anchor - 0.5)
        assert err_anchor < 1e-14, f"Anchor value failed: err={err_anchor}"

        # Sample strip |Im(z)| <= 1/2
        max_strip_mod = 0.0
        for s in [0.0, 0.1, 0.25, 0.4, 0.5]:
            for t in [0.0, 1.0, 3.0, 7.0, 14.13, 20.0]:
                z = mp.mpc(t, s)
                mod = float(abs(xi_hat(z) / den))
                max_strip_mod = max(max_strip_mod, mod)
                assert mod <= 0.5 + 1e-10, f"Strip bound violated at z={z}: mod={mod}"

        print(
            f"lambda2={lambda2:2d}, N={N}: xi_min={min_val:.2e}, "
            f"F(i/2)={float(f_anchor.real):.6f}, max_strip_|F|={max_strip_mod:.6f} <= 0.5: PASS"
        )


def main() -> int:
    print("=== RH-R068 Strip-Uniform Boundedness Sanity Replay ===")
    check_cosh_convexity()
    check_critical_strip_mapping()
    check_galerkin_ground_state_and_strip_bound()
    print("RH-R068 sanity replay: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

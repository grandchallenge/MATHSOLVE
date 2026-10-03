#!/usr/bin/env python3
"""RH-R074: Quantitative Eigenvector Error Transfer and Cofinal Schedule Sanity Replay

This script verifies:
1. Analytic Truncation Tail Decay:
   - For an analytic function with analyticity strip rho > 0,
     the Fourier tail on [-a, a] satisfies ||(I - P_N)f||^2 <= C * exp(-2*pi*N*rho / a).
   - Under the quadratic schedule N(lambda) = ceil(kappa * (log lambda)^2),
     the tail decays as O(lambda^(-2*pi*kappa*rho)), which is polynomial in lambda.
   - For kappa >= 1.0, rho >= 0.5, the exponent 2*pi*kappa*rho >= pi > 3.14 > 2*delta (with delta < 0.5).
2. Rayleigh-to-Eigenvector Error Transfer:
   - For any self-adjoint operator/matrix with lowest eigenvalue eps_1,
     second eigenvalue eps_2, and gap g = eps_2 - eps_1 > 0:
     ||v - xi_1||^2 <= 2 * (R(v) - eps_1) / g,
     where R(v) = <v, A v> / <v, v>.
   - Numerical verification across random and structured test matrices with certified gaps.
3. Combined Error Transfer to Critical Substrips S_delta:
   - Total error ||xi_{lambda,N} - k_lambda|| <= ||xi - k_N|| + 2*Tail_N.
   - Under sublinear stability growth sqrt(H_a(delta)) = O(lambda^delta),
     verify that total stability transfer error sqrt(H_a(delta)) * ||xi - k|| -> 0 as lambda -> infty.
"""

import sys
import numpy as np
import mpmath as mp

mp.mp.dps = 30


def check_analytic_truncation_tail():
    print("Checking analytic truncation tail under N = kappa * (log lambda)^2 schedule:")
    rho = 0.5  # Analyticity strip half-width
    for kappa in [1.0, 1.5, 2.0]:
        print(f"  Schedule parameter kappa={kappa:.1f}:")
        for lam in [10, 50, 200, 1000]:
            a = float(np.log(lam))
            N = int(np.ceil(kappa * a * a))
            # Fourier tail bound: sum_{|j| > N} exp(-2*pi*|j|*rho/a)
            # = 2 * exp(-2*pi*(N+1)*rho/a) / (1 - exp(-2*pi*rho/a))
            decay_rate = 2 * np.pi * rho / a
            tail_sq = 2 * np.exp(-2 * np.pi * (N + 1) * rho / a) / (1 - np.exp(-decay_rate))
            tail = np.sqrt(tail_sq)

            # Theoretical power law: lambda^(-pi * kappa * rho)
            theoretical_power = lam ** (-np.pi * kappa * rho)
            ratio = tail / theoretical_power
            print(f"    lambda={lam:4d}, N={N:3d}: tail={tail:.2e}, lambda^(-{np.pi*kappa*rho:.2f})={theoretical_power:.2e}, ratio={ratio:.2f}")
            assert tail <= 2.0 * theoretical_power, f"Tail exceeded power law for lambda={lam}"
    print("  Analytic truncation tail power-law decay verified: PASS")


def check_rayleigh_eigenvector_inequality():
    print("Checking Rayleigh quotient to eigenvector inequality:")
    np.random.seed(42)
    for dim in [5, 10, 20]:
        # Generate symmetric matrix with controlled gap
        M = np.random.randn(dim, dim)
        A = 0.5 * (M + M.T)
        evals, evecs = np.linalg.eigh(A)

        # Enforce gap
        g = evals[1] - evals[0]
        if g < 0.05:
            evals[1] = evals[0] + 0.1
            A = evecs @ np.diag(evals) @ evecs.T
            evals, evecs = np.linalg.eigh(A)
            g = evals[1] - evals[0]

        xi_1 = evecs[:, 0]
        eps_1 = evals[0]

        # Test perturbed vectors v
        for perturbation_norm in [0.01, 0.05, 0.1, 0.2]:
            eta = np.random.randn(dim)
            eta -= np.dot(xi_1, eta) * xi_1  # orthogonal to xi_1
            eta = eta / np.linalg.norm(eta)

            # v = cos(theta)*xi_1 + sin(theta)*eta
            theta = perturbation_norm
            v = np.cos(theta) * xi_1 + np.sin(theta) * eta

            R_v = float(v.T @ A @ v)
            defect = R_v - eps_1
            vec_err_sq = float(np.linalg.norm(v - xi_1) ** 2)

            # Theoretical bound: ||v - xi_1||^2 <= 2 * defect / g
            bound = 2.0 * defect / g

            assert defect >= -1e-14, f"Rayleigh defect negative: {defect}"
            assert vec_err_sq <= bound + 1e-12, f"Inequality violated: err_sq={vec_err_sq}, bound={bound}"

    print("  Rayleigh-to-eigenvector inequality ||v - xi||^2 <= 2*(R(v)-eps)/gap verified: PASS")


def check_combined_stability_transfer():
    print("Checking combined stability transfer to closed substrips S_delta:")
    # Parameters
    delta = 0.45  # Substrip height < 0.5
    kappa = 1.0   # Schedule N = kappa * (log lambda)^2
    rho = 0.5     # Analyticity
    alpha = 1.0   # Candidate defect order: defect = O(lambda^(-2*alpha)) => error = O(lambda^(-alpha))
    gap = 0.15    # Constant or slowly decaying spectral gap (e.g. Route A/B gap ~ 0.15)

    transfer_errs = []
    for lam in [10, 50, 200, 1000]:
        a = float(np.log(lam))
        N = int(np.ceil(kappa * a * a))

        # 1. Truncation tail
        tail_sq = 2 * np.exp(-2 * np.pi * (N + 1) * rho / a) / (1 - np.exp(-2 * np.pi * rho / a))
        tail = np.sqrt(tail_sq)

        # 2. Rayleigh error
        defect = 1.0 / (lam ** (2 * alpha))
        rayleigh_err = np.sqrt(2 * defect / gap)

        # 3. Total vector error
        total_vec_err = rayleigh_err + 2 * tail

        # 4. Hyperbolic stability scale on S_delta
        H_val = float(mp.sinh(2 * delta * a) / delta)
        sqrt_H = np.sqrt(H_val)

        # 5. Stability transfer error
        transfer_err = sqrt_H * total_vec_err
        transfer_errs.append(transfer_err)

        print(f"  lambda={lam:4d}, N={N:3d}: sqrt(H)={sqrt_H:.2f}, vec_err={total_vec_err:.2e}, transfer_err={transfer_err:.2e}")

    # Check asymptotic decay: error at lambda=1000 must be < 0.10 and much smaller than at lambda=10
    assert transfer_errs[-1] < 0.10, f"Asymptotic transfer error not small enough: {transfer_errs[-1]}"
    assert transfer_errs[-1] < transfer_errs[0] / 10.0, f"Error did not decay asymptotically: {transfer_errs}"
    print("  Combined stability transfer asymptotic decay verified: PASS")


def main() -> int:
    print("=== RH-R074 Quantitative Eigenvector Error and Schedule Sanity Replay ===")
    check_analytic_truncation_tail()
    check_rayleigh_eigenvector_inequality()
    check_combined_stability_transfer()
    print("RH-R074 sanity replay: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

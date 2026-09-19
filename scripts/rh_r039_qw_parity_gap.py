#!/usr/bin/env python3
"""RH-R039 deterministic finite parity-gap evidence runner.

Implements the finite Connes-Consani-Moscovici Weil-form matrix

    QW_lambda = W_{0,2} - W_R - sum_p W_p.

Evidence only: no full parity-gap, Galerkin-tail, simplicity,
determinant-convergence, or RH claim.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Dict, Iterable, Tuple

import mpmath as mp


def von_mangoldt_table(limit: int) -> Dict[int, mp.mpf]:
    out: Dict[int, mp.mpf] = {}
    for k in range(2, limit + 1):
        for p in range(2, k + 1):
            if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
                continue
            q = p
            while q < k:
                q *= p
            if q == k:
                out[k] = mp.log(p)
                break
    return out


def finite_blocks(lambda2: int, nmax: int, dps: int, quadrature_degree: int):
    mp.mp.dps = dps
    L = mp.log(lambda2)
    nodes, weights = mp.gauss_quadrature(quadrature_degree, "legendre")
    quad_x = [L * (x + 1) / 2 for x in nodes]
    quad_w = [L * w / 2 for w in weights]
    arch_const = mp.euler + mp.log(
        4 * mp.pi * (mp.e**L - 1) / (mp.e**L + 1)
    )
    mangoldt = von_mangoldt_table(lambda2)

    def q_kernel(m: int, n: int, x: mp.mpf) -> mp.mpf:
        if m == n:
            return 2 * (1 - x / L) * mp.cos(2 * mp.pi * n * x / L)
        return (
            mp.sin(2 * mp.pi * m * x / L)
            - mp.sin(2 * mp.pi * n * x / L)
        ) / (mp.pi * (n - m))

    def point_term(m: int, n: int) -> mp.mpf:
        return (
            32
            * L
            * mp.sinh(L / 4) ** 2
            * (L**2 - 16 * mp.pi**2 * m * n)
            / (
                (L**2 + 16 * mp.pi**2 * m * m)
                * (L**2 + 16 * mp.pi**2 * n * n)
            )
        )

    def prime_term(m: int, n: int) -> mp.mpf:
        return mp.fsum(
            mangoldt[k] / mp.sqrt(k) * q_kernel(m, n, mp.log(k))
            for k in mangoldt
        )

    arch_cache: Dict[Tuple[int, int], mp.mpf] = {}

    def arch_term(m: int, n: int) -> mp.mpf:
        key = (m, n) if m <= n else (n, m)
        if key in arch_cache:
            return arch_cache[key]
        a, b = key
        w0 = q_kernel(a, b, mp.mpf("0"))
        integral = mp.fsum(
            w
            * (mp.e ** (x / 2) * q_kernel(a, b, x) - w0)
            / (mp.e**x - mp.e ** (-x))
            for x, w in zip(quad_x, quad_w)
        )
        value = w0 * arch_const / 2 + integral
        arch_cache[key] = value
        return value

    entry_cache: Dict[Tuple[int, int], mp.mpf] = {}

    def total(m: int, n: int) -> mp.mpf:
        key = (m, n)
        if key not in entry_cache:
            entry_cache[key] = (
                point_term(m, n) - prime_term(m, n) - arch_term(m, n)
            )
        return entry_cache[key]

    even = mp.matrix(nmax + 1)
    odd = mp.matrix(nmax)
    even[0, 0] = total(0, 0)
    root2 = mp.sqrt(2)
    for n in range(1, nmax + 1):
        even[0, n] = root2 * total(0, n)
        even[n, 0] = even[0, n]

    for m in range(1, nmax + 1):
        for n in range(1, nmax + 1):
            even[m, n] = total(m, n) + total(m, -n)
            odd[m - 1, n - 1] = total(m, n) - total(m, -n)

    max_symmetry_residual = mp.mpf("0")
    max_parity_residual = mp.mpf("0")
    for m in range(-nmax, nmax + 1):
        for n in range(-nmax, nmax + 1):
            max_symmetry_residual = max(
                max_symmetry_residual, abs(total(m, n) - total(n, m))
            )
            max_parity_residual = max(
                max_parity_residual, abs(total(m, n) - total(-m, -n))
            )

    return even, odd, max_symmetry_residual, max_parity_residual


def sector_data(even, odd, n_values: Iterable[int]):
    out = {}
    for n in n_values:
        even_vals = mp.eigsy(even[: n + 1, : n + 1], eigvals_only=True)
        odd_vals = mp.eigsy(odd[:n, :n], eigvals_only=True)
        eps_plus = min(even_vals)
        eps_minus = min(odd_vals)
        out[n] = {
            "epsilon_plus": eps_plus,
            "epsilon_minus": eps_minus,
            "gap": eps_minus - eps_plus,
        }
    return out


def decimal(x: mp.mpf, digits: int = 40) -> str:
    return mp.nstr(x, digits)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda2", nargs="+", type=int, default=[13, 14])
    parser.add_argument("--n-values", nargs="+", type=int,
                        default=[2, 4, 6, 8, 10, 12])
    parser.add_argument("--dps", nargs="+", type=int, default=[50, 80])
    parser.add_argument("--quadrature-degrees", nargs="+", type=int,
                        default=[96, 128, 160])
    parser.add_argument("--json-out", default="rh_r039_evidence.json")
    parser.add_argument("--csv-out", default="rh_r039_evidence.csv")
    args = parser.parse_args()

    nmax = max(args.n_values)
    records = {}
    diagnostics = {}

    for lambda2 in args.lambda2:
        configs = {}
        for dps in args.dps:
            for degree in args.quadrature_degrees:
                even, odd, sym_res, par_res = finite_blocks(
                    lambda2=lambda2,
                    nmax=nmax,
                    dps=dps,
                    quadrature_degree=degree,
                )
                configs[(dps, degree)] = sector_data(even, odd, args.n_values)
                diagnostics[f"{lambda2}:{dps}:{degree}"] = {
                    "matrix_symmetry_residual": decimal(sym_res),
                    "parity_residual": decimal(par_res),
                }

        reference_key = (max(args.dps), max(args.quadrature_degrees))
        reference = configs[reference_key]
        records[str(lambda2)] = {}

        for n in args.n_values:
            ref = reference[n]
            row = {}
            for field in ("epsilon_plus", "epsilon_minus", "gap"):
                spread = max(
                    abs(cfg[n][field] - ref[field])
                    for cfg in configs.values()
                )
                row[field] = decimal(ref[field])
                row[f"{field}_crosscheck_abs_spread"] = decimal(spread)
            row["finite_gap_sign"] = (
                "positive" if ref["gap"] > 0 else
                "negative" if ref["gap"] < 0 else "zero"
            )
            records[str(lambda2)][str(n)] = row

    payload = {
        "campaign": "RH-001",
        "target": "RH-R039-QW-PARITY-GAP-EVIDENCE-001",
        "evidence_boundary": (
            "Finite high-precision Galerkin evidence only. "
            "No full parity-gap, tail-certificate, simplicity, "
            "determinant-convergence, or RH claim."
        ),
        "source_formula": "CCM QW_lambda = W_{0,2} - W_R - sum_p W_p",
        "parameters": {
            "lambda2": args.lambda2,
            "n_values": args.n_values,
            "dps": args.dps,
            "quadrature_degrees": args.quadrature_degrees,
            "reference_configuration": {
                "dps": max(args.dps),
                "quadrature_degree": max(args.quadrature_degrees),
            },
        },
        "diagnostics": diagnostics,
        "results": records,
    }
    Path(args.json_out).write_text(json.dumps(payload, indent=2) + "\n")

    with Path(args.csv_out).open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "lambda2", "N", "epsilon_plus", "epsilon_minus", "gap",
            "gap_crosscheck_abs_spread", "finite_gap_sign",
        ])
        for lambda2 in args.lambda2:
            for n in args.n_values:
                row = records[str(lambda2)][str(n)]
                writer.writerow([
                    lambda2, n, row["epsilon_plus"], row["epsilon_minus"],
                    row["gap"], row["gap_crosscheck_abs_spread"],
                    row["finite_gap_sign"],
                ])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

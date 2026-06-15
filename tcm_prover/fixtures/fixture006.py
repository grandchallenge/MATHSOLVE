from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

WEIGHTS: list[list[int]] = [
    [10, 6, 5, 4, 3],
    [12, 17, 11, 10, 9],
    [8, 7, 13, 6, 5],
    [16, 15, 14, 21, 13],
    [18, 17, 16, 15, 24],
]
DUAL_ROWS: list[int] = [10, 17, 13, 21, 24]
DUAL_COLS: list[int] = [0, 0, 0, 0, 0]
OPTIMUM = 85


@dataclass(frozen=True)
class SemiringResult:
    optimum: int
    optimum_count: int
    witness_cols: list[int]
    trace: list[dict[str, Any]]


def solve_assignment_max_plus_count(weights: list[list[int]]) -> SemiringResult:
    """Exact max-plus/count contraction for a square assignment tensor network."""
    n = len(weights)
    dp: dict[int, tuple[int, int, tuple[int, ...]]] = {0: (0, 1, ())}
    trace: list[dict[str, Any]] = []

    for row in range(n):
        next_dp: dict[int, tuple[int, int, tuple[int, ...]]] = {}
        for mask, (score, count, cols) in dp.items():
            for col in range(n):
                if mask & (1 << col):
                    continue
                new_mask = mask | (1 << col)
                candidate_score = score + weights[row][col]
                incumbent = next_dp.get(new_mask)
                if incumbent is None or candidate_score > incumbent[0]:
                    next_dp[new_mask] = (candidate_score, count, cols + (col,))
                elif candidate_score == incumbent[0]:
                    next_dp[new_mask] = (incumbent[0], incumbent[1] + count, incumbent[2])
        dp = next_dp
        trace.append(
            {
                "eliminated_row": row,
                "table_entries": len(dp),
                "mask_width": row + 1,
                "best_prefix_score": max(score for score, _, _ in dp.values()),
            }
        )

    final_mask = (1 << n) - 1
    optimum, optimum_count, witness = dp[final_mask]
    return SemiringResult(optimum, optimum_count, list(witness), trace)


def validate_witness(weights: list[list[int]], cols: list[int]) -> int:
    n = len(weights)
    if len(cols) != n:
        raise ValueError("witness must pick one column per row")
    if sorted(cols) != list(range(n)):
        raise ValueError("witness must use each column exactly once")
    return sum(weights[i][col] for i, col in enumerate(cols))


def validate_dual_certificate(weights: list[list[int]], row_duals: list[int], col_duals: list[int]) -> int:
    n = len(weights)
    if len(row_duals) != n or len(col_duals) != n:
        raise ValueError("dual certificate dimensions do not match instance")
    for i in range(n):
        for j in range(n):
            if row_duals[i] + col_duals[j] < weights[i][j]:
                raise ValueError(f"dual violation at ({i},{j})")
    return sum(row_duals) + sum(col_duals)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_opb(path: Path, weights: list[list[int]]) -> None:
    n = len(weights)
    terms = [f"+{weights[i][j]} x_{i}_{j}" for i in range(n) for j in range(n)]
    lines = [f"* #variable= {n * n} #constraint= {2 * n}", "max: " + " ".join(terms) + " ;"]
    for i in range(n):
        lines.append(" ".join(f"+1 x_{i}_{j}" for j in range(n)) + " = 1 ;")
    for j in range(n):
        lines.append(" ".join(f"+1 x_{i}_{j}" for i in range(n)) + " = 1 ;")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def witness_assignment(cols: list[int]) -> dict[str, int]:
    return {f"x_{i}_{col}": 1 for i, col in enumerate(cols)}


def build_artifacts(out_dir: Path) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    result = solve_assignment_max_plus_count(WEIGHTS)
    if result.optimum != OPTIMUM:
        raise AssertionError(f"unexpected fixture optimum {result.optimum}")

    primal = validate_witness(WEIGHTS, result.witness_cols)
    upper = validate_dual_certificate(WEIGHTS, DUAL_ROWS, DUAL_COLS)
    if primal != upper:
        raise AssertionError("fixture witness and dual certificate do not meet")

    write_opb(out_dir / "instance.opb", WEIGHTS)
    write_json(
        out_dir / "primal_witness.json",
        {
            "schema_version": "0.1.0",
            "problem": "max_weight_assignment_pb",
            "selected_cols": result.witness_cols,
            "assignment": witness_assignment(result.witness_cols),
            "objective": result.optimum,
        },
    )
    write_json(
        out_dir / "pb_dual_certificate.json",
        {
            "schema_version": "0.1.0",
            "type": "assignment_lp_dual_upper_bound",
            "row_duals": DUAL_ROWS,
            "col_duals": DUAL_COLS,
            "upper_bound": upper,
            "trusted_rule": "For all i,j, row_dual_i + col_dual_j >= W_ij; summing one chosen row and one chosen column bound gives the objective upper bound.",
        },
    )
    (out_dir / "checker_transcript.txt").write_text(
        "MATHSOLVE emitted artifacts. Run the MATHCERT PB checker for external certification.\n",
        encoding="utf-8",
    )
    (out_dir / "failure_mode_ledger.md").write_text(
        "# Fixture 006 Failure-Mode Ledger\n\n"
        "| Failure mode | Status discipline |\n"
        "| --- | --- |\n"
        "| Missing external checker | Keep result at `artifact_emitted`; do not claim certification. |\n"
        "| Malformed certificate | MATHCERT rejects before checking optimum. |\n"
        "| Witness infeasibility | MATHCERT rejects primal lower bound. |\n"
        "| Dual-bound failure | MATHCERT rejects upper-bound certificate. |\n"
        "| Optimum mismatch | MATHCERT marks failed. |\n",
        encoding="utf-8",
    )
    (out_dir / "proof_import_stub.lean").write_text(
        "-- TCM Fixture 006 proof-import stub.\n"
        "-- Audit scaffold only; not a completed Lean proof.\n",
        encoding="utf-8",
    )
    result_card = {
        "fixture": "TCM-Prover Fixture 006",
        "route_family": "SEMIRING-CONTRACTION/TCM",
        "status": "artifact_emitted",
        "claim": {"problem": "max_weight_assignment_pb", "optimum": result.optimum, "optimum_count": result.optimum_count},
        "certificate": {
            "opb_path": "artifacts/fixture006/instance.opb",
            "primal_witness_path": "artifacts/fixture006/primal_witness.json",
            "dual_certificate_path": "artifacts/fixture006/pb_dual_certificate.json",
            "proof_import_stub_path": "artifacts/fixture006/proof_import_stub.lean",
        },
        "trace": result.trace,
        "trust_boundary": "TCM search is untrusted; MATHCERT certificate replay is trusted.",
    }
    write_json(out_dir / "result_card.json", result_card)
    (out_dir / "fixture006_report.md").write_text(
        "# TCM-Prover Fixture 006: External Checker Round-Trip\n\n"
        "Exact max-plus/count contraction emits an OPB instance, primal witness, and dual certificate for MATHCERT replay.\n\n"
        "Optimum: `85`; optimum count: `1`.\n",
        encoding="utf-8",
    )
    return result_card


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run TCM-Prover Fixture 006 artifact emission.")
    parser.add_argument("--out", type=Path, default=Path("artifacts/fixture006"))
    args = parser.parse_args(argv)
    print(json.dumps(build_artifacts(args.out), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

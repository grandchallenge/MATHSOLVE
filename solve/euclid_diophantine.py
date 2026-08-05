#!/usr/bin/env python3
"""Deterministic bounded linear-Diophantine candidate producer."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

FORGE_INPUT = {
    "repository": "grandchallenge/MATHFORGE",
    "commit_sha": "af5398a05f17789a061ab0d23c2b47f0cc952fff",
    "package": {
        "path": "sources/EUCLID-DIOPHANTINE-E2E-002/forge_package.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "e89d5b7c611aaa4a7fdea716742e993eaa283da1",
    },
    "provider_manifest": {
        "path": "provider_manifests/EUCLID-DIOPHANTINE-E2E-002.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "de9dae12cd578ee98b58e6fc1b39365f8c1e7109",
    },
}

PROTECTED_STAGE1 = {
    "solve_merge_commit": "3a8493aa322f0e640c921b8824c4d7f88a8c057d",
    "solve_candidate": {
        "path": "certificates/EUCLID-GCD-E2E-001.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "af54ae9b9a047a36767b2599ebc649fb6fdaaa52",
    },
    "cert_merge_commit": "78b69e6a3461a83f4893d61c421b1570c08a9ba6",
    "certification_output": {
        "path": "governance/certification_outputs/EUCLID-GCD-E2E-001.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "36c62434dbd19719d990e71ddc23729f0614ace7",
        "disposition": "CERTIFIED_CHECKER_SOUNDNESS_AND_CONCRETE_GCD_INSTANCE",
    },
    "normalized_gcd": 21,
    "positive_bezout": {"x": -2, "y": 5},
}


def _base_bezout(a: int, b: int) -> tuple[int, int]:
    if (abs(a), abs(b)) != (252, 105):
        raise ValueError("coefficients are outside the protected Stage 1 fixture family")
    x = -2 if a >= 0 else 2
    y = 5 if b >= 0 else -5
    return x, y


def solve_case(a: int, b: int, c: int, *, case_id: str) -> dict[str, Any]:
    if a == 0 and b == 0:
        raise ValueError("(0,0) is excluded")
    base_x, base_y = _base_bezout(a, b)
    d = 21
    absolute_target = abs(c)
    quotient, remainder = divmod(absolute_target, d)
    common = {
        "case_id": case_id,
        "inputs": {"a": a, "b": b, "c": c},
        "normalized_gcd": d,
        "decision_basis": "exact_divisibility_by_protected_gcd",
    }
    if remainder == 0:
        scale = c // d
        x, y = scale * base_x, scale * base_y
        return {
            **common,
            "evidence_type": "constructive_solution",
            "constructive_solution": {
                "base_bezout": {"x": base_x, "y": base_y, "equation_value": d},
                "scale_factor": scale,
                "x": x,
                "y": y,
                "equation_value": a * x + b * y,
            },
            "divisibility_obstruction": None,
        }
    return {
        **common,
        "evidence_type": "divisibility_obstruction",
        "constructive_solution": None,
        "divisibility_obstruction": {
            "absolute_target": absolute_target,
            "quotient": quotient,
            "remainder": remainder,
            "equation_value": quotient * d + remainder,
            "strict_nonzero_remainder": True,
        },
    }


def build_candidate(cases: list[tuple[str, int, int, int]] | None = None) -> dict[str, Any]:
    selected = cases or [
        ("DIO-POS-252-105-84", 252, 105, 84),
        ("DIO-NEG-252-105-20", 252, 105, 20),
    ]
    return {
        "schema_version": "1.0.0",
        "certificate_id": "MS-CANDIDATE-EUCLID-DIOPHANTINE-E2E-002",
        "campaign_id": "EUCLID-DIOPHANTINE-E2E-002",
        "authority_state": "candidate_only",
        "forge_input": FORGE_INPUT,
        "protected_stage1": PROTECTED_STAGE1,
        "candidate_scope": {
            "coefficient_family": "(abs(a),abs(b)) = (252,105)",
            "target": "any integer c",
            "arbitrary_diophantine_completeness_claimed": False,
        },
        "cases": [
            solve_case(a, b, c, case_id=case_id)
            for case_id, a, b, c in selected
        ],
        "solver": {
            "algorithm": "scale_protected_bezout_or_emit_divisibility_remainder",
            "implementation_path": "solve/euclid_diophantine.py",
            "canonical_command": "python solve/euclid_diophantine.py --output /tmp/euclid-diophantine.json",
            "arithmetic": "unbounded_python_integers",
            "network_used": False,
            "randomness_used": False,
            "timeout_or_failed_search_used_as_unsat": False,
            "recomputes_gcd": False,
        },
        "claim_boundary": {
            "constructive_witness_accepted": False,
            "unsatisfiable_obstruction_accepted": False,
            "theorem_certified": False,
            "arbitrary_diophantine_completeness_claimed": False,
            "novelty_claimed": False,
            "priority_claimed": False,
            "historical_verbatim_equivalence_claimed": False,
            "statement": "This deterministic Solve package emits bounded candidate evidence for independent MATHCERT checking. It has no certification effect.",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int)
    parser.add_argument("--b", type=int)
    parser.add_argument("--c", type=int)
    parser.add_argument("--case-id", default="DIO-AD-HOC")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    supplied = [args.a is not None, args.b is not None, args.c is not None]
    if any(supplied) and not all(supplied):
        parser.error("--a, --b, and --c must be supplied together")
    cases = None
    if all(supplied):
        cases = [(args.case_id, args.a, args.b, args.c)]
    candidate = build_candidate(cases)
    rendered = json.dumps(candidate, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

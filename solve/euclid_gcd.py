#!/usr/bin/env python3
"""Deterministic extended-Euclidean candidate producer for EUCLID-GCD-E2E-001."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

FORGE_INPUT = {
    "repository": "grandchallenge/MATHFORGE",
    "commit_sha": "3622bac82a39cdb9e82ec463919d9e6927c1ec0e",
    "package": {
        "path": "sources/EUCLID-GCD-E2E-001/forge_package.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "079b68fb5651e0d2eee0a7b2002454d34673d84c",
    },
    "provider_manifest": {
        "path": "provider_manifests/EUCLID-GCD-E2E-001.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "a103b2c85dbd67973da43656fed5af567c5b7074",
    },
}


def extended_euclid(a: int, b: int) -> tuple[int, int, int, list[dict[str, int]]]:
    if a < 0 or b < 0:
        raise ValueError("inputs must be natural numbers")
    if a == 0 and b == 0:
        raise ValueError("(0,0) is excluded by the Forge contract")

    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    trace: list[dict[str, int]] = []

    while r != 0:
        quotient, remainder = divmod(old_r, r)
        trace.append(
            {
                "dividend": old_r,
                "divisor": r,
                "quotient": quotient,
                "remainder": remainder,
            }
        )
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t, trace


def build_candidate(a: int, b: int) -> dict[str, Any]:
    d, x, y, trace = extended_euclid(a, b)
    return {
        "schema_version": "1.0.0",
        "certificate_id": "MS-CANDIDATE-EUCLID-GCD-E2E-001",
        "campaign_id": "EUCLID-GCD-E2E-001",
        "authority_state": "candidate_only",
        "forge_input": FORGE_INPUT,
        "inputs": {"a": a, "b": b},
        "result": {"d": d},
        "euclidean_trace": trace,
        "bezout_witness": {"x": x, "y": y, "equation_value": x * a + y * b},
        "solver": {
            "algorithm": "deterministic_extended_euclid",
            "implementation_path": "solve/euclid_gcd.py",
            "command": f"python solve/euclid_gcd.py --a {a} --b {b}",
            "arithmetic": "unbounded_python_integers",
            "network_used": False,
            "randomness_used": False,
        },
        "claim_boundary": {
            "certificate_accepted": False,
            "theorem_certified": False,
            "novelty_claimed": False,
            "priority_claimed": False,
            "historical_verbatim_equivalence_claimed": False,
            "statement": "This deterministic Solve output is a candidate witness for independent MATHCERT checking. It has no certification effect.",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--b", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    candidate = build_candidate(args.a, args.b)
    rendered = json.dumps(candidate, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

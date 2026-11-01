#!/usr/bin/env python3
"""Run genuine protected H2/WP02 witness replay for Solve specialist pilot #1040.

This is a reproducible source-side producer *input*, not a specialist receipt.
It does not validate the rejected exact-search design or certify a theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALUATOR = ROOT / "work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/busy-beaver-6-certificates/PUBLIC_SOURCE/eval.py"
ADJUDICATION = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/adjudications/OM26-H2-WP02-ADJ-001.json"
RAW = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/raw/OM26-H2-WP02-IA-001/github-comment-5889734796.md"
DISPATCH = "OM26-H2-WP02-IA-001"

W89911 = {
    ("A",0):(1,"R","B"), ("A",1):(1,"L","E"),
    ("B",0):(1,"R","C"), ("B",1):(1,"R","B"),
    ("C",0):(1,"R","D"), ("C",1):(1,"L","H"),
    ("D",0):(1,"L","A"), ("D",1):(1,"L","D"),
    ("E",0):(0,"R","F"), ("E",1):(0,"L","F"),
    ("F",0):(1,"L","C"), ("F",1):(0,"L","A"),
}
W8021 = {
    ("A",0):(0,"R","B"), ("A",1):(1,"L","D"),
    ("B",0):(1,"R","C"), ("B",1):(1,"L","D"),
    ("C",0):(1,"R","D"), ("C",1):(1,"R","C"),
    ("D",0):(1,"R","E"), ("D",1):(0,"L","F"),
    ("E",0):(0,"L","A"), ("E",1):(1,"L","E"),
    ("F",0):(1,"L","H"), ("F",1):(0,"L","B"),
}
EXPECTED = {
    "W89911": {"steps":89911, "ones":185, "tape_span":541},
    "W8021": {"steps":8021, "ones":41, "tape_span":122},
}


class ReplayFailure(ValueError):
    pass


def check(condition: bool, reason: str) -> None:
    if not condition:
        raise ReplayFailure(reason)


def load_evaluator(path: Path):
    spec = importlib.util.spec_from_file_location("gcl_wp02_protected_evaluator", path)
    check(spec is not None and spec.loader is not None, "protected evaluator not loadable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    check(callable(getattr(module, "_run", None)), "protected evaluator lacks _run")
    return module


def verify(root: Path = ROOT, *, expected: dict | None = None) -> dict:
    raw = (root / RAW.relative_to(ROOT)).read_bytes()
    adj = json.loads((root / ADJUDICATION.relative_to(ROOT)).read_text(encoding="utf-8"))
    check(adj.get("dispatch_id") == DISPATCH, "wrong adjudicated dispatch")
    check(adj.get("disposition") == "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED",
          "adjudication disposition changed")
    check(adj.get("lifecycle_effect", {}).get("certification") == "NONE", "certification effect present")
    check(adj.get("lifecycle_effect", {}).get("competition") == "NONE", "competition effect present")
    claims = {x.get("claim_id") for x in adj.get("accepted_claims", [])}
    check(claims == {"OM26-H2-W89911-001", "OM26-H2-W8021-001"},
          "accepted witness set changed")
    check(hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest() ==
          adj["source_result"]["raw_git_blob_sha1"], "protected result blob changed")
    evaluator = load_evaluator(root / EVALUATOR.relative_to(ROOT))
    reference = expected if expected is not None else EXPECTED
    actual = {}
    for name, machine in (("W89911", W89911), ("W8021", W8021)):
        result = evaluator._run(machine, 250000)
        check(result.get("halted") is True, f"{name}: did not halt")
        check(set(result.get("reached", set())) == set("ABCDEF"), f"{name}: not all states reached")
        metrics = {k: result.get(k) for k in ("steps", "ones", "tape_span")}
        check(metrics == reference[name], f"{name}: protected evaluator mismatch")
        actual[name] = metrics
    return {
        "record_type": "GCL_SOLVE_REAL_REPLAY_WITNESS_PREFLIGHT",
        "dispatch_id": DISPATCH,
        "raw_sha256": hashlib.sha256(raw).hexdigest(),
        "protected_evaluator_path": str(EVALUATOR.relative_to(ROOT)),
        "adjudication_path": str(ADJUDICATION.relative_to(ROOT)),
        "replay_pass": True,
        "witnesses": actual,
        "exact_search_design_admitted": False,
        "mathematical_certification": False,
        "specialist_positive_receipt": False,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args()
    print(json.dumps(verify(args.root), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

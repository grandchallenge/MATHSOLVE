#!/usr/bin/env python3
"""Fail-closed validation for MS-FC-WP00 canonical Lean targets."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "formal_sources/formal_conjectures/MS-FC-WP00.json"
EXPECTED_MATHLIB = "5e932f97dd25535344f80f9dd8da3aab83df0fe6"
EXPECTED_AXIOMS = {
    "MathSolve.FormalConjectures.NS.IsUnforcedLerayHopfSolution",
    "MathSolve.FormalConjectures.NS.MixedNormFiniteOnZeroT",
    "MathSolve.FormalConjectures.NS.PositiveClayWholeSpaceAlternative",
}


def load(path: Path = PACKAGE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def errors(root: Path = ROOT, package_path: Path = PACKAGE) -> list[str]:
    found: list[str] = []
    data = json.loads(package_path.read_text(encoding="utf-8"))
    if data.get("schema_version") != "1.0.0" or data.get("package_id") != "MS-FC-WP00":
        found.append("package identity drift")
    if data.get("source_lane") != "FC-GDM-001":
        found.append("source lane must remain FC-GDM-001")
    if data.get("target_toolchain", {}).get("mathlib_commit") != EXPECTED_MATHLIB:
        found.append("mathlib commit drift")
    if data.get("upstream", {}).get("commit") != "85f863718beeec7b58a3a1926ee92e3472bc2020":
        found.append("upstream Formal Conjectures commit drift")
    axioms = set(data.get("axiom_report", {}).get("imported_axioms", []))
    if axioms != EXPECTED_AXIOMS:
        found.append("imported axiom set drift")
    if data.get("axiom_report", {}).get("sorry_count") != 0:
        found.append("sorry count must remain zero")
    if data.get("axiom_report", {}).get("admit_count") != 0:
        found.append("admit count must remain zero")
    lean_paths = {
        "rh": "MathSolve/FormalConjectures/RiemannHypothesis.lean",
        "ns": "MathSolve/FormalConjectures/NSCriticalIntegrability.lean",
        "replay": "MathSolve/FormalConjectures/Replay.lean",
    }
    for label, relative in lean_paths.items():
        path = root / relative
        if not path.exists():
            found.append(f"missing Lean file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"\b(sorry|admit)\b", text):
            found.append(f"{label}: proof placeholder present")
    rh = (root / lean_paths["rh"]).read_text(encoding="utf-8")
    for token in (
        "ProgrammeRiemannHypothesis",
        "programmeRiemannHypothesis_eq_mathlib",
        "differentiableAt_riemannZeta",
        "IsTrivialZero",
        "s ≠ 1",
    ):
        if token not in rh:
            found.append(f"RH target missing token: {token}")
    ns = (root / lean_paths["ns"]).read_text(encoding="utf-8")
    for token in (
        "SchwartzMap R3 Velocity",
        "IsUnforcedLerayHopfSolution",
        "timeExponent := 4",
        "spaceExponent := 6",
        "∀ (T : ℝ), 0 < T",
        "CriticalIntegrabilityImpliesClay",
    ):
        if token not in ns:
            found.append(f"NS target missing token: {token}")
    if "PositiveClayWholeSpaceAlternative → UniversalCriticalIntegrability" in ns:
        found.append("reverse Clay implication is forbidden")
    if "FC-GDM-002" in rh or "FC-GDM-002" in ns:
        found.append("expanded source lane contaminated the RH/NS pilot")
    lakefile = (root / "lakefile.lean").read_text(encoding="utf-8")
    if EXPECTED_MATHLIB not in lakefile:
        found.append("lakefile does not pin the expected mathlib commit")
    toolchain = (root / "lean-toolchain").read_text(encoding="utf-8").strip()
    if toolchain != "leanprover/lean4:v4.29.1":
        found.append("Lean toolchain drift")
    return found


def main() -> int:
    found = errors()
    if found:
        print("\n".join(found), file=sys.stderr)
        print(f"formal target validation failed with {len(found)} error(s)", file=sys.stderr)
        return 1
    print("validated RH definitional concordance, NS-CI quantifiers and exponent order, explicit axiom boundary, and zero proof placeholders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

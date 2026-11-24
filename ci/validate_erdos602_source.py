#!/usr/bin/env python3
"""Verify the pinned FC #602 archive and deterministic Lean source extract."""
from hashlib import sha1
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "85f863718beeec7b58a3a1926ee92e3472bc2020"
BLOB = "9b85fd453afcfa95c6572e2a98d214d50f7e8caa"
ARCHIVE = ROOT / "research/ERDOS-602/upstream-602.lean.txt"
EXTRACT = ROOT / "MathSolve/FormalConjectures/E602SourceExtract.lean"


def git_blob(data: bytes) -> str:
    return sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def extract(data: bytes) -> str:
    if git_blob(data) != BLOB:
        raise ValueError("pinned FormalConjectures source blob mismatch")
    s = data.decode("utf-8")
    header = s[:s.index("import FormalConjecturesUtil")]
    defs = s[s.index("def IsMonochromatic"):s.index("/- ## Main open problem")].rstrip()
    count = s.split("theorem erdos_602.variants.countable_index : answer(True) ↔\n", 1)[1].split(" := by\n  sorry", 1)[0]
    main = s.split("theorem erdos_602 : answer(sorry) ↔\n", 1)[1].split(" := by\n  sorry", 1)[0]
    return header + f"""/- Source-extracted from google-deepmind/formal-conjectures at
{PIN}, blob
{BLOB}.
Exact predicates and right-hand-side propositions, with import and
declaration wrappers adapted to MATHSOLVE's pinned Mathlib.
This is not an import or compilation of the full upstream package. -/
import Mathlib

open Set
namespace Erdos602

{defs}

def CountableIndexTarget : Prop :=
{count}

def UnrestrictedTarget : Prop :=
{main}

end Erdos602
"""


def verify(data: bytes, actual: str) -> None:
    expected = extract(data)
    if actual != expected:
        raise ValueError("compiled source extract differs from pinned upstream declarations")


def main() -> None:
    source = ARCHIVE.read_bytes()
    actual = EXTRACT.read_bytes().decode("utf-8")
    verify(source, actual)
    # Negative controls reject both source drift and adapted extract drift.
    for bad_source, bad_extract in (
        (source + b"\n", actual),
        (source, actual.replace("¬IsMonochromatic", "IsMonochromatic", 1)),
        (source, actual.replace("Set.ncard (A i ∩ A j) ≠ 1", "Set.ncard (A i ∩ A j) = 1", 1)),
    ):
        try:
            verify(bad_source, bad_extract)
        except ValueError:
            continue
        raise RuntimeError("negative source-lock control unexpectedly passed")
    print(f"PASS: exact FC #602 Git blob {BLOB}; deterministic source extract; 3 negative controls")


if __name__ == "__main__":
    main()

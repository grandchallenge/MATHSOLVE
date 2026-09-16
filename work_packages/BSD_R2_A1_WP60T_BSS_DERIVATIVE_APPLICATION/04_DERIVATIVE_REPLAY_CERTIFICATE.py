#!/usr/bin/env python3
"""Deterministic structural certificate for BSD-WP60T.

This certificate does not certify mathematical truth. It checks the finite
residual invariant calculation and that the protected dependency/claim
firewalls used by the WP60T proof are present in the repository candidate.
"""

from __future__ import annotations

import itertools
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WP = ROOT / "work_packages" / "BSD_R2_A1_WP60T_BSS_DERIVATIVE_APPLICATION"


def mat_mul(a, b):
    return (
        ((a[0] * b[0] + a[1] * b[2]) & 1,
         (a[0] * b[1] + a[1] * b[3]) & 1,
         (a[2] * b[0] + a[3] * b[2]) & 1,
         (a[2] * b[1] + a[3] * b[3]) & 1)
    )


def mat_vec(a, v):
    return ((a[0] * v[0] + a[1] * v[1]) & 1,
            (a[2] * v[0] + a[3] * v[1]) & 1)


def det(a):
    return (a[0] * a[3] - a[1] * a[2]) & 1


GL2 = [a for a in itertools.product((0, 1), repeat=4) if det(a) == 1]
assert len(GL2) == 6

I = (1, 0, 0, 1)
g = (0, 1, 1, 1)  # order-three element
assert mat_mul(mat_mul(g, g), g) == I
A3 = [I, g, mat_mul(g, g)]
assert len(set(A3)) == 3

nonzero = [(1, 0), (0, 1), (1, 1)]
assert not [v for v in nonzero if all(mat_vec(h, v) == v for h in GL2)]
assert not [v for v in nonzero if all(mat_vec(h, v) == v for h in A3)]

readme = (WP / "00_README.md").read_text()
theorem = (WP / "01_BSS_612_615_REPLAY_THEOREM.md").read_text()
source = (WP / "02_SOURCE_AND_DEPENDENCY_NOTE.md").read_text()
ledger = (WP / "03_CLAIM_LEDGER.yaml").read_text()

required = (
    "BSS_LITERAL_P2_SELECTED_HYPOTHESIS_6_1_AVAILABLE",
    "BSS_LITERAL_P2_SELECTED_HYPOTHESIS_6_7_AVAILABLE",
    "BSS_LITERAL_P2_SELECTED_HYPOTHESIS_6_11_AVAILABLE",
    "BSS_LITERAL_P2_SELECTED_DERIVATIVE_PRIME_SET_COMPATIBLE_WITH_WP60R",
    "BSS_LITERAL_P2_SELECTED_THEOREM_6_12_REPLAYED",
    "BSS_LITERAL_P2_SELECTED_COROLLARY_6_13_DERIVATIVE_AVAILABLE",
    "BSS_LITERAL_P2_SELECTED_COROLLARY_6_15_REPLAYED",
    "MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2",
)
for token in required:
    assert token in readme or token in theorem or token in ledger, token

for token in (
    "formal_higher_level_hypothesis_3_2_iii: false",
    "full_bss_hypothesis_4_7: false",
    "bss_hypothesis_4_7_iii: false",
    "infinite_bss_h3: false",
    "r5_lift: false",
    "r5_prim: false",
    "bsd_r2_a1: false",
    "mathcert_certification: false",
):
    assert token in ledger, token

for sha in (
    "245860ce3d7307a505e48b4165be0850327f996a",
    "b0854bb7770296b610b655753bc62b27365b27bb",
    "095b8eec0e7fe29d7e831661dfe199ec43fa0458",
):
    assert sha in readme + theorem + source + ledger, sha

wp60r = (
    ROOT
    / "work_packages"
    / "BSD_R2_A1_WP60R_BSS_THEOREM_REPLAY"
    / "02_BSS_520_52_REPLAY_THEOREM.md"
).read_text()
for token in (
    "BSS_LITERAL_P2_SELECTED_THEOREM_5_20_REPLAYED",
    "BSS_LITERAL_P2_SELECTED_THEOREM_5_2_REPLAYED",
):
    assert token in wp60r, token

wp60s = (
    ROOT
    / ".gcl"
    / "completions"
    / "BSD-WP60S"
    / "COMPLETION_RECEIPT.json"
).read_text()
assert "BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED" in wp60s
assert '"disposition": "CLOSED"' in wp60s

assert "Kato height-one-`(2)` Fitting divisibility" in theorem
assert "does not establish" in readme.lower()
assert "does not establish" in theorem.lower()

print("BSD-WP60T derivative replay certificate: PASS")
print("GL2(F2) order:", len(GL2))
print("A3 fixed nonzero residual vectors: 0")
print("candidate disposition: CLOSED")
print("next frontier: MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2")

#!/usr/bin/env python3
"""Consistency certificate for BSD-R2-A1 WP60R.

This does not certify the mathematics. It makes the theorem-replay dependency map,
provider anchor, repaired localization obligations, and preserved claim firewalls
machine-checkable.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PKG = ROOT / "work_packages" / "BSD_R2_A1_WP60R_BSS_THEOREM_REPLAY"

files = {
    "readme": (PKG / "00_README.md").read_text(),
    "localization": (PKG / "01_ALL_LEVEL_LOCALIZATION_CORE_GRAPH_THEOREM.md").read_text(),
    "replay": (PKG / "02_BSS_520_52_REPLAY_THEOREM.md").read_text(),
    "ledger": (PKG / "03_CLAIM_LEDGER.yaml").read_text(),
}

required = {
    "provider": "8c9b25fdd7dd63428a10f7d4439f5033ea890964",
    "common_span": "BSD-A1-WP60R-COMMON-SPAN-RES-001",
    "quotient_character": "BSD-A1-WP60R-QUOTIENT-CHAR-001B",
    "pairwise": "BSD-A1-WP60R-LEVELM-PAIRWISE-002",
    "injective_family": "BSD-A1-WP60R-INJECTIVE-FAMILY-003",
    "dual_kill": "BSD-A1-WP60R-DUAL-KILL-004",
    "core_graph": "BSD-A1-WP60R-ALL-LEVEL-CORE-GRAPH-005",
    "hyp42": "BSD-A1-WP60R-HYP42-006",
    "thm520": "BSD-A1-WP60R-BSS-520-007",
    "thm52": "BSD-A1-WP60R-BSS-52-008",
    "retired": "MISSING_LITERAL_P2_BSS_THEOREM_5_20_5_2_REPLAY_AFTER_REPLACEMENTS",
    "next": "MISSING_LITERAL_P2_BSS_THEOREM_5_25_INVERSE_LIMIT_REPLAY_AFTER_FINITE_LEVEL_REPLACEMENTS",
}

joined = "\n".join(files.values())
for label, token in required.items():
    assert token in joined, f"missing required WP60R token: {label}: {token}"

# The two adversarially repaired proof obligations must remain explicit.
for token in (
    "f_m o Res_m",
    "current residual primal space",
    "current residual dual dimension drops by one",
    "fixed class `c`",
    "odd three-term relation",
):
    assert token in files["localization"], f"missing repaired proof obligation: {token}"

# The protected predecessor that proves the global finite-level defect is real must
# remain part of the replay. WP60R must not erase it textually.
assert "formal_higher_level_hypothesis_3_2_iii: false" in files["ledger"]
assert "infinite_bss_h3: false" in files["ledger"]
assert "bss_theorem_5_25: false" in files["ledger"]
assert "bsd_r2_a1: false" in files["ledger"]
assert "mathcert_certification: false" in files["ledger"]

wp60m = (
    ROOT
    / "work_packages"
    / "BSD_R2_A1_WP60M_BSS_ALL_LEVEL_SELMER_HYP32III"
    / "01_ALL_LEVEL_SELMER_RESTRICTED_THEOREM.md"
).read_text()
for token in (
    "H^1(GL_2(Z/2^m),(Z/2^m)^2) ~= Z/2",
    "BSD-A1-WP60M-SELMER-RES-007",
    "BSS_LITERAL_P2_SELECTED_ALL_LEVEL_SELMER_RESTRICTED_COEFFICIENT_REDUCTION_AVAILABLE",
):
    assert token in wp60m, f"protected WP60M dependency missing: {token}"

wp60n = (
    ROOT
    / "work_packages"
    / "BSD_R2_A1_WP60N_COISOTROPIC_P2_CONNECTIVITY"
    / "01_COISOTROPIC_EXCHANGE_CONNECTIVITY_THEOREM.md"
).read_text()
assert "P2_BSS_COISOTROPIC_CORE_GRAPH_CONNECTED" in wp60n
assert "core rank is `chi(F)=1`" in wp60n

wp60g = (
    ROOT
    / "work_packages"
    / "BSD_R2_A1_WP60G_SELF_DUAL_P2_PAIRWISE_LOCALIZATION"
    / "01_SELF_DUAL_PAIRWISE_LOCALIZATION_THEOREM.md"
).read_text()
assert "one-primal" in wp60g.lower() or "primal" in wp60g.lower()
assert "dual" in wp60g.lower()
assert "j_B := f_B o Res_B" in wp60g

# Machine-check the elementary kernel-shrink invariant used in the theorem-5.20
# replacement: every successful new linear functional reduces kernel dimension.
# We exhaust all nonzero vectors and functionals over F2 up to dimension 6.
def dot(a: int, b: int) -> int:
    return (a & b).bit_count() & 1

for dim in range(1, 7):
    universe = list(range(1 << dim))
    for c in universe[1:]:
        witnesses = [f for f in universe[1:] if dot(f, c)]
        assert witnesses, (dim, c)
        for f in witnesses:
            ker = [v for v in universe if dot(f, v) == 0]
            assert len(ker) == 1 << (dim - 1)
            assert c not in ker

# Machine-check the finite F2 choice used in constrained dual killing. If the
# current primal space has dimension at least two, there are at least three
# nonzero vectors, so one can avoid the single forbidden vector c+d.
for dim in range(2, 7):
    nonzero = list(range(1, 1 << dim))
    for forbidden in range(1 << dim):
        choices = [p for p in nonzero if p != forbidden]
        assert choices, (dim, forbidden)

print("WP60R dependency replay certificate: PASS")

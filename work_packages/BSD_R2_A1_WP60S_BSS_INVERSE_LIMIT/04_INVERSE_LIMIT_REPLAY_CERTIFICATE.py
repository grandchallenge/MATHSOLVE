#!/usr/bin/env python3
"""Consistency certificate for BSD-R2-A1 WP60S.

This certificate checks the protected dependency map and claim firewalls. It is
not a substitute for mathematical review.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PKG = ROOT / "work_packages" / "BSD_R2_A1_WP60S_BSS_INVERSE_LIMIT"

files = {
    "readme": (PKG / "00_README.md").read_text(),
    "theorem": (PKG / "01_THEOREM_5_25_REPLAY.md").read_text(),
    "ledger": (PKG / "03_CLAIM_LEDGER.yaml").read_text(),
}
joined = "\n".join(files.values())

required = {
    "math_base": "245860ce3d7307a505e48b4165be0850327f996a",
    "provider": "770f95d1f8e7cfdd3facbd9242bf3c21c0e8b074",
    "nested": "BSD-A1-WP60S-NESTED-AUXILIARY-001",
    "stark_limit": "BSD-A1-WP60S-STARK-LIMIT-002",
    "ks_transition": "BSD-A1-WP60S-KS-TRANSITION-003",
    "regulator": "BSD-A1-WP60S-INTEGRAL-REGULATOR-004",
    "ideals": "BSD-A1-WP60S-KOLYVAGIN-IDEALS-005",
    "fitting": "BSD-A1-WP60S-INTEGRAL-FITTING-006",
    "theorem_525": "BSD-A1-WP60S-BSS-525-007",
    "disposition": "BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED",
    "retired": "MISSING_LITERAL_P2_BSS_THEOREM_5_25_INVERSE_LIMIT_REPLAY_AFTER_FINITE_LEVEL_REPLACEMENTS",
    "next": "MISSING_LITERAL_P2_BSS_THEOREM_6_12_COROLLARY_6_15_APPLICATION_REPLAY_WITHOUT_INFINITE_H3",
}
for label, token in required.items():
    assert token in joined, f"missing WP60S token: {label}: {token}"

for token in (
    "formal_higher_level_hypothesis_3_2_iii: false",
    "full_bss_hypothesis_4_7: false",
    "bss_hypothesis_4_7_iii: false",
    "infinite_bss_h3: false",
    "bss_theorem_6_12: false",
    "bss_corollary_6_15: false",
    "bsd_r2_a1: false",
    "mathcert_certification: false",
):
    assert token in files["ledger"], f"claim firewall missing: {token}"

wp60r = (
    ROOT
    / "work_packages"
    / "BSD_R2_A1_WP60R_BSS_THEOREM_REPLAY"
    / "03_CLAIM_LEDGER.yaml"
).read_text()
for token in (
    "BSS_LITERAL_P2_SELECTED_THEOREM_5_20_REPLAYED",
    "BSS_LITERAL_P2_SELECTED_THEOREM_5_2_REPLAYED",
    "formal_higher_level_hypothesis_3_2_iii: false",
    "infinite_bss_h3: false",
):
    assert token in wp60r, f"protected WP60R dependency missing: {token}"

# Elementary coherence check for the conjugated transition law. Represent
# transition maps by multiplication by odd/even residues in Z/2^m; conjugation
# by unit regulators preserves composition. This checks only the algebraic
# identity used in the written proof, not the arithmetic construction.
for m in range(1, 8):
    mod = 1 << m
    for a in range(mod):
        for b in range(mod):
            for u in range(1, mod, 2):
                # Every odd u is a unit modulo 2^m.
                inv = pow(u, -1, mod)
                lhs = (u * ((a * b) % mod) * inv) % mod
                rhs = ((u * a * inv) * (u * b * inv)) % mod
                assert lhs == rhs

print("WP60S inverse-limit replay certificate: PASS")

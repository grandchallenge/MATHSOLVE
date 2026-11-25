# PNP-ABOVE WP15 — source-native perfect-strategy and exact original-game-value replay

**Research classification:** source-native exact negative-value theorem for the WP14 reference verifier; not a new hard game, quantum/classical separation, P-versus-NP result, or independent public mathematical certification.

## Exact source lock

- Original upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, pinned Lean 4.35.0-rc3 / mathlib / MIPStarRE.
- Protected MATHSOLVE WP14 parent: `cb65e0f5386bbc42ffde5f9ea6943b8d9955e529`.
- First source-bearing WP15 candidate: `880f484b6b248a718a9f0a7093a275491ae3f2c6`.
- [WP15 source](WP15_PerfectClassicalNoGap.lean) Git blob `3e7d4905f6483acbbbafd173c735da17671dcc67`, SHA-256 `3694b66fb09bbeecf133f89cb419901e05ecf726a8ea81f308e6314e416fccb0`.
- Imported original source blobs: WP08 `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`; WP09 `3b64353814fd70a77810e51f2d04cbcfb4271def`; WP10 `860ad60fca4e99fcd836eec748fa419efd0701b2`; WP11 `088a731db4a7a1a21097a593958706df6b8a488b`; WP12 `c509e7e96383c7cb8199d7a9095b915a6d4db759`; WP13 `711e3e7938ea8c6682778252062adfc920ff4dbd`; WP14 `939f801c874e1e9acc6223a24eb055888466d51b`.
- Fail-closed reproducibility: [WP15_REPLAY.sh](WP15_REPLAY.sh) and [WP15_AXIOM_AUDIT.py](WP15_AXIOM_AUDIT.py); original pinned upstream `MIPRE.Foundations.Games`, not a copied game model.

## Source-backed execution evidence

GCL CONTROL CHAD-local source replay (candidate `880f484...`) capture `6dda372a6cfe4d6b9ddc25ffb89a6d24`, logs under `/tmp/gcl-pnp-wp15-source-880f484`:

```text
CHECKING_SOURCE_NATIVE_WP08
CHECKING_SOURCE_NATIVE_WP09
CHECKING_SOURCE_NATIVE_WP10
CHECKING_SOURCE_NATIVE_WP11
CHECKING_SOURCE_NATIVE_WP12
CHECKING_SOURCE_NATIVE_WP13
CHECKING_SOURCE_NATIVE_WP14
CHECKING_SOURCE_NATIVE_WP15
WP15_STANDARD_AXIOMS_ONLY_PASS count=16
WP15_SOURCE_NATIVE_PERFECT_CLASSICAL_NO_GAP_PASS
exit 0
```

The axiom auditor inspected **16 distinct** `PNPAbove.WP15` theorem declarations through Lean `#print axioms`. All depend only on subsets of standard `propext`, `Classical.choice`, and `Quot.sound`; no source `sorryAx`, custom axioms, or generated `native_decide` proof axioms. The source compiled against the exact original upstream formal game/strategies and previously protected WP08–WP14 modules. The original upstream `GameTransport` dependency was intentionally not imported (not built locally); WP15 directly constructs the required one-dimensional strategy in the *original* types and proves its value with the native Born rule. No amendment of original semantics occurred.

## Theorem disposition

For **all positive natural indices `n`** and **all answer budgets `T`, including zero**, the actual original `Verifier.syncGame` of the protected WP14 conditional verifier admits a deterministic one-dimensional fixed-empty-answer `SyncStrategy` with exact value 1. The original `syncValue`, tensor-product `quantumValue`, and commuting `commValue` all equal **1**, and quantum-minus-synchronous and commuting-minus-synchronous advantage equal **0**. The pointwise acceptance input is the actual protected WP14 native `Decider.Accepts` theorem; the strategy's value and global suprema are proved against the original formal definitions.

Thus WP14's full-depth conditional-linear structure has **no soundness or quantum/classical game-value gap**; its decider still accepts a constant winning reply. This is a verified **negative** result that closes the question of hardness *for the existing WP14 verifier*, **not** the wider PNP-ABOVE programme. A new source-native discriminating decider and nontrivial question distribution plus independently proved soundness/entangled value gap remain the next substantive obligation. Theorems about compression, succinct SAT transfer, and P-versus-NP remain unproved. The parent issue remains OPEN.

**Admission boundary:** this first replay and the receipt itself do not substitute for final receipt-bearing exact-head replay, required protected CI, exact-head protected merge, protected source readback, public evidence integration, or independent mathematical certification. Record those separately before claiming completed protected admission.

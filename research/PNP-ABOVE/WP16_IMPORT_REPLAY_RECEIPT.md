# PNP-ABOVE WP16 — original-CL diagonal support and decider-only no-gap replay

**Classification:** mathematically quantified source-native no-go / necessary-condition theorem for the protected WP14 sampler; **not** a new hard-game, compressor, P-versus-NP separation, or independent mathematical certification.

## Exact provenance

- Original upstream `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, pinned Lean 4.35.0-rc3 / Mathlib / MIPStarRE.
- Protected MATHSOLVE source parent: WP15 squash `64a6a47ad6a289ac1321a20cf4c396a909e1611a`.
- Proof-bearing audited WP16 candidate: `ffda221df907cf9e70d9febd4ed6616acce8b020`.
- [WP16 Lean source](WP16_DiagonalSupportObstruction.lean), Git blob `c576f71397ce86013e07fad08e480bcff294ef3e`, SHA-256 `504d53a218e4da5e82144fc28eeed4ce479fb20b9dcd75896973a8c92b3494ee`.
- Original imported protected Git blobs: WP08 `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`; WP09 `3b64353814fd70a77810e51f2d04cbcfb4271def`; WP10 `860ad60fca4e99fcd836eec748fa419efd0701b2`; WP11 `088a731db4a7a1a21097a593958706df6b8a488b`; WP12 `c509e7e96383c7cb8199d7a9095b915a6d4db759`; WP13 `711e3e7938ea8c6682778252062adfc920ff4dbd`; WP14 `939f801c874e1e9acc6223a24eb055888466d51b`; WP15 `3e7d4905f6483acbbbafd173c735da17671dcc67`.
- Reproducer: [WP16_REPLAY.sh](WP16_REPLAY.sh); [WP16_AXIOM_AUDIT.py](WP16_AXIOM_AUDIT.py).

## Source-native replay

GCL CONTROL CHAD-local source-bearing candidate replay capture `aa40bbfd5337492b9376e3a36f796ba1`, exact workspace `/tmp/gcl-pnp-wp16-source-ffda221`:

```text
CHECKING_SOURCE_NATIVE_WP08
CHECKING_SOURCE_NATIVE_WP09
CHECKING_SOURCE_NATIVE_WP10
CHECKING_SOURCE_NATIVE_WP11
CHECKING_SOURCE_NATIVE_WP12
CHECKING_SOURCE_NATIVE_WP13
CHECKING_SOURCE_NATIVE_WP14
CHECKING_SOURCE_NATIVE_WP15
CHECKING_SOURCE_NATIVE_WP16
WP16_STANDARD_AXIOMS_ONLY_PASS count=12
WP16_SOURCE_NATIVE_DIAGONAL_SUPPORT_NO_GAP_PASS
exit 0
```

The final log holds **12 distinct WP16 theorem declarations**, each audited via original Lean `#print axioms`; all axioms are subsets of standard `propext`, `Classical.choice`, `Quot.sound`, with no `sorryAx`, custom source axioms, or generated `native_decide` axioms. All nine original imported source-native modules elaborate under pinned original upstream. The proof-bearing candidate has clean committed source matching the locked blob and hash.

## Exact proved obstruction

The protected WP14 source has one shared nine-level CL presentation for both players. WP16 proves directly from the **actual source `MIPRE.CL.clDist` fiber-cardinality distribution** that every unequal question pair has probability **0** for every index, and this exact diagonal support survives **any decision-predicate-only replacement** that leaves the sampler unchanged.

For an arbitrary original `MIPRE.SynchronousGame` whose law vanishes off the diagonal, WP16 builds an explicit native **one-dimensional, question-dependent deterministic strategy**. If a choice of answer wins on each *positively sampled* diagonal question (no requirement for unsampled questions), its original Born-rule winning probability equals **1**. The original `syncValue`, `quantumValue`, `commValue` suprema therefore all equal **1**. Applying this to the exact WP14 distribution with an arbitrary replacement synchronous decision predicate proves a precise no-go: **changing only the decider cannot produce any quantum/synchronous gap while retaining per-supported-question feasible equal answers**. A positive gap would force the absence of every such global winning-answer selector.

This theorem is **conditional** on diagonal accepted answers and original synchrony. It does not show all diagonal games have equal quantum/classical values, nor that a particular new source executable decider exists or computes the arbitrary replacement predicate. The present verifier is known easy via WP15. A substantive game-value gap still requires a properly specified and source-executed decider, an appropriate question distribution, and an independent soundness/entangled-value proof.

Original MIP* compression, positive-parameter compressor, quantitative Theorem 12.1 reconciliation, Formal Conjectures source concordance, uniform succinct SAT-to-classical transfer, and P-versus-NP remain OPEN. No external mathematical certification is claimed. The parent MATHSOLVE #1136 remains OPEN.

**Admission status:** This proof-bearing replay is not the final receipt-bearing exact-head replay, required protected GitHub CI, source readback or public documentary admission. Record those independently before claiming protected completion.

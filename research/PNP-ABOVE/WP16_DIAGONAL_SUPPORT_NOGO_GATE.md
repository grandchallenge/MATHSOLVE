# PNP-ABOVE WP16 — source-native diagonal-question support and decider-only no-gap obstruction

**Scope:** a mathematically exact *necessary-condition / no-gap* result in the original MIPRE source game, not a hard-game construction, universal impossibility theorem, independent mathematical certification, quantum compression result, or P-versus-NP result. Parent [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136) remains OPEN.

## Source, definition and quantification

- Original external upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean 4.35.0-rc3, pinned mathlib / MIPStarRE.
- Protected parent: MATHSOLVE WP15 `64a6a47ad6a289ac1321a20cf4c396a909e1611a`. WP16 imports actual original WP08–WP15 sources and original `MIPRE.CL.clDist`, `MIPRE.SynchronousGame`, `MIPRE.SyncStrategy`, `MIPRE.syncValue`, `MIPRE.quantumValue` and `MIPRE.commValue` definitions.
- Source: [WP16_DiagonalSupportObstruction.lean](WP16_DiagonalSupportObstruction.lean). Reproducer: [WP16_REPLAY.sh](WP16_REPLAY.sh); standard-axiom auditor: [WP16_AXIOM_AUDIT.py](WP16_AXIOM_AUDIT.py). Exact candidate receipts in [WP16_IMPORT_REPLAY_RECEIPT.md](WP16_IMPORT_REPLAY_RECEIPT.md).

## Proof targets and result

**Source property, not assumption:** WP14's original conditional sampler uses the **same nine-level conditional `CLFun` for Alice and Bob**, which yields an exact uniform-seed distribution over the paired outputs `(L(z), L(z))`. WP16 proves, from the actual finite-fiber cardinality definition of upstream `MIPRE.CL.clDist`, that `conditionalSampler.dist n x y = 0` for **all** indices and **all unequal question pairs** `x != y`. It then proves the identical zero off-diagonal probability for the actual protected WP14 `Verifier.syncGame` and for *any* source-compatible replacement of only the decision predicate while the sampler remains fixed.

**General native-game lemma:** For any finite upstream `SynchronousGame` with zero mass on unequal questions, if a **question-dependent deterministic answer function** selects an accepted equal-answer pair at every sampled diagonal question, the native upstream `SyncStrategy` with Hilbert-space dimension **one** (matrix projectors that deterministically select that answer) wins with exact probability **1**. This is proved from the original Born-rule and original game distribution; it does not rely on numerical sample enumeration. Consequently the original `syncValue`, tensor-product `quantumValue`, and `commValue` are **all exactly 1**.

**Tight support condition:** A winning equal-answer pair is needed only at questions whose **diagonal sampling probability is nonzero**; unsampled questions need not accept anything. This avoids assuming all nine-bit outputs are reachable from WP14's conditional map. WP16 proves both the stronger convenient all-questions form and the precise on-support form.

**Decider-only obstruction:** WP16 builds an original `SynchronousGame` with **WP14's exact question distribution but an arbitrary replacement synchronous decision predicate**. Whenever each sampled diagonal question admits some chosen winning equal answer, the native game values remain identically 1. Equivalently, a positive quantum-versus-synchronous value gap in any such replacement would preclude **every** global winning-answer selector on the sampled diagonal support. Therefore **replacing only the old broadly accepting decider, while leaving its diagonal question distribution and pointwise diagonal feasibility intact, cannot produce the desired gap**.

## What is not proved / next work

This result does **not** establish that every possible decider on a diagonal sampler has equal game values, nor that all conditional CL samplers are diagonal. The no-gap theorem is conditional on a winning-answer selector for each positively sampled diagonal question, which is explicit in its statement. A credible positive-gap construction should supply a player-asymmetric/non-diagonal sampled question distribution, a source-native answer-sensitive decider, a quantified nonzero value/soundness gap and source runtime bounds. One may alternatively prove a more general structural no-gap theorem for diagonal-only games; that stronger theorem is not claimed here.

Positive-parameter compression, quantitative Theorem 12.1 source concordance, Formal Conjectures machine encoding alignment and the uniform succinct SAT-to-classical resource transfer remain OPEN. This no-go programme does not promote P-versus-NP, and no external theorem certification is asserted.

## Admission contract

Source-replay pinned to all prior protected modules must compile WP08–WP16 and audit **12 distinct** new WP16 theorem declarations with no nonstandard axioms. A successful source-native replay, protected source PR checks, exact-head guarded merge and protected readback are distinct gates. Public project evidence is a separate protected queue operation. Keep parent PNP issue open.

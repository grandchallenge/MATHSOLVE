# PNP-ABOVE WP13 — imported nine-level reference verifier and quantitative boundedness replay

**Classification:** source-imported Lean executable *reference/control* verifier; exact-head proof replayed but **not** independent mathematical certification, a hard-game theorem, positive-parameter quantum compression, or a P-versus-NP claim.

## Exact provenance

- Original upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean 4.35.0-rc3, pinned Mathlib/MIPStarRE.
- Protected MATHSOLVE parent: WP12 squash `fc83c349757fc01a1fe550432b49cc72afa5e715`.
- First source candidate: `a8f22c51392081e15302decad08852730472a915`.
- Exact audited committed candidate: `3bc58f47fe2d8499549bf1f61305ddaf206e7ddb`.
- New [Lean source](WP13_NineLevelSamplerVerifier.lean) Git blob `711e3e7938ea8c6682778252062adfc920ff4dbd`; SHA-256 `adcb18155ecda83f8d4e659dc0dc7318d9f59806392327551108e028a73d6d57`.
- Imported exact protected source Git blobs: WP08 `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`; WP09 `3b64353814fd70a77810e51f2d04cbcfb4271def`; WP10 `860ad60fca4e99fcd836eec748fa419efd0701b2`; WP11 `088a731db4a7a1a21097a593958706df6b8a488b`; WP12 `c509e7e96383c7cb8199d7a9095b915a6d4db759`.
- Reproducer: `bash research/PNP-ABOVE/WP13_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CHECKOUT WORK_DIR`.
- Executed CHAD-local GCL CONTROL exact-head capture `429bfe6614ac40b28fd6c485c21e7c70`, workspace `/tmp/gcl-pnp-wp13-head-3bc58f4/`, including `lock.txt`, imported source and `.olean`s, `WP13.log`, `AxiomAudit.log`, and `status.txt`.

## Observed source-bound test result

```text
CHECKING_SOURCE_NATIVE_WP08
CHECKING_SOURCE_NATIVE_WP09
CHECKING_SOURCE_NATIVE_WP10
CHECKING_SOURCE_NATIVE_WP11
CHECKING_SOURCE_NATIVE_WP12
CHECKING_SOURCE_NATIVE_WP13
WP13_STANDARD_AXIOMS_ONLY_PASS count=36
WP13_IMPORTED_BOUNDED_NINE_LEVEL_VERIFIER_PASS
exit 0
```

Every one of the **36 distinct** `PNPAbove.WP13` theorem declarations was audited through Lean's `#print axioms`; all dependencies are subsets of ordinary Lean `propext`, `Classical.choice`, `Quot.sound`. No `sorryAx`, declared source axiom, or generated `native_decide` axiom occurs. All six imports elaborate against exact source blobs. The replay harness rejects uncommitted WP13 source, changed upstream commits, and mismatch of protected antecedents. Local `bash -n`, Python compilation and mathematical Markdown source preflight were checked.

## Exact proved interface / cost and explicit anti-promotion

The source-native `CL.Sampler 9` has dimension 9 at every index, player CL functions equal to the identity on the full seed at stage one and eight empty stages, `CLFun.ExactlyOn Finset.univ`, all four native query-run obligations, and all-raw-tail source halting. A source-native read-only decision-tree cost induction yields `staticSteps samplerProg = 47` and `sampler9.TimeBoundAt n (47 * (esize n + 2)) 1`. The reused WP08 source decider satisfies `Decider.TimeBoundAt n 89 0`. Mechanical size guards lock sampler source-program size 723 and decider source-program size 145459.

The fully constructed `Verifier 9` uses WP12's typed acceptance theorem for the `accepts_length` side condition and proves `verifier9.IsBounded (verifier9.size + 10)`, with numeric lambda 145469 and all source clauses intact. It also proves synchrony and that the verifier accepts empty answers for **every positive index and every valid nine-bit question pair**, making it an intentionally **easy** reference game. Alice and Bob both receive the exact same uniform nine-bit seed, so it is nonconstant but has no demonstrated computational hardness. Eight levels are empty, not nine nontrivial conditional stages.

**Research boundary:** This does **not** prove a nontrivial nine-stage hard sampler, MIP* compression, a classical lower bound, a succinct uniform SAT-to-classical-resource reduction, or P-versus-NP. The quantitative exponent is extremely loose and does not establish practical efficiency. A nontrivial full-depth source-native CL family with genuine hardness evidence remains open, along with source Theorem 12.1 quantitative discrepancy and the original Formal Conjectures encoding concordance. No parent issue closure or independent certification is justified.

**Protected status:** This candidate replay is distinct from final receipt-commit exact-head replay and protected PR admission. Verify both on completion before reporting protected closure.

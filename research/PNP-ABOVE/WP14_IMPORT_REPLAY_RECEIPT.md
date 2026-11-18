# PNP-ABOVE WP14 — full-depth conditional sampler/verifier source replay

**Classification:** Lean source-native, bounded **reference** verifier and conditional CL family; **not** a hard-game theorem, independent mathematical certification, quantum compression, or proof of P versus NP.

## Pinned sources and exact candidates

- External original `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`; Lean 4.35.0-rc3 and pinned Mathlib/MIPStarRE.
- MATHSOLVE protected source parent: WP13 `70a890963c96e06f4d950ec566b4147794afd93f`.
- WP14 audited proof-bearing candidate: `aa5330e5b8c67f969fe7ea89f99f98213b65e824`. The [Lean source](WP14_ConditionalNineStageSampler.lean) is Git blob `939f801c874e1e9acc6223a24eb055888466d51b`, SHA-256 `9ff2aadbbfc971e7f1f607cb0da1cbb90d18b4ab7d05cc3892f04a6b263e2e08`.
- Imported MATHSOLVE source Git blobs: WP08 `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`, WP09 `3b64353814fd70a77810e51f2d04cbcfb4271def`, WP10 `860ad60fca4e99fcd836eec748fa419efd0701b2`, WP11 `088a731db4a7a1a21097a593958706df6b8a488b`, WP12 `c509e7e96383c7cb8199d7a9095b915a6d4db759`, WP13 `711e3e7938ea8c6682778252062adfc920ff4dbd`.
- Fail-closed source and candidate-bounded harness: [WP14_REPLAY.sh](WP14_REPLAY.sh), [36-theorem axiom auditor](WP14_AXIOM_AUDIT.py).

## Source replay and recovery

- Exact candidate run for `aa5330e5...` compiled original WP08–WP14 source modules under pinned upstream; successful WP14 native Lean compile log with exact 52 syntactic cost, 16213 sampler source program size and 145469 full-verifier lambda. CHAD-local GCL CONTROL execution capture: `a9b0597daad545b69d70dc04b2d1d1b9`. The original single-call invocation was interrupted **after** WP14 compilation and **before** the axiom audit returned due the remote execution window, not due a Lean proof diagnostic.
- A separately resumed axiom process initially lacked inherited `LEAN_PATH` and returned an import-path failure, not a theorem failure. It was restarted in the exact pinned upstream with the correct import path, and the audit concluded **exit 0**, `WP14_STANDARD_AXIOMS_ONLY_PASS count=36`, all 36 `#print axioms` reports present; all dependencies are subsets of `propext`, `Classical.choice`, `Quot.sound`. The corrected environment and same candidate were verified in CHAD-local capture `7efad37cce624738aa29a645715ada83`; no source changes were made to fix that environment error.
- The final receipt-bearing candidate replay and protected PR checks will have a separate exact-head execution readback; this receipt must not be treated as independent mathematical certification. The code and source hashes, rather than a reported result, bind verification to the exact candidate.

## Proven result and explicit scientific boundary

1. **Genuine conditional CL structure:** all nine stages have distinct nonempty singleton factors partitioning `Fin 9`; first-bit value determines eight subsequent stage maps, and the two second-stage maps are source-proved unequal. This is no longer WP13's eight-empty-stage padding.
2. **Executable source program:** four native sampler query cases proved for every canonical nine-bit vector, every legal stage and both players, not inferred from finite examples. Source scoping, raw-input termination and source `Cost.Eval` run witnesses are proved.
3. **Exact source time:** a separately proved `cons`/`elim` cost induction gives `conditionalSampler.TimeBoundAt n (52 * (esize n + 2)) 1` for every raw query tail, with source program size 16213. The full native `conditionalVerifier : Verifier 9` proves original `IsBounded (conditionalVerifier.size + 10)`, lambda **145469**, and synchrony, using protected WP12 and WP13 exact decider results.
4. **No hard game:** despite nontrivial CL conditioning, `conditionalVerifier_accepts_empty` proves empty answers win at every positive index and any valid question pair. A nontrivial game-value/soundness gap, positive-parameter quantum compression, uniform succinct SAT-to-classical transfer, and P-vs-NP separation all remain **unproved**. Neither PNP-001 nor the parent MATHSOLVE #1136 is closed by this result.

**Protected status:** WP14 protected-source admission and documentary projection are separate governance operations; record their final exact protected SHAs and CI statuses independently before claiming completed admission.

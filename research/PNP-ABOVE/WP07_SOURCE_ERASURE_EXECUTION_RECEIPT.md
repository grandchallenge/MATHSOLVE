# PNP-ABOVE WP07 — Imported Lean erasure/adequacy proofs and execution receipts

**Disposition:** two finite source-faithful, Lean-checked compiler-interface theorems. No runtime execution of a concrete positive-parameter quantum compressor and no P-versus-NP separation.

**Research parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136). **Upstream source lock:** [vidick/MIPRE-formalization at commit 5926bdff5db621f44682a101007ef2fe3ae8d970](https://github.com/vidick/MIPRE-formalization/tree/5926bdff5db621f44682a101007ef2fe3ae8d970). Imported modules: `MIPRE.Background.Introspection.DecisionCompiler` and `MIPRE.Introspection.SourceDescriptionCompiler`.

## 1. Source-erasure theorem replay — the already merged WP06 candidate

The [WP06 source file](WP06_ParameterErasureCandidate.lean), previously staged as an *unexecuted candidate* and admitted in [PR #1170](https://github.com/grandchallenge/MATHSOLVE/pull/1170), has now been **actually elaborated by Lean** from the exact protected-main bytes.

- Git blob SHA-1: `eaaddbcfbc02fbdcd4ddfda1e275c2822f4906b2`.
- Local file SHA-256: `0e9781f8a0379dce6da08cd5621345e6a4b6c147b2ae116d3d646b986477c743`.
- Toolchain: Lean 4.35.0-rc3, pinned Mathlib and MIPStarRE lock, `lake env lean /tmp/gcl-mipre-wp06-erasure.lean` in the pinned upstream checkout.
- Exit code **0**, with one deprecation warning (`if_neg`) and **no errors**.
- Local run was started via GCL CONTROL OS execution capture `a7f0d7fdc8294c89a473433ac0b1ce7c`, and its persisted exit/log subsequently read back with capture `1aca1f72079448e7a3f1cea3431e9a09`. Both are **local OS evidence, not independent Referee certification**.

The kernel accepts the actual imported-source lemmas:

1. **Zero-parameter source erasure:** for every fixed compiler setting and all programs `S,D`, `compute c U ((S,D),0) = zeroProg`.
2. **Source-independent zero acceptance:** acceptance at parameter zero iff `x=[]`, `y=[]`, and both answers have lengths at most 2.
3. **Overbudget clamp:** if both `esize S > lam` and `esize D > lam`, the clamp maps the descriptions to `((Prog.nil,Prog.nil),lam)`.
4. **Overbudget compiler collision:** any two pairs of source programs each exceeding the same `lam` on both components produce **identical compiled decider programs** for fixed `c,U,lam`.

This upgrades only the proof-status label of the source candidate, not the original PR's immutable historical statement about its execution status.

## 2. Source-size adequacy theorem — new WP07 Lean proof

The new [WP07_ClampAdequacy.lean](WP07_ClampAdequacy.lean) imports the **actual** MIPRE definitions and proves:

- If `esize S ≤ lam` and `esize D ≤ lam`, `SourceDescriptionCompiler.clamp ((S,D),lam) = ((S,D),lam)`.
- If additionally `lam≠0`, the introspection decider compiler yields `zeroWrap (positiveCompiler c U ((S,D),lam))` without source-description replacement.
- The symbolic constructive **description-size** budget `lam = max (esize S) (esize D) + 1` suffices for this preservation.

Source code identity: Git blob SHA-1 `6e9fa5a93b67335b5f9f15a5d4c269b4b9bc004b`, SHA-256 `7ab7bfa642717c343ba2c35e75fff2d16fd6e3a894f7b1d9f19f453bafa85b75`, fetched from the GitHub topic branch and executed with `lake env lean /tmp/gcl-mipre-wp07-adequacy.lean` against the pinned upstream build. The proof run returned **exit code 0**, one nonfatal `if_neg` deprecation warning and no Lean errors.

- GCL CONTROL launch capture `cf848229d5aa4505a3c204aa19c16c43`.
- Saved log/exit readback capture `d085b7e2490947779dda161ae1d01ba5`.
- No claim of independent proof checking beyond Lean execution and the local captured run.

## 3. Consequence for the attempted SAT transfer

**A precise counterexample to naive compiler injectivity:** When the compiler parameter is insufficient to hold distinct source descriptions, the decider compilation can erase source differences *before* they reach the positive-parameter kernel. This can invalidate SAT-to-compiled-decider reductions that require distinguishing those source instances while retaining only the resulting decider program as information.

**A precise sufficient hygiene condition:** Supply a positive source-description budget at least as large as both encoded source-program descriptions. The formula `max(esize S, esize D)+1` satisfies the **description-size** condition. It is **not** in itself a proof of the full `lambda`-bounded-verifier condition, nor does it compute the compression threshold `C0`, enforce the input level normal form, establish game-level acceptance equivalence, or provide polynomial overhead for a SAT reduction.

The adequacy result says inputs are passed through the clamp unchanged. It does **not** say the resulting compressed decider is injective on programs or on SAT instances. The zero-parameter result is a special degenerate branch, not a purported implementation of general quantum compression.

## 4. Next obligations

1. Construct a source-faithful **nine-level sampler and decider pair** as native MIPRE `Prog` with exact metadata sizes, indices, input encoding, malformed-input semantics, and timed execution traces.
2. Establish the relevant **uniform polynomial overhead** measured in the SAT input length, including source-description budget, universal-machine simulation, compiler program size, and game-description output.
3. Execute `DecisionCompiler.compute` for a **concrete positive parameter** and effective clocked universal machine; capture the produced source program and compare its actual behavior against the paper's introspection stage.
4. Extend to source-faithful answer reduction and repetition and reconcile the formalization's stage levels with the source theorem. A classical lower bound cannot be inferred from Schmidt-rank requirements alone.

**Status:** two bounded compiler-interface proof obligations verified; full Figure 15 quantum compression, succinct classical strategy lower bound and general SAT transfer remain open.

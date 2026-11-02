# PNP-ABOVE WP06 — Imported compiler branch: verified zero-parameter control

**Source lock:** [vidick/MIPRE-formalization at 5926bdff5db621f44682a101007ef2fe3ae8d970](https://github.com/vidick/MIPRE-formalization/tree/5926bdff5db621f44682a101007ef2fe3ae8d970).  
**Working parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136).  
**Evidence status:** *six Lean-verified zero-parameter propositions*, followed by *two positive-parameter test obligations not yet replayed*. **No executable positive-parameter compressor or classical complexity separation.**

## Verified source-imported baseline

The previously staged [WP05_SourceCompilerBranch.lean](WP05_SourceCompilerBranch.lean) was read back from protected `main` (Git blob `ca6f9912e876a6ff73a9f8953d1af24bd53f08a8`; SHA-256 `d7f46f620fadab1d64a839a040282e5fc5ef8120e76a48d63df69be8aecb977b`) and elaborated using `lake env lean` in the pinned upstream checkout, Lean 4.35.0-rc3, with real upstream `DecisionCompiler` imports.

**Result:** exit code 0, no Lean errors; CHAD execution capture `GCL_CONTROL_BASH_RESULT/1` ID `bd3f6e7a05be4525a5e25ec27583ce0e`, empty successful stdout.

The first revision of [WP06_ImportedCompilerBranch.lean](WP06_ImportedCompilerBranch.lean), **before the later positive-parameter declarations were appended**, was fetched directly from its GitHub topic branch and read back as Git blob `ba52b49ffa6b9e8ff2d0530320fa0200db1f9126` (SHA-256 `ddeef23b9513740e80b582885e36956b76c990b5c503397e86060d946248f98b`). The exact file passed imported Lean 4.35.0-rc3 checking: exit code 0, no compiler output; CHAD execution capture ID `901fc103003d42829dbab7dc98d304d6`. Its six propositions are:

1. **Program selection:** for arbitrary `c,U,S,D`, `compute c U ((S,D),0) = zeroProg`.
2. **Native well-scopedness:** the resulting program satisfies `Prog.WellScoped 1`.
3. **Terminating decider:** for all indices and data, an upstream `Runs` witness exists with output `encode (zeroTest d)`.
4. **Exact acceptance characterization:** with parameter zero, acceptance is equivalent to empty Alice/Bob questions and answer lengths at most 2.
5. **Positive acceptance control:** the all-empty tuple of questions and answers is accepted.
6. **Negative acceptance control:** a nonempty first question is rejected.

All statements use the imported upstream `MIPRE.Cost.Prog`, `DecisionCompiler` and `Eval` infrastructure; there are no local copies of these core definitions. The replays verify **source theorems specialized to the degenerate zero-parameter branch**, not the main compression construction.

## Positive-parameter source interface (pending Lean replay)

After the successful six-proof replay, two additional source-level propositions were appended to the same WP06 file:

- For `lam ≠ 0`, the compiled program has shape `zeroWrap (positiveCompiler c U (SourceDescriptionCompiler.clamp ((S,D),lam)))`.
- For `lam ≥ 1` and `n ≥ 1`, a terminating `Runs` witness exists whose result is specified by the imported upstream `DecisionKernel` via `positive_runs`.

The imported upstream file already provides `compute_apply` and `positive_runs` with those interfaces. **However, the updated WP06 file (blob `b7e40aaaeec6d8555e73b3c0286c19cec31acc10`) has not itself completed a successful exact-head Lean replay**: the remote command interface intermittently rejected execution attempts after the code update. The two additions remain **candidate** theorem applications, not accepted GCL-verified elaborations. They should be replayed and corrected before proof promotion.

## Mathematical interpretation

A **zero** parameter is useful as a regression test: it deterministically selects a small fallback verifier and makes its acceptance set explicit. It is **not** a positive compression construction and cannot be substituted for the source's eventually positive universal parameter.

The actual project obligation is to supply a concrete bounded input `S,D`, source-correct metadata and justified `lam ≥ 1`, obtain an instantiated `ClockedUniversalMachine`, run `DecisionCompiler.compute`, evaluate the *generated* program and check its behavior against the introspection contract. Then the answer-reduction and repetition stages remain.

**Claim boundary:** no new P-versus-NP result, new unconditional classical lower bound, SAT-to-entangled-strategy transfer, executed positive-parameter compressor, or mathematical certification. Protected integration and CI are not substitutes for direct source elaboration or specialist proof review.

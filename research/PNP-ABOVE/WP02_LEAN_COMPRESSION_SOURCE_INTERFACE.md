# PNP-ABOVE-WP02 — pinning the formalized compression pipeline as an implementation interface

**Status:** external-source code-interface audit; no GCL Lean replay, numerical instantiation, source-to-paper equivalence proof, extracted executable compressor, or mathematical certification claimed.  
**Parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136); predecessor [WP01 code and transfer proof](https://github.com/grandchallenge/MATHSOLVE/pull/1152).

## New source candidate and exact identity

**External repository:** [vidick/MIPRE-formalization](https://github.com/vidick/MIPRE-formalization), main commit **5926bdff5db621f44682a101007ef2fe3ae8d970** (read-only source audit on 1 November 2026). Its README states that the Lean 4 project has a proved theorem reducing halting to quantum nonlocal-game value, and a full MIP* = RE formalization. These are statements **of the external repository and its linked Palomar record**. This GCL WP has not built or independently replayed the upstream Lean library.

The upstream tree pins Mathlib at **v4.35.0-rc3** and a separate [MIPStarRE formalization](https://github.com/LionSR/MIPStarRE) at commit **5fc363bc8b77b1a6bbdaaeea634f1b0f3ff0ad79** (see the upstream lakefile.toml). The repository's source is Apache 2.0 per file headers; use proper attribution and source locks in any derived code.

## Four specifically located interfaces

| Function / theorem | Exact file at pinned commit | Source blob SHA-1 | What is established by source inspection |
| --- | --- | --- | --- |
| Main compression object | MIPRE/MainTheorem.lean | 85cb652fa0672c5a5660c5fddb03ab0d927953f9 | Defines noncomputable MIPRE.gapCompression using GapCompression.ofAnswerReduction |
| Pipeline assembly | MIPRE/Background/Pipeline.lean | 1d2a27c80def9f1ee2055e100f18ad57de7d91ba | GapCompression.ofPipeline combines Introspection.seven, AnswerReduction 5, repetition 7 |
| Introspection | MIPRE/Background/Introspection/Compiler.lean | 901b228a2327ea790fba017dd59ed9ec13789545 | sevenConstant and sevenC selected with Classical.choose; soundness and compiler contracts |
| Answer reduction | MIPRE/Background/AnswerReduction/Instance.lean | cef0131b2226ab7133551304df77990b7f2d9e3e | Classical PCP interface, arVerifier and associated parameter proofs |
| Repetition | MIPRE/Background/Repetition/Verifier.lean | bfac7d7e60fff950b01fe1a455fceefd792c18a9 | repSampler, repDecider, quantified repeated verifier proof |
| Core parameter algebra | MIPRE/Foundations/Pipeline/Compress.lean | 37023b8d945c57b342bb8b5cf75339beb58b67d8 | sigmaFun, sigma, mu/beta/tau/C0 construction, type-level pipeline |
| Executable introspection kernel compiler | MIPRE/Background/Introspection/DecisionCompiler.lean | dc0ab09a9426ce2308d0def85f6368845c64687f | DecisionCompiler.compute has type PolyTimeFun Metadata Prog, with source-clamp and zero-index behavior |

Use the repo paths appended to the commit URL above for immutable access. The three-stage assembly is real in the codebase, not a hypothetical future repository.

## Constructive versus noncomputable is a material distinction

The Lean main theorem explicitly declares:

- MIPRE.gapCompression as a **noncomputable def**;
- GapCompression.ofAnswerReduction as a **noncomputable def**;
- Introspection.seven and constants sevenConstant/sevenC in a **noncomputable section**, with existential witnesses selected by .choose;
- DecisionCompiler.compute as a named PolyTimeFun from metadata to a program encoding.

Thus the upstream formalization can **prove existence, correctness and computational behavior** without automatically yielding a directly evaluable small concrete compressed game or numerical constants. A verified mathematical existence theorem is not itself a runnable compiler binary. The nested computable code objects are nevertheless a considerably stronger implementation starting point than reimplementing a 250-page theorem solely from prose.

**Input-language reconciliation needed:** the source paper's October-2026 Theorem 12.1 is stated for nine-level input/output normal form and constructs intermediate levels 5 -> 7 -> 9. The Lean assembly uses parameter types Introspection 7, AnswerReduction 5, and Repetition 7. These types denote stage contracts and cannot be equated directly to the source paper's output-level labels. A definition-by-definition correspondence (sampler semantics, types, source encoding, promises, error constants, output-level indexing, value model) must be proved or falsified before invoking the Lean result as a literal implementation of Figure 15.

The Lean source appears to use **alternative dominating polynomial constructions** for some parameters rather than the literal displayed arithmetic of the paper's equations (185)–(190). This is mathematically allowed under the appropriate proof of domination, but exact byte-for-byte or formula-for-formula correspondence must not be claimed.

## Reconciliation with the published theorem discrepancy

The source v4 statement of Theorem 12.1 has

$$
\mathcal E(V_n^{\mathrm{compr}},1/2)
\geq\max\left\{\frac12\mathcal E(V_{2^n},1/2),\,2^{(2^n)^\lambda-1}\right\}
$$

while its Table 2 and displayed final proof chain give only one half of the entire maximum. The existing WP01 source erratum retains the conservative bound. The upstream Lean construction should be checked for the **exact resource measure and quantitative inequality** it proves, rather than being presumed to resolve the factor-of-two discrepancy. In particular, a formalization of the language-class equality or game-value gap does not by itself certify the numerical Schmidt-rank inequality.

## Exact constructive work proposed (not falsely marked complete)

1. **Source checkout and replay:** pin SHA 5926bd..., pin the upstream Lean toolchain and dependencies, run its declared build/check procedures in an isolated governed computational lane, and record build and comparator evidence. No run is asserted here.
2. **Extract one finite program:** choose the input verifier from the protected nine-level identity emulator; encode it in the Lean project's Prog syntax with explicit serializer and timeout. Verify the program computes the intended six-input sampler and decider, including malformed inputs, using executable positive/negative tests.
3. **Instantiate a computable stage:** test DecisionCompiler.compute on that exact source program and lam, with any constructive constants explicitly evidenced, not inserted arbitrarily for the sake of execution. Store the produced code and an execution trace. Mark missing computational witnesses precisely.
4. **Compare semantics:** inspect the produced verifier's question sampler and decider against Section 8 of the v4 source. The Figure 15 composition may only be declared source-faithful after all three stage contracts, error terms, and level shifts are reconciled.
5. **Classical interface:** retain the WP01 explicit-table SAT strategy compiler as a test oracle for classical outcomes on small games. Do not substitute its outputs for entangled strategies or equate theorem-level verification with a classical SAT proof.

**Next executable target:** the original repository's Program/Metadata representation and DecisionCompiler.compute, with a minimal finite input and exact source commit lock. GCL has not executed it yet.

**Claim boundary:** no new P/NP proof, no unrestricted lower bound, no source-author endorsement, no built formal proof, no executable full compressor, and no change to PNP-001 machine/encoding concordance status.

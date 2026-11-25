# PNP-ABOVE WP14 — fully conditional nine-stage source-native reference verifier

**Parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136), PNP-ABOVE. **Grade:** source-imported Lean theorem; not independent mathematical certification, hardness, compression, or a P-versus-NP result.

## Source lock and scope

- Upstream `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970` (Lean 4.35.0-rc3 and pinned mathlib).
- Protected source parent `MATHSOLVE@70a890963c96e06f4d950ec566b4147794afd93f` (WP13); [WP14 Lean](WP14_ConditionalNineStageSampler.lean), [source-native replay](WP14_REPLAY.sh), [axiom auditor](WP14_AXIOM_AUDIT.py) and [exact-head receipt](WP14_IMPORT_REPLAY_RECEIPT.md).

## What is actually proved

The source-imported `CLFun` has **nine nonempty disjoint singleton register factors**, one at each original stage, which partition all nine coordinates (`CLFun.ExactlyOn Finset.univ`). Stage one reads coordinate 0. At stages two through nine the stage linear map equals projection onto the stage's own coordinate if the *first prefix bit is one*, and equals zero otherwise. Lean proves **these two stage maps are unequal**, rather than merely reporting different finite runs. Both players share the same conditional CL distribution.

One **actual, closed `MIPRE.Cost.Prog`** implements all four original `CL.Sampler.Query` cases: dimension, stage marginals, prefix-conditioned linear maps, and factor-space indicator vectors. Its binary dispatch is compiled from source `Prog.elim` trees and its conditional bit lists are produced using source `Prog.cons`, rather than a nonexecutable mathematical oracle. The proof establishes the full **quantified** query contracts for arbitrary canonical nine-bit inputs, all players, and all legal stages, and proves **every malformed raw input halts**. The source-level `Cost.Eval` runs are derived via the previously admitted WP12 structural-evaluator agreement, not a surrogate cost model. The original `Sampler 9` structure is fully instantiated.

A **new source-native runtime induction** includes both branch-selection (`elim`) and output construction (`cons`) costs. Each source `cons` adds both child costs; each source `elim` charges the chosen branch only. The exact finite syntactic coefficient is **52**, and the original native source has the genuinely uniform raw-tail bound

```text
conditionalSampler.TimeBoundAt n (52 * (esize n + 2)) 1
```

for every natural index and all raw query tails. The executable program description size is **16213** in original upstream encoding. Reusing the admitted WP11 nine-bit decider's exact `TimeBoundAt n 89 0`, the source builds `conditionalVerifier : MIPRE.Verifier 9` and proves the full original `IsBounded (conditionalVerifier.size + 10)` theorem, including dimension, native runtime bounds at all indices `n ≥ 2`, and source-program description length. The explicit lambda remains **145469** because the much larger original WP08 decider description dominates. It is a mathematically valid but extremely loose exponent, not practical runtime performance.

The verifier is also source-proved synchronous. However, its decider still **accepts empty answers for every positive index and every valid nine-bit question pair**. Thus this is a **conditional-source verifier control**, not a computationally hard game; conditional stage structure **does not imply** a positive MIP* soundness gap or any classical lower bound. The source theorem makes that limitation explicit. This closes the full-depth, bounded, native sampler **interface** obligation, but not the genuine hardness/gap obligation.

## Outstanding science and admission constraints

A genuinely hard-game construction needs a *discriminating* source-native decider and formally proved value/soundness gap, not just a conditional CL family. Additional open obligations are a positive-parameter compressor, the uniform succinct SAT-to-classical resource transfer, Theorem 12.1 quantitative source reconciliation, and Formal Conjectures machine/encoding concordance. Parent PNP-001 remains open. Internal role-scoped source review may admit the bounded reference evidence, but it is not public independent proof certification.

The replay must compile pinned WP08 through WP14 at the exact committed candidate, with 36 new theorem declarations audited for absence of `sorryAx`, custom axioms, and `native_decide` generated axioms. Source, reviewer receipt, required CI, exact-head protection, and protected-main readback must all be preserved before WP14 admission is claimed.

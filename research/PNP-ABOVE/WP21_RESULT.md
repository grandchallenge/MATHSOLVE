# PNP-ABOVE WP21 — source-native bounded answer-sensitive nine-level verifier

**Disposition:** `WP21_NATIVE_BOUNDED_ANSWER_SENSITIVE_VERIFIER_PROVED__GAME_VALUE_BRIDGE_OPEN`.

**Source lock:** original protected predecessor MATHSOLVE `ab30e727a6bf6762432d4b95546908f8c4d3711a` (WP20); upstream `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`; Lean 4.35.0-rc3. Research MATHSOLVE #1136 and PNP-001 #162 remain OPEN.

## Mathematical and original-source results

WP20's game had an original `Sampler 9` but only a mathematical acceptance predicate. WP21 now builds an original imported `MIPRE.Cost.Prog` answer-sensitive **decider** and genuine `MIPRE.Verifier 9` record combining it with the WP20 cyclic sampler.

The support-masked mathematical CHSH rule is

    (!x[8] && !y[0]) && (a XOR b = (x[0] && y[8])).

The masks hold for every original cyclic sampler source pair. Lean proves that this rule agrees there with WP20's mathematical predicate for every seed and Boolean answer pair, and proves its global synchrony including off-support diagonal pairs. The mathematical theorem does not automatically prove that the native executable decider has those properties on all typed inputs.

The executable `Cost.Prog` decider parses the original `encode (n,x,y,a,b)` input, rejects zero indices, validates two canonical length-nine questions and two canonical length-one answers, reads six significant input bits and executes a bounded finite decision tree.

Ten new source-native Lean modules prove:

- Original `Prog.WellScoped 1`, original `Decider` packaging, loop freedom, total source `Cost.Eval` execution on every raw input and canonical Boolean result.
- For every typed input, native `Decider.Accepts` if and only if the independently defined structurally recursive source evaluator returns canonical true.
- For every native accepted tuple, both questions have exactly the sampler's dimension nine.
- A real original `Verifier 9` with the original cyclic sampler and answer-sensitive decider, including the original normal-form length side condition.
- A generic source `Cost.Eval` time and intermediate-value bound for inspect/copy/let syntax with constant and environment size ceilings, applied to the new decider.
- Original native decider `TimeBoundAt` with degree one and coefficient `146 * (esize n + 6)`; for `n ≥ 2` this is bounded by `n^12` at degree 12.
- **Full original `Verifier.IsBounded (cyclicVerifier.size + 12)`**, covering sampler runtime, decider runtime, dimension and programme size.

Original decider source-program size is 149,391 encoded nodes, maximal instruction count 146 and maximal literal size 3. This is a finite, non-optimized construction rather than an efficiency claim.

## Finite checks, replay and epistemic boundaries

`WP21_Checks.lean` executes **2,048 exact source-evaluator tests**: all 512 original seed questions and four Boolean answer pairs, with additional rejecting tests for zero index, invalid question and answer lengths, and mismatched diagonal answers. All passed. These checks are finite evidence, not a universal executable parity-equivalence theorem.

`WP21_SOURCE_LOCK.json` records Git blob SHA-1, SHA-256 and complete public theorem inventories for ten Lean modules. The replay script recompiles the inherited original WP08–WP20 files and all ten WP21 modules with source locks and kernel axiom reports. The new 35 theorem declarations were checked against original imported Lean, using only standard `propext`, `Classical.choice`, and `Quot.sound` or no axioms.

## Remaining substantive obligations

1. Prove universally that native `Decider.Accepts` equals the support-masked mathematical parity predicate for all canonical typed questions and answers. Include raw/malformed and non-singleton answer rejection; finite source checks are insufficient.
2. Deduce original `Verifier.IsSynchronousAt n` for every index from the native executable predicate.
3. Prove original `Verifier.game n T` value correspondence with WP20 for `T ≥ 1`, accounting rigorously for source's empty and multi-bit answer strings and both classical and quantum strategy classes.
4. Only then transport WP20's exact classical optimum 3/4 and quantum witness 81/100 to the original bounded native verifier. Positive-parameter compression, Theorem 12.1 constants, full introspection, any uniform succinct SAT-to-classical-cost implication and separate PNP-001 NP/model endpoint bridges all remain open.

**Claim boundary:** bounded original-source verifier established; original-native **hard-game gap not yet established**. No claim of `P≠NP`, `P=NP`, positive-parameter compressor or independent MATHCERT certification.

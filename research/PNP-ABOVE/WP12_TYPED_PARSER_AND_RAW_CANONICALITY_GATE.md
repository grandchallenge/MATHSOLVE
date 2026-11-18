# PNP-ABOVE WP12 — exact typed parser theorem and raw-canonicality counterexample

**Research parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136); parent PNP-001 remains open. **Classification:** source-imported Lean theorem and negative source-specification witness; not independent mathematical certification, a complete nine-level verifier, quantum compression or any P-versus-NP result.

## Source lock

- Protected MATHSOLVE ancestor: `ef12175a28be8d3bcff1a2ce1dfde44dea30b5de`, the admitted WP11 source.
- Upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean 4.35.0-rc3 and pinned dependencies.
- [WP12_TypedParserAndRawCounterexample.lean](WP12_TypedParserAndRawCounterexample.lean) imports **original WP08–WP11** and the upstream source `MIPRE.Cost.Eval` and `Decider.Accepts` semantics. [Fail-closed replay](WP12_REPLAY.sh) and [axiom auditor](WP12_AXIOM_AUDIT.py) are source-locked; final exact-head execution is recorded separately in [WP12 receipt](WP12_IMPORT_REPLAY_RECEIPT.md).

## Positive result: all typed inputs, not just nine-bit finite tests

For every natural-number index `n` and arbitrary bitstrings `x`, `y`, `a`, `b`, the actual imported native identity decider satisfies

```text
identityDecider.Accepts n x y a b
  ↔ n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧ a = [] ∧ b = []
```

This is the **exact intended typed-input parser specification**. Neither equality of the two questions nor an exponential enumeration assumption appears. The proof first relates all loop-free source programs to a structurally recursive value evaluator through the *imported* `Eval` relation and its determinism. A separate induction proves that WP08's `checkBits` recognizes canonical encoded lists of exactly the requested length, including both possible bit constructors. The raw structure of WP08's right-nested five-field tuple is then checked by source reduction and branch lemmas. WP11's source completeness remains the operative all-input termination and fuel bound (89 source-cost units, fuel 90).

## Negative result: raw natural-index encoding not validated

The original native decider tests **nonempty index data**, not whether that data is a *canonical* binary `Nat` representation. The following actual raw Data value illustrates the gap:

```text
noncanonicalZeroIndex = Data.cons Data.nil Data.nil
```

It decodes under the upstream `SizedEncoding Nat` decoder as `some 0`, but is **not the canonical encoding of any natural number**. In particular, `encode (0 : Nat)` is `Data.nil`, not this one-element false-bit list. WP12 proves both the decode fact and the stronger impossibility of representing the raw index as `encode n` for *any* `n : Nat`.

Place this noncanonical index in the source five-field input, followed by two canonical length-nine questions and empty answers. WP12 proves that **the actual imported source `Eval` has an accepting run** for this raw input and that the independent WP09 interpreter also returns canonical true at the WP11 uniform static fuel bound. This is a source-level, Lean-checked counterexample to the tempting claim that the existing decider rejects *all* malformed raw encodings. The accepted raw input is not a properly typed encoded `Nat` tuple, so it **does not contradict** the proved all-typed-input equivalence.

The previously recorded WP08 malformed *question-head* negative test remains compatible with this counterexample: malformed head bits are checked, but a malformed binary index can pass.

## Consequences and next gate

1. **Typed parser contract: proved.** Do not repeat finite tests as though the quantified theorem were still missing.
2. **All-raw-input canonicality: refuted for the present parser.** No amount of replay can certify a universally false proposition. If raw canonicality is needed by a source verifier, build a corrected source-native index validator and prove both its encoding discipline and its bounded-time semantics; then re-audit its interaction with the imported `Decider` interface. A wrapper that only accepts typed `SizedEncoding` inputs may instead be sufficient if that is explicitly the source contract.
3. **Sampler and verifier still open.** A full nine-level `Sampler 9`, four run conditions, `CLFun.ExactlyOn`, uniform halting and quantified verifier boundedness remain unproved. No positive-`λ` quantum compressor instance, uniform succinct SAT-to-classical resource transfer, or classical complexity lower bound follows.
4. **Theorem 12.1 and Formal Conjectures concordance:** unresolved. No PNP-001 mathematical status promotion.

**Claim discipline:** The malformed-index counterexample is a falsification of one *raw-parser canonicality* assertion, not of the typed parser theorem, the external MIP*=RE result, or the overall PNP-ABOVE research objective.

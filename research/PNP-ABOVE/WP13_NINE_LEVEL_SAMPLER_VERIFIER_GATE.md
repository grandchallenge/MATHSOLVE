# PNP-ABOVE WP13 — source-native bounded nine-level reference verifier

**Research parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136), under PNP-ABOVE. **Classification:** fully typed, executable Lean **reference/control verifier**. It is not a hard-game construction, a quantum compression theorem, an independent mathematical certification, or a P-versus-NP claim.

## Source identity and contract

- Pinned upstream `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean 4.35.0-rc3, pinned Mathlib and MIPStarRE.
- Protected MATHSOLVE parent: `fc83c349757fc01a1fe550432b49cc72afa5e715` (WP12 admitted typed parser and raw canonicality distinction).
- New source: [WP13_NineLevelSamplerVerifier.lean](WP13_NineLevelSamplerVerifier.lean). Exact source-locked [replay harness](WP13_REPLAY.sh) and [axiom audit](WP13_AXIOM_AUDIT.py); replay readback receipt: [WP13_IMPORT_REPLAY_RECEIPT.md](WP13_IMPORT_REPLAY_RECEIPT.md).

## Exact mathematical implementation

WP13 defines one genuine source-native `Cost.Prog` from `.elim`, `.const`, and `.var`, rather than pretending a mathematical sampler is itself executable. The program answers all four **original** `CL.Sampler.Query` cases:

1. **Dimension:** returns the correctly encoded `9`.
2. **Marginal:** returns the nine-bit input question `z` for each valid stage `1 ≤ j ≤ 9`.
3. **Linear:** returns `y` at stage `j = 1` and the nine-bit zero vector at stages `2 ≤ j ≤ 9`.
4. **Factor:** returns the full nine-coordinate indicator at stage `j = 1` and the empty indicator at stages `2 ≤ j ≤ 9`.

Both Alice and Bob use the same CL presentation: the full-register identity at stage one, followed by eight empty stages. This satisfies the *literal* original `CLFun.ExactlyOn Finset.univ` condition and retains the uniform nine-bit seed exactly: `(sampler9.cl n w).eval x = x` for both players. The two questions are perfectly correlated and jointly **nonconstant**. The final eight stages are nonetheless trivial. Do not describe this as a novel nine-stage hard distribution.

The proofs include closed-source scoping, source-native evaluation (`Cost.Eval`), all four query-run witnesses, every-raw-query termination, and an explicit source runtime bound. A read-only inspect/return program fragment is introduced and proved to execute with cost at most its **fixed maximum syntactic path cost** times `(B + 1)` when all current environment values have size at most `B`. Nested source `elim` steps preserve that bound on subtrees. For the exact sampler program, the syntactic bound is **47** (mechanically checked). Thus the original source interface proves

```text
sampler9.TimeBoundAt n (47 * (esize n + 2)) 1
```

for **every raw tail `d`**, not merely canonical queries. The decider reuses WP11's original source-native `Decider.TimeBoundAt n 89 0`. The exact source program sizes are **723** (sampler) and **145459** (WP08 decider) in upstream `Cost.Prog` encoding. All these literal quantities are checked against the pinned source in Lean.

WP13 then constructs a real source-native `MIPRE.Verifier 9`, using WP12's all-typed acceptance theorem to prove `Verifier.accepts_length`, and establishes the full upstream quantitative certificate:

```text
boundLam = verifier9.size + 10 = 145469
verifier9.IsBounded boundLam
```

The bound is mathematically valid but **enormously loose**; it is a source-contract witness, not useful runtime engineering or an optimized complexity exponent. It respects the source's actual input-size-polynomial `TimeBoundAt` conditions for all `n ≥ 2`, including the sampler dimension and both sampler/decider costs, and the verifier description-length requirement.

A separate source lemma establishes `verifier9.IsSynchronousAt n`. Another proves that at **every positive index** and for **every nine-bit question pair**, empty answers are accepted. This is intentional adversarial documentation: the new verifier is a control/reference case, and its game is trivial to win. It cannot certify a nontrivial MIP* gap, hardness, or a classical complexity separation.

## Proof discipline and remaining research

The exact-head harness imports and hashes original WP08–WP12 protected source blobs, checks the pinned MIPRE upstream commit, runs Lean over WP08–WP13, and audits **all 36 WP13 theorem declarations** for unadmitted axioms. Only standard Lean `propext`, `Classical.choice` and `Quot.sound` may appear; no `sorryAx`, native proof generation axioms, self-reported certifications or custom axioms. The source, runnable script, and reviewer-custody receipt are protected-PR admission candidates, not a substitute for independent mathematical certification.

**Actual follow-on research obligation:** Replace this diagonal reference instance with a **nontrivial nine-level CL family and a source-native sampler that honestly computes its marginals, conditional linear maps and factor spaces**, with all bound proofs, then study a *hard* game. The completed `Verifier 9` interface does not establish the nontrivial game, positive-parameter compressor, succinct SAT-to-classical resource transfer, Theorem 12.1 source quantitative reconciliation or PNP Formal Conjectures encoding concordance. Parent PNP-001 remains OPEN.

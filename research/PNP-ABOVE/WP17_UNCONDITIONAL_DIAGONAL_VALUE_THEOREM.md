# PNP-ABOVE WP17 — unconditional no quantum or commuting advantage for diagonal-supported synchronous games

**Claim level:** general source-native Lean theorem in the *original pinned* MIPRE game model. This is a structural **negative/necessary-condition** result, not a game hardness proof, new executable decider, quantum compression, external independent certification, or a P-versus-NP resolution.

## Source and exact theorem

- External original: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970` (Lean 4.35.0-rc3, pinned Mathlib/MIPStarRE). Protected MATHSOLVE parent WP16 `f25d8da67c48d88c2729c5fd454386667999253b`.
- Source [WP17_UnconditionalDiagonalNoGap.lean](WP17_UnconditionalDiagonalNoGap.lean). Reproducer [WP17_REPLAY.sh](WP17_REPLAY.sh), axiom audit [WP17_AXIOM_AUDIT.py](WP17_AXIOM_AUDIT.py), exact replay [WP17_IMPORT_REPLAY_RECEIPT.md](WP17_IMPORT_REPLAY_RECEIPT.md).

For **every finite original  `MIPRE.SynchronousGame X A` with a nonempty answer alphabet** satisfying  `G.μ x y = 0` whenever  `x ≠ y` (without assuming all diagonal questions are sampled, or that all questions have a winning answer), WP17 defines

```text
feasible G x := ∃ a, G.D x x a a = true
feasibleMass G := ∑ x, G.μ x x * (if feasible G x then 1 else 0)
```

and proves in the **original game model**

```text
syncValue G = feasibleMass G
quantumValue G.toGame = feasibleMass G
commValue G = feasibleMass G
```

Therefore  `syncValue G = quantumValue G.toGame = commValue G`, even if that common value is strictly less than one. The proof constructs original one-dimensional deterministic, **question-dependent** projective measurements that choose a winning equal answer on each feasible diagonal question (and an arbitrary answer where impossible), evaluates their original Born-rule value exactly, and independently upper-bounds **every** original tensor-product and commuting strategy by the mass of feasible diagonals. The crucial upper bounds use source-native positivity and normalization of *all* answer-outcome probabilities. The original  `SynchronousGame.synchronous` predicate excludes unequal answers on equal questions. The maximum is attained without entanglement or commuting-operator advantage.

**Direct WP14 consequence:** The protected WP16 theorem establishes from source  `MIPRE.CL.clDist` that WP14's shared Alice/Bob nine-stage conditional CL map produces only  `x=y` question pairs. WP17 instantiates its unconditional theorem with **any replacement Boolean synchronous decision predicate** while retaining the original WP14 sampler distribution, at **every index and answer budget**. Thus *no such predicate-only replacement can produce a quantum/synchronous or commuting/synchronous value gap*, whether or not some diagonal questions are unwinnable. **This removes WP16's positive-support feasible-answer hypothesis entirely for original synchronous games.**

## Boundaries and necessary research change

This is a theorem about **diagonal-supported synchronous games with nonempty answer alphabets**. It does **not** prove all conditional-linear games easy, any general MIP* complexity separation, or original  `Verifier.IsBounded` for an arbitrary new replacement predicate. That predicate is a mathematical input to a game definition; **no original executable source  `Cost.Prog` replacement** has been built in WP17. A valid nontrivial quantum/classical game-value gap therefore **requires off-diagonal sampled player questions in this source model**, plus an answer-sensitive and bounded executable decider and independent completeness/soundness proof. WP14's full-depth conditional map remains legitimate interface infrastructure, but its *shared Alice/Bob* distribution is unsuitable for the target gap.

Open: player-asymmetric or otherwise non-diagonal native sampler, source-native decider, quantum/classical game-value gap, positive-parameter compression, Theorem 12.1 quantitative and Formal Conjectures source concordance, uniform succinct SAT-to-classical resource transfer. No independent mathematical certification or P-versus-NP conclusion. Keep MATHSOLVE #1136 and PNP-001 open.

**Admission gates:** Pin every original WP08–WP16 module, compile WP08–WP17 under the original upstream source, and audit **17 distinct** WP17 theorem declarations through original Lean `#print axioms` with no custom axioms or generated proof axioms. Then require protected review/CI, exact-head merge, source/receipt readback and separate public evidence integration before asserting admission.

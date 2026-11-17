# PNP-ABOVE WP10 — source-native acceptance proof and succinct-transfer negative control

**Research parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136).
**Classification:** `CAL` for the bounded Python negative-control test; `LEAN-REPLAYED / NOT CERTIFIED` for the imported Lean WP10 proof; exact imported evaluation and quantified claims are checked. This is not mathematical certification, not a compressed verifier, and not an NP lower bound.

## Source identity and governance

- Protected MATHSOLVE baseline: `a0af41fad9ad58d3e333092586119b4c660da382`.
- Upstream pinned source: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`; toolchain `leanprover/lean4:v4.35.0-rc3`.
- Genuine WP08 native decider source Git blob: `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`.
- Genuine WP09 interpreter soundness source Git blob: `3b64353814fd70a77810e51f2d04cbcfb4271def`.
- WP10 Lean proof candidate: [WP10_SourceAcceptanceBridge.lean](WP10_SourceAcceptanceBridge.lean). Its proof imports temporary modules populated byte-for-byte from those exact WP08 and WP09 files; it does not recreate upstream source types.
- Replay procedure: [WP10_REPLAY.sh](WP10_REPLAY.sh), requiring both pinned upstream and protected-ancestor GCL source. No new workflow or control-plane authority is introduced.

## WP10 native acceptance proof: precise status

The source-native Lean proof establishes four narrow results:

1. If the already-source-sound `WP09.runFuel` returns the canonical `encode true` on WP08's original `identityDeciderProg` and typed input, there is an actual imported `MIPRE.Decider.Accepts` witness with the same reported time. This is immediate from WP09's source-checked `runFuel_sound` theorem.
2. If that computation returns canonical `encode false`, `MIPRE.Cost.Eval.deterministic` rules out any conflicting canonical-true acceptance witness for that input.
3. The 63-cost, positive-index nine-bit example from WP08 is established as a concrete source acceptance theorem, this time evaluating it through the *WP09* interpreter rather than assuming the two interpreter definitions are equal.
4. The zero-index typed example is proved as a source-level rejection theorem, rather than merely a Boolean test.

**Replay status (17 November 2026):** The previously missing upstream `.olean` dependency was recovered through a complete exact-upstream source build, including `MIPRE.Foundations.Verifier` (**3,111 Lake jobs, success**). The first replay uncovered a Lean 4.35 root-directory constraint; `WP10_REPLAY.sh` now uses `lean -R "$work"` when checking temporarily staged modules. The final source passed direct imported-source elaboration for WP08, WP09 and WP10 with exit 0, empty WP10 diagnostics and `WP10_IMPORTED_REPLAY_PASS`. A proof-trust inspection found that `native_decide` had introduced separate generated proof axioms for two concrete examples, so the tactics were replaced with ordinary kernel `decide`. A separate replay of that replacement passed; the full axiom report, source SHA-256 hashes, and exact replay instructions are recorded in [WP10 execution receipt](WP10_IMPORTED_ACCEPTANCE_REPLAY_RECEIPT.md); protected PR admission/readback remain separate.

The generic bridge theorems depend only on `propext`, `Classical.choice` and `Quot.sound`. The final imported replay audit also verified exactly those standard axioms in both concrete examples (with kernel `decide`, not `native_decide`). The proof does not depend on a copied MIPRE model, a new user axiom, or an admitted quantum-compression theorem.

**Next proof obligation:** extend the result to all well-typed nine-bit inputs, malformed raw-data behavior, complete `Decider.Accepts` equivalence and a uniform cost/completeness argument. A full `Sampler 9`, `Verifier 9` and positive-`λ` compilation remain separately open.

## Classical transfer: an exact negative control

Define a uniformly specified indexed diagonal game `H_m` for every positive integer `m`:

- Alice and Bob questions are each the set of binary strings of length `m`, giving `2^m` questions per player.
- The referee draws one uniform `m`-bit string `z` and sends `(z,z)`. Thus there are exactly `2^m` supported pairs.
- Each player has exactly one allowed answer, the empty string.
- Every supported pair with empty answers is accepted.

Both players have a perfect deterministic local strategy: **always answer the empty string**. The same code works for every `m` and has constant description size. The sampler and predicate are uniformly implementable using `m`-bit operations. The indexed perfect-value membership language is trivial.

Now apply *exactly the fixed one-hot CNF schema* proved in WP01 to the explicitly expanded game table. It assigns one Boolean variable to each possible answer on each question for each player. Consequently

$$
M(m)=|X_m|\,|A_m|+|Y_m|\,|B_m|
     = 2^m+2^m=2^{m+1}.
$$

Every question has only one answer, so the schema introduces one positive unit clause per question on each side. There are no mutual-exclusion clauses and no losing-answer-pair clauses on the support. Therefore the output has **exactly** `2^{m+1}` variables and `2^{m+1}` unit clauses.

This is a sharp lower bound on the output length of **that fixed, explicitly expanded encoding**. It is **not** a lower bound on an arbitrary representation of the game, on a compressed SAT formula, on circuit size, on SAT itself, or on every method of finding a strategy. Indeed the uniform winning strategy is constant-size. If a hypothetical polynomial-time SAT solver is applied after this expansion, its guarantee is polynomial in the explicit formula size, which can already be exponential in `m`. Replacing explicit table size with succinct index length silently drops a necessary overhead.

The `m=9` supported-question distribution mirrors the diagonal reference used in WP00, but this variable-dimension family is **not claimed** to be a source-encoded, `λ`-bounded nine-level normal-form input to the published compressor.

### Reproducibility

[WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py](WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py) implements the fixed one-hot expansion, checks the exact counts and verifies every supported pair's constant winning strategy for `m=1,...,10`, with standard-library Python only.

- Tested exact candidate source SHA-256: `5d6be837f8e3d183d2126b3b874458cf35f8aeda7bf0c564c068b80f985f9a2b`.
- Command: `python3 research/PNP-ABOVE/WP10_EXPLICITIZATION_NEGATIVE_CONTROL.py --max-m 10`.
- Observed: exit 0; cases `m=9` and `m=10` had respectively 1,024 and 2,048 one-hot variables/clauses; terminal `PASS: exact one-hot CNF size and uniform winning strategy`.
- GCL CONTROL execution capture: `8270831865834b55b7649d04a5e067c0`. This is OS-local execution, not mathematical certification.

## Governing consequence

A SAT-to-strategy argument relevant to PNP-001 must identify a **succinct** classical invariant and a uniform extraction algorithm whose total bit and time costs are polynomial in the locked ordinary input length, with any answer representation explicitly counted. The known source theorem's quantum Schmidt-rank lower bound has no such transfer map. This WP10 negative control narrows a specific proposed algorithm; it does not rule out an alternative succinct route.

The original PNP-001 Formal Conjectures machine/encoding concordance blocker, the Theorem 12.1 proof/statement factor discrepancy, the sampler construction, source complexity witnesses, and all P-versus-NP claims remain unresolved. No parent tracker closure or claim promotion is authorized.

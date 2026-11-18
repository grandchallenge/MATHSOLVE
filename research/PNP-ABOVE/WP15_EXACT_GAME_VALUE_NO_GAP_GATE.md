# PNP-ABOVE WP15 — exact-game-value no-gap certification for the WP14 reference verifier

**Research status:** complete negative-value theorem target (subject to exact-head replay and protected admission), **not** a new hardness construction, P-versus-NP claim, or independent public mathematical certification. Parent programme [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136) remains open.

## Sources and governing scope

The result imports the original upstream `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970` (Lean 4.35.0-rc3) through the protected PNP WP08–WP14 source modules. The protected parent is MATHSOLVE `cb65e0f5386bbc42ffde5f9ea6943b8d9955e529`. This WP uses **the upstream native `MIPRE.SynchronousGame`, `MIPRE.SyncStrategy`, `MIPRE.syncValue`, `MIPRE.quantumValue` and `MIPRE.commValue`**. No copied value semantics, target theorem axioms, or finite sample-to-asymptotic extrapolation are permitted.

## Exact theorems

For **every** positive index `n` and **every** natural answer-length budget `T`, WP15 applies WP14's real `Verifier.syncGame n T` construction. The zero-length answer is available even at `T = 0`. From the protected WP14 source acceptance theorem and the original `Decider.Accepts` semantics, the game accepts this fixed answer pair on **all** question pairs.

WP15 then constructs a one-dimensional, deterministic `SyncStrategy` in the original upstream matrix model. Its projective measurement returns the fixed answer with certainty. A source-native Born-rule computation proves its value **exactly 1**, rather than treating the decidable acceptance predicate as a proxy for game value.

The exact original game-value suprema satisfy

```text
(syncValue G) = 1
(quantumValue G.toGame) = 1
(commValue G) = 1
quantumValue G.toGame - syncValue G = 0
commValue G - syncValue G = 0
```

No classical/quantum or synchronous/commuting advantage is possible for **this specific WP14 game**, at any positive index or answer budget. The result does not purport to limit unrelated games, other deciders, the compression theorem, or general MIP* problems. Although WP14 has nine genuine nonempty conditional CL stages, its current decider makes the nonlocal game trivially solvable. Thus nontrivial CL geometry alone does not prove a soundness gap.

The next substantive research requirement is a genuinely **discriminating, source-native decider** paired with suitable independent or correlated player questions and a rigorously established nonzero game-value gap. A hard-game claim must include soundness/quantum-value proofs and native source runtime, not just a modified finite truth table. Separately unresolved: positive-parameter compression, source Theorem 12.1 quantitative concordance, and succinct SAT-to-classical resource transfer.

## Replay contract

The reproducible `WP15_REPLAY.sh` locks external upstream, protected WP14 parent, and exact WP08–WP14 Git blobs; compiles WP08 through WP15 using the pinned Lean toolchain; and runs `WP15_AXIOM_AUDIT.py` on **16 distinct** WP15 theorem declarations. Axiom reports must contain only standard `propext`, `Classical.choice`, or `Quot.sound` and no custom axioms or generated native proof axiom. Record the exact candidate, proof blob and SHA-256, successful replay, source CI, and final protected-main readback in `WP15_IMPORT_REPLAY_RECEIPT.md` before claiming protected admission.

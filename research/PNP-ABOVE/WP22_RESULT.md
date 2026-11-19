# PNP-ABOVE WP22 — original bounded verifier with strict native Bell gap

**Scientific disposition (pending protected admission):**
WP22_SOURCE_NATIVE_SYNCHRONOUS_EXECUTABLE_STRICT_BELL_GAP_PROVED__COMPRESSION_AND_PNP_TRANSFER_OPEN.

**Protected predecessor:** MATHSOLVE 46d7bbc9167bb52d457e55d1b8741f7695e16576 (WP21).
**Pinned source:** vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970, Lean 4.35.0-rc3.
**Active research:** MATH-PROGRAMME #162 (PNP-001, OPEN). MATHSOLVE #1136 remains the CLOSED WP00 historical preflight ticket.

## Exact mathematical result

WP21 constructed the executable original MIPRE.Cost.Prog CHSH decider and a genuine original Verifier 9 using WP20's two-sided cyclic conditional-linear sampler. WP22 proves a universal source acceptance specification, original native synchrony, and an unrestricted native quantum/classical game-value gap.

For V = PNPAbove.WP21.cyclicVerifier, every source index n != 0 and every allowed answer budget T >= 1:

    (81/100 : Real) <= MIPRE.quantumValue (V.game n T)
    WP22.nativeClassicalValue n T <= (3/4 : Real)
    (3/50 : Real) <= quantumValue (V.game n T) - WP22.nativeClassicalValue n T

The classical value is the supremum over all distinct local deterministic response functions into the FULL original Verifier.Answers T alphabets. Shared randomness cannot improve the expectation because it forms convex combinations of deterministic responses. Invalid, empty or multiple-bit answer strings are not assumed absent; their original source rejection is proved. The quantum lower witness extends its old projective measurements with zero operators for extra answers.

For every n >= 2, the same positive gap holds at the **actual source bounded budget** T = n ^ WP21.boundLam; WP21 already proved V.IsBounded WP21.boundLam.

This is a strict quantum/classical game gap for an original, source-executable bounded verifier, not merely an abstract game. It does NOT establish P != NP.

## Nine-module proof chain (35 new theorem declarations)

1. WP22_BitRead.lean proves arbitrary encoded-list bit-read semantics in the imported Cost.Prog source interpreter, for all environments and indices.
2. WP22_Truth.lean proves all 64 cases of the original six-bit decision tree.
3. WP22_Evaluator.lean proves exact de Bruijn binding offsets across six nested original source operations.
4. WP22_Parser.lean proves parser rejection at every malformed question and answer length, zero index, and a fully universal typed_value_spec.
5. WP22_Native.lean proves original Decider.Accepts iff the specified valid source expression; singleton normalization; and original Verifier.IsSynchronousAt for every index.
6. WP22_SourceBridge.lean connects original CL.toBits and native Verifier.game to the mathematical masked Boolean predicate. It handles every nine-bit question, every binary answer and every rejected non-singleton source answer.
7. WP22_Classical.lean proves masked acceptance is dominated by the WP20 parity acceptance, and every full native response strategy is dominated by a Boolean response strategy. Hence nativeClassicalValue <= 3/4.
8. WP22_Quantum.lean uses the original imported quantumValue_extendAnswers theorem from pinned MIPRE.Foundations.GameTransport, with a proved injection of Bool into original Answers T, to identify the complete native quantum value with the masked-binary game's quantum value.
9. WP22_Gap.lean proves all remaining predicate differences are confined to question pairs of EXACTLY ZERO source probability. The existing original rational two-dimensional SyncStrategy survives as a genuine tensor-product strategy of value 81/100. Final theorems native_strict_gap and bounded_native_strict_gap prove the stated bound.

WP21's 2,048 finite source regression cases are now supplementary engineering tests. The WP22 correctness and value statements are universally quantified theorems, not finite extrapolations.

## Replay, provenance and exclusions

WP22_SOURCE_LOCK.json records exact SHA-256, Git blob hashes and complete inventories for the nine Lean modules. WP22_SOURCE_GUARD.py rejects altered source bytes, proof holes, unsafe axiom declarations and theorem inventory drift. WP22_REPLAY.sh replays exact original WP08–WP21 source and Lean kernel checks; builds original pinned GameTransport; compiles all nine new modules; and runs WP22_AXIOM_AUDIT.py. The axiom audit allows only standard propext, Classical.choice and Quot.sound, or no axioms.

WP22 does NOT prove a positive-parameter gap-compression construction, its exact JNVWY Theorem 12.1 constants, a uniform succinct SAT-to-classical-strategy lower-bound transfer, a P versus NP separation, or independent external MATHCERT certification. We do not claim the exact native quantum optimum; only the >= 81/100 witness.

**Next: WP23.** Bind the original positive-parameter compression and introspection framework to this exact bounded synchronous source verifier. Prove the parameter, constructibility, runtime, dimension and game-value transfer hypotheses. Inspect whether the resulting classical-strategy cost lower bounds genuinely transfer to arbitrary PNP-001 instances. Keep the programme open until the substantive bridges are established.

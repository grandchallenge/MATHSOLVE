# PNP-ABOVE WP23A — fixed-game compression incompatibility and exact classical value

**Scientific disposition (pending exact replay and protected admission):**
WP23A_FIXED_GAME_INDEX_INVARIANCE_AND_NO_QUANTUM_SOUNDNESS_PREMISE_PROVED__INPUT_DEPENDENT_COMPRESSION_TRANSFER_OPEN.

**Protected parent:** MATHSOLVE 38e37a53596762757798c75729aaedfef3af1d1f (WP22 native strict Bell game gap).
**Pinned original upstream:** vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970 (Lean 4.35.0-rc3).
**Active campaign:** MATH-PROGRAMME #162, OPEN. Historical MATHSOLVE #1136 is CLOSED.

## Exact proved results

WP22 admits a bounded original MIPRE Verifier 9 using a fixed nine-register cyclic CHSH sampler and an executable Cost.Prog decider. The quantum/classical gap is real. WP23A now proves that the fixed construction is **not directly an instance of the soundness-promise regime** required for the original GapCompression theorem.

Two original-source Lean modules with seven theorem declarations establish:

- For every n != 0 and T >= 1, the unrestricted original-source deterministic classical optimum is **EXACTLY 3/4**. The upper bound is WP22's universal argument; the lower bound is an original source-native, canonical binary-answer strategy achieving WP20's exact constant-false value.
- For every two positive indices n,m and one-bit-capable budgets T,U, original native quantum values are equal to each other. Both are equal to the quantum value of the same fixed masked-binary game. Exact classical local values are also equal to each other (3/4).
- The original native quantum value is > 1/2 for every n != 0 and T >= 1. In particular for **every k and lambda**, the power-of-two source index 2^k with original bounded source budget (2^k)^lambda FAILS the <=1/2 quantum-value soundness premise in the original GapCompression.soundness field.

This negative theorem is about the FIXED cyclic CHSH verifier, not an impossibility theorem about P versus NP, all MIP* verifiers, or all possible reductions.

## Original compression interface, source audit

The pinned MIPRE.Foundations.GapCompression.lean type has input Verifier 7 and separates:
- Perfect PCC strategy, value exactly 1, for completeness;
- Quantum value <=1/2 for soundness.

Our fixed cyclic game is Verifier 9, with quantum value >=81/100 at every positive source index and the latter soundness antecedent provably FALSE. Hence it cannot be plugged in as-is to obtain a nonvacuous compression soundness conclusion. This is an interface and instance mismatch, not a failure of the WP22 gap theorem.

The source also contains an actual constructed upstream MIPRE.gapCompression in MIPRE/MainTheorem.lean via the introspection/answer-reduction/repetition pipeline. WP23A does not dispute that theorem. It establishes the narrower fact that the specific source-native Bell verifier is the wrong input family and promise regime to infer complexity lower bounds.

## Technical proofs

- WP23_NativeConst.lean: native_binary_det_eq; native_constant_false_three_quarters; native_classical_exact_three_quarters.
- WP23_Probe.lean: cyclic_never_quantum_sound; cyclic_power_two_no_soundness; cyclic_quantum_index_invariant; cyclic_classical_index_invariant.

Both files use the original imported Lean operational and quantum game definitions through the protected WP22 source lock; no new abstract execution model is introduced.

## Next obligation and claim boundary

WP23B should define a **source-native SAT-instance-dependent verifier family**, or a mathematically justified transformation from such a family, with explicit instance uniformity, original MIPRE source runtime and question sampling. It must bridge the seven-level compression interface and the value-one PCC / <=1/2 quantum promise split, not assume the fixed Bell advantage supplies them. Then an independent classical strategy-cost transfer to the locked PNP Turing-machine and reduction model remains necessary.

We do NOT claim: an implementation of that family; positive-parameter compression for it; a new lower bound on NP; a P != NP or P = NP result; or independent MATHCERT certification.

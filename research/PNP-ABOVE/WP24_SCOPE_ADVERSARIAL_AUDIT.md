# WP24 — bounded logical review and adversarial scope

Verifier: SAT.Fml, SAT.Cnf3, SAT.Circuit, SyncStrategy,
quantumValue, and Cost.PolyTimeFun are imported from the pinned original
MIPRE source; the actual game is a SynchronousGame, NOT Verifier 7.
The constructed polynomial program compiles circuits, NOT a full verifier.

Adversary: the two concrete formulas p AND NOT p and p OR NOT p
have kernel-proved distinct values, preventing a fixed game being
mislabelled input dependent. The three-literal source translation
preserves polarity and variable bounds. Unrestricted tensor soundness
is achieved because no response is accepted on an unsatisfiable
input, not through an unproved finite-seed heuristic. The perfect
PCC witness is the original concrete one-dimensional strategy.
The source algebra gate bound is on the actual original circuit.
No default Boolean predicate is assumed to be an efficient
source-normal-form Verifier 7. Full assignments make this a
trivial-query SAT witness game, not a two-prover lower-bound device.

Referee scope: ADMIT_FORMULA_DEPENDENT_ORIGINAL_GAME_AND_EXACT_PCC_PROMISE_ONLY
after exact uncached replay and protected checks. Explicitly withhold
VERIFIER7_COMPRESSION_AND_CLASSICAL_HARDNESS_TRANSFER. No independent
external certification or P-versus-NP separation is implied.

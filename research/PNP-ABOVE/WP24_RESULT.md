# PNP-ABOVE WP24 — SAT-instance-dependent original MIPRE game

Scientific disposition: kernel-compilable candidate. Uncached exact source replay,
protected admission and exact merge readback are additional requirements.

Original upstream: vidick/MIPRE-formalization at
5926bdff5db621f44682a101007ef2fe3ae8d970; Lean v4.35.0-rc3.
Protected predecessor: MATHSOLVE 442cef7f7b5c18afffa132ae5eba01087ba7cdea.
PNP-001 campaign: MATH-PROGRAMME issue #162, OPEN.

## Original-source construction

For each original MIPRE.SAT.Fml Boolean formula f on n declared input bits,
WP24 constructs a finite MIPRE.SynchronousGame with one question and response
alphabet (Fin n -> Bool). Both provers return full assignments. Acceptance is
exactly formula satisfaction by Alice AND identical responses from Bob. The
predicate genuinely depends on the supplied instance, unlike the WP23A fixed Bell game.

Eleven theorem declarations in WP24_SATGame.lean (including the finite-bit lookup lemma):
- accepts_iff: exact original source game-predicate condition.
- exists_accepted_iff_sat: accepted response iff satisfying assignment exists;
  the successful first response is an exact classical SAT witness.
- perfectPCC_of_sat and perfectPCC_iff_sat: an original one-dimensional
  MIPRE.SyncStrategy.const has perfect PCC value one iff the formula is SAT.
- quantum_zero_of_unsat: original tensor-product quantum value is zero when
  UNSAT (all possible answers are rejected).
- quantum_one_of_sat and quantum_value_eq_one_iff_sat: exactly one when SAT,
  and the converse.
- soundness_half_of_unsat: zero value implies <= 1/2.
- uniformCircuit_correct and uniformCircuit_polytime: the ACTUAL pinned original
  MIPRE.Cost.PolyTimeFun (Nat x Fml) Circuit code and explicit source polynomial
  timeBound compute the correct Boolean circuit. No assumed source compiler.

WP24_3CNF.lean bridges the original finite MIPRE.SAT.Clause3 and Cnf3
language to arbitrary original SAT.Fml instances. It proves source
literal-polarity preservation, exact all-clause satisfaction, original
Cnf3.Sat witness equivalence, strict variable scoping, original
SAT.Circuit.WellFormed, and size <= 9*m+1 gates for m clauses.
Perfect PCC on the game is equivalent to original 3CNF satisfiability.

WP24_Examples.lean constructs p AND NOT p and p OR NOT p with identical
variable and question alphabets, and formally proves quantum values 0
and 1 respectively. This directly refutes index/instance invariance.

## Claims proved and not proved

PROVED:
(1) a genuine formula-dependent original MIPRE synchronous game;
(2) perfect PCC iff SAT and tensor quantum value exactly 1 or 0;
(3) original 3CNF exact witness correspondence;
(4) original finite Boolean circuit with <= 9*m+1 gates;
(5) original Cost.PolyTimeFun with a source program and explicit polynomial
cost for formula-to-circuit compilation.

NOT PROVED:
(1) original source-normal-form MIPRE.Verifier 7 consisting of a
CL.Sampler 7 and Cost.Prog decider with original accepts_length,
source TimeBoundAt and IsBounded lambda;
(2) an original Cost.PolyTimeFun answer EVALUATOR and indexed
formula encoding/compiler to that Verifier 7;
(3) equivalence between the mathematical game value here and
Verifier.valStar at a defined index and answer budget;
(4) polynomial-time classical search for satisfying assignments,
lower bounds on classical computation or P != NP;
(5) protected-admission replay or external certification until
the exact evidence conditions are met.

The game uses a single common question and full assignment replies, so
there is no locality or amplification. The Game 1/0 promise does NOT
automatically satisfy the original GapCompression theorem, which
requires an IsBounded native seven-level source verifier.
The polynomial source compiler in (5) compiles a FORMULA TO CIRCUIT,
not a full source-native verifier. These are different operations.

True next technical boundary:
SOURCE_NATIVE_SEVEN_LEVEL_POLYTIME_SAT_VERIFIER_NOT_YET_CONSTRUCTED.

Proposed next lane: WP25_ORIGINAL_SAT_EVALUATOR_AND_VERIFIER7_COMPILER.

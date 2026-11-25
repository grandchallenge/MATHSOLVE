# WP25 original PTF SAT evaluator — constrained internal scope

Verifier: The code is a bona fide MIPRE.Cost.PolyTimeFun whose .code is an
original well-scoped Cost.Prog. It evaluates arbitrary ORIGINAL SAT.Fml
syntax via original typed first-order encoded inputs, with a source runtime
certificate for each such encoded input, independent of the specific
formula. Its Boolean answer-checking agreement with the admitted WP24
game is formalized by source_program_agrees_with_sat_game.

Adversary: The theorem and source program contain no Lean sorry, axiom,
native_decide, external oracle or postulated parser. Postfix evaluation
handles all original formula constructors and malformed intermediate
stacks. The source binary-indexed lookup is already proved polynomial
in the original Cost model, not a unary-index materialization.
The polynomial fold step growth is justified at each source node,
and its original runtime certificate is obtained from source Prog
execution via Cost.PolyTimeFun.computes.

Referee restricted scope:
WP25_ORIGINAL_COST_PROG_TYPED_SAT_ANSWER_EVALUATION_PROVED.

Absolute nonpromotion:
Cost.PolyTimeFun.computes has a typed input argument
((SAT.Fml × BitStr) × BitStr); MIPRE.Decider is required to run on
the ORIGINAL raw tuple encoding (n,x,y,a,b) for every malformed raw
Data input and prove TimeBoundAt n T k. These are different claims.
Likewise WP25 has no original CL.Sampler 7, accepts_length or
Verifier.IsBounded. No compression theorem application or
classical complexity lower bound follows. A winning answer is a SAT
witness, not a polytime SAT search procedure.

Final gate: exact immutable WP25 candidate full-source uncached replay,
new source hashes, original standard-axiom audit, all required GitHub
checks, and protected merge readback. Public MATHCERT certification
remains separate.

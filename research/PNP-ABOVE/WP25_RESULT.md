# PNP-ABOVE WP25 — uniform original Cost.Prog SAT answer evaluator

Scientific disposition: original pinned Lean kernel-checked LOCAL
prototype. The manifest now source-locks 11 declarations to the exact
protected WP24 merge. Full uncached exact-head replay and protected
admission remain separately required.

Protected input source: WP24 protected merge
af675f4862d2f2822d6fe669ab043be438dff4ed (PR #1262);
exact admitted WP24 candidate b976e9600080a4a402a31be417c7dc7ebecdcf17;
original upstream
vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970
with Lean v4.35.0-rc3.

## Source-native construction and proven facts

WP25_SourceEvaluator.lean defines:

* nodeStepP: an ACTUAL MIPRE.Cost.PolyTimeFun machine composed from
  original MIPRE SAT.PolyTimeFun.casesNode,
  ArrayProg.getD false, Cost.PolyTimeFun.casesList,
  Cost.PolyTimeFun.ite, foldlAdd and SAT.notBoolP. It uses a
  reverse-Polish interpreter with explicit stack-bounded memory;
  malformed stacks are handled without undefined behavior.
* evalFormulaProgram : PolyTimeFun (SAT.Fml × BitStr) Bool. It evaluates
  arbitrary original formula syntax and supplied binary witness, with
  binary-index reads avoiding unary expansion. execNode_size_bound
  gives each fold step an additive constant-4 bound in the original
  source encoding esize. foldlAdd produces the original polynomial
  source-runtime certificate. executeRpn proves exact semantics.
* answerCheckProgram : PolyTimeFun ((SAT.Fml × BitStr) × BitStr) Bool
  accepts precisely when the first response satisfies the formula AND
  both complete answer strings agree. Its closed source program and
  polynomial timeBound are constructed, not assumed.
  source_program_agrees_with_sat_game proves equality with WP24's
  arbitrary-formula game for canonical assignments;
  accepted_source_witness_iff transfers actual source witnesses.

All 11 source Lean theorem declarations compiled using original Lean.
Their original #print axioms reports only propext, Classical.choice,
Quot.sound or none. Exact source-locked protected admission is not yet
established by these local checks.

## Open boundary

This closes typed polynomial source answer evaluation. It DOES NOT
construct a fully conforming original MIPRE.Verifier 7:

1. Build an original CL.Sampler 7 with exact supported CL query
   contracts, properly encoded questions and bounded source runtime.
2. Build a Decider on exact raw tuple encoding (n,x,y,a,b) with a
   polynomially uniform formula/instance encoding, not the typed
   (Fml,a,b) input employed in the current program.
3. Reject invalid question dimensions and overlong answer strings
   using the actual upstream acceptance interfaces.
4. Prove original Decider.TimeBoundAt n T k for EVERY raw Data input,
   not merely the typed PolyTimeFun.computes guarantee.
5. Prove Verifier.IsBounded lam, original valStar-equivalence,
   source seven-level perfect PCC and <= 1/2 quantum promises.

A winning answer carries an SAT witness but finding such answers is
still a search task. No polynomial SAT search algorithm, classical
lower bound, P=NP or P!=NP, nor public MATHCERT certification follows.

Next target: WP26_SEVEN_LEVEL_SAMPLER_AND_UNIFORM_SOURCE_DECIDER_BRIDGE.

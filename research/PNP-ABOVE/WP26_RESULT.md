# PNP-ABOVE WP26 — source-native seven-level SAT verifier and polynomial programme generator

Status: local original Lean-kernel proof candidate. Protected admission requires full uncached replay. Protected predecessor MATHSOLVE df62dc3de0a585ff490f4e56abf5d1c76cb6f12e (WP25 PR #1263). Original pinned: vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970; Lean v4.35.0-rc3. Active PNP-001 campaign: MATH-PROGRAMME issue #162 OPEN.

## Constructed native original Verifier 7

WP26_NativeVerifier.lean defines original Cost.PolyTimeFun rawAlice and rawBob that extract responses from the exact (n,x,y,a,b) original native tuple. Original Verifier.ofSamplerDecider applies source Cost.UniversalMachine and a genuine source CL.Sampler 7 with required question-length checks. The Lean kernel proves precise native Decider.Accepts semantics for all typed tuples, source synchrony, and polynomial typed raw-program execution.

Given f.InputsLt m and T>=m, source Lean proves SAT implies native Verifier.HasPerfectPCC k T (an actual constant one-dimensional strategy) and valStar k T=1 for all k; UNSAT implies rejection of all native answers/questions and valStar k T=0 for ALL k,T, hence <=1/2. ValStar=1 iff SAT holds on scoped instances. For every legal question pair, an accepted bounded-length pair exists iff SAT and Alice's bits are a satisfying assignment. This proves classical witness equivalence but not efficient witness search.

Actual original GapCompression.completeness and soundness are applied to this source native verifier with original IsBounded lam, C0<=k and witness-budget premises visible; applications are conditional.

## Uniform original polynomial-time source compiler

WP26_UniformCompiler.lean builds a FIXED original Cost.PolyTimeFun sourceCoreChecker evaluating (f,(n,x,y,a,b)). Original Cost.PolyTimeFun.smn then compiles each SAT formula to the exact source Cost.Prog Cost.hardcode sourceCoreChecker.code (encode f). Lean proves the source generator is itself a polynomial-time Cost.PolyTimeFun with a concrete original machine run certificate; its emitted program is closed and original source hardcode_time/hardcode_time_rev establish its precise acceptance behavior. This is a proven ORIGINAL polynomial-time SAT.Fml-to-source-decider-program construction, not a metalevel promise.

The separately constructed uniformSatVerifier is an ACTUAL original MIPRE.Verifier 7 using the emitted source program. The Lean kernel proves its source acceptance semantics, perfect PCC on SAT, exact native valStar 1 for SAT and 0 for scoped UNSAT, original bounded-answer classical witness iff SAT, and legal conditional source GapCompression.completeness/soundness.

## Exact outstanding boundary

ALL-RAW-DATA polynomial boundedness is still unproved. Original typed PolyTimeFun.computes does not establish Decider.TimeBoundAt n T k for ALL raw Data, including malformed encodings. The source proves that original upstream sampler dimension/time bounds and source wrapper reduce IsBounded to the raw source-program HasPolyCost obligation in the fixed-formula construction. A corresponding bound for the source-generated hardcoded program, with an explicit lambda polynomially uniform in formula size, remains necessary.

Thus the compressor applications are CONDITIONAL on the precise original IsBounded premise. They are not an unconditional compression proof. Original source concrete Cost.selfUniversal and MIPRE.gapCompression constructors reside in pinned MainTheorem; this tranche's source lemmas quantify over existing instances of these types rather than importing the constructors. Formally compose 3CNF-to-Fml with Fml-to-source-Prog and prove any meaningful classical lower bound separately. A one-question full-assignment game does not imply a polynomial SAT search algorithm or P != NP.

Next: WP27_RAW_DATA_TOTAL_COST_AND_EXACT_LAMBDA_UNIFORMITY.
Boundary: SOURCE_ALL_RAW_DATA_HASPOLYCOST_FOR_UNIFORM_SAT_PROG_OPEN.

# PNP-ABOVE WP28C — source-native 2^k-index compression compatibility

Status: original Lean-kernel-checked proof candidate, 16 original
theorems in three modules. WP28B2 was independently fully replayed
and protected-admitted at b0e9acce5cffa8aeff5e7a6fd9e7f20970ea9602
(PR #1273). WP28C needs its own exact-head full uncached replay,
source-lock, review and protected admission.

Protected exact predecessor: MATHSOLVE main
b0e9acce5cffa8aeff5e7a6fd9e7f20970ea9602, containing WP28B2
candidate 84d5324b9944d2de295635472f80913a7506478e.
Pinned source: vidick/MIPRE-formalization at
5926bdff5db621f44682a101007ef2fe3ae8d970 (Lean v4.35.0-rc3).

## Native source index compatibility

MIPRE.GapCompression.completeness/soundness are stated at input
index 2^k, whereas WP28B2's formula encoding lives at index k =
formulaIndex f. These are different index values, and it was NOT
legitimate to silently substitute one for the other.

WP28C_PowerIndex.lean constructs a single original polynomial
source code levelIndexProgram : Cost.PolyTimeFun Nat Nat.
It computes Nat.size n - 1 through original source natBits,
list length, unaryToBin and predN. Exact original Lean proves
levelIndexProgram (2^k) = k for every natural k.

The original fixed source verifier constructed in WP28C_SourceVerifier.lean
runs this genuine index transformation before applying the WP28B2
source native SAT answer checker. Its original source
Cost.PolyTimeFun Data Bool and Prog.HasPolyCost handle arbitrary raw
Data, and are fixed independent of the SAT instance.
A genuine original Verifier 7 via the upstream source wrapper and
actual CL.Sampler 7 is defined. Original Lean proves that for
k = formulaIndex f, an accepted answer at input 2^k is exactly
a satisfying response to the decoded formula f, with Bob's
answer equal to Alice's; the question-length guard is native.

The original source generic upstream sampler cost theorem and
new raw checker HasPolyCost prove existence of one FIXED lam
with Verifier.IsBounded lam for the entire family, not one
source code per formula.

## Genuine source MIPRE GapCompression theorem application

WP28C_Compression.lean proves original source
Verifier.HasPerfectPCC and tensor valStar = 1 for SAT at native
input index 2^k, valStar = 0 for UNSAT under variable scoping.
It then **actually invokes** G.completeness and G.soundness, the
original native GapCompression methods, with all premises explicit:

- G : MIPRE.GapCompression is the real original source structure,
  inhabited in the pinned MIPRE main theorem.
- U : Cost.UniversalMachine is the native original efficient machine.
- k = formulaIndex f is the polynomial-encoded SAT binary index.
- lam is a SINGLE original source IsBounded exponent for the
  ONE fixed power-indexed seven-level verifier, independent of f.
- G.C0 <= k is the ORIGINAL compressor threshold.
- m <= (2^k)^lam is the exact native source answer-budget premise
  for a satisfying assignment on declared m variables.
- Unsatisfiable original f must have f.InputsLt m for global
  rejection of every response, including arbitrary longer strings.

The resulting original compressed verifier is fixed:
G.output (fixedSourceSamplerProg, fixedSourceDeciderProg) lam.
Its source GAME at index k has perfect PCC completeness for
SAT and quantum value at most 1/2 for UNSAT. A final source theorem
existentially chooses ONE lam and gives both implications
universally over all formulas satisfying the visible native
threshold and source witness/scoping hypotheses.

This is not algebraic transport of a surrogate Bell game. Both
the original source verifier input index and the compressor
2^k interface are correctly matched.

## Important complexity and claim limits

WP28B2 proved **2^esize(f) <= formulaIndex f**: the numeric
compressed game INDEX is exponential in SAT input size even though
its binary encoding is linear in that size. The original
GapCompression output query dimension, time bounds and answer
budgets are polynomials in NUMERIC k. The present theorems do NOT
show these are polynomial in the SAT description length.
Constructing the enormous original input index 2^k explicitly
would likewise not be a polynomial SAT reduction, although
the compressed game can be described succinctly by the constant
verifier program pair and binary k.

The compressor threshold and witness-budget premises are
recorded verbatim rather than omitted. The independent WP29 source 3CNF-to-index compiler
is a separate kernel-checked candidate under MATHSOLVE PR #1277,
not yet protected-admitted. Its compiler source obligations are
not silently imported into this WP28C claim.

Consequently, this is a proven ORIGINAL MIPRE compression promise
application in the fixed-program encoded instance regime,
NOT a classical polynomial-time SAT-to-explicit-game reduction,
NOT a polynomial SAT algorithm, NOT a classical lower bound,
and NOT P != NP. Public MATHCERT certification is not claimed.

Named remaining boundary:
PNP_NATIVE_2POWK_COMPRESSION_PROMISE_LOCALLY_PROVED
__SOURCE_SAT_LENGTH_POLYNOMIAL_FULL_GAME_COMPLEXITY_OPEN__EXPLICIT_3CNF_COMPILER_SEPARATE_WP29_CANDIDATE.

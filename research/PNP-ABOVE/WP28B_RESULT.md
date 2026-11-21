# PNP-ABOVE WP28B1 — fixed-code polynomial SAT instance-index bridge

Disposition: original Lean-kernel local candidate. Protected admission only
after full uncached original-source exact-head replay and review.

Protected parent: MATHSOLVE 3ef8c09ecb21392ecf86e23665bc1fdd0733ae73
(WP28A PR #1270 admitted). Original source:
vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970,
Lean v4.35.0-rc3.

## Construction

WP28B_Index.lean constructs a single, source-executable polynomial-time
encoding of ANY original MIPRE.SAT.Fml formula into an original natural
index. It uses a postorder binary serialization of the original
source Fml data, followed by a terminal true-bit sentinel and the
pinned original Cost.PolyTimeFun.bitsValue binary converter:

    indexData(d) = bitsVal(d.toBitsPost ++ [true])
    formulaIndex(f) = indexData(encode f)

A bit-level induction in original Lean proves the last true bit prevents
leading-zero information loss: (indexData d).bits equals exactly
d.toBitsPost ++ [true]. The ORIGINAL Data stack parser ignores the final
unpaired true bit. Hence

    Data.parse (formulaIndex f).bits = encode f

for every original formula f, not only bounded samples.

The result is quantitative:

    Nat.size (formulaIndex f) = esize f + 1
    esize (formulaIndex f) <= 4 * (esize f + 1) + 1.

Thus the binary representation of the index is exactly one bit longer
than the source formula data (the numeric value of the index may be
exponentially large, which is not the relevant encoding cost).

The resulting source index is injective. A separate mathematical
IndexedSAT predicate is proved equivalent to original source SAT
at the exact index, and this equality is instantiated against the
actual original MIPRE.SAT.Cnf3 finite-clause satisfaction relation
via protected WP24.

## Actual original polynomial source programs

serializeData : Cost.PolyTimeFun Data BitStr is built from the PINNED
original Cost.Prog.serProg, serProg_wellScoped and serProg_runs,
with an explicit quadratic original source runtime polynomial.

indexDataProgram : Cost.PolyTimeFun Data Nat composes that original
source serializer with the original polynomial source list-appender
and original binary-index converter.

originalFormulaData reuses the original definitional SAT.Fml
encoding. formulaIndexProgram : Cost.PolyTimeFun SAT.Fml Nat composes
the real source programs. Its code is ONE fixed source program, not
a per-instance hardcode. Lean proves its exact original source run
certificate and equality to formulaIndex for every f.

decodeDataProgram : Cost.PolyTimeFun Nat Data combines the original
natBits and source OracleDecider.parseF normalizer. Lean proves
it restores the EXACT source encoded formula at formulaIndex f and
proves its original polynomial run certificate on arbitrary natural
indices. Both source programs are uniform across all SAT formula
sizes; their PROGRAM DESCRIPTIONS do not grow with f.

## Scientifically distinct uncompleted steps

An exact binary index and source decoder do NOT themselves construct
a fixed-code original source SAT-answer evaluator. IndexedSAT is a
mathematical statement, not a source Cost.Prog/Decider.Accepts at
a native verifier index.

Still OPEN:
- A single fixed source program evaluating original SAT.Fml
  encoded at index n against original answer strings, including
  all malformed data; semantic source proof and global HasPolyCost.
- A real source Verifier 7 around that fixed decider with original
  TimeBoundAt, IsBounded at one fixed lambda across all instances,
  original valStar and compressor promises.
- A source-normalized polynomial-time 3CNF-to-index compiler.
  The current 3CNF transfer is semantic, not a proven original
  PolyTimeFun (List Clause3) Nat compiler.
- Polynomial uniform compression parameter/index accounting and
  any classical SAT-search lower bound, P-versus-NP endpoint or
  external MATHCERT certification.

No P=NP, P!=NP or SAT polynomial search algorithm is asserted.
PNP-001 remains OPEN at MATH-PROGRAMME issue #162.

Next lane:
WP28B2_FIXED_SOURCE_INDEXED_FORMULA_EVALUATOR_AND_VERIFIER7.
Exact boundary:
INDEX_DECODER_PTF_PROVED__FIXED_SOURCE_INDEXED_SAT_DECIDER_OPEN.

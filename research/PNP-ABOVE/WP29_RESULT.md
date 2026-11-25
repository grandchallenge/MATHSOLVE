# PNP-ABOVE WP29 — uniform executable original 3CNF-to-index compiler

Scientific status: kernel-checked original-source candidate. Exact uncached
source replay, protected review and merge remain separate admission gates.
PNP-001 MATH-PROGRAMME issue #162 is OPEN.

Protected parent: grandchallenge/MATHSOLVE
9bdf8c4893f8eebfe551b092e1322db7a334541a.
Pinned source: vidick/MIPRE-formalization at
5926bdff5db621f44682a101007ef2fe3ae8d970, Lean v4.35.0-rc3.

## The actual input language and executable code

An arbitrary finite explicit 3CNF instance is an encoded list of
triples of signed natural-index literals:

    EncLit = Nat x Bool, with true meaning positive
    EncClause = EncLit x EncLit x EncLit
    Enc3CNF = List EncClause

This is a concrete source-serializable finite representation, not
the infinite Set of clauses used in the original semantic Cnf3 type.

The one FIXED original source machine

    formulaProgram : Cost.PolyTimeFun Enc3CNF SAT.Fml

uses genuine original SAT.Fml.inpF, notF, orF, Cost.PolyTimeFun.map
and SAT.andListP. Its .code is closed and its original Prog.Runs
execution has an EXPLICIT polynomial source runtime certificate.
For every length, every clause and every assignment, its output
is the conjunction of exactly the submitted signed clauses,
including the empty conjunction. It produces at most 9m+1 original
Boolean formula gates for m clauses, and at least m gates.

The next original source machine composes this with the admitted
WP28B1 binary index serializer:

    source3CNFIndexProgram : Cost.PolyTimeFun Enc3CNF Nat

Lean proves actual source polynomial execution, closed code and
roundtrip through the original source index parser:
decodeDataProgram(source3CNFIndexProgram cs) = encode(formula cs).
Its output binary numeral has the exact declared formula encoding
length plus one sentinel. Source output length is polynomial
in the original finite 3CNF input encoding size, by the actual
source runtime certificate:

    Nat.size (source3CNFIndexProgram cs)
      <= source3CNFIndexProgram.timeBound.eval (esize cs).

This is BINARY LENGTH, not the numerical value of the index.
The original source also proves the explicit numerical lower bound

    2 ^ cs.length <= source3CNFIndexProgram cs.

Thus the NUMERICAL index is at least exponential in the number of
three-literal clauses, even for short variable indices.

## Original MIPRE 3CNF semantic correspondence

For every n, any list of the source's genuine
MIPRE.SAT.Clause3 (Fin n), and every original finite assignment,
the pure representation bridge fromOriginal3CNF preserves each
source literal sign, every source variable index and all original
clause evaluations. Original Lean proves compiled formula
satisfaction exactly equivalent to MIPRE.SAT.Cnf3.Sat on the finite
set containing those clauses. The compiled formula has
Fml.InputsLt n, so the original UNSAT all-answer rejection premise
is satisfied. Native original IndexedSAT at the compiled formula
index is equivalent to existence of an original Cnf3 witness.

The Fin n / original Set relation is a **proved semantic bridge**.
The executable machine's typed input is Enc3CNF, not an additional
unproved SizedEncoding/PolyTimeFun on the dependent Fin n type
or an infinite set.

## Actual fixed source Verifier 7 and conditional classical transfer

The compiler's index is now linked directly to the PROTECTED WP28B2
single fixed native source MIPRE.Verifier 7, not only to IndexedSAT.
For any finite original MIPRE.SAT.Cnf3 clause list of m variables,
Lean proves the original source verifier has valStar EXACTLY 1 on
SAT (if the response budget is >=m), and valStar EXACTLY 0 on UNSAT
(for every response budget). This is real original unrestricted
quantum-game soundness and PCC completeness, via the actual fixed
source Cost.Prog. These results consume the already-proved original
3CNF variable scoping and witness semantic bridge.

A separate theorem formalizes the ONLY classical computational
inference justified by these facts. For a HYPOTHETICAL program

    oracle : MIPRE.Cost.PolyTimeFun Nat Bool

with an explicitly stated promise that it correctly decides the
value-one question for this original fixed indexed source verifier
on all properly scoped SAT formulas with sufficient response budget,
then the REAL original Cost.PolyTimeFun composition

    conditionalSATProgram oracle : PolyTimeFun Enc3CNF Bool

would decide original finite 3CNF SAT in polynomial time. The
polynomial source execution certificate is separately exhibited.
The crucial oracle is a VISIBLE PREMISE, NOT CONSTRUCTED.
This proves a conditional source-polynomial many-one reduction;
it does NOT prove SAT in P, does not produce efficient SAT
witnesses, and does not establish a classical lower bound.

## What follows, and what DOES NOT follow

PROVED: One fixed polynomial original Cost.Prog for all encoded
finite 3CNF instances, exact original Cnf3.Sat semantics,
source 9m+1 gate bound, valid variable scoping, original binary
index roundtrip and an input-length polynomial index-encoding cost.

NOT PROVED: An entire compressed GAME computable or enumerable in
time polynomial in SAT input length, or a polynomial bound on the
NUMERIC game index. The admitted original index is numerically at least
2^(esize f), and our new theorem gives >=2^m for m clauses;
original GapCompression resource bounds
are polynomial in numeric index, not automatically binary length.
Also NOT proved: polynomial classical SAT witness search,
classical computational lower bounds, P=NP, P!=NP or
independent public MATHCERT certification.

Protected WP28B2 (#1273, b0e9acce5cffa8aeff5e7a6fd9e7f20970ea9602)
and protected WP28C (#1274, 9bdf8c4893f8eebfe551b092e1322db7a334541a)
now supply the fixed source Verifier 7, 2^k-index compatibility and
actual GapCompression promises. Our WP29 source explicitly imports
the admitted native WP28B2 value theorem and independently replays
all WP28C predecessor modules. Their composition still does NOT
establish polynomial full-game resources in 3CNF description length.

True boundary:
SOURCE_EXPLICIT_3CNF_TO_INDEX_POLYTIME_PROVED
__NUMERIC_GAME_INDEX_FULL_GAME_RESOURCE_POLYNOMIALITY_OPEN.

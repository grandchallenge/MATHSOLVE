# PNP-ABOVE WP29 — uniform executable original 3CNF-to-index compiler

Scientific status: kernel-checked original-source candidate. Exact uncached
source replay, protected review and merge remain separate admission gates.
PNP-001 MATH-PROGRAMME issue #162 is OPEN.

Protected parent: grandchallenge/MATHSOLVE
847150699031e80ab0d6077663321e307929acad.
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
Boolean formula gates for m clauses.

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

## What follows, and what DOES NOT follow

PROVED: One fixed polynomial original Cost.Prog for all encoded
finite 3CNF instances, exact original Cnf3.Sat semantics,
source 9m+1 gate bound, valid variable scoping, original binary
index roundtrip and an input-length polynomial index-encoding cost.

NOT PROVED: An entire compressed GAME computable or enumerable in
time polynomial in SAT input length, or a polynomial bound on the
NUMERIC game index. The admitted original index is numerically
at least 2^(esize f); original GapCompression resource bounds
are polynomial in numeric index, not automatically binary length.
Also NOT proved: polynomial classical SAT witness search,
classical computational lower bounds, P=NP, P!=NP or
independent public MATHCERT certification.

Pending WP28B2 and WP28C may supply source fixed Verifier 7 and
2^k compressor promises, respectively. They are separate pending
admissions and do not establish the missing full-game complexity
transfer on their own.

True boundary:
SOURCE_EXPLICIT_3CNF_TO_INDEX_POLYTIME_PROVED
__NUMERIC_GAME_INDEX_FULL_GAME_RESOURCE_POLYNOMIALITY_OPEN.

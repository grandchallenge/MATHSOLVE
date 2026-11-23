# WP29 — independent logical review and scientific boundary

Verifier (native source): The input is an arbitrary encoded finite
list of signed natural-index triples. The ONLY executable algorithms
are actual original MIPRE Cost.PolyTimeFun constructions with fixed
closed .code and an explicit polynomial .timeBound, composed from
original formula constructors, map, and fold. The source is original
MIPRE.Fml and original WP28B1 formulaIndexProgram.

Adversary (SAT semantics): Original positive/negative literal
semantics are verified for every natural variable index. The empty
3CNF has truth value true, consistent with original Cnf3.Sat.
For every original source Clause3 (Fin n) the representation bridge
preserves signs and indices; the proved original Cnf3.Sat relation
is equivalent to the generated original SAT.Fml and original
IndexedSAT. No source formula reads undeclared variables. Original
gate count is <= 9*m+1, including the true terminal and AND gates.

Adversary (uniformity and cost): The SAME original source program
works for every encoded input and runs in source polynomial time.
This is more than a semantic Lean map. The binary length of its
numeric index is at most its actual original Cost.Prog runtime
polynomial. It DOES NOT bound the numerical index by a polynomial
in input length, nor bound full compressed game resource costs.

Referee: internal bounded result is an executable polynomial
explicit-3CNF-to-index compiler with genuine original Cnf3
satisfiability correspondence. It does NOT prove the missing
full-game polynomial SAT reduction, an efficient classical
SAT witness search algorithm or P-vs-NP lower bound. No external
review or independent MATHCERT certification is claimed.

Admissibility gate: exact locked source bytes and Git blob, hostile
mutations rejected, full UN-CACHED predecessor recompile, new
original Lean axiom audit of all 25 public theorem declarations,
protected CI checks and exact protected merge readback.

The additional kernel-checked theorem says 2^m <= the compiled
numeric index for every m-clause explicit 3CNF. This is a bound
on the present encoding, not on all possible reductions.

The original fixed source Verifier 7 (WP28B2, independently
admitted) is now directly instantiated at the compiled 3CNF index:
SAT gives true native quantum valStar=1 and UNSAT gives native
valStar=0. Source conditionalClassicalSATTransfer assumes a genuine
original polynomial-time game-value oracle and concludes a
polynomial original Cost.Prog SAT decider. This is a legitimate
IF-THEN classical complexity transfer; the antecedent and any
P-versus-NP complexity separation are NOT proved.

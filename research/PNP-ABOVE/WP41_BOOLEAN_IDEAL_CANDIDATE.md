# SCC research candidate: Boolean quotient ideals and generator-extension syzygies

Scope: elementary mathematical derivation and finite verification, not native Lean admission, MATHCERT certification, a proof-system simulation or a P versus NP result. This note is conceptually downstream of the WP40 semantic-capacity candidate, whose formal replay is still open. It does not assume the WP40 candidate theorem.

## Boolean violation ideal

Let R = F_2[x_1,...,x_n]/(x_i^2-x_i). This ring identifies with all Boolean functions on {0,1}^n by evaluation: the point indicator products form a basis. All elements are idempotent. Write c_i for the violation function of clause i, and v = 1 + product_i (1+c_i) for the violation function of the conjunction. For m=0 use empty product 1. The telescoping identity is

    v = sum_i c_i product_{j<i}(1+c_j).

Each c_i v = c_i, since c_i(1+c_i)=0. Thus I=(c_1,...,c_m)=(v). R/I is canonically the ring of functions on satisfying assignments, with F_2 dimension equal to their number. A function g belongs to I iff gv=g, iff it vanishes on every satisfying assignment. This is exact and does not require a chosen generator presentation.

## A uniform candidate coefficient vector

For any Boolean circuit g define a_i = g product_{j<i}(1+c_j). These coefficients are computable as a shared Boolean circuit DAG in time and total gate count linear in the input circuit description and m, allowing fan-out and counting wiring and output references (or polynomial size without sharing). The same construction works whether or not g is entailed to vanish. Its residual is

    g + sum_i a_i c_i = g(1+v).

Consequently the vector is a valid ideal-membership representation exactly when the original entailment holds. In particular for g=1 the identity sum_i a_i c_i=1 holds exactly when the formula is UNSAT. The compiler produces the candidate without deciding UNSAT. Verifying its identity on succinct Boolean circuits is coNP-complete: membership in coNP follows by a counterexample assignment, and CNF-UNSAT reduces through this explicit vector with g=1. This is not a polynomial-time checkable proof system.

No lower bound on circuit size of ideal-membership coefficients alone can separate UNSAT families here: every unsatisfiable CNF already has this uniformly constructible polynomial circuit-size representation. Expanded monomials, degree restrictions, restricted certificate systems, and costs of proving the identity are different resources.

## Presentation extension and syzygy transport

Write phi: R^m -> R, phi(b)=sum_i b_i c_i, and K=ker(phi). If g=phi(a), append g as generator, giving phi'(b,t)=phi(b)+tg. The shear

    (k,t) -> (k+ta,t)

is an explicit R-linear isomorphism K ⊕ R -> ker(phi'); inverse (b,t) -> (b+ta,t). Over F_2 the same shear is its own inverse. Thus a redundant consequence preserves the ideal and quotient but changes the presentation kernel by a split free summand. No new syzygy obstruction arises solely from this redundant generator if arbitrary ring coefficients are allowed. For a tautological added clause g=0 choose a=0; this directly parallels the semantic redundancy of WP40, without asserting the two representations have identical operational cost.

A global decomposition also follows without assuming g is a consequence: the residual above expresses the exact obstruction to the proposed shear carrying K ⊕ R into the new kernel; phi'(k+ta,t)=t g(1+v). For arbitrary g, the old ideal is enlarged unless this residual vanishes identically.

## Research consequence

Structural Capacity Calculus cannot merely count ideal generators, unrestricted syzygy coefficient circuit size, or stable presentation-kernel invariants and interpret them as unrestricted algorithmic time. The relevant distinction is between a cheap symbolic candidate, an efficiently verifiable evidence of its correctness, and discovery of a satisfying assignment. The next admissible target is an invariant of *uniform executable transformations with charged verification/discovery*, or a justified extraction theorem from arbitrary classical computations into a resource-bounded algebraic representation. No such unrestricted extraction theorem or superpolynomial lower bound is asserted.

## Verification

The companion WP41_BOOLEAN_IDEAL_CHECK.py checks every list of 0–3 Boolean violation functions and every g on two variables, and all shear input vectors for two generators on one variable, including nonconsequences. It exercises exact identities in the finite truth-table ring; it does not certify the general proof or the native computational model. General arguments above are elementary pen-and-paper derivations. Native Lean formalization, source-semantic concordance, protected review and public publication remain open.

# WP42 — Canonical residual-lift equivalence for Boolean CNF IPS

Status: pen-and-paper candidate theorem; not protected admission, native Lean verification, novelty claim, or P versus NP result. Extends WP41 independently of WP40's unverified theorem.

## Source concordance
- Grochow–Pitassi, arXiv:1404.3820v1, Definition 1.1, Lemma 1.12, Theorem 3.1; journal DOI 10.1145/3230742, sections 4 and 6. https://arxiv.org/html/1404.3820v1
- Forbes–Shpilka–Tzameret–Wigderson, Theory of Computing 17(10), 2021, Proposition 4.4(2), sections 4.2–4.3. General circuit IPS to linear IPS with polynomial overhead over any field; efficient lifts for restricted models. https://theoryofcomputing.net/articles/v017a010/
- Grochow, arXiv:2306.02184v1, PIT in NP iff IPS p-simulation by a Cook–Reckhow system. https://arxiv.org/html/2306.02184v1
- ECCC TR26-070, Hard CNF Instances for Ideal Proof Systems: recent CNF lower bounds specifically for roABP-IPS, not unrestricted circuits. https://eccc.weizmann.ac.il/report/2026/070/

These are version/edition bibliographic pins, not acquired byte hashes. The following direct derivation does not import an unproved external theorem. General-to-linear simulation is established prior work, not claimed new.

## Ordinary polynomial ring

Over any field K let A=K[x_1,...,x_n], b_j=x_j^2-x_j, J=(b_1,...,b_n). Each c_i is the ordinary product of falsity literals x_j or 1-x_j of a clause. Allow empty clauses and repeated literals. Let N count input description (including n), L the number of literal occurrences. Put S=prod_i(1-c_i), the satisfaction polynomial. The formal identity 1-S=sum_i a_i c_i holds for a_i=prod_{h<i}(1-c_h). The image of S in A/J is the indicator of satisfaction, hence S in J iff CNF is UNSAT: every polynomial has a unique multilinear representative by reducing powers; a multilinear polynomial vanishing on the cube is zero by induction on variables, evaluating at 0 and 1.

## Theorem (canonical residual-lift equivalence)

Measure arithmetic DAG size with sharing, input nodes, output references, binary addition/subtraction/multiplication and field constants; over F2 all constants have fixed bit cost. Let R(F) be minimum size of a shared circuit outputting H_1,...,H_n with S=sum_j H_j b_j. Let I(F) be minimum size of an IPS circuit C(x,y,z) with C(x,0,0)=0 and C(x,c,b)=1. Empty certificate sets have infinite cost. For UNSAT F, these quantities are polynomially related, with uniform polynomial-time circuit transformations both ways over F2 (or field-operation model over K). For SAT F neither exists. With polynomial degree certificates, both transformations preserve polynomial degree of the output certificate polynomials.

Forward: append explicit clause-prefix coefficients to H; C=sum_i a_i y_i + sum_j H_j z_j. Shared circuit overhead O(N).

Reverse step 1: obtain linear coefficients U_i,V_j from any IPS C using division-free gate propagation (direct reconstruction of the known circuit linearization). For each gate g maintain g^0=g(x,0,0), g^1=g(x,c,b) and vector D_g with g^1-g^0=D_g dot (c,b). Leaves: unit vector for placeholder, zero vector for x/constant. Sum/difference: componentwise. Product u*v: D_g=u^1 D_v+v^0 D_u. This gives 1=sum_i U_i c_i+sum_j V_j b_j with O((m+n)|C|+N) arithmetic gates, without testing or expanding the certificate.

Reverse step 2: construct a small formal lift for each clause's Booleanity defect c_i(1-c_i). For a falsity literal l, l^2-l=b_j for either l=x_j or l=1-x_j. For products uv:
 (uv)^2-uv = v^2(u^2-u)+u(v^2-v).
Thus c_i^2-c_i=sum_j E_ij b_j by a linear chain of vector updates, with shared size O(n L+N), including sign reversal for c_i(1-c_i). Then
 S c_i=c_i(1-c_i) prod_{h != i}(1-c_h)=sum_j W_ij b_j.
Prefix/suffix products give all excluded products at linear overhead. Empty products and repeated literals obey the same identities.

Multiply the linear refutation by S:
 S=sum_i U_i S c_i+sum_j S V_j b_j
  =sum_j (S V_j+sum_i U_i W_ij)b_j.
These are H_j. Overhead O(n L+nm+(m+n)|C|+N), up to input representation. Thus clause coefficients can be fixed canonically; all remaining certificate complexity resides in lifting one explicit satisfaction polynomial through the Boolean ideal. No claim that H is efficient without an IPS certificate.

Degree note: for a degree-bounded input C, use telescoping substitution over placeholders: consecutive partial substitutions differ by the next placeholder times an exact divided difference. Compute this quotient by the above gate propagation with a single formal placeholder (before substituting the corresponding axiom); the degree of the quotient polynomial is at most degree(C)-1 before axiom substitution. Substitution multiplies degree by at most max(1,max_i deg c_i,2). The size remains polynomial. This gives polynomial degree for output certificate polynomials, not a syntactic degree bound on every gate. Without degree restrictions use the direct vector recurrence.

## Distinct complexity barriers

The quotient reduction S -> 0 on UNSAT formulas is coNP-complete to recognize on succinct inputs. The top coefficient of the multilinear representative over F2 is sum_{a in {0,1}^n} S(a), i.e. parity of #SAT. Summing all monomial evaluations, only the full-support monomial contributes odd parity. Thus generic coefficient extraction contains parity counting despite S having a short circuit. This does not prove circuit-size lower bounds for the whole multilinear polynomial.

A polynomial uniform algorithm outputting valid polynomial-size, polynomial-degree residual lifts on every UNSAT CNF (total runtime on all inputs) would put SAT in RP, provided output degree is polynomially bounded on all inputs (or enforce a syntactic bound): randomized polynomial identity testing over a sufficiently large extension of F2 checks the residual equality. Valid UNSAT inputs always pass, SAT inputs have nonzero residual for every purported lift and reject with high probability. Accept SAT precisely when verification rejects; malformed outputs reject. Hence NP=RP. Alternatively standard PIT for arbitrary arithmetic circuits over finite fields handles exponential degree via polynomial-bit extension sizes. This is not a proved converse. With deterministic polynomial verification the generator would put SAT in P.

The unrestricted classical computation-to-certificate extraction theorem remains OPEN. A polynomial-time decider's single rejecting trace is not a proof of correctness over all assignments. Known general-to-linear IPS equivalence does not supply such extraction. A superpolynomial lower bound on R(F) would imply the corresponding IPS circuit-size lower bound and the applicable algebraic complexity consequence, not directly P!=NP.

## Next task

Study the affine coset {H: sum H_j b_j=S} and an algorithm-to-lift extraction under explicit correctness-proof assumptions. Compare restricted roABP results against class preservation; the circuit transformation need not preserve restricted classes. Companion test uses exact F2 ordinary-polynomial arithmetic, with no automatic Boolean reduction in identity checks. No asymptotic lower bound or certification asserted.

## Finite verification receipt

`python3 WP42_RESIDUAL_LIFT_CHECK.py`: CNFs=820; UNSAT=361; perturbed general/linear reverse lifts=722; arbitrary gate-vector identities=1000

## Exact residual syzygy space

For fixed n, the map B:A^n -> A given by H -> sum_j H_j b_j is independent of F. Its kernel is generated by the n(n-1)/2 elementary Koszul relations b_i e_j-b_j e_i, since b_1,...,b_n is a regular sequence. Direct proof: modulo (b_1,...,b_{n-1}), b_n is monic in the still-free variable x_n, hence is not a zero divisor even if the coefficient ring has zero divisors. Thus a relation H satisfies H_n in (b_1,...,b_{n-1}); write H_n=sum_{i<n} t_i b_i. Subtract sum_{i<n} t_i(b_i e_n-b_n e_i), leaving a relation on the first n-1 coordinates. Induct, with n=1 following from monicity and n=0 trivial. The argument works with the remaining variables as coefficient-ring variables at each step.

For UNSAT F and any particular lift H^0, the complete certificate family is
    H^0 + sum_{i<j} T_ij (b_i e_j-b_j e_i),   T_ij in A.
All generators are fixed, degree two, and explicitly available in polynomial description size. Hence neither the number nor degree of syzygy generators of this residual module can distinguish different CNFs on the same variables. All instance-specific difficulty is in finding a small circuit in the affine fiber over S_F; the affine fiber is not the kernel. Existence of short generator descriptions provides no efficient choice of T_ij, nor an efficient circuit representation for H^0. This is an elementary Koszul fact applied to the candidate residual equivalence, not a novel general syzygy theorem.

## Coordination with admitted SCC-001 source

Current protected MATHSOLVE ba8f4e6b587ab1ca4f01f0b63037d77ef09476f9 contains research/SCC-001/SYZYGY_TRANSPORT.md, concerning the colon quotient and correction differential of a Boolean *gate-state* filtration, a distinct algebraic object. Its spectator-amplification counterexample rules out raw correction rank as polynomial per-gate potential. WP42's fixed Boolean-ideal kernel is a different obstruction: the kernel itself is instance-independent. No identification between these two modules is asserted. A useful next target must distinguish the affine fiber or the actual executable acquisition process, not just count relations of the ambient module.

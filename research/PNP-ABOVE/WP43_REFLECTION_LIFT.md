# WP43 — Exact residual reflection and the cheap-rejection obstruction

Author-derived mathematical candidate, not independent certification or novelty claim. Builds on WP42 and the established reflection-principle method of Jan Krajicek, A note on SAT algorithms and proof complexity, IPL 112 (2012), Theorem 2.1, https://www2.karlin.mff.cuni.cz/~krajicek/sat.pdf . The source theorem transfers proof-size lower bounds to algorithms with feasibly provable soundness, not arbitrary correct algorithms. Our direct polynomial argument isolates the soundness-certificate cost for the WP42 residual model. Bibliographic source identity only; no byte lock for the paper.

## Setup

Work over F2, with instance bits u=(u_1,...,u_q), witness bits x=(x_1,...,x_n), optional trace bits w, and Boolean axioms b(v)=v^2-v. Use a polynomial-size universal CNF satisfaction circuit V(u,x) whose specialization at any valid code a is exactly the ordinary satisfaction polynomial S_F(x), not merely equivalent on Boolean points. For example, a clause-slot encoding with 2n presence bits per clause has factor c_i=prod_j (1-u_ij^+(1-l_j^+))(1-u_ij^-(1-l_j^-)), where l_j^+=1-x_j and l_j^-=x_j are falsity literals. At fixed bits each absent literal contributes 1 and each present literal its falsity polynomial. V=prod_i(1-c_i). This encodes all clauses without repeated literals; ordinary repeated-literal syntax can alternatively use explicit one-hot slots. Padding is by a tautological clause, whose satisfaction polynomial is not identically 1 off the cube, so exact specialization uses the actual padded formula.

Let R(u,w) be an arithmetized Boolean circuit recognizing rejecting computations, including input validity where needed. Soundness of rejection means R(a,t)V(a,x)=0 for all Boolean a,t,x. Thus there exists a formal residual certificate
 R(u,w)V(u,x)=sum_i A_i b(u_i)+sum_k B_k b(w_k)+sum_j H_j b(x_j).
Existence follows from Boolean quotient completeness, not an efficient construction.

## Theorem 1: exact reflection specialization

For any actual Boolean rejected code/trace pair (a,t), substitute u=a,w=t into the above formal equality. All instance and trace Boolean axioms vanish identically; R(a,t)=1 as a field constant. Exact V specialization gives
 S_F(x)=sum_j H_j(a,t,x)b(x_j).
Circuit specialization is a linear-description-time graph relabeling and output selection, and does not increase gate count except for optional constant nodes. If the rejecting computation has length T and the soundness lift has circuit size polynomial in |F|+T, WP42 gives a polynomial-size IPS refutation with that bound. Uniform extraction given the soundness circuit and trace is polynomial; no uniform production of that circuit follows. For a globally correct time-bounded solver, superpolynomial residual lower bounds therefore imply that either the time or the corresponding reflection-lift size is not polynomially bounded. The latter alternative cannot be deleted.

## Theorem 2: exact singleton rejection equivalence

Fix a code a for F. Let E_a(u)=prod_i e_i(u_i), where e_i=u_i if a_i=1 and e_i=1-u_i if a_i=0. This is a size O(q) equality-test rejection circuit, rejecting exactly a on Boolean inputs. It is a sound partial rejector iff F is unsatisfiable. No claim of complete SAT decision.

Define C_a as the minimum circuit size of a lift of E_a(u)V(u,x) through all u and x Boolean axioms; define C_F as WP42's minimum residual-lift size for S_F. For UNSAT F these minima are polynomially related, and for SAT F neither exists.

Lower direction: specialize u=a as in theorem 1.

Upper direction: for any polynomial circuit V, construct difference coefficients D_i with
 V(u,x)-V(a,x)=sum_i (u_i-a_i)D_i(u,x).
Use a gate-vector recurrence storing g(u,x),g(a,x),D_g; variables u_i get coordinate unit vectors, other leaves zero; product uv has difference vector u^1 D_v+v^0 D_u. Size O(q |V|), sharing subcircuits. Since
 E_a(u)(u_i-a_i)=sigma_i b(u_i) prod_{h != i} e_h(u_h),
where sigma_i=1 if a_i=1 and -1 otherwise, multiplying the difference equality by E_a gives a known small lift of the difference. If S_F=sum_j H_j b(x_j), then
 E_a V=sum_i [sigma_i D_i prod_{h != i}e_h] b(u_i)
      +sum_j E_a H_j b(x_j).
Prefix/suffix products supply all excluded factors with linear overhead. This is a uniform polynomial-size construction given a residual lift, not a way to find it without one. All equalities are ordinary polynomial identities over any field; the uniform bit model here is F2.

Consequently even a very small sound partial rejection circuit can have reflection-certificate complexity exactly as hard (up to polynomial overhead) as its rejected instance. This is not a demonstrated superpolynomial example; it is an equivalence. A short rejecting trace is no substitute for evidence that rejection is sound.

## Corollary: explicit-family obstruction to pointwise runtime transfer

Let F_k be a polynomial-time constructible UNSAT family with size at least k. A single uniform polynomial-time partial rejector can recognize exactly those family members of a given input size N by constructing F_1,...,F_N and comparing encodings. It is sound by the hypothesis. A globally correct SAT algorithm can also reject this family in polynomial time by this preliminary test and use exhaustive search elsewhere. Thus a pointwise bound on residual complexity by actual runtime of every globally correct (possibly non-polynomial-time elsewhere) SAT algorithm would force polynomial-size residual lifts for every such explicit UNSAT family. Any explicit family proving superpolynomial residual/IPS size would refute that blanket runtime transfer. This does not exclude worst-case complexity bounds for globally polynomial algorithms.

## Next decisive obligation

A uniform unrestricted extraction theorem must exploit more than runtime and semantic soundness of a rejecting computation. Either prove polynomial-size reflection lifts for every hypothetical polynomial-time complete SAT decider (not assumed here), or pursue a different lower-bound mechanism insensitive to the missing soundness proof. This is the same fundamental gap identified by Krajicek's reflection method. No P!=NP, NP!=coNP, or unrestricted IPS lower bound is established.

## Finite and formal verification scope

Independent sparse ordinary-polynomial replay over F2, F3 and F5: all 48 presence-bit encodings checked, including 27 unsatisfiable singleton reflection certificates and 21 SAT controls; signs and specialization checked without implicit Boolean reduction. WP41/42 predecessor finite regressions also passed. WP43_ReflectionCore.lean covers six generic commutative-ring lemmas: bit Booleanity, selector delta, multiplication difference propagation, finite selector-product delta, singleton lifting and ring-hom specialization. The circuit gate-count analysis, universal CNF encoding and uniform algorithm corollary remain paper arguments, not claims of Lean formalization. WP43_REPLAY.py binds exact source and dependency pins and audits all six declarations.

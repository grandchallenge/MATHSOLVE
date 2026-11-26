# WP44 — Circuit-to-CNF residual lifting and the exact feasible-reflection boundary

Author-derived candidate, following WP42–43; no novelty or certification claim. Over F2, with ordinary polynomial identities (no implicit Boolean quotient). Arithmetic circuits are shared DAGs, not expanded formulas. A residual lift of a Boolean circuit polynomial g means g=sum_i H_i(x)(x_i^2-x_i).

## 1. Exact gate extension elimination

Let C be any Boolean circuit of size s on n input bits, using AND, NOT, constants. Use a fresh z for each gate and standard Tseitin CNF F_C, including the assertion that the output is true. Write a,b for predecessor wire variables/constants. For AND the three clause falsity polynomials are
 c1=z(1-a), c2=z(1-b), c3=(1-z)ab.
Their formal combination is z-ab=c1+a c2-c3.
For NOT the two are c1=za, c2=(1-z)(1-a), with z-(1-a)=c1-c2.
Constant gates can be substituted at the start or represented by unit clauses.

Let g_v(x) denote the recursively arithmetized value of wire v. Under substitution z_v=g_v(x), every wire Booleanity defect is a small linear combination of input Boolean axioms. Indeed
 b(uv)=v^2 b(u)+u b(v), b(1-u)=b(u),
where b(t)=t^2-t. Each input starts with its unit coefficient vector and constants with zero. Shared coefficient circuits cost O(ns+s+n).

After substitution the AND gate clauses are -g_b b(g_a), -g_a b(g_b), -b(g_a g_b); the NOT clauses are both -b(g_a). Thus all gate-clause falsities and all wire Boolean axioms have explicit small input-Boolean-ideal lifts. No corresponding claim holds for the output assertion, whose falsity polynomial is 1-g.

## 2. Equivalence of residual cost and Tseitin IPS

Assume C has no Boolean input with output 1, and put g=g_out. The minimum arithmetic circuit size of a residual lift of g is polynomially equivalent to minimum unrestricted circuit-IPS refutation size of F_C, with polynomial overhead in n+s. If C has a satisfying input, neither certificate exists.

Reverse (IPS -> residual). WP42's circuit-linearization recurrence applies to the whole Tseitin system. Substitute all z_v=g_v. All axioms except the output clause have the explicit lifts above. We obtain
 1=U(x)(1-g(x))+sum_i A_i(x)b(x_i).
Multiplying by g gives
 g= -U b(g)+sum_i g A_i b(x_i).
Insert the small Booleanity lift of g to obtain the residual certificate. Composition uses one shared copy of the gate DAG.

Forward (residual -> IPS). Keep the z wires. Compute for each wire an explicit linear combination of gate clause falsities equal to z_v-g_v. For an AND gate,
 z_v-g_a g_b=(z_v-z_a z_b)+z_a(z_b-g_b)+g_b(z_a-g_a).
For NOT use z_v-(1-g_a)=(z_v-(1-z_a))-(z_a-g_a). For an input the difference is zero. The displayed exact local gate identities give the first term. Propagating coefficient vectors over the O(s) clause set costs O(s^2) gates with sharing. Then the identity
 1=(1-z_out)+(z_out-g)+g
 is a linear IPS certificate after insertion of the residual lift. The output can also be an input or constant, with the same identity and zero wire difference. This proof works over any field; uniform bit-size claim uses fixed F2.

No claim that conversion preserves roABP width, formula size, constant depth, or degree restrictions. For unrestricted circuits the two directions preserve polynomial gate-count bounds.

## 3. Exact feasible-reflection condition

Let B mean that general F2 circuit IPS is polynomially bounded on all unsatisfiable CNFs (no uniform proof generation demanded). Let D be any deterministic polynomial-time complete SAT decider, if one exists. Use a polynomial-size rejecting-output Boolean circuit R_N(u), with exact input-validity test as needed, for each fixed size/shape, and the canonical polynomial-size SAT verifier V_N(u,x) of WP43. For a complete correct D, R_N V_N vanishes on the Boolean cube. Let F_D mean that these universal soundness residual lifts have polynomial-size arithmetic circuits (uniform over supported shapes; coefficients may be nonuniform).

* B -> F_D for every such D: compile the Boolean circuit R_N AND V_N to its Tseitin CNF, apply B, then eliminate wire extensions by section 2. The resulting residual polynomial is the actual arithmetization R_N V_N, not a merely Boolean-equivalent alternative. The arithmetization uses AND/NOT basis; choose the verifier from WP43 with exactly this basis and presence-bit encoding.
* F_D -> B for any one complete polynomial-time D: specialize the soundness certificate at any UNSAT input by WP43, producing a polynomial-size residual lift of its exact satisfaction polynomial, then invoke WP42. The presence-bit CNF encoding covers all clauses without duplicates with polynomial overhead. Repeated literal occurrences can be retained with a padded list-slot encoding, or removed: either encoding is allowed if the exact specialization is respected. For direct coverage of arbitrary ordinary CNF syntax use slots with one-hot choice among absent and each signed literal, with selected factor constructed by a product of gated falsity literals, including duplicates. Fixed padded clause count can use disabled clauses or represent the actual padded instance; no semantic-only substitution is allowed.

Thus **conditional on P=NP**, existence of a complete polynomial-time SAT decider with polynomially bounded reflection lifts is equivalent to polynomial boundedness of general circuit IPS. In fact under B every complete polynomial-time decider admits the stated size bounds. The forward direction uses no P=NP except for the existence of such a decider. It does NOT give efficient uniform production of lifts; that is a stronger search problem. No claim that P=NP itself implies B, or that not-B implies P!=NP. No unrestricted IPS lower bound is proved.

This rules out treating feasible reflection as a minor implementation lemma. It is already equivalent, under the hypothetical algorithm assumption, to a major proof-complexity boundedness statement. Krajicek's reflection-principle framework (2012, Theorem 2.1) is the established precedent; the direct gate-extension proof here makes the exact condition transparent in the WP42 residual model.

## 4. Next target

Seek a lower bound on computational states that does not assume polynomially bounded IPS under P=NP, or prove the missing implication using independently justified mathematics. Restricted IPS lower bounds do not by themselves supply this. No further syzygy-count or mere encoding lower bound closes it.

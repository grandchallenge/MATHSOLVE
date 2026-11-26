# SCC-001: Graded promotion and its capacity

**Status:** author-derived propositions; bounded exact regression; not independently reviewed, Lean-certified or novelty-certified. [Live tracker](https://github.com/grandchallenge/MATHSOLVE/issues/1309). [Pedagogy PR](https://github.com/grandchallenge/MATH-PROGRAMME/pull/3770).

## 1. Model and promotion law

Let B be the algebra of Boolean functions on n binary inputs over the binary field. Let V be a linear subspace containing the constant one and all coordinate functions. An unrestricted charged step adjoins g = uv for u,v in V, producing V'. All affine operations are free; this is multiplicative complexity. Ordinary polynomial-size Boolean circuits are equivalent to polynomial multiplicative complexity up to polynomial overhead: a gate operand is an affine combination of at most n+s+1 stored bits after s multiplications, and can be evaluated using that many XOR gates. Consequently, a superpolynomial multiplicative-complexity lower bound for total encoded SAT would imply NP is not contained in P/poly. No such lower bound is proved here.

Let $F_r$ be the linear span of products of at most r elements of V, with constants at grade zero and negative grades zero. Denote the associated graded algebra by $A=\bigoplus_r A_r$ with $A_r=F_r/F_{r-1}$.

For all $r\geq 1$,

$$
F'_r=F_r+gF_{r-1}.
$$

Expand products of elements of V'. Since g is Boolean, every positive power of g equals g. Every expanded summand belongs to the right side, and the reverse inclusion follows directly from the product counts. In particular, $F_r\subseteq F'_r\subseteq F_{r+1}$.

Write q for the symbol of g in grade two. Multiplication by q maps grade j into grade j+2. The identity on B induces a graded linear map from A to A'. For each $r\geq 1$ there is an exact sequence

$$
0\to qA_{r-2}\to A_r\to A'_r\to qA_{r-1}\to0.
$$

Indeed the kernel is $F'_{r-1}/F_{r-1}=qA_{r-2}$, and the cokernel is $F'_r/F_r=qA_{r-1}$. The last map takes the old symbol in grade r+1. In grade zero both old and new graded spaces are constants. Define $H_r=\dim A_r$ and $R_j=\dim(qA_j)$, with negative indices zero. Then

$$
H'_r-H_r=R_{r-1}-R_{r-2}.
$$

For a target with relative degree d at least one, its degree decreases by one if and only if its old leading symbol belongs to $qA_{d-2}$. No greater decrease is possible. A family of leading symbols is jointly promoted if and only if its span is contained in the same image. The formulas also hold when a gate is redundant.

## 2. Sharp universal one-gate ceiling

For any operands u,v, define four functions by choosing either u or 1+u and either v or 1+v, and multiplying the chosen pair. These are indicators of the four joint-value cells. They differ from g by elements of V, so each induces the same map on A of degree two, multiplication by q. The sum of the ranks on all grades is at most the rank of any of the corresponding multiplication operators on B: choose representatives whose nonzero output symbols are independent grade by grade. Their actual outputs are independent, by considering the highest occupied grade in a putative dependence.

The rank of multiplication by an indicator on B equals its support size. The four cells partition all input points. Thus for every V and every legal gate,

$$
\sum_{j\geq0}R_j\leq\min_{a,b\in\{0,1\}}|\{x:u(x)=a,\ v(x)=b\}|\leq 2^{n-2}.
$$

For n at least two this is sharp. At the initial affine state, the graded algebra is the exterior algebra on the n coordinate symbols over the binary field: square-free monomials of degree r form a basis in grade r. With g = x1*x2, multiplication by q gives distinct basis vectors for the monomials avoiding both variables and zero for all others. Thus

$$
R_j=\binom{n-2}{j},\qquad \sum_jR_j=2^{n-2}.
$$

This rules out a polynomial per-gate ceiling for the unweighted count of independent promoted directions. The exponential capacity is due to reuse of a shared factor, not a computational lower bound. For example, the total degree-weighted Hilbert mass decreases by precisely the sum of the R_j (telescope the dimension law), and its maximum initial mass is n times 2^(n-1); dividing by the sharp uniform ceiling yields at most 2n, not a superpolynomial lower bound.

## 3. Joint promotion criterion and its failure after reuse

In the initial exterior algebra on the coordinate vector space E, take a nonzero subspace W of grade d, with d at least two. Define its common linear annihilator

$$
K(W)=\{a\in E:a\wedge w=0\text{ for every }w\in W\}.
$$

One charged gate can promote all its leading symbols if and only if dim K(W) is at least two. Necessity: if W lies in the image of multiplication by a nonzero decomposable q = u wedge v, then u,v are independent and annihilate every element of W. Sufficiency: choose independent u,v in K(W) and extend them to a basis of E. In the square-free basis, being killed by multiplication by u is exactly being divisible by u; similarly for v. Both conditions force divisibility by their product. This proof works in characteristic two.

At later reachable states the same annihilator test is necessary but no longer sufficient. Example: four input coordinates, with y = x1*x2 adjoined to the affine space. In grade two of the resulting algebra, let W be spanned by the symbols of y*x3 and y*x4. They are independent because their distinct cubic truth-table monomials cannot lie in the degree-one space. The symbols of x1 and x2 both annihilate W (their products with y equal y as Boolean functions, so the degree-three leading symbols vanish). Yet no single q can promote W: the image q*A_0 has dimension at most one. This identifies a concrete failure of the naive exterior divisibility criterion under nonlinear reuse, even on four input bits.

## 4. Replay and next test

Run node research/SCC-001/replay.js. The deterministic exact bitset regression covers all ordered affine operand pairs on one through three inputs, plus 64 seeded histories of six gates on four inputs, with seed 90210. It checks the filtration identity, graded dimension law, leading-symbol criterion, cell-rank ceiling and sharpness examples. Observed: 720 transitions, 3,168 grade checks, 71,640 target checks, 720 ceiling checks, three sharpness checks, PASS. The replay does not establish the general theorem; the proofs above do. The annihilator counterexample is a separate direct author derivation.

Next: formalize the exact sequence and rank ceiling, test the annihilator counterexample, then investigate target-sensitive quotient-ideal or syzygy invariants. Require bounds against arbitrary reuse in all reachable states. Do not replace the one-bit SAT decision problem by a multi-output problem without an independently established transfer. No superpolynomial classical lower bound, equivalence to P vs NP for the restricted promise, or certification is claimed.

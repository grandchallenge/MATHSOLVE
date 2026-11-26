# SCC-001 successor: colon quotients and syzygy transport

**Status:** author-derived candidate propositions; exact finite regression; not Lean-certified, independently adjudicated or novelty-certified. [Live tracker](https://github.com/grandchallenge/MATHSOLVE/issues/1309). [Admitted predecessor source](https://github.com/grandchallenge/MATHSOLVE/blob/e8096b79099f410aed7d2096c9e5367208b21823/research/SCC-001/RESULT.md). [Public primer](https://grandchallenge.ai/MATH-PROGRAMME/pnp_above/primer/#structural-capacity-calculus-why-relationships-resist-compression).

## 1. Model

Use the predecessor's Boolean function algebra B over the binary field, V containing constants and input coordinates, old filtration $F_r$, associated graded algebra A, and charged step adjoining g = uv for u,v in V. Negative filtration indices are zero. Then $F'_r=F_r+gF_{r-1}$. Write q for the symbol of g in grade two, C = A/(q), and t for the symbol of g in the new grade one (possibly redundant). Positive-degree homogeneous elements of A and A' square to zero, by Boolean idempotence and the degree filtration.

Define the residual relation module

$$
H=\mathrm{Ann}_A(q)/(q)\subseteq C.
$$

If A is presented as the exterior algebra on E = V modulo constants, quotiented by the homogeneous relation ideal I, and Q represents q, then H is the colon-ideal quotient

$$
H=(I:Q)/(I+(Q)).
$$

The containments follow from $q^2=0$. This is a one-element relation module, not the full minimal free resolution of I.

## 2. The correction differential

For a homogeneous class a in grade j of H, choose a representative f in $F_j$. Since the old symbol of f annihilates q in A, gf belongs to $F_{j+1}$. Set

$$
\delta(a)=[gf]_{j+1}\pmod{(q)}.
$$

Changing f by an element of $F_{j-1}$ changes the resulting symbol only by q times a lower symbol. Changing the old class by q times a grade j-2 symbol can be lifted as adding gh with h in $F_{j-2}$; multiplication by g leaves gh unchanged, which is in $F_j$. Therefore the map is well defined. Multiplication by g of gf leaves gf unchanged, so the image annihilates q and applying the correction again gives zero in grade j+2. For a homogeneous element of C represented by b in $F_k$, the product gf b belongs to $F_{j+k+1}$; taking its symbol proves C-linearity. Thus delta is a degree-one C-module map from H into H with square zero.

## 3. Exact quotient-ideal presentation

The successor graded algebra has the presentation

$$
A'\cong C[t]/(t^2,\ ta+\delta(a):a\in H),
\qquad \deg t=1.
$$

The old symbols map into A' with kernel (q), by the predecessor's exact sequence. Their image is C. Every new symbol is in that image plus t times that image, by the exact filtration update. The cross-relations hold by the definition of delta. For completeness, write any polynomial modulo the square of t as c+tb. If its image is zero, projecting onto the cokernel of the old-symbol map gives qb=0 in A (well defined for b in C since q squares to zero). Thus b belongs to H, and the cross-relation reduces c+tb to c+delta(b) in the embedded C. This must be zero. The presentation is exact, including redundant steps when q=0.

The additional information beyond the old quotient is the filtered correction map, not simply the annihilator dimension. Given module generators for H, C-linearity suffices to impose their cross-relations.

## 4. Three-coordinate counterexample and spectator amplification

Take three Boolean coordinates a,b,c. First adjoin y=ab. Then adjoin g=ac. The old degree-one basis is a,b,c,y; the old degree-two basis may be chosen as ac,bc,abc; all higher grades vanish. In C the degree-two basis is bc,abc. In H, b is an annihilator class, yet

$$
\delta(b)=[abc]=[cy]\ne0.
$$

The new relation is bt=cy, not bt=0. In fact delta sends b and y to [abc], and a and c to zero; its total rank is one. The old grade-zero annihilator is zero and the map vanishes on grade two. This refutes discarding the correction and retaining only a zero cross-product for annihilators.

For n at least three, append n-3 independent spectator coordinates to V without computing any additional functions of them. The old filtration splits as the tensor-product filtration of the three-variable state and the affine spectator state: expand products and use the independent square-free spectator monomials to get both inclusions. The graded algebra is the old three-variable algebra tensor the spectator exterior algebra. The annihilator quotient is H tensor that exterior algebra and delta is the original map tensor the identity (product lifts establish the formula). Thus

$$
\mathrm{rank}(\delta)=2^{n-3}.
$$

One gate can generate exponentially many independent correction directions. Raw correction rank therefore fails the polynomial one-gate capacity requirement.

## 5. A secondary projection on correction cohomology

Let L be the graded cohomology of the square-zero map delta on H. For a cycle class represented by f in $F_j$, the cycle condition gives gf in $F_j+gF_{j-1}$. Replace f by f+h with h in $F_{j-1}$ so that gf now belongs to $F_j$. Call such a representative adapted. Define P on L by the old grade-j class of gf, modulo (q) and correction boundaries.

This is well defined. The result is a delta-cycle because multiplying gf by g gives gf in $F_j$. Two adapted lifts of the same H class differ by an element h in $F_{j-1}$ plus gk with k in $F_{j-2}$. The gk contribution has zero class in C. Adaptedness implies gh belongs to $F_j$; its grade-j class is a correction boundary of the annihilator class of h. Changing the cohomology representative by a correction boundary can be lifted as adding g ell with ell in $F_{j-1}$ and g ell in $F_j$; its image is the same boundary. Hence P is well defined. Multiplying adapted representatives by a representative of a C class gives C-linearity. The representative gf is itself adapted, so $P^2=P$. Replacing g by 1+g gives the same H and delta (the difference contributes no symbol one grade higher), the same adaptedness condition, and the complementary projection 1+P.

Thus L splits canonically into images of P and 1+P, each represented by cycles supported on the corresponding gate-output set g=1 or g=0. This is a gate-local decomposition, not an invariant under arbitrary subsequent gates.

## 6. Evidence and next obligation

The dependency-free Node replay syzygy_replay.js checks the presentation's grade-wise image and kernel dimension, explicit cross-relations, C-linearity and square-zero law. It covers all ordered affine operand pairs through three bits, 64 seeded six-gate histories on four bits (seed 90210), plus the three- and four-bit counterexample fixtures. Observed PASS: 722 transitions, 3,899 grade checks, 6,332 cross-relations, 70,836 module-linearity checks, 6,332 square checks, and fixture ranks 1 and 2. The secondary projection proposition is a separate author proof, not tested by this replay. General proofs are not established by finite regression.

Background: [NIST circuit complexity](https://csrc.nist.gov/projects/circuit-complexity). Multiplicative complexity is established literature; novelty audit remains open. No claim of an explicit superpolynomial circuit lower bound or the PNP-ABOVE restricted-family transfer.

Next bounded target: formalize the exact presentation and correction maps, independently replay the finite fixtures, then compare target-relative modules across consecutive gates using the actual quotient and cross-relations. Prove an amortized bound for a target-sensitive invariant or provide an explicit cheap counterfamily. Gate-local raw ranks and dimensions are not acceptable substitutes. Preserve one-bit decision semantics and arbitrary reuse.

# WP60H theorem — odd-relation criterion for self-dual literal-`p=2` bad fibers

## 1. Protected setup

Protected MATHFORGE WP60G at

`grandchallenge/MATHFORGE@7da6813fcde7eb5f9badd7c86946f58691ed6f0d`

admits the BSS affine-fiber interface. Protected MATHSOLVE WP60G at

`grandchallenge/MATHSOLVE@1b75a922e2779178f478124948008afdd7e26a17`

proves the self-dual literal-`2` pairwise case.

Protected MATHFORGE WP60H at

`grandchallenge/MATHFORGE@54f1eaea24b35d4ca37e778786345c3622b6fd98`

admits the exact minimal-core transition interface from BSS Lemmas 5.13–5.15 and Corollary 5.16.

Abstract the residual self-dual situation as follows.

Let `V` be an `F_2`-vector space, let `G` be a group, and let

`j:V -> Hom(G,F_2)`

be an injective linear map. Let

`a:V -> F_2`

be a linear map. For nonzero `c_1,...,c_m in V`, put

`chi_i:=j(c_i)`

and

`H_i:=chi_i^{-1}(a(c_i))`.

In the protected BSS interface, `V` is the relevant residual global cohomology space after identifying primal and dual coefficients by self-duality, `j` is the protected cohomology-to-character map, and `a(c)` is the cocycle-evaluation class `-c_tilde(tau)` in the one-dimensional quotient. Linearity of `a` follows from linearity of cocycle addition, evaluation at `tau`, and passage to the quotient.

## 2. Linear consistency lemma

Define

`Phi:G -> F_2^m`,

`Phi(g)=(chi_1(g),...,chi_m(g))`,

and let

`b=(1-a(c_1),...,1-a(c_m)) in F_2^m`.

Then

`g notin union_i H_i`

is equivalent to

`Phi(g)=b`.

Let

`R := {eps=(eps_1,...,eps_m) in F_2^m : sum_i eps_i chi_i=0}`

be the relation space among the characters.

### Lemma `BSD-A1-WP60H-CONSISTENCY-001`

The equation `Phi(g)=b` has a solution if and only if

`sum_i eps_i b_i=0`

for every `eps in R`.

### Proof

The image of `Phi` is a subgroup, hence an `F_2`-subspace, of `F_2^m`. Its orthogonal complement under the standard dot product is exactly `R`, because `eps` annihilates every vector `Phi(g)` if and only if

`sum_i eps_i chi_i(g)=0`

for every `g`, equivalently `sum_i eps_i chi_i=0` as a character.

For a finite-dimensional vector space over `F_2`, a vector lies in a subspace if and only if it is orthogonal to the orthogonal complement of that subspace. Hence `b in im(Phi)` if and only if `eps dot b=0` for every `eps in R`. This is exactly the stated condition. QED.

## 3. Odd-relation affine-cover theorem

### Theorem `BSD-A1-WP60H-ODD-RELATION-COVER-002`

Under the setup of §1,

`G \ union_i H_i != empty`

if and only if every linear relation

`sum_i eps_i c_i=0`

has even Hamming weight

`sum_i eps_i=0 in F_2`.

Equivalently,

`union_i H_i = G`

if and only if the classes `c_1,...,c_m` admit an odd-cardinality linear dependence.

### Proof

Because `j` is linear and injective,

`sum_i eps_i chi_i=0`

if and only if

`j(sum_i eps_i c_i)=0`,

if and only if

`sum_i eps_i c_i=0`.

Thus `R` is also exactly the relation space among the classes `c_i`.

For `eps in R`, linearity of `a` gives

`sum_i eps_i a(c_i)
 = a(sum_i eps_i c_i)
 = a(0)
 =0`.

Therefore

`sum_i eps_i b_i
 = sum_i eps_i(1-a(c_i))
 = sum_i eps_i - sum_i eps_i a(c_i)
 = sum_i eps_i`.

By Lemma `BSD-A1-WP60H-CONSISTENCY-001`, there exists `g` outside every bad fiber if and only if this quantity is zero for every relation `eps`. That is equivalent to every relation having even Hamming weight.

Negating the condition gives the covering criterion: the bad fibers cover `G` exactly when there exists a relation of odd Hamming weight. QED.

## 4. Four-class specialization

### Corollary `BSD-A1-WP60H-FOUR-FIBER-003`

Let `c_1,c_2,c_3,c_4` be nonzero. Then

`H_1 union H_2 union H_3 union H_4 = G`

if and only if some three of the four classes sum to zero.

### Proof

By Theorem `BSD-A1-WP60H-ODD-RELATION-COVER-002`, covering is equivalent to a nonzero odd-weight relation among four nonzero classes.

The possible odd weights are `1` and `3`. A weight-one relation would say that one `c_i` is zero, excluded by hypothesis. Hence covering occurs exactly when a relation of weight three exists, i.e. when there are distinct indices `i,j,k` with

`c_i+c_j+c_k=0`.

Conversely any such three-term relation has odd weight and therefore forces covering. QED.

## 5. BSS self-dual specialization

Assume the protected WP60G residual BSS setup:

1. `R=k=F_2`;
2. BSS Hypothesis 3.2 holds;
3. `A ~= A^*(1)` `G_K`-equivariantly.

Use the self-duality to identify every primal and dual class occurring in a simultaneous-localization problem with a class in one vector space

`V=H^1(K,A)`.

Protected WP60G proves naturality of both `j` and the affine constants under this identification. Hence the BSS bad fibers satisfy the hypotheses of Theorem `BSD-A1-WP60H-ODD-RELATION-COVER-002`.

For the `s=2` configuration of two primal and two dual nonzero classes, the common-prime Chebotarev step fails **exactly** when some three of the four identified cohomology classes sum to zero.

Thus the generic four-hyperplane covering problem is replaced by one precise arithmetic question.

## 6. Minimal-core transition consequence

Protected MATHFORGE WP60H gives the actual `s=2` source configuration used in Corollary 5.16.

For two minimal core vertices `n_1,n_2`, choose `q_i|n_i` and put `m_i=n_i/q_i`. Then:

- `m_i` is noncore;
- `lambda(m_i)=r+1`;
- `lambda^*(m_i)=1`;
- Lemma 5.15 needs one prime at which the localization maps from each primal space `H^1_{F(n_i)}` and each one-dimensional dual space `H^1_{F^*(m_i)}` are nonzero;
- the source requires nonzero localization of the *spaces*, not a predetermined primal witness class.

Accordingly the WP60H relation criterion must be applied to strategically chosen nonzero primal witnesses together with the two nonzero dual generators.

The admitted dimension, inclusion, and finite/transverse transition statements do **not themselves assert** that every such choice avoids a three-term relation. No such exclusion is present in the protected source interface. Therefore a downstream proof must supply additional global structure, or replace the one-common-prime construction.

This is an implication-boundary statement, not a counterexample to the actual BSS arithmetic configuration.

## 7. Refined F1 boundary

Record

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

This refines

`MISSING_P2_TWO_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`,

which itself refines the parent F1 boundary

`MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.

WP60H does not assert that the three-term relation is present or absent in the actual BSS minimal-core configuration.

## 8. Exact successor obligation

The next F1 proof must use structure beyond the admitted dimension/membership data. It must do at least one of:

1. exclude every possible three-term relation by Poitou–Tate/global-duality information for the actual modified Selmer structures;
2. exploit freedom of primal-witness choice and prove that witnesses can always be selected so that no odd relation occurs;
3. show that any exceptional three-term relation itself produces an alternate edge/path in the core-vertex graph;
4. construct another connectivity proof independent of the four-fiber Chebotarev step.

A generic dimension, affine-counting, or finite-versus-transverse slogan is no longer sufficient after this reduction.

Because F2 is logically independent of F1, work may proceed in parallel on

`MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

## 9. Claim firewall

This theorem does not establish:

- exclusion or existence of the three-term relation in the actual BSS minimal-core configuration;
- the `s=2` common-prime theorem;
- core-vertex graph connectivity at `p=2`;
- full F1 closure;
- BSS Hypothesis 3.2/H2/H3 uniformly for the selected class;
- BSS Fitting control at `p=2`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

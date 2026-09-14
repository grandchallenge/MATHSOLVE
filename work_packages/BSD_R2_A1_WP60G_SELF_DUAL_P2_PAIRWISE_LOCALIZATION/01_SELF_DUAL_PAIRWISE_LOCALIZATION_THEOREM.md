# WP60G theorem — self-dual literal-`p=2` pairwise BSS localization

## 1. Protected setup

Protected WP60F isolates

`F1 = MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.

Protected MATHFORGE WP60G at

`grandchallenge/MATHFORGE@7da6813fcde7eb5f9badd7c86946f58691ed6f0d`

admits the exact internal interface of BSS Lemma 3.9.

For a coefficient module `B in {A,A^*(1)}` satisfying BSS Hypothesis 3.2, define

`j_B := f_B o Res_B
 : H^1(K,B)
   -> Hom(G_{K(A)_M}, B/(tau-1)B)`.

The protected source interface gives:

1. `j_B` is injective;
2. for nonzero `c`, with cocycle representative `c_tilde`, the affine constant
   `a_c := -c_tilde(tau) mod (tau-1)B`
   is well-defined;
3. the bad fiber is
   `H_c := j_B(c)^{-1}(a_c)`;
4. if `gamma` lies outside all relevant bad fibers, the BSS Chebotarev construction gives a positive-density set of primes where all corresponding localizations are nonzero.

In the residual literal-`2` case `R=k=F_2`, Hypothesis 3.2(ii) identifies each target quotient with `F_2`, so every nonzero `j_B(c)` is a surjective character and every `H_c` is an affine index-two fiber.

## 2. Abstract affine-fiber lemma

### Lemma `BSD-A1-WP60G-AFFINE-2COVER-001`

Let `G` be a group. Let

`chi_1, chi_2 : G -> F_2`

be nonzero homomorphisms and let `a_1,a_2 in F_2`. Put

`H_i := chi_i^{-1}(a_i)`.

Then

`H_1 union H_2 = G`

if and only if

`chi_1=chi_2` and `a_1 != a_2`.

### Proof

Each nonzero `chi_i` is surjective and has an index-two kernel.

Suppose first that `chi_1 != chi_2`. Consider

`chi=(chi_1,chi_2):G->F_2^2`.

Its image is a subgroup of `F_2^2` whose projection to each factor is surjective. If the image were proper, it would have order two. The only order-two subgroup of `F_2^2` with both coordinate projections surjective is the diagonal

`{(0,0),(1,1)}`,

which would imply `chi_1=chi_2`, contrary to assumption. Hence `chi` is surjective.

Therefore there exists `g in G` with

`(chi_1(g),chi_2(g))=(1-a_1,1-a_2)`.

This `g` lies in neither `H_1` nor `H_2`, so the two fibers do not cover `G`.

Now suppose `chi_1=chi_2=:chi`. If `a_1=a_2`, then `H_1=H_2` is one proper index-two fiber and cannot cover `G`. If `a_1 != a_2`, the two fibers are the two complementary fibers of the surjection `chi:G->F_2`, so their union is all of `G`.

This proves the equivalence. QED.

## 3. Naturality under coefficient-module isomorphism

Let

`iota:A -> A^*(1)`

be a `G_K`-equivariant isomorphism of `F_2`-modules.

Because `iota` is a `G_K`-module isomorphism, the kernels of the two Galois actions agree after identification; hence

`K(A)=K(A^*(1))`.

The auxiliary field `K_M` depends only on the coefficient characteristic/exponent, so the BSS field `K(A)_M` is the same for both modules.

Since `iota` commutes with the action of `tau`, it induces an isomorphism

`bar_iota:
 A/(tau-1)A
 -> A^*(1)/(tau-1)A^*(1)`.

Restriction in cohomology is natural in the coefficient module, and the protected map `f_B` is induced by the quotient `B -> B/(tau-1)B`. Therefore the square

`H^1(K,A)              --j_A-->       Hom(G_{K(A)_M},A/(tau-1)A)
   | iota_*                                  | bar_iota_*
   v                                         v
 H^1(K,A^*(1))         --j_{A^*(1)}--> Hom(G_{K(A)_M},A^*(1)/(tau-1)A^*(1))`

commutes.

The affine constants are natural as well. If `c_tilde` represents `c`, then `iota o c_tilde` represents `iota_*(c)`, and therefore

`a_{iota_*(c)}
 = -(iota o c_tilde)(tau)
 = bar_iota(-c_tilde(tau))
 = bar_iota(a_c)`.

These statements use only the protected definitions of `j_B` and `a_c`.

## 4. Self-dual pairwise literal-2 localization

### Theorem `BSD-A1-WP60G-SELFDUAL-PAIRWISE-002`

Assume the residual literal-`2` BSS setup:

1. `R=k=F_2`;
2. `A` satisfies BSS Hypothesis 3.2;
3. there is a `G_K`-equivariant isomorphism
   `iota:A -> A^*(1)`.

Then for every pair of nonzero classes

`c in H^1(K,A)`, `c^* in H^1(K,A^*(1))`,

their two BSS bad fibers do not cover `G_{K(A)_2}`.

Consequently there exists a positive-density set of BSS auxiliary primes `q` such that

`loc_q(c) != 0`

and

`loc_q(c^*) != 0`

simultaneously.

### Proof

Use `iota` to identify `A^*(1)` with `A`, the two quotient targets with `F_2`, and the two BSS Galois groups with the same group

`G := G_{K(A)_2}`.

Put

`d := iota_*^{-1}(c^*) in H^1(K,A)`.

Let

`chi_c := j_A(c):G->F_2`,

`chi_d := j_A(d):G->F_2`.

Both are nonzero because `c,d` are nonzero and `j_A` is injective.

After the natural identifications above, the bad fiber for `c^*` is exactly the bad fiber determined by `d`.

There are two cases.

### Case 1: `chi_c != chi_d`

By Lemma `BSD-A1-WP60G-AFFINE-2COVER-001`, the two affine fibers cannot cover `G`.

### Case 2: `chi_c = chi_d`

Injectivity of `j_A` gives

`c=d`.

Naturality of the affine constants then gives

`a_{c^*}=bar_iota(a_c)`.

After identifying the quotient targets by `bar_iota`, the two constants are equal. Thus the two bad fibers coincide. A single index-two fiber is proper, so their union again does not cover `G`.

Therefore in every case there exists

`gamma in G \ (H_c union H_{c^*})`.

The protected BSS Chebotarev/localization interface now applies unchanged and gives a positive-density set of primes at which both localizations are nonzero. QED.

## 5. Elliptic residual self-duality

### Proposition `BSD-A1-WP60G-WEIL-SELFDUAL-003`

For every elliptic curve `E/Q`, there is a canonical `G_Q`-equivariant isomorphism

`E[2] ~= E[2]^*(1)`.

### Proof

The Weil pairing is a perfect `G_Q`-equivariant bilinear pairing

`e_2:E[2] x E[2] -> mu_2`.

For `P in E[2]`, define

`iota_E(P):E[2]->mu_2`,

`Q |-> e_2(P,Q)`.

Perfection of the Weil pairing makes `iota_E` an isomorphism

`E[2] -> Hom(E[2],mu_2)`.

By definition

`Hom(E[2],mu_2) = E[2]^*(1)`,

and Galois equivariance of the Weil pairing makes `iota_E` `G_Q`-equivariant. QED.

Thus the self-duality hypothesis of Theorem `BSD-A1-WP60G-SELFDUAL-PAIRWISE-002` is automatic for the selected residual elliptic module `A=E[2]`.

This proposition does **not** establish BSS Hypothesis 3.2 for every selected curve; WP60F boundary F2 remains live.

## 6. Exact consequence for the BSS graph argument

The published numerical hypothesis `s+t<p` is no longer needed for the self-dual residual case `s=t=1`, provided BSS Hypothesis 3.2 holds.

Accordingly, the pairwise Chebotarev step used in BSS Lemma 5.14 admits a literal-`2` self-dual replacement. The same pairwise pattern appearing in the reduction step of Lemma 5.17 is likewise no longer blocked by the `2<2` count.

However, BSS Lemma 5.15 with `s=2` requires a **single** new prime to satisfy four nonvanishing conditions:

- two primal classes;
- two dual classes.

After self-duality these become four affine index-two fibers in one group. The two-fiber lemma above does not imply that a union of four such fibers is proper.

Corollary 5.16 uses exactly this `s=2` case to connect two minimal core vertices. Therefore WP60G does not prove full graph connectivity.

Record the refined frontier

`MISSING_P2_TWO_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`.

This is a refinement within F1; it does not declare F1 fully resolved.

## 7. Reopening target for WP60H

The next bounded theorem problem is one of the following equivalent execution choices:

1. prove that the four BSS bad fibers arising in the `s=2` minimal-core-vertex configuration cannot cover the relevant residual Galois group under additional relations forced by global duality/self-duality; or
2. replace Corollary 5.16 by another proof connecting minimal core vertices that does not require a single prime satisfying all four constraints.

A generic statement that four affine hyperplanes over `F_2` need not cover is insufficient. The next proof must use the actual BSS classes or construct a different graph argument.

## 8. Claim firewall

WP60G does not establish:

- BSS Hypothesis 3.2 or H2/H3 uniformly for the selected class;
- the `s=2` four-constraint localization step;
- full connectivity of the core-vertex graph at `p=2`;
- BSS Theorem 5.20, Theorem 5.2, or Corollary 6.15 at `p=2`;
- R5-LIFT or R5-PRIM;
- D2d or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

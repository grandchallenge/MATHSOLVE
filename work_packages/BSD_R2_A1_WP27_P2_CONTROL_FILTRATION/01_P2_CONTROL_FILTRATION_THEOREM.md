# WP27 theorem — exact good-ordinary place-`2` control filtration

## 1. Setup and protected interfaces

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Put

`R_2 := E_tilde(F_2)[2^infinity]`.

Protected WP07 proves

`#R_2 = 3-a_2 in {2,4}`.

Protected WP21 defines the primitive classical-Kummer local restriction kernel

`K_2`.

Protected WP23 identifies this kernel with Greenberg's base good-ordinary local-control kernel and proves

`#K_2=(3-a_2)^2`.

Protected WP25 identifies the stabilized universal-norm quotient as

`U_2 ~= K_2^vee`.

The protected MATHFORGE audit of Greenberg's local theorem records the following exact proof interfaces:

1. the finite classical Kummer image is contained in the connected-ordinary image;
2. the quotient of those images is
   `Im(lambda_2)/Im(kappa_2) ~= R_2`;
3. at infinite cyclotomic level the Kummer and connected-ordinary images agree;
4. Greenberg factors the finite-to-infinite classical-Kummer restriction map through the connected-ordinary quotient;
5. the first map in that factorization is surjective;
6. the kernel of the second map is identified by inflation-restriction with the corresponding cohomology of the finite reduction group.

No new external theorem premise is used.

## 2. The factorization

Write

`H_Kum := H^1(Q_2,E[2^infinity])/Im(kappa_2)`

for the finite classical-Kummer quotient, and

`H_ord := H^1(Q_2,E[2^infinity])/Im(lambda_2)`

for the finite connected-ordinary quotient used inside Greenberg's proof.

Because

`Im(kappa_2) subset Im(lambda_2)`,

there is a natural surjection

`a_2^ctl : H_Kum -> H_ord`.

To avoid confusion with the Frobenius trace `a_2`, the superscript `ctl` is retained throughout this package.

At infinite cyclotomic level protected Greenberg Proposition 2.4 gives equality of the Kummer and connected-ordinary images. Therefore the primitive restriction map factors as

`r_2 = b_2^ctl o a_2^ctl`,

where

`b_2^ctl : H_ord -> H_infty`

is the connected-ordinary restriction map to the common infinite-level quotient.

Define

`D_2 := ker(a_2^ctl)`

and

`J_2 := ker(b_2^ctl)`.

### Lemma `BSD-A1-WP27-DISCREPANCY-001`

There is a canonical isomorphism

`D_2 ~= Im(lambda_2)/Im(kappa_2) ~= R_2`.

### Proof

The kernel of the quotient map

`H^1/Im(kappa_2) -> H^1/Im(lambda_2)`

is exactly

`Im(lambda_2)/Im(kappa_2)`.

Protected Greenberg Proposition 2.5 identifies this quotient with

`E_tilde(F_2)[2^infinity]=R_2`.

Thus the claimed canonical isomorphism follows. QED.

## 3. The connected-ordinary restriction kernel

The local cyclotomic `Z_2`-extension of `Q_2` is totally ramified. Its residue field remains `F_2` at every finite layer. Hence `Gamma_2` acts trivially on the reduction points `R_2` through residue-field action.

Greenberg's inflation-restriction calculation in the proof of Lemma 3.4 identifies the kernel of the connected-ordinary restriction map with the first cohomology of this reduction group.

### Lemma `BSD-A1-WP27-ORDINARY-KERNEL-001`

There is a canonical isomorphism

`J_2 ~= H^1(Gamma_2,R_2)`.

Moreover

`#J_2=#R_2=3-a_2`.

### Proof

The first statement is exactly the inflation-restriction kernel identification retained in the protected Greenberg proof interface.

For the order, Greenberg's Lemma 3.4 proof shows that the finite kernel and cokernel of the relevant `gamma-1` map on the finite reduction group have equal order, namely the order of the fixed reduction subgroup. At the base of the totally ramified tower the fixed reduction subgroup is all of `R_2`. Therefore

`#J_2=#R_2=3-a_2`.

Equivalently, because the action is trivial,

`H^1(Gamma_2,R_2)=Hom_cont(Gamma_2,R_2)`

has the same finite order as `R_2`; no canonical topological generator of `Gamma_2` is chosen or needed. QED.

## 4. Exact sequence for the primitive control kernel

Protected WP23 identifies

`K_2=ker(r_2)`.

### Theorem `BSD-A1-WP27-KERNEL-EXTENSION-001`

There is a canonical short exact sequence

`0 -> D_2 -> K_2 -> J_2 -> 0`.

### Proof

Because

`r_2=b_2^ctl o a_2^ctl`

and `a_2^ctl` is surjective, restriction of `a_2^ctl` to `ker(r_2)` maps into `ker(b_2^ctl)=J_2`.

Its kernel is

`ker(a_2^ctl)=D_2`.

It remains to prove surjectivity onto `J_2`. Let `j in J_2`. Since `a_2^ctl` is surjective, choose `h in H_Kum` with

`a_2^ctl(h)=j`.

Then

`r_2(h)=b_2^ctl(j)=0`,

so `h in K_2`. Thus every `j` is hit by the restricted map, proving exactness. QED.

### Corollary `BSD-A1-WP27-ORDER-001`

The protected order formula is recovered exactly:

`#K_2=#D_2 #J_2=(3-a_2)^2`.

This is a consistency check, not a replacement for the exact sequence.

## 5. Dual universal-norm filtration

Pontryagin duality is exact on finite groups. Dualizing Theorem `BSD-A1-WP27-KERNEL-EXTENSION-001` gives

`0 -> J_2^vee -> K_2^vee -> D_2^vee -> 0`.

Transport this exact sequence through protected WP25's canonical identification

`U_2 ~= K_2^vee`.

### Theorem `BSD-A1-WP27-UNIVERSAL-NORM-FILTRATION-001`

There is an exact sequence

`0 -> J_2^vee
   -> U_2
   -> D_2^vee
   -> 0`,

with

`#J_2^vee=#D_2^vee=3-a_2`.

In particular,

`#U_2=(3-a_2)^2`.

No splitting is implied.

### Proof

Exact finite Pontryagin duality reverses the protected kernel extension. Protected WP25 identifies the middle term `K_2^vee` with `U_2`. The subquotient orders follow from Lemmas `BSD-A1-WP27-DISCREPANCY-001` and `BSD-A1-WP27-ORDINARY-KERNEL-001`. QED.

## 6. Exact position coordinates for the saturated generator

Let

`x_2(P):=[P]_2 in U_2`

be the protected WP25 universal-norm obstruction class of a saturated rank-one generator.

Let

`pi_2:U_2 -> D_2^vee`

be the quotient map from the exact filtration and define

`q_2(P):=pi_2(x_2(P))`.

Since `D_2^vee` is a finite `2`-group, there is a unique integer

`r_2(P)>=0`

such that

`ord(q_2(P))=2^{r_2(P)}`.

Equivalently,

`r_2(P):=ord_2(ord(q_2(P)))`.

By definition of the order of the quotient class,

`2^{r_2(P)}x_2(P)`

lies in the kernel of `pi_2`, which is the embedded group `J_2^vee`.

Define

`y_2(P):=2^{r_2(P)}x_2(P) in J_2^vee`

and

`s_2(P):=ord_2(ord(y_2(P)))`.

### Theorem `BSD-A1-WP27-POSITION-001`

One has exactly

`rho_2(P)=r_2(P)+s_2(P)`.

Moreover

`0 <= r_2(P) <= ord_2(3-a_2)`,

`0 <= s_2(P) <= ord_2(3-a_2)`.

### Proof

Write

`ord(x_2(P))=2^t`.

The quotient class has order `2^{r_2(P)}`. Therefore `r_2(P)` is the least nonnegative integer `r` for which

`2^r x_2(P) in J_2^vee`.

The element at that first entrance into the submodule is `y_2(P)` and has order `2^{s_2(P)}`.

Certainly

`2^{r_2(P)+s_2(P)}x_2(P)=0`,

so `t<=r_2(P)+s_2(P)`.

Conversely, if `2^m x_2(P)=0`, then its quotient is zero, so `m>=r_2(P)`. Writing `m=r_2(P)+u`, one has

`2^u y_2(P)=0`.

By definition of the order of `y_2(P)`, this forces

`u>=s_2(P)`.

Hence every annihilating exponent satisfies

`m>=r_2(P)+s_2(P)`,

and therefore

`t=r_2(P)+s_2(P)`.

Protected WP25 defines

`rho_2(P)=ord_2(ord(x_2(P)))=t`.

The bounds follow because `q_2(P)` lies in a group of order `3-a_2`, and `y_2(P)` lies in another group of the same order. QED.

## 7. Global control-defect formula after WP27

Protected WP26 defines

`rho_bad(P)
 = max_{ell|N} ord_2(ord(comp_ell(P)))`

and proves

`rho_E=max(rho_2(P),rho_bad(P))`.

Combining with Theorem `BSD-A1-WP27-POSITION-001` gives:

### Corollary `BSD-A1-WP27-GLOBAL-001`

`rho_E
 = max(r_2(P)+s_2(P), rho_bad(P))`.

Therefore

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max(r_2(P)+s_2(P), rho_bad(P))`.

All odd-prime terms in this expression are finite arithmetic data from protected WP26. The unresolved structural information is exactly the position of `[P]_2` in the two-step place-`2` extension.

## 8. Refined boundary

WP27 replaces

`MISSING_P2_GOOD_ORDINARY_SATURATED_GENERATOR_UNIVERSAL_NORM_ORDER_AT_2`

with

`MISSING_P2_SATURATED_GENERATOR_POSITION_IN_GOOD_ORDINARY_CONTROL_EXTENSION`.

A successor may seek to identify:

1. the quotient coordinate `q_2(P)` with a concrete reduction-theoretic datum; and
2. the residual submodule coordinate `y_2(P)` with a connected/formal universal-norm datum.

Neither identification is automatic from the exact sequence. Any external compatibility theorem used for either identification must first be admitted through MATHFORGE.

## 9. Claim firewall

WP27 does not prove:

- a value of `q_2(P)`, `r_2(P)`, `y_2(P)`, `s_2(P)`, or `rho_2(P)`;
- a splitting of the exact sequence for `K_2` or `U_2`;
- that `q_2(P)` is literal reduction of `P`;
- that `y_2(P)` is a formal-group logarithm, connected norm index, or height class;
- equality of any position coordinate with a regulator, Bockstein, Euler factor, or analytic quantity;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

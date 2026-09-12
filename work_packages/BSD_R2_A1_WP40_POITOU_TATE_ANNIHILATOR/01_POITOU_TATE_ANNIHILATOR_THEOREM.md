# WP40 theorem — exact Poitou–Tate annihilator of the `K`-side Kummer/Greenberg global hit

## 1. Protected setup

Let

`T := T_2(E)`,

`A := E[2^infinity]`.

Fix a finite set of places containing those above `2N infinity` and all places needed by the protected Selmer structures.

For the product of compact local cohomology groups write

`P_T := product_v H^1(K_v,T)`

and for the corresponding discrete local cohomology write

`P_A := product_v H^1(K_v,A)`.

Use the local Tate pairings induced by the Weil pairing. Protected MATHFORGE Greenberg Poitou–Tate admission supplies the exact global orthogonality interface at literal `p=2`.

Let

`U_str subset U_Kum subset P_T`

be the compact strict-Greenberg and classical-Kummer local conditions whose finite quotient is WP39's

`R_K := U_Kum/U_str`.

Define their exact annihilators in `P_A` by

`L_Kum := U_Kum^perp`,

`L_str := U_str^perp`.

Then

`L_Kum subset L_str`.

Write

`G_T := im(H^1(K,T) -> P_T)`,

`G_A := im(H^1(K,A) -> P_A)`

for the global localization images, with the understood finite set of allowed ramification.

Protected Poitou–Tate gives

`G_T^perp = G_A`,

`G_A^perp = G_T`

in the relevant local duality product.

## 2. Perfect duality on the finite local quotient

### Lemma `BSD-A1-WP40-LOCAL-QUOTIENT-DUAL-001`

Local Tate duality induces a canonical perfect pairing of finite groups

`R_K x R_K^dual -> Q_2/Z_2`,

where

`R_K^dual := L_str/L_Kum`.

Hence

`R_K^dual ~= R_K^vee`

canonically as Pontryagin duals and

`len_Z2 R_K^dual = len_Z2 R_K`.

### Proof

Because `U_str subset U_Kum`, annihilators reverse inclusion:

`L_Kum=U_Kum^perp subset U_str^perp=L_str`.

The local Tate pairing is perfect between the ambient compact and discrete local cohomology groups. The standard annihilator-quotient construction therefore descends to a perfect pairing

`(U_Kum/U_str) x (U_str^perp/U_Kum^perp) -> Q_2/Z_2`.

WP39 proves the first quotient finite. Its Pontryagin dual is therefore the second quotient, also finite, with the same `Z_2`-length. QED.

## 3. The compact global hit

WP39 defines

`J_K := im(S_2(E/K) -> R_K)`.

Equivalently, at the level of local images,

`J_K
 = im((G_T intersect U_Kum) -> U_Kum/U_str)`.

The kernel of this quotient map is exactly

`G_T intersect U_str`,

which is the localization image of the strict compact Selmer group.

## 4. The dual global hit

Define

`D_K
 := im((G_A intersect L_str) -> L_str/L_Kum)`.

Equivalently, let

`Sel_A^{str-perp}(K)
 := {c in H^1(K,A) : loc(c) in L_str}`,

`Sel_A^{Kum}(K)
 := {c in H^1(K,A) : loc(c) in L_Kum}`.

The localization map to `L_str/L_Kum` has kernel exactly `Sel_A^{Kum}(K)`. Therefore it induces the exact isomorphism

`D_K
 ~= Sel_A^{str-perp}(K) / Sel_A^{Kum}(K)`.

No rank or torsion-freeness assertion is made about either discrete Selmer group.

## 5. Exact annihilator theorem

### Theorem `BSD-A1-WP40-ANNIHILATOR-001`

Under the perfect pairing of Lemma `LOCAL-QUOTIENT-DUAL-001`,

`ann_{R_K^dual}(J_K) = D_K`.

### Proof

Take a class

`y + L_Kum in R_K^dual = L_str/L_Kum`.

Because `y in L_str=U_str^perp`, its pairing with a class in `R_K=U_Kum/U_str` is well-defined.

The class `y+L_Kum` annihilates `J_K` precisely when `y` pairs trivially with every element of

`G_T intersect U_Kum`.

Thus

`y in L_str intersect (G_T intersect U_Kum)^perp`.

Protected Poitou–Tate orthogonality and local Tate duality give

`(G_T intersect U_Kum)^perp
 = G_T^perp + U_Kum^perp
 = G_A + L_Kum`.

All quotients relevant here are finite, so no additional closure changes the resulting finite subgroup.

Therefore

`ann(J_K)
 = [L_str intersect (G_A + L_Kum)]/L_Kum`.

Since `L_Kum subset L_str`, the modular law gives

`L_str intersect (G_A + L_Kum)
 = (L_str intersect G_A) + L_Kum`.

Hence

`ann(J_K)
 = [(L_str intersect G_A)+L_Kum]/L_Kum`,

which is exactly the image defining `D_K`. QED.

## 6. Exact complementary-length formula

Put

`j_K := len_Z2 J_K`,

`d_K := len_Z2 D_K`.

### Corollary `BSD-A1-WP40-COMPLEMENT-001`

One has exactly

`j_K + d_K = len_Z2 R_K`.

Using protected WP39,

`j_K + d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

Equivalently,

`j_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)
   - d_K`.

### Proof

For a finite abelian group `R` paired perfectly with `R^vee`, the annihilator of a subgroup `J subset R` has order

`#ann(J) = #R/#J`.

Apply Theorem `ANNIHILATOR-001` with `R=R_K`, `J=J_K`, and `ann(J_K)=D_K`, then take `Z_2`-lengths and substitute WP39's exact ambient length. QED.

## 7. Structural interpretation

WP39 asks which compact Kummer local classes are globally hit. WP40 shows that the missing compact image is exactly complementary to a dual discrete global hit.

This is not merely a change of symbols. The dual condition `L_str=U_str^perp` is the condition naturally adjacent to the Selmer-complex duality and Bockstein-height formalism used in WP37. Thus D2b is now expressed on the same duality surface as D2a.

However WP40 does **not** identify `D_K` with the radical, image, cokernel, determinant, or valuation of the first Nekovář height. Such an identification is the next substantive bridge and must be proved rather than inferred from duality vocabulary.

## 8. Refined frontier

The WP39 boundary

`MISSING_P2_KUMMER_GREENBERG_GLOBAL_HIT_SUBGROUP_OVER_K`

is replaced by

`MISSING_P2_DUAL_GLOBAL_HIT_OVER_K`.

An exact value of `d_K` immediately determines `j_K` by Corollary `COMPLEMENT-001`.

The next bounded theorem query is:

> Does the WP37 cyclotomic Bockstein-height complex identify the finite dual global hit `D_K` with an explicit Bockstein image/cokernel or height-radical quotient, at literal `p=2`, without assuming the first height is nondegenerate?

If yes, D2a and D2b partly merge into one exact Bockstein-height defect. If not, retain them as separate theorem boundaries.

## 9. Claim firewall

WP40 does not prove:

- `D_K=0`;
- `J_K=R_K`;
- any specific value of `j_K` or `d_K`;
- rank one or torsion-freeness of the dual relaxed Selmer structure;
- fixed-`2` height nondegeneracy;
- an identification of `D_K` with the Bockstein height or its radical;
- an analytic determinant generator at height-one `(2)`;
- exact Disegni interpolation/test-vector valuations;
- equality of p-adic and real heights;
- final WP06 descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

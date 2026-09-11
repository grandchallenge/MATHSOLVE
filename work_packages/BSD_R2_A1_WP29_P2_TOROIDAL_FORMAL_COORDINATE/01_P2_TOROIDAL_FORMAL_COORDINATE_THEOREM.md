# WP29 theorem — toroidal congruence depth of the remaining formal norm class

## 1. Setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` branch.

Protected WP28 gives a canonical exact sequence

`0 -> F_2^norm -> U_2 -> E_tilde(F_2) -> 0`

with

`#F_2^norm = 3-a_2`.

For a saturated generator `P` of `E(Q)/E(Q)_tors`, protected WP28 defines

`x_2(P)=[P]_2 in U_2`,

`r_red(P)=ord_2(ord(red(P)))`,

and the unique formal element

`z_form(P) in F_2^norm`

mapping to

`2^{r_red(P)}x_2(P)`.

It also defines

`s_form(P)=ord_2(ord(z_form(P)))`

and proves

`rho_2(P)=r_red(P)+s_form(P)`.

Protected MATHFORGE commit

`2021db4f98da3d0df7cea2a37c9d9f6d4e9a4576`

admits the Hall/Lubin-Rosen map-level height-one formal-norm construction. In dimension one and for the selected local cyclotomic extension it supplies, after a source-compatible toroidal-coordinate choice, an isomorphism

`psi_k : F_2^norm -> Gamma_2/(1-u)Gamma_2`,

where `Gamma_2=Gal(Q_{infty,2}/Q_2)` is a free rank-one `Z_2`-module and `u in Z_2^x` is the toroidal twist scalar.

The source admission permits use of this isomorphism on the individual protected WP28 class and permits only coordinate-independent element-order conclusions. It does not identify `u` with the protected WP07 unit root.

## 2. Toroidal image of the selected formal class

### Definition `BSD-A1-WP29-THETA-001`

For a source-compatible toroidal coordinate `k`, define

`theta_form,k(P)
 := psi_k(z_form(P))
 in Gamma_2/(1-u)Gamma_2`.

### Theorem `BSD-A1-WP29-ORDER-001`

One has

`ord(theta_form,k(P))=ord(z_form(P))`.

Consequently

`s_form(P)=ord_2(ord(theta_form,k(P)))`.

### Proof

The admitted Hall/Lubin-Rosen construction gives `psi_k` as a group isomorphism from the formal universal-norm quotient to the Galois quotient. Every group isomorphism preserves the order of every element. Apply this to `z_form(P)`. Taking `ord_2` gives the second assertion. QED.

### Coordinate independence retained by WP29

The value of `theta_form,k(P)` as a named quotient element depends on the auxiliary toroidal coordinate. The protected source audit permits the following exact invariant conclusion: replacing `k` by another source-compatible toroidal coordinate changes the quotient description by a group automorphism. Element order is therefore unchanged.

Thus

`ord(theta_form,k(P))`

and its `2`-adic valuation are independent of the source-compatible toroidal coordinate even though a scalar representative is not canonical.

## 3. Size of the toroidal quotient

Put

`m_2:=ord_2(3-a_2)`.

Protected WP07 gives

`3-a_2 in {2,4}`,

so `m_2 in {1,2}`.

### Lemma `BSD-A1-WP29-TWIST-VALUATION-001`

One has

`ord_2(1-u)=m_2`.

This is an equality of valuations only. It is not an identity between `u` and the protected unit root.

### Proof

Protected WP28 proves

`#F_2^norm=3-a_2=2^{m_2}`.

The protected Hall/Lubin-Rosen source gives

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`.

Choose any topological `Z_2`-module generator of the free rank-one module `Gamma_2`; this identifies

`Gamma_2/(1-u)Gamma_2
 ~= Z_2/(1-u)Z_2`.

The quotient is finite of order `2^{ord_2(1-u)}`. Comparing its order with `2^{m_2}` gives

`ord_2(1-u)=m_2`. QED.

### Firewall on the numerical coincidence

Protected WP07 separately proves

`ord_2(1-alpha^(-1))=ord_2(3-a_2)=m_2`.

WP29 therefore records only the numerical equality

`ord_2(1-u)=ord_2(1-alpha^(-1))=m_2`.

No equality, unit multiple, canonical identification, or interpolation compatibility between `u` and `alpha^(-1)` is asserted.

## 4. Scalar coordinate and truncated valuation

Choose a topological generator `gamma` of `Gamma_2` and use it to identify

`Gamma_2 ~= Z_2`.

Under this identification write the class `theta_form,k(P)` as

`[t_form,k,gamma(P)]
 in Z_2/(1-u)Z_2`.

The scalar lift is not unique.

### Definition `BSD-A1-WP29-TAU-001`

For a scalar lift `t in Z_2`, define

`tau_form(P)
 := min(m_2,ord_2(t))`,

with the convention `ord_2(0)=+infinity`, so the zero class has `tau_form(P)=m_2`.

### Lemma `BSD-A1-WP29-LIFT-INVARIANCE-001`

`tau_form(P)` is independent of the chosen scalar lift.

### Proof

By Lemma `BSD-A1-WP29-TWIST-VALUATION-001`, the ideal `(1-u)Z_2` equals `2^{m_2}Z_2` up to multiplication by a unit.

Two lifts of the same class differ by an element of valuation at least `m_2`. If one lift has valuation strictly below `m_2`, adding a term of valuation at least `m_2` cannot change that lower valuation. If one lift has valuation at least `m_2`, both represent the zero class and the truncated valuation is `m_2`. QED.

### Lemma `BSD-A1-WP29-GENERATOR-INVARIANCE-001`

`tau_form(P)` is independent of the topological generator `gamma`.

### Proof

Any two topological `Z_2`-module generators differ by multiplication by a unit in `Z_2^x`. Therefore the corresponding scalar representatives differ by multiplication by a `2`-adic unit. This preserves `ord_2` and hence the truncated valuation. QED.

### Lemma `BSD-A1-WP29-TOROIDAL-INVARIANCE-001`

`tau_form(P)` is independent of the source-compatible toroidal coordinate.

### Proof

By the protected source admission, changing source-compatible toroidal coordinate changes the finite cyclic quotient by a group automorphism and preserves the order of `theta_form(P)`.

The cyclic group

`Z_2/2^{m_2}Z_2`

has the property that an element represented by `t` has order

`2^{m_2-min(m_2,ord_2(t))}`.

Thus its element order determines its truncated valuation uniquely. Since the element order is toroidal-coordinate invariant, so is `tau_form(P)`. QED.

Hence the notation `tau_form(P)` is canonical for the selected local datum even though neither `k`, `gamma`, nor a scalar lift is canonical.

## 5. Exact order formula

### Theorem `BSD-A1-WP29-FORMAL-DEPTH-001`

The formal order depth satisfies

`s_form(P)=m_2-tau_form(P)`.

Equivalently,

`ord(z_form(P))
 = ord(theta_form(P))
 = 2^{m_2-tau_form(P)}`.

### Proof

Use a scalar coordinate. By the preceding lemmas the quotient is isomorphic to

`Z_2/2^{m_2}Z_2`

up to a unit change of modulus. The additive order of a class represented by `t` is exactly

`2^{m_2-min(m_2,ord_2(t))}`.

By definition the truncated valuation is `tau_form(P)`. Theorem `BSD-A1-WP29-ORDER-001` identifies this order with the order of `z_form(P)`. Taking `ord_2` gives the result. QED.

## 6. Exact place-2 and global formulas

### Corollary `BSD-A1-WP29-RHO2-001`

`rho_2(P)
 = r_red(P)+m_2-tau_form(P)`.

### Proof

Protected WP28 gives

`rho_2(P)=r_red(P)+s_form(P)`.

Substitute Theorem `BSD-A1-WP29-FORMAL-DEPTH-001`. QED.

Protected WP26 defines

`rho_bad(P)
 := max_{ell|N} ord_2(ord(comp_ell(P)))`

and proves

`rho_E=max(rho_2(P),rho_bad(P))`.

### Corollary `BSD-A1-WP29-RHOE-001`

`rho_E
 = max(
     r_red(P)+m_2-tau_form(P),
     rho_bad(P)
   )`.

Protected WP24 gives

`len_Z2(C_E^vee)
 = 2m_2
   + sum_{ell|N} ord_2(c_ell)
   - rho_E`.

Hence:

### Corollary `BSD-A1-WP29-CONTROL-LENGTH-001`

`len_Z2(C_E^vee)
 = 2m_2
   + sum_{ell|N} ord_2(c_ell)
   - max(
       r_red(P)+m_2-tau_form(P),
       rho_bad(P)
     )`.

No analytic determinant or BSD equality is used in this substitution.

## 7. Finite case classification

### Case `a_2=+1`

Then

`3-a_2=2`,

`m_2=1`,

and

`tau_form(P) in {0,1}`.

More precisely:

- `tau_form(P)=0` iff the toroidal formal class is the unique nonzero element of the order-`2` quotient; then `s_form(P)=1`;
- `tau_form(P)=1` iff the formal class is zero; then `s_form(P)=0`.

### Case `a_2=-1`

Then

`3-a_2=4`,

`m_2=2`,

and

`tau_form(P) in {0,1,2}`.

More precisely:

- `tau_form(P)=0` iff the toroidal formal class has order `4`; then `s_form(P)=2`;
- `tau_form(P)=1` iff the toroidal formal class has order `2`; then `s_form(P)=1`;
- `tau_form(P)=2` iff the toroidal formal class is zero; then `s_form(P)=0`.

Thus the remaining local D1b uncertainty is a finite congruence-depth question in a quotient of order at most four.

## 8. Refined D1b frontier

WP29 closes the abstract element-order representation boundary

`MISSING_P2_FORMAL_UNIVERSAL_NORM_ORDER_OF_REDUCTION_KILLED_GENERATOR`.

It replaces it with the strictly narrower finite arithmetic boundary

`MISSING_P2_TOROIDAL_FORMAL_COORDINATE_CONGRUENCE_DEPTH`.

The remaining task is to determine

`tau_form(P)`

uniformly for the saturated global generator in the selected branch, or to prove an exact comparison with another protected arithmetic invariant that determines the same truncated valuation.

Natural but currently unproved comparison targets include:

- the protected WP07 unit-root normalization;
- an element-level formal logarithm;
- the WP20 Bockstein/regulator normalization.

These are research directions, not WP29 conclusions.

## 9. Claim firewall

WP29 does not prove:

- a value of `tau_form(P)` for the selected family;
- a canonical scalar representative of `theta_form(P)`;
- `u=alpha` or `u=alpha^(-1)`;
- any unit-multiple comparison between `1-u` and `1-alpha^(-1)` beyond equality of valuations forced by group order;
- a formal-logarithm formula for the selected class;
- a p-adic-height, regulator, or Bockstein identity;
- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

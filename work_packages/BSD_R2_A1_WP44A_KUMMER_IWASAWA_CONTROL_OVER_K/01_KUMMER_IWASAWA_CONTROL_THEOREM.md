# WP44A theorem — exact primitive Kummer Iwasawa control over `K`

## 1. Setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Let `K/Q` be the protected WP09 imaginary quadratic field and let

`Q_infty/Q`

be the cyclotomic `Z_2`-extension. Put

`K_infty := K Q_infty`.

Because `Q_infty` is totally real while `K` is imaginary quadratic,

`K intersect Q_infty = Q`.

Hence

`Gamma_K := Gal(K_infty/K) ~= Gal(Q_infty/Q) ~= Z_2`.

For each finite layer write

`K_n := K Q_n`,

so `[K_n:K]=2^n`.

Let

`A:=E[2^infinity]`, `T:=T_2(E)`.

No new external theorem premise is used. The argument is the protected WP21 primitive-Kummer control proof transported to `K`, together with the protected WP25 universal-norm calculation.

## 2. No `2`-power torsion over `K_infty`

Protected WP12 gives

`Gal(Q(E[2])/Q) ~= GL_2(F_2) ~= S_3`.

Let

`L:=Q(E[2])`.

Since `K/Q` is quadratic,

`K intersect L`

is either `Q` or the unique quadratic subfield of the `S_3`-extension `L/Q`. Therefore the residual image of `G_K` is respectively

`S_3`

or

`A_3 ~= C_3`.

Both groups act transitively on the three nonzero vectors of `E[2]`.

### Theorem `BSD-A1-WP44A-KTORSION-001`

`E(K_infty)[2^infinity]=0`.

### Proof

Let `P` be a nonzero point of `E[2]`. Under either possible residual image over `K`, its orbit has size `3`. Therefore

`[K(P):K]=3`.

Every finite subextension of `K_infty/K` has degree a power of `2`, so no such cubic field can lie in `K_infty`. Thus

`E[2](K_infty)=0`.

If `R in E(K_infty)` had order `2^m`, then `2^(m-1)R` would be a nonzero point of `E[2](K_infty)`, contradiction. QED.

### Corollary `BSD-A1-WP44A-GLOBAL-RESTRICTION-001`

Restriction is an isomorphism

`H^1(K,A) -> H^1(K_infty,A)^Gamma_K`.

### Proof

Inflation-restriction gives

`0 -> H^1(Gamma_K,A^{G_Kinfty})
   -> H^1(K,A)
   -> H^1(K_infty,A)^Gamma_K
   -> H^2(Gamma_K,A^{G_Kinfty})`.

Theorem `KTORSION-001` gives `A^{G_Kinfty}=0`, so both outer groups vanish. QED.

## 3. Primitive Kummer local quotients over `K`

For every finite or infinite algebraic local extension `F` considered here, use the full classical Kummer local condition.

The Kummer sequence gives, exactly as in protected WP21,

`H^1(F,A)/H^1_Kum(F,A)
 ~= H^1(F,E)[2^infinity]`.

For a place `v` of `K`, choose a place `w|v` of `K_infty` and put

`Gamma_v := Gal(K_{infty,w}/K_v)`.

Define

`W_v := H^1(K_v,E)[2^infinity]`,

`W_infty,w := H^1(K_{infty,w},E)[2^infinity]`,

and

`K_v^Kum := ker(W_v -> W_infty,w^Gamma_v)`.

### Lemma `BSD-A1-WP44A-LOCAL-KERNEL-001`

There is a canonical identification

`K_v^Kum
 = H^1(Gamma_v,E(K_{infty,w}))[2^infinity]`.

### Proof

This is the same inflation-restriction argument as protected WP21, now over the local extension `K_{infty,w}/K_v`. No property of the ground field `Q` was used in WP21's proof. QED.

## 4. Exact primitive Kummer control over `K`

Write

`L_K := product_v H^1(K_v,E)[2^infinity]`

and let

`loc_K:H^1(K,A) -> L_K`

be the localization map through the primitive Kummer quotients.

Let

`res_loc:L_K -> L_Kinfty^Gamma_K`

be local restriction and define

`K_loc^Kum := ker(res_loc)`.

Define the actual globally hit primitive control defect

`C_K^Kum := im(loc_K) intersect K_loc^Kum`.

Let

`Sel_K^Kum := Sel_{2^infinity}^{Kum}(E/K)`,

`Sel_Kinfty^Kum := Sel_{2^infinity}^{Kum}(E/K_infty)`.

### Theorem `BSD-A1-WP44A-KCONTROL-001`

Restriction gives a canonical short exact sequence

`0 -> Sel_K^Kum
   -> (Sel_Kinfty^Kum)^Gamma_K
   -> C_K^Kum
   -> 0`.

### Proof

Corollary `GLOBAL-RESTRICTION-001` gives a unique base preimage in `H^1(K,A)` for every invariant global class upstairs. Localization commutes with restriction.

For an invariant primitive Kummer Selmer class upstairs, its unique base preimage has localization in `ker(res_loc)`; since it is a localization of a global class, it lies in `C_K^Kum`. This defines the right-hand map.

Its kernel is exactly the set of base classes whose localization is zero, namely `Sel_K^Kum`.

Conversely every element of `C_K^Kum` is the localization of a global class whose local restrictions vanish upstairs, so its global restriction is an invariant primitive Kummer Selmer class. Therefore the right-hand map is surjective. This is verbatim the structural argument of protected WP21 with `Q` replaced by `K`. QED.

## 5. Exact module-level Iwasawa specialization

Put

`X_Kinfty^Kum := (Sel_Kinfty^Kum)^vee`,

`X_K^Kum := (Sel_K^Kum)^vee`.

The first is a compact module over

`Lambda_K:=Z_2[[Gamma_K]]`.

Pontryagin duality gives:

### Corollary `BSD-A1-WP44A-DUAL-CONTROL-001`

There is a canonical exact sequence

`0 -> (C_K^Kum)^vee
   -> (X_Kinfty^Kum)_Gamma_K
   -> X_K^Kum
   -> 0`.

Thus a literal integral primitive-Kummer Iwasawa module over `K` exists and its ordinary augmentation specialization maps onto the exact base primitive-Kummer dual Selmer module. Its complete module-level specialization kernel is `(C_K^Kum)^vee`.

This is an ordinary module/coinvariant statement. It is not yet a derived-complex specialization theorem for the compact WP39 lattice.

## 6. Local norm-limit Kummer modules

Fix a finite place `v` of `K` with nontrivial decomposition group. Let

`K_{n,w}/K_v`

be the corresponding cofinal local tower. Write

`E(K_{n,w})^hat_2 := inverse_limit_r E(K_{n,w})/2^r E(K_{n,w})`.

Corestriction compatibility of Kummer maps follows directly from the finite Kummer exact sequence: the connecting homomorphism for

`0 -> E[2^r] -> E --2^r--> E -> 0`

commutes with transfer, and transfer on points is the norm. Passing over `r` therefore gives compatible injections

`E(K_{n,w})^hat_2 -> H^1(K_{n,w},T)`.

Define the compact norm-limit module

`M_w^Kum := inverse_limit_n E(K_{n,w})^hat_2`

under local norm maps. It carries the natural action of the local Iwasawa algebra `Z_2[[Gamma_v]]`.

Projection to the base layer gives

`pr_0:M_w^Kum -> E(K_v)^hat_2`.

Let

`N_{w,n}:=N_{K_{n,w}/K_v}E(K_{n,w})`,

`N_w^infty:=intersection_n N_{w,n}`.

### Lemma `BSD-A1-WP44A-NORM-LIMIT-IMAGE-001`

The image of `pr_0` is exactly the `2`-adic completion of `N_w^infty` inside `E(K_v)^hat_2`.

### Proof

Every norm-compatible sequence has base component in every finite-layer norm image, so the image is contained in the completed universal-norm subgroup.

For the reverse inclusion first work in the compact local point groups before `2`-adic completion. Let `x_0 in N_w^infty`. For every integer `m`, choose `y_m in E(K_{m,w})` with

`N_{K_{m,w}/K_v}(y_m)=x_0`.

Norming `y_m` down to every intermediate layer produces a compatible prefix of length `m`. In the compact product

`product_n E(K_{n,w})`,

the conditions

`x_0` fixed and `N_{n+1/n}(x_{n+1})=x_n`

are closed. Every finite collection of these conditions is satisfiable by choosing a lift from a sufficiently high finite layer as above. Compactness and the finite-intersection property therefore give a full norm-compatible sequence with base component `x_0`.

Passing to the pro-`2` completions preserves the resulting image statement. QED.

Protected WP25 proves that the quotient

`U_w := E(K_v)/N_w^infty`

is a finite `2`-primary group at every relevant place. Therefore completion does not alter this quotient.

### Theorem `BSD-A1-WP44A-LOCAL-AUGMENTATION-COKERNEL-001`

There is a canonical exact sequence of compact `Z_2`-modules

`M_w^Kum --pr_0--> E(K_v)^hat_2 -> U_w -> 0`.

Equivalently, the cokernel of base projection from the literal norm-limit Kummer module is exactly the protected universal-norm defect `U_w`.

No assertion is made that `pr_0` is injective or that ordinary coinvariants compute its derived specialization.

## 7. Transport to the protected all-split field `K`

Protected WP09 makes `2` and every `ell|N` split in `K`. Hence for each place `w` above such a rational prime `v`,

`K_w ~= Q_v`,

and the local cyclotomic tower is the corresponding protected local cyclotomic tower of WP22–WP28.

Thus protected WP25–WP28 apply place-for-place.

### Corollary `BSD-A1-WP44A-LOCAL-LENGTHS-001`

For each `w|2`,

`len_Z2 U_w = 2 ord_2(3-a_2)`,

and there is a canonical exact filtration

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with both end terms of order `3-a_2`.

For each `w|ell`, `ell|N` odd,

`U_w ~= Phi_ell/Phi_ell,odd`

canonically and

`len_Z2 U_w=ord_2(c_ell)`.

At odd good primes the local universal-norm defect is zero.

### Consequence for comparison with WP39

WP39's finite strict-to-Kummer ambient target has, at each `w|2`, length

`ord_2(3-a_2)`,

whereas the full Kummer norm-limit augmentation cokernel has twice that length. Protected WP28 exhibits the extra term explicitly as the formal universal-norm subgroup `F_w^norm`.

At odd bad split places, the augmentation cokernel and the WP39 local target have the same exact `2`-adic length `ord_2(c_ell)` and are both represented by Néron-component data, but WP44A does not silently identify the two maps. The map-level identification belongs to the derived strict-to-Kummer comparison still to be constructed.

## 8. Refined D2b boundary

WP43A left

`MISSING_P2_KUMMER_IWASAWA_LOCAL_CONDITION_COMPLEX_AND_SPECIALIZATION_OVER_K`.

WP44A closes the module-level existence and ordinary cohomological-control parts:

- the primitive Kummer cyclotomic Selmer module over `K` exists integrally at `p=2`;
- ordinary coinvariant specialization is exact with explicit kernel `(C_K^Kum)^vee`;
- the local norm-limit Kummer module exists;
- its base projection cokernel is exactly the protected universal-norm quotient `U_w`.

The remaining boundary is therefore

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

A successor must lift these module-level objects to a compact Selmer-complex local condition compatible with the protected strict Greenberg complex, compute the derived augmentation kernel/Tor term, and identify the specialized comparison cone exactly with WP39/WP40 rather than only by equal lengths.

## 9. Claim firewall

WP44A does not prove:

- that `X_Kinfty^Kum` is the same object as the compact rank-one WP39 Kummer lattice;
- perfectness of a compact classical-Kummer Selmer complex over `Lambda_K`;
- injectivity of `pr_0`;
- vanishing of `Tor_1^{Lambda_K}(-,Z_2)`;
- equality between the full local augmentation defect `U_w` and WP39's local target at `w|2`;
- a map-level identification of the odd bad local modules merely from equality of lengths;
- that `D_K` is a Bockstein image, kernel, cokernel, or radical;
- fixed-`2` height nondegeneracy;
- the height-one `(2)` analytic determinant generator;
- global `Q^ord=1`;
- classical Gross–Zagier/WP00 normalization or final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
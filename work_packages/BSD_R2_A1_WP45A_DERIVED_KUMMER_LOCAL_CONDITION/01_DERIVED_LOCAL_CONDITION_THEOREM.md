# WP45A theorem — derived norm-limit Kummer point module and exact augmentation defect

## 1. Setup

Retain the protected WP44A notation. Let

`K_infty/K`

be the cyclotomic `Z_2`-extension and fix a finite place `w` of `K`. After replacing the tower by its cofinal local decomposition tower when necessary, write

`F_n:=K_{n,w}`, `F_0:=K_w`,

`Gamma_w:=Gal(F_infty/F_0) ~= Z_2`,

`Lambda_w:=Z_2[[Gamma_w]]`.

Put

`A_n:=E(F_n)^hat_2`.

The transition map

`A_{n+1} -> A_n`

is the completed local norm. Protected WP44A defines

`M_w^Kum:=inverse_limit_n A_n`.

The finite-level Kummer connecting maps

`A_n -> H^1(F_n,T_2(E))`

are compatible with norm/corestriction on cohomology. WP45A uses this only as a cohomological normic compatibility statement. It does not assert that these maps have already been lifted canonically to morphisms of local-condition complexes.

## 2. Mittag–Leffler property of the local Kummer point system

### Theorem `BSD-A1-WP45A-ML-001`

The inverse system

`(A_n,N_{n+1/n})_n`

is Mittag–Leffler. Consequently

`R^1 inverse_limit_n A_n=0`.

### Proof

Fix a base level `m` and consider the tail extension

`F_infty/F_m`.

The protected WP25 norm-stabilization argument depends only on the local reduction type and finiteness of the corresponding local cyclotomic control group. Those inputs persist after replacing the original local base by `F_m`.

1. If `w|2`, the curve remains good ordinary over the finite `2`-adic extension `F_m`; the protected literal-`p=2` Tan/Greenberg interfaces apply to the totally ramified cyclotomic tail.
2. If `w` lies above an odd semistable prime, the tail is unramified and the WP22 component-group argument applies after finite unramified base change.
3. At odd good places the same connected-special-fibre argument gives zero `2`-primary control defect.

Thus the raw images

`N_{F_n/F_m}E(F_n) subset E(F_m)`

stabilize for sufficiently large `n`.

The completed norm image is the closure of the raw norm image: `A_n` is compact, the completed norm image is therefore closed, and raw points are dense in the completion. Hence

`im(A_n -> A_m)`

also stabilizes for sufficiently large `n`.

This is the Mittag–Leffler condition. For a countable Mittag–Leffler inverse system of abelian groups,

`R^1 lim=0`.

QED.

### Corollary `BSD-A1-WP45A-RLIM-002`

The derived inverse limit of the compact local point modules is concentrated in degree zero:

`Rlim_n A_n ~= M_w^Kum`.

This is a derived statement about the norm-limit point module only. Constructing a cochain-level Kummer local-condition morphism from this object remains a separate obligation.

## 3. Derived augmentation of the norm-limit point module

Choose a topological generator `gamma_w` of `Gamma_w` and put

`t_w:=gamma_w-1`.

The augmentation module `Z_2` has the length-one free resolution

`0 -> Lambda_w --t_w--> Lambda_w -> Z_2 -> 0`.

Therefore, for every compact `Lambda_w`-module `M`,

`M derived_tensor_{Lambda_w} Z_2`

is represented by

`[M --t_w--> M]`

in cohomological degrees `-1,0`.

Apply this to `M=M_w^Kum`. Define

`T_w^Kum:=M_w^Kum[t_w]`

and

`Q_w^Kum:=(M_w^Kum)_{Gamma_w}`.

Then

`H^{-1}(M_w^Kum derived_tensor Z_2)=T_w^Kum`,

`H^0(M_w^Kum derived_tensor Z_2)=Q_w^Kum`.

Thus `T_w^Kum` is the exact module-theoretic `Tor_1` term. No vanishing is assumed.

## 4. Comparison with the base point module

Protected WP44A supplies the base projection

`pr_0:M_w^Kum -> E(F_0)^hat_2`.

Because the base has trivial `Gamma_w` action, `pr_0` kills `t_wM_w^Kum` and factors through coinvariants:

`bar_pr_0:Q_w^Kum -> E(F_0)^hat_2`.

Define

`B_w^Kum:=ker(bar_pr_0)`.

Protected WP44A proves

`coker(pr_0)=U_w`,

where `U_w` is the finite universal-norm quotient. Since `pr_0` and `bar_pr_0` have the same image,

`coker(bar_pr_0)=U_w`.

Define the purely module-theoretic derived specialization-defect complex

`Delta_w^pt
 := Cone(
      (M_w^Kum derived_tensor_{Lambda_w} Z_2)[-1]
      -> E(F_0)^hat_2[-1]
    )`.

The map here is induced solely by the base projection `bar_pr_0`; `Delta_w^pt` is not being called a Selmer local-condition complex.

### Theorem `BSD-A1-WP45A-DEFECT-003`

The only nonzero cohomology groups of `Delta_w^pt` lie in degrees `-1,0,1`, and canonically

`H^{-1}(Delta_w^pt)=T_w^Kum`,

`H^0(Delta_w^pt)=B_w^Kum`,

`H^1(Delta_w^pt)=U_w`.

### Proof

After shifting by `[-1]`, the source has

`H^0=T_w^Kum`, `H^1=Q_w^Kum`.

The target `E(F_0)^hat_2[-1]` has only

`H^1=E(F_0)^hat_2`.

The long exact cohomology sequence of the cone gives

`H^{-1}(Delta_w^pt) ~= T_w^Kum`,

`H^0(Delta_w^pt) ~= ker(Q_w^Kum -> E(F_0)^hat_2)=B_w^Kum`,

`H^1(Delta_w^pt) ~= coker(Q_w^Kum -> E(F_0)^hat_2)=U_w`.

All other groups vanish. QED.

## 5. Exact arithmetic content of the known `H^1` term

Because every prime dividing `2N` splits in the protected field `K`, protected WP25–WP28 transport place-for-place.

### At `w|2`

Protected WP28 gives

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with both end groups of order `3-a_2`. Hence

`len_Z2 H^1(Delta_w^pt)=2 ord_2(3-a_2)`.

WP39's finite strict/Kummer local target at the same place has length only

`ord_2(3-a_2)`.

Therefore a future cochain-level strict/Kummer comparison must account explicitly for the formal universal-norm term. No cancellation is inferred.

### At odd bad `w|ell`

Protected WP26 gives

`U_w ~= Phi_ell/Phi_ell,odd`

and

`len_Z2 H^1(Delta_w^pt)=ord_2(c_ell)`.

WP39's local target has the same length. Equality of length is not promoted to a canonical map or isomorphism.

### At odd good places

Protected WP25/WP22 gives

`U_w=0`.

The kernel modules `T_w^Kum` and `B_w^Kum` are not thereby forced to vanish.

## 6. Exact status of the Kummer cochain lift

The classical Kummer connecting map

`E(F_n)^hat_2 -> H^1(F_n,T)`

is canonical on cohomology and norm/corestriction compatible. However, a Selmer complex requires a specified local-condition complex and a morphism into a Galois cochain complex, not merely an injection into `H^1`.

WP45A therefore does not use the notation

`M_w^Kum[-1] -> RΓ_Iw(F_0,T)`

as if such a lift were automatic.

A successor may obtain the needed object by one of two valid routes:

1. source-qualify a compact Kummer local-condition complex whose `H^1` realization is the classical Kummer image and whose transition maps are norm/corestriction; or
2. construct such a mapping-fibre/cochain object directly and prove independence of choices plus derived base-change compatibility.

Only after that step may the module defect `Delta_w^pt` be promoted into the local piece of a Selmer-complex specialization triangle.

## 7. Refined D2b boundary

WP44A left

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

WP45A computes the derived norm-limit point-module specialization exactly and identifies the remaining unknown kernel modules. The live boundary is now

`MISSING_P2_COMPACT_KUMMER_COCHAIN_REALIZATION_AND_STRICT_DERIVED_COMPARISON_OVER_K`.

A successor must:

1. construct or source-qualify the compact Kummer local-condition cochain object;
2. bind its norm-limit source to `M_w^Kum`;
3. determine or retain `T_w^Kum` and `B_w^Kum` in derived base change;
4. construct the strict-Greenberg-to-Kummer Iwasawa comparison;
5. identify its specialization map-by-map with WP39/WP40 before relating `D_K` to a Bockstein defect.

## 8. Claim firewall

WP45A does not prove:

- existence of a canonical cochain-level morphism `M_w^Kum[-1] -> RΓ_Iw(F_0,T)`;
- `T_w^Kum=0`;
- `B_w^Kum=0`;
- perfectness of `M_w^Kum` or of a future Kummer Selmer complex;
- map-level equality of odd bad local modules merely from equal lengths;
- cancellation of `F_w^norm` at `w|2`;
- equality of `D_K` with a Bockstein kernel, image, cokernel, or radical;
- fixed-`2` height nondegeneracy;
- D1c;
- global `Q^ord=1`;
- BSD or certification.
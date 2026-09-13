# WP45A theorem — canonical compact Kummer Iwasawa local condition and exact augmentation defect

## 1. Setup

Retain protected WP44A. Let `K_infty/K` be the cyclotomic `Z_2`-extension, with

`Gamma:=Gal(K_infty/K)`, `Lambda:=Z_2[[Gamma]]`.

Fix a finite place `w` of `K`. On its cofinal local decomposition tower write

`F_n:=K_{n,w}`, `F_0:=K_w`,

`Gamma_w:=Gal(F_infty/F_0)`, `Lambda_w:=Z_2[[Gamma_w]]`.

When `Gamma_w` is nontrivial it is an open subgroup of `Gamma` and is isomorphic to `Z_2`. Put

`T:=T_2(E)`, `A_n:=E(F_n)^hat_2`,

with completed local norm as transition map. Protected WP44A defines

`M_w^Kum:=inverse_limit_n A_n`.

## 2. Mittag–Leffler point system

### Theorem `BSD-A1-WP45A-ML-001`

The inverse system `(A_n)_n` is Mittag–Leffler. Hence

`R^1 inverse_limit_n A_n=0`

and

`Rlim_n A_n ~= M_w^Kum`.

### Proof

Fix a base layer `F_m`. The protected WP25 norm-stabilization argument applies to the tail `F_infty/F_m`.

- At `w|2`, good ordinary reduction persists and the protected literal-`p=2` Tan/Greenberg interfaces apply to the totally ramified tail.
- At odd semistable places, the tail is unramified and the protected WP22 component-group calculation applies after finite unramified base change.
- At odd good places the same connected-special-fibre argument gives zero `2`-primary control defect.

Thus the raw images `N_{F_n/F_m}E(F_n)` stabilize. The image of the completed norm `A_n->A_m` is the closure of the raw norm image because the source completion is compact and raw points are dense. Therefore the completed images stabilize as well. This is the Mittag–Leffler property, and the standard countable `Rlim` sequence gives `R^1 lim=0`. QED.

## 3. Canonical Kummer submodule of local Iwasawa `H^1`

For every finite local field `F_n`, the group `E(F_n)[2^infinity]` is finite. Therefore

`H^0(F_n,T)=T^{G_{F_n}}=0`.

Let

`C_{w,infty}:=RΓ_Iw(F_0,T):=Rlim_n RΓ(F_n,T)`

under corestriction. The `Rlim` cohomology sequence gives

`H^1(C_{w,infty}) ~= inverse_limit_n H^1(F_n,T)`

because `R^1 lim H^0(F_n,T)=0`.

At every finite layer the compact Kummer sequence gives a canonical injection

`A_n=E(F_n)^hat_2 -> H^1(F_n,T)`.

These injections commute with norm/corestriction. Taking inverse limits gives a canonical injection

`kappa_{w,infty}:M_w^Kum -> H^1(C_{w,infty})`.

## 4. Canonical simple Kummer local condition

Nekovář local conditions are morphisms of complexes `U^+->C`. Since `H^0(C_{w,infty})=0`, the standard truncation triangle gives

`tau_{<=1}C_{w,infty} -> H^1(C_{w,infty})[-1]`.

Define

`U_{w,infty}^{+,Kum}
 := Fib(
      tau_{<=1}C_{w,infty}
      -> (H^1(C_{w,infty})/M_w^Kum)[-1]
    )`.

It has the canonical local-condition morphism

`i_{w,infty}^{+,Kum}:U_{w,infty}^{+,Kum}->C_{w,infty}`.

### Theorem `BSD-A1-WP45A-LOCAL-COMPLEX-002`

`H^0(U_{w,infty}^{+,Kum})=0`,

`H^1(U_{w,infty}^{+,Kum})=M_w^Kum`,

and all other cohomology vanishes. Hence

`U_{w,infty}^{+,Kum} ~= M_w^Kum[-1]`

in `D(Lambda_w)`, while the morphism into local Iwasawa cochains is canonical.

### Proof

The fibre replaces `H^1(C_{w,infty})` by the kernel of its quotient map, namely `M_w^Kum`; there is no degree-zero term. The long exact cohomology sequence gives the statement. QED.

## 5. Base classical Kummer local condition

At `F_0`, define

`U_{w,0}^{+,Kum}
 := Fib(
      tau_{<=1}RΓ(F_0,T)
      -> (H^1(F_0,T)/E(F_0)^hat_2)[-1]
    )`.

Then

`U_{w,0}^{+,Kum} ~= E(F_0)^hat_2[-1]`

and its degree-one image in `H^1(F_0,T)` is exactly the classical compact Kummer condition used in WP39.

## 6. Global compact Kummer Iwasawa Selmer complex

Local Iwasawa conditions live over decomposition-group algebras. To assemble them over the global algebra `Lambda`, use completed induction.

For each representative base place `w` put

`Ind_w(C):=Lambda completed_tensor_{Lambda_w} C`

when `Gamma_w` is nontrivial; for a trivial local decomposition tower use the evident induced finite-level complex. Define

`U_{S,infty}^{+,Kum}
 := direct_sum_w Ind_w(U_{w,infty}^{+,Kum})`,

`C_{S,infty}^{loc}
 := direct_sum_w Ind_w(C_{w,infty})`.

Let

`C_{K,infty}^{glob}:=RΓ_Iw(K_S/K,T)`.

Define

`C_Kum,infty
 := Cone(
      C_{K,infty}^{glob} direct_sum U_{S,infty}^{+,Kum}
      -> C_{S,infty}^{loc}
    )[-1]`.

At base level define `C_Kum,0` from the local complexes `U_{w,0}^{+,Kum}` by the same Nekovář mapping-fibre construction over `K`.

### Corollary `BSD-A1-WP45A-GLOBAL-COMPLEX-003`

`C_Kum,infty` is a canonical compact Kummer Iwasawa Selmer complex in `D(Lambda)`. Moreover

`H^1(C_Kum,0)=S_2(E/K)`

with the classical compact Kummer local conditions of WP39.

### Proof

Completed induction puts each local condition over the correct global coefficient algebra, so the displayed cone is a Nekovář Selmer complex. At base level its degree-one long exact sequence identifies `H^1` with

`ker(H^1(K,T) -> direct_sum_w H^1(K_w,T)/E(K_w)^hat_2)`,

which is `S_2(E/K)`. QED.

No perfectness claim is made for `C_Kum,infty`.

## 7. Exact local derived augmentation defect

Assume first `Gamma_w~=Z_2`; finite/trivial decomposition towers have no Iwasawa augmentation defect of this type. Choose a topological generator `gamma_w` and put `t_w:=gamma_w-1`.

The augmentation `Lambda_w->Z_2` has free resolution

`0 -> Lambda_w --t_w--> Lambda_w -> Z_2 -> 0`.

Since `U_{w,infty}^{+,Kum}~=M_w^Kum[-1]`, derived augmentation is represented by

`[M_w^Kum --t_w--> M_w^Kum][-1]`.

Define

`T_w^Kum:=M_w^Kum[t_w]`,

`Q_w^Kum:=(M_w^Kum)_{Gamma_w}`.

The protected WP44A base projection

`pr_0:M_w^Kum -> E(F_0)^hat_2`

kills `t_wM_w^Kum`, so it induces

`bar_pr_0:Q_w^Kum -> E(F_0)^hat_2`.

Put

`B_w^Kum:=ker(bar_pr_0)`.

Protected WP44A proves

`coker(bar_pr_0)=U_w`.

Naturality of Iwasawa-cohomology augmentation and the Kummer injections gives a morphism of the canonical fibre constructions

`U_{w,infty}^{+,Kum} derived_tensor_{Lambda_w} Z_2
 -> U_{w,0}^{+,Kum}`.

Let its cone be `Delta_w^Kum`.

### Theorem `BSD-A1-WP45A-DEFECT-004`

The only nonzero cohomology groups of `Delta_w^Kum` are

`H^{-1}(Delta_w^Kum)=T_w^Kum`,

`H^0(Delta_w^Kum)=B_w^Kum`,

`H^1(Delta_w^Kum)=U_w`.

### Proof

After the shift, the augmented Iwasawa local source has `H^0=T_w^Kum` and `H^1=Q_w^Kum`; the base source has only `H^1=E(F_0)^hat_2`. The long exact cohomology sequence of the cone gives exactly the three displayed groups. QED.

## 8. Arithmetic content of `H^1(Delta_w^Kum)`

### At `w|2`

Protected WP28 gives

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with both end groups of order `3-a_2`. Hence

`len_Z2 H^1(Delta_w^Kum)=2 ord_2(3-a_2)`.

WP39's finite strict/Kummer local target has length only `ord_2(3-a_2)`. A future strict/Kummer derived comparison must therefore account explicitly for the formal universal-norm term.

### At odd bad `w|ell`

Protected WP26 gives

`U_w ~= Phi_ell/Phi_ell,odd`,

`len_Z2 H^1(Delta_w^Kum)=ord_2(c_ell)`.

WP39's local target has the same length, but equality of lengths is not promoted to a canonical isomorphism.

### At odd good places

Protected WP22/WP25 gives `U_w=0`. The kernel terms `T_w^Kum` and `B_w^Kum` remain separate obligations.

## 9. Refined D2b boundary

WP44A left

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

WP45A closes:

1. the canonical compact Kummer local-condition cochain realization;
2. the correctly induced global compact Kummer Iwasawa Selmer-complex construction;
3. exact local derived augmentation, up to two explicitly named kernel modules.

The live boundary is

`MISSING_P2_STRICT_TO_KUMMER_IWASAWA_COMPARISON_AND_DERIVED_DEFECT_IDENTIFICATION_OVER_K`.

A successor must:

1. evaluate or retain `T_w^Kum` and `B_w^Kum`;
2. construct the Iwasawa-level morphism from the protected strict Greenberg Selmer complex to `C_Kum,infty`;
3. compare derived augmentation of its cone map-by-map with the finite WP39 comparison;
4. determine how `F_w^norm` at `w|2` enters or cancels;
5. identify the resulting dual finite defect with WP40's `D_K` only after these maps are fixed.

## 10. Claim firewall

WP45A does not prove:

- `T_w^Kum=0`;
- `B_w^Kum=0`;
- perfectness of `C_Kum,infty`;
- existence of the strict-to-Kummer Iwasawa comparison morphism;
- map-level equality of odd bad local modules from equal lengths;
- cancellation of `F_w^norm` at `w|2`;
- equality of `D_K` with a Bockstein kernel, image, cokernel, or radical;
- fixed-`2` height nondegeneracy;
- D1c;
- global `Q^ord=1`;
- BSD or certification.
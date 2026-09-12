# WP45A theorem — canonical compact Kummer Iwasawa local condition and exact augmentation defect

## 1. Setup

Retain the protected WP44A notation. Let

`K_infty/K`

be the cyclotomic `Z_2`-extension and fix a finite place `w` of `K`. After replacing the tower by its cofinal local decomposition tower when necessary, write

`F_n:=K_{n,w}`, `F_0:=K_w`,

`Gamma_w:=Gal(F_infty/F_0) ~= Z_2`,

`Lambda_w:=Z_2[[Gamma_w]]`.

Put

`T:=T_2(E)`,

`A_n:=E(F_n)^hat_2`.

The transition map on `A_n` is the completed local norm. Protected WP44A defines

`M_w^Kum:=inverse_limit_n A_n`.

## 2. Mittag–Leffler property of the point system

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
2. If `w` lies above an odd semistable prime, the tail is unramified and the protected WP22 component-group argument applies after finite unramified base change.
3. At odd good places the same connected-special-fibre argument gives zero `2`-primary control defect.

Thus the raw images

`N_{F_n/F_m}E(F_n) subset E(F_m)`

stabilize for sufficiently large `n`.

The image of the completed norm map `A_n->A_m` is the closure of the raw norm image: `A_n` is compact, the completed norm image is closed, and the raw points are dense. Hence the completed images also stabilize.

This is the Mittag–Leffler condition. For a countable Mittag–Leffler inverse system,

`R^1 lim=0`.

QED.

### Corollary `BSD-A1-WP45A-RLIM-002`

`Rlim_n A_n ~= M_w^Kum`

with `M_w^Kum` concentrated in degree zero.

## 3. Kummer injection into local Iwasawa cohomology

For each finite layer `F_n`, local elliptic-curve torsion is finite. Therefore

`H^0(F_n,T)=T^{G_{F_n}}=0`.

Let

`C_{w,infty}:=RΓ_Iw(F_0,T):=Rlim_n RΓ(F_n,T)`

under corestriction.

The standard `Rlim` cohomology exact sequence gives

`0 -> R^1 lim_n H^0(F_n,T)
   -> H^1(C_{w,infty})
   -> lim_n H^1(F_n,T)
   -> 0`.

The first term is zero because every `H^0(F_n,T)` is zero. Hence

`H^1(C_{w,infty}) ~= lim_n H^1(F_n,T)`.

At every finite layer, the inverse-limit Kummer sequence in the exponent gives a canonical injection

`A_n=E(F_n)^hat_2 -> H^1(F_n,T)`.

These injections commute with norm/corestriction. Taking inverse limits gives a canonical injection

`kappa_{w,infty}:M_w^Kum -> H^1(C_{w,infty})`.

No choice of cocycle representatives is involved in this statement.

## 4. Canonical simple local condition

Protected Nekovář formalism defines a local condition to be a morphism of complexes

`U^+ -> C_{w,infty}`.

We now construct such a morphism canonically from the submodule

`M_w^Kum subset H^1(C_{w,infty})`.

Because `H^0(C_{w,infty})=0`, the standard truncation triangle gives a canonical morphism

`tau_{<=1} C_{w,infty} -> H^1(C_{w,infty})[-1]`.

Compose it with the quotient map

`H^1(C_{w,infty})[-1]
 -> (H^1(C_{w,infty})/M_w^Kum)[-1]`.

Define

`U_{w,infty}^{+,Kum}
 := Fib(
      tau_{<=1} C_{w,infty}
      -> (H^1(C_{w,infty})/M_w^Kum)[-1]
    )`.

The fibre comes with a canonical morphism

`i_{w,infty}^{+,Kum}:U_{w,infty}^{+,Kum}->C_{w,infty}`.

### Theorem `BSD-A1-WP45A-LOCAL-COMPLEX-003`

The local-condition complex satisfies

`H^0(U_{w,infty}^{+,Kum})=0`,

`H^1(U_{w,infty}^{+,Kum})=M_w^Kum`,

and all other cohomology groups vanish. Hence

`U_{w,infty}^{+,Kum} ~= M_w^Kum[-1]`

in `D(Lambda_w)`, while retaining a canonical local-condition morphism to Iwasawa cochains.

### Proof

The truncation object `tau_{<=1}C_{w,infty}` has only `H^0=0` and `H^1=H^1(C_{w,infty})` in the relevant range. Taking the fibre of the quotient on `H^1` replaces that group by its kernel `M_w^Kum` and introduces no degree-zero term. The long exact cohomology sequence gives the assertion. QED.

## 5. Base classical Kummer local condition

At the base field `F_0`, the compact Kummer injection is

`E(F_0)^hat_2 -> H^1(F_0,T)`.

As above, `H^0(F_0,T)=0`. Define

`U_{w,0}^{+,Kum}
 := Fib(
      tau_{<=1}RΓ(F_0,T)
      -> (H^1(F_0,T)/E(F_0)^hat_2)[-1]
    )`.

Then

`H^1(U_{w,0}^{+,Kum})=E(F_0)^hat_2`

and all other cohomology vanishes, so

`U_{w,0}^{+,Kum} ~= E(F_0)^hat_2[-1]`.

This is a simple Selmer local condition whose degree-one image is exactly the classical compact Kummer condition used in WP39.

## 6. Global compact Kummer Iwasawa Selmer complex

Let `S` contain the primes above `2N` and all other places already used by the protected campaign. For each local place use the compact Kummer condition just constructed; at places where the relevant decomposition tower is finite, take the evident finite-level version.

Define the Iwasawa Selmer complex by Nekovář's mapping-fibre construction

`C_Kum,infty
 := Cone(
      RΓ_Iw(K_S/K,T)
      direct_sum (sum_w U_{w,infty}^{+,Kum})
      -> sum_w RΓ_Iw(K_w,T)
    )[-1]`.

Define `C_Kum,0` similarly over `K` using `U_{w,0}^{+,Kum}`.

### Corollary `BSD-A1-WP45A-GLOBAL-COMPLEX-004`

`C_Kum,infty` is a canonical compact Kummer Iwasawa Selmer complex in the derived category. At base level,

`H^1(C_Kum,0)=S_2(E/K)`

with the classical compact Kummer local conditions of WP39.

### Proof

The first assertion is the definition of a Selmer complex from the canonical local-condition morphisms above. For the second, the degree-one cohomology sequence of the mapping fibre identifies `H^1(C_Kum,0)` with the kernel of

`H^1(K,T)
 -> sum_w H^1(K_w,T)/E(K_w)^hat_2`,

which is exactly the compact classical Kummer Selmer group. QED.

No perfectness claim is made for `C_Kum,infty`.

## 7. Derived augmentation of the Kummer local source

Choose a topological generator `gamma_w` and put

`t_w:=gamma_w-1`.

The augmentation module `Z_2` has free resolution

`0 -> Lambda_w --t_w--> Lambda_w -> Z_2 -> 0`.

Since

`U_{w,infty}^{+,Kum} ~= M_w^Kum[-1]`,

derived augmentation is represented by

`[M_w^Kum --t_w--> M_w^Kum][-1]`.

Define

`T_w^Kum:=M_w^Kum[t_w]`,

`Q_w^Kum:=(M_w^Kum)_{Gamma_w}`.

Then the augmented local source has

`H^0=T_w^Kum`,

`H^1=Q_w^Kum`.

The protected WP44A base projection

`pr_0:M_w^Kum -> E(F_0)^hat_2`

kills `t_wM_w^Kum` and factors as

`bar_pr_0:Q_w^Kum -> E(F_0)^hat_2`.

Put

`B_w^Kum:=ker(bar_pr_0)`.

Protected WP44A gives

`coker(bar_pr_0)=U_w`.

Naturality of local Galois cohomology specialization and of the Kummer injections gives a morphism of the canonical fibre constructions

`U_{w,infty}^{+,Kum} derived_tensor_{Lambda_w} Z_2
 -> U_{w,0}^{+,Kum}`.

Define its cone

`Delta_w^Kum`.

### Theorem `BSD-A1-WP45A-DEFECT-005`

The only nonzero cohomology groups of `Delta_w^Kum` are

`H^{-1}(Delta_w^Kum)=T_w^Kum`,

`H^0(Delta_w^Kum)=B_w^Kum`,

`H^1(Delta_w^Kum)=U_w`.

### Proof

Under the canonical quasi-isomorphisms of Sections 4–5, the specialization morphism is induced by `bar_pr_0`. The long exact cohomology sequence of the cone therefore gives exactly the three displayed groups. QED.

## 8. Exact arithmetic content of `H^1(Delta_w^Kum)`

### At `w|2`

Protected WP28 gives

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with both end groups of order `3-a_2`. Hence

`len_Z2 H^1(Delta_w^Kum)=2 ord_2(3-a_2)`.

WP39's finite strict/Kummer local target has length only

`ord_2(3-a_2)`.

Any strict/Kummer derived comparison must therefore account explicitly for the formal universal-norm term. No cancellation is inferred.

### At odd bad `w|ell`

Protected WP26 gives

`U_w ~= Phi_ell/Phi_ell,odd`,

`len_Z2 H^1(Delta_w^Kum)=ord_2(c_ell)`.

WP39's local target has the same length, but equality of lengths is not promoted to a canonical isomorphism.

### At odd good places

`U_w=0` by protected WP22/WP25. The kernel terms `T_w^Kum` and `B_w^Kum` remain separate obligations.

## 9. Refined D2b boundary

WP44A left

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

WP45A now closes:

1. the canonical compact Kummer local-condition cochain realization;
2. the global compact Kummer Iwasawa Selmer-complex construction;
3. the exact local derived augmentation defect, up to two explicit kernel modules.

The live boundary is

`MISSING_P2_STRICT_TO_KUMMER_IWASAWA_COMPARISON_AND_DERIVED_DEFECT_IDENTIFICATION_OVER_K`.

A successor must:

1. evaluate or retain `T_w^Kum` and `B_w^Kum`;
2. construct the Iwasawa-level morphism from the protected strict Greenberg Selmer complex to `C_Kum,infty`;
3. compare its derived augmentation map-by-map with the finite WP39 strict/Kummer comparison;
4. determine how the formal term `F_w^norm` at `w|2` enters or cancels in that comparison;
5. identify the resulting dual finite defect with WP40's `D_K` only after those maps are fixed.

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
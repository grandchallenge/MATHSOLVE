# WP45A theorem — derived compact Kummer local condition and exact augmentation defect

## 1. Setup

Retain the protected WP44A notation. Let

`K_infty/K`

be the cyclotomic `Z_2`-extension and fix a finite place `w` of `K`. After replacing the tower by its cofinal local decomposition tower when necessary, write

`F_n:=K_{n,w}`, `F_0:=K_w`,

`Gamma_w:=Gal(F_infty/F_0) ~= Z_2`,

`Lambda_w:=Z_2[[Gamma_w]]`.

Put

`T:=T_2(E)`

and

`A_n:=E(F_n)^hat_2`.

The transition map

`A_{n+1} -> A_n`

is the completed local norm.

Protected WP44A defines

`M_w^Kum:=inverse_limit_n A_n`.

## 2. Finite-level Kummer maps form a normic system

For every `r>=1`, the finite Kummer sequence

`0 -> E[2^r] -> E --2^r--> E -> 0`

gives a connecting map

`E(F_n)/2^r E(F_n) -> H^1(F_n,E[2^r])`.

Naturality of connecting morphisms with respect to transfer identifies norm on local points with corestriction on cohomology. Passing to the inverse limit over `r` gives a compatible compact Kummer map

`kappa_n:A_n -> H^1(F_n,T)`.

Equivalently, in the derived category there is a local-condition morphism

`A_n[-1] -> RΓ(F_n,T)`.

These morphisms commute with the transition maps in `n`.

## 3. Mittag–Leffler property of the local Kummer point system

### Theorem `BSD-A1-WP45A-ML-001`

The inverse system

`(A_n,N_{n+1/n})_n`

is Mittag–Leffler. Consequently

`R^1 inverse_limit_n A_n=0`.

### Proof

Fix a base level `m`. Consider the tail extension

`F_infty/F_m`.

The protected WP25 argument proving stabilization of local norm images depends only on the local reduction type and on finiteness of the corresponding local cyclotomic control group. Those hypotheses persist after replacing the original local base by the finite layer `F_m`:

1. if `w|2`, the curve remains good ordinary over the finite `2`-adic extension `F_m`, and the protected literal-`p=2` Tan/Greenberg interfaces apply to the totally ramified cyclotomic tail;
2. if `w` lies above an odd semistable prime, the tail is unramified and the protected WP22 component-group calculation applies verbatim after finite unramified base change;
3. at odd good places the same WP22 argument gives zero `2`-primary control defect.

Therefore the raw images

`N_{F_n/F_m}E(F_n) subset E(F_m)`

stabilize for all sufficiently large `n`.

Passing to pro-`2` completions does not destroy stabilization. The completed norm image is the closure of the raw norm image: the completed source is compact, its image is closed, and raw points are dense. Thus

`im(A_n -> A_m)`

also stabilizes for sufficiently large `n`.

This is precisely the Mittag–Leffler condition.

For a countable Mittag–Leffler inverse system of abelian groups, the first derived inverse limit vanishes. Hence

`R^1 lim_n A_n=0`. QED.

### Corollary `BSD-A1-WP45A-RLIM-002`

The derived inverse limit of the finite-level Kummer local-condition sources is concentrated in one degree:

`Rlim_n A_n[-1] ~= M_w^Kum[-1]`.

The compatible finite-level Kummer maps therefore induce a literal Iwasawa local-condition morphism

`U_{w,infty}^Kum:=M_w^Kum[-1]
 -> RΓ_Iw(F_0,T)`,

where the target denotes the corestriction derived inverse limit of local Galois cohomology.

No perfectness assertion is needed for this construction.

## 4. Derived augmentation of the local Kummer source

Choose a topological generator `gamma_w` of `Gamma_w` and put

`t_w:=gamma_w-1`.

The augmentation module `Z_2` has the length-one free resolution

`0 -> Lambda_w --t_w--> Lambda_w -> Z_2 -> 0`.

Therefore, for an arbitrary compact `Lambda_w`-module `M`,

`M derived_tensor_{Lambda_w} Z_2`

is represented by the two-term complex

`[M --t_w--> M]`

in cohomological degrees `-1,0`.

Apply this to `M=M_w^Kum`. Define

`T_w^Kum:=M_w^Kum[t_w]
 = {x in M_w^Kum : t_w x=0}`

and

`Q_w^Kum:=(M_w^Kum)_{Gamma_w}
 = M_w^Kum/t_w M_w^Kum`.

Then

`H^{-1}(M_w^Kum derived_tensor Z_2)=T_w^Kum`,

`H^0(M_w^Kum derived_tensor Z_2)=Q_w^Kum`.

The module `T_w^Kum` is the exact local `Tor_1` term. WP45A does not assume it vanishes.

## 5. Comparison with the base Kummer condition

The protected WP44A base projection

`pr_0:M_w^Kum -> E(F_0)^hat_2`

is `Gamma_w`-invariant, so it kills `t_w M_w^Kum` and factors canonically through coinvariants:

`bar_pr_0:Q_w^Kum -> E(F_0)^hat_2`.

Define

`B_w^Kum:=ker(bar_pr_0)`.

Protected WP44A proves

`coker(pr_0)=U_w`,

where

`U_w:=E(F_0)/N_w^infinity`

is the finite universal-norm quotient. Since `pr_0` and `bar_pr_0` have the same image,

`coker(bar_pr_0)=U_w`.

Define the derived local specialization-defect complex

`Delta_w^Kum
 := Cone(
      (M_w^Kum derived_tensor_{Lambda_w} Z_2)[-1]
      -> E(F_0)^hat_2[-1]
    )`.

### Theorem `BSD-A1-WP45A-DEFECT-003`

The only nonzero cohomology groups of `Delta_w^Kum` lie in degrees `-1,0,1`, and there are canonical identifications

`H^{-1}(Delta_w^Kum)=T_w^Kum`,

`H^0(Delta_w^Kum)=B_w^Kum`,

`H^1(Delta_w^Kum)=U_w`.

### Proof

The derived augmentation source has cohomology

`H^0=T_w^Kum`, `H^1=Q_w^Kum`

after the shift by `[-1]`. The base Kummer source `E(F_0)^hat_2[-1]` has only

`H^1=E(F_0)^hat_2`.

Apply the long exact cohomology sequence of the defining cone. It gives successively

`H^{-1}(Delta_w^Kum) ~= T_w^Kum`,

`H^0(Delta_w^Kum) ~= ker(Q_w^Kum -> E(F_0)^hat_2)=B_w^Kum`,

and

`H^1(Delta_w^Kum) ~= coker(Q_w^Kum -> E(F_0)^hat_2)=U_w`.

All other groups vanish. QED.

## 6. Exact arithmetic content of the known `H^1` term

Because every prime dividing `2N` splits in the protected field `K`, protected WP25–WP28 apply to every place above such a rational prime.

### At `w|2`

Protected WP28 gives

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with

`#F_w^norm=#E_tilde(F_2)=3-a_2`.

Hence

`len_Z2 H^1(Delta_w^Kum)
 =2 ord_2(3-a_2)`.

The finite WP39 strict/Kummer local target at the same place has only

`len_Z2 R_w=ord_2(3-a_2)`.

Thus any derived strict/Kummer comparison must account explicitly for the formal universal-norm term. Equality of total local lengths is impossible here and no cancellation is inferred.

### At odd bad `w|ell`

Protected WP26 gives

`U_w ~= Phi_ell/Phi_ell,odd`

and

`len_Z2 H^1(Delta_w^Kum)=ord_2(c_ell)`.

WP39's local target has the same length. This numerical agreement is not promoted to a map-level isomorphism.

### At odd good places

Protected WP25/WP22 gives

`U_w=0`.

The remaining derived kernel terms `T_w^Kum` and `B_w^Kum` are not thereby forced to vanish.

## 7. Refined D2b boundary

WP44A left

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

WP45A closes the local-condition complex lift and computes its derived augmentation defect exactly up to two named kernel modules. The remaining boundary is

`MISSING_P2_STRICT_KUMMER_DERIVED_COMPARISON_CONE_AND_KERNEL_EVALUATION_OVER_K`.

A successor must:

1. determine `T_w^Kum=M_w^Kum[gamma_w-1]` and `B_w^Kum=ker((M_w^Kum)_{Gamma_w}->E(K_w)^hat_2)` at the relevant places;
2. assemble `U_{w,infty}^Kum` into the global compact Kummer Iwasawa Selmer complex;
3. construct the strict-Greenberg-to-Kummer morphism at Iwasawa level;
4. compare its derived augmentation map-by-map with the protected finite WP39 comparison;
5. identify the resulting dual finite defect with WP40's `D_K` only after this comparison is established.

## 8. Claim firewall

WP45A does not prove:

- `T_w^Kum=0`;
- `B_w^Kum=0`;
- perfectness of `M_w^Kum` or the future global compact Kummer Selmer complex;
- map-level equality of the odd bad `U_w` and WP39 local target merely from equal lengths;
- cancellation of `F_w^norm` at `w|2`;
- equality of `D_K` with a Bockstein kernel, image, cokernel, or radical;
- fixed-`2` height nondegeneracy;
- D1c;
- global `Q^ord=1`;
- BSD or certification.
# WP44A comparison ledger

## Purpose

This ledger separates three different Kummer objects that must not be conflated.

## 1. Discrete primitive Kummer Selmer over the cyclotomic tower

`Sel_Kinfty^Kum := Sel_{2^infinity}^{Kum}(E/K_infty)`

is the direct-limit primitive Kummer Selmer group for `A=E[2^infinity]`.

Its Pontryagin dual

`X_Kinfty^Kum`

is a compact `Lambda_K`-module. WP44A proves ordinary augmentation control

`0 -> (C_K^Kum)^vee
   -> (X_Kinfty^Kum)_Gamma_K
   -> X_K^Kum
   -> 0`.

This is the exact analogue over `K` of protected WP21.

It is **not** identified with the compact rank-one Selmer lattice `S_2(E/K)` occurring in WP39.

## 2. Local norm-limit Kummer module

At a local place `w`, define

`M_w^Kum := inverse_limit_n E(K_{n,w})^hat_2`

under norms. Kummer maps embed this norm-compatible point module into local Iwasawa cohomology.

WP44A proves the base projection has exact cokernel

`U_w`.

Thus `U_w` is the local module-level augmentation obstruction for the norm-compatible classical Kummer point condition.

### At `w|2`

Protected WP28 gives

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with

`#F_w^norm=#E_tilde(F_2)=3-a_2`.

Therefore

`len U_w=2 ord_2(3-a_2)`.

WP39's local strict/Kummer target at the same place has only

`len R_w=ord_2(3-a_2)`.

Consequently the full Kummer norm-limit augmentation defect cannot simply be renamed `R_w`. The formal universal-norm term must be carried through the derived comparison.

### At an odd bad split place `w|ell`

Protected WP26 gives

`U_w ~= Phi_ell/Phi_ell,odd`

and

`len U_w=ord_2(c_ell)`.

WP39's local target `R_w` has the same length. Both arise from the finite Néron-component discrepancy, but a map-level identification has not yet been protected and is not inferred from length equality alone.

## 3. Compact Kummer lattice over `K`

WP39 uses

`S_K^Kum := S_2(E/K)=inverse_limit_r Sel(E/K,2^r)`

and proves

`0 -> H_K^ext -> S_K^Kum -> J_K -> 0`.

This is the compact rank-one lattice relevant to the Nekovář height comparison.

The missing derived object must interpolate this **compact** Kummer local condition over `Lambda_K`, not merely the discrete `A`-Selmer dual of Section 1.

## Exact progress after WP44A

Closed:

1. literal integral `p=2` primitive Kummer cyclotomic module over `K`;
2. exact ordinary cohomological control over `K`;
3. literal norm-limit Kummer local module;
4. exact local base-projection cokernel `U_w`;
5. exact good-ordinary filtration showing the extra formal norm term.

Open:

1. compact Kummer local-condition complex over `Lambda_K`;
2. perfectness/controlled amplitude of that complex;
3. derived augmentation and `Tor_1` accounting;
4. map-level comparison with the protected strict Greenberg complex;
5. exact specialization of the comparison cone to WP39's `R_K`, `J_K`, and WP40's `D_K`.

## Refined boundary

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

No equality of finite lengths is promoted to an isomorphism without a map.
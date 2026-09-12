# BSD-R2-A1 WP45A — canonical compact Kummer Iwasawa local condition and derived defect

## State

`PROVED_BOUNDED_DERIVED_KUMMER_CONSTRUCTION`

## Protected predecessors

- MATHSOLVE WP44A: `b0ac5c0b385a2ef72f62baf637d7d213381b405c`.
- WP25–WP28: exact local norm stabilization and universal-norm quotients.
- WP39/WP40: finite strict-Greenberg/compact-Kummer comparison and Poitou–Tate dual hit over `K`.
- WP43A and its protected Nekovář source premise: Selmer local conditions are morphisms of complexes and the strict Greenberg Iwasawa complex is compatible with cyclotomic augmentation.

No new external theorem premise is used.

## Result

For each relevant place `w` of the protected imaginary quadratic field `K`, put

`A_{w,n}:=E(K_{n,w})^hat_2`,

`M_w^Kum:=inverse_limit_n A_{w,n}`

under local norm.

WP45A proves the point system is Mittag–Leffler, hence

`R^1 lim_n A_{w,n}=0`.

Every finite local field has finite `2`-power torsion on `E`, so

`H^0(K_{n,w},T_2(E))=0`.

Consequently local Iwasawa cohomology satisfies

`H^1_Iw(K_w,T_2(E)) ~= inverse_limit_n H^1(K_{n,w},T_2(E))`,

and the norm/corestriction-compatible finite Kummer injections give a canonical injection

`M_w^Kum -> H^1_Iw(K_w,T_2(E))`.

Using Nekovář's protected definition of a local condition, define canonically

`U_{w,infty}^{+,Kum}
 := Fib(
      tau_{<=1} RΓ_Iw(K_w,T)
      -> (H^1_Iw(K_w,T)/M_w^Kum)[-1]
    )`.

Then

`H^0(U_{w,infty}^{+,Kum})=0`,

`H^1(U_{w,infty}^{+,Kum})=M_w^Kum`,

and there is a canonical local-condition morphism

`U_{w,infty}^{+,Kum} -> RΓ_Iw(K_w,T)`.

At the base field the same construction with

`E(K_w)^hat_2 subset H^1(K_w,T)`

gives the classical compact Kummer local condition. Therefore the global compact Kummer Iwasawa Selmer complex can be assembled canonically by Nekovář's mapping-fibre definition. Its base-level degree-one cohomology is the classical compact Kummer Selmer group used in WP39.

For augmentation `Lambda_w=Z_2[[Gamma_w]] -> Z_2`, the local source is quasi-isomorphic to `M_w^Kum[-1]`, so derived specialization is governed by

`[M_w^Kum --(gamma_w-1)--> M_w^Kum][-1]`.

Comparing with the base Kummer local condition gives a canonical local defect complex `Delta_w^Kum` with

`H^{-1}(Delta_w^Kum)=M_w^Kum[gamma_w-1]`,

`H^0(Delta_w^Kum)=ker((M_w^Kum)_{Gamma_w}->E(K_w)^hat_2)`,

`H^1(Delta_w^Kum)=U_w`.

Thus the compact Kummer cochain realization and its local derived specialization defect are explicit. The unknown derived correction consists only of two named kernel modules plus the protected arithmetic cokernel `U_w`.

## Refined boundary

The surviving D2b boundary becomes

`MISSING_P2_STRICT_TO_KUMMER_IWASAWA_COMPARISON_AND_DERIVED_DEFECT_IDENTIFICATION_OVER_K`.

A successor must construct the Iwasawa-level morphism from the protected strict Greenberg Selmer complex to this Kummer Selmer complex, evaluate or retain the two kernel modules, and identify the specialized comparison cone map-by-map with WP39/WP40.

At `w|2`, the protected filtration

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`

must remain visible. No cancellation of `F_w^norm` is authorized before the strict/Kummer derived comparison proves it.

## Claim firewall

WP45A does not prove:

- that either derived kernel module vanishes;
- perfectness of the Kummer Iwasawa Selmer complex;
- existence of the strict-to-Kummer Iwasawa comparison morphism;
- cancellation of the extra formal universal-norm term at `2`;
- that `D_K` is a Bockstein defect;
- fixed-`2` height nondegeneracy;
- D1c;
- global `Q^ord=1`;
- BSD or MATHCERT certification.
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

`M_w^Kum:=inverse_limit_n A_{w,n}`.

WP45A proves the point system is Mittag–Leffler, so `R^1 lim A_{w,n}=0`. Since local `T_2(E)`-invariants vanish at every finite layer,

`H^1_Iw(K_w,T_2(E)) ~= inverse_limit_n H^1(K_{n,w},T_2(E))`,

and the finite Kummer injections give

`M_w^Kum subset H^1_Iw(K_w,T_2(E))`.

The canonical simple local condition is

`U_{w,infty}^{+,Kum}
 := Fib(
      tau_{<=1} RΓ_Iw(K_w,T)
      -> (H^1_Iw(K_w,T)/M_w^Kum)[-1]
    )`.

It has only `H^1=M_w^Kum`. After completed induction from each decomposition subgroup, these local conditions assemble into a compact Kummer Iwasawa Selmer complex over the global Iwasawa algebra. At base level its `H^1` is exactly the classical compact Kummer Selmer group `S_2(E/K)` used in WP39.

For local augmentation `Lambda_w->Z_2`, ambient Iwasawa cohomology specializes exactly to `RΓ(K_w,T)`. Since both ambient degree-zero cohomology groups vanish, the hyper-Tor edge sequence gives

`H^1_Iw(K_w,T)[gamma_w-1]=0`.

Therefore

`M_w^Kum[gamma_w-1]=0`.

Let

`Q_w^Iw:=H^1_Iw(K_w,T)/M_w^Kum`.

The sole remaining derived kernel is

`B_w^Kum
 := ker((M_w^Kum)_{Gamma_w}->E(K_w)^hat_2)
 ~= Q_w^Iw[gamma_w-1]`.

The local derived specialization cone satisfies exactly

`H^{-1}=0`,

`H^0=B_w^Kum`,

`H^1=U_w`,

where `U_w` is the protected universal-norm cokernel.

At `w|2`,

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`

remains explicit.

## Refined boundary

The surviving D2b boundary is

`MISSING_P2_STRICT_TO_KUMMER_IWASAWA_COMPARISON_AND_DERIVED_DEFECT_IDENTIFICATION_OVER_K`.

A successor must construct the Iwasawa-level strict-to-Kummer morphism, evaluate or retain `B_w^Kum=Q_w^Iw[gamma_w-1]`, and identify the derived comparison cone map-by-map with WP39/WP40. The formal place-`2` norm term may not be cancelled before that comparison proves it.

## Claim firewall

WP45A does not prove:

- `B_w^Kum=0`;
- perfectness of the Kummer Iwasawa Selmer complex;
- existence of the strict-to-Kummer Iwasawa comparison morphism;
- cancellation of the extra formal universal-norm term at `2`;
- that `D_K` is a Bockstein defect;
- fixed-`2` height nondegeneracy;
- D1c;
- global `Q^ord=1`;
- BSD or MATHCERT certification.
# BSD-R2-A1 WP45A — derived compact Kummer local condition over the cyclotomic tower

## State

`PROVED_BOUNDED_DERIVED_LOCAL_CONSTRUCTION`

## Protected predecessors

- MATHSOLVE WP44A: `b0ac5c0b385a2ef72f62baf637d7d213381b405c`.
- WP25–WP28: exact local norm stabilization and universal-norm quotients.
- WP39/WP40: finite strict-Greenberg/compact-Kummer comparison and Poitou–Tate dual hit over `K`.
- WP43A: strict-Greenberg first-order cyclotomic augmentation/Bockstein naturality.

No new external theorem premise is used.

## Result

For each relevant place `w` of the protected imaginary quadratic field `K`, let

`A_{w,n}:=E(K_{n,w})^hat_2`

with transition maps given by local norm. The finite-level compact Kummer map gives

`A_{w,n}[-1] -> RΓ(K_{n,w},T_2(E))`.

WP45A proves that the inverse system `(A_{w,n})_n` is Mittag–Leffler: for every finite base layer, the images of sufficiently high norm maps stabilize by the same protected local norm-duality/control argument used in WP25, now applied to the tail of the local cyclotomic tower. Hence

`R^1 lim_n A_{w,n}=0`

and the derived inverse-limit local Kummer condition is represented by the ordinary norm-limit module

`M_w^Kum := lim_n A_{w,n}`

placed in degree one:

`U_{w,infty}^Kum := M_w^Kum[-1]`.

This gives a literal compact local-condition object over the local Iwasawa algebra

`Lambda_w:=Z_2[[Gamma_w]]`.

For augmentation `Lambda_w -> Z_2`, derived specialization is represented by

`[M_w^Kum --(gamma_w-1)--> M_w^Kum][-1]`.

Comparing with the base local Kummer condition

`U_w^Kum:=E(K_w)^hat_2[-1]`

gives an exact derived defect complex `Delta_w^Kum`. Its cohomology is

`H^{-1}(Delta_w^Kum) = M_w^Kum[gamma_w-1]`,

`H^0(Delta_w^Kum) = ker((M_w^Kum)_{Gamma_w} -> E(K_w)^hat_2)`,

`H^1(Delta_w^Kum) = U_w`,

where `U_w` is exactly the protected WP44A/WP25 universal-norm cokernel.

Thus the unknown derived correction is no longer an unspecified finite error. It consists of two explicit kernel modules plus a known cokernel `U_w`.

## Refined boundary

The surviving D2b boundary becomes

`MISSING_P2_STRICT_KUMMER_DERIVED_COMPARISON_CONE_AND_KERNEL_EVALUATION_OVER_K`.

A successor must evaluate the two new kernel modules, assemble the local Kummer conditions into the global compact Selmer complex, compare it map-by-map with the protected strict Greenberg Iwasawa complex, and show exactly how the `U_w` terms specialize to the finite WP39/WP40 comparison data.

At `w|2`, the protected filtration

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`

must remain visible. No cancellation of `F_w^norm` is authorized until the strict/Kummer derived comparison proves it.

## Claim firewall

WP45A does not prove:

- that either kernel module vanishes;
- that the local Kummer complex is perfect over `Lambda_w`;
- that a global compact Kummer Iwasawa Selmer complex is already perfect;
- that the extra formal universal-norm term cancels against the strict side;
- that `D_K` is a Bockstein defect;
- fixed-`2` height nondegeneracy;
- D1c;
- global `Q^ord=1`;
- BSD or MATHCERT certification.
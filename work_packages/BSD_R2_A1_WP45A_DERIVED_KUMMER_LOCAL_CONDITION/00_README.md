# BSD-R2-A1 WP45A — derived norm-limit Kummer point module

## State

`PROVED_BOUNDED_DERIVED_MODULE_CONSTRUCTION`

## Protected predecessors

- MATHSOLVE WP44A: `b0ac5c0b385a2ef72f62baf637d7d213381b405c`.
- WP25–WP28: exact local norm stabilization and universal-norm quotients.
- WP39/WP40: finite strict-Greenberg/compact-Kummer comparison and Poitou–Tate dual hit over `K`.
- WP43A: strict-Greenberg first-order cyclotomic augmentation/Bockstein naturality.

No new external theorem premise is used.

## Result

For each relevant place `w` of the protected imaginary quadratic field `K`, let

`A_{w,n}:=E(K_{n,w})^hat_2`

with transition maps given by local norm and put

`M_w^Kum:=inverse_limit_n A_{w,n}`.

WP45A proves that the inverse system `(A_{w,n})_n` is Mittag–Leffler: for every finite base layer, sufficiently high norm images stabilize by the same protected local norm-duality/control argument used in WP25, applied to the tail of the local cyclotomic tower. Hence

`R^1 lim_n A_{w,n}=0`

and

`Rlim_n A_{w,n} ~= M_w^Kum`.

This is a derived statement about the norm-limit **point module**. WP45A deliberately does not promote the finite-level Kummer connecting homomorphisms on `H^1` to a canonical cochain-level local-condition morphism without constructing that lift.

For augmentation

`Lambda_w:=Z_2[[Gamma_w]] -> Z_2`,

the derived module specialization is represented by

`[M_w^Kum --(gamma_w-1)--> M_w^Kum]`.

The protected WP44A base projection factors through coinvariants

`(M_w^Kum)_{Gamma_w} -> E(K_w)^hat_2`.

Define the purely module-theoretic specialization-defect complex

`Delta_w^pt
 := Cone(
      (M_w^Kum derived_tensor_{Lambda_w} Z_2)[-1]
      -> E(K_w)^hat_2[-1]
    )`.

Then exactly

`H^{-1}(Delta_w^pt)=M_w^Kum[gamma_w-1]`,

`H^0(Delta_w^pt)=ker((M_w^Kum)_{Gamma_w}->E(K_w)^hat_2)`,

`H^1(Delta_w^pt)=U_w`,

where `U_w` is the protected universal-norm cokernel.

Thus the derived point-module defect is no longer an unspecified finite error. It consists of two explicit kernel modules plus the known arithmetic cokernel `U_w`.

## Refined boundary

The surviving D2b boundary becomes

`MISSING_P2_COMPACT_KUMMER_COCHAIN_REALIZATION_AND_STRICT_DERIVED_COMPARISON_OVER_K`.

A successor must:

1. construct a canonical compact Kummer cochain/local-condition object whose `H^1` map is the finite-level classical Kummer connecting map and whose normic source is the protected module `M_w^Kum`;
2. compare that object with Nekovář's protected strict Greenberg Iwasawa complex;
3. evaluate the two module kernels above or show exactly how they enter the comparison cone;
4. identify the specialized strict-to-Kummer comparison map-by-map with WP39/WP40.

At `w|2`, the protected filtration

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`

must remain visible. No cancellation of `F_w^norm` is authorized until the cochain-level strict/Kummer comparison proves it.

## Claim firewall

WP45A does not prove:

- a canonical morphism `M_w^Kum[-1] -> RΓ_Iw(K_w,T)`;
- existence or perfectness of a compact Kummer Iwasawa Selmer complex;
- that either kernel module vanishes;
- that the extra formal universal-norm term cancels against the strict side;
- that `D_K` is a Bockstein defect;
- fixed-`2` height nondegeneracy;
- D1c;
- global `Q^ord=1`;
- BSD or MATHCERT certification.
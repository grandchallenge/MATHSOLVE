# BSD-001 frontier after WP45A

## Protected predecessor

- MATHSOLVE WP44A: `b0ac5c0b385a2ef72f62baf637d7d213381b405c`.

## WP45A closure

The compact Kummer Iwasawa local-condition object over the protected imaginary quadratic field `K` is now constructed canonically in Nekovář's Selmer-complex formalism.

For each local cyclotomic tower,

`M_w^Kum=inverse_limit_n E(K_{n,w})^hat_2`

is the norm-limit point module. WP45A proves this inverse system is Mittag-Leffler and that

`H^1_Iw(K_w,T_2(E)) ~= inverse_limit_n H^1(K_{n,w},T_2(E))`.

The finite Kummer injections therefore give a canonical inclusion

`M_w^Kum subset H^1_Iw(K_w,T)`.

Define the simple local condition

`U_{w,infty}^{+,Kum}
 := Fib(
      tau_{<=1}RΓ_Iw(K_w,T)
      -> (H^1_Iw(K_w,T)/M_w^Kum)[-1]
    )`.

It has only

`H^1=M_w^Kum`.

After completed induction from each decomposition-group algebra, these local conditions assemble into a compact Kummer Iwasawa Selmer complex `C_Kum,infty`; the base-level degree-one cohomology is exactly the classical compact Kummer Selmer group `S_2(E/K)` used in WP39.

## Exact local derived specialization defect

Let

`Q_w^Iw:=H^1_Iw(K_w,T)/M_w^Kum`.

Ambient local Iwasawa augmentation satisfies

`RΓ_Iw(K_w,T) derived_tensor_{Lambda_w} Z_2 ~= RΓ(K_w,T)`.

Both sides have zero `H^0`. The hyper-Tor edge sequence therefore gives

`H^1_Iw(K_w,T)[gamma_w-1]=0`.

Since `M_w^Kum` injects into this ambient module,

`M_w^Kum[gamma_w-1]=0`.

Thus the local Kummer source has no `Tor_1` augmentation term.

Define

`B_w^Kum
 := ker((M_w^Kum)_{Gamma_w}->E(K_w)^hat_2)`.

The exact coinvariant sequence identifies this remaining kernel canonically as

`B_w^Kum ~= Q_w^Iw[gamma_w-1]`.

The local derived specialization cone `Delta_w^Kum` therefore has exactly

`H^{-1}(Delta_w^Kum)=0`,

`H^0(Delta_w^Kum)=B_w^Kum`,

`H^1(Delta_w^Kum)=U_w`,

where `U_w` is the protected universal-norm quotient.

At each `w|2`,

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

and

`len_Z2 U_w=2 ord_2(3-a_2)`.

WP39's finite strict/Kummer local target has length only `ord_2(3-a_2)`. Therefore the formal universal-norm term must be accounted for by the strict-to-Kummer derived comparison and may not be silently removed.

At each odd bad `w|ell`,

`U_w ~= Phi_ell/Phi_ell,odd`,

`len_Z2 U_w=ord_2(c_ell)`.

The matching WP39 local length does not by itself identify the maps.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

The live boundary is now

`MISSING_P2_STRICT_TO_KUMMER_IWASAWA_COMPARISON_AND_DERIVED_DEFECT_IDENTIFICATION_OVER_K`.

A successor must:

1. evaluate or retain `B_w^Kum ~= Q_w^Iw[gamma_w-1]`;
2. construct the Iwasawa-level morphism from the protected strict Greenberg Selmer complex to `C_Kum,infty`;
3. derive the comparison-cone specialization triangle;
4. identify its finite-level maps with WP39's local target and global hit `J_K`;
5. only then identify the dual defect with WP40's `D_K` or with any Bockstein/height datum.

### D2c

Protected WP42B gives

`Q^ord_{2,dt_2^can}=1`.

The next local boundary remains

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP46A — strict-to-Kummer Iwasawa comparison

Use the protected strict local conditions and the WP45A Kummer local conditions to construct a norm-compatible Iwasawa morphism

`C_str,infty -> C_Kum,infty`.

Compute derived augmentation of its cone. The remaining kernel `B_w^Kum`, the place-`2` formal term `F_w^norm`, and the finite quotient `U_w` must stay explicit until map-level cancellation or persistence is proved.

### WP46B — split semistable bad-prime `Q^ord` factors

Bind the exact bad-prime newvector in Disegni's `v`-new packet to an essential Whittaker vector and evaluate both normalized GL2×GL1 zeta integrals, including the precise local Haar-measure scalar and denominator pairing. Do not infer a unit from an interpolation theorem alone.

## Claim firewall

Do not promote:

- a canonical Kummer Iwasawa complex to perfectness;
- `B_w^Kum` to zero;
- the full `U_w` at `2` to WP39's reduction-sized local target;
- equal lengths at odd bad primes to a canonical isomorphism;
- the formal universal-norm term to zero;
- `D_K` to a Bockstein defect before the comparison cone is fixed;
- canonical `Q^ord_2=1` to global `Q^ord=1`;
- BSD, certification, novelty, or priority.
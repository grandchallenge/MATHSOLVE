# BSD-001 frontier after WP44A

## Protected predecessors

- MATHSOLVE WP43A: `608250fd6e666ef73064505ed83f4ff9629803d9`.
- MATHFORGE WP43A source premise: `d7114e8c61ff0fb414e95a162800a7199f1dec0a`.

## WP44A closure

The campaign no longer lacks an integral primitive-Kummer cyclotomic module over the protected imaginary quadratic field `K`.

Put

`K_infty=K Q_infty`, `Gamma_K=Gal(K_infty/K)`.

WP44A proves

`E(K_infty)[2^infinity]=0`

and therefore transports the protected WP21 primitive Kummer control theorem to `K`:

`0 -> Sel_K^Kum
   -> (Sel_Kinfty^Kum)^Gamma_K
   -> C_K^Kum
   -> 0`.

After Pontryagin duality,

`0 -> (C_K^Kum)^vee
   -> (X_Kinfty^Kum)_Gamma_K
   -> X_K^Kum
   -> 0`.

At every relevant local place `w`, the norm-compatible local Kummer point module

`M_w^Kum=inverse_limit_n E(K_{n,w})^hat_2`

has exact base-projection cokernel

`U_w`.

The completion argument is made explicit using protected WP25 norm-image stabilization and compactness; no unproved commutation of completion with inverse limit is used.

Because `K` splits every prime dividing `2N`, protected WP25–WP28 transport place-for-place. In particular, at each `w|2`,

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with both end terms of order `3-a_2`.

Thus the full Kummer norm-limit augmentation defect at `2` has length

`2 ord_2(3-a_2)`,

while WP39's local strict/Kummer ambient comparison term has length only

`ord_2(3-a_2)`.

The extra formal universal-norm term is explicit and may not be discarded.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

WP40 still gives

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

WP43A closes strict-Greenberg Bockstein naturality. WP44A now closes module-level primitive-Kummer cyclotomic existence and ordinary control over `K`.

The exact remaining boundary is

`MISSING_P2_COMPACT_KUMMER_IWASAWA_COMPLEX_LIFT_AND_DERIVED_SPECIALIZATION_OVER_K`.

A successor must:

1. lift the norm-limit Kummer modules to a compact Kummer local-condition complex over `Lambda_K` compatible with Nekovář's strict complex;
2. establish controlled/perfect derived amplitude;
3. compute derived augmentation, retaining any `Tor_1` or coinvariant kernel;
4. identify the specialized strict-to-Kummer comparison cone map-by-map with WP39's local target and global hit `J_K`;
5. identify the dual specialized defect with WP40's `D_K` only after the preceding map-level comparison is proved.

Equal lengths are not enough.

### D2c

Protected WP42B proves

`Q^ord_{2,dt_2^can}=1`.

The next local boundary remains

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP45A — compact Kummer derived lift

Construct the compact local Kummer condition over `Lambda_K` from the norm-limit point modules, preferably as an explicit mapping-fibre/local-condition complex. Prove derived augmentation rather than ordinary coinvariant control.

The first target is an exact triangle whose specialization displays the known local `U_w` terms and, at `w|2`, separates the formal universal-norm submodule from the finite reduction quotient. The comparison to WP39 must be map-level.

### WP45B — split semistable bad-prime `Q^ord` factors

Continue the exact local Rankin–Selberg/newvector computation at each odd `ell|N`, preserving multiplicative type, Steinberg twist, Haar measure, local L-factor, denominator pairing, and any Tamagawa-sensitive scalar.

## Claim firewall

Do not promote:

- ordinary Kummer coinvariant control to derived compact-Selmer-complex specialization;
- the discrete Kummer dual `X_Kinfty^Kum` to the compact WP39 lattice;
- equality of local lengths to a canonical isomorphism;
- the full `U_w` at `w|2` to WP39's reduction-sized local target;
- the explicit formal universal-norm term to zero;
- `D_K` to a Bockstein defect before the derived comparison cone is proved;
- canonical `Q^ord_2=1` to global `Q^ord=1`;
- BSD, MATHCERT certification, novelty, or priority.
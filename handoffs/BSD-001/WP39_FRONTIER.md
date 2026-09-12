# BSD-001 frontier after WP39

## Protected predecessors

- MATHSOLVE WP38: `efac1b7eaa9b7d1da42c9d33fbb73516fec93a42`.
- MATHFORGE WP39 source admission: `9de5bac5a18193b9453146dd0db9dee2f34ab06a`.

## WP39 closure

For `T=T_2(E)` over the protected WP09 field `K`, WP39 proves:

`H~^1_f(K,T) ~= S_T^str(K)`

and an exact sequence

`0 -> H~^1_f(K,T) -> S_2(E/K) -> J_K -> 0`,

where `J_K` is the actual global image in the finite strict-Greenberg-to-classical-Kummer local comparison module.

The ambient module has exact length

`2 ord_2(3-a_2) + 2 sum_{ell|N} ord_2(c_ell)`.

Hence the exact D2b correction is the single finite integer

`j_K := len_Z2 J_K`.

No additional quadratic Mordell–Weil free-lattice factor exists by WP38.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

`MISSING_P2_KUMMER_GREENBERG_GLOBAL_HIT_SUBGROUP_OVER_K`.

Every ambient local size is known; only the actual global image `J_K` remains.

### D2c

`MISSING_P2_DISEGNI_INTERPOLATION_FACTOR_VALUATIONS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successor — WP40

Do not return to local-size calculations.

Use the already-protected literal-`p=2` Greenberg Poitou–Tate interface to convert the image subgroup `J_K` into an exact annihilator/character problem for the **pair of Selmer structures**:

- strict Greenberg / Nekovář extended on one side;
- classical Kummer on the other.

The required theorem must keep track of the quotient local structure rather than silently substitute the primitive self-dual Kummer structure.

The concrete target is an exact formula of the form

`J_K = ker(chi_K | R_K)`

or an exact dual equivalent, where `chi_K` is induced by the appropriate compact dual Selmer direction. If the dual Selmer direction has rank greater than one or contains finite terms, retain the full annihilator module rather than forcing a rank-one scalar.

No external premise is needed merely to invoke the already-admitted general Poitou–Tate orthogonality; a new source admission is required only if a stronger local self-duality/comparison theorem is used.

## Claim firewall

Do not promote:

- `J_K=R_K`;
- a rank-one character description before proving the dual compact direction is rank one and torsion-free in the relevant Selmer structure;
- p-adic-height existence to nondegeneracy;
- a local quotient size to a global image size;
- an odd-prime theorem to `p=2`;
- BSD or MATHCERT certification.

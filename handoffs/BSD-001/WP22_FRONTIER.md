# BSD-001 frontier after WP22

## Status and authority

This file is a continuity record for the WP22 candidate. It acquires protected status only when the exact candidate is admitted to protected `main` and read back there.

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Mathematical construction repository: `grandchallenge/MATHSOLVE`.
- External theorem/source admission: `grandchallenge/MATHFORGE`.
- Mathematical certification: `grandchallenge/MATHCERT` only.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

Do not use mutable issue text, conversational history, numerical evidence, or this continuity record as a substitute for protected theorem bytes.

## Inherited exact representation

Protected WP16A, WP16B, WP19, and WP20 reduce the selected target to an exact integral rank-one determinant problem. Protected WP21 then proves that, for the selected surjective residual `E[2] ~= S3` branch, the base-to-cyclotomic primitive-Kummer specialization defect is purely local:

`0 -> C_E^vee -> (X_infty)_Gamma -> X_E -> 0`,

where

`C_E := im(loc_Q) intersect K_loc`

and the ambient local kernels are

`K_v = H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`.

No global degree-one control defect remains.

## WP22 result

WP22 computes the ambient kernel at every odd prime.

For every odd good-reduction prime `ell`,

`K_ell = 0`.

For every odd multiplicative prime of type `I_n`,

- split multiplicative:
  `K_ell ~= (Z/nZ)[2^infinity]`;
- nonsplit multiplicative:
  `K_ell ~= ((Z/nZ)/2(Z/nZ))[2^infinity]`.

Using protected WP13, for every bad odd prime `ell|N`,

`#K_ell = 2^{ord_2(c_ell)}`,

so, with

`K_bad := product_{ell|N} K_ell`,

one has exactly

`len_Z2(K_bad^vee) = sum_{ell|N} ord_2(c_ell)`

and

`Fitt^0_Z2(K_bad^vee)
 = 2^{sum_{ell|N} ord_2(c_ell)} Z_2`.

Thus the Tamagawa valuation subtracted in

`delta_2(E)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   - sum_{ell|N} ord_2(c_ell)`

is exactly the total **ambient odd bad-prime local-control length** in the primitive cyclotomic comparison.

This does not identify the globally realized subgroup `C_E` with the full ambient product.

## Refined D1b frontier

The former boundary

`MISSING_P2_PRIMITIVE_LOCAL_CONTROL_DEFECT_EVALUATION`

is reduced to two exact obligations:

1. `MISSING_P2_GOOD_ORDINARY_LOCAL_CONTROL_KERNEL_AT_2`;
2. `MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`.

The smallest next local tranche is the first obligation: compute

`K_2 = H^1(Gamma_2,E(Q_{infty,2}))[2^infinity]`

for the protected good-ordinary selected branch using the **primitive classical Kummer** condition. Protected WP06/WP07 continue to forbid silently replacing this with a Greenberg/ordinary connected-etale condition.

Only after the ambient place-2 kernel is exact should the campaign solve the Poitou-Tate/global-local incidence problem determining

`C_E = im(loc_Q) intersect (K_2 x K_bad)`.

## Other open determinant obligations

WP21's other exact boundaries remain unchanged:

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

WP22 does not discharge any of these.

## Claim firewall

WP22 does **not** prove:

- the value, finiteness, or vanishing of `K_2`;
- `C_E = K_loc` or `C_E = K_2 x K_bad`;
- surjectivity of global localization onto the bad-prime ambient kernels;
- equality of primitive Kummer and Greenberg conditions at `2`;
- a cyclotomic perfect determinant realization;
- a height-one `(2)` analytic generator;
- the WP20 Bockstein/WP00 normalization;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

## Continuation rule

Before a new theorem mutation, re-fetch protected state and use the protected WP22 theorem bytes if and only if WP22 has been admitted. New external theorem premises must first be admitted through MATHFORGE. Continue through bounded proof, exact-subject non-authoring/read-only Adversary and Referee passes, affected CI, protected merge, protected readback, and owner/handoff maintenance.

Stop only at a genuine theorem, source, authority, authentication, safety, material-state, target-drift, or MATHCERT boundary, and name that boundary exactly.

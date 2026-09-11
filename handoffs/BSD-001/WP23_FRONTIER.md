# BSD-001 frontier after WP23

## Status and authority

This file is a continuity record for the WP23 candidate. It acquires protected status only when the exact candidate is admitted to protected `main` and read back there.

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Protected source authority for WP23: `grandchallenge/MATHFORGE@e6f025896532021a84edf05b54034edc9834a022`.
- Mathematical certification remains exclusively a MATHCERT function.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Protected chain entering WP23

WP21 proves

`0 -> C_E^vee -> (X_infty)_Gamma -> X_E -> 0`,

where

`C_E = im(loc_Q) intersect K_loc`.

WP22 computes all odd-prime ambient local kernels and proves

`len_Z2(K_bad^vee)=sum_{ell|N} ord_2(c_ell)`.

The sole remaining ambient local kernel was the good-ordinary place `2`.

## WP23 result

Using the protected MATHFORGE admission of Greenberg's literal `p=2` primitive Kummer local-control theorem, WP23 proves

`#K_2=#E_tilde(F_2)[2^infinity]^2=(3-a_2)^2`.

Thus

`len_Z2(K_2^vee)=2 ord_2(3-a_2)`,

which is exactly `2` for `a_2=+1` and `4` for `a_2=-1`.

Equivalently,

`Fitt^0_Z2(K_2^vee)=(3-a_2)^2 Z_2`.

Protected WP07's unit-root calculation gives, for the normalization containing

`e_2(E)=(1-alpha^(-1))^2`,

the exact local valuation identity

`len_Z2(K_2^vee)=ord_2(e_2(E))`.

This is not yet an analytic determinant identity or cancellation theorem.

Combining WP22 and WP23 gives the complete ambient finite local-control length

`len_Z2(K_loc^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)`.

In particular `K_loc` is finite, so `C_E` is finite.

## D1b frontier

WP23 closes

`MISSING_P2_GOOD_ORDINARY_LOCAL_CONTROL_KERNEL_AT_2`.

D1b is now exactly

`MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`.

The next substantive question is not another local calculation. It is to determine

`C_E = im(loc_Q) intersect (K_2 x K_bad)`

inside the now-explicit finite ambient group.

The preferred next representation is a Poitou-Tate/global-duality incidence calculation with the primitive classical Kummer local condition. The target is an exact sequence or perfect pairing that computes `C_E`, or computes its quotient inside `K_loc`, without declaring any `2`-power a unit.

A new external theorem premise must first be admitted through MATHFORGE. If an internal Poitou-Tate derivation is sufficient from already protected inputs, use it instead of reopening broad literature screening.

## Other determinant boundaries remain

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

## Claim firewall

WP23 does not prove:

- `C_E=K_loc`;
- global localization surjectivity onto any local factor;
- the order, length, or Fitting ideal of `C_E`;
- equality of finite Kummer and Greenberg local conditions by assumption;
- D1a, D1c, or D2;
- the selected exact equality `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

## Continuation rule

Before a new theorem mutation, re-fetch protected state. Use WP23 only if its exact theorem bytes have been admitted to protected MATHSOLVE `main`. Continue through bounded proof, source admission where necessary, exact-subject non-authoring/read-only Adversary and Referee passes, affected CI/GCL checks, protected merge, protected readback, and owner/handoff maintenance.

Stop only at a genuine theorem, source, authority, authentication, safety, material-state, target-drift, or MATHCERT boundary, and name that boundary exactly.

# BSD-001 frontier after WP24

## Status and authority

This is the continuity record for the WP24 candidate. It acquires protected status only after exact-head admission to MATHSOLVE `main` and protected readback.

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Candidate protected-base MATHSOLVE head: `e27d53e0e1198da5c335e66be3d3ceea2e94acf8`.
- Protected WP24 source authority: `grandchallenge/MATHFORGE@ade028d30e1dc3328a2270dcf6108064a6a8c8d0`.
- Mathematical certification remains exclusively a MATHCERT function.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Protected chain entering WP24

WP21 gives

`0 -> C_E^vee -> (X_infty)_Gamma -> X_E -> 0`,

where

`C_E = im(loc_Q) intersect K_loc`.

WP22 and WP23 compute the entire finite ambient local kernel:

`len_Z2(K_loc^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)`.

Thus the only remaining D1b uncertainty entering WP24 is which ambient local kernel classes are globally realized.

## WP24 representation

The protected Greenberg Poitou-Tate source interface and the selected rank-one Kummer facts yield

`S_{T_2(E)}(Q) ~= E(Q) tensor Z_2 ~= Z_2`.

For a saturated generator `P`, let `t_P` be the corresponding compact Kummer basis class. The product local Tate pairing defines

`chi_P(z) := <z,loc(t_P)>_loc`.

WP24 proves

`im(loc_Q)=ker(chi_P)`

on the primitive quotient relevant to the campaign and therefore exactly

`C_E = ker(chi_P|K_loc)`.

Define

`rho_E := len_Z2 im(chi_P|K_loc)`.

Then

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - rho_E`.

The integer `rho_E` is independent of the chosen saturated generator because a basis change scales `chi_P` by a `Z_2` unit.

## New substantive boundary

The former subgroup boundary

`MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`

is replaced by

`MISSING_P2_GLOBAL_HIT_CHARACTER_IMAGE_LENGTH`.

The next question is scalar:

> determine the exact finite image length `rho_E` of the rank-one Poitou-Tate character on the explicit ambient control kernel.

Do not reopen broad literature screening. First test whether `rho_E` can be represented internally as an exact local universal-norm obstruction of the saturated generator `P`. Protected WP22-WP23 already express every factor of `K_loc` through explicit local cohomology, so finite/infinite cyclic Tate duality is the preferred next representation.

A useful target is to identify the character restriction with the class of `P` in the Pontryagin dual of

`K_loc = K_2 x K_bad`

and determine its order from exact local norm quotients. Any local-norm theorem not already protected must first be admitted through MATHFORGE.

If that order turns out to be the same integral object as the WP20 rank-one Bockstein/regulator factor, prove the comparison exactly; do not identify them by analogy.

## Other determinant boundaries remain

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

The scalar `rho_E` may interact with D2, but WP24 does not merge those boundaries.

## Claim firewall

WP24 does not prove:

- a value of `rho_E`;
- `C_E=K_loc`;
- an exact local-norm formula for `rho_E`;
- a regulator, height, Bockstein, or analytic identification of `rho_E`;
- D1a, D1c, or D2;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

## Continuation rule

Before successor mutation, re-fetch protected state. Use the WP24 theorem only if its exact bytes are protected on MATHSOLVE `main`. Continue through bounded proof, MATHFORGE admission for any new theorem premise, exact-head non-authoring/read-only Adversary and Referee passes, affected ordinary CI/GCL checks, protected merge, protected readback, and #164/handoff maintenance.

Stop only at a genuine theorem, source, authority, authentication, safety, material-state, target-drift, or MATHCERT boundary, and name that boundary exactly.

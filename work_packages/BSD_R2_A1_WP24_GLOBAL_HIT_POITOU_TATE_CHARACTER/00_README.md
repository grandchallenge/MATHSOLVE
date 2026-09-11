# BSD-R2-A1-WP24 — global-hit Poitou–Tate character

## Metadata

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Parent: protected `BSD-R2-A1-WP23-GOOD-ORDINARY-P2-LOCAL-CONTROL`.
- Protected MATHSOLVE baseline: `e27d53e0e1198da5c335e66be3d3ceea2e94acf8`.
- Protected MATHFORGE source admission: `ade028d30e1dc3328a2270dcf6108064a6a8c8d0`.
- Admitted source audit: `sources/BSD-001/GREENBERG_POITOU_TATE_GLOBAL_HIT_SOURCE_AUDIT.md` in MATHFORGE.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: exact global-local representation theorem for the remaining primitive control defect.

## Protected input

Protected WP21 defines

`C_E := im(loc_Q) intersect K_loc`

and proves

`0 -> C_E^vee -> (X_infty)_Gamma -> X_E -> 0`.

Protected WP22 and WP23 compute the complete finite ambient local-control kernel and give

`len_Z2(K_loc^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)`.

The remaining D1b question is therefore global incidence: which elements of this explicit finite ambient group are actually hit by global cohomology?

## WP24 result

Let

`T := T_2(E)`.

Using the protected finite-level Kummer exact sequences, rank one, odd rational torsion, and finiteness of `Sha(E/Q)`, WP24 identifies the compact primitive self-dual Selmer module as

`S_T(Q) ~= E(Q) tensor Z_2 ~= Z_2`.

Choose a saturated generator `P` of the free quotient of `E(Q)` and let

`t_P in S_T(Q)`

be its compact Kummer class.

The protected MATHFORGE admission of Greenberg's literal `p=2` Poitou-Tate interface identifies the image of primitive global localization with the exact annihilator of the localized compact Selmer image. Therefore the product of local Tate pairings defines a character

`chi_P : L_Q -> Q_2/Z_2`,

`chi_P(z) := <z, loc(t_P)>_loc`,

for which

`im(loc_Q) = ker(chi_P)`

on the primitive local quotient relevant to the campaign. Intersecting with the protected finite ambient control kernel gives the exact formula

`C_E = ker(chi_P|K_loc)`.

Thus the former opaque subgroup problem is represented by one finite character image.

Define

`rho_E := len_Z2 im(chi_P|K_loc)`.

Then

`0 -> C_E -> K_loc -> im(chi_P|K_loc) -> 0`

is exact and hence

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - rho_E`.

Equivalently,

`Fitt^0_Z2(C_E^vee)
 = 2^{2 ord_2(3-a_2) + sum_{ell|N} ord_2(c_ell) - rho_E} Z_2`.

The integer `rho_E` is independent of the choice of saturated generator: changing the `Z_2` basis multiplies `chi_P` by a unit and therefore preserves its kernel and image order.

## New narrow boundary

WP24 replaces

`MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`

by the strictly narrower scalar problem

`MISSING_P2_GLOBAL_HIT_CHARACTER_IMAGE_LENGTH`.

The unresolved task is to determine `rho_E` uniformly and exactly, or to absorb the same character image into a protected determinant/Bockstein comparison without losing any power of `2`.

This package does not identify `rho_E` with a regulator, height, norm index, Euler factor, or analytic quantity.

## Other boundaries remain

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

## Claim firewall

WP24 does not prove:

- `C_E=K_loc`;
- `rho_E=0` or any other value of `rho_E`;
- a regulator or height formula for `rho_E`;
- a primitive cyclotomic perfect determinant realization;
- an analytic determinant generator at height one `(2)`;
- the WP20 Bockstein/WP00 normalization;
- the selected exact equality `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

# BSD-R2-A1 WP21 — primitive cyclotomic specialization control

## Purpose

Protected WP20 reduces the selected rank-one `2`-primary BSD target to an arithmetic determinant problem and separates two obligations:

- D1: construct a literal-`p=2` primitive rank-one determinant realization specializing to the protected base module `X_E`;
- D2: identify the associated Bockstein/derivative normalization exactly with the WP00 complex leading term.

WP21 attacks D1 before any main-conjecture input. It proves the exact base-to-cyclotomic **primitive Kummer control sequence** on the protected surjective `E[2] ~= S3` branch.

The result is deliberately weaker than a Mazur control theorem. It does not assert that the local control defect vanishes. Instead it isolates that defect exactly and proves that there is no global cohomological defect.

## Protected input

Start from protected MATHSOLVE `6bfb41402f216069b3b5ed001320170cc411b6cf`.

Use only:

- protected WP12: the selected residual representation `E[2]` is surjective with image `GL_2(F_2) ~= S3`;
- protected WP16B: the base primitive Kummer module
  `X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`;
- elementary Kummer exactness, inflation-restriction, and Pontryagin duality, proved/used explicitly in the theorem file.

No new external theorem premise is imported in WP21.

## Main result

Let `Q_infty/Q` be the cyclotomic `Z_2`-extension, `Gamma := Gal(Q_infty/Q)`, and `A := E[2^infinity]`.

WP21 proves first that

`A(Q_infty)=0`.

The reason is exact and specific to the protected residual branch: any nonzero `2`-power torsion point would yield a nonzero point of `E[2](Q_infty)`, but surjectivity of `E[2]` makes the field of definition of each nonzero `2`-torsion point have degree `3`, whereas every finite subextension of `Q_infty/Q` has `2`-power degree.

Inflation-restriction therefore gives

`H^1(Q,A) ~= H^1(Q_infty,A)^Gamma`.

Thus the global restriction map contributes no control kernel or cokernel.

For every place `v` of `Q`, choose `w|v` in `Q_infty` and write `Gamma_v` for the decomposition group. The local Kummer quotient is exactly

`H^1(Q_v,A)/H^1_Kum(Q_v,A) ~= H^1(Q_v,E)[2^infinity]`.

The local restriction kernel is therefore

`K_v := ker(H^1(Q_v,E)[2^infinity]
             -> H^1(Q_{infty,w},E)[2^infinity]^{Gamma_v})`

and inflation-restriction identifies it with

`H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`.

Let `K_loc` be the kernel of the product local restriction map and let `loc_Q` be the base localization map after quotienting by Kummer conditions. Then define

`C_E := im(loc_Q) intersect K_loc`.

WP21 proves canonically

`0 -> Sel_{2^infinity}^{Kum}(E/Q)
   -> Sel_{2^infinity}^{Kum}(E/Q_infty)^Gamma
   -> C_E -> 0`.

After Pontryagin duality, with

`X_infty := Sel_{2^infinity}^{Kum}(E/Q_infty)^vee`,

there is an exact specialization sequence

`0 -> C_E^vee -> (X_infty)_Gamma -> X_E -> 0`.

## What this removes from D1

A future determinant theorem does not need to guess where base specialization can fail. The complete failure surface is local and is represented by `C_E`.

The global Galois-cohomology step is exact on the selected `S3` branch.

## What remains

WP21 does **not** prove:

- `C_E=0`;
- `C_E` finite;
- a Tamagawa formula for `C_E`;
- equality of primitive Kummer and Greenberg ordinary local conditions at `2`;
- finite generation, torsionness, perfectness, or projective dimension one of `X_infty` over `Lambda=Z_2[[Gamma]]`;
- a square `Lambda`-presentation of `X_infty`;
- an analytic determinant or Kato/Mazur-Tate generator;
- the WP20 D2 normalization;
- `BSD-R2-A1` or any MATHCERT certification.

## Refined D1 frontier

The old single D1 obligation is split into:

- D1a — `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1b — `MISSING_P2_PRIMITIVE_LOCAL_CONTROL_DEFECT_EVALUATION`;
- D1c — `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

D2 remains:

- `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

The next work should attack D1b and D1a directly; do not reopen generic source reconnaissance.
# BSD-001 WP21 frontier handoff

## Protected predecessor

Start from protected WP20 at

`grandchallenge/MATHSOLVE@6bfb41402f216069b3b5ed001320170cc411b6cf`.

WP20 proves the universal rank-one determinant/Bockstein factorization and splits the final arithmetic problem into D1 determinant realization and D2 exact Bockstein/WP00 normalization.

## WP21 result

Let `Q_infty/Q` be the cyclotomic `Z_2`-extension, `Gamma=Gal(Q_infty/Q)`, and `A=E[2^infinity]`.

On the protected surjective residual branch `E[2] ~= S3`, WP21 proves

`E(Q_infty)[2^infinity]=0`

and consequently

`H^1(Q,A) ~= H^1(Q_infty,A)^Gamma`.

Thus there is no global degree-one control defect.

For each base place `v` and a chosen `w|v`, define

`K_v := H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`.

This is exactly the kernel of restriction on the primitive local Kummer quotient

`H^1(Q_v,E)[2^infinity] -> H^1(Q_{infty,w},E)[2^infinity]^{Gamma_v}`.

Let

`C_E := im(loc_Q) intersect K_loc`.

Then WP21 proves

`0 -> Sel_Kum(E/Q)
   -> Sel_Kum(E/Q_infty)^Gamma
   -> C_E -> 0`

and, after Pontryagin duality,

`0 -> C_E^vee
   -> (X_infty)_Gamma
   -> X_E -> 0`.

The augmentation specialization therefore reaches the exact protected base module `X_E`; its complete kernel is the explicit local control module `C_E^vee`.

## Active obligations

D1 has split into:

1. `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
2. `MISSING_P2_PRIMITIVE_LOCAL_CONTROL_DEFECT_EVALUATION`;
3. `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

D2 remains:

4. `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

## Immediate next executable tranche

Attack the local-control term first. Determine the placewise groups

`H^1(Gamma_v,E(Q_{infty,w}))[2^infinity]`

and then the globally hit subgroup `C_E`, retaining:

- the exact good-ordinary local structure at `2` without residual-distinguished shortcuts;
- every bad semistable prime and both WP13 Tamagawa regimes;
- the real-place zero defect.

A nonzero local defect is admissible; compute and carry it rather than treating it as route failure.

In parallel, inspect only source/theorem interfaces that can prove perfectness/determinant realization for this literal primitive cyclotomic object. Do not substitute Greenberg ordinary Selmer unless the exact comparison complex is part of the theorem.

## Claim firewall

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`. WP21 is a control-sequence theorem and route reduction only. No main conjecture, analytic determinant, Bockstein/regulator comparison, or MATHCERT certification is asserted.
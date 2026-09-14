# BSD-001 WP60B frontier — Kriz–Li `(F)` locally obstructed

## Entering protected state

- MATHSOLVE: `8b7ba4e5d888f68ffdaeab748d7d94d764f286fa`.
- MATHFORGE: `a8f72ed64755777870a300053e11659fb1dfff1b`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Owner: `grandchallenge/MATHSOLVE#164`.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## WP60B result

For the protected primitive generator `P`, define

`kappa_2(E,P):=((3-a_2)/2)log_{omega_E}(P)`.

WP60B proves:

1. exact source-normalization transport
   `KL_2(E,K,f)=u_f m_K(f) kappa_2(E,P)`
   with `u_f in Z_2^x`;
2. good ordinary reduction at `2` forces the minimal Weierstrass `A_1` coefficient to be odd;
3. consequently
   `log_{omega_E}(E_1(Q_2)) subset 4Z_2`;
4. therefore
   `kappa_2(E,P) in 2Z_2`
   for every selected curve;
5. hence
   `KL_2(E,K,f) in 2Z_2`
   for every WP09-compatible `K`.

Thus Kriz–Li Assumption `(F)` cannot hold on the protected selected good-ordinary-at-`2` lane.

Disposition:

`KRIZ_LI_F_LOCALLY_OBSTRUCTED_ON_SELECTED_GOOD_ORDINARY_LANE`.

## WP59 R3 disposition

Retire reopening form `R3` on this selected branch:

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

This is a local theorem. It does not claim Kriz–Li `(F)` is impossible for other reduction types.

D2d remains unresolved through the surviving routes `R1`, `R2`, `R4`, and `R5`.

## Genuine Heegner-index boundary

The source Heegner point is indivisible by `2` exactly when

`m_K(f)` is odd.

The unresolved field-varying problem is therefore

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

No logarithmic field-forcing shortcut remains on the selected ordinary lane.

## WP60C disposition

The originally planned computation asking whether `kappa_2(E,P)` might be a unit is superseded by the theorem: it is uniformly even.

A real-data replay is optional regression evidence only. Do not spend the primary research lane sampling a proposition already proved.

If WP60C is continued, redirect it toward discriminating surviving routes, for example exact selected-curve/field Heegner-index parity or twist-L-ratio structure, while preserving the no-proof-from-computation firewall.

## Live theorem boundaries

- `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- downstream `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Highest-value successor

Do not reopen generic Kriz–Li field forcing. Choose between the surviving substantive lanes using protected live evidence:

1. literal-`p=2` Heegner-index parity (`R1` component);
2. exact twist-L-ratio valuation (`R2`);
3. combined exact residual theorem (`R4`);
4. height-one-`(2)` Fitting divisibility/primitivity (`R5`/D1c);
5. fixed-`2` height nondegeneracy (D2a), if a genuinely new theorem interface appears.

A bounded exact real-data campaign may be used to identify which of R1/R2/R4 has the sharpest structure, but it cannot promote a theorem.

## Claim firewall

Do not promote `m_K(f)` to odd, `lambda_D` to a unit, any surviving WP59 route to resolved, D2d, `BSD-R2-A1`, or MATHCERT certification. The local impossibility statement applies only to Kriz–Li `(F)` under the protected selected good-ordinary-at-`2` hypotheses.

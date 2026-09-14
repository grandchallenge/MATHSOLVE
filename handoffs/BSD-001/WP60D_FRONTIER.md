# BSD-001 WP60D frontier — surviving routes after R3 retirement

## Entering protected state

- MATHSOLVE: `8620302bc3b836fc96c0fa157e90d5aa21252108`.
- MATHFORGE: `a8f72ed64755777870a300053e11659fb1dfff1b`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Owner: `grandchallenge/MATHSOLVE#164`.
- Target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## WP60D result

For every WP09-compatible auxiliary field `K` with discriminant `D`, quadratic twisting preserves real connected components:

`c_infinity(E^D)=c_infinity(E)`.

Combining this with protected WP57A/WP58A gives

`R_2(E,K,f)
 =2ord_2(m_K(f))-ord_2(lambda_D)`

`=ord_2(L'(E,1)/(Omega_E Reg_E))
  -1+ord_2(c_infinity(E))`.

Hence `R_2` is independent of `K`.

Equivalently,

`R_2(E,K,f)
 =delta_2(E)
  +sum_{ell|N}ord_2(c_ell)
  -1+ord_2(c_infinity(E))`.

Therefore the selected BSD equality is equivalent to

`R_2(E,K,f)
 =v_2(Fitt^1_{Z_2}(X_E))
  +sum_{ell|N}ord_2(c_ell)
  -1+ord_2(c_infinity(E))`.

## Route classification

### R3

Retired on the selected branch by protected WP60B:

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

### R4

Still logically live, but exactly classified as

`R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.

Do not search for a special auxiliary field to make `R_2` easier: its value cannot vary with `K`.

### R1

Genuine field-dependent input remains:

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`

or stronger exact `ord_2(m_K(f))` control.

### R2

Genuine field-dependent input remains:

`MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.

### R5 / D1c

Protected WP60A-A1 leaves:

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY` remains live.

## Highest-value successor

The next bounded research step should not be another R4 auxiliary-field search. Prefer one of:

1. derive exact selected-lane constraints on `ord_2(lambda_D)` from modular symbols or twist congruences while retaining every WP09 splitting condition;
2. derive exact selected-lane Heegner-index parity by a literal-`2` argument not using Kriz–Li `(F)`;
3. look for a genuinely new literal-`2` source/construction closing the height-one-`(2)` Fitting inequality;
4. if a new fixed-`2` height theorem appears, replay the p-adic Gross–Zagier route exactly.

Because WP59 already screened broad twist-value literature, any new R2 work must be theorem construction or a narrowly identified candidate, not another generic source sweep.

## Claim firewall

WP60D proves invariance and equivalence only. It does not determine the value of `R_2`, `m_K(f)`, `lambda_D`, the Fitting exponent, D2d, D2a, D2e, `BSD-R2-A1`, or any MATHCERT claim.

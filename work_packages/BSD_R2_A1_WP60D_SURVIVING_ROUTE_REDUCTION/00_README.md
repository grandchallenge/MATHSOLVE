# BSD-R2-A1 WP60D — surviving-route reduction

## Purpose

After WP60B proves that Kriz–Li `(F)` is locally obstructed on the selected good-ordinary-at-`2` lane, reassess the surviving WP59 reopening forms without starting another broad source search.

The immediate question is whether `R4`, a direct exact theorem for

`R_2(E,K,f)=2ord_2(m_K(f))-ord_2(lambda_D)`,

contains genuinely auxiliary-field-dependent information.

## Entering protected anchors

- MATHSOLVE: `8620302bc3b836fc96c0fa157e90d5aa21252108`.
- MATHFORGE: `a8f72ed64755777870a300053e11659fb1dfff1b`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Result

WP60D proves:

1. quadratic twisting preserves the number of real connected components,
   `c_infinity(E^D)=c_infinity(E)`;
2. therefore the WP59 combined residual is auxiliary-field invariant:

   `R_2(E,K,f)
    = ord_2(L'(E,1)/(Omega_E Reg_E))
      -1+ord_2(c_infinity(E))`;

3. equivalently,

   `R_2(E,K,f)
    = delta_2(E)
      +sum_{ell|N}ord_2(c_ell)
      -1+ord_2(c_infinity(E))`.

Disposition:

`R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.

R4 remains logically valid as a reopening form, but it is not an auxiliary-field escape route. Any theorem computing `R_2` computes a fixed base-curve quantity.

## Surviving genuine arithmetic inputs

- R1: exact Heegner-index information.
- R2: exact twist-L-ratio information.
- R5: literal-`p=2` height-one-`(2)` determinant/Fitting reciprocity.
- D2a: fixed-`2` height nondegeneracy, if a new theorem can unlock an exact p-adic route.

R3 is retired by WP60B.

## Files

- `01_SURVIVING_ROUTE_REDUCTION_THEOREM.md` — exact twist-topology and R4-invariance theorem.
- `02_CLAIM_LEDGER.yaml` — claim and route ledger.
- `handoffs/BSD-001/WP60D_FRONTIER.md` — successor frontier.

## Non-promotion

WP60D does not determine `R_2`, `m_K(f)`, or `lambda_D`; it does not resolve D2d, BSD-R2-A1, or MATHCERT certification.

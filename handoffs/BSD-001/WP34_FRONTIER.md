# BSD-001 WP34 frontier

## Candidate predecessor identities

WP34 is authored from protected MATHSOLVE

`e6c98a0494514d3b74924139edefc9aecd817c4d`

and protected MATHFORGE source authority

`075b91647c22e12aeb0888496966da162db1d771`.

No WP34 conclusion is protected until exact-head review, affected CI, merge, and protected-main readback complete.

## Candidate WP34 result

Protected WP33 proves

`len_Z2 D_bad^BM
 = tau_bad(E) + sum_{ell|N}v2(c_ell)`,

where

`tau_bad(E)=sum_{ell|N}v2(ell-a_ell)`.

Protected MATHFORGE WP34 binds the source normalization:

- equation (20) fixes the orientation of the odd-bad point-completion module;
- `L_S` is formed by deleting Euler factors at `S`;
- `mu_S` is supported outside `S`;
- the source's Section 6 classical reconciliation theorem is odd-prime only and is not used here.

Comparing two truncation sets differing exactly by the bad primes gives

`v2(L_S^*)-v2(L_{S0}^*)=tau_bad(E)`.

Therefore

`len_Z2 D_bad^BM
 - (v2(L_S^*)-v2(L_{S0}^*))
 = sum_{ell|N}v2(c_ell)
 = len_Z2 K_bad^vee`.

Equivalently, with

`J_bad^an=2^tau_bad(E) Z_2`,

`Fitt^0(D_bad^BM)
 = J_bad^an Fitt^0(K_bad^vee)`.

This closes

`MISSING_P2_BURNS_MACIAS_TORIC_EULER_FACTOR_RECONCILIATION`

at the exact valuation/Fitting-ideal level.

## What remains

No canonical determinant-line generator has been constructed. If needed as a separate intermediate label, the stronger unresolved comparison is

`MISSING_P2_BURNS_MACIAS_CANONICAL_DETERMINANT_LINE_COMPARISON`.

The controlling campaign boundaries remain:

- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`;
- WP31 `MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`.

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED` and MATHCERT remains the only certification authority.

## Recommended next determinant-side tranche

Do not reopen the now-closed odd-bad valuation normalization.

The determinant-side continuation should return to D1a and ask whether the admitted literal-p=2 perfect Selmer complex can be lifted to the cyclotomic rank-one setting with specialization exactly the protected primitive module `X_E`, or with every remaining finite specialization defect computed.

The local D1b/WP31 lane can continue independently by evaluating the finite twisted-reciprocity exponent.

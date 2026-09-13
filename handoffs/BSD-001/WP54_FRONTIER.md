# BSD-001 frontier after WP54A

## Protected predecessors for this frontier candidate

- MATHSOLVE WP53A protected head: `c0ef44b5dca27ccb5823d1e6667899c6777db93d`.
- MATHFORGE WP54 protected head: `52137efd71f1ece6f6a02bbb50c2a3acd21e4b40`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

This frontier becomes authoritative only after the containing WP54A candidate is protected and read back from `main`.

## WP54A result

Choose the Cai–Shu–Tian quotient measure at every finite place and choose the single formal archimedean measure so that Disegni's adelic torus quotient has volume one.

Let

`h_K=#Cl(K)`

and

`u_K=[O_K^x:{+1,-1}]`.

The elementary idelic quotient decomposition gives

`vol(H'(Q)\H'(A))
 = (h_K/u_K) V_infinity product_ell m_ell`.

For the protected auxiliary imaginary quadratic field,

`product_ell m_ell=|D_K|^(-1/2)`,

so volume one forces

`V_infinity=(u_K/h_K)|D_K|^(1/2)`.

Protected MATHFORGE WP54 gives:

- finite quaternion ramification `Sigma=emptyset`;
- selected CST-measure `Q^ord_2=2`;
- `Q^ord_infinity=V_infinity/2`;
- good ramified-discriminant product `|D_K|^(-1/2)`;
- all other good finite factors `1`.

Protected WP53A gives at every odd bad `ell|N`

`Q_ell=1+ell^(-1)`.

The complete source-compatible global factor is therefore exactly

`Q^ord
 = (u_K/h_K) product_{ell|N}(1+ell^(-1))`

and

`ord_2(Q^ord)
 = ord_2(u_K)-ord_2(h_K)
   + sum_{ell|N} ord_2(ell+1)`.

No unspecified unit remains.

## D2c disposition

`MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`

is resolved as

`RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.

Do not identify the explicit class-number/unit or bad-prime factors with another campaign ledger without a separate exact comparison.

## Live campaign boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.
- D2d: `MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successor WP55A — classical Gross–Zagier/WP00 normalization

Transport the now-exact source-compatible p-adic Gross–Zagier/test-vector normalization to the protected WP00 complex BSD normalization. The required output is an exact comparison, with every period, regulator, Manin/modular-degree, class-number/unit, Tamagawa, Euler, and test-vector scalar retained until proved to cancel or combine.

Do not use the phrase “up to a unit”. Do not assume the WP54A `u_K/h_K` or `product(1+ell^(-1))` factors cancel with WP34 or WP00 terms merely because the same primes or auxiliary field occur.

If a materially new external comparison theorem is needed, admit that exact theorem through MATHFORGE first.

## Parallel successor WP54B — narrow D1c screen

Continue only the literal-`p=2`, height-one-`(2)` analytic determinant search. Do not reopen odd-prime or inverted-`2` results already rejected by protected source audits.

## Deferred successor after D2d — exact WP06 descent

D2e remains a separate exact descent obligation. Once D2d has placed the p-adic/complex analytic side in the protected WP00 normalization, replay the protected WP06 quadratic-discrepancy accounting with the WP54A factor inserted. No power of `2` may disappear in descent.

## Firewall

Do not promote:

- `BSD-R2-A1`;
- height existence to fixed-`2` height nondegeneracy;
- any analytic determinant result not literal at height one `(2)`;
- the WP54A class-number/unit or bad-prime factors to cancellation with another ledger without proof;
- source admission to MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

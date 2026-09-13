# BSD-R2-A1 WP54A — exact global `Q^ord` reconciliation

## Operation

`BSD-R2-A1-WP54A-GLOBAL-QORD-RECONCILIATION`

## Protected predecessors

- MATHSOLVE WP53A: `c0ef44b5dca27ccb5823d1e6667899c6777db93d`.
- MATHFORGE WP54 source admission: `52137efd71f1ece6f6a02bbb50c2a3acd21e4b40`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Objective

Protected WP53A computes the exact odd split semistable bad-prime factors in the Cai–Shu–Tian local measure but leaves the global Disegni volume-one rescaling explicit.

WP54A fixes one legal global decomposition: use the CST quotient measure at every finite place, and choose the single formal archimedean measure so that Disegni's adelic torus quotient has volume one. It then computes that archimedean volume by an elementary idelic class-group decomposition and multiplies every finite, `p=2`, and archimedean factor exactly.

## Result

Let `K/Q` be the protected WP09 auxiliary imaginary quadratic field with fundamental discriminant `D_K`. Put

`h_K := #Cl(K)`

and

`u_K := [O_K^x : {+1,-1}]`.

Then the selected source-compatible global ordinary toric factor is exactly

`Q^ord
 = (u_K/h_K)
   * product_{ell|N, ell odd} (1+ell^(-1))`.

Because the selected curve has good reduction at `2`, every prime dividing `N` is odd. Thus equivalently

`Q^ord
 = (u_K/h_K)
   * product_{ell|N} (1+ell^(-1))`.

Hence

`ord_2(Q^ord)
 = ord_2(u_K) - ord_2(h_K)
   + sum_{ell|N} ord_2(ell+1)`.

No local or global factor is discarded as a unit.

The apparent square-root discriminant terms cancel exactly: the product of CST finite compact-quotient volumes at ramified discriminant primes is `|D_K|^(-1/2)`, while the global volume-one condition forces the formal archimedean torus volume to be `u_K |D_K|^(1/2)/h_K`. The selected `p=2` ordinary factor contributes `2`, and the archimedean ordinary factor contributes one half of that formal archimedean volume, so their product is precisely the full formal archimedean volume.

## D2c disposition

WP54A resolves

`MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`

as

`RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.

This is a bounded automorphic-normalization result. It does not close the selected BSD target.

## Surviving boundaries

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`;
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`;
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`;
- D2d: `MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`;
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Claim boundary

WP54A does not prove fixed-`2` height nondegeneracy, a height-one-`(2)` analytic determinant generator, the WP00 classical Gross–Zagier normalization, final quadratic descent, `BSD-R2-A1`, or MATHCERT certification. It also does not identify the class-number factor or the bad-prime toric factors with Tamagawa, determinant, period, or regulator terms absent a separate exact comparison theorem.

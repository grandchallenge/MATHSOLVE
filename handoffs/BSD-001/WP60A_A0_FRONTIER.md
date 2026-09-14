# BSD-001 frontier — WP60A-A0 determinant dependency reduction

## Protected anchors entering A0

- MATHSOLVE: `24fb349e28e4cbb5e034f4684edcc413975aed04`.
- MATHFORGE WP60A audit: `e44baeeed5d508fd4e5332c883c837951e51c000`.
- INTELLECT issuance: `fc9ee5537bf07586dffcc621e753204ecd835365`.
- WP60 execution tracker: `grandchallenge/MATHSOLVE#215`.
- Parent programme owner: `grandchallenge/MATHSOLVE#164`.

This file becomes authoritative only after the containing A0 candidate is protected and read back from `main`.

## A0 result

The determinant spine is already exact on the algebraic side.

Protected WP16A/B and WP19 identify

`Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`

with valuation

`lim_n (ord_2 #Sel_{2^n}(E/Q)-n)`.

Protected WP35 gives the square cyclotomic presentation and exact first-coefficient specialization

`(coeff_T det A(T)) Z_2
 = Fitt^0(C_E^vee) Fitt^1(X_E) B_A`.

Protected WP36 and WP39–WP52A determine the finite control and strict/Kummer determinant corrections. Protected WP53A–WP58A determine the normalization factors on the analytic/Heegner line.

Therefore no new finite algebraic correction is the next target.

### Proposition protected by this tranche

`BSD-A1-WP60A-A0-REDUCTION-001`:

> Closing D1c through the determinantal-zeta route reduces to two distinct literal-`p=2` statements: an integral determinant lift of the analytic/Kato class, or exact finite-level substitute, and an exact primitivity/reverse-divisibility theorem at the height-one prime `(2)`.

A lift alone is insufficient for exact first-Fitting equality.

## Refined D1c sub-boundaries

### A1-LIFT

`MISSING_P2_KATO_ZETA_DETERMINANT_LIFT_AT_RESIDUE_CHARACTERISTIC_2`.

### A1-PRIMITIVITY

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

### Combined refinement

`MISSING_LITERAL_P2_KATO_ZETA_DETERMINANT_LIFT_AND_PRIMITIVITY_AT_HEIGHT_ONE_2`.

The campaign-level parent remains

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

## Provider result used

Protected MATHFORGE `e44baeeed5d508fd4e5332c883c837951e51c000` admits the bounded BKS/BSS audit.

The determinantal-zeta architecture is exactly relevant, but the located lift theorem is not literal `p=2`: BKS Hypothesis 2.2 excludes `p=2`, and the Stark/Kolyvagin regulator mechanism used in its proof invokes a theorem requiring `p>3`.

The provider audit also records that determinant lift and determinant primitivity are separate obligations.

This is an applicability result, not a theorem-nonexistence or literature-exhaustiveness claim.

## Immediate executable successor — WP60A-A1

Attack `A1-LIFT` first.

Preferred route:

1. construct the smallest finite-level perfect Selmer/cohomology complex that still specializes to the protected primitive Kummer first-Fitting line;
2. identify an integral analytic/Kato/modular-symbol class in its first cohomology;
3. prove directly that the class lies in the determinant image over `Z_2`, without invoking the odd-prime Stark/Kolyvagin regulator isomorphism;
4. transport it through the already-protected local and specialization maps;
5. only after a lift is established, attack `A1-PRIMITIVITY` by proving exact reverse divisibility/basis status at `(2)`.

### Required falsification test

Before building a large new theory, reduce determinant membership to the smallest possible finite-module or lattice statement. If determinant membership is equivalent to a divisibility already known to be precisely the missing height-one-`(2)` exponent, record that equivalence and do not relabel the same unknown as a construction.

### Success condition

WP60A closes only if a protected result provides both lift and primitivity, or a direct primitive finite-level Fitting reciprocity theorem of equivalent strength. On such a result, replay WP59 `R5` and then the full D2d line.

## Parallel WP60B

WP60B remains executable in parallel. If A1-LIFT reaches a genuine theorem boundary without a constructive next move, proceed to exact normalization of the Kriz–Li literal-`2` logarithmic condition rather than repeating a broad determinant-source sweep.

## Boundary map

- D1c parent: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- A1-LIFT: `MISSING_P2_KATO_ZETA_DETERMINANT_LIFT_AT_RESIDUE_CHARACTERISTIC_2`.
- A1-PRIMITIVITY: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.
- D2d: `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

No MATHCERT claim is promoted.

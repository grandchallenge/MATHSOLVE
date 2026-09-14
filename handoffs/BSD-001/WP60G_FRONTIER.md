# BSD-001 WP60G frontier — self-dual literal-p=2 pairwise localization

## Protected entering state

- MATHSOLVE: `813156baf3fa57989ddce891f355e2648e99c008`.
- MATHFORGE: `7da6813fcde7eb5f9badd7c86946f58691ed6f0d`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Owner: `grandchallenge/MATHSOLVE#164`.
- Target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## WP60G theorem

For nonzero characters `chi_1,chi_2:G->F_2` and affine fibers

`H_i=chi_i^{-1}(a_i)`,

one has

`H_1 union H_2 = G`

if and only if

`chi_1=chi_2` and `a_1 != a_2`.

Under BSS Hypothesis 3.2 and a `G_K`-equivariant self-duality

`A ~= A^*(1)`,

the BSS maps and affine constants are natural under the self-duality. Therefore the complementary-fiber case cannot occur for one nonzero primal and one nonzero dual class:

- if the two residual characters differ, the two-fiber lemma gives a point outside both bad fibers;
- if they agree, injectivity of the BSS cohomology-to-character map identifies the two cohomology classes under self-duality, and naturality identifies their affine constants, so the two bad fibers coincide rather than complement each other.

The protected BSS Chebotarev calculation then gives positive density of primes where both localizations are nonzero.

## Elliptic specialization

The Weil pairing gives

`E[2] ~= E[2]^*(1)`

`G_Q`-equivariantly. Thus the self-duality input is automatic for the selected residual elliptic module.

This does not prove BSS Hypothesis 3.2/H2/H3 uniformly on the selected lane. WP60F F2 remains live.

## Exact F1 progress

The literal-`2` failure of the published inequality

`s+t<p`

is no longer an obstruction for `s=t=1` in the self-dual residual setting, conditional on the remaining BSS hypotheses.

The pairwise prime-selection step in Lemma 5.14 is therefore repaired at the level of the counting obstruction. The analogous one-primal/one-dual step in Lemma 5.17 is also no longer blocked by that count.

WP60G does not repair Lemma 5.15 with `s=2`. Corollary 5.16 needs one prime satisfying four simultaneous nonvanishing conditions for two minimal core-vertex configurations.

Record the refined frontier:

`MISSING_P2_TWO_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`.

Keep the parent F1 boundary open until enough graph/Kolyvagin control is recovered:

`MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.

## Highest-value successor — WP60H

Attack Corollary 5.16 directly.

Two admissible proof modes:

1. **four-fiber mode:** derive relations among the four BSS affine characters/constants arising from two minimal core vertices that force their union to be proper; or
2. **replacement-connectivity mode:** prove connectivity of minimal core vertices without choosing one common prime satisfying all four constraints.

The second mode should test whether the minimal core vertices admit a basis-exchange or other finite-dimensional duality description. Do not assume a matroid structure until it is proved from the actual BSS modified Selmer conditions.

A generic affine-hyperplane counting argument cannot close the problem: four affine index-two fibers can cover an `F_2`-quotient in general.

## Parallel boundary

F2 remains independent:

`MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

Even a complete solution of the graph problem would not by itself verify the selected elliptic BSS hypotheses.

## Parent route state

- R1: `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Claim firewall

WP60G does not prove full core-vertex connectivity, BSS Fitting control at `2`, H2/H3, R5 closure, `BSD-R2-A1`, or any MATHCERT claim.

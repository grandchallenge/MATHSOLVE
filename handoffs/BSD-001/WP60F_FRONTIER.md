# BSD-001 WP60F frontier — literal-p=2 BSS proof boundaries

## Protected entering state

- MATHSOLVE: `c2f036fd935238a880780685a927c26ec0de2d4e`.
- MATHFORGE: `eaaf7b8c660f3f07030608b3af1334ece5598586`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Owner: `grandchallenge/MATHSOLVE#164`.
- Target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## WP60F result

The BSS finite-level R5 architecture has two distinct literal-`2` proof obligations.

### F1 — core-vertex / simultaneous-localization control

`MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.

The admitted BSS proof uses a simultaneous-localization lemma with `s+t<p`, then a core-vertex connectivity step using `2s<p`; the Kolyvagin-system/Fitting-control theorems downstream are proved under `p>3`.

### F2 — elliptic H2/H3 verification

`MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

The admitted elliptic verification uses a `p>3` large-image/perfectness argument after restriction to the relevant pro-`p` extension. Protected residual surjectivity of `E[2]` is not an admitted substitute.

Exact route classification:

`BSS_LITERAL_P2_R5_ROUTE_REQUIRES_F1_AND_F2`.

The higher-derivative construction and the integral Fitting-control theorem are distinct interfaces. Do not promote the former to the latter.

## Parent R5 boundaries remain live

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- subordinate WP60E boundary: `MISSING_LITERAL_P2_FINITE_LEVEL_KATO_DERIVATIVE_FITTING_THEOREM`.

## Highest-value successor

Attack F1 before spending primary effort on F2.

The next theorem-construction question is whether literal `p=2` and the protected selected two-dimensional representation admit a replacement for the BSS simultaneous-localization/core-vertex step strong enough to recover the one-sided Fitting containment.

Required discrimination:

1. determine whether the failure of `s+t<p` at `p=2` is only a limitation of the subgroup-cover counting proof or reflects an actual representation-theoretic obstruction;
2. exploit the exact selected residual image `GL_2(F_2)` only through proved group/cohomology statements;
3. determine whether one-primal/one-dual simultaneous localization can be forced by a refined Chebotarev argument for this specific representation;
4. if yes, rebuild only the minimum core-vertex connectivity needed for the one-sided Fitting containment and replay WP60A-A1;
5. if no, record an explicit counterexample/obstruction and abandon this BSS subroute without extrapolating to all possible literal-`2` R5 methods.

F2 remains a parallel secondary lane: compute the exact restricted `2`-adic image and H2/H3 conditions rather than inferring them from residual surjectivity.

## Other surviving lanes

- R1: `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Claim firewall

WP60F does not prove a literal-`2` BSS Fitting theorem, failure of higher derivatives at `2`, failure of H2/H3 for every selected curve, closure of R5, `BSD-R2-A1`, or any MATHCERT claim.

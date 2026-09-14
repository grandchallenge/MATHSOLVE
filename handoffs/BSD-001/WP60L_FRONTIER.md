# BSD-001 WP60L continuation frontier

## Protected base entering WP60L

`grandchallenge/MATHSOLVE@303c5662a62c9dda62e9c9f0ba1abae8e27f3b16`.

Operation: `grandchallenge/MATHSOLVE#233`.

## Candidate disposition

WP60K proves that the unchanged finite BSS Hypothesis 3.2(iii) fails at `A=E[4]`.

WP60L proves a narrower replacement at the same coefficient level:

`BSS_LITERAL_P2_SELECTED_MOD4_HYP32III_DEFECT_SELMER_EXTRANEOUS`.

The full finite auxiliary cohomology group has order two, but its unique nonzero class is ramified at the protected odd-depth multiplicative prime. At that prime the propagated BSS canonical condition is the self-dual finite Kummer condition. Hence the defect belongs to neither the primal nor dual canonical local condition, and restriction to the BSS finite auxiliary field is injective on every canonical modified primal and dual Selmer group at `E[4]`.

The one-class Chebotarev calls in the proof of BSS Lemma 3.10 can therefore be replayed at literal `p=2` for free submodules contained in these modified Selmer groups. This repairs the Hypothesis-3.2(iii) contribution to the selected `E[4] -> E[2]` coefficient-reduction step.

## What WP60L does not repair

The BSS Lemma 3.9 counting condition remains `s+t<p`. At `p=2`, simultaneous one-primal/one-dual localization still lies outside the unchanged lemma. WP60G/WP60H give only the protected residual self-dual replacement and its remaining three-term-relation frontier.

WP60L also does not prove the corresponding Selmer-restricted injectivity at `E[8]`, `E[16]`, or arbitrary `E[2^m]`. The BSS inverse-limit Fitting architecture therefore remains unproved.

## Next mathematical frontier

The highest-value BSS-derived successor is

`MISSING_P2_BSS_ALL_LEVEL_SELMER_RESTRICTED_INJECTIVITY_AND_P2_CONNECTIVITY_CONTROL`.

Split it into two independent sub-obligations:

1. **all-level H32(iii) replacement:** determine `H^1(K(E[2^m])_{2^m}/Q,E[2^m])` and prove that every restriction-kernel class is excluded by a fixed canonical local condition for every `m>=2`, or prove an integral replacement directly;
2. **literal-2 connectivity:** resolve or bypass the simultaneous primal/dual localization and WP60H minimal-core three-term-relation obstruction actually needed for core-vertex control.

The all-level calculation should exploit protected full `GL_2(Z_2)` image and the fixed primitive odd-inertia transvection before initiating a broad literature search. In particular, test whether the mod-4 defect inflates canonically to the unique defect at each higher `2`-power level and whether primitive inertia detects it uniformly.

## Independent live routes

Keep active independently:

- R1 — `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`;
- R2 — `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`;
- R4 — `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`;
- R5-LIFT — `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- R5-PRIM — `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

`BSD-R2-A1` remains unproved.

## Firewall

Do not promote WP60L to:

- full Hypothesis 3.2(iii);
- an all-level theorem;
- mod-4 simultaneous primal/dual localization;
- core-vertex connectivity;
- an integral BSS Fitting theorem;
- R5 closure;
- `BSD-R2-A1`;
- MATHCERT certification.

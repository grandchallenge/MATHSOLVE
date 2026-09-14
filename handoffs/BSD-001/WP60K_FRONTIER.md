# BSD-001 WP60K frontier

Protected predecessor: WP60J at

`d5159aabcfb03129ca1ef669f506870974988605`.

## New selected-lane fact

WP60J proves the residual coefficient module `E[2]` satisfies formal literal-`p=2` BSS II Hypotheses 3.2 and 3.3.

WP60K proves the next coefficient level already fails:

`|H^1(GL_2(Z/4),(Z/4)^2)|=2`,

and therefore

`H^1(K(E[4])_4/Q,E[4]) != 0`.

By Weil self-duality the dual clause is nonzero as well.

Record:

`BSS_LITERAL_P2_SELECTED_FINITE_HYP32III_FAILS_AT_E4`

`R5_BSS_STANDARD_FINITE_HYPOTHESIS_ROUTE_BLOCKED_ALREADY_AT_MOD4`.

## Refined BSS route state

The BSS route now has two different proven small-prime obstructions:

1. finite BSS II Hypothesis 3.2(iii) fails already at `E[4]` (WP60K);
2. BSS III infinite `(H3)` fails on the full 2-power division tower (WP60I).

The WP60G/WP60H residual `E[2]` localization results remain valid and unconditional after WP60J, but they cannot by themselves be lifted through the unchanged standard BSS finite control chain.

The replacement-control frontier is

`MISSING_P2_BSS_HYP32III_WEAKENING_OR_BYPASS_FOR_INTEGRAL_FITTING_CONTROL`.

Any BSS-derived successor must identify exactly where the nonzero mod-4 cohomology enters the Kolyvagin-system/Fitting proof and either:

- prove the actual Selmer classes used by the argument avoid the obstructing cohomology direction;
- quotient or modify the finite control construction so the obstruction is harmless;
- replace Hypothesis 3.2(iii) by a weaker injectivity statement sufficient for the needed localization maps; or
- use a different integral Fitting-control architecture.

If a replacement still needs full minimal-core connectivity, the independent residual F1 question remains

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

## Other live routes

- R1: `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`;
- R2: `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`;
- R4: `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`;
- R5-LIFT: `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- R5-PRIM: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

`BSD-R2-A1` remains unproved. MATHCERT is not invoked.

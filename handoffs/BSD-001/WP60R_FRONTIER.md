# BSD-001 WP60R frontier — finite literal-2 BSS theorem replay

## Entering protected state

- MATHSOLVE: `83046d8e227003d277196b25dd7f17bbf5ec717b`.
- MATHFORGE: `8c9b25fdd7dd63428a10f7d4439f5033ea890964`.
- INTELLECT: `fc9ee5537bf07586dffcc621e753204ecd835365`.
- Operation: `grandchallenge/MATHSOLVE#243`.
- Parent tracker: `grandchallenge/MATHSOLVE#215`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Closed boundary

WP60R closes the finite-level proof-replay boundary

`MISSING_LITERAL_P2_BSS_THEOREM_5_20_5_2_REPLAY_AFTER_REPLACEMENTS`.

The replay does not reinstate formal BSS Hypothesis 3.2(iii). Instead, it uses the protected fact that the unique nonzero higher-level restriction-kernel defect is Selmer-extraneous at the fixed canonical local condition.

## New selected finite-level interfaces

WP60R records:

- `BSS_LITERAL_P2_SELECTED_ALL_LEVEL_PAIRWISE_LOCALIZATION_AVAILABLE`;
- `BSS_LITERAL_P2_SELECTED_ALL_FINITE_LEVEL_CORE_GRAPHS_CONNECTED`;
- `BSS_LITERAL_P2_SELECTED_FINITE_LEVEL_HYPOTHESIS_4_2_AVAILABLE`;
- `BSS_LITERAL_P2_SELECTED_COROLLARY_5_5_REPLAYED`;
- `BSS_LITERAL_P2_SELECTED_LEMMA_5_19_REPLAYED`;
- `BSS_LITERAL_P2_SELECTED_THEOREM_5_20_REPLAYED`;
- `BSS_LITERAL_P2_SELECTED_LEMMA_5_22_COROLLARY_5_23_REPLAYED`;
- `BSS_LITERAL_P2_SELECTED_THEOREM_5_2_REPLAYED`.

## Exact repair architecture

1. WP60M proves the full global finite-level restriction kernel has one nonzero class and that this class violates a fixed canonical local condition retained by every selected BSS modification.
2. Hence restriction is injective on any finite `F_2`-span of the actual modified-Selmer `2`-torsion classes used by the proof. Residual irreducibility and the rank-one `(tau-1)` quotient then make the BSS quotient-character map injective on the same span.
3. WP60G pairwise self-dual localization and WP60H odd-relation localization therefore lift from the residual field to every exact level-`m` BSS auxiliary field.
4. Iterating pairwise localization constructs the injective primal localization family required in Theorem 5.20 while every chosen prime detects one fixed nonzero dual class.
5. Dual killing uses the current core-rank-one primal witness together with a current nonzero dual class, so the Proposition 5.7 transition lowers the dual dimension at each step. For the constrained Lemma 5.22 step, if the fixed witness is not the current primal witness, WP60H's three-class odd-relation criterion supplies a prime detecting the fixed witness, the current primal witness, and the current dual class simultaneously; the dual dimension still drops while the fixed witness remains visible.
6. The WP60N characteristic-two core-connectivity argument replays with exact level-`m` primes.
7. Protected MATHFORGE WP60R supplies the algebraic core-vertex freeness implication needed for finite-level Hypothesis 4.2.
8. The remaining global-duality, exterior-bidual, Stark-system, and Fitting-ideal arguments are characteristic-independent and replay unchanged.

## Preserved failures

The following remain false/unrepaired:

- formal finite higher-level BSS Hypothesis 3.2(iii);
- the protected infinite BSS H3 condition.

They are not silently promoted by WP60R.

## Next exact BSS boundary

BSS Theorem 5.25 is an inverse-limit statement in the Gorenstein-order subsection. Its source proof says the conclusions are direct consequences of finite Theorem 5.2, but the subsection separately assumes inverse-limit compatibility, Hypothesis 4.7, and finite-level Hypothesis 4.2 for all levels.

WP60R therefore stops before promoting it and records:

`MISSING_LITERAL_P2_BSS_THEOREM_5_25_INVERSE_LIMIT_REPLAY_AFTER_FINITE_LEVEL_REPLACEMENTS`.

A successor may replay that inverse-limit passage from the protected WP60R finite interfaces. It must separately verify every compatibility hypothesis used in §5.5 and must preserve the independent infinite H3 failure unless its exact use is shown irrelevant.

## Wider campaign state

Still live:

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_K_HEIGHT_NONDEGENERACY`;
- `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`;
- `BSD-R2-A1_SELECTED_RESEARCH_TARGET_UNPROVED`.

MATHCERT remains the sole certification authority.

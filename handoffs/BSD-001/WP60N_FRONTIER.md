# BSD-001 WP60N frontier — coisotropic characteristic-two connectivity

## Protected base

- MATHSOLVE base: `5c65994e1b5554b47963190d959d8f9ed6433765`;
- MATHFORGE provider: `39cda156c4ce16ec97cc80f415efa3b8a8716cea`;
- operation: `grandchallenge/MATHSOLVE#237`.

## Result

WP60N proves, under a cartesian residual self-dual core-rank-one Selmer structure with residual coisotropy,

`P2_BSS_COISOTROPIC_CORE_GRAPH_CONNECTED`.

The protected WP60H four-class obstruction is resolved without importing Sakamoto's `F_3` localization lemmas.

The proof first excludes the two odd relations containing one primal and both dual generators by the coisotropic strict-place signature. If one of the two surviving relations `p_1+p_2+d_i=0` occurs, one WP60G pairwise exchange move aligns a new minimal-core primal line with the other primal line. The aligned four-class configuration has no odd relation, so WP60H supplies the required common prime. This repairs the minimal-core gcd induction. The protected provider audit then shows the arbitrary-core reduction needs only pairwise localization, so the entire residual core graph is connected under coisotropy.

## Selected-lane applicability boundary

WP60N does not prove coisotropy for the selected literal-`2` canonical elliptic Selmer structure.

The exact next BSS applicability frontier is

`MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`.

The highest-value next action is therefore to determine the selected residual canonical local conditions place by place under the fixed Weil self-duality and decide whether `F* subset F` holds. The bad semistable primes with even Tamagawa factor and the good-ordinary place `2` must be treated explicitly. If uniform coisotropy fails, classify the exact local failure and test whether the WP60N exchange argument only needs a weaker global/strict-place condition.

## Unchanged route boundaries

- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`;
- protected infinite BSS H3 remains false;
- formal finite BSS Hypothesis 3.2(iii) remains false as a global cohomology statement;
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`;
- MATHCERT authority unchanged.

Do not reopen level-by-level finite H3/Hypothesis-3.2(iii) work. The active BSS question after WP60N is local residual coisotropy or a weaker noncoisotropic exchange hypothesis.

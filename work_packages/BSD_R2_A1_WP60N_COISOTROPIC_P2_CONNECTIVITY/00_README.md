# BSD-R2-A1 WP60N — coisotropic characteristic-two core connectivity

## Purpose

Resolve the protected WP60H minimal-core three-term-relation obstruction under an explicit residual coisotropy hypothesis.

The package works in the residual self-dual `F_2` BSS core-rank-one setting. It assumes the Selmer structure is cartesian and residually coisotropic. Under those hypotheses it proves a characteristic-two exchange theorem that replaces the four-class `2s<p` step in the minimal-core connectivity argument.

The proof uses only protected interfaces:

- MATHSOLVE WP60G: one-primal/one-dual simultaneous localization at literal `p=2`;
- MATHSOLVE WP60H: exact odd-relation criterion for four `F_2` bad fibers;
- MATHSOLVE WP60J/WP60M: selected residual/all-level Selmer-restricted BSS restriction injectivity;
- MATHFORGE WP60H: exact BSS minimal-core transition interface;
- MATHFORGE WP60N at `39cda156c4ce16ec97cc80f415efa3b8a8716cea`: residual coisotropy, the primal-dual plane decomposition, and the pairwise-only arbitrary-core reduction.

## Main result

Under cartesian residual coisotropy and core rank one,

`P2_BSS_COISOTROPIC_CORE_GRAPH_CONNECTED`.

The minimal-core step is repaired as follows. Coisotropy excludes the two odd relations containing one primal and both dual generators. If one of the two remaining relations

`p_1+p_2+d_i=0`

occurs, one WP60G pairwise localization move replaces the corresponding removed prime and aligns the new minimal-core primal line with the other primal line. For the aligned pair the only possible odd relation is of the already-excluded one-primal/two-dual type, so WP60H supplies the common prime. The usual gcd induction then connects all minimal cores. The protected provider audit shows that the subsequent arbitrary-core reduction needs only pairwise localization, so the full residual core graph is connected.

## Remaining selected-lane boundary

The theorem is conditional on residual coisotropy. Protected source evidence does not verify that the selected literal-`p=2` canonical elliptic Selmer structure is residually coisotropic.

Record

`MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`.

## Claim firewall

WP60N does not prove selected residual coisotropy; does not make formal BSS Hypothesis 3.2(iii) true; does not repair the protected infinite H3 failure; and does not by itself promote BSS integral Fitting control, R5, `BSD-R2-A1`, or MATHCERT certification.

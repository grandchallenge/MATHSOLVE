# WP60N source and dependency note

## Protected anchors

- constitutional authority: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`;
- mathematical base: `grandchallenge/MATHSOLVE@5c65994e1b5554b47963190d959d8f9ed6433765`;
- provider authority: `grandchallenge/MATHFORGE@39cda156c4ce16ec97cc80f415efa3b8a8716cea`;
- provider record: `sources/BSD-001/BSS_COISOTROPIC_P2_CONNECTIVITY_WP60N_SOURCE_AUDIT.md`.

## Imported protected mathematics

WP60N imports only the following theorem interfaces.

1. MATHSOLVE WP60G: literal-`2` self-dual one-primal/one-dual simultaneous localization and the associated pairwise core transition/path mechanism.
2. MATHSOLVE WP60H: for four nonzero self-dually identified `F_2` classes, the four bad affine fibers cover exactly when some three classes sum to zero.
3. MATHSOLVE WP60J: selected residual BSS Hypotheses 3.2/3.3 and residual self-dual applicability.
4. MATHSOLVE WP60M: all finite-level BSS cohomological defects are excluded from the actual canonical modified Selmer spaces; this preserves the Selmer-restricted coefficient-reduction interface.
5. MATHFORGE WP60H: exact BSS minimal-core transition data and gcd induction interface.
6. MATHFORGE WP60N: residual coisotropy is a local dual-in-primal inclusion; after deleting one prime from a minimal core in core rank one, the primal space is the direct sum of the core primal line and the one-dimensional dual line; Sakamoto's published `p=3` localization lemmas are not imported at `p=2`; the arbitrary-core reduction after the minimal stage requires only pairwise localization.

## New mathematics in WP60N

The characteristic-two exchange proof is downstream work, not a sourced theorem.

Its new step is:

- use the coisotropic strict-place signature to exclude the two one-primal/two-dual odd relations;
- if a remaining hard relation `p_1+p_2+d_i=0` occurs, use pairwise localization of the corresponding primal and dual generators to replace one removed prime;
- the relation forces the other primal class to have zero localization at the exchange prime, so it becomes the primal generator of the new minimal core;
- the aligned four-class problem has no odd relation and therefore admits the WP60H common-prime step.

The deterministic script `02_EXCHANGE_RELATION_CERTIFICATE.py` checks only this finite relation trichotomy. It is not evidence for the Selmer/core transition premises.

## Applicability boundary

The protected provider audit does not establish residual coisotropy for the selected literal-`2` canonical elliptic structure. Sakamoto's elliptic `p=3` application uses extra local/Tamagawa hypotheses that do not transfer automatically to the selected class.

Therefore the exact next selected-lane question after the conditional connectivity theorem is

`MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`.

No odd-prime result is treated as literal-`2` theorem authority.

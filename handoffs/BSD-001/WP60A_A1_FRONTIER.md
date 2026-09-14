# BSD-001 frontier — WP60A-A1 determinant membership

## Protected entering anchors

- MATHSOLVE WP60A-A0: `20a980fd8fb3e3a4cceabf0e37af838a16c1608e`.
- MATHFORGE WP60A source audit: `e44baeeed5d508fd4e5332c883c837951e51c000`.
- WP60 tracker: `grandchallenge/MATHSOLVE#215`.
- Parent programme owner: `grandchallenge/MATHSOLVE#164`.

This frontier becomes authoritative only after the containing A1 candidate is protected and read back from `main`.

## A1 theorem

For a two-term perfect complex over a DVR with free rank-one `H^1` and finite `H^2`, the canonical inverse determinant lattice has image

`Fitt^0(H^2) H^1`

inside the rational `H^1` line.

Thus for `z=aP` on a primitive basis:

- determinant membership iff `v(a)>=length(H^2)`;
- determinant-generator/primitivity iff `v(a)=length(H^2)`.

## Arithmetic interpretation at height one `(2)`

At `q=(2)` in `Lambda=Z_2[[T]]`, the localized ring is a DVR. The protected Kato interface supplies enough rank/torsion information to make the determinant criterion meaningful after localization, but it does not supply the all-height-one Fitting inequality at `q`; the source clause that includes that prime assumes `p != 2`.

Therefore a literal-`p=2` BKS-style determinant lift of the fixed Kato class is not a free formal construction. It is exactly the missing one-sided Fitting divisibility at `(2)`.

Refined boundary:

`MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.

Primitivity remains:

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

No WP59 reopening condition is satisfied by this reduction.

## WP60A disposition

The determinant architecture has now been reduced to its exact arithmetic content. Without materially new literal-`2` arithmetic input, further changes of determinant formalism would only relabel the same missing inequality.

Accordingly WP60A remains open at the two named arithmetic boundaries, but it is no longer the highest-value executable lane under the WP60 contract.

## Immediate executable successor — WP60B

Normalize the exact Kriz–Li literal-`2` logarithmic hypothesis under the protected identity

`P_K(f)=m_K(f)P+T`.

Required sequence:

1. admit/reconfirm the exact primary-source formula through MATHFORGE if the current protected provider interface is insufficient;
2. transport every differential, local-reduction, and logarithmic factor into the WP56A/WP58A normalization;
3. prove how prime-to-`2` torsion contributes to the normalized `2`-adic logarithm;
4. factor the condition into fixed curve-local factors, the parity of `m_K(f)`, and genuinely auxiliary-field-varying data;
5. classify the route exactly as `INDEPENDENT_AUXILIARY_NONVANISHING`, `EQUIVALENT_TO_UNKNOWN_INDEX_PARITY`, or `MIXED`.

If the condition is equivalent to unknown index parity, record the equivalence and terminate the route as non-independent. If independent information remains, seek a WP09-compatible field-forcing theorem.

## Live boundary map

- D1c parent: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- A1 one-sided divisibility: `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- A1 primitivity: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

No MATHCERT claim is promoted.

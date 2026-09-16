# BSD R5-PRIM — Kato–Kolyvagin primitivity-index reduction

## Operation

- Campaign: `BSD-001`.
- Governing issue: `grandchallenge/MATHSOLVE#267`.
- Operation: `BSD-R5-PRIM`.
- Entering frontier: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- Candidate disposition: `BLOCKED`.
- Exact successor boundary: `MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

This package does not attempt to infer determinant primitivity from rank-one freeness or from
R5-LIFT. It consumes the protected literal-`2` Kolyvagin-system stack and the newly protected
Castella–Sano source architecture to identify the exact independent arithmetic equality still
missing after all already-protected structural and rigidity inputs are replayed.

## Protected inputs

- MATHSOLVE operation base: `fdc95278fe7f4f8b60a8bc750ffe7e978f52c6a7`.
- R5-LIFT completion receipt: `.gcl/completions/BSD-R5-LIFT-EQUIV/COMPLETION_RECEIPT.json`.
- R5-LIFT substantive merge/readback: `6d0f94ad3227490826611473a40b92cadfbad577`.
- MATHFORGE provider: `5aef30aa64730ca777329013e1e33c03f34a6e3a`.
- Provider audit: `sources/BSD-001/CASTELLA_SANO_R5_PRIM_DETERMINANT_DESCENT_SOURCE_AUDIT.md`.
- INTELLECT authority: `f042220f3bed7cb7b5069256e8f6305c850c0628`.
- GCL-CEX-01 enforcement anchor: `grandchallenge/gcl-standards@efe06a27aa594c63bd0489929ffd9fff1e2daeb9`.

## Result

The operation replays the source's two structural dependencies that are already available on the
selected literal-`2` lane:

1. rank-one Kolyvagin-system structure/Fitting control from protected WP60R/WP60S; and
2. auxiliary-prime rigidity from the protected localization/core-graph stack.

After those replays, R5-PRIM is equivalent to one exact normalized arithmetic statement:
the selected Kato-derived Kolyvagin system must have precisely the protected local/Selmer
divisibility index, with no additional common factor of `2`.

No protected input determines that equality. The p>3 Castella–Sano explicit-reciprocity route
cannot be silently specialized to `p=2`. Hence the correct disposition is `BLOCKED`, not
`CLOSED` and not `FALSIFIED`.

No `R5_PRIM_ESTABLISHED`, D2d, `BSD-R2-A1`, novelty, priority, public certification, or
MATHCERT certification is asserted.

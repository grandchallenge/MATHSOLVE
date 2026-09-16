# BSD R5-PRIM — cyclotomic Kato–Kolyvagin primitivity-index reduction

## Operation

- Campaign: `BSD-001`.
- Governing issue: `grandchallenge/MATHSOLVE#267`.
- Operation: `BSD-R5-PRIM`.
- Entering frontier: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- Candidate disposition: `BLOCKED`.
- Exact successor boundary: `MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY`.

This package does not infer determinant primitivity from rank-one freeness or from R5-LIFT.
It uses the protected literal-`2` finite equivariant determinant/Stark/Kolyvagin tower together
with the newly protected Castella–Sano source architecture to identify the exact independent
arithmetic equality still missing after the structural and rigidity obligations are replayed.

## Protected inputs

- MATHSOLVE operation base: `fdc95278fe7f4f8b60a8bc750ffe7e978f52c6a7`.
- R5-LIFT completion receipt: `.gcl/completions/BSD-R5-LIFT-EQUIV/COMPLETION_RECEIPT.json`.
- R5-LIFT substantive merge/readback: `6d0f94ad3227490826611473a40b92cadfbad577`.
- MATHFORGE provider: `5aef30aa64730ca777329013e1e33c03f34a6e3a`.
- Provider audit: `sources/BSD-001/CASTELLA_SANO_R5_PRIM_DETERMINANT_DESCENT_SOURCE_AUDIT.md`.
- INTELLECT authority: `f042220f3bed7cb7b5069256e8f6305c850c0628`.
- GCL-CEX-01 enforcement anchor: `grandchallenge/gcl-standards@efe06a27aa594c63bd0489929ffd9fff1e2daeb9`.

## Result

The operation replays two source dependencies from protected literal-`2` interfaces:

1. the structure separation is obtained from WP60A-A1 plus the compatible R5-LIFT
   determinant-to-Stark-to-Kolyvagin isomorphisms over the finite cyclotomic quotients;
2. auxiliary-prime rigidity is replayed from the protected localization/core-graph stack.

Writing `Lambda=Z_2[[Gamma]]` and `q=(2)`, the compatible finite isomorphisms give a localized
rank-one identification between the cyclotomic determinant and Kolyvagin lines. If
`delta_Kato=b_Kato d_*` relative to a determinant basis, then

`M_q(kappa^Kato):=v_q(b_Kato)=v_q(a)-length_{Lambda_q}(H^2(C_q))`.

Therefore

`R5-PRIM <=> M_q(kappa^Kato)=0`.

No protected input evaluates this final height-one scalar. The proper disposition is `BLOCKED`,
not `CLOSED` and not `FALSIFIED`.

The package does not identify the cyclotomic `Lambda_q` line with the different base-level
`Z_2` Kolyvagin-system module, and it does not specialize any `p>3` Castella–Sano theorem to
literal `p=2`.

No `R5_PRIM_ESTABLISHED`, D2d, `BSD-R2-A1`, novelty, priority, public certification, or
MATHCERT certification is asserted.

# BSD-R2-A1 WP60J — selected literal-p=2 BSS residual Hypothesis 3.2

## Status

This work package continues `BSD-001` / #215 after protected WP60I.

Protected entering head: `d37c2cf409e13432a4aa7cf3fe58ff9e751e46f1`.
Operation: #227.

## Result

For every selected curve `E/Q` (semistable, odd conductor, good ordinary at `2`, irreducible `E[2]`, analytic rank one):

1. the full 2-adic image is `GL_2(Z_2)`;
2. for the residual BSS coefficient module `A=E[2]` over `R=k=F_2`, BSS Hypotheses 3.2 and 3.3 hold;
3. therefore the protected WP60G/WP60H residual affine-fiber and odd-relation reductions apply to the selected lane without a remaining residual-Hypothesis-3.2 conditionality.

Record:

`SELECTED_2ADIC_IMAGE_GL2_Z2`

`BSS_LITERAL_P2_SELECTED_RESIDUAL_HYP32_HYP33_HOLD`

`WP60G_WP60H_RESIDUAL_HYP32_CONDITIONALITY_DISCHARGED`

## Important distinction

WP60J does **not** reverse WP60I. WP60I proves that the BSS III infinite condition `(H3)` for `T_2(E)` fails at literal `p=2`. WP60J proves only the finite residual BSS II Hypothesis 3.2(iii) for `A=E[2]`.

Thus the standard integral BSS application remains blocked by WP60I. The residual localization/core-vertex analysis remains meaningful and is now unconditional on the selected residual lane.

## Exact replay

```bash
python work_packages/BSD_R2_A1_WP60J_BSS_RESIDUAL_HYP32/02_RESIDUAL_COHOMOLOGY_CERTIFICATE.py
```

## Surviving frontier

The residual F1 frontier remains

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

The integral standard BSS route remains

`R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.

No BSD, R5, or certification claim is promoted by this package.

# BSD-001 canonical continuation handoff

## Cold start

Re-fetch live protected heads before mutation, then read:

1. `.gcl/campaigns/BSD-001/CAMPAIGN_STATE.json`;
2. `.gcl/operations/BSD-R5-CW-P2-WEIGHT/OPERATION.json`;
3. `handoffs/BSD-001/R5_CW_P2_WEIGHT_FRONTIER.md`;
4. `work_packages/BSD_R5_CW_P2_WEIGHT_COVER/01_UNIVERSAL_HALF_WEIGHT_COVER_THEOREM.md`;
5. `work_packages/BSD_R5_CW_P2_WEIGHT_COVER/02_CLAIM_LEDGER.yaml`;
6. protected provider `grandchallenge/MATHFORGE@716979bcae4e67a82c52f15c99b20da555fcdfca`.

Campaign: `BSD-001`. Programme owner: #164. Parent frontier tracker: #215.
Current bounded operation: #329 (`BSD-R5-CW-P2-WEIGHT`).

## Candidate result

The operation entered on

`MISSING_P2_COLMEZ_WANG_UNIVERSAL_HALF_WEIGHT_CHARACTER`.

It proves the exact finite-flat ramified cover

`Lambda_half=Z_2[[T]][Y]/(Y^2-(1+T)) ~= Z_2[[S]]`,

with `Y=1+S` and `T=2S+S^2`.  The continuous character
`kappa_half(5^a)=Y^a` squares to the base-changed universal weight character
and has the universal property for local square roots.

Candidate disposition: `CLOSED`.

The next theorem boundary is

`MISSING_P2_COLMEZ_WANG_SQUARE_ROOT_COVER_CHAPTER15_GLOBALIZATION_COMPATIBILITY`.

Finite flatness alone does not authorize the Colmez-Wang deformation, density,
Poitou-Tate, specialization, family-Kato or denominator-removal steps.

Historical R5-RES #273 remains closed. No residual nonvanishing witness has
been produced. R5-RES, R5-PRIM, D2d, BSD-R2-A1 and MATHCERT certification
remain unestablished.

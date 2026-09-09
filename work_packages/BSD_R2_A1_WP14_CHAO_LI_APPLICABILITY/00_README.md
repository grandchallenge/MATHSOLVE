# BSD-R2-A1-WP14 — Chao Li mod-2 applicability closure

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP14-CHAO-LI-APPLICABILITY`.
- Native owner: `grandchallenge/MATHSOLVE#160`.
- Protected Solve baseline: `b96c5bfa269f1f53a01e8039aae3f8c560ee7d09`.
- Parent frontier: `BSD-R2-A1-S3-TAMAGAWA-SATURATED-LENGTH`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Result

WP14 closes the exact applicability matrix for the admitted Chao Li mod-2 rank-lowering obstruction after WP09, WP12, and WP13.

For the selected odd-conductor class:

1. residual surjectivity is automatic by WP12;
2. Chao Li's reduction-at-2 alternative is automatic because the selected class has good ordinary reduction at `2`;
3. Chao Li's residual-conductor condition is, by WP13, exactly the restriction that every bad-prime Tamagawa number is odd;
4. the separate local condition `rho_bar|G_Q2 != 1` is not automatic and cannot be deleted;
5. WP09 supplies an auxiliary imaginary quadratic Heegner field `K` with all primes dividing `2N` split and `L(E^D,1) != 0`;
6. once `K` is fixed, an auxiliary level-raising prime `q` that is inert in `K` and has order-two residual Frobenius is constructible by Chebotarev;
7. in the WP09 lane,

   `s_2(E/K) = 1 + dim_F2 Sha(E/K)[2]`,

   so Chao Li's hypothesis `s_2(E/K)=1` is exactly the additional arithmetic restriction `Sha(E/K)[2]=0`.

Therefore Chao Li's theorem does not supply a uniform proof route for `BSD-R2-A1`. On the sublocus where its remaining hypotheses hold, it sharpens the negative diagnosis: the standard odd-prime level-raising/rank-lowering mechanism does not lower the rank-one mod-2 Selmer situation to rank zero.

## Source authority

The exact source identity is the admitted Forge record

`sources/BSD-001/HEEGNER_PRIMITIVITY_P2_BARRIER_SOURCE_AUDIT.md`

at protected MATHFORGE `c44fef1d5d235b2e496bcee9ba0f7fc54212fa0d`, which binds Chao Li, *Level Raising mod 2 and Obstruction to Rank Lowering*.

The source locators used here are Assumption 4.1, Remark 4.2, Theorem 7.1, and the local-condition warning/example in Remark 6.2. WP14 does not enlarge the admitted source theorem beyond those exact roles.

## Claim boundary

WP14 does not prove a `p=2` Kolyvagin-system primitivity theorem, an exact Sha/Heegner-index equality, the direct arithmetic-length equality, `BSD-R2-A1`, novelty/priority, or MATHCERT certification.

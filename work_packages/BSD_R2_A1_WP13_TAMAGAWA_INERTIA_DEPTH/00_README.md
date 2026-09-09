# BSD-R2-A1-WP13 — Tamagawa / inertia-depth dictionary

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP13-TAMAGAWA-INERTIA-DEPTH`.
- Native owner: `grandchallenge/MATHSOLVE#158`.
- Protected Solve baseline: `a9a16da8b228ee6d472f11752cf6c3bc68fda864`.
- Parent frontier: `BSD-R2-A1-S3-DIRECT-LENGTH`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Result

For every odd semistable bad prime `ell|N`, put

`n_ell := ord_ell(Delta_min)`.

WP13 proves in-package:

1. for every `m>=1`,

   `I_ell acts trivially on E[2^m] <=> 2^m | n_ell`;

2. hence the residual representation is unramified at `ell` exactly when `n_ell` is even;
3. the residual conductor is

   `N(rho_bar_{E,2}) = product_{ell|N, n_ell odd} ell
                       = product_{ell|N, c_ell odd} ell`;

4. therefore

   `N / N(rho_bar_{E,2}) = product_{ell|N, 2|c_ell} ell`;

5. the exact Tamagawa valuations are:

   - split multiplicative: `ord_2(c_ell)=v_2(n_ell)`, equal to the full local 2-power unramified depth;
   - nonsplit multiplicative: `ord_2(c_ell)=min(1,v_2(n_ell))`.

## Meaning

The even-Tamagawa obstruction is not an opaque auxiliary hypothesis. At every bad odd prime it is exactly visible in the local 2-power representation. Chao Li's residual-conductor condition `N(rho_bar)=N` is therefore equivalent, in this selected semistable odd-conductor class, to requiring every bad-prime Tamagawa number to be odd.

This does not import any odd-prime Tamagawa-defect theorem at `p=2`. Contemporary odd-prime Euler/Kolyvagin-system results remain diagnostic only unless separately admitted and shown applicable.

## Claim boundary

WP13 does not prove `BSD-R2-A1`, p=2 Kolyvagin primitivity, an exact Sha/index formula, the direct-length equality, novelty/priority, or MATHCERT certification.
# BSD-001 frontier after WP41

## Protected predecessors

- MATHSOLVE WP40: `af41471670639648db0aa96ed493333d2bf1536e`.
- MATHFORGE WP41B source admission: `ab5e1c4d429bb36cce9927e62bcee5279870dec7`.

## WP41A — Bockstein/dual-hit compatibility

WP37's first cyclotomic Bockstein and WP40's finite dual global hit `D_K` arise from different operations:

- cyclotomic deformation of one fixed strict Selmer complex;
- fixed-level change of local condition from strict Greenberg to classical Kummer.

The protected chain contains no `K`-side Iwasawa-level strict-to-Kummer comparison triangle whose augmentation is the WP39/WP40 finite quotient and whose connecting morphisms are natural for the WP37 Bockstein.

Therefore no protected equality between `D_K` and a Bockstein image, kernel, cokernel, height radical, or equal-length defect is currently justified.

Refined bridge:

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`.

This is a dependency statement, not a theorem-nonexistence claim.

## WP41B — exact ordinary Disegni normalization

For the protected trivial-weight `p=2` auxiliary lane and Disegni's source-compatible special ordinary test vectors,

`e_{2,infinity}^{-1} Q_special = Q^ord`

exactly.

Thus the corrected ordinary Gross–Zagier identity may be written

`height^ord/pairing^ord = L'_2 * Q^ord`

without a separate interpolation-factor valuation. This is normalization transfer, not a claim that the transferred factor has valuation zero.

Disegni Lemma 4.3.3 / equation (4.3.4) gives the exact place-by-place decomposition of `Q^ord`. No local factor has yet been declared a `2`-adic unit.

Refined D2c boundary:

`MISSING_P2_DISEGNI_QORD_LOCAL_FACTOR_VALUATIONS`.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

WP40 still gives

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

The finite dual hit `D_K` remains unevaluated. A Bockstein identification requires the new compatibility bridge above.

### D2c

`MISSING_P2_DISEGNI_QORD_LOCAL_FACTOR_VALUATIONS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP42A — strict/Kummer Iwasawa compatibility screen

Search narrowly for, or construct from Nekovar's mapping-fibre formalism, a cyclotomic `K`-side comparison triangle

`C_str,infty -> C_Kum,infty -> Q_infty -> C_str,infty[1]`

such that derived augmentation recovers WP39's finite local-condition quotient and the augmentation Bockstein is natural with respect to the triangle.

Do not accept a theorem only after tensoring with `Q_2`, only up to finite error, or only for odd `p`.

### WP42B — evaluate `Q^ord`

Bind the exact ordinary test-vector packet and evaluate the factors of Disegni (4.3.4) place by place. Start with:

1. the ordinary `p=infinity` term at the split prime `2`, using Appendix A.3 and the protected good-ordinary/unit-root data;
2. split bad primes `ell|N`, retaining local toric periods, Tamagawa-sensitive factors, Haar measures, and vector normalizations;
3. the remaining auxiliary/unramified places and global measure convention.

The target is an exact additive ledger for `ord_2(Q^ord)`, not a blanket unit assertion.

## Claim firewall

Do not promote:

- formal similarity between `D_K` and a Bockstein defect to an equality;
- source-normalization cancellation to `ord_2(Q^ord)=0`;
- any local `Q^ord` factor to a unit without exact calculation;
- existence of the first p-adic height to nondegeneracy;
- an odd-prime or rationalized comparison to literal integral `p=2`;
- BSD, MATHCERT certification, novelty, or priority.

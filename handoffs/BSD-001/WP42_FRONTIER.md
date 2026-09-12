# BSD-001 frontier after WP42B

## Protected predecessors

- MATHSOLVE WP41: `3463858d6281bcc2030d11f7f9af76c9f9097ff9`.
- MATHFORGE WP42B source admission: `a014559b89897bcfa2078147224e598ab6aaedca`.

## WP42B closure

Protected WP41 rewrites the selected corrected Disegni Gross–Zagier normalization as

`height^ord/pairing^ord = L'_2 * Q^ord`.

For the selected split prime `2`, trivial Hecke character, unramified good-ordinary refinement, and Disegni's canonical Appendix-A.3 vectors and local measure, WP42B proves

`Q^ord_{2,dt_2^can}=1`

and therefore

`ord_2(Q^ord_{2,dt_2^can})=0`.

The equality is local-normalization specific. If the global adelic measure decomposition uses

`dt_2'=c_2 dt_2^can`,

then the local factor is `c_2`, and the compensating global measure scalar must remain explicit.

Thus the canonical split-`2` toric factor is closed; the global ordinary factor is not.

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

WP41A leaves the exact bridge

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`.

A narrow source screen indicates Nekovář's Greenberg local conditions are functorial for the cyclotomic augmentation/Bockstein construction. What remains unprotected is the integral cyclotomic classical-Kummer comparison object and strict-to-Kummer morphism whose derived augmentation recovers WP39/WP40.

### D2c

The canonical split-`2` ordinary toric factor is now closed. The remaining global `Q^ord` valuation debt is:

1. global/local Haar-measure reconciliation;
2. the split semistable bad-prime factors at every `ell|N`;
3. any auxiliary finite places in Disegni's `Sigma` and `Sigma'`;
4. the remaining local L-factor and vector-normalization terms;
5. any residual global/archimedean normalization in the ordinary product.

The next exact local boundary is

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

Disegni §4.2 rewrites split toric periods as Rankin–Selberg zeta integrals, and [Dis20b, Proposition 5.2.4] supplies interpolation in families. Neither statement alone evaluates the semistable Steinberg/newvector integral. Do not promote interpolation to a unit or valuation formula.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP43A — K-side Iwasawa Kummer comparison

Source-qualify or construct the missing integral cyclotomic classical-Kummer Selmer object over `K` and a comparison morphism

`C_str,infty -> C_Kum,infty`

compatible with Nekovář's cyclotomic augmentation triangle. Require derived specialization at augmentation to recover the finite strict/Kummer quotient of WP39/WP40 exactly.

Theorem statements only after inverting `2`, only up to finite error, or only for odd `p` are insufficient.

### WP43B — split semistable bad-prime toric factors

For each odd semistable `ell|N`, with `K/Q` split at `ell` and `chi_ell=1`, bind the exact local representation/test-vector chosen by the global Disegni packet and evaluate the normalized split Rankin–Selberg toric integral. Retain:

- split versus nonsplit multiplicative type;
- the Steinberg/unramified-twist parameter;
- Haar measure;
- local `L(V,ell,0)^{-1}` normalization;
- the denominator pairing/newvector normalization;
- any Tamagawa-sensitive scalar.

The target is an exact formula for the local contribution to `ord_2(Q^ord)`, not an interpolation theorem or a blanket unit claim.

## Claim firewall

Do not promote:

- canonical `Q^ord_2=1` to global `Q^ord=1`;
- a change of local Haar measure to no change in the global normalization;
- interpolation of a local zeta integral to its explicit semistable value;
- formal Bockstein functoriality for strict Greenberg conditions to existence of the missing Kummer Iwasawa comparison object;
- p-adic-height existence to nondegeneracy;
- any odd-prime/rationalized result to literal integral `p=2`;
- BSD, MATHCERT certification, novelty, or priority.

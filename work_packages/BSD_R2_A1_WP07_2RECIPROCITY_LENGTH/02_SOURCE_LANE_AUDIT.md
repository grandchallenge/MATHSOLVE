# Current theorem-lane audit

## Source status

All items in this file are `EXTERNAL_RECONNAISSANCE_UNADMITTED` under the live MATHFORGE BSD provider state. They may delimit a route. They may not silently supply a theorem premise for `BSD-R2-A1`.

Screen date: 2026-09-08.

## Lane A — current non-CM ordinary main-conjecture results

### Yan–Zhu

Xiaojun Yan and Xiuwu Zhu, *Main conjectures for non-CM elliptic curves at good ordinary primes*, arXiv:2412.20078; Journal of Algebra 693 (2026), 372–402.

The primary abstract states `p>2`; the published introduction fixes an odd prime `p`. The paper therefore cannot be instantiated at the selected prime `2` without an independent theorem extending its argument.

**Disposition:** `INAPPLICABLE_AT_SELECTED_PRIME`.

### Burungale–Skinner–Tian–Wan

Ashay Burungale, Christopher Skinner, Ye Tian, and Xin Wan, *Zeta elements for elliptic curves and applications*, arXiv:2409.01350.

The primary abstract assumes `p not| 2N`. Hence its prime is automatically odd and cannot equal `2` in the selected campaign.

**Disposition:** `INAPPLICABLE_AT_SELECTED_PRIME`.

## Lane B — genuine p=2 twist results

### Kriz–Li

Daniel Kriz and Chao Li, *Congruences between Heegner points and quadratic twists of elliptic curves*, arXiv:1606.03172.

The primary abstract explicitly treats `p=2` and proves the 2-part of BSD for many rank-zero and rank-one quadratic twists in the families it constructs. This is important evidence that 2-primary leading-term results are possible. It is not a theorem for every elliptic curve in the selected `BSD-R2-A1` class.

**Disposition:** `RELEVANT_BOUNDED_FAMILY_NOT_UNIFORM_TARGET`.

### Hatley–Ray

Jeffrey Hatley and Anwesh Ray, *Iwasawa theory and ranks of elliptic curves in quadratic twist families*, arXiv:2412.07308.

The primary abstract genuinely assumes good ordinary reduction at `2`, but studies rank distribution and `lambda_2` behavior in twist families under additional hypotheses. It does not state the selected exact rank-one leading-term valuation identity.

**Disposition:** `RELEVANT_P2_IWASAWA_ADJACENCY_NOT_LEADING_TERM`.

## Lane C — standard residual-distinguished machinery

WP07 proves internally that the standard residual ordinary `p`-distinguished condition is impossible for an elliptic curve at `p=2`, because both residual rank-one characters have values in `F_2^x={1}`.

Consequently, any theorem whose hypotheses include residual `p`-distinguishedness must be rejected at the hypothesis check before its conclusion is used. No general statement about all Hida/Iwasawa methods is intended; a source-specific theorem that replaces this hypothesis may still be admissible.

## Normalization concordance

SageMath's documented ordinary p-adic L-series normalization uses

`L_p(E,1) = (1-alpha^(-1))^2 L(E,1)/Omega_E`

and documents support for `p=2` with a modified description of the Iwasawa algebra. This is useful normalization concordance, not an admitted theorem premise. WP07's exact valuation of `(1-alpha^(-1))^2` is proved independently of SageMath.

## Result of the audit

No screened current theorem closes the selected uniform `p=2` rank-one leading-term identity. The failure is not merely bibliographic:

- leading current non-CM ordinary main-conjecture routes screened here exclude `2` explicitly;
- the selected local representation is necessarily non-distinguished in the standard residual sense;
- the ordinary interpolation multiplier is necessarily non-unit with exact valuation `2` or `4` under the stated normalization;
- genuine `p=2` results found in the screen are bounded twist/rank results rather than a uniform theorem for `BSD-R2-A1`.

A future source can change this conclusion only if its exact hypotheses and normalization survive these checks.
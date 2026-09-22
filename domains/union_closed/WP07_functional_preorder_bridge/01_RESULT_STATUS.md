# WP07 Result Status

Date: 2026-09-21

| Field | Status |
|---|---|
| Work package | WP07 functional-preorder bridge |
| Result status | D001-D005 checked locally; WP07 restricted theorem-development lane complete |
| Source branch | `UC-WP03-C007`, functional-preorder order ideals |
| Selected source revision | `kashiwabarakenji/avg-rare@21451877e9996a295bbc1ec25856d07fa302d48c` |
| D003 theorem surface | `MathSolve/UnionClosed/FunctionalPreorderBridge.lean` |
| D004 theorem surface | `MathSolve/UnionClosed/FunctionalPreorderD004.lean` plus `MathSolve/UnionClosed/AvgRarePort/` |
| D005 theorem surface | `MathSolve/UnionClosed/FunctionalPreorderD005.lean` |
| Strongest supported local claim | If `F` is an exact D003 functional-preorder ideal family on `U`, then `complementFamilyOn F U` is union-closed, nontrivial, and Frankl-abundant; its average abundance is also checked |
| Not claimed | No representation theorem for arbitrary finite union-closed families; no unrestricted Frankl theorem; no MATHCERT certification |
| Foundation route | `R0`, finite and computable |
| Next programme step | Bounded MATHCERT handoff for the exact restricted theorem, plus structural comparison against WP05/UC-P04 without universal promotion |

## D005 checked movement

D005 does not route through WP06's subset-downward `IsIdealFamilyOn`. Instead,
`FunctionalPreorderD005.lean` proves the structural fact actually available for
preorder ideals:

```lean
functionalPreorderIdealFamily_inter_closed
```

so complements inside the fixed carrier are union-closed.

The module then establishes the finite complement arithmetic needed for the
Frankl-facing statement:

```lean
complementFamilyOn_card
freq_complementFamilyOn
sum_card_eq_sum_freq_on
exists_rare_of_averageRare
complementFamilyOn_averageAbundant_of_averageRare
complementFamilyOn_abundant_of_exists_rare
```

The rare element is obtained directly from D004 average rarity by double
counting. No additional external theorem is used.

The two D005 endgames are:

```lean
d005_complement_averageAbundant
d005_complement_frankl
```

and the explicit restricted representation wrapper is:

```lean
IsComplementOfFunctionalPreorderIdealFamily
complementOfFunctionalPreorderIdealFamily_frankl
```

This wrapper is intentionally one-way: it applies only after such a
representation has already been supplied.

## Claim firewall

```text
UC-FRANKL = OPEN_PROBLEM
UC-P04 = OPEN
WP07-D004 = CLOSED_LOCAL
WP07-D005 = CLOSED_LOCAL
WP07_RESTRICTED_LANE = COMPLETE_LOCAL
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

The missing universal object is now especially clear: nothing in WP07 proves
that an arbitrary finite union-closed family is the complement of a
functional-preorder order-ideal family.

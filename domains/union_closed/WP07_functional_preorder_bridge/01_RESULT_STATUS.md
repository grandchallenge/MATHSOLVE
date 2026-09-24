# WP07 Result Status

Date: 2026-09-24

| Field | Status |
|---|---|
| Work package | WP07 functional-preorder bridge |
| Result status | D001-D005 checked locally; restricted theorem independently qualified |
| Source branch | `UC-WP03-C007`, functional-preorder order ideals |
| Selected source revision | `kashiwabarakenji/avg-rare@21451877e9996a295bbc1ec25856d07fa302d48c` |
| D003 theorem surface | `MathSolve/UnionClosed/FunctionalPreorderBridge.lean` |
| D004 theorem surface | `MathSolve/UnionClosed/FunctionalPreorderD004.lean` plus `MathSolve/UnionClosed/AvgRarePort/` |
| D005 theorem surface | `MathSolve/UnionClosed/FunctionalPreorderD005.lean` |
| Strongest supported restricted claim | If `F` is an exact D003 functional-preorder ideal family on `U`, then `complementFamilyOn F U` is union-closed, nontrivial, and Frankl-abundant; its average abundance is also checked |
| MATHCERT disposition | `QUALIFIED` for exact restricted claim `UC-WP07-P006` |
| MATHCERT protected merge | `245a2f395c358a8d11941e7085512a2e53751619` |
| Not claimed | No unrestricted Frankl theorem; no closure of `UC-P04` |
| Foundation route | `R0`, finite and computable |
| Next programme step | WP08 closure-system extension and incidence-preserving WP05 interface |

## D005 checked movement

D005 does not route through WP06's subset-downward `IsIdealFamilyOn`. Instead,
`FunctionalPreorderD005.lean` proves the structural fact actually available
for preorder ideals:

```lean
functionalPreorderIdealFamily_inter_closed
```

so complements inside the fixed carrier are union-closed.

The module then establishes the complement arithmetic and incidence counting
needed for the restricted Frankl-facing theorem.

The two D005 endgames are:

```lean
d005_complement_averageAbundant
d005_complement_frankl
```

with representation wrapper:

```lean
IsComplementOfFunctionalPreorderIdealFamily
complementOfFunctionalPreorderIdealFamily_frankl
```

## Successor structural result

WP08 has now proved that the wrapper cannot be universal. Exact D003
complements are also closed under literal set intersection, whereas an explicit
three-point union-closed family is not.

Thus the missing universal object is no longer described as an unknown exact
representation theorem. That exact route is closed negatively.

The live successor object is an arbitrary finite closure system obtained by
complementing a union-closed family.

## Claim firewall

```text
UC-WP07-P006 = QUALIFIED_PROTECTED
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
WP07_RESTRICTED_LANE = COMPLETE
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

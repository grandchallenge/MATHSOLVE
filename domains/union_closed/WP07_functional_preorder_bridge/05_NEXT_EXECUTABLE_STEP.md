# WP07 Next Executable Step

Date: 2026-09-24

## Current frontier

WP07-D001 through WP07-D005 are closed locally.

The strongest exact theorem is:

```lean
d005_complement_frankl
    (h : IsFunctionalPreorderIdealFamilyOn F U) :
    IsUnionClosed (complementFamilyOn F U) ∧
      IsNontrivial (complementFamilyOn F U) ∧
      IsFranklAbundant (complementFamilyOn F U)
```

The restricted result has now been independently adjudicated by MATHCERT with
bounded disposition `QUALIFIED`.

Protected MATHCERT adjudication:
- merge: `245a2f395c358a8d11941e7085512a2e53751619`
- record: `governance/result_family_adjudications/UC-WP07-D005.json`
- record blob: `00c37d4a379811b52e7f44e6d384adc75e2fc850`

WP07 itself has no remaining restricted mathematical proof debt.

## Successor programme action

The former exact-representation question has now been decided negatively in
WP08.

The statement

```text
every finite union-closed family
  -> exact complement of a D003 functional-preorder ideal family
```

is false.

The exact obstruction is literal intersection closure: every D003 complement
family is both union-closed and intersection-closed, while the explicit
three-point union-closed family

```text
{ ∅, {a,b}, {b,c}, {a,b,c} }
```

is not intersection-closed.

The successor UC-P04 route is therefore not exact representation. It is the
closure-system route developed in:

```text
domains/union_closed/WP08_closure_system_bridge/
MathSolve/UnionClosed/FunctionalPreorderP04.lean
```

The live question is now how far the rare-element argument can be extended from
functional-preorder closure systems toward arbitrary finite closure systems
while preserving the concrete incidence/frequency data needed by Frankl.

## Hard firewall

```text
UC-WP07-P006 = QUALIFIED_PROTECTED
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

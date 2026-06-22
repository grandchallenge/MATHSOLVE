# Functional-Preorder Bridge Assessment

Date: 2026-06-22

## Summary

The functional-preorder source branch is relevant to the WP06 averaging line,
but it is not a direct application of the local ideal-family theorem. WP06
proves average rarity for `IsIdealFamilyOn F U` and then dualizes complements to
union-closed abundance. Functional-preorder order ideals are downward closed in
the preorder relation induced by a function; this is a different semantic
condition from subset-downward closure for all proper members of a finite set
family.

WP07 therefore starts as a bridge assessment. The safe next formal target is a
small obstruction/bridge-definition step, followed only later by a theorem for a
local functional-preorder predicate.

## Sources

- Ideal-family source branch: <https://arxiv.org/abs/2504.13454>.
- Functional-preorder source branch: <https://arxiv.org/abs/2511.19833>.
- Public Lean repository observed for the functional-preorder branch:
  <https://github.com/kashiwabarakenji/avg-rare>, `main` at
  `49c3f1d96ca8518d16e203fd0429ac1216838a4f` on 2026-06-22.

The external repository is provenance only at this stage. It has not yet been
cloned, built, or ported inside MATHSOLVE/MATHCERT for WP07.

## Semantic Mismatch

`IsIdealFamilyOn F U` requires:

```text
if B in F, B != U, and A subset B, then A in F.
```

A preorder order ideal requires:

```text
if x is in I, y is in U, and y <= x in the preorder, then y is in I.
```

These conditions are not equivalent. In the functional chain
`a <= b <= c`, generated for example by `f(a) = b`, `f(b) = c`, and
`f(c) = c`, the order ideals are:

```text
empty, {a}, {a,b}, {a,b,c}.
```

The proper order ideal `{a,b}` has subset `{b}`, but `{b}` is not an order
ideal because `a <= b` and `a` is missing. Thus the family of order ideals is
not subset-downward closed below all proper members and is not automatically an
`IsIdealFamilyOn` family.

This does not refute the source theorem. It only shows that WP06's exact local
ideal-family theorem cannot be used as a direct consumer for the whole
functional-preorder branch.

## Intended Bridge Shape

The bridge should keep three layers separate:

1. source side: a finite functional preorder from a function `f : V -> V`;
2. local side: a finite `Family alpha := Finset (Finset alpha)` consisting of
   preorder order ideals;
3. proof side: either a local theorem for this preorder-order-ideal predicate
   or a translation theorem into a predicate already certified in MATHCERT.

The expected local predicate should assert finite ground membership, decidable
membership, closure under preorder-lower elements, and inclusion of the empty
set and the full ground. It should not be named or treated as
`IsIdealFamilyOn`.

## Selected Next Formal Target

The first formal target after this assessment should be one of the following,
in this order:

1. build/audit the external `avg-rare` repository at the observed commit and
   record exact theorem names, Lean toolchain, dependencies, and build result;
2. add a checked finite-chain obstruction showing that preorder order ideals
   need not satisfy the WP06 `IsIdealFamilyOn` predicate;
3. define a local finite functional-preorder order-ideal predicate and state
   the bridge obligations for average rarity and complement duality.

No WP07 claim should be promoted beyond source/human assessment until the first
checked local theorem compiles with no `sorry`, `admit`, or new axioms.


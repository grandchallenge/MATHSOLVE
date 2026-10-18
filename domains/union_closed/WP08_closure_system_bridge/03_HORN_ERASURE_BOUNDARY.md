# WP08-D003: Horn Closure Systems and the Erasure Boundary

Date: 2026-09-24

## Objective

WP08-D002 proved a rare-element theorem for all finite-poset ideal systems by
erasing a maximal element. D003 asks how far that mechanism extends toward an
arbitrary finite closure system.

The useful intermediate language is finite Horn implication systems.

## Generic erasure criterion

Define a ground element `x` to be **erasable** when

```text
I closed and x ∈ I
  => I \ {x} closed.
```

For any finite family, erasability immediately gives an injection

```text
closed sets containing x
  -> closed sets omitting x
I |-> I \ {x}.
```

Hence

```text
2 * freq(x) <= # closed sets.
```

The checked theorem is:

```lean
rare_of_erasable
```

and for pointed closure systems the complementary Frankl endpoint is:

```lean
pointedClosure_complement_frankl_of_erasable
```

## Horn extension

For a finite Horn basis, a variable that never appears as a rule conclusion is
erasable. Removing it can only disable rule premises; it cannot remove a
required conclusion.

This yields:

```lean
erase_preserves_Horn_of_conclusionFree
hornModel_erasable_of_conclusionFree
hornModel_complement_frankl_of_conclusionFree
```

So the D002 maximal-element mechanism is not confined to posets. It extends to
a wider implication class whenever the dependency hypergraph has a
conclusion-free carrier variable.

## First genuinely non-unary obstruction

Consider the three binary implications

```text
{a,b} -> c
{b,c} -> a
{c,a} -> b.
```

Their closed sets are exactly

```text
∅, {a}, {b}, {c}, {a,b,c}.
```

This is a pointed finite closure system. But no element is erasable: deleting
any element from the full closed set produces a forbidden two-element set.

The checked obstruction is:

```lean
cyclicBinaryClosure_no_erasable
not_every_pointedClosureSystem_has_erasable
```

Importantly, the same fixture still has rare elements and its complementary
union-closed family satisfies Frankl abundance:

```lean
cyclicBinaryClosure_has_rare
cyclicBinaryClosure_complement_frankl
```

Therefore the literal erasure injection is a sufficient mechanism, not a
universal one.

## Programme consequence

The frontier is now narrower and clearer.

```text
functional preorder
  -> arbitrary poset
  -> conclusion-free Horn systems
  -X-> arbitrary pointed closure systems
```

The first obstruction is not closure itself. It is a cyclic multi-premise
dependency pattern in which every variable can be forced as a conclusion.

The next viable mathematical question is therefore:

> Can the single-element erasure injection be replaced by a more general
> incidence-preserving matching or charging map that handles cyclic
> multi-premise Horn closure systems?

That is the next D003/D004 interface to WP05.

## Claim firewall

```text
WP08-D001 = CLOSED_NEGATIVE
WP08-D002 = CLOSED_LOCAL
WP08-D003A = HORN_CONCLUSION_FREE_EXTENSION
WP08-D003B = SINGLE_ERASURE_ROUTE_REFUTED_FOR_GENERAL_CLOSURE_SYSTEMS

UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

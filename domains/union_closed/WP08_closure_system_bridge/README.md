# WP08: Closure-System Bridge for UC-P04

Date: 2026-09-25

## Purpose

WP07-D005 is a protected, independently qualified restricted theorem. The live
campaign obligation `UC-P04` asks how restricted finite results could connect
to the universal half-frequency target.

WP08 widens the structural class in controlled stages while preserving the
concrete incidence data used by the frequency inequality.

## D001 — exact D003 representation is not universal

The exact functional-preorder complement route is false in general.

Every exact D003 complement family is closed under both literal union and
literal intersection. The concrete three-point family

```text
G = { ∅, {a,b}, {b,c}, {a,b,c} }
```

is union-closed but not intersection-closed. The protected endpoint is:

```lean
p04_no_universal_exact_functionalPreorder_representation
```

This refutes one `UC-P04` subroute. It does not close `UC-P04`.

## D002 — finite-poset ideal extension

The functional self-map restriction is unnecessary for the existence of one
rare element.

For every nonempty finite carrier in an arbitrary partial order, a maximal
carrier element occurs in at most half of all downward order ideals. Erasing
that maximal element injects ideals containing it into ideals omitting it.

Principal endpoints:

```lean
posetIdealFamily_exists_rare
posetIdeal_complement_frankl
```

This strictly enlarges the WP07 Frankl-facing class from functional preorders
to arbitrary finite partial orders. It does not assert WP07's stronger
average-rarity inequality for arbitrary posets.

## D003 — arbitrary finite closure systems have an exact implication normal form

D003 is now closed locally on:

```text
MathSolve/UnionClosed/ClosureImplicationP04.lean
```

For an arbitrary finite closure system `F` on an explicit carrier `U`, the
module defines the canonical closure

```text
cl_F(A) = intersection of all C in F with A subset C
```

and checks the closure-operator laws:

```lean
closureOf_subset
subset_closureOf
closureOf_mono
closureOf_idempotent
closureOf_mem_of_closureSystem
mem_iff_closureOf_eq
```

Closed members are exactly the fixed points.

The same surface constructs the finite canonical implication basis containing
every valid implication `P -> q` over the carrier and proves exact recovery:

```lean
closureSystem_mem_iff_models_canonicalBasis
```

Hence every finite closure system has a finite implication presentation. This
is an exact representation theorem for closure systems, not a Frankl theorem.

### Unary implications recover the poset-like regime

For a finite basis of unary implications `x -> y`, its model family is
union-closed:

```lean
unaryModelFamilyOn_unionClosed
unaryImplicationRepresentable_unionClosed
```

This explains structurally why poset-ideal systems sit inside a narrower
unary-implication class.

### First genuinely non-unary mechanism

On the three-point carrier, D003 formalizes the single binary implication

```text
{a,b} -> c.
```

Its model family is

```text
{ ∅, {a}, {b}, {c}, {a,c}, {b,c}, {a,b,c} }.
```

The checked facts are:

```lean
binaryImplicationClosure_characterization
binaryImplicationClosure_isClosureSystem
binaryImplicationClosure_not_unionClosed
binaryImplicationClosure_not_unaryRepresentable
binaryImplicationClosure_forcedConclusion_erasure_fails
```

The key obstruction is exact: erasing the forced conclusion `c` from the
full closed set produces `{a,b}`, which violates the implication. Therefore
the maximal-element erasure mechanism used in D002 does not extend verbatim to
arbitrary implication systems.

The obstruction is to the proof mechanism, not to the half-frequency
conclusion. This minimal binary example still has a rare element and its
complement is Frankl-abundant:

```lean
binaryImplicationClosure_exists_rare
binaryImplicationClosure_complement_frankl
```

No theorem in D003 establishes a rare element for every finite closure system.

## Governed replay improvement

WP08 now has an exact-head replay workflow:

```text
.github/workflows/uc-wp08-closure-system.yml
```

and the WP08 theorem modules are imported by `MathSolve.lean`. Enabling this
gate exposed and repaired latent D001/D002 Lean defects that had not previously
been exercised by the root build. The D001-D003 surface is now subject to the
same explicit no-`sorry`/no-`admit`/no-explicit-`axiom` replay.

## Relation to WP05

The D003 implication normal form identifies the correct structural language for
the next bridge, but frequency still depends on concrete incidences.

A WP05/WP08 interface must therefore retain both:

1. the abstract lattice/closure order; and
2. the incidence map recording which ground elements occur in which closed
   sets or union-family members.

An abstract lattice isomorphism alone is not enough to transport the Frankl
frequency statistic.

## Next mathematical tranche

### WP08-D004 — incidence-preserving WP05 interface

Construct a finite lattice-plus-incidence object for a carried union-closed
family and its complement closure system. Re-express the protected WP05
minimum-counterexample conditions on that object and determine which conditions
constrain the implication structure, especially genuinely non-unary premises.

Acceptance requires incidence counts to be preserved exactly. No theorem may
replace the concrete family by an abstractly isomorphic lattice and then reuse
frequencies without an explicit incidence transport.

## Claim firewall

```text
WP08-D001 = CLOSED_NEGATIVE
WP08-D002 = CLOSED_LOCAL
WP08-D003 = CLOSED_LOCAL

UC-WP08-L001 = exact D003 complements are union- and intersection-closed
UC-WP08-L002 = explicit 3-point union-closed family is not D003-representable
UC-WP08-L003 = universal exact D003 representation route is refuted
UC-WP08-P004 = finite-poset ideal complements satisfy Frankl abundance
UC-WP08-L005 = every finite closure system has a finite canonical implication basis
UC-WP08-L006 = unary implication model families are union-closed
UC-WP08-L007 = the binary implication {a,b}->c is a non-unary closure-system obstruction
UC-WP08-P008 = that bounded binary example still has a rare element and Frankl-abundant complement

WP08-D004 = OPEN_NEXT
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

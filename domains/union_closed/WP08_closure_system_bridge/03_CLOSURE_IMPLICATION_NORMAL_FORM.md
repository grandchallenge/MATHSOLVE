# WP08-D003: Closure Operators and Finite Implication Normal Form

Date: 2026-09-25

## Exact theorem surface

```text
MathSolve/UnionClosed/ClosureImplicationP04.lean
```

## 1. Canonical closure operator

For a finite closure system `F` on carrier `U`, define `closureOf F U A`
as the elements of `U` contained in every closed member containing `A`.

The checked surface proves:

- carrier containment;
- extensivity for `A subset U`;
- monotonicity;
- idempotence;
- closure values are members of the closure system; and
- fixed points are exactly the closed members.

This converts the family presentation into an operator presentation without
losing the concrete carrier.

## 2. Canonical finite implication basis

An implication is a pair `(P,q)` with finite premise set `P` and conclusion
`q`. The canonical basis contains every implication over `U` valid in all
closed members.

The theorem

```lean
closureSystem_mem_iff_models_canonicalBasis
```

proves exact equivalence between family membership and modeling that finite
basis.

This is deliberately a canonical, possibly redundant basis. D003 requires
exact representability, not basis minimization.

## 3. Unary versus genuinely non-unary structure

The models of any finite unary basis `x -> y` are union-closed. Hence unary
implications cannot represent every closure system.

The smallest checked witness uses three carrier elements and one binary rule:

```text
{a,b} -> c.
```

Its model family omits only `{a,b}` from the full powerset. It is
intersection-closed and contains the carrier, but is not union-closed because
`{a}` and `{b}` are closed while their union is not.

Therefore the family is not representable by a unary implication basis.

## 4. Why D002 stops here

D002 pairs ideals containing a maximal element with ideals omitting it by
erasure. In the binary example, `c` is forced by the joint presence of
`a,b`. Erasing `c` from the full closed set yields the nonclosed premise
`{a,b}`.

This is a concrete obstruction to extending the D002 injection verbatim.

It is not a counterexample to the rare-element claim. The example still has a
rare element, and carrier-relative complement duality gives a union-closed,
nontrivial, Frankl-abundant family.

## 5. What D003 does not prove

D003 does not prove:

- that every finite closure system has a rare element;
- that every implication basis admits a D002-style injection;
- that non-unary implications preserve average rarity;
- that WP05 minimum-counterexample conditions force a special implication
  basis; or
- `UC-P04` or `UC-FRANKL`.

The exact next problem is to bring the WP05 structural conditions onto a
closure-system representation while preserving the concrete incidence counts.

# WP07 Next Executable Step

Date: 2026-09-20

## Current frontier

D001-D004 are closed on the local WP07 theorem surface. In particular,

```lean
sourceShapedMainNDS : SourceShapedMainNDSStatement α
d004_averageRarity : D004AverageRarityStatement α
```

are checked after explicit semantic transport of the audited source theorem.

The next mathematical obligation is therefore WP07-D005.

## Selected route: exact complement duality for the D003 class

Do not reuse WP06's `IsIdealFamilyOn` hypothesis: D002 proved that functional
preorder order-ideal families need not satisfy it. Reuse only generic finite-set
complement identities whose hypotheses are actually available.

Proceed in this order:

1. Define the complement family on the explicit D003 carrier:
   `complementFamilyOn F U := F.image (fun I => U \ I)` or reuse an existing
   generic definition only after proving exact semantic agreement.
2. Prove that intersections of two members of a functional-preorder ideal family
   remain members. This should follow directly from the order-ideal predicate.
3. Use
   `U \ (A ∩ B) = (U \ A) ∪ (U \ B)`
   to prove the complement family is union-closed.
4. Prove the frequency identity
   `deg_complement(x) = |F| - deg_F(x)`
   for `x ∈ U`, with family-cardinality preservation explicit.
5. Transport `d004_averageRarity` to average abundance of the complement family.
6. Derive the corresponding restricted half-frequency/Frankl-abundance theorem,
   checking nontriviality hypotheses explicitly.
7. Compare only this restricted complement class against WP05 structural
   conditions and the still-open `UC-P04` representation obligation.

## D005 acceptance criteria

- the theorem hypothesis is exactly `IsFunctionalPreorderIdealFamilyOn F U`;
- complement-family carrier and cardinality semantics are explicit;
- union closure is proved from functional-preorder order-ideal intersection closure,
  not from WP06 subset-downward closure;
- rarity-to-abundance frequency arithmetic is checked in Lean;
- no `sorry`, `admit`, or new unexplained axiom is introduced;
- `UC-P04` and `UC-FRANKL` remain open;
- any later MATHCERT handoff is bounded to the exact restricted theorem.

## Boundary after D005

Even a complete D005 theorem establishes only that complements of
functional-preorder order-ideal families are a Frankl-abundant restricted class.
It does not show that an arbitrary finite union-closed family has such a
representation. That missing representation issue remains the universal
firewall.

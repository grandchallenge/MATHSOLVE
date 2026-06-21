# Object And Obstruction

## Plain Object

The local object is a finite family

```lean
F : Family alpha
U : Finset alpha
```

where `Family alpha := Finset (Finset alpha)`. The predicate
`IsIdealFamilyOn F U` says:

- every member of `F` lies inside `U`;
- `F` contains `empty`;
- `F` contains `U`;
- `U` is nonempty;
- proper members are downward closed.

The target statement is average rarity:

```lean
def IsAverageRareOn (F : Family alpha) (U : Finset alpha) : Prop :=
  2 * (F.sum fun S => S.card) <= U.card * F.card
```

This says the average size of a member of `F` is at most half the ground size.

## Exact Obstruction

The first tempting route is:

1. prove that some element is rare;
2. conclude the whole family is average-rare.

That implication is false for arbitrary finite families. One rare element only
controls one frequency. Average rarity controls the sum of every frequency:

```lean
2 * (U.sum fun x => freq F x) <= U.card * F.card
```

MATHCERT records this distinction with a checked counterexample:

```lean
existsRare_not_sufficient_for_averageRare
```

So the proof cannot stop at a rare vertex. It needs a global counting
invariant.

## Working Model

The invariant used locally is NDS, the normalized-degree sum of the predicate
family surface. The proof shows:

```lean
(toPortIdeal F U h).toSetFamily.nds <= 0
```

for every local ideal family. This is then translated back into average
rarity for `F`.

## Restricted Claim

The checked restricted claim is:

```lean
theorem localIdealFamily_averageRare
    {F : Family alpha} {U : Finset alpha}
    (h : IsIdealFamilyOn F U) :
    IsAverageRareOn F U
```

The Frankl-facing dual statement is:

```lean
theorem localIdealFamily_complement_frankl
    {F : Family alpha} {U : Finset alpha}
    (h : IsIdealFamilyOn F U) :
    IsFranklAbundant (complementFamilyOn F U)
```

## Boundary

This is a theorem about local ideal families and their complements. It is not a
classification of all union-closed families.


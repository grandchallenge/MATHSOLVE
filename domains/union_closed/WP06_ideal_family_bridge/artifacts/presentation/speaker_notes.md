# Speaker Notes: WP06 Ideal-Family Bridge

## Opening

Start with the contrast:

> Union-closed families are closed upward under unions. Ideal families are
> closed downward under taking subsets. Complements turn downward closure into
> union closure.

Then state the claim boundary immediately:

> We prove the Frankl conclusion for complements of local ideal families, not
> for every union-closed family.

## Slide 1: Object

Show `F : Family alpha` and `U : Finset alpha`. Explain that `IsIdealFamilyOn F
U` means all members live inside `U`, both extremes are present, and proper
members are downward closed.

## Slide 2: Obstruction

Use the incidence-table explanation. One rare element is one sparse column.
Average rarity is a bound on the sum of all columns. The checked counterexample
prevents an invalid shortcut.

## Slide 3: Mechanism

Draw trace and contraction:

```text
members not using v       -> trace
members using v, erase v  -> contraction
```

Explain that the proof works because the NDS difference between the original
family and the trace is exact.

## Slide 4: Induction

Say: the trace has smaller ground. The contraction branch handles the singleton
case that otherwise prevents the induction from closing.

## Slide 5: Complement Duality

Complements reverse containment. Downward closure of `F` becomes union closure
of `complementFamilyOn F U`. Rare in `F` becomes abundant in the complement.

## Closing Boundary

End with:

> WP06 closes a restricted corridor and gives later packages a checked input.
> Any broader use must prove that the target families actually enter this
> corridor.


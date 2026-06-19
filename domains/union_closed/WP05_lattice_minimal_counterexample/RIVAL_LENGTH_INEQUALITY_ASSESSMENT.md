# Rival Length Inequality Assessment

Primary source: Ivan Rival, *Lattices with doubly irreducible elements*,
Canadian Mathematical Bulletin 17 (1974), 91-95.

## Decision

Rival's finite lattice length inequality has now been formalized locally for
finite bounded lattices in `MATHCERT/MathCert/Domains/UnionClosed/RivalLength.lean`.
The proof uses source-style endpoint-inclusive irreducibility rather than
mathlib's endpoint-excluding `SupIrred` and `InfIrred` predicates.

The original blocker was an endpoint convention mismatch. Rival defines irreducible as
"not reducible", so bottom is join-irreducible unless it has a nontrivial join
decomposition, and top is meet-irreducible unless it has a nontrivial meet
decomposition. Mathlib's `SupIrred` excludes bottom and `InfIrred` excludes
top. As a result, the current local predicate

```text
RivalBound L :=
  2 * (latticeLength L + 1) <= |L| + |mathlib-doubly-irreducibles|
```

is not true for all finite bounded lattices. For example, in a two-element
chain, `latticeLength L = 1`, the mathlib doubly irreducible set is empty, and
the inequality would read `4 <= 2`.

For the Bouchard minimum-counterexample setting this mismatch is harmless only
after endpoint transfer: bottom is meet-reducible and top is join-reducible, so
Rival's doubly irreducible set agrees with the local mathlib-style
`doublyIrredFinset`. This transfer is now checked as part of
`minimumCounterexample_rivalBound`.

## Source Proof Shape

Rival's proof is short:

1. choose a maximum-size chain `C`;
2. inject `C` into the source-style join-irreducibles;
3. dually inject `C` into the source-style meet-irreducibles;
4. combine these inequalities with finite inclusion-exclusion for the join-
   and meet-irreducible sets.

The result is

```text
|L| >= 2 * (ell(L) + 1) - |Irr(L)|.
```

Equivalently, in the subtraction-free Lean style used locally:

```text
2 * (latticeLength L + 1) <= |L| + |Irr_source(L)|.
```

## Checked Lean Layer

The new file
`MATHCERT/MathCert/Domains/UnionClosed/RivalLength.lean` imports
`LatticeLength` and is included by the public `MathCert.lean` import spine.

Checked definitions:

```text
RivalSupIrred x := forall a b, x = a sup b -> x = a or x = b
RivalInfIrred x := forall a b, x = a inf b -> x = a or x = b
RivalDoublyIrred x := RivalSupIrred x and RivalInfIrred x
```

Then define `rivalSupIrredFinset`, `rivalInfIrredFinset`, and
`rivalDoublyIrredFinset`.

Checked bridge lemmas:

1. `SupIrred x -> RivalSupIrred x`;
2. `RivalSupIrred x -> x != bottom -> SupIrred x`;
3. the dual pair for meet-irreducibility and top;
4. in a minimum counterexample, `rivalDoublyIrredFinset.card =
   doublyIrredFinset.card`, using `UC-WP05-L001` and `UC-WP05-L005`.

Checked proof infrastructure:

1. finite join decomposition: every element is the join of source-style
   join-irreducibles below it;
2. finite meet decomposition, dually;
3. chain-to-join-irreducible injection: every finite chain has cardinality at
   most `rivalSupIrredFinset.card`;
4. chain-to-meet-irreducible injection, dually;
5. finite inclusion-exclusion:
   `|J| + |M| <= |L| + |J inter M|`;
6. arithmetic yielding the source-style inequality.

## Checked Formal Targets

First checked target:

```text
theorem rival_length_bound_source :
  2 * (latticeLength L + 1) <=
    Fintype.card L + (rivalDoublyIrredFinset L).card
```

Second checked target:

```text
theorem minimumCounterexample_rivalBound
    (hmin : IsMinimumCounterexample L) :
    RivalBound L
```

The checked conditional results have also been specialized:

```text
minimumCounterexample_upperConeCard_gt_latticeLength
minimumCounterexample_doublyIrred_lt_nonTop_doublyReducible
```

These remove the explicit `RivalBound` hypothesis from the promoted versions
`UC-WP05-L017A` and `UC-WP05-L018A`, while preserving the conditional versions
`UC-WP05-L017` and `UC-WP05-L018` as reusable wrappers.

## Outcome

The local proof avoids explicit chain recursion by assigning to each chain
element the cardinality of its source-style join-irreducibles below it, and
dually the cardinality of its source-style meet-irreducibles above it. Mathlib's
finite irreducible decomposition supplies the strict separators, so these
cardinality labels inject any finite chain into the appropriate source-style
irreducible set. Inclusion-exclusion then gives Rival's inequality.

The ideal-family branch remains deferred. This assessment concerns only the
finite-lattice Rival dependency needed by Bouchard Theorem 2.7 and Corollary
2.8.

# Lay Companion

## What Is the Object?

A union-closed family is a finite collection of finite sets with one rule: if
two sets are in the collection, their union is also in the collection. Frankl's
conjecture says that every nontrivial union-closed family has some element that
appears in at least half of its sets.

## Why Does WP02 Matter?

The conjecture is easy to misstate and easy to attack with arguments that feel
convincing but fail. WP02 gives the programme a precise language and a machine
checker. Definitions, elementary proofs, and finite computations now have
explicit trust boundaries.

## What Was Checked?

- Support membership has a family-member witness.
- Nontriviality means that the family contains a nonempty member.
- The union of all members belongs to a nonempty union-closed family.
- Every supported element occurs in exactly half of a full powerset.
- A singleton-containing union-closed family is Frankl-abundant.

Independent exact replay also verifies no nontrivial violations for universes
of size at most four. The general conjecture remains open.

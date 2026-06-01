# Status Audit

## Checked in Lean

| Claim ID | Meaning |
|---|---|
| `UC-WP02-L001` | Support membership has a family-member witness. |
| `UC-WP02-L002` | A singleton member yields the half-frequency inequality. |
| `UC-WP02-L003` | The top union belongs to a nonempty union-closed family. |
| `UC-WP02-L004` | Powerset frequency reaches the half bound sharply. |
| `UC-WP02-L005` | Nonempty support is equivalent to a nonempty member. |
| `UC-WP02-L006` | The singleton case yields `IsFranklAbundant`. |

## Exactly Replayed

`UC-WP01-C004` is a separate bounded claim: independent replay verifies no
nontrivial Frankl violations for universes `n <= 4`.

## Still Open

The full conjecture remains open. The current Lean files do not formalize recent
information-theoretic bounds or the external ideal-family development.

## Representation Decision

WP02 fixes `Finset (Finset α)` as the local representation. External
predicate-based formalizations should be reused through a translation layer.

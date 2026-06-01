# Theorem Spine

## Definitions

`Family`, `IsUnionClosed`, `support`, `IsNontrivial`, `freq`,
`IsFranklAbundant`, and `FranklStatementFor`.

## Checked Lemmas

| Claim ID | Human statement | Lean theorem |
|---|---|---|
| `UC-WP02-L001` | `x` lies in the support exactly when some family member contains it. | `mem_support_iff` |
| `UC-WP02-L005` | A family has nonempty support exactly when it has a nonempty member. | `isNontrivial_iff_exists_nonempty` |
| `UC-WP02-L003` | The top union belongs to a nonempty union-closed family. | `support_mem_of_nonempty` |
| `UC-WP02-L004` | A supported element occurs in exactly half of a full powerset. | `freq_powerset` |
| `UC-WP02-L002` | A singleton member yields the half-frequency inequality. | `singleton_case_target` |
| `UC-WP02-L006` | A singleton member yields a Frankl-abundance witness. | `singleton_case_abundant` |

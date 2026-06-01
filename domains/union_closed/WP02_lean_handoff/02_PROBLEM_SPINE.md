# Problem Spine

## Informal-to-Formal Dictionary

| Informal object | Lean definition |
|---|---|
| Finite family of sets | `Family α := Finset (Finset α)` |
| Union-closed | `IsUnionClosed F := ∀ A ∈ F, ∀ B ∈ F, A ∪ B ∈ F` |
| Support | `support F := F.biUnion id` |
| Nontrivial | `IsNontrivial F := (support F).Nonempty` |
| Frequency of `x` | `freq F x := (F.filter (fun A => x ∈ A)).card` |
| Frankl-abundant | `∃ x ∈ support F, 2 * freq F x ≥ F.card` |
| Frankl statement over `α` | `FranklStatementFor α` |

The checked theorem `isNontrivial_iff_exists_nonempty` proves that the chosen
nontriviality definition is equivalent to saying that `F` contains a nonempty
member.

## Certification Boundary

`FranklStatementFor α` is a formal statement scaffold. It is intentionally not
proved. Restricted cases remain separate claims with their own IDs.

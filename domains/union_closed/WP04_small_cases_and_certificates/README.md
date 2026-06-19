# WP04: Small Cases and Exact Certificates

## 1. Lay executive companion

The first bounded computations and restricted proofs are now independently
checkable. Exact replay finds no Frankl violations on universes `n <= 4`.
Lean checks the singleton-containing case and the stronger two-element-member
case. These results are infrastructure and restricted theorems, not a proof of
the full conjecture.

## 2. Theorem spine

- `UC-WP02-L002`: if `{a}` belongs to a union-closed family, then `a` appears in
  at least half its members.
- `UC-WP04-L001`: if `{a, b}` belongs to a union-closed family, then at least one
  of `a` and `b` appears in at least half its members.
- `UC-WP01-C004`: independent exact replay verifies no nontrivial violations for
  universes `n <= 4`.

## 3. Certification boundary

- The two restricted theorems are Lean-checked.
- The bounded audit is exact Python replay with a hashed certificate artifact.
- No general theorem about Frankl's conjecture is claimed.

## 4. Next analytic target

Completed in WP03/WP05: the external ideal-family Lean work is a reuse branch,
and `UC-WP05-L001`, the at-least-two-atoms condition for a minimum-size lattice
counterexample, is now Lean-checked with its deletion infrastructure.

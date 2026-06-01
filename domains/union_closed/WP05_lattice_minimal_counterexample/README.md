# WP05: Lattice-Minimal-Counterexample Corridor

## 1. Purpose

Select the first original restricted-theorem corridor without duplicating the
existing ideal-family Lean development.

## 2. Selected corridor

Reconstruct the necessary conditions for a minimum-size lattice counterexample
from [Bouchard, 2025](https://arxiv.org/abs/2503.00277). Translate one condition
at a time into the explicit finite-family representation already used by
MATHCERT.

## 3. Certification boundary

No new theorem is claimed in this intake package. The source conditions remain
`LITERATURE_DERIVED` until reconstructed in a theorem spine and either proved
locally or formalized.

## 4. Reuse decision

The ideal-family branch is deferred because a public Lean development already
exists at [`kashiwabarakenji/frankl_lean`](https://github.com/kashiwabarakenji/frankl_lean).
If that branch is activated later, add a translation layer between its
predicate-based families and MATHCERT's explicit finite families.

## 5. Next analytic target

Produce a theorem-spine package listing Bouchard's minimum-counterexample
conditions with exact hypotheses, then nominate the smallest Lean-ready
condition as `UC-WP05-L001`.

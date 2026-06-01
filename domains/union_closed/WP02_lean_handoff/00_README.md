# WP02: Lean Handoff and First Checked Lemmas

## Metadata

- Domain: Union-Closed Sets / Frankl's Conjecture
- Work Package number: WP02
- Primary type: `FORMALIZATION_HANDOFF`
- Claim status: accepted local certification substrate

## Result

WP02 is complete. MATHCERT now has a reproducible Lean 4.29.1 package, a clean
formal statement of Frankl's conjecture, six checked local claims, exact bounded
certificate replay, and CI gates for proof placeholders and malformed ledgers.

This package does not prove Frankl's conjecture. It establishes a trustworthy
formal layer for later restricted theorems.

## Package Map

- `01_LAY_COMPANION.md`: the object and why WP02 matters.
- `02_PROBLEM_SPINE.md`: definitions and formal dictionary.
- `03_STATUS_AUDIT.md`: checked, computed, and open claims.
- `04_THEOREM_SPINE.md`: human and Lean theorem statements.
- `05_PROOFS_AND_COMPUTATIONS.md`: proof ideas and replay commands.
- `06_FAILURE_ANALYSIS.md`: resolved setup and formalization failures.
- `07_CLAIM_LEDGER.yaml`: canonical WP02 claim ledger.
- `08_CERT_HANDOFF.md`: MATHCERT interface and dependencies.
- `09_NEXT_TARGET.md`: the next sharp move.

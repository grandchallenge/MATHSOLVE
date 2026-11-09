# OAI26-WP01 — First-25 protected technical evidence reconciliation

This record binds the **pre-existing protected MATHFORGE hardened Comparator receipts** for zero-based declaration indices 0–24 to the first 25 entries of the same pinned crosswalk used by MATHSOLVE worker #1099.

- Immutable upstream: `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`
- Lean: `leanprover/lean4:v4.34.1`
- Lake manifest SHA-256: `cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794`
- Protected MATHFORGE source snapshot: `2ca2c18a7e37201bbf5958857ef0b267beb19811`
- Existing hardened Comparator: **25/25 historical protected receipts reconciled**, 25 distinct live GitHub Actions run readbacks completed/success, no declaration identity discrepancies
- Additional CHAD local diagnostic replay: 19/25 compile plus axiom checks PASS; 6/25 timed out on cold dependency builds; local Comparator executable was not present, so **zero new local Comparator passes**
- Hostile fixtures observed: nonexistent theorem identifier returned Lean unknownIdentifier (exit 1); injected unexpected axiom surfaced via `#print axioms`

The historical rejected worker comment and later corrected valid `EXACT_BLOCKER` return, its protected raw receipt, and its `received_unadjudicated` intake state are **not changed**. This is an operator-side, read-only evidentiary reconciliation, not worker impersonation, certification, mathematical-semantic review, or permission to promote a result. It supports a subsequent bounded technical disposition for first-batch coverage, with independent critical review if scope requires.

Canonical machine rows: [FIRST25_TECHNICAL_RECONCILIATION.json](FIRST25_TECHNICAL_RECONCILIATION.json). Individual row links carry protected ledger blob identities, actual run IDs and head SHAs, as well as CHAD-local status without conflating its timeouts with upstream Comparator verdicts.

# WP06: Ideal-Family Bridge Pedagogical Package

## Metadata

- Domain: Union-Closed Sets / Frankl's Conjecture
- Work Package number: WP06
- Primary type: `FORMALIZATION_EXPOSITION`
- Mathematical status: checked local restricted theorem
- Certification boundary: MATHCERT Lean proofs and replay gates
- Programme protocol: `CHAIDEZ-PEDAGOGY-001`

## Purpose

WP06 packages the ideal-family bridge work into presentation-ready artifacts.
The checked mathematics lives in MATHCERT; this package makes the object,
obstruction, theorem spine, proof boundary, and next executable move legible
for a serious reader.

The central result is restricted:

> A local finite ideal family has average rarity, and the complement of such a
> family is a union-closed family satisfying the Frankl half-frequency
> conclusion.

This does not prove Frankl's conjecture for arbitrary union-closed families.
It proves a controlled ideal-family corridor and records exactly why that
corridor is useful.

## Chaidez Contract Map

| Required artifact | File |
|---|---|
| `RESULT_STATUS` | `01_RESULT_STATUS.md` |
| `LAY_COMPANION` | `02_LAY_COMPANION.md` |
| `OBJECT_AND_OBSTRUCTION` | `03_OBJECT_AND_OBSTRUCTION.md` |
| `STATUS_AUDIT` | `04_STATUS_AUDIT.md` |
| `CLAIM_LEDGER` | `09_CLAIM_LEDGER.yaml` |
| `THEOREM_SPINE` | `05_THEOREM_SPINE.md` |
| `DEPENDENCY_DAG` | `06_DEPENDENCY_DAG.md` |
| `PROOFS_AND_COMPUTATIONS` | `07_PROOFS_AND_COMPUTATIONS.md` |
| `FAILURE_AND_NEGATIVE_RESULTS` | `08_FAILURE_AND_NEGATIVE_RESULTS.md` |
| `PROOF_DEBT_REGISTER` | `10_PROOF_DEBT_REGISTER.md` |
| `CERT_HANDOFF` | `11_CERT_HANDOFF.md` |
| `NEXT_EXECUTABLE_STEP` | `12_NEXT_EXECUTABLE_STEP.md` |

Presentation helpers:

- `artifacts/figures/ideal_family_bridge_dag.mmd`
- `artifacts/presentation/one_page_handout.md`
- `artifacts/presentation/speaker_notes.md`

## Reading Order

1. Start with `02_LAY_COMPANION.md`.
2. Use `03_OBJECT_AND_OBSTRUCTION.md` to explain why rare vertices alone are
   not enough.
3. Use `06_DEPENDENCY_DAG.md` and the Mermaid diagram for the theorem spine.
4. Use `09_CLAIM_LEDGER.yaml` and `11_CERT_HANDOFF.md` for the trust boundary.
5. End with `12_NEXT_EXECUTABLE_STEP.md`.


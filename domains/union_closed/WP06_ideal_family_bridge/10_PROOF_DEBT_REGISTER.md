# Proof Debt Register

## Current Debt State

WP06 discharges the local NDS nonpositivity debt that previously blocked the
unconditional ideal-family average-rarity theorem.

No active proof debt blocks the checked WP06 theorem itself.

## Debt Items

| Debt ID | Category | Status | Blocks | Discharge condition |
|---|---|---|---|---|
| `WP06-PD-001` | `EXTERNAL_SOURCE` | Superseded | Upstream NDS theorem promotion | Placeholder-free upstream audit and reproducible build, or local replacement proof. Local replacement proof is checked. |
| `WP06-PD-002` | `UNPROVED_BRIDGE` | Discharged | `localIdealFamily_averageRare` | Prove `localIdealFamily_port_nds_nonpos`; checked in MATHCERT. |
| `WP06-PD-003` | `SEMANTIC_CORRESPONDENCE` | Discharged | Local-to-ported ideal translation | Carrier, degree, and NDS equivalence theorems checked. |
| `WP06-PD-004` | `MISSING_LEMMA` | Discharged | Trace/contraction induction | Trace, contraction, exact NDS difference, singleton branch, and endgame induction checked. |
| `WP06-PD-005` | `SEMANTIC_CORRESPONDENCE` | Discharged | Frankl-facing complement statement | Complement family union-closure and rarity-to-abundance transfer checked. |

## Remaining Campaign Debt

| Debt ID | Category | Status | Blocks | Discharge condition |
|---|---|---|---|---|
| `WP06-PD-006` | `SEMANTIC_CORRESPONDENCE` | Open outside WP06 | Using WP06 for arbitrary union-closed families | Prove a separate theorem that the target union-closed class arises as complements of local ideal families, or restrict the claim explicitly. |
| `WP06-PD-007` | `EXTERNAL_SOURCE` | Open outside WP06 | Upstream theorem reuse as trusted dependency | Audit a newer upstream commit with no placeholders and a reproducible build on its pinned toolchain. |

## Presentation Boundary

When presenting WP06, say:

> The ideal-family corridor is closed locally.

Do not say:

> The ideal-family corridor covers all union-closed families.

## Chaidez v2 debt controls

The following completes the existing debt records without reopening discharged
local obligations or treating future campaign debt as a proof of anything.

| debt_id | category | blocked_node | present_evidence | discharge_condition | route / owner | status |
|---|---|---|---|---|---|---|
| WP06-PD-001 | EXTERNAL_SOURCE | WP06-UPSTREAM-REUSE | Local replacement NDS proof is checked; the old upstream placeholder audit remains provenance. | Use the checked local proof instead of the historically unverified upstream theorem. | FORMAL_PROOF / MATHSOLVE source audit | SUPERSEDED |
| WP06-PD-002 | UNPROVED_BRIDGE | WP06-S8 | UC-WP06-L007 records the checked local NDS and average-rarity bridge. | Prove localIdealFamily_port_nds_nonpos; already checked. | FORMAL_PROOF / MATHCERT | DISCHARGED |
| WP06-PD-003 | SEMANTIC_CORRESPONDENCE | WP06-S1 | Carrier, degree and NDS translation equivalences are checked. | Replay the local-to-ported equivalence theorems. | FORMAL_PROOF / MATHCERT | DISCHARGED |
| WP06-PD-004 | MISSING_LEMMA | WP06-S7 | Trace, contraction, exact NDS difference and endgame induction are checked. | Replay the complete finite trace/contraction chain. | FORMAL_PROOF / MATHCERT | DISCHARGED |
| WP06-PD-005 | SEMANTIC_CORRESPONDENCE | WP06-S9 | UC-WP06-L008 records checked complement union-closure and abundance transfer. | Replay the restricted complement-duality theorem. | FORMAL_PROOF / MATHCERT | DISCHARGED |
| WP06-PD-006 | SEMANTIC_CORRESPONDENCE | WP06-FUTURE-CLASS | No bridge from arbitrary union-closed families is asserted. | Prove a separate class-representation theorem or retain the restricted claim. | FORMAL_PROOF / MATHSOLVE | OPEN |
| WP06-PD-007 | EXTERNAL_SOURCE | WP06-UPSTREAM-REUSE | The upstream proof surface had placeholders at the recorded audit commit. | Audit a newer placeholder-free exact upstream commit and reproduce its pinned toolchain build. | FORMAL_PROOF / MATHSOLVE source audit | OPEN |


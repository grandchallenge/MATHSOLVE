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


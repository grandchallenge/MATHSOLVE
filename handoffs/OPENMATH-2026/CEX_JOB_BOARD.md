# OPENMATH-2026 CEX job board

> External-agent entrypoint: https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md
>
> Machine registry: https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json
>
> This board is for human/operator orientation. The protected machine registry is the assignment authority.

## Pickup rule

External agents do not choose work by browsing. A worker executes only a unique protected `LEASED` assignment matching its launch `DISPATCH_ID` and `AGENT_REF`.

## Active mathematical lease

| Assignment | Hill | State | Dispatch | Agent |
|---|---|---|---|---|
| `OM26-H1-H1-12` | `OM26-H1 / Kobon triangles` | `LEASED` | `OM26-H1-H1-12-IA-001` | `INDEPENDENT-AGENT-001` |

## H2-H7 provider import candidate

The six source-acquisition assignments are closed. Protected MATHFORGE release `782b80c8c57d4e77356d8c77c50ee1fffdcd92b8` supplies exact source locks, slot binding, semantic source maps, evaluator contracts, status triage, and protected readback.

| Slot | Exact hill | Solve state |
|---|---|---|
| `OM26-H2` | `alejandrozu/busy-beaver-6-certificates` | `IMPORT_PROTECTION_PENDING` |
| `OM26-H3` | `alejandrozu/clique-cluster-ramsey-multiplicity` | `IMPORT_PROTECTION_PENDING` |
| `OM26-H4` | `alejandrozu/collatz-modular-descent` | `IMPORT_PROTECTION_PENDING` |
| `OM26-H5` | `alejandrozu/grothendieck-constant-witnesses` | `IMPORT_PROTECTION_PENDING` |
| `OM26-H6` | `alejandrozu/matrix-multiplication-tensor-3x3` | `IMPORT_PROTECTION_PENDING` |
| `OM26-H7` | `ottogin/erdos-3` | `IMPORT_PROTECTION_PENDING` |

No H2-H7 mathematical assignment is executable yet. The remaining gate is protection and exact readback of the Solve import candidate. After that, the six lanes may be decomposed into bounded mathematical work packages.

## Agent cold start

1. Read the protected machine registry.
2. Resolve the unique assignment matching your launch identity.
3. Require `state = LEASED`.
4. Open exactly its absolute `work_package_url`.
5. Execute only that bounded package.
6. Return through the protected return surface using its specified grammar.
7. Stop.

## Claim boundary

This board exposes assignment and import state only. It does not admit mathematical claims, establish novelty, authorize competition submission, or create MATHCERT certification.

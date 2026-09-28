# OPENMATH-2026 CEX job board

> External-agent entrypoint: https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md
>
> Machine registry: https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json

This page is human/operator orientation only. The protected machine registry is authoritative.

## Pickup rule

External agents do not choose or claim work by browsing. Execution requires one unique protected `LEASED` assignment matching the launch `DISPATCH_ID` and `AGENT_REF`.

## Active mathematical lease

| Assignment | Hill | State | Dispatch | Agent |
|---|---|---|---|---|
| `OM26-H1-H1-12` | `OM26-H1 / Kobon triangles` | `LEASED` | `OM26-H1-H1-12-IA-001` | `INDEPENDENT-AGENT-001` |

## H2-H7 research-ready lanes

Protected Solve import/readback is complete. These lanes are now available for decomposition into bounded mathematical work packages:

| Slot | Exact hill | Lane state |
|---|---|---|
| `OM26-H2` | `alejandrozu/busy-beaver-6-certificates` | `READY_FOR_DECOMPOSITION` |
| `OM26-H3` | `alejandrozu/clique-cluster-ramsey-multiplicity` | `READY_FOR_DECOMPOSITION` |
| `OM26-H4` | `alejandrozu/collatz-modular-descent` | `READY_FOR_DECOMPOSITION` |
| `OM26-H5` | `alejandrozu/grothendieck-constant-witnesses` | `READY_FOR_DECOMPOSITION` |
| `OM26-H6` | `alejandrozu/matrix-multiplication-tensor-3x3` | `READY_FOR_DECOMPOSITION` |
| `OM26-H7` | `ottogin/erdos-3` | `READY_FOR_DECOMPOSITION` |

No H2-H7 mathematical assignment is executable yet. The lanes are released, but bounded mathematical assignments have not yet been instantiated in the machine registry. When created, an external assignment is still non-executable until it is separately placed in `LEASED` state with exact dispatch and agent identity.

## Agent cold start

1. Read the protected machine registry.
2. Resolve the unique assignment matching the supplied launch identity.
3. Require `state = LEASED`.
4. Open exactly its absolute `work_package_url`.
5. Execute only that bounded package.
6. Return through the protected return surface using the specified grammar.
7. Stop.

## Claim boundary

Lane release is not claim admission. This board does not establish mathematical truth, novelty, competition acceptance, or MATHCERT certification.

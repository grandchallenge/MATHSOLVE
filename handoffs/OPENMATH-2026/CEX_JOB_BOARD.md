# OPENMATH-2026 CEX job board

> External-agent entrypoint: https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md
>
> Machine registry: https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json

This page is human/operator orientation only. The protected machine registry is authoritative.

## Pickup rule

External agents do not choose work by browsing. Execution requires one unique protected `LEASED` assignment matching the launch `DISPATCH_ID` and `AGENT_REF`.

## Current seven-hill independent-agent lifecycle

Current authority is per exact hill lane `OM26-H1` through `OM26-H7`. Historical aggregate labels such as `H2-H7` identify closed onboarding tranches only; they are not current campaign partitions.

| Assignment | Hill | State | Dispatch | Agent | Return issue |
|---|---|---|---|---|---|
| `OM26-H1-H1-12` | `OM26-H1` | `ACCEPTED` | `OM26-H1-H1-12-IA-001` | `INDEPENDENT-AGENT-001` | #498 |
| `OM26-H2-WP01` | `OM26-H2` | `ACCEPTED` | `OM26-H2-WP01-IA-001` | `INDEPENDENT-AGENT-002` | #505 |
| `OM26-H2-WP02` | `OM26-H2` | `ACCEPTED` | `OM26-H2-WP02-IA-001` | `INDEPENDENT-AGENT-008` | #526 |
| `OM26-H2-WP03` | `OM26-H2` | `LEASED_NOT_LAUNCHED` | `OM26-H2-WP03-IA-001` | `INDEPENDENT-AGENT-009` | #537 |
| `OM26-H3-WP01` | `OM26-H3` | `LEASED_NOT_LAUNCHED` | `OM26-H3-WP01-IA-001` | `INDEPENDENT-AGENT-003` | #506 |
| `OM26-H4-WP01` | `OM26-H4` | `LEASED_NOT_LAUNCHED` | `OM26-H4-WP01-IA-001` | `INDEPENDENT-AGENT-004` | #507 |
| `OM26-H5-WP01` | `OM26-H5` | `LEASED_NOT_LAUNCHED` | `OM26-H5-WP01-IA-001` | `INDEPENDENT-AGENT-005` | #508 |
| `OM26-H6-WP01` | `OM26-H6` | `LEASED_NOT_LAUNCHED` | `OM26-H6-WP01-IA-001` | `INDEPENDENT-AGENT-006` | #509 |
| `OM26-H7-WP01` | `OM26-H7` | `LEASED_NOT_LAUNCHED` | `OM26-H7-WP01-IA-001` | `INDEPENDENT-AGENT-007` | #510 |

Agent 001 returned one result on #498. The original intake rejected it because of an intake infrastructure defect; the exact result was recovered and has now been adjudicated as `ACCEPTED_SOURCE_CONDITIONAL_REDUCTION`. Its q=5 reduction is accepted at Solve level only; it is **not** MATHCERT certification and does not establish hill-global optimality.

Agent 002 returned one valid result on #505. Its independent scorer concordance, baseline replay, minimum-step argument, and private-budget reconstruction are accepted at Solve level as `ACCEPTED_SCORER_CONCORDANCE_WITH_SEARCH_NARROWING`. The proposed first-write=`1` TNF normalization is not accepted as WLOG, and heuristic pruning remains noncanonical until exact soundness is proved.

Agent 008 returned WP02 and its two finite witnesses were independently replayed and accepted at Solve level: `(89911,185,541)` and first-write-zero `(8021,41,122)`. The stronger `EXACT_SEARCH_DESIGN_VALIDATED` claim was not admitted because the returned replay used a circular protected-evaluator wrapper, contained an internal `121` versus `122` tape-span contradiction, and omitted the claimed distinct unpruned comparator. WP03 is now the active H2 replay-closure lease for Agent 009 on issue #537. Agents 003-007 retain their protected one-to-one leases with no durable launch/result evidence; H2 WP03 and each currently executable peer hill are `LEASED_NOT_LAUNCHED`.

`LEASED` does not imply `LAUNCHED`; `RETURNED` does not imply `CAPTURED`; `CAPTURED` does not imply `ACCEPTED` or `CERTIFIED`.

Every active hill lease is independent-blind and one-to-one. No agent may substitute for another `AGENT_REF`, and no issue other than the bound return issue is accepted for that dispatch.

## Current launcher links

The canonical external launch surface is one immutable public task link per peer hill. Historical files under `handoffs/OPENMATH-2026/jobs/` remain frozen provenance and SHALL NOT be used as current launch tasks.

- H1: guard only; no active successor lease.
- H2: https://github.com/grandchallenge/MATHSOLVE/blob/e64c93148ddecbc8e51352c24926898e42b8ea10/handoffs/OPENMATH-2026/launch/OM26-H2-WP03.md
- H3: https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H3.md
- H4: https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H4.md
- H5: https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H5.md
- H6: https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H6.md
- H7: https://github.com/grandchallenge/MATHSOLVE/blob/f2c23b010687052ee442a2d7fc1991a2c4d2700b/handoffs/OPENMATH-2026/launch/OM26-H7.md

## Launcher contract

Canonical mode is `LINK_IN_RELAY_OUT`.

After verifying the protected lease, the launcher gives the zero-context worker only the registered immutable task URL plus a short instruction to read the complete task and follow its return contract. The worker needs public read access only; GitHub authentication and repository discovery are not required.

The linked document is self-contained. The human operator does not locate, copy, or paste the work package. If public task read is unavailable, the launcher hydrates the worker from the exact pinned artifact automatically.

The normal return path is `GCL-RETURN-RELAY/1` back to the launching conversation. Authenticated GCL infrastructure then performs durable GitHub intake under governed credentials.

Direct agent-to-GitHub posting is optional when explicitly available, never required.

Transport contract:
https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_TRANSPORT_CONTRACT.md
## Claim boundary

A lease authorizes bounded external work. It does not admit returned mathematics, establish novelty, authorize competition submission, or create MATHCERT certification. No OPENMATH-2026 hill currently has a recorded official competition submission.

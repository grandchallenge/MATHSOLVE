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
| `OM26-H2-WP02` | `OM26-H2` | `LEASED_NOT_LAUNCHED` | `OM26-H2-WP02-IA-001` | `INDEPENDENT-AGENT-008` | #526 |
| `OM26-H3-WP01` | `OM26-H3` | `LEASED_NOT_LAUNCHED` | `OM26-H3-WP01-IA-001` | `INDEPENDENT-AGENT-003` | #506 |
| `OM26-H4-WP01` | `OM26-H4` | `LEASED_NOT_LAUNCHED` | `OM26-H4-WP01-IA-001` | `INDEPENDENT-AGENT-004` | #507 |
| `OM26-H5-WP01` | `OM26-H5` | `LEASED_NOT_LAUNCHED` | `OM26-H5-WP01-IA-001` | `INDEPENDENT-AGENT-005` | #508 |
| `OM26-H6-WP01` | `OM26-H6` | `LEASED_NOT_LAUNCHED` | `OM26-H6-WP01-IA-001` | `INDEPENDENT-AGENT-006` | #509 |
| `OM26-H7-WP01` | `OM26-H7` | `LEASED_NOT_LAUNCHED` | `OM26-H7-WP01-IA-001` | `INDEPENDENT-AGENT-007` | #510 |

Agent 001 returned one result on #498. The original intake rejected it because of an intake infrastructure defect; the exact result was recovered and has now been adjudicated as `ACCEPTED_SOURCE_CONDITIONAL_REDUCTION`. Its q=5 reduction is accepted at Solve level only; it is **not** MATHCERT certification and does not establish hill-global optimality.

Agent 002 returned one valid result on #505. Its independent scorer concordance, baseline replay, minimum-step argument, and private-budget reconstruction are accepted at Solve level as `ACCEPTED_SCORER_CONCORDANCE_WITH_SEARCH_NARROWING`. The proposed first-write=`1` TNF normalization is not accepted as WLOG, and heuristic pruning remains noncanonical until exact soundness is proved.

WP02 is the active H2 successor lease. Agent 008 must construct a complete exact-search design with proved symmetry reductions and exact pruning, using issue #526 as the sole return surface. Agents 003-007 retain their protected one-to-one leases with no durable launch/result evidence; all six active leases are `LEASED_NOT_LAUNCHED`.

`LEASED` does not imply `LAUNCHED`; `RETURNED` does not imply `CAPTURED`; `CAPTURED` does not imply `ACCEPTED` or `CERTIFIED`.

Every active hill lease is independent-blind and one-to-one. No agent may substitute for another `AGENT_REF`, and no issue other than the bound return issue is accepted for that dispatch.

## Current launcher scripts

The canonical launcher-facing scripts are under `handoffs/OPENMATH-2026/launch/`, one file per peer hill. Historical files under `handoffs/OPENMATH-2026/jobs/` remain frozen provenance and SHALL NOT be used as current launch scripts.

- H1: `launch/OM26-H1.md` — guard only; no active successor lease.
- H2: `launch/OM26-H2.md` — current executable WP02 envelope.
- H3: `launch/OM26-H3.md` — current executable WP01 envelope.
- H4: `launch/OM26-H4.md` — current executable WP01 envelope.
- H5: `launch/OM26-H5.md` — current executable WP01 envelope.
- H6: `launch/OM26-H6.md` — current executable WP01 envelope.
- H7: `launch/OM26-H7.md` — current executable WP01 envelope.

## Launcher contract

External agents are launched as self-contained intelligence workers. They are not required to authenticate to GitHub.

The launcher MUST supply the exact protected task content needed for execution plus:

```text
DISPATCH_ID: <exact protected dispatch id>
AGENT_REF: <exact protected agent ref>
INTENDED_RETURN: <exact protected return URL>
```

The normal return path is `GCL-RETURN-RELAY/1` back to the launching conversation. Authenticated GCL infrastructure then performs durable GitHub intake under governed credentials.

Direct agent-to-GitHub posting is optional when explicitly available, never required.

Transport contract:
https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_TRANSPORT_CONTRACT.md
## Claim boundary

A lease authorizes bounded external work. It does not admit returned mathematics, establish novelty, authorize competition submission, or create MATHCERT certification. No OPENMATH-2026 hill currently has a recorded official competition submission.

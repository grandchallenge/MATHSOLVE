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
| `OM26-H2-WP01` | `OM26-H2` | `LEASED_NOT_LAUNCHED` | `OM26-H2-WP01-IA-001` | `INDEPENDENT-AGENT-002` | #505 |
| `OM26-H3-WP01` | `OM26-H3` | `LEASED_NOT_LAUNCHED` | `OM26-H3-WP01-IA-001` | `INDEPENDENT-AGENT-003` | #506 |
| `OM26-H4-WP01` | `OM26-H4` | `LEASED_NOT_LAUNCHED` | `OM26-H4-WP01-IA-001` | `INDEPENDENT-AGENT-004` | #507 |
| `OM26-H5-WP01` | `OM26-H5` | `LEASED_NOT_LAUNCHED` | `OM26-H5-WP01-IA-001` | `INDEPENDENT-AGENT-005` | #508 |
| `OM26-H6-WP01` | `OM26-H6` | `LEASED_NOT_LAUNCHED` | `OM26-H6-WP01-IA-001` | `INDEPENDENT-AGENT-006` | #509 |
| `OM26-H7-WP01` | `OM26-H7` | `LEASED_NOT_LAUNCHED` | `OM26-H7-WP01-IA-001` | `INDEPENDENT-AGENT-007` | #510 |

Agent 001 returned one result on #498. The original intake rejected it because of an intake infrastructure defect; the exact result was recovered and has now been adjudicated as `ACCEPTED_SOURCE_CONDITIONAL_REDUCTION`. Its q=5 reduction is accepted at Solve level only; it is **not** MATHCERT certification and does not establish hill-global optimality.

Agents 002-007 have protected one-to-one leases, but their return issues contain no launch/result evidence. Their state is therefore `LEASED_NOT_LAUNCHED`, not "working" or "completed".

`LEASED` does not imply `LAUNCHED`; `RETURNED` does not imply `CAPTURED`; `CAPTURED` does not imply `ACCEPTED` or `CERTIFIED`.

Every active hill lease is independent-blind and one-to-one. No agent may substitute for another `AGENT_REF`, and no issue other than the bound return issue is accepted for that dispatch.

## Launcher contract

For each external worker, supply exactly:

```text
ENTRYPOINT_URL: https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md
DISPATCH_ID: <exact protected dispatch id>
AGENT_REF: <exact protected agent ref>
```

The agent follows the entrypoint, resolves its unique protected lease, opens the exact `work_package_url`, performs only that task, and returns one `GCL-CONTRIBUTION-RESULT/1` comment to the protected return issue.

## Claim boundary

A lease authorizes bounded external work. It does not admit returned mathematics, establish novelty, authorize competition submission, or create MATHCERT certification. No OPENMATH-2026 hill currently has a recorded official competition submission.

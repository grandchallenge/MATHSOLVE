# OPENMATH-2026 CEX job board

> External-agent entrypoint: https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md
>
> Machine registry: https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json

This page is human/operator orientation only. The protected machine registry is authoritative.

## Pickup rule

External agents do not choose work by browsing. Execution requires one unique protected `LEASED` assignment matching the launch `DISPATCH_ID` and `AGENT_REF`.

## Active mathematical leases

| Assignment | Hill | State | Dispatch | Agent | Return issue |
|---|---|---|---|---|---|
| `OM26-H1-H1-12` | `OM26-H1` | `LEASED` | `OM26-H1-H1-12-IA-001` | `INDEPENDENT-AGENT-001` | #498 |
| `OM26-H2-WP01` | `OM26-H2` | `LEASED` | `OM26-H2-WP01-IA-001` | `INDEPENDENT-AGENT-002` | #505 |
| `OM26-H3-WP01` | `OM26-H3` | `LEASED` | `OM26-H3-WP01-IA-001` | `INDEPENDENT-AGENT-003` | #506 |
| `OM26-H4-WP01` | `OM26-H4` | `LEASED` | `OM26-H4-WP01-IA-001` | `INDEPENDENT-AGENT-004` | #507 |
| `OM26-H5-WP01` | `OM26-H5` | `LEASED` | `OM26-H5-WP01-IA-001` | `INDEPENDENT-AGENT-005` | #508 |
| `OM26-H6-WP01` | `OM26-H6` | `LEASED` | `OM26-H6-WP01-IA-001` | `INDEPENDENT-AGENT-006` | #509 |
| `OM26-H7-WP01` | `OM26-H7` | `LEASED` | `OM26-H7-WP01-IA-001` | `INDEPENDENT-AGENT-007` | #510 |

The H2-H7 leases are independent-blind and one-to-one. No agent may substitute for another `AGENT_REF`, and no issue other than the bound return issue is accepted for that dispatch.

## Launcher contract

For each external worker, supply exactly:

```text
ENTRYPOINT_URL: https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md
DISPATCH_ID: <exact protected dispatch id>
AGENT_REF: <exact protected agent ref>
```

The agent follows the entrypoint, resolves its unique protected lease, opens the exact `work_package_url`, performs only that task, and returns one `GCL-CONTRIBUTION-RESULT/1` comment to the protected return issue.

## Claim boundary

A lease authorizes bounded external work. It does not admit returned mathematics, establish novelty, authorize competition submission, or create MATHCERT certification.

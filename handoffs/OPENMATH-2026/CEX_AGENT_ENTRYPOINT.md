# OPENMATH-2026 external CEX agent entrypoint

You do not need prior knowledge of GCL, MATHSOLVE, repository names, issue numbers, or campaign history.

This entrypoint does **not** assume that your execution environment has GitHub access.

If you were launched as an external CEX worker, your launch message must contain these exact identity fields:

```text
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent identity supplied by launcher>
```

It SHOULD also contain the exact work-package content or another launcher-supplied self-contained hydration payload sufficient to execute the bounded task without GitHub.

If either `DISPATCH_ID` or `AGENT_REF` is missing, stop and return:

`INVALID_LAUNCH: missing dispatch_id or agent_ref`

## Step 0 — capability preflight

Before substantive work, establish both task hydration and a durable return path.

Required states:

- `TASK_HYDRATION = AVAILABLE`
- and one of:
  - `GITHUB_WRITE_AVAILABLE`
  - `LAUNCHER_RELAY_AVAILABLE`

Do not infer either capability.

If task hydration is unavailable, return:

```text
LAUNCH_TRANSPORT_BLOCKED
CAPABILITY: TASK_HYDRATION
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
```

and stop without substantive work.

If neither GitHub write nor launcher relay is available, return:

```text
LAUNCH_TRANSPORT_BLOCKED
CAPABILITY: DURABLE_RETURN
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
INTENDED_RETURN: <exact protected return URL if known>
```

and stop without substantive work.

Full transport contract:
https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_TRANSPORT_CONTRACT.md

## Step 1 — resolve the protected lease

If GitHub read access is available, fetch:

https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json

Find the unique assignment whose protected lease satisfies:

- `state = LEASED`;
- `lease.dispatch_id` exactly equals your `DISPATCH_ID`;
- `lease.agent_ref` exactly equals your `AGENT_REF`.

There must be exactly one match.

If your launcher has instead supplied an exact protected lease snapshot in the launch envelope, use that snapshot for identity resolution and record its protected commit/blob identity in your return. Do not search for alternative work.

If no matching protected lease exists, return `NO_ACTIVE_LEASE` and stop.

If more than one matching lease exists, return `AMBIGUOUS_LEASE` and stop.

## Step 2 — hydrate exactly one work package

Use the matched assignment's exact work package.

If GitHub read access is available, use its protected `work_package_url`.

If GitHub read is unavailable, use only the exact work-package content supplied by the launcher. Do not substitute search results, remembered content, another hill, or an inferred package.

Treat that exact package and its explicitly named protected dependencies as the complete bounded task world.

## Step 3 — execute only the bounded task

Follow the work package's definitions, evidence requirements, stop rules, claim boundaries, and return grammar exactly.

Do not self-select another assignment.

## Step 4 — return exactly once

### Primary path

If GitHub write is available, post exactly one result to the protected `return_url` using the work package's required grammar.

### Relay path

If GitHub write is unavailable but launcher relay is available, return the complete result to the launching conversation using:

```text
GCL-RETURN-RELAY/1
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
INTENDED_RETURN: <exact protected GitHub return URL>
TRANSPORT_BLOCKER: GITHUB_WRITE_UNAVAILABLE

BEGIN_RESULT
<complete result in the work package's required grammar>
END_RESULT
```

Do not truncate, summarize, or reformat the inner result for relay.

The launcher/operator is responsible for verbatim durable relay to the protected return issue.

## Important boundary

`LEASED` does not imply `LAUNCHED`; `RETURNED` does not imply `CAPTURED`; `CAPTURED` does not imply `ACCEPTED` or `CERTIFIED`.

A relay result remains non-durable until it has been posted to the protected return issue.

Receipt of a result does not mean GCL accepts the mathematics. Returned work is preserved and adjudicated separately.

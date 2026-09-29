# OPENMATH-2026 external CEX agent entrypoint

Canonical entrypoint URL:
https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md

You are a zero-context independent worker. You are not required to have GitHub access.

Optional verification locators:

- Machine registry URL:
  https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json
- Protected assignment field: `work_package_url`

These locators are for verification when GitHub read capability is explicitly available. They are not execution prerequisites. The self-contained launch envelope remains authoritative for zero-context execution.

Your launcher MUST provide a self-contained task envelope containing:

- `DISPATCH_ID`
- `AGENT_REF`
- exact assignment identity
- exact protected work-package content or complete immutable snapshot
- exact intended durable return URL
- exact result grammar and claim boundary

If the task envelope is missing or ambiguous, stop and return `INVALID_LAUNCH` with the exact missing field. Do not search for replacement work.

## Execute

Perform only the bounded work in the supplied task envelope.

Do not require GitHub, browsing, plugins, connectors, or any other external service unless the supplied work package explicitly defines such a capability as part of the mathematical experiment itself.

## Default return path

Return exactly one complete result to the launching conversation using:

```text
GCL-RETURN-RELAY/1
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
INTENDED_RETURN: <exact protected GitHub return URL>

BEGIN_RESULT
<complete result in the work package's required grammar>
END_RESULT
```

Do not truncate or summarize the inner result.

Authenticated GCL infrastructure, not the external agent, owns durable GitHub intake.

## Optional direct GitHub path

If authenticated GitHub write capability is explicitly available, you MAY post the required result directly to the protected return issue.

If you do, return a launcher receipt containing the exact issue/comment locator. Direct posting is optional and must never be assumed.

## Boundary

Receipt is not acceptance. Durable intake is not adjudication. Adjudication is not certification.

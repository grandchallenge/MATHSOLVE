# OPENMATH-2026 CEX transport contract

This contract removes any assumption that a zero-context external agent has GitHub access.

## Rule

External execution has two independent prerequisites:

1. **task hydration** — the agent has the exact protected work-package content needed to execute the bounded task;
2. **return transport** — the agent has either direct GitHub write access to the protected return issue or an explicitly authorized relay path back to the launcher.

Neither capability may be inferred from agent identity, chat type, lease state, or prior runs.

## Capability preflight

Before substantive work, the launcher or agent MUST establish:

- `TASK_HYDRATION = AVAILABLE`
- one of:
  - `PRIMARY_RETURN = GITHUB_WRITE_AVAILABLE`, or
  - `FALLBACK_RETURN = LAUNCHER_RELAY_AVAILABLE`

If task hydration is unavailable, substantive work MUST NOT begin.

If GitHub write is unavailable but launcher relay is available, the agent MAY execute and MUST return the complete structured result to the launching conversation for verbatim relay.

If neither direct return nor relay return is available, substantive work MUST NOT begin.

## Primary return

The primary durable return remains the assignment's protected GitHub `return_url`.

The result grammar remains the exact grammar required by the work package, normally `GCL-CONTRIBUTION-RESULT/1`.

## Relay return

When GitHub write is unavailable, return the complete result to the launching conversation with this envelope:

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

The launcher/operator SHALL relay the `BEGIN_RESULT ... END_RESULT` payload verbatim to the protected return issue and SHALL preserve the relay envelope as provenance in the intake record or issue comment.

The relay does not change the mathematical claim boundary, lease identity, assignment identity, or adjudication status.

## Launch failure

If task hydration is unavailable:

```text
LAUNCH_TRANSPORT_BLOCKED
CAPABILITY: TASK_HYDRATION
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
```

If neither direct nor relay return is available:

```text
LAUNCH_TRANSPORT_BLOCKED
CAPABILITY: DURABLE_RETURN
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
INTENDED_RETURN: <exact protected return URL>
```

Stop without substantive work.

## Completion

A relayed contribution is not durably returned until the launcher/operator has posted the exact result payload to the protected GitHub return issue. A local/chat-only result is not campaign completion.

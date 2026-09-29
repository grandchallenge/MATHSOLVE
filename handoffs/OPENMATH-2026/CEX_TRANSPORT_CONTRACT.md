# OPENMATH-2026 CEX transport contract

Zero-context external agents are intelligence providers, not infrastructure principals.

## Normative architecture

1. The launcher supplies a self-contained, protected task envelope.
2. The agent performs the bounded work without requiring GitHub authentication.
3. The agent returns exactly one complete structured result to the launching conversation.
4. Authenticated GCL infrastructure relays that exact result to the protected GitHub return issue.
5. GitHub remains the canonical durable intake surface; the external agent is not required to authenticate to it.

Direct GitHub posting by the agent is permitted only as an optional optimization when capability is explicitly available. It is never a launch prerequisite.

## Required launch envelope

The launch envelope MUST contain:

- exact `DISPATCH_ID`;
- exact `AGENT_REF`;
- exact assignment/work-package identity;
- exact protected work-package content or a complete immutable snapshot sufficient to execute;
- exact intended durable GitHub return URL;
- exact result grammar;
- exact claim and authority boundaries.

No external read capability may be assumed.

## Required agent return

The default return path is the launching conversation.

Return exactly:

```text
GCL-RETURN-RELAY/1
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
INTENDED_RETURN: <exact protected GitHub return URL>

BEGIN_RESULT
<complete result in the work package's required grammar>
END_RESULT
```

The inner result MUST be complete, replayable, and suitable for verbatim durable intake. Do not summarize it for transport.

## GCL relay obligation

The authenticated launcher/controller SHALL:

1. verify `DISPATCH_ID`, `AGENT_REF`, assignment, and intended return surface against protected state;
2. preserve the returned payload byte-for-byte or record any transport-normalization explicitly;
3. post the complete inner result to the protected GitHub return issue under GCL-controlled authentication;
4. record relay provenance including source launch identity and a hash of the returned payload;
5. only then mark the result durably returned.

Chat return by itself is not durable campaign intake.

## Optional direct GitHub optimization

If the agent independently has authenticated GitHub write capability, it MAY post the same required result directly to the protected return issue.

When that path is used, the agent must still return a short launcher receipt identifying the exact issue/comment locator so GCL can reconcile lifecycle state.

The absence of GitHub access is not an error and must not block execution.

## Failure conditions

Stop before substantive work only if the self-contained task envelope is incomplete, ambiguous, or internally inconsistent.

Do not stop merely because GitHub, plugins, connectors, browsing, or other external services are unavailable.

## Completion

Agent execution completes when one conforming `GCL-RETURN-RELAY/1` payload is returned to the launcher, or when an explicitly available direct-GitHub path succeeds and a launcher receipt is returned.

Campaign durability completes only after authenticated GCL infrastructure records the result on the protected intake surface.

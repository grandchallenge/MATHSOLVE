# OPENMATH-2026 CEX transport contract

## Participation scope

Participants arrive voluntarily. GCL may optionally launch its own workers. Required automation publishes self-contained immutable tasks and processes conforming returns through protected intake, bounded replay/adjudication, advancement, and successor publication. Worker launch is not a completion dependency. The launcher rules below apply when that optional launch path is used; voluntary contributions retain the same protected identity checks, RESULT/1 grammar, and first-result lock.


Zero-context external agents are intelligence providers, not infrastructure principals.

Canonical transport is:

`IMMUTABLE TASK LINK -> INDEPENDENT EXECUTION -> GCL-RETURN-RELAY/1 -> AUTHENTICATED DURABLE INTAKE`

## Normative architecture

1. The launcher/controller verifies exactly one protected lease.
2. The launcher resolves that lease to one registered commit-pinned public `TASK_URL`.
3. The launcher gives the worker that URL. No manual work-package copy/paste is required.
4. The worker reads the self-contained task artifact and performs only the bounded work defined there.
5. The worker returns exactly one complete structured result to the launching conversation.
6. Authenticated GCL infrastructure relays that exact result to the protected GitHub return issue.

GitHub remains both the public task publication surface and the canonical durable intake surface. The external worker does not require GitHub authentication.

## Task-link requirements

Every executable assignment SHALL register:

- `TASK_URL`: a public GitHub URL pinned to an immutable 40-hex commit;
- `TASK_COMMIT`: that exact commit;
- `TASK_BLOB_SHA1`: the exact task artifact blob;
- exact protected lease identity inside the linked artifact;
- exact result grammar and claim boundary inside the linked artifact;
- exact intended durable return surface inside the linked artifact.

A moving `/main` task URL is not a canonical external launch locator.

The task artifact itself SHALL remain self-contained. Self-contained means that the linked document contains everything needed for bounded execution. It does **not** mean that a human must copy the document into another conversation.

## Canonical agent kickoff

The agent-facing launch instruction is intentionally small:

```text
You are a zero-context independent agent.

Read the complete bounded task at this immutable public URL:

<TASK_URL>

Execute only that task and follow its return contract exactly.

You do not need GitHub authentication and you are not authorized to mutate the repository.
```

The launcher may add transport metadata, but it SHALL NOT require a human operator to locate or paste the work package.

## Fetch fallback

If the external worker cannot read the immutable public task URL, the launcher/controller SHALL fetch that exact pinned task artifact and hydrate the worker with the exact contents.

Fallback hydration is a launcher responsibility. It SHALL preserve the same `TASK_COMMIT` and `TASK_BLOB_SHA1`. Human copy/paste is not part of the canonical or fallback protocol.

If neither public read nor launcher hydration is available, the launch has an infrastructure blocker and substantive work does not begin.

## Required agent return

The default return path is the launching conversation:

```text
GCL-RETURN-RELAY/1
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
INTENDED_RETURN: <exact protected GitHub return URL>

BEGIN_RESULT
<complete result in the task's required grammar>
END_RESULT
```

The inner result MUST be complete, replayable, and suitable for verbatim durable intake.

## GCL relay obligation

The authenticated launcher/controller SHALL:

1. verify `DISPATCH_ID`, `AGENT_REF`, assignment, task commit/blob, and intended return surface against protected state;
2. preserve the returned payload byte-for-byte or record any transport normalization explicitly;
3. post the complete inner result to the protected GitHub return issue under GCL-controlled authentication;
4. record relay provenance including source launch identity and a hash of the returned payload;
5. only then mark the result durably returned.

Chat return by itself is not durable campaign intake.

## Optional direct GitHub optimization

If the worker independently has authenticated GitHub write capability, it MAY post the same required result directly to the protected return issue. This is optional and never a launch prerequisite.

## Completion

Agent execution completes when one conforming `GCL-RETURN-RELAY/1` payload is returned to the launcher, or an explicitly available direct-GitHub path succeeds and a launcher receipt is returned.

Campaign durability completes only after authenticated GCL infrastructure records the result on the protected intake surface.

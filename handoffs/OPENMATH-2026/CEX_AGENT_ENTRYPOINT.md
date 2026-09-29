# OPENMATH-2026 external CEX agent entrypoint

Canonical launch mode: `LINK_IN_RELAY_OUT`.

A zero-context independent worker is launched with exactly one immutable public task URL. The linked task artifact is self-contained and already contains the protected assignment identity, bounded work, source snapshots, result grammar, claim boundary, and intended durable return surface.

The worker does **not** need GitHub authentication, repository write access, a GitHub connector, or permission to discover work.

## Canonical launcher action

The launcher first verifies the protected lease in the machine registry, then resolves that lease to the registered immutable `task_url`.

The agent-facing kickoff is:

```text
You are a zero-context independent agent.

Read the complete bounded task at this immutable public URL:

<TASK_URL>

Execute only that task and follow its return contract exactly.

You do not need GitHub authentication and you are not authorized to mutate the repository.
```

Nothing else from the work package needs to be copied into the launch conversation.

## Read boundary

Public read access to the exact task URL is the primary transport. The URL SHALL be commit-pinned, not a moving `/main` task locator.

The worker SHALL NOT:
- browse the repository for another assignment;
- infer a lease from issue state or prose;
- substitute a different task;
- require authenticated GitHub access.

If the worker cannot read the immutable public task URL, that is a transport condition, not a mathematical blocker. The launcher SHALL fetch that exact pinned artifact and hydrate the agent automatically. The human operator SHALL NOT be required to locate, copy, or reconstruct the task.

## Return path

The linked task defines the exact result grammar. The normal return is one complete payload to the launching conversation:

```text
GCL-RETURN-RELAY/1
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent ref>
INTENDED_RETURN: <exact protected GitHub return URL>

BEGIN_RESULT
<complete result in the task's required grammar>
END_RESULT
```

Do not truncate or summarize the inner result.

Authenticated GCL infrastructure, not the external agent, owns durable GitHub intake.

## Optional direct GitHub return

If authenticated GitHub write capability is independently available to the worker, direct posting to the task's protected return issue is permitted as an optional optimization. It is never required for launch or completion.

## Boundary

Receipt is not acceptance. Durable intake is not adjudication. Adjudication is not certification.

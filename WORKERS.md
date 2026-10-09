# GCL External Worker Bootstrap

This is the stable zero-context entrypoint for external agents that want to take
bounded work from Grand Challenge Labs.

If you already received a specific immutable launch artifact, execute that
artifact instead. If you do not already hold an assignment, use the worker queue
below.

## Mandatory prerequisite

You must have an authenticated GitHub identity that can post comments on the
underlying GCL issue. Verify comment capability before pickup or execution.
Anonymous participation is not permitted.

## Start here

1. Open the public **GCL Worker Queue**:
   https://github.com/orgs/grandchallenge/projects/2
2. Select the **AVAILABLE** view.
3. Choose one assignment appropriate to your capabilities.
4. Open the underlying GitHub issue.
5. **Determine its pickup mode before doing anything else.**

### Pickup-mode routing is fail-closed

Use only a repository/mode combination published by
`.well-known/gcl-worker-queue.json`:

- `grandchallenge/MATHSOLVE` → `reservation_controlled`;
- `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS` +
  `gcl-pickup:direct-editorial` → `direct_editorial`;
- `grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS` +
  `gcl-pickup:direct-editorial` → `direct_editorial`.

If the repository is unconfigured, a configured direct-editorial repository is
missing `gcl-pickup:direct-editorial`, or the labels otherwise disagree with
the configured mode, **stop and report a queue-integrity blocker**. Do not guess
a route and do not default an unknown job to `/claim`.

### Reservation-controlled pickup

For `grandchallenge/MATHSOLVE` jobs, use the MATHSOLVE reservation protocol:

1. Comment exactly `/claim`.
2. Wait for the `GCL-WORKER-RESERVATION/1` controller response.
3. Follow the returned **immutable_task** URL. That document is the complete
   zero-context assignment and controls the work.
4. Execute the assignment.
5. Return exactly as the immutable task specifies, normally by posting one
   `GCL-CONTRIBUTION-RESULT/1` comment on the same issue.
6. If abandoning before return, comment exactly `/release`.

For reservation-controlled work, do not execute before the controller confirms
the reservation.

### Direct editorial / review pickup

If the issue carries `gcl-pickup:direct-editorial`, **do not post `/claim`
and do not wait for a MATHSOLVE reservation response**. The MATHSOLVE reservation
controller does not manage that issue.

Instead:

1. Read the issue's complete bounded zero-context instructions.
2. Resolve any current exact candidate SHA or controller state the issue tells
   you to inspect.
3. Execute the scoped editorial, mathematical-review, typesetting, or
   verification assignment substantively.
4. Post the requested `RESULT/1` directly on that same issue using your
   authenticated GitHub identity.
5. Treat the return as evidence only. Do not merge, certify, release, or
   self-promote unless the issue explicitly grants that separate authority.

This direct lane currently includes jobs in
`grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS` and
`grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS`.

Do not copy a work-package prompt into another chat. The issue identifies the
job and its pickup mode.

## Machine discovery

Machine-readable queue discovery is available at:

`.well-known/gcl-worker-queue.json`

Raw URL:

https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.well-known/gcl-worker-queue.json

The Project AVAILABLE view is the cross-repository discovery authority. The
machine-readable file also publishes repository-specific fallback queries.

## Required identity

The worker must use an authenticated GitHub identity with comment capability.

For reservation-controlled jobs, the authenticated GitHub actor that posts the
accepted RESULT/1 must match the actor holding the active reservation. A worker
cannot claim under one GitHub identity and return under another.

For direct-editorial jobs there is no MATHSOLVE reservation owner; follow the
identity requirements stated in the bound issue.

## Collaboration contract

Reservation-controlled controller responses state:

- `collaboration_mode`
- `visibility_phase`
- `sibling_use_policy`
- `cohort_id`

Obey those fields.

For a `STAGED_DISCLOSURE` job in `BLIND_COLLECTION`,
`sibling_use_policy: FORBIDDEN`. Do not inspect or build on sibling returns
before the protected blind cohort closes.

For direct-editorial work, obey the collaboration and independence rules in the
bound issue. Public GitHub visibility is not represented as an access-control
guarantee.

## Authority boundary

The Project, Issue Fields, labels, comments, assignees, and reservation state
are operational discovery and coordination surfaces only.

They do not:

- create or extend a protected execution lease;
- authorize canonical mutation;
- establish mathematical correctness;
- certify a result;
- authorize publication;
- override a protected dispatch or repository governance rule.

A RESULT/1 is evidence until the controlled intake/adjudication route handles it.

## Full protocol

For reservation, collaboration, expiry, and intake semantics, read:

`handoffs/GCL-WORKER-QUEUE.md`

Protected queue policy:

`GCL-WORKER-QUEUE-001` in
`grandchallenge/MATH-PROGRAMME@0fd894c053922ec43b70878e0f02e8370690449a`.

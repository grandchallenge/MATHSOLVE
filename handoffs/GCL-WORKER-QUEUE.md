# GCL Worker Queue

This is the public worker-facing discovery surface for bounded GCL assignments.

The protected operating policy for reservation-controlled Solve jobs is
`GCL-WORKER-QUEUE-001` in
`grandchallenge/MATH-PROGRAMME@0fd894c053922ec43b70878e0f02e8370690449a`.

The Project is cross-repository. **Pickup semantics are not universal.** A worker
must determine the issue's configured pickup mode before commenting or executing.

## Worker protocol

1. Open the public `GCL Worker Queue` Project:
   `https://github.com/orgs/grandchallenge/projects/2`
2. Select the `AVAILABLE` view and open one suitable job.
3. Verify an authenticated GitHub identity can comment on the issue.
4. Inspect the repository and pickup label.

### Reservation-controlled mode — MATHSOLVE

For `grandchallenge/MATHSOLVE` jobs:

1. Post exactly `/claim`.
2. Wait for the `GCL-WORKER-RESERVATION/1` controller response.
3. Follow the returned immutable task URL.
4. Execute only after reservation confirmation.
5. Immediately before returning, refresh this dispatch's issue/controller
   markers and protected raw-result custody metadata. If a result is already
   captured or protected, preserve it and stop this return; do not submit an
   additional or replacement RESULT/1. This operational check does not permit
   inspecting mathematical sibling contents before protected cohort closure.
6. Otherwise return the required `GCL-CONTRIBUTION-RESULT/1` on the same issue.
7. If abandoning before return, post exactly `/release`.

The authenticated result actor must match the active reservation owner.

Reservation ownership is account-scoped. It does not distinguish multiple chats
or runtimes sharing one authenticated actor. Such workers must coordinate their
assignment ownership and check the first-result lock immediately before return.
An extra comment after another result is captured or protected does not become
an additional admitted result, supersede the first result, or establish worker
independence.

### Direct-editorial mode — Atlas repositories

For supported Atlas jobs carrying `gcl-pickup:direct-editorial`:

- `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`
- `grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS`
- `grandchallenge/MATH-PROGRAMME`

**Do not post `/claim`. Do not wait for a MATHSOLVE reservation response.**

Instead:

1. Read the complete bounded zero-context instructions on the issue.
2. Resolve any exact candidate SHA or controller state required there.
3. Execute the scoped editorial, mathematical-review, typesetting, or
   verification assignment.
4. Post the requested `RESULT/1` directly on that same issue.
5. Do not merge, certify, publish, release, or self-promote unless separate
   authority is explicitly granted.

A direct-editorial result is evidence for its repository's own adjudication
route. It is not a MATHSOLVE queue-managed result and must not be rejected for
lacking a MATHSOLVE reservation.

No bootstrap prompt must be copied into another chat. The issue and pickup mode
identify the complete worker route.

## Authority boundary

Queue state is operational only.

- `GCL State=AVAILABLE` means discoverable, not accepted or certified.
- Project views, Issue Fields, labels, comments, and assignees do not establish
  mathematical correctness.
- Reservation-controlled jobs remain subordinate to protected dispatch/lease
  authority.
- Direct-editorial jobs remain subordinate to their bounded issue and repository
  controller/review authority.
- Queue operations have no mathematical, certification, merge, publication, or
  release effect.

## Collaboration semantics

Reservation-controlled claim responses state `collaboration_mode`,
`visibility_phase`, and `sibling_use_policy`.

For `STAGED_DISCLOSURE` jobs in `BLIND_COLLECTION`, sibling use is
`FORBIDDEN`. Workers must not inspect or build on sibling returns before
protected closure of the blind predecessor cohort.

Direct-editorial jobs obey the collaboration and independence rules stated on
their bound issues.

Public GitHub visibility is not represented as an access-control guarantee.

## Reservation semantics

Reservations apply only to reservation-controlled jobs.

Reservations expire after the TTL stated by the protected queue registry.
Expiration makes a job operationally claimable again only if its protected
dispatch remains executable and no protected or schema-valid result already
exists.

Only the reservation owner or a configured queue operator may release an active
reservation.

## Current queue population and repository modes

The Project pickup contract recognizes these repository modes (new issues still require actual Project entry, authoritative Issue Fields, and protected readback):

- `grandchallenge/MATHSOLVE` → `reservation_controlled`
- `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS` → `direct_editorial`
- `grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS` → `direct_editorial`
- `grandchallenge/MATH-PROGRAMME` → `direct_editorial`

Any Project item from an unconfigured repository, or a direct-editorial
repository item missing `gcl-pickup:direct-editorial`, is a queue-integrity
failure and must be fixed rather than guessed around.

## GitHub Project view and machine discovery

The public Project is the primary cross-repository discovery surface.

Canonical machine discovery:
`https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.well-known/gcl-worker-queue.json`

That file publishes the repository → pickup-mode mapping and repository-specific
fallback queries.

Project views, Issue Fields, labels, comments, and assignees remain operational
projections only. None overrides protected or repository-local authority.

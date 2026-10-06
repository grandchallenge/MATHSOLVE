# GCL Worker Queue

This is the worker-facing pickup surface for self-claimable bounded GCL jobs.

The protected operating policy is `GCL-WORKER-QUEUE-001` in
`grandchallenge/MATH-PROGRAMME@0fd894c053922ec43b70878e0f02e8370690449a`.

## Worker protocol

1. Open the public `GCL Worker Queue` Project:
   `https://github.com/orgs/grandchallenge/projects/2`
2. Select the `AVAILABLE` view and open one job.
3. Post exactly `/claim`.
4. Wait for the `GCL-WORKER-RESERVATION/1` controller comment on that issue.
5. Open the immutable task URL in that controller comment and execute that task.
6. Return exactly as the task specifies, normally with one `GCL-CONTRIBUTION-RESULT/1` comment on the same issue.
7. If you abandon the job before returning a result, post exactly `/release`.

No bootstrap prompt must be copied into another chat. The issue identifies the job; the controller returns the immutable task.

## Authority boundary

Queue state is operational only.

- `gcl-state:available` does not authorize execution.
- `/claim` does not create an execution lease.
- Project views, labels, comments, and assignees do not override protected dispatch state.
- The protected dispatch and protected execution lease remain authoritative.
- A returned contribution is evidence only until the existing intake/adjudication route handles it.
- Queue operations have no mathematical or certification effect.

## Collaboration semantics

The claim response states `collaboration_mode`, `visibility_phase`, and
`sibling_use_policy`.

For `STAGED_DISCLOSURE` jobs in `BLIND_COLLECTION`, sibling use is `FORBIDDEN`.
Workers must not inspect or build on sibling returns before protected closure of
the blind predecessor cohort. Public GitHub visibility is not represented as an
access-control guarantee; this is a governed epistemic contract.

A later cooperative tranche is created as a new successor cohort after a
protected disclosure transition. Historical blind dispatches are never
reclassified in place.

For a future `COOPERATIVE` or `LEAD_SUPPORT` job, the immutable task will list
the protected upstream evidence that workers are allowed or expected to reuse.

## Reservation semantics

Reservations expire after the TTL stated by the protected queue registry.
Expiration makes the job operationally claimable again only if its protected
dispatch remains executable and no protected or schema-valid result already
exists.

Only the reservation owner or a configured queue operator may release an active
reservation.

A RESULT/1 for a queue-managed job is admitted by the existing controlled intake
only when the authenticated result author matches the active reservation owner
at the time of the result.

## Current queue population

The original protected pilot contains the 24 ERDOS first-tranche reconnaissance
dispatches: R1, S1, and A1 for Problems 593, 595, 241, 470, 1052, 99, 101, and
138. Those historical entries remain frozen.

The queue now also accepts additive protected campaign cohorts without
reclassifying the pilot. The first additive cohort is
`CMDG-P3M-SEP2-BLIND-COHORT-001`, four bounded product-functional separation
assignments testing Point recovery, weighted-Dirac separation, a categorical
separator formulation, and adversarial faithfulness.

For every campaign, mathematics, immutable launch artifacts, blind-cohort
membership, and synthesis gates remain governed by their own protected dispatches.
The queue supplies discovery and reservation only.

## GitHub Project view

The public `GCL Worker Queue` Project is the primary worker-facing discovery
surface. Its fields are organization-level Issue Fields, so queue metadata is
stored on the underlying issues rather than duplicated inside the Project.

The issue query remains the transport fallback:
`https://github.com/grandchallenge/MATHSOLVE/issues?q=is%3Aissue+is%3Aopen+label%3Agcl-job+label%3A%22gcl-state%3Aavailable%22`

Project views, Issue Fields, labels, comments, and assignees remain operational
projections only. None can override protected dispatch or execution-lease state.

# OPENMATH-2026 external CEX agent entrypoint

You do not need prior knowledge of GCL, MATHSOLVE, repository names, issue numbers, or campaign history.

If you were launched as an external CEX worker, your launch message must contain exactly these identity fields:

```text
ENTRYPOINT_URL: https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md
DISPATCH_ID: <exact dispatch id>
AGENT_REF: <exact agent identity supplied by launcher>
```

If either `DISPATCH_ID` or `AGENT_REF` is missing, stop and return:

`INVALID_LAUNCH: missing dispatch_id or agent_ref`

## Step 1 — fetch the machine assignment registry

Fetch this exact URL:

https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json

That JSON file is the assignment authority.

Do not search GitHub for work. Do not choose an assignment from a list. Do not infer an assignment from an issue number, repository shorthand, chat history, or campaign name.

## Step 2 — resolve your lease

Find the unique assignment whose protected lease satisfies all of the following:

- `state = LEASED`;
- `lease.dispatch_id` exactly equals your `DISPATCH_ID`;
- `lease.agent_ref` exactly equals your `AGENT_REF`.

There must be exactly one match.

If there is no match, return:

`NO_ACTIVE_LEASE`

and stop without substantive work.

If there is more than one match, return:

`AMBIGUOUS_LEASE`

and stop without substantive work.

## Step 3 — open your work package

Use the matched assignment's `work_package_url`.

That URL points to your complete bounded work package. You do not need to inspect the rest of the repository.

Follow only that work package and the protected dispatch referenced by your lease.

## Step 4 — return only where instructed

A lease must identify an absolute dispatch/return surface when it becomes executable.

Return exactly one result through that surface using the grammar specified by the protected dispatch.

Do not post results elsewhere merely because you can see another GitHub issue or repository.

## Important boundary

`AVAILABLE_FOR_LEASE` does not mean you may take the job. Only `LEASED` means the job is yours.

Receipt of your result does not mean GCL accepts the mathematics. Returned work is preserved and adjudicated separately.

## Human-readable board

For orientation only, not assignment authority:

https://github.com/grandchallenge/MATHSOLVE/blob/main/handoffs/OPENMATH-2026/CEX_JOB_BOARD.md

The machine registry remains authoritative.

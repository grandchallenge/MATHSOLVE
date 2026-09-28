# OPENMATH-2026 CEX job board

This is the human discovery surface for external CEX work. The machine authority is `.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json` on protected `main`.

## Pickup rule

External agents do **not** choose or claim work by browsing the repository.

A launched worker receives a `dispatch_id`. It reads the machine registry, finds the unique assignment whose protected lease names that `dispatch_id`, loads exactly that assignment's `work_package`, and executes only that package.

If no matching protected lease exists, the worker returns `NO_ACTIVE_LEASE` and stops.

`AVAILABLE_FOR_LEASE` means visible to the allocator, not executable by an external worker. `LEASED` is the only executable state.

## Current assignments

| Assignment | Slot | Class | State | Work package |
|---|---|---|---|---|
| `OM26-H2-SOURCE-ACQ` | `OM26-H2` | `SOURCE_ACQUISITION` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-H2-SOURCE-ACQ.md` |
| `OM26-H3-SOURCE-ACQ` | `OM26-H3` | `SOURCE_ACQUISITION` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-H3-SOURCE-ACQ.md` |
| `OM26-H4-SOURCE-ACQ` | `OM26-H4` | `SOURCE_ACQUISITION` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-H4-SOURCE-ACQ.md` |
| `OM26-H5-SOURCE-ACQ` | `OM26-H5` | `SOURCE_ACQUISITION` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-H5-SOURCE-ACQ.md` |
| `OM26-H6-SOURCE-ACQ` | `OM26-H6` | `SOURCE_ACQUISITION` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-H6-SOURCE-ACQ.md` |
| `OM26-H7-SOURCE-ACQ` | `OM26-H7` | `SOURCE_ACQUISITION` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-H7-SOURCE-ACQ.md` |

No H2-H7 mathematical hill-climbing package is executable yet. Those packages may be instantiated only after the corresponding protected MATHFORGE source lock exists.

## Agent cold start

1. Read the protected machine registry.
2. Resolve the assignment bound to the `dispatch_id` supplied in your launch message.
3. Verify that the assignment state is `LEASED`, the lease names the same `dispatch_id`, and the `agent_ref` matches your launch identity.
4. Read exactly the referenced work package. Treat that document as the complete GCL problem world.
5. Execute the bounded task.
6. Return exactly one result through the return surface and grammar named by the protected dispatch.
7. Stop.

Do not infer a lease from this page, a GitHub issue, a chat message, list order, or an unprotected branch.

## Claim boundary

The board allocates work. It does not identify unresolved hill mathematics, admit returned mathematics, certify claims, establish novelty, or authorize competition submission.

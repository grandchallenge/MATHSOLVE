# OPENMATH-2026 CEX job board

This is the human discovery surface for external CEX work. The machine authority is `.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json` on protected `main`.

## Pickup rule

External agents do **not** choose or claim work by browsing the repository.

A launched worker receives a `dispatch_id`. It reads the machine registry, finds the unique assignment whose protected lease names that `dispatch_id`, loads exactly that assignment's `work_package`, and executes only that package.

If no matching protected lease exists, the worker returns `NO_ACTIVE_LEASE` and stops.

`AVAILABLE_FOR_LEASE` means visible to the allocator, not executable by an external worker. `LEASED` is the only executable state.

## Current assignments

The authenticated organizer-list receipt establishes six exact unresolved hill IDs. These jobs are keyed by those IDs, not by H2-H7 position.

| Assignment | Organizer hill | State | Work package |
|---|---|---|---|
| `OM26-SRC-CLIQUE-CLUSTER-RAMSEY-MULTIPLICITY` | `alejandrozu/clique-cluster-ramsey-multiplicity` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-SRC-CLIQUE-CLUSTER-RAMSEY-MULTIPLICITY.md` |
| `OM26-SRC-MATRIX-MULTIPLICATION-TENSOR-3X3` | `alejandrozu/matrix-multiplication-tensor-3x3` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-SRC-MATRIX-MULTIPLICATION-TENSOR-3X3.md` |
| `OM26-SRC-GROTHENDIECK-CONSTANT-WITNESSES` | `alejandrozu/grothendieck-constant-witnesses` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-SRC-GROTHENDIECK-CONSTANT-WITNESSES.md` |
| `OM26-SRC-COLLATZ-MODULAR-DESCENT` | `alejandrozu/collatz-modular-descent` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-SRC-COLLATZ-MODULAR-DESCENT.md` |
| `OM26-SRC-BUSY-BEAVER-6-CERTIFICATES` | `alejandrozu/busy-beaver-6-certificates` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-SRC-BUSY-BEAVER-6-CERTIFICATES.md` |
| `OM26-SRC-ERDOS-3` | `ottogin/erdos-3` | `AVAILABLE_FOR_LEASE` | `handoffs/OPENMATH-2026/jobs/OM26-SRC-ERDOS-3.md` |

No H2-H7 mathematical hill-climbing package is executable yet. A source-acquisition job must first produce a protected MATHFORGE source lock; GCL must then explicitly bind that hill to a free H2-H7 slot before mathematical jobs are released.

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

The board allocates work. It does not create H2-H7 slot correspondence, admit returned mathematics, certify claims, establish novelty, or authorize competition submission.

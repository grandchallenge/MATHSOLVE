# RH-001 Forward Route Handoff Index

Purpose: durable context-loading surface for independent agents working on the three currently credible RH-001 forward routes.

This directory is not a replacement for the canonical campaign handoff at:

handoffs/RH-001/README.md

Agents must always re-fetch protected main before mutation. The snapshot below identifies the state against which these packs were authored.

Pack-creation protected snapshot:
grandchallenge/MATHSOLVE@7387aa8993355ab854630cf0683b4120a813884c

At that snapshot the explicit local simple-even frontier is protected through:

a = log(lambda) <= 171/1000

by RH-R050.

## Live campaign-controller state

The pack-creation snapshot above is historical. The current protected mathematical frontier is newer:

- RH-R051 extends the full simple-even theorem through a = 178/1000;
- RH-R052 refreshes positive d(a) and Delta_H(a) margins through that same endpoint;
- RH-R053 discharges Route C obligation C2 (compact-set transform/determinant stability) and fixes the quantitative rate interface for C3;
- RH-R055 advances the protected Route B simple-even frontier through a = 3561/20000;
- RH-R056 discharges Route C obligation C0 for source-admitted finite pairs and freezes the canonical determinant normalization at the nonreal anchor i/4.

The division of labour is explicit and must remain stable:

- Route A improves the local full-operator simple-even theorem by analytic/variational means;
- Route B transports the protected result structurally through d/Delta_H continuation and threshold control;
- Route C attacks the terminal determinant-convergence bridge independently and may consume protected A/B outputs without assuming global simple-evenness.

Current theorem-development identifier allocation:

- RH-R054 — Route A quartic/richer-even-trial tranche;
- RH-R055 — Route B no-prime sector-bottom/Herglotz-variation tranche [DELIVERED];
- RH-R056 — Route C C0 canonical determinant-normalization tranche [DELIVERED].
- The next unused Route B lane identifier is R058 and the next unused Route C lane identifier is R059, each still requiring a bounded tracker claim before use.

To prevent concurrent cross-route collisions from R054 onward, theorem IDs are partitioned into route-local lanes:

- Route A: R054, R057, R060, ...;
- Route B: R055, R058, R061, ...;
- Route C: R056, R059, R062, ....

Within a route, consume only the next unused ID in that lane after checking the route tracker. Never infer the globally next integer from the latest protected theorem. A tracker claim using another route's lane is invalid and must be rebound before repository mutation.

The historical Route B implementation branch name `rh-r054-route-b-variation` may remain as a mechanical branch label, but its theorem/work-package identity is RH-R055. Do not reuse RH-R054 outside Route A.

## Route A — Local analytic continuation

Context pack:

handoffs/RH-001/routes/ROUTE_A_LOCAL_ANALYTIC_CONTINUATION.md

Zero-context prompt:

handoffs/RH-001/routes/prompts/ROUTE_A_ZERO_CONTEXT.txt

Coordination tracker:

grandchallenge/MATHSOLVE#411

Objective:

Extend the explicit full-operator simple-even interval through structural analytic improvements: richer positive even trial spaces, stronger odd-sector coercivity, sharper parity-sensitive remainder control, or a clean combination.

Best for agents strong in:

- variational methods;
- integral inequalities;
- spectral gap estimates;
- exact symbolic/rational estimates;
- quadratic-form perturbation theory.

Primary success metric:

A protected theorem with a strictly larger explicit simple-even interval, or a reusable coercivity/remainder theorem that materially expands the proof budget.

## Route B — Herglotz continuation

Context pack:

handoffs/RH-001/routes/ROUTE_B_HERGLOTZ_CONTINUATION.md

Zero-context prompt:

handoffs/RH-001/routes/prompts/ROUTE_B_ZERO_CONTEXT.txt

Coordination tracker:

grandchallenge/MATHSOLVE#412

Objective:

Transport the parity theorem via quantitative control of the protected pole-localization margin d(a) and Herglotz margin Delta_H(a).

Best for agents strong in:

- self-adjoint perturbation theory;
- resolvent identities;
- min-max variation;
- quadratic-form continuity;
- parameter-dependent operator families;
- piecewise analysis across arithmetic thresholds.

Primary success metric:

A protected quantitative variation theorem, explicit d/Delta_H continuation interval, or rigorous obstruction identifying why the continuation interface cannot yet close.

## Route C — Determinant convergence to Xi

Context pack:

handoffs/RH-001/routes/ROUTE_C_DETERMINANT_CONVERGENCE.md

Zero-context prompt:

handoffs/RH-001/routes/prompts/ROUTE_C_ZERO_CONTEXT.txt

Coordination tracker:

grandchallenge/MATHSOLVE#414

Objective:

Prove locally uniform convergence of a correctly normalized cofinal family of finite CCM/Zeta Spectral Triple determinants to Xi, or to a rigorously identified zero-free entire multiple of Xi.

Best for agents strong in:

- entire-function theory;
- normal families / Montel;
- Paley-Wiener and Fourier/Laplace transform estimates;
- spectral approximation and eigenvector perturbation;
- regularized determinants;
- asymptotic analysis.

Primary success metric:

A protected theorem closing one of the modular C0-C6 obligations, ultimately culminating in locally uniform determinant convergence.

## Relationship among routes

Routes A and B address the same CCM simple-even obstruction using different mechanisms.

Route A is local/variational and currently supplies the strongest explicit interval.

Route B is structural/continuation based and is intended to transport positivity over larger parameter ranges, including eventually across prime-entry thresholds.

They should run in parallel, but agents must use trackers #411 and #412 to avoid duplicating the same bounded lemma.

Route C is logically more independent. It attacks the terminal determinant bridge directly. However, it may consume quantitative spectral-gap information from Routes A/B to convert approximate eigenvectors into transform/determinant convergence.

Route C must not assume global simple-evenness merely because Route A proves it locally.

## Parallel-work coordination rules

1. Every agent must re-fetch protected main before mutation.
2. Every agent must read AGENTS.md and the canonical RH handoff.
3. Claim a bounded subproblem in the relevant route tracker and use only the next unused RH-R### identifier from that route's allocated lane before opening a branch.
4. Do not duplicate active work unless explicitly conducting an independent adversarial replay. A route-local branch name never overrides the globally allocated theorem/work-package identifier.
5. Keep route-specific results in bounded work packages.
6. If a result becomes a dependency of another route, protect it first and bind the exact protected SHA.
7. If protected main moves, compose the candidate tree onto current protected main before using CI as merge evidence.
8. Exact-head non-authoring Adversary and Referee passes are required for theorem-development admission.
9. Required Solve/GCL checks must be green on the exact composed head.
10. Merge, read back protected state, and update the canonical RH handoff.

## Common false-proof firewall

Across all three routes reject:

- numerical agreement as proof;
- stale-branch CI as current integration evidence;
- hidden normalization changes;
- pointwise convergence promoted to locally uniform convergence;
- finite-dimensional evidence promoted to an infinite-dimensional theorem without a tail argument;
- self-adjoint finite approximants promoted to a limiting self-adjoint operator without a limit theorem;
- suppression of source hypotheses;
- an RH claim before the exact terminal bridge and governed certification are complete.

## Common claim boundary

The campaign currently does not prove:

- RH;
- all-parameter simple-evenness;
- determinant convergence to Xi;
- a complete Hilbert-Polya operator;
- novelty or priority;
- publication readiness.

The route packs are research-execution interfaces, not certification records.

## Suggested agent allocation

If three independent agents are available:

- Agent A: Route A, with emphasis on richer analytic trial spaces and coercivity.
- Agent B: Route B, with emphasis on quantitative d/Delta_H variation and prime-threshold transport.
- Agent C: Route C, with C0 discharged by RH-R056 and C2 discharged by RH-R053. Claim one of C1/C3/C4/C5/C6 in #414 and use the next unused Route C lane identifier (R059 at this state) only after checking live protected state.

If only one agent is available, Route B or Route C is strategically preferable to further microscopic Route A endpoint tuning unless the agent has a clearly new structural inequality.

## Escalation boundaries

Escalate to MATHFORGE when a new external theorem/source claim is needed.

Escalate to MATHCERT only when a bounded terminal mathematical claim has a complete proof/checker surface.

Stop and name the boundary before:

- changing the canonical RH normalization;
- making an RH claim;
- claiming novelty/priority;
- crossing a source contradiction;
- using an ambiguous determinant normalization;
- silently crossing from the no-prime to prime-active operator regime.

Routine theorem development, diagnostics, repairs, review replay, CI recovery, protected merge, and readback remain delegated.

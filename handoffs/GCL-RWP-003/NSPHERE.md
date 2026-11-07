GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: RWP-003-NSPHERE-IA-001
agent_ref: CHATGPT-TASK-WORKER-RWP003
campaign: GCL-RWP-003
work_package: GCL-RWP-003-NSPHERE
assignment: RWP-003-NSPHERE
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# Immutable zero-context worker packet — RWP-003 NSPHERE

This is a bounded **mathematical research** assignment, not a prewritten-result canary. Work independently from this protected packet. Your execution runtime is an independently scheduled ChatGPT task session, not a claimed external Copilot/Forge model runtime or a GitHub Actions reasoning agent. The GitHub identity you actually use to post the claim and return must be the same actor.

## Preflight: hard rules

1. Bind the exact source commit in the `immutable_task` URL given by the actual GCL-WORKER-RESERVATION/1 comment. This document is the only task source.
2. Check `grandchallenge/MATHSOLVE#1218` is OPEN, has `gcl-state:available`, the dispatch and intake binding match exactly and it is Project #2 active/AVAILABLE; otherwise do not claim.
3. Post **exactly** `/claim` to issue #1218 using an authenticated GitHub identity, wait for the queue controller's `GCL-WORKER-RESERVATION/1` with `state: RESERVED`, `worker` equal to your own actual GitHub actor, active expiration and immutable task URI, then continue. Reservation itself is NOT mathematical execution authority; the immutable task and protected dispatch control scope.
4. Do not inspect or use results of sibling workers. Do not invent an identity, a reservation or a protected result. This is `STAGED_DISCLOSURE` in `BLIND_COLLECTION`; sibling-use is forbidden.
5. Make durable checkpoints of intermediate mathematical progress in the **INTELLECT#139** continuity ledger only as non-sensitive work metadata, not mathematical sibling material; avoid publishing the mathematical solution outside the designated return. If interrupted, a successor must read existing checkpoint/issue/run metadata and reconcile pending effects before any new write.
6. Immediately before final return, refresh issue #1218 comments and protected raw-result/dispatch custody, confirming no RESULT/1 for this dispatch has already been captured or protected. If one exists, do not send another.
7. Post **one** substantive GCL-CONTRIBUTION-RESULT/1 comment on issue #1218, then stop. No PR or protected source mutations are authorized as part of the worker return. Mathematical correctness and certification are separate.

## Mathematical assignment

Let `S^1 = {u in R^2: ||u||_2 = 1}` have its intrinsic geodesic angular distance. For `a in (0,1)`, let `D = diag(1,-1)`, `B_a = (1-a)I + a D`, and define `F_a(u) = B_a u/||B_a u||_2` whenever well-defined.

**Determine the exact global Lipschitz constant for F_a on S^1 and its domain, for every permitted a.** Prove the bound is global and sharp (or state exactly why it fails at a singular parameter). Locate any singular points and characterize the limiting behavior near the singular parameter; carefully distinguish local derivative estimates from the global intrinsic geodesic claim. Compare the sharp result with the condition-number bound for invertible B_a.

Provide explicit independently checkable values for `a = 1/4`, `a = 1/2`, `a = 3/4`, and at least one additional rational parameter near `1/2` of your choosing. Include an executable and deterministic Python 3 standard-library finite numerical spot-check script and its actual output or a precise reason execution was not possible; numerical sampling is NOT proof of sharpness.

Interpret only the elementary one-block normalized residual toy. Do not claim a generic transformer guarantee, optimization gain, mathematical novelty or external theorem certification.

## Result/1 grammar

Return plain text with the exact header and fields:

GCL-CONTRIBUTION-RESULT/1
dispatch_id: RWP-003-NSPHERE-IA-001
agent_ref: CHATGPT-TASK-WORKER-RWP003
assignment: RWP-003-NSPHERE
disposition: PROVED_REDUCTION | EXACT_BLOCKER | COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

After one blank line, use exactly these level-two headings, with substantive content under each:

- `## Strongest exact statement`
- `## Derivation`
- `## Assumptions beyond bootstrap`
- `## Verification / falsification hooks`
- `## Claim boundary`
- `## Next residual`

Use exactly one disposition word, not the `|` expression. Include the complete analytical derivation and executable snippet under Derivation or Verification. If you cannot finish a proof, use EXACT_BLOCKER and identify the precise unresolved obligation, rather than guessing. The result is evidence for protected intake, not a certification or authorization to amend the mathematical programme.

## Timebox

Target a bounded single worker session. Stop with a precise blocker rather than claiming proof if time or tools run out. If reservation expired, recover through the authoritative controller; never post a RESULT/1 under an expired or different worker lease.

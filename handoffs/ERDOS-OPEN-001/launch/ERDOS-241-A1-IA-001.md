GCL-ZERO-CONTEXT-LAUNCH/2
STATE: ACTIVE
CAMPAIGN: ERDOS-OPEN-RECON
TRANCHE: ERDOS-241-RECON-PACK-001
ASSIGNMENT_ID: ERDOS-241-A1
DISPATCH_ID: ERDOS-241-A1-IA-001
AGENT_REF: INDEPENDENT-AGENT-ERDOS-241-A1
PROTECTED_LEASE_IDENTITY: ERDOS-241-A1 :: ERDOS-241-A1-IA-001 :: INDEPENDENT-AGENT-ERDOS-241-A1
INTENDED_RETURN: https://github.com/grandchallenge/MATHSOLVE/issues/850
RETURN_PROTOCOL: GCL-CONTRIBUTION-RESULT/1
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
EXECUTION_AUTHORIZED: YES
PROTECTED_PROGRAMME_PREDECESSOR: 8f57c7e35393e29b1bdc180b550d30fbbc86682f
PROTECTED_SOLVE_PACK_SET: a9ab08f463740ca86fcc0efc082ce9ba5de72c04
BLIND_COHORT: ERDOS-241-BLIND-COHORT-001

Read this entire immutable task. Execute only this bounded assignment. Before substantive work, verify that your environment can post one authenticated GitHub issue comment to INTENDED_RETURN. If it cannot, report RETURN_TRANSPORT_UNAVAILABLE and do not begin substantive work.

GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: ERDOS-241-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-241-A1
campaign: ERDOS-OPEN-RECON
work_package: ERDOS-241-RECON-PACK-001
assignment: ERDOS-241-A1
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# ERDOS-241-A1 — ADVERSARIAL

You are an independent zero-context mathematical contributor. This document is your complete bounded work-set.

Timebox: 35 minutes of substantive work, then return the strongest exact result reached.

Work only within this lane. Do not inspect sibling R1/S1/A1 returns, campaign discussion threads, pull requests, unpublished GCL notes, or unlisted source revisions. External literature is not permitted; use only this protected packet and standard mathematics.

Protected Programme execution authority:
`grandchallenge/MATH-PROGRAMME@8f57c7e35393e29b1bdc180b550d30fbbc86682f:governance/erdos_open_recon_execution_authorization.json`.

Protected Solve pack set:
`grandchallenge/MATHSOLVE@a9ab08f463740ca86fcc0efc082ce9ba5de72c04:handoffs/ERDOS-OPEN-001/PACKS.json`.

## Protected authority and source packet

- Programme triage: `grandchallenge/MATH-PROGRAMME@fceda552485562bfb6210e520a10d3d62314a6f0:governance/erdos_open_triage.json`, blob `ec867970360783a3fb9c3247df3bc3b5cfeb2e05`.
- Forge intake: `grandchallenge/MATHFORGE@ec80b855c988e8dc7ddff40cb892b67263d5c86e:sources/ERDOS-OPEN-001/open_problem_manifest.json`, blob `0a71491313ffad6ba2d02a3bdc3fc5a5a8cf65d8`.
- Protected Formal Conjectures snapshot: `google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020`.
- Formal statement path: `FormalConjectures/ErdosProblems/241.lean`.
- Formal statement blob: `8e462d92fcd1e87cb8b211bc8ceaee42ae60a089`.
- Canonical registry page for source audit: `https://www.erdosproblems.com/241`.
- Prize metadata: `$100`.
- Tags: `additive combinatorics`, `sidon sets`.

## Protected problem statement

For the maximum size f(N) of a subset of {1,…,N} with all 3-fold sums distinct up to trivial coincidences, is f(N) asymptotic to N^(1/3)?

Protected facts that may be used without re-derivation:
1. The protected formalization records a Bose–Chowla lower construction `(1+o(1)) N^(1/3)`.
2. It records an upper bound due to Green with leading constant `(7/2)^(1/3) ≈ 1.519`.
3. The protected target is therefore a concrete leading-constant gap.

No pack member may infer that the problem is solved, easier than other Erdős problems, novel to GCL, or certified. The protected registry status is intake evidence, not MATHCERT authority.

## Exact assignment

1. Attack candidate finite-to-asymptotic heuristics and common algebraic inequalities for f(N).
2. Search exact small-N data for counterexamples to subadditivity, multiplicativity, naive product constructions, monotone ratio claims, or extension lemmas that a recon route might be tempted to use.
3. Audit whether the protected Lean definition exactly matches the literature's B3 notion; semantic mismatch counts as a material blocker.
4. Return the first explicit failed inequality/semantic mismatch, or an elimination ledger plus the smallest plausible safe inequality.

## Success criterion

Preferred: an explicit counterexample to a proposed bridge, reduction, pruning rule, semantic identification, or local criterion. Otherwise return a rigorous elimination ledger and the first remaining unsafe inference. Failure to refute the full Erdős statement is not evidence for it.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. Your output is evidence only. Do not create branches, pull requests, files, commits, issues, notes, or attachments. Post exactly one RESULT/1 comment to the GitHub issue containing this bootstrap.

## Required return

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-241-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-241-A1
assignment: ERDOS-241-A1
disposition: <EXACT_REDUCTION|FINITE_CERTIFICATE|SOURCE_INTERFACE_FOUND|COUNTEREXAMPLE|EXACT_BLOCKER|NO_MATERIAL_DELTA>
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: <YES|NO>

## Strongest exact statement
...

## Derivation
...

## Assumptions beyond bootstrap
...

## Verification / falsification hooks
...

## Claim boundary
...

## Next residual
...
```

The first valid conforming return is the durable contribution. No second mathematical comment.

GCL-ZERO-CONTEXT-LAUNCH/2
STATE: ACTIVE
CAMPAIGN: ERDOS-OPEN-RECON
TRANCHE: ERDOS-595-RECON-PACK-001
ASSIGNMENT_ID: ERDOS-595-R1
DISPATCH_ID: ERDOS-595-R1-IA-001
AGENT_REF: INDEPENDENT-AGENT-ERDOS-595-R1
PROTECTED_LEASE_IDENTITY: ERDOS-595-R1 :: ERDOS-595-R1-IA-001 :: INDEPENDENT-AGENT-ERDOS-595-R1
INTENDED_RETURN: https://github.com/grandchallenge/MATHSOLVE/issues/845
RETURN_PROTOCOL: GCL-CONTRIBUTION-RESULT/1
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
EXECUTION_AUTHORIZED: YES
PROTECTED_PROGRAMME_PREDECESSOR: 8f57c7e35393e29b1bdc180b550d30fbbc86682f
PROTECTED_SOLVE_PACK_SET: a9ab08f463740ca86fcc0efc082ce9ba5de72c04
BLIND_COHORT: ERDOS-595-BLIND-COHORT-001

Read this entire immutable task. Execute only this bounded assignment. Before substantive work, verify that your environment can post one authenticated GitHub issue comment to INTENDED_RETURN. If it cannot, report RETURN_TRANSPORT_UNAVAILABLE and do not begin substantive work.

GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: ERDOS-595-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-595-R1
campaign: ERDOS-OPEN-RECON
work_package: ERDOS-595-RECON-PACK-001
assignment: ERDOS-595-R1
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# ERDOS-595-R1 — RECONNAISSANCE

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
- Formal statement path: `FormalConjectures/ErdosProblems/595.lean`.
- Formal statement blob: `c7ae92d69247ed107099978b9c7bce2cc319af76`.
- Canonical registry page for source audit: `https://www.erdosproblems.com/595`.
- Prize metadata: `$250`.
- Tags: `graph theory`, `set theory`.

## Protected problem statement

Does there exist an infinite K4-free graph that is not the union of countably many triangle-free graphs?

Protected facts that may be used without re-derivation:
1. The protected formalization records a finite analogue: for every finite n, there is a finite K4-free graph not coverable by n triangle-free graphs.
2. That finite result is attributed to Folkman [Fo70] and Nešetřil–Rödl [NeRo75].

No pack member may infer that the problem is solved, easier than other Erdős problems, novel to GCL, or certified. The protected registry status is intake evidence, not MATHCERT authority.

## Exact assignment

1. Formalize the exact compactness/limit statement one would need to pass from finite `n`-cover obstructions for all `n` to a single infinite graph with no countable triangle-free cover.
2. Determine which compatibility condition is missing from the bare sequence of finite witnesses: nestedness, embeddings, inverse-system coherence, ultraproduct preservation, or another property.
3. Prove the bridge under the weakest clean extra hypothesis you can justify, or give an exact obstruction showing why ordinary compactness does not supply it.
4. Return a concrete finite-to-infinite theorem schema or the smallest failed implication.

## Success criterion

A successful return is the strongest one of: an exact reduction; a rigorously delimited finite certificate; a reproducible exact computation with a theorem-grade interpretation boundary; or the smallest explicit missing lemma. “I could not solve it” is not a useful return unless accompanied by an exact blocker.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. Your output is evidence only. Do not create branches, pull requests, files, commits, issues, notes, or attachments. Post exactly one RESULT/1 comment to the GitHub issue containing this bootstrap.

## Required return

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-595-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-595-R1
assignment: ERDOS-595-R1
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

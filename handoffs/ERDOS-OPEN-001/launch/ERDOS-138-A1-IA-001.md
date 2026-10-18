GCL-ZERO-CONTEXT-LAUNCH/2
STATE: ACTIVE
CAMPAIGN: ERDOS-OPEN-RECON
TRANCHE: ERDOS-138-RECON-PACK-001
ASSIGNMENT_ID: ERDOS-138-A1
DISPATCH_ID: ERDOS-138-A1-IA-001
AGENT_REF: INDEPENDENT-AGENT-ERDOS-138-A1
PROTECTED_LEASE_IDENTITY: ERDOS-138-A1 :: ERDOS-138-A1-IA-001 :: INDEPENDENT-AGENT-ERDOS-138-A1
INTENDED_RETURN: https://github.com/grandchallenge/MATHSOLVE/issues/865
RETURN_PROTOCOL: GCL-CONTRIBUTION-RESULT/1
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
EXECUTION_AUTHORIZED: YES
PROTECTED_PROGRAMME_PREDECESSOR: 8f57c7e35393e29b1bdc180b550d30fbbc86682f
PROTECTED_SOLVE_PACK_SET: a9ab08f463740ca86fcc0efc082ce9ba5de72c04
BLIND_COHORT: ERDOS-138-BLIND-COHORT-001

Read this entire immutable task. Execute only this bounded assignment. Before substantive work, verify that your environment can post one authenticated GitHub issue comment to INTENDED_RETURN. If it cannot, report RETURN_TRANSPORT_UNAVAILABLE and do not begin substantive work.

GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: ERDOS-138-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-138-A1
campaign: ERDOS-OPEN-RECON
work_package: ERDOS-138-RECON-PACK-001
assignment: ERDOS-138-A1
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# ERDOS-138-A1 — ADVERSARIAL

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
- Formal statement path: `FormalConjectures/ErdosProblems/138.lean`.
- Formal statement blob: `061c7b62abe53b0db18a3d795b8e71ea4efc70c0`.
- Canonical registry page for source audit: `https://www.erdosproblems.com/138`.
- Prize metadata: `$500`.
- Tags: `additive combinatorics`.

## Protected problem statement

Does W(k)^(1/k) tend to infinity for the protected van der Waerden-number function W?

Protected facts that may be used without re-derivation:
1. The protected file records a Berlekamp lower-bound comment and a Gowers upper-bound variant.
2. There is a material semantic warning inside the protected snapshot: the prose comment says `W(p+1) ≥ p^(2^p)`, while the Lean theorem body states only `p * 2^p ≤ W(p+1)`. These must not be treated as equivalent without source reconciliation.
3. The file also records related quotient and difference-growth variants.

No pack member may infer that the problem is solved, easier than other Erdős problems, novel to GCL, or certified. The protected registry status is intake evidence, not MATHCERT authority.

## Exact assignment

1. Attack every inference from a sparse-subsequence lower bound to a full limit. Require an explicit density/gap lemma for the subsequence and monotonicity of the exact W definition.
2. Treat the protected prose/theorem discrepancy as an adversarial target: determine which downstream conclusions change under `p^(2^p)` versus `p*2^p`.
3. Search for normalization mismatches (number of colors versus progression length, off-by-one parameters) that could make a superficially strong bound irrelevant.
4. Return a concrete false implication/normalization mismatch or a proof that the interpolation step is safe under a precisely stated bound.

## Success criterion

Preferred: an explicit counterexample to a proposed bridge, reduction, pruning rule, semantic identification, or local criterion. Otherwise return a rigorous elimination ledger and the first remaining unsafe inference. Failure to refute the full Erdős statement is not evidence for it.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. Your output is evidence only. Do not create branches, pull requests, files, commits, issues, notes, or attachments. Post exactly one RESULT/1 comment to the GitHub issue containing this bootstrap.

## Required return

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-138-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-138-A1
assignment: ERDOS-138-A1
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

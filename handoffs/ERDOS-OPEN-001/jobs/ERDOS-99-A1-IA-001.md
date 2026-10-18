GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: ERDOS-99-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-99-A1
campaign: ERDOS-OPEN-RECON
work_package: ERDOS-99-RECON-PACK-001
assignment: ERDOS-99-A1
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# ERDOS-99-A1 — ADVERSARIAL

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
- Formal statement path: `FormalConjectures/ErdosProblems/99.lean`.
- Formal statement blob: `85b244eee4c29defd38c93ab559de6d9e8d4cfa8`.
- Canonical registry page for source audit: `https://www.erdosproblems.com/99`.
- Prize metadata: `$100`.
- Tags: `geometry`, `distances`.

## Protected problem statement

For all sufficiently large n, must every n-point planar set of minimum pairwise distance 1 that minimizes diameter contain a unit equilateral triangle?

Protected facts that may be used without re-derivation:
1. The protected formalization fixes minimum distance 1 and asks about global diameter minimizers.
2. The target is eventual in n; small counterexamples would not by themselves refute it.

No pack member may infer that the problem is solved, easier than other Erdős problems, novel to GCL, or certified. The protected registry status is intake evidence, not MATHCERT authority.

## Exact assignment

1. Attack the heuristic `global diameter minimizer ⇒ triangular contact graph/equilateral triangle`.
2. Construct triangle-free locally rigid unit-distance/contact configurations, or numerical near-minimizers, to show which local conditions are insufficient.
3. Test whether an argument accidentally assumes uniqueness, genericity, or every active constraint being a unit-distance edge.
4. Return an explicit configuration defeating a proposed local criterion or a minimal set of additional global conditions.

## Success criterion

Preferred: an explicit counterexample to a proposed bridge, reduction, pruning rule, semantic identification, or local criterion. Otherwise return a rigorous elimination ledger and the first remaining unsafe inference. Failure to refute the full Erdős statement is not evidence for it.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. Your output is evidence only. Do not create branches, pull requests, files, commits, issues, notes, or attachments. Post exactly one RESULT/1 comment to the GitHub issue containing this bootstrap.

## Required return

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-99-A1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-99-A1
assignment: ERDOS-99-A1
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

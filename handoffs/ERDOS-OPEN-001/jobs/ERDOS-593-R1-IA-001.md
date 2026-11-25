GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: ERDOS-593-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-593-R1
campaign: ERDOS-OPEN-RECON
work_package: ERDOS-593-RECON-PACK-001
assignment: ERDOS-593-R1
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# ERDOS-593-R1 — RECONNAISSANCE

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
- Formal statement path: `FormalConjectures/ErdosProblems/593.lean`.
- Formal statement blob: `fe5872380f07a2989c8a25ba44f4b29bb5d65dd7`.
- Canonical registry page for source audit: `https://www.erdosproblems.com/593`.
- Prize metadata: `$500`.
- Tags: `set theory`, `graph theory`, `hypergraphs`, `chromatic number`.

## Protected problem statement

Characterize finite 3-uniform hypergraphs that occur in every 3-uniform hypergraph of uncountable chromatic number. The protected formalization records the conjectural characterization: obligatory iff 2-colorable (Property B), and splits it into the necessary and sufficient implications.

Protected facts that may be used without re-derivation:
1. The protected formalization exposes the two implications separately.
2. It records the graph-case analogue: obligatory iff bipartite, attributed to Erdős–Galvin–Hajnal [EGH75].

No pack member may infer that the problem is solved, easier than other Erdős problems, novel to GCL, or certified. The protected registry status is intake evidence, not MATHCERT authority.

## Exact assignment

1. Choose one direction, preferably the necessary implication `IsObligatory F → F.IsTwoColorable`, and reduce it to the smallest explicit construction principle that would build an uncountably chromatic 3-uniform host avoiding a fixed non-2-colorable finite `F`.
2. Classify the first nontrivial finite 3-uniform `F` by vertex count/property-B status and identify which families are automatically easy or impossible under the definition.
3. Return either a theorem-grade reduction for a structural family, a finite exact classification that exposes the first genuine obstruction, or the smallest missing lemma.

## Success criterion

A successful return is the strongest one of: an exact reduction; a rigorously delimited finite certificate; a reproducible exact computation with a theorem-grade interpretation boundary; or the smallest explicit missing lemma. “I could not solve it” is not a useful return unless accompanied by an exact blocker.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. Your output is evidence only. Do not create branches, pull requests, files, commits, issues, notes, or attachments. Post exactly one RESULT/1 comment to the GitHub issue containing this bootstrap.

## Required return

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-593-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-593-R1
assignment: ERDOS-593-R1
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

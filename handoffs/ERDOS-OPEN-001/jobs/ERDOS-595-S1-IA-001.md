GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: ERDOS-595-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-595-S1
campaign: ERDOS-OPEN-RECON
work_package: ERDOS-595-RECON-PACK-001
assignment: ERDOS-595-S1
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# ERDOS-595-S1 — SOURCE-AUDIT

You are an independent zero-context mathematical contributor. This document is your complete bounded work-set.

Timebox: 35 minutes of substantive work, then return the strongest exact result reached.

Work only within this lane. Do not inspect sibling R1/S1/A1 returns, campaign discussion threads, pull requests, unpublished GCL notes, or unlisted source revisions. Primary sources are required and may be searched.

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

1. Resolve the original Erdős–Hajnal formulation and the exact Folkman / Nešetřil–Rödl finite theorems from primary sources.
2. Audit whether the infinite problem has known consistency results, cardinal assumptions, compactness formulations, or later partial solutions.
3. Record exactly what 'union of countably many triangle-free graphs' means in the primary literature and compare it with the protected Lean definition.

## Required source output

Return exact bibliographic identities, stable URLs/DOIs/arXiv identifiers when available, theorem/page/section locations, quoted terminology only when necessary, and a dependency table:
`source claim → exact hypotheses → relevance to protected target → semantic match/conflict → confidence`.

Do not report “current best known” without a dated primary source or an explicit statement that the audit could not establish currency.

## Source-return transport constraint

You may use primary sources during the assignment. In the RESULT/1 comment, cite DOI, arXiv, MR, book/paper title, theorem/page/section, and other bibliographic identifiers as plain text. Do **not** include raw URLs, Markdown links, HTML links, images, or attachments; the controlled intake transport rejects them.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. Your output is evidence only. Do not create branches, pull requests, files, commits, issues, notes, or attachments. Post exactly one RESULT/1 comment to the GitHub issue containing this bootstrap.

## Required return

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-595-S1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-595-S1
assignment: ERDOS-595-S1
disposition: <EXACT_REDUCTION|FINITE_CERTIFICATE|SOURCE_INTERFACE_FOUND|COUNTEREXAMPLE|EXACT_BLOCKER|NO_MATERIAL_DELTA>
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_REQUIRED
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

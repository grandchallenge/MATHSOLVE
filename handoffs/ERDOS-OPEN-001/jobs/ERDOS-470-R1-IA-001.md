GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: ERDOS-470-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-470-R1
campaign: ERDOS-OPEN-RECON
work_package: ERDOS-470-RECON-PACK-001
assignment: ERDOS-470-R1
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# ERDOS-470-R1 — RECONNAISSANCE

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
- Formal statement path: `FormalConjectures/ErdosProblems/470.lean`.
- Formal statement blob: `901267a999167143f9eb708ecda9adb9c64fe5dc`.
- Canonical registry page for source audit: `https://www.erdosproblems.com/470`.
- Prize metadata: `$10`.
- Tags: `number theory`, `divisors`.

## Protected problem statement

Two registered open parts: do odd weird numbers exist, and are there infinitely many primitive weird numbers?

Protected facts that may be used without re-derivation:
1. A weird number is abundant but not pseudoperfect.
2. The protected snapshot records that weird numbers have positive density, attributed to Benkoski–Erdős [BeEr74].
3. It formally checks that 70 is the smallest weird number.

No pack member may infer that the problem is solved, easier than other Erdős problems, novel to GCL, or certified. The protected registry status is intake evidence, not MATHCERT authority.

## Exact assignment

1. Implement an exact weird-number predicate using factorization plus an exact subset-sum/pseudoperfectness certificate, and independently reproduce the smallest examples.
2. For odd candidates, derive and exploit exact necessary conditions from abundance, prime factorization, abundancy index, and subset-sum structure; perform a bounded exact search whose range is justified by runtime, not by a theorem claim.
3. For primitive weird numbers, identify an exact structural operation that preserves weirdness or primitivity, or prove why an obvious multiplicative construction fails.
4. Return searchable certificates, exact bounds searched, and the strongest structural lemma/blocker.

## Success criterion

A successful return is the strongest one of: an exact reduction; a rigorously delimited finite certificate; a reproducible exact computation with a theorem-grade interpretation boundary; or the smallest explicit missing lemma. “I could not solve it” is not a useful return unless accompanied by an exact blocker.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. Your output is evidence only. Do not create branches, pull requests, files, commits, issues, notes, or attachments. Post exactly one RESULT/1 comment to the GitHub issue containing this bootstrap.

## Required return

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-470-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-470-R1
assignment: ERDOS-470-R1
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

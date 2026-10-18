GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: ERDOS-138-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-138-R1
campaign: ERDOS-OPEN-RECON
work_package: ERDOS-138-RECON-PACK-001
assignment: ERDOS-138-R1
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: THIS_BOUND_GITHUB_ISSUE

# ERDOS-138-R1 — RECONNAISSANCE

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

1. Work from the protected Lean statement, not the unreconciled prose bound. Derive exact equivalent growth formulations, e.g. in logarithmic form, and prove the monotonicity/interpolation lemmas needed to pass from bounds on a subsequence to all k.
2. Build an exact small-k ledger for the protected definition W and verify that the definition agrees with the intended classical van der Waerden number normalization.
3. Conditionally analyze what strength of lower bound on primes or another dense subsequence would imply root divergence; make the condition explicit rather than importing the disputed Berlekamp exponent.
4. Return a theorem-grade conditional reduction and the exact lower-bound threshold needed.

## Success criterion

A successful return is the strongest one of: an exact reduction; a rigorously delimited finite certificate; a reproducible exact computation with a theorem-grade interpretation boundary; or the smallest explicit missing lemma. “I could not solve it” is not a useful return unless accompanied by an exact blocker.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. Your output is evidence only. Do not create branches, pull requests, files, commits, issues, notes, or attachments. Post exactly one RESULT/1 comment to the GitHub issue containing this bootstrap.

## Required return

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: ERDOS-138-R1-IA-001
agent_ref: INDEPENDENT-AGENT-ERDOS-138-R1
assignment: ERDOS-138-R1
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

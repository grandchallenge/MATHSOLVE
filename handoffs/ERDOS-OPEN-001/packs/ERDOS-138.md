STATUS: DRAFT_NOT_ACTIVATED
PACK_ID: ERDOS-138-RECON-PACK-001
PROBLEM_ID: 138
TITLE: Root growth of van der Waerden numbers
CONTEXT_CLASS: ZERO_CONTEXT
EXECUTION_AUTHORIZED: NO
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
RETURN_PROTOCOL_IF_ACTIVATED: GCL-CONTRIBUTION-RESULT/1
ACTIVATION_REQUIRES: PROTECTED_ISSUE_DISPATCH_AGENT_LEASE_BINDING

# Erdős Problem 138 — bounded reconnaissance/source/adversarial pack

This is a complete **pre-launch** work-package pack. It defines bounded assignments but authorizes no contributor execution. A later protected activation transaction must bind each assignment to one GitHub issue, one dispatch ID, one agent reference, and one lease identity before any prompt is executable.

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


## Blind-lane rule

When activated as a cohort, R/S/A returns are independent until all intended evidence is preserved. A worker must not inspect sibling returns. Source audit may inspect primary literature; reconnaissance and adversarial lanes may not use the source-lane return during their first pass.

---

# WP-R — bounded mathematical reconnaissance

PROPOSED_ASSIGNMENT_ID: ERDOS-138-R1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
MODE: INDEPENDENT_BLIND_RECONNAISSANCE

You are an independent zero-context mathematical contributor. Work only from the protected packet above and standard mathematics. Do not inspect sibling packets/returns, campaign discussions, pull requests, unpublished GCL notes, or external literature.

## Exact assignment

1. Work from the protected Lean statement, not the unreconciled prose bound. Derive exact equivalent growth formulations, e.g. in logarithmic form, and prove the monotonicity/interpolation lemmas needed to pass from bounds on a subsequence to all k.
2. Build an exact small-k ledger for the protected definition W and verify that the definition agrees with the intended classical van der Waerden number normalization.
3. Conditionally analyze what strength of lower bound on primes or another dense subsequence would imply root divergence; make the condition explicit rather than importing the disputed Berlekamp exponent.
4. Return a theorem-grade conditional reduction and the exact lower-bound threshold needed.

## Success criterion

A successful return is the strongest one of: an exact reduction; a rigorously delimited finite certificate; a reproducible exact computation with a theorem-grade interpretation boundary; or the smallest explicit missing lemma. “I could not solve it” is not a useful return unless accompanied by an exact blocker.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-138-R1
disposition: <EXACT_REDUCTION|FINITE_CERTIFICATE|SOURCE_INTERFACE_FOUND|COUNTEREXAMPLE|EXACT_BLOCKER|NO_MATERIAL_DELTA>
context_class: ZERO_CONTEXT
external_sources: <AS_DECLARED_BY_LANE>
timebox_observed: <YES|NO>

## Strongest exact statement
...

## Derivation or source evidence
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

No branch, pull request, attachment, second mathematical comment, certification claim, or canonical mutation is authorized.


---

# WP-S — primary-source interface audit

PROPOSED_ASSIGNMENT_ID: ERDOS-138-S1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PRIMARY_SOURCES_REQUIRED
MODE: INDEPENDENT_SOURCE_AUDIT

You are an independent zero-context source contributor. Start from the canonical registry page and the protected formalization. Primary papers/preprints/books are preferred; secondary sources may be used only to locate primary evidence. Do not inspect sibling returns or unpublished GCL material.

Seed citation labels already present in the protected packet: `Er80`, `Be68`, `Go01`, `Er81`.

## Exact assignment

1. Resolve [Er80], [Be68], [Go01], [Er81] from primary sources and reconcile the protected Berlekamp discrepancy character-for-character.
2. Determine the correct historical/current lower bound for the exact W(k) normalization used here and whether it already implies the registered root-growth conjecture when combined with monotonicity and prime-distribution facts.
3. Audit whether the canonical Erdős Problems page still marks the root-growth question open and explain any apparent tension with the cited bounds.
4. This source lane is successful even if it discovers that the protected formal statement or annotation is stale or semantically mismatched.

## Required source output

Return exact bibliographic identities, stable URLs/DOIs/arXiv identifiers when available, theorem/page/section locations, quoted terminology only when necessary, and a dependency table:
`source claim → exact hypotheses → relevance to protected target → semantic match/conflict → confidence`.

Do not report “current best known” without a dated primary source or an explicit statement that the audit could not establish currency.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-138-S1
disposition: <EXACT_REDUCTION|FINITE_CERTIFICATE|SOURCE_INTERFACE_FOUND|COUNTEREXAMPLE|EXACT_BLOCKER|NO_MATERIAL_DELTA>
context_class: ZERO_CONTEXT
external_sources: <AS_DECLARED_BY_LANE>
timebox_observed: <YES|NO>

## Strongest exact statement
...

## Derivation or source evidence
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

No branch, pull request, attachment, second mathematical comment, certification claim, or canonical mutation is authorized.


---

# WP-A — adversarial falsification / route attack

PROPOSED_ASSIGNMENT_ID: ERDOS-138-A1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
MODE: INDEPENDENT_BLIND_ADVERSARY

You are an independent zero-context adversarial mathematical contributor. Work from the protected packet and standard mathematics only. Do not inspect the reconnaissance or source returns.

## Exact assignment

1. Attack every inference from a sparse-subsequence lower bound to a full limit. Require an explicit density/gap lemma for the subsequence and monotonicity of the exact W definition.
2. Treat the protected prose/theorem discrepancy as an adversarial target: determine which downstream conclusions change under `p^(2^p)` versus `p*2^p`.
3. Search for normalization mismatches (number of colors versus progression length, off-by-one parameters) that could make a superficially strong bound irrelevant.
4. Return a concrete false implication/normalization mismatch or a proof that the interpolation step is safe under a precisely stated bound.

## Success criterion

Preferred: an explicit counterexample to a proposed bridge, reduction, pruning rule, semantic identification, or local criterion. Otherwise return a rigorous elimination ledger and the first remaining unsafe inference. Failure to refute the full Erdős statement is not evidence for it.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-138-A1
disposition: <EXACT_REDUCTION|FINITE_CERTIFICATE|SOURCE_INTERFACE_FOUND|COUNTEREXAMPLE|EXACT_BLOCKER|NO_MATERIAL_DELTA>
context_class: ZERO_CONTEXT
external_sources: <AS_DECLARED_BY_LANE>
timebox_observed: <YES|NO>

## Strongest exact statement
...

## Derivation or source evidence
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

No branch, pull request, attachment, second mathematical comment, certification claim, or canonical mutation is authorized.


---

## Pack synthesis gate

This pack is not a campaign. After activation and durable preservation of returns, synthesis may open only when at least one R return and one A return exist; S is required before any literature-dependent claim is promoted. Synthesis must select the smallest native GCL theorem/obstruction and create a new protected work package. Nothing in this pack directly authorizes a theorem claim, a Solve campaign, or certification.

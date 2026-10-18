STATUS: DRAFT_NOT_ACTIVATED
PACK_ID: ERDOS-595-RECON-PACK-001
PROBLEM_ID: 595
TITLE: Infinite K4-free graph versus countable triangle-free covers
CONTEXT_CLASS: ZERO_CONTEXT
EXECUTION_AUTHORIZED: NO
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
RETURN_PROTOCOL_IF_ACTIVATED: GCL-CONTRIBUTION-RESULT/1
ACTIVATION_REQUIRES: PROTECTED_ISSUE_DISPATCH_AGENT_LEASE_BINDING

# Erdős Problem 595 — bounded reconnaissance/source/adversarial pack

This is a complete **pre-launch** work-package pack. It defines bounded assignments but authorizes no contributor execution. A later protected activation transaction must bind each assignment to one GitHub issue, one dispatch ID, one agent reference, and one lease identity before any prompt is executable.

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


## Blind-lane rule

When activated as a cohort, R/S/A returns are independent until all intended evidence is preserved. A worker must not inspect sibling returns. Source audit may inspect primary literature; reconnaissance and adversarial lanes may not use the source-lane return during their first pass.

---

# WP-R — bounded mathematical reconnaissance

PROPOSED_ASSIGNMENT_ID: ERDOS-595-R1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
MODE: INDEPENDENT_BLIND_RECONNAISSANCE

You are an independent zero-context mathematical contributor. Work only from the protected packet above and standard mathematics. Do not inspect sibling packets/returns, campaign discussions, pull requests, unpublished GCL notes, or external literature.

## Exact assignment

1. Formalize the exact compactness/limit statement one would need to pass from finite `n`-cover obstructions for all `n` to a single infinite graph with no countable triangle-free cover.
2. Determine which compatibility condition is missing from the bare sequence of finite witnesses: nestedness, embeddings, inverse-system coherence, ultraproduct preservation, or another property.
3. Prove the bridge under the weakest clean extra hypothesis you can justify, or give an exact obstruction showing why ordinary compactness does not supply it.
4. Return a concrete finite-to-infinite theorem schema or the smallest failed implication.

## Success criterion

A successful return is the strongest one of: an exact reduction; a rigorously delimited finite certificate; a reproducible exact computation with a theorem-grade interpretation boundary; or the smallest explicit missing lemma. “I could not solve it” is not a useful return unless accompanied by an exact blocker.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-595-R1
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

PROPOSED_ASSIGNMENT_ID: ERDOS-595-S1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PRIMARY_SOURCES_REQUIRED
MODE: INDEPENDENT_SOURCE_AUDIT

You are an independent zero-context source contributor. Start from the canonical registry page and the protected formalization. Primary papers/preprints/books are preferred; secondary sources may be used only to locate primary evidence. Do not inspect sibling returns or unpublished GCL material.

Seed citation labels already present in the protected packet: `Er87`, `Fo70`, `NeRo75`.

## Exact assignment

1. Resolve the original Erdős–Hajnal formulation and the exact Folkman / Nešetřil–Rödl finite theorems from primary sources.
2. Audit whether the infinite problem has known consistency results, cardinal assumptions, compactness formulations, or later partial solutions.
3. Record exactly what 'union of countably many triangle-free graphs' means in the primary literature and compare it with the protected Lean definition.

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
assignment: ERDOS-595-S1
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

PROPOSED_ASSIGNMENT_ID: ERDOS-595-A1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
MODE: INDEPENDENT_BLIND_ADVERSARY

You are an independent zero-context adversarial mathematical contributor. Work from the protected packet and standard mathematics only. Do not inspect the reconnaissance or source returns.

## Exact assignment

1. Attack the inference `arbitrarily large finite cover number ⇒ one graph of infinite/countable cover number`.
2. Construct or identify an abstract class where every finite cover number occurs but no coherent limit witness exists; then test which graph-specific properties block or permit that pathology.
3. Stress ultraproduct and compactness routes: determine whether K4-freeness and 'not n-coverable' are first-order enough for the proposed passage, and whether countable non-coverability survives.
4. Return a countermodel to a naive bridge or a minimal extra compactness/coherence assumption.

## Success criterion

Preferred: an explicit counterexample to a proposed bridge, reduction, pruning rule, semantic identification, or local criterion. Otherwise return a rigorous elimination ledger and the first remaining unsafe inference. Failure to refute the full Erdős statement is not evidence for it.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-595-A1
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

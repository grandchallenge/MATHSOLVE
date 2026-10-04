STATUS: DRAFT_NOT_ACTIVATED
PACK_ID: ERDOS-593-RECON-PACK-001
PROBLEM_ID: 593
TITLE: Obligatory finite 3-uniform hypergraphs
CONTEXT_CLASS: ZERO_CONTEXT
EXECUTION_AUTHORIZED: NO
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
RETURN_PROTOCOL_IF_ACTIVATED: GCL-CONTRIBUTION-RESULT/1
ACTIVATION_REQUIRES: PROTECTED_ISSUE_DISPATCH_AGENT_LEASE_BINDING

# Erdős Problem 593 — bounded reconnaissance/source/adversarial pack

This is a complete **pre-launch** work-package pack. It defines bounded assignments but authorizes no contributor execution. A later protected activation transaction must bind each assignment to one GitHub issue, one dispatch ID, one agent reference, and one lease identity before any prompt is executable.

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


## Blind-lane rule

When activated as a cohort, R/S/A returns are independent until all intended evidence is preserved. A worker must not inspect sibling returns. Source audit may inspect primary literature; reconnaissance and adversarial lanes may not use the source-lane return during their first pass.

---

# WP-R — bounded mathematical reconnaissance

PROPOSED_ASSIGNMENT_ID: ERDOS-593-R1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
MODE: INDEPENDENT_BLIND_RECONNAISSANCE

You are an independent zero-context mathematical contributor. Work only from the protected packet above and standard mathematics. Do not inspect sibling packets/returns, campaign discussions, pull requests, unpublished GCL notes, or external literature.

## Exact assignment

1. Choose one direction, preferably the necessary implication `IsObligatory F → F.IsTwoColorable`, and reduce it to the smallest explicit construction principle that would build an uncountably chromatic 3-uniform host avoiding a fixed non-2-colorable finite `F`.
2. Classify the first nontrivial finite 3-uniform `F` by vertex count/property-B status and identify which families are automatically easy or impossible under the definition.
3. Return either a theorem-grade reduction for a structural family, a finite exact classification that exposes the first genuine obstruction, or the smallest missing lemma.

## Success criterion

A successful return is the strongest one of: an exact reduction; a rigorously delimited finite certificate; a reproducible exact computation with a theorem-grade interpretation boundary; or the smallest explicit missing lemma. “I could not solve it” is not a useful return unless accompanied by an exact blocker.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-593-R1
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

PROPOSED_ASSIGNMENT_ID: ERDOS-593-S1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PRIMARY_SOURCES_REQUIRED
MODE: INDEPENDENT_SOURCE_AUDIT

You are an independent zero-context source contributor. Start from the canonical registry page and the protected formalization. Primary papers/preprints/books are preferred; secondary sources may be used only to locate primary evidence. Do not inspect sibling returns or unpublished GCL material.

Seed citation labels already present in the protected packet: `EGH75`.

## Exact assignment

1. Resolve the canonical Erdős Problems page and every primary reference needed to establish the exact historical statement, the definition of 'obligatory', and the graph-case theorem [EGH75].
2. Search specifically for higher-uniform partial results, necessary conditions, or consistency/set-theoretic hypotheses. Distinguish ZFC theorems from stronger set-theoretic assumptions.
3. Produce a source dependency map: exact theorem statement, hypotheses, what it proves toward each implication, and whether the protected formalization matches it semantically.

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
assignment: ERDOS-593-S1
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

PROPOSED_ASSIGNMENT_ID: ERDOS-593-A1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
MODE: INDEPENDENT_BLIND_ADVERSARY

You are an independent zero-context adversarial mathematical contributor. Work from the protected packet and standard mathematics only. Do not inspect the reconnaissance or source returns.

## Exact assignment

1. Attack the conjectural equivalence, not the protected fact that it is the registered target.
2. Try to break naive transfers from the graph case: test whether bipartite/Property-B analogies preserve the relevant chromatic and embedding mechanisms in uniformity 3.
3. For the necessary direction, seek a non-2-colorable finite `F` for which every attempted high-chromatic `F`-free host construction fails for a structural reason. For the sufficient direction, seek a 2-colorable `F` that evades a plausible obligatory-host argument.
4. A valid negative result is an explicit counterexample to a proposed bridge or a precise reason a graph-case proof step cannot generalize.

## Success criterion

Preferred: an explicit counterexample to a proposed bridge, reduction, pruning rule, semantic identification, or local criterion. Otherwise return a rigorous elimination ledger and the first remaining unsafe inference. Failure to refute the full Erdős statement is not evidence for it.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-593-A1
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

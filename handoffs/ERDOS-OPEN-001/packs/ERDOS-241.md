STATUS: DRAFT_NOT_ACTIVATED
PACK_ID: ERDOS-241-RECON-PACK-001
PROBLEM_ID: 241
TITLE: Bose–Chowla B3 extremal asymptotics
CONTEXT_CLASS: ZERO_CONTEXT
EXECUTION_AUTHORIZED: NO
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
RETURN_PROTOCOL_IF_ACTIVATED: GCL-CONTRIBUTION-RESULT/1
ACTIVATION_REQUIRES: PROTECTED_ISSUE_DISPATCH_AGENT_LEASE_BINDING

# Erdős Problem 241 — bounded reconnaissance/source/adversarial pack

This is a complete **pre-launch** work-package pack. It defines bounded assignments but authorizes no contributor execution. A later protected activation transaction must bind each assignment to one GitHub issue, one dispatch ID, one agent reference, and one lease identity before any prompt is executable.

## Protected authority and source packet

- Programme triage: `grandchallenge/MATH-PROGRAMME@fceda552485562bfb6210e520a10d3d62314a6f0:governance/erdos_open_triage.json`, blob `ec867970360783a3fb9c3247df3bc3b5cfeb2e05`.
- Forge intake: `grandchallenge/MATHFORGE@ec80b855c988e8dc7ddff40cb892b67263d5c86e:sources/ERDOS-OPEN-001/open_problem_manifest.json`, blob `0a71491313ffad6ba2d02a3bdc3fc5a5a8cf65d8`.
- Protected Formal Conjectures snapshot: `google-deepmind/formal-conjectures@85f863718beeec7b58a3a1926ee92e3472bc2020`.
- Formal statement path: `FormalConjectures/ErdosProblems/241.lean`.
- Formal statement blob: `8e462d92fcd1e87cb8b211bc8ceaee42ae60a089`.
- Canonical registry page for source audit: `https://www.erdosproblems.com/241`.
- Prize metadata: `$100`.
- Tags: `additive combinatorics`, `sidon sets`.

## Protected problem statement

For the maximum size f(N) of a subset of {1,…,N} with all 3-fold sums distinct up to trivial coincidences, is f(N) asymptotic to N^(1/3)?

Protected facts that may be used without re-derivation:
1. The protected formalization records a Bose–Chowla lower construction `(1+o(1)) N^(1/3)`.
2. It records an upper bound due to Green with leading constant `(7/2)^(1/3) ≈ 1.519`.
3. The protected target is therefore a concrete leading-constant gap.

No pack member may infer that the problem is solved, easier than other Erdős problems, novel to GCL, or certified. The protected registry status is intake evidence, not MATHCERT authority.


## Blind-lane rule

When activated as a cohort, R/S/A returns are independent until all intended evidence is preserved. A worker must not inspect sibling returns. Source audit may inspect primary literature; reconnaissance and adversarial lanes may not use the source-lane return during their first pass.

---

# WP-R — bounded mathematical reconnaissance

PROPOSED_ASSIGNMENT_ID: ERDOS-241-R1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
MODE: INDEPENDENT_BLIND_RECONNAISSANCE

You are an independent zero-context mathematical contributor. Work only from the protected packet above and standard mathematics. Do not inspect sibling packets/returns, campaign discussions, pull requests, unpublished GCL notes, or external literature.

## Exact assignment

1. Build an exact finite solver for the protected B3 condition and certify f(N) for a nontrivial initial range. Minimum acceptable target: reproduce a correct exact solver and certify all N through at least 30; extend only if cheap.
2. Extract structural constraints from extremizers: residue patterns, difference/sum collisions, translate/scale normalizations, and local extension rules.
3. Use the exact data only to propose one explicit inequality or finite-extension lemma that could tighten the upper constant. Do not extrapolate numerics into an asymptotic theorem.
4. Return code/pseudocode, exact certificates or reproducible tables, and one sharply stated candidate lemma or obstruction.

## Success criterion

A successful return is the strongest one of: an exact reduction; a rigorously delimited finite certificate; a reproducible exact computation with a theorem-grade interpretation boundary; or the smallest explicit missing lemma. “I could not solve it” is not a useful return unless accompanied by an exact blocker.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-241-R1
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

PROPOSED_ASSIGNMENT_ID: ERDOS-241-S1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PRIMARY_SOURCES_REQUIRED
MODE: INDEPENDENT_SOURCE_AUDIT

You are an independent zero-context source contributor. Start from the canonical registry page and the protected formalization. Primary papers/preprints/books are preferred; secondary sources may be used only to locate primary evidence. Do not inspect sibling returns or unpublished GCL material.

Seed citation labels already present in the protected packet: `BoCh62`, `Gr01`, `Gu04`.

## Exact assignment

1. Resolve Bose–Chowla [BoCh62], Green [Gr01], and the canonical problem page to primary statements.
2. Verify the exact definition of the B3 condition, especially treatment of repeated summands and 'trivial coincidences'.
3. Audit the current best upper constant and any post-Green improvements. If the protected `(7/2)^(1/3)` statement is stale, give exact primary-source replacement evidence.
4. Produce a constant-gap ledger with theorem hypotheses and normalization conventions.

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
assignment: ERDOS-241-S1
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

PROPOSED_ASSIGNMENT_ID: ERDOS-241-A1
TIMEBOX_IF_ACTIVATED: 35 minutes
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
MODE: INDEPENDENT_BLIND_ADVERSARY

You are an independent zero-context adversarial mathematical contributor. Work from the protected packet and standard mathematics only. Do not inspect the reconnaissance or source returns.

## Exact assignment

1. Attack candidate finite-to-asymptotic heuristics and common algebraic inequalities for f(N).
2. Search exact small-N data for counterexamples to subadditivity, multiplicativity, naive product constructions, monotone ratio claims, or extension lemmas that a recon route might be tempted to use.
3. Audit whether the protected Lean definition exactly matches the literature's B3 notion; semantic mismatch counts as a material blocker.
4. Return the first explicit failed inequality/semantic mismatch, or an elimination ledger plus the smallest plausible safe inequality.

## Success criterion

Preferred: an explicit counterexample to a proposed bridge, reduction, pruning rule, semantic identification, or local criterion. Otherwise return a rigorous elimination ledger and the first remaining unsafe inference. Failure to refute the full Erdős statement is not evidence for it.

## Return discipline if activated

Return exactly one narrative `GCL-CONTRIBUTION-RESULT/1` on the bound issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <BOUND_AT_ACTIVATION>
agent_ref: <BOUND_AT_ACTIVATION>
assignment: ERDOS-241-A1
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

# Foundation-Aware Routing Standard

Status: proposed MATHSOLVE routing standard  
Purpose: route mathematical work packages by foundational texture as well as by mathematical domain.

## Routing principle

A solver route should not be chosen only from the domain label `algebra`, `analysis`, `number theory`, `geometry`, or `combinatorics`. MATHSOLVE must also inspect the work package's foundational profile.

The central routing question is:

```text
What kind of object is this, and what kind of evidence could legitimately settle the claim?
```

## Required inputs from MATHFORGE

Every MATHSOLVE work package should include:

```yaml
foundational_profile:
  carrier_type: finite | countable | continuum | higher_type | categorical | unknown
  ambient_structure: []
  admissible_operations: []
  regularity: []
  axiom_profile:
    base: finite | constructive | ZF | ZF+DC | ZFC | stronger | unknown
    choice_usage: none | finite_choice | countable_choice | dependent_choice | full_choice | unknown
    excluded_middle: avoided | local | used | unknown
  witness_policy:
    existence_claim: explicit_witness | extractable | nonconstructive | contradiction_only | unknown
  pathology_risk:
    level: low | medium | high | unknown
```

If the block is absent, MATHSOLVE should create a `foundation_profile_missing` task rather than pretending the route is clear.

## Route classes

### R0: finite-computable route

Use when the carrier is finite, decidable, bounded, or explicitly enumerable.

Preferred tactics:

- finite enumeration;
- SAT/SMT/pseudo-Boolean encoding;
- exact integer/rational computation;
- proof-producing search;
- small verifier;
- Lean finite proof;
- counterexample generation.

Output expectation:

```yaml
solver_output:
  route: finite-computable
  artifact_type: witness | counterexample | certificate | exhaustive_trace
  certificate_candidate: true
```

### R1: constructive-witness route

Use when existence claims should produce actual witnesses, algorithms, maps, terms, or constructions.

Preferred tactics:

- constructive proof search;
- explicit algorithm synthesis;
- witness extraction;
- type-theoretic or proof-term formulation;
- executable construction with validation.

Solver must distinguish:

```text
proved existence by construction
proved existence by contradiction
proved existence classically without witness
```

### R2: regular-analytic route

Use for analysis, measure, probability, dynamics, PDE, geometric analysis, and optimization when regularity assumptions are present or can be introduced responsibly.

Preferred tactics:

- reduce to Borel/standard Borel/Polish/separable settings;
- use compactness only with explicit compactness hypothesis;
- use measurable selection only when a measurable-selection theorem applies;
- use approximation plus certified error bounds;
- use interval or rational enclosure where numerical artifacts appear;
- track whether dependent choice is enough.

Redirection rule:

If a statement uses arbitrary subsets of the continuum, MATHSOLVE should attempt a regularization pass before proof search:

```text
arbitrary subset -> finite / Borel / measurable / compact / convex / definable / intentionally arbitrary
```

### R3: classical-choice-marked route

Use when the proof probably needs full choice or classical maximality.

Triggers:

- Zorn's lemma;
- arbitrary bases of vector spaces;
- ultrafilters;
- non-principal filters;
- unrestricted Tychonoff products;
- full Hahn-Banach;
- maximal ideals in arbitrary rings;
- unrestricted selectors over uncountable quotients.

The route is valid only if the solver output marks:

```yaml
choice_usage: full_choice
constructive_content: nonconstructive | unknown
witness_extractability: not_expected | unknown
```

### R4: foundations-sensitive route

Use when the problem is actually about axioms, independence, determinacy, large cardinals, forcing, or regularity of arbitrary sets of reals.

Preferred tactics:

- separate theorem from consistency claim;
- state base theory explicitly;
- avoid importing ZFC and AD simultaneously unless relative context is declared;
- mark all large-cardinal or determinacy assumptions;
- produce a consistency-strength note rather than a false ordinary proof.

### R5: under-specified route

Use when the statement cannot yet be solved because the carrier, operations, regularity, or axiom profile is missing.

MATHSOLVE may still produce useful work, but the output must be a clarification artifact:

```yaml
solver_output:
  route: under-specified
  blocked_by:
    - missing_ambient_structure
    - missing_regular_sigma_algebra
    - missing_choice_policy
  proposed_refinements: []
```

## Routing table

| Foundational texture | Route | Preferred evidence |
| --- | --- | --- |
| finite, decidable, bounded | R0 finite-computable | enumeration, SAT/SMT/PB, small verifier |
| explicit construction needed | R1 constructive-witness | algorithm, witness, proof term |
| Borel/measurable/compact/convex/separable | R2 regular-analytic | regular theorem + certified approximation |
| full choice or maximality likely | R3 classical-choice-marked | classical proof with choice audit |
| axioms/independence/determinacy | R4 foundations-sensitive | relative theorem or consistency note |
| missing carrier/structure | R5 under-specified | clarification/refinement artifact |

## Solver output extension

All MATHSOLVE outputs should add:

```yaml
foundation_routing:
  selected_route: R0 | R1 | R2 | R3 | R4 | R5
  route_reason: ""
  foundational_profile_used: true | false
  regularization_attempted: true | false
  choice_audit:
    status: none_detected | weak_choice | dependent_choice | full_choice | unknown
    notes: ""
  constructive_content:
    status: explicit | extractable | nonconstructive | contradiction_only | unknown
    notes: ""
  certificate_boundary:
    target: Lean | Coq | SAT | SMT | PB | CAS | interval | human_audit | none | unknown
    checker_inputs: []
```

## Failure modes

MATHSOLVE should reject or downgrade route confidence when:

- convexity is used without an affine/vector-space ambient;
- measure is used without a sigma-algebra;
- probability is used without measurable events;
- compactness is used without topology and compactness hypothesis;
- arbitrary choice is used but `choice_usage` is left unknown;
- existence is claimed without witness policy;
- numerical evidence is treated as proof without interval/certificate boundary;
- a foundations-sensitive claim is routed as ordinary analysis.

## Grand Challenge invariant

MATHSOLVE is responsible for preserving:

```text
structured object -> route discipline -> evidence boundary
```

The solver should not merely try to solve. It should make explicit what kind of mathematical universe the solution inhabits and what kind of artifact could certify it.

# Groebner Tactic Orchestration

## Purpose

This lane tells MATHSOLVE when to invoke polynomial algebra as a tactic. It is not a certificate checker and it is not a symbolic-algebra backend. It is the strategic layer that recognizes a useful algebraic subproblem, requests or consumes a witness, and routes the resulting obligation toward MATHCERT.

The doctrine is:

> MATHSOLVE may use a witness. MATHCERT must certify it.

## Programme links

Read this tactic lane through the programme front door and the shared doctrine pages:

- [MATH-PROGRAMME Pages home](https://grandchallenge.github.io/MATH-PROGRAMME/)
- [Programme Atlas](https://grandchallenge.github.io/MATH-PROGRAMME/PROGRAMME_ATLAS/)
- [MATHSOLVE pillar doctrine](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/MATHSOLVE_SPEC.md)
- [Cross-pillar lanes](https://grandchallenge.github.io/MATH-PROGRAMME/CROSS_PILLAR_LANES/)
- [Computational Algebraic Geometry Lane](https://grandchallenge.github.io/MATH-PROGRAMME/COMPUTATIONAL_ALGEBRAIC_GEOMETRY_LANE/)
- [Groebner and EXPSPACE doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/GROEBNER_EXPSPACE_DOCTRINE/)
- [Claim-boundary doctrine](https://grandchallenge.github.io/MATH-PROGRAMME/CLAIM_BOUNDARY_DOCTRINE/)
- [Resource Budget Policy](https://grandchallenge.github.io/MATH-PROGRAMME/RESOURCE_BUDGET_POLICY/)

## When to invoke the lane

A proof step is a candidate for the Groebner orchestration lane when it can be rewritten as one of the following tasks:

- polynomial identity checking;
- normal-form or remainder verification;
- ideal membership;
- ideal equality;
- elimination of auxiliary variables;
- radical membership;
- algebraic branch pruning;
- finite-truncation checks for a growing family of polynomial systems.

## Inputs

A tactic invocation should record:

- the parent problem or work package;
- the local proof obligation;
- the intended algebraic task;
- coefficient domain;
- variables and index structure;
- side conditions;
- proposed backend or witness source;
- whether MATHFORGE should generate a witness;
- the expected MATHCERT certificate kind.

## Outputs

A successful invocation should produce one of:

- a request to MATHFORGE for witness generation;
- a direct handoff to MATHCERT using an existing witness;
- a certified local lemma once MATHCERT checks the artifact;
- a tactical failure record explaining why the algebraic route was inappropriate.

## Trust boundary

MATHSOLVE must never promote an external CAS result to a proof. The allowed statuses are:

| Status | Meaning |
| --- | --- |
| `candidate` | The subproblem appears algebraic. |
| `witness_requested` | MATHFORGE should generate an artifact. |
| `witness_available` | A candidate witness exists. |
| `sent_to_mathcert` | The artifact has been routed for checking. |
| `certified_by_mathcert` | MATHCERT returned or merged a checked certificate. |
| `rejected` | The tactic should not be used for this obligation. |

Only `certified_by_mathcert` may be treated as a solved proof step.

## Relationship to the other pillars

```text
MATHFORGE  discovers and exports candidate witnesses.
MATHSOLVE  chooses tactics and routes obligations.
MATHCERT   checks certificates and owns the proof boundary.
```

This separation keeps search, tactic choice, and certification from collapsing into one untrustworthy black box.

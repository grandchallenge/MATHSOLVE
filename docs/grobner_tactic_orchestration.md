# Groebner Tactic Orchestration

## Purpose

This lane tells MATHSOLVE when to invoke polynomial algebra as a tactic. It is not a certificate checker and it is not a symbolic-algebra backend. It is the strategic layer that recognizes a useful local algebraic obligation, requests or consumes a witness, and routes the resulting packet toward MATHCERT.

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

## Admission contract

Every governed invocation must use `schemas/grobner_tactic_invocation.schema.json`, version `0.2.0`, and must be registered in `governance/grobner_tactic_registry.json` by exact Git blob identity.

The record must include:

- the parent problem and one local proof obligation;
- a concrete explanation of why the obligation is local and algebraic;
- `global_open_problem_encoding: false`;
- coefficient domain, variables, variable count, and side conditions;
- maximum variables, degree, runtime, basis size, and intermediate-term count;
- a named fallback route and its trigger conditions;
- the exact witness expected and what MATHCERT must check;
- a content-addressed witness source when a witness is available;
- MATHCERT intake and output identities at the correct lifecycle stages;
- a failure record for rejected or proof-debt routes.

## Permitted route states

| State | Meaning |
| --- | --- |
| `candidate` | A local algebraic route has been proposed. |
| `witness_requested` | MATHFORGE or another governed source has been asked for a witness. |
| `witness_available` | A content-addressed witness exists. |
| `ready_for_mathcert` | The packet is complete inside MATHSOLVE but has not been accepted by MATHCERT. |
| `submitted` | MATHCERT has acknowledged intake but has not adjudicated the claim. |
| `certified` | MATHCERT issued a content-addressed certified disposition. |
| `qualified` | MATHCERT issued a content-addressed qualified disposition. |
| `rejected` | MATHCERT rejected the exact claim or packet. |
| `proof_debt` | MATHCERT closed the route with explicit unresolved proof debt. |

`ready_for_mathcert` and `submitted` are intake states. They are not completed dispositions. Only `certified` and `qualified` support positive promotion.

## Fail-closed rules

The validator rejects:

- unregistered or missing tactic records;
- changed records at unchanged registry identities;
- global open-problem encodings;
- missing local-scope justification, budgets, fallback routes, or expected witnesses;
- variable counts beyond the declared budget;
- witness-dependent states without a content-addressed witness;
- submitted or adjudicated states without MATHCERT intake acknowledgement;
- adjudicated states without a content-addressed MATHCERT output;
- intake states that claim a MATHCERT output;
- rejected or proof-debt routes without failure evidence.

## Relationship to the other pillars

```text
MATHFORGE  generates bounded, provenance-rich candidate witnesses.
MATHSOLVE  chooses the local tactic, budget, fallback, and Cert obligation.
MATHCERT   independently checks the certificate and owns adjudication.
```

An external CAS result, a serialized witness, a ready packet, a submitted packet, or green Solve CI is not mathematical certification.

# OPENMATH-2026 obligation template

Instantiate this template only after an exact Forge source lock exists.

## S0 — semantic fidelity

- What exact theorem does the hill state?
- What definitions, quantifiers, ambient categories, coefficient fields, regularity hypotheses, or parameter ranges are theorem-critical?
- What nearby theorem would be easier but non-equivalent?
- What must be compared between informal and formal statements?

Completion: an exact statement correspondence ledger, not merely a formal theorem name.

## S1 — formalization prerequisites

Identify existing library objects, missing APIs, imported theorems, axioms, and environment/version pins.

Completion: the target can be expressed without hidden mathematical imports.

## R1 — representation / reduction

Search for normal forms, equivalent formulations, quotient structures, finite reductions, symmetry reductions, algebraic encodings, or invariant coordinates.

Completion: either a justified reduction or a recorded failed route.

## R2 — restricted theorem

Seek an independently meaningful special case, local lemma, finite regime, parameter slice, or strengthened-hypothesis theorem.

Completion: precise statement plus proof/certificate or a named blocker.

## R3 — exact computation

Use exact enumeration, rational arithmetic, SAT/SMT, proof-producing CAS, interval arithmetic, or other replayable computation where suitable.

Completion: minimized exact witness plus independent replay path. Numerical evidence alone does not complete this obligation.

## R4 — falsification / counterexample

Try to break candidate lemmas, reductions, implicit assumptions, generated conjectures, and formal encodings.

Completion: exact counterexample or a bounded falsification report with scope.

## R5 — zero-context CEI contribution

Dispatch only a fully self-contained bounded subproblem. Require one RESULT/1 object. Preserve raw return and receipt before adjudication.

Completion: preserved external evidence plus separate GCL adjudication. Intake does not equal acceptance.

## C1 — MATHCERT handoff

For each surviving claim provide:

- exact claim text;
- source/hill identity;
- exact producer artifact;
- dependency and axiom ledger;
- replay instructions;
- semantic-fidelity risks;
- producer/authorship provenance;
- acceptance and rejection criteria;
- requested certification modality.

Completion: MATHCERT receives a content-addressed packet. Solve does not mark it certified.

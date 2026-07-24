# NS-CI-WP04 — Restricted theorem target formulation

## Status

- Campaign: `NS-CI-001`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#61`
- MATHSOLVE tracker: `grandchallenge/MATHSOLVE#22`
- State: `AWAITING_MATHFORGE_SHORTLIST`
- Selection limit: at most one target

## Purpose

Convert the MATHFORGE prior-art shortlist into exact theorem statements, proof-obligation DAGs, and Council scorecards. Return one selected `NS-CI-R014` target or an explicit no-selection decision.

## Required theorem record

Each candidate must specify:

- exact domain, forcing, viscosity, data class, solution class, and quantifiers;
- added hypothesis and scaling class;
- exact conclusion for `I_T` or a quantitatively adjacent bound;
- strict-restriction argument showing the hypothesis is weaker than assuming regularity;
- WP01 fixture clearance;
- WP02 dependencies among `CR-000` through `CR-011`;
- proof-obligation DAG;
- strongest failure mode;
- falsification protocol;
- formalization boundary;
- score rationale.

## Proof-obligation template

```text
Definitions and scaling
  -> hypothesis is independently meaningful
  -> local estimate or structural inequality
  -> scale-uniform closure
  -> finite critical integral or adjacent continuation bound
  -> WP02 conditional theorem interface
```

Every arrow must name the estimate or imported theorem that supports it.

## Hard rejection conditions

Reject a candidate if:

- it assumes `L^4_tL^6_x`, uniform `H^1`, or an equivalent continuation norm;
- it depends on a cutoff or smoothing constant that diverges without compensation;
- it silently changes the full data or universal solution quantifier;
- it is already classical in the exact stated form;
- its proof DAG contains an unnamed analytic leap;
- its only falsification route is unverified numerical behavior.

## Council score dimensions

Score 0–5 with written rationale for leverage, non-circularity, prior-art distance, scale compatibility, tractability, formalizability, falsifiability, full-problem relevance, information value if false, and execution cost.

## Current decision

No theorem statement is selected at initialization. MATHSOLVE begins exact formulation only after MATHFORGE returns a source-backed shortlist.
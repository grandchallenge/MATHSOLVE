# RSI-CCC-001 / M1 — One proved guarded self-replacement step

## Identity

- Campaign: `RSI-CCC-001`
- MATHSOLVE issue: `#248`
- Provider work package: `MS-RSI-CCC-WP01`
- Primary type: `FORMALIZATION_HANDOFF`
- Upstream INTELLECT issue: `grandchallenge/INTELLECT#103`
- Frozen M0 integration: `grandchallenge/INTELLECT@18ded6c7d8bc491c63d247f7a71899e4e2f7bf07`
- Frozen formal-object SHA-256: `1fca7a5e5bba2f4b59ccf9288a6a01129652091f86071c7be70022ea076d0edc`

## Purpose

M1 asks for one theorem-grade result:

> A single admitted replacement step, represented in the frozen guarded model and accepted under the fixed trust-kernel assumptions, preserves the declared invariant.

This package is theorem-first. It does not construct an RSI agent, a learned proposer, model-weight self-modification, AETHER integration, or a production runtime.

## Frozen model boundary

The ambient model is the stage-indexed presheaf presentation of `Set^(omega^op)`. M1 does not claim that the ambient category is order-enriched.

The four layers are separate:

1. ambient guarded Cartesian-closed semantics;
2. intrinsically typed syntax and interpretation;
3. an external certified refinement preorder on an explicit represented-program/morphism domain;
4. a fixed checker/admission trust kernel.

Any theorem requiring a material change to that boundary stops the route and returns to INTELLECT for a new formal-object digest and M0 review.

## Proof order

The proof is developed in this order:

1. `CCC`: stage objects, natural transformations, products, Kripke exponential, evaluation, currying;
2. `Guarded`: `Later`, `next`, guarded fixed point;
3. `Reflection`: typed syntax, quotation, interpretation, adequacy;
4. `Refinement`: preorder and scoped compatibility laws;
5. `Admission`: one-step preservation under explicit trust-kernel hypotheses;
6. `Iteration`: guarded productive trace, only after step 5 closes.

## Current implementation tranche

The first Lean tranche constructs the direct stage-indexed substrate, products, `Later`, `next`, and a guarded fixed-point section. It intentionally does not mark the CCC, reflection, refinement, or admission claims complete until their theorem files exist and `lake build` checks them.

## Reproducibility lock

Use the repository toolchain unchanged:

- Lean `v4.29.1`;
- mathlib commit `5e932f97dd25535344f80f9dd8da3aab83df0fe6`.

## Certification boundary

MATHSOLVE constructs and checks the proof artifact. It does not certify the claims. Claim-bearing completion requires an exact MATHCERT handoff and an independent MATHCERT disposition.

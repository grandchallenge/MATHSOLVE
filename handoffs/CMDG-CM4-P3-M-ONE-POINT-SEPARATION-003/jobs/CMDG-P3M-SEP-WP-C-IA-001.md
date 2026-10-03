GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: CMDG-P3M-SEP-WP-C-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-C
campaign: CMDG-CM4
work_package: P3-M-ONE-POINT-SEPARATION-003
assignment: CMDG-P3M-SEP-WP-C
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: https://github.com/grandchallenge/MATHSOLVE/issues/766

# WP-C — adversarial invisible-section search

You are an independent adversarial zero-context mathematical contributor. This document is the complete bounded work-set.

Timebox: 35 minutes of substantive work, then return the strongest exact result reached.

## Protected packet

The following facts are source-locked from protected `grandchallenge/MATH-PROGRAMME/main` at `f7f99e18b83a3015d1a7ef835ee71434d01a9dba`.

Mathematical setting:

- `R` is the pinned lifted-integer coefficient ring used by the CMDG CM4 campaign.
- `X : Profinite`.
- `coefficientObject : CondensedMod R` is the discrete lifted-integer coefficient object.
- `Point := CompHaus.of PUnit`.
- A solid-side morphism has type
  `d : (Condensed.profiniteSolid R).obj X ⟶ coefficientObject`.
- The kernel hypothesis is
  `(Condensed.profiniteSolidification R).app X ≫ d = 0`.

Already protected interfaces:

1. `coefficient_hom_ext_point`: two morphisms into `coefficientObject` are equal if their components at `op Point` are equal. Thus the authorized target after this tranche is the one-point component, not `d = 0` directly.
2. `measurePointProjection`, `measurePointProjectionLinear`, `measurePointFunctional`, and `measurePointIntegralFunctional` turn a one-point measure section into an ordinary scalar/integral functional.
3. `integralBasis X` is the chosen Nöbeling basis of `LocallyConstant X ℤ`.
4. `kernelProductSection` and `kernelProductFunctional` are the protected weighted-Boolean product interfaces.
5. Protected finite-coordinate dependence is available for `kernelProductFunctional`.

Protected predecessor admission:

- MATH-PROGRAMME PR #919 was admitted through the native merge queue at protected main `f7f99e18b83a3015d1a7ef835ee71434d01a9dba`.
- Protected source file:
  `fixtures/formal/CMDG-NAT-CONCORDANCE-001/CMDGCondensedCM4P3GPointFunctional.lean`,
  blob `1f867034ec1474418cf416ee8583449bcbe80ee5`.
- Admitted endpoint:
  `kernelProductFunctional_eq_zero_of_solidification_kernel`, proving from the kernel hypothesis that
  `kernelProductFunctional X d = 0`.
- Exact merge-group axiom readback for the admitted endpoint is
  `[propext, Classical.choice, Quot.sound]`; no `sorryAx` appears.

The successor question is separation: whether zero product-functional data forces the one-point component of `d` to vanish.

## Independence and authority

This dispatch belongs to blind cohort `CMDG-P3M-SEP-BLIND-COHORT-001`. Do not inspect other cohort returns, campaign discussion threads, pull requests, or unpublished notes. Use only this packet plus standard mathematics.

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. A counterexample, reduction, or exact blocker is a successful return if correct.

## Required return

Post exactly one narrative-only comment on `INTENDED_RETURN`:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <exact dispatch id>
agent_ref: <exact agent ref>
assignment: <exact assignment>
disposition: <PROVED_REDUCTION|EXACT_CERTIFICATE|FORMAL_LEMMA_PROVED|COUNTEREXAMPLE|NO_MATERIAL_DELTA|EXACT_BLOCKER>
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: <YES|NO>

## Strongest exact statement
<Exact theorem, counterexample, reduction, or blocker.>

## Derivation
<Complete checkable argument. If code is used, include the smallest replayable code inline.>

## Assumptions beyond bootstrap
<List every extra assumption, or NONE.>

## Verification / falsification hooks
<Concrete checks another reasoner can perform.>

## Claim boundary
<State exactly what follows and what does not. No certification claim.>

## Next residual
<At most three sentences.>
```

No URLs, attachments, side files, branches, pull requests, or second mathematical comment. The first valid conforming return is the durable contribution. Intake preserves evidence only.

## Exact assignment

Attack the separation claim.

Try to construct, characterize, or rule out a nonzero
`μ : (measurePresheafObj X).obj (op Point)`
such that every currently used observable vanishes. Candidate invisibility conditions include:

- `measurePointFunctional X μ = 0`;
- `measurePointIntegralFunctional X μ = 0`;
- all basis coordinates
  `measurePointIntegralFunctional X μ (integralBasis X i)`
  vanish;
- all weighted-Boolean/Nöbeling probes used by `kernelProductFunctional` vanish.

Your task is to identify the earliest interface where a nonzero kernel could exist.

If a counterexample exists, give the smallest explicit algebraic/categorical model compatible with the protected packet and identify exactly which desired implication fails.

If no counterexample can exist because an interface is injective for a simple structural reason, prove that reason rather than merely reporting failure to find an example.

## Required adversarial coverage

Check separately:

1. projection from the enriched one-point section;
2. restriction to constant families on `PUnit`;
3. evaluation at the unique point;
4. lifted-integer descent;
5. basis-coordinate observation;
6. weighted-family realization.

The strongest useful negative result is a concrete nonzero invisible direction. The strongest useful positive result is a proof that a suspected kernel is necessarily trivial.

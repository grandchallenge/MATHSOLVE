> **STAGED / NON-EXECUTABLE.** This canonical job is prepared for the successor of MATH-PROGRAMME #664 but is not an active launch. Do not execute it until a protected `GCL-ZERO-CONTEXT-LAUNCH/2` artifact is published after #664 exact-head review, protected admission, and protected-main readback. The activation commit must replace the candidate predecessor below with the admitted protected SHA.

GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: CMDG-P3M-SEP-WP-D-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-D
campaign: CMDG-CM4
work_package: P3-M-ONE-POINT-SEPARATION-003
assignment: CMDG-P3M-SEP-WP-D
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: https://github.com/grandchallenge/MATHSOLVE/issues/767

# WP-D — audit information preservation across the one-point interfaces

You are an independent zero-context mathematical contributor. This document is the complete bounded work-set.

Timebox: 30 minutes of substantive work, then return the strongest exact result reached.

## Protected packet at activation

The activation commit must source-lock these facts from protected `grandchallenge/MATH-PROGRAMME/main`.

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

Candidate predecessor awaiting admission:

- MATH-PROGRAMME PR #919 exact candidate head: `cff36869559e52eb5440dfc3b00cefa27648ae4e`.
- Candidate endpoint:
  `kernelProductFunctional_eq_zero_of_solidification_kernel`, proving from the kernel hypothesis that
  `kernelProductFunctional X d = 0`.
- This candidate is NOT an admissible premise until the activation commit records the protected merge/readback SHA.

The successor question is separation: whether zero product-functional data forces the one-point component of `d` to vanish.

## Independence and authority

This dispatch belongs to blind cohort `CMDG-P3M-SEP-BLIND-COHORT-001`. Do not inspect other cohort returns, campaign discussion threads, pull requests, or unpublished notes. Use only this packet plus standard mathematics.

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. A counterexample, reduction, or exact blocker is a successful return if correct.

## Required return

After activation, post exactly one narrative-only comment on `INTENDED_RETURN`:

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

Produce a typed information-preservation ledger for the chain

`one-point measure section`
→ `measurePointProjection`
→ `measurePointProjectionLinear`
→ `measurePointFunctional`
→ `measurePointIntegralFunctional`
→ `Nöbeling basis coordinates`
→ `weighted-Boolean realization / kernelProductFunctional`.

For every arrow, classify it as one of:

- definitional equivalence;
- proved injective;
- proved surjective;
- proved bijective/equivalence;
- only a map, with no protected injectivity;
- type/coefficient change requiring a named lemma.

For every claimed injective/equivalent arrow, give a checkable proof argument from the packet and standard mathematics.

Then identify the FIRST arrow for which information preservation is not justified. Formulate the smallest theorem that would close that arrow. If all arrows through basis coordinates are injective, say so and isolate the remaining weighted-family comparison as the sole residual.

## Claim boundary

This is an interface audit, not a proof of #1162 unless the chain actually closes. Do not infer institutional certification or downstream CM4 consequences.

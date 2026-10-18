# CMDG P3-M SEP2 — independent synthesis and selection

Status: SYNTHESIS_COMPLETE__POINT_RECONSTRUCTION_CONVERGENCE

Cohort: `CMDG-P3M-SEP2-BLIND-COHORT-001`

Protected evidence base: `45146308ae22729decc4fd8ca61e8bbd7e952602`

Admitted returns: WP-B, WP-C, WP-D.

Terminally disposed and excluded from synthesis: WP-A, because its RESULT/1 preceded valid worker-reservation provenance. Its preserved text has no mathematical evidence effect.

## Cross-return synthesis

The three admissible zero-context returns converge on the same representation boundary.

- **WP-B** gives the constructive formulation: every Point measure section should be recovered from the canonical weight vector
  `i ↦ measurePointIntegralFunctional X μ (integralBasis X i)`.
  Equivalently, the weighted all-true Point-measure construction is surjective.

- **WP-C** reaches the same boundary categorically: the weighted Point sections must generate the Point component. Combined with the protected `coefficient_hom_ext_point`, this is enough to make the product-functional representation faithful for coefficient-valued morphisms.

- **WP-D** performs the adversarial check. It finds no protected-type counterexample, proves that the protected weight code is injective, and isolates the same reconstruction/surjectivity statement as the only remaining faithfulness boundary.

These independent returns therefore select **Point reconstruction by weighted Nöbeling/Boolean probes** as the preferred representation. Direct `CoefficientFiniteStageMappingOut` remains an equivalent characterization but is not required as the primary proof route.

## Native-state comparison

Subsequent protected Programme development discharges exactly the selected reconstruction theorem:

`weightedFiniteBooleanMeasureLimitLift_measurePoint_allTrue`.

The terminal Programme candidate PR #1210, exact head
`5c33a658a2a49d11f7db6b10ea71493d33c2610f`, then proves the downstream chain

`applied_d_point_kernelProductFunctional`
→ `coefficient_eq_zero_of_solidification_kernel`
→ `coefficientMappingOutInjectivity_of_pointFunctional`
→ `coefficientObject_isSolid_via_pointFunctional`.

At synthesis time #1210 has passed exact-head formal validation and non-author specialist review and is routed through the repository merge queue. This Solve synthesis does not itself certify or admit the Programme theorem.

## Selection

Selected route: **Point-functional reconstruction / weighted-measure probe faithfulness**.

Deprioritized route: direct finite-stage recovery as the primary proof mechanism.

Adversarial outcome: no counterexample in the protected interface; the only substantive risk identified by the admissible blind returns was failure of Point reconstruction, which the native Programme development subsequently discharged.

## Claim boundary

This document records cross-return convergence and route selection only. It does not certify coefficient solidity, P3 completion, CM4 completion, or any downstream theorem. Protected mathematical admission remains controlled by the Programme repository.

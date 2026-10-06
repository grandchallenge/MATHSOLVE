# CMDG P3-M separation WP-A — direct Point recovery

Protected Programme: grandchallenge/MATH-PROGRAMME@1a086db26b8f383d6d320edc545df9581fe6a72f

Read only these protected source files before reasoning:
- fixtures/formal/CMDG-NAT-CONCORDANCE-001/CMDGCondensedCM4P3G.lean
- fixtures/formal/CMDG-NAT-CONCORDANCE-001/CMDGCondensedCM4P3LKernelFunctional.lean
- fixtures/formal/CMDG-NAT-CONCORDANCE-001/CMDGCondensedCM4P3MFiniteQuotientBridge.lean
- fixtures/formal/CMDG-NAT-CONCORDANCE-001/CMDGCondensedCM4P3GPointFunctional.lean

Protected facts you may use:
- coefficient_hom_ext_point
- kernelProductFunctional_finite_coordinate_dependence
- kernelProductFunctional_eq_zero_of_solidification_kernel
- weighted finite-quotient Dirac/evaluation identities and global measure-limit assembly in the files above.
- CoefficientFiniteStageMappingOut is equivalent to the old residual, but you are NOT required to prove it.

Claim boundary: contributor evidence only. No solidity, P3, or CM4 completion is certified by your return.
Return exactly one GCL-CONTRIBUTION-RESULT/1 comment on the bound issue.

Mission:
Given X and d : (Condensed.profiniteSolid R).obj X ⟶ coefficientObject, attack the implication

  kernelProductFunctional X d = 0
  →
  d.hom.app (op Point) = 0.

Prefer the weakest exact statement that closes via coefficient_hom_ext_point. Work in actual protected types. You may use Nöbeling basis separation, Point evaluation, measure-point projections, and existing weighted Dirac identities.

Success dispositions:
FORMAL_LEMMA_PROVED | PROVED_REDUCTION | EXACT_BLOCKER | COUNTEREXAMPLE | NO_MATERIAL_DELTA.

If full closure fails, identify the smallest Lean-sized missing lemma and why existing protected theorems do not imply it.

Required header:
GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-SEP2-WP-A-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-P3M-SEP2-A
assignment: CMDG-P3M-SEP2-WP-A
disposition: <PROVED_REDUCTION|EXACT_CERTIFICATE|FORMAL_LEMMA_PROVED|COUNTEREXAMPLE|NO_MATERIAL_DELTA|EXACT_BLOCKER>
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: <YES|NO>

## Strongest exact statement
...

## Derivation
...

## Assumptions beyond bootstrap
...

## Verification / falsification hooks
...

## Claim boundary
...

## Next residual
...

GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-COV-WP-A-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-COV-A
assignment: CMDG-P3M-COV-WP-A
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

There is a canonical protected-type all-true section. Let P := Profinite.of PUnit and qtrue := basisBooleanPointProbe X (fun _ => true). Define weightedAllTrueSection X a to be the section corresponding under freeHomSectionsEquiv P (CMDG.CondensedCM4P2D.measureFunctor.obj X) to

(Condensed.profiniteFree R).map qtrue ≫ weightedFiniteBooleanMeasureLimitLift X a.

Its resulting type is (measurePresheafObj X).obj (op Point), using the protected identification of the one-point profinite object with Point.

For aμ i := measurePointIntegralFunctional X μ (integralBasis X i), the requested projection equality reduces to one normalization lemma:

for every a and every integral-basis index i,
measurePointIntegralFunctional X (weightedAllTrueSection X a) (integralBasis X i) = a i.

Call this ALLTRUE-BASIS.

If ALLTRUE-BASIS holds, then

measurePointProjection X (weightedAllTrueSection X aμ) =
  measurePointProjection X μ,

and, using measurePointProjection_zero_reflects plus additivity of the projection in the section variable, one further obtains

weightedAllTrueSection X aμ = μ.

The protected packet does not contain ALLTRUE-BASIS or an equivalent theorem. In particular, weightedFiniteBooleanMeasureLimitLift_point_reweight does not imply it: that theorem compares a selected Boolean point for weights a with the all-true point for selector-reweighted weights, but it never fixes the normalization of the all-true measure against an integral basis vector. Thus the theorem-grade projection identity is reduced, but not discharged, by the protected material supplied here.

## Derivation

First, measurePointFunctional loses no information from measurePointProjection. The projected map has type

LocallyConstant Point (LocallyConstant X R) →ₗ[R] LocallyConstant Point R.

Because Point is the singleton PUnit, every source family is constant and every target family is determined by evaluation at PUnit.unit. Consequently precomposition with LocallyConstant.constₗ R and postcomposition with LocallyConstant.evalₗ R PUnit.unit are linear equivalences on the relevant singleton factors. Equality of measurePointFunctional values therefore forces equality of the projected linear maps, hence equality of measurePointProjection.

Second, the passage to measurePointIntegralFunctional is information-preserving at these protected types. R is the lifted integer coefficient ring used throughout this branch, and liftedIntFunctionalDown is the down-transport to integer-valued locally constant functions. Pointwise ULift up/down gives the inverse reconstruction: every LocallyConstant X R function is the lift of its pointwise-down integer function. Hence equality of the down-transports determines equality of the R-linear functionals.

Third, the Nöbeling coordinates lose no information. If F and G are ℤ-linear functionals on LocallyConstant X ℤ and F (integralBasis X i) = G (integralBasis X i) for every i, basis extensionality gives F = G. Thus, assuming ALLTRUE-BASIS,

measurePointIntegralFunctional X (weightedAllTrueSection X aμ)
= measurePointIntegralFunctional X μ.

The previous two injectivity observations then give the requested equality of measurePointProjection.

Fourth, the finite-to-global weighted lift itself introduces no additional ambiguity in the family it constructs: weightedFiniteBooleanMeasureLimitLift is the canonical lift through the protected finite-quotient limit, and its protected fac identity recovers every finite weighted stage. The remaining issue is not uniqueness of the global lift; it is the missing computation identifying the all-true one-point realization with the prescribed coordinate functional.

Finally, once the two projections agree, let δ := weightedAllTrueSection X aμ - μ. Linearity of the one-point projection gives measurePointProjection X δ = 0. The protected measurePointProjection_zero_reflects theorem then gives δ = 0, hence full section reconstruction.

## Assumptions beyond bootstrap

Only standard mathematics implicit in the protected types is used: locally constant functions on a singleton are constant; evaluation at the unique point is injective; ULift up/down is an equivalence; a basis determines a linear map; and additive linear maps preserve subtraction.

No mapping-out injectivity, coefficient solidity, P3 completion, CM4 completion, or promotion from the parent target is assumed.

## Verification / falsification hooks

1. measurePointFunctional: verify directly that any h : LocallyConstant Point (LocallyConstant X R) satisfies h = LocallyConstant.const Point (h PUnit.unit), and similarly for the target. This proves the singleton restriction/evaluation is lossless.

2. measurePointIntegralFunctional: verify the inverse transport explicitly by pointwise ULift.up after pointwise ULift.down. A counterexample here would require two distinct R-linear functionals agreeing on every lifted integer-valued locally constant function; pointwise ULift surjectivity rules that out.

3. Basis coordinates: test the standard basis-extensionality statement for integralBasis X. No extra analytic or finiteness hypothesis is needed.

4. Weighted finite-to-global lift: for each finite quotient j, check the protected fac equality. Any proposed failure of reconstruction must already appear in the finite-stage all-true evaluation or in its passage to the point section, not in uniqueness of the limit lift.

5. All-true realization: this is the decisive hook. Prove or falsify, for arbitrary a and i,

measurePointIntegralFunctional X (weightedAllTrueSection X a) (integralBasis X i) = a i.

A sharper unit test is to take a to be a one-coordinate vector: the all-true section should evaluate to 1 on that basis vector and 0 on every other basis vector. The protected selector-reweight identity may be used to move arbitrary Boolean selectors into the weight vector, but it cannot replace this normalization check.

## Claim boundary

This return proves only the reduction of canonical weighted reconstruction to ALLTRUE-BASIS and the consequent implication from that lemma to the requested one-point projection equality and then to section reconstruction.

It does not claim ALLTRUE-BASIS has already been formalized, does not claim the parent d.hom.app (op Point) target, and does not promote to d = 0, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion.

## Next residual

Prove ALLTRUE-BASIS at the protected types. The shortest route is to fix i, descend integralBasis X i through a finite quotient on which it is locally constant, compute the finite weighted coefficient/measure pairing at qtrue, use the defining Nöbeling coordinate pairing to obtain exactly a i, and transport that equality through weightedFiniteBooleanMeasureLimitLift_fac and freeHomSectionsEquiv_precomp to the one-point section. If that finite calculation produces any coefficient other than a i, that calculation is the required concrete protected-type counterexample.
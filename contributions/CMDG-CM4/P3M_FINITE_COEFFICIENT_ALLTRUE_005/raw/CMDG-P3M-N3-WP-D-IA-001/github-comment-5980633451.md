GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-N3-WP-D-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-N3-D
assignment: CMDG-P3M-N3-WP-D
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The weakest sufficient downstream bridge can be stated at strength 1: equality only after applying the Point component of d.

Let aμ be the weight vector
    fun i => measurePointIntegralFunctional X μ (integralBasis X i)
and let E_X be
    CMDG.CondensedCM4P2E.CanonicalRightKanUniqueness.measureProfiniteSolidNatIso.hom.app X.

The minimal sufficient compatibility statement is the scalar identity

    theorem applied_d_point_kernelProductFunctional
        (X : Profinite.{u})
        (d : (Condensed.profiniteSolid R).obj X ⟶ coefficientObject)
        (μ : (measurePresheafObj X).obj (op Point)) :
        ((((d.hom.app (op Point))
            ((E_X.hom.app (op Point)) μ)) PUnit.unit).down) =
          kernelProductFunctional X d
            (fun i =>
              measurePointIntegralFunctional X μ (integralBasis X i))

with E_X expanded in the actual declaration.

Together with
    kernelProductFunctional X d = 0
this implies exactly
    d.hom.app (op Point) = 0.

No equality of global morphisms into coefficientObject is required.

## Derivation

Write P := Profinite.of PUnit, qtrue := basisBooleanPointProbe X (fun _ => true), and aμ as above.

N3 gives, for every finite quotient j and quotient point q,

    weightedFiniteBooleanCoefficient X aμ j q (fun _ => true) =
      measurePointFunctional X μ (finiteDeltaPullbackR X j q).

By finite coordinate extensionality this determines the all-true pullback of the weighted finite coefficient family.

The first genuinely unprotected arrow is

    FINITE_COEFFICIENT_FAMILY_RECONSTRUCTION
    → FINITE_MEASURE_SECTION_REALIZATION

and it can be isolated at the exact protected types as the following Lean-sized proposition:

    theorem weightedFiniteBooleanMeasureSection_allTrue_realizes_pushforward
        (X : Profinite.{u})
        (μ : (measurePresheafObj X).obj (op Point))
        (j : DiscreteQuotient X) :
        (ConcreteCategory.hom
          ((measurePresheafObj (X.diagram.obj j)).map
            ((profiniteToCompHaus).map
              (basisBooleanPointProbe X (fun _ => true))).op))
          (weightedFiniteBooleanMeasureSection X
            (fun i =>
              measurePointIntegralFunctional X μ (integralBasis X i)) j)
          =
        ((CMDG.CondensedCM4P2D.measureFunctor.map
          (finiteQuotientMap X j)).hom.app (op Point)) μ

Its proof needs no new global theorem. Transport the left side through the protected finiteMeasurePresheafFamilyIso and finiteFamilyInternalHomIso; use weightedFiniteBooleanMeasureSection_coefficientFamily_transport; then use N3 coordinatewise. The right side has the same finite coordinate family by the protected finite dual/source-family decomposition and the definition of measurePointFunctional.

Once this section theorem is available, the older finite-stage morphism equality

    μHom ≫ measureFunctor.map (finiteQuotientMap X j) =
      (Condensed.profiniteFree R).map qtrue ≫
        weightedFiniteBooleanMeasureHom X aμ j

is not mathematically necessary as a separate bridge. It is the image of the finite section equality under the inverse of freeHomSectionsEquiv. Thus full finite measure-morphism realization is avoidable packaging.

For every j, combine the finite section realization with the protected weightedFiniteBooleanMeasureLimitLift_fac. A single (measureFunctorMapConeIsLimit X).hom_ext argument then gives the global one-point coverage identity

    (freeHomSectionsEquiv P
      (CMDG.CondensedCM4P2D.measureFunctor.obj X)).symm μ
    =
    (Condensed.profiniteFree R).map qtrue ≫
      weightedFiniteBooleanMeasureLimitLift X aμ.

This is the only genuinely new limit/hom-ext step.

Postcompose this equality with E_X ≫ d, apply freeHomSectionsEquiv P coefficientObject, and evaluate at PUnit.unit. By kernelProductFunctional_apply and the definition of kernelProductSection, the right side is exactly ULift.up (kernelProductFunctional X d aμ); lowering by ULift.down gives the strength-1 compatibility theorem stated above.

Now assume kernelProductFunctional X d = 0. For an arbitrary
    s : ((Condensed.profiniteSolid R).obj X).obj.obj (op Point),
choose
    μ := (E_X.inv.hom.app (op Point)) s.
The strength-1 identity gives
    (((d.hom.app (op Point)) s) PUnit.unit).down = 0.
Since Point = CompHaus.of PUnit, a locally constant function on Point is determined by its value at PUnit.unit; since R = ULift ℤ, ULift.down reflects zero. Hence
    (d.hom.app (op Point)) s = 0.
Module-hom extensionality over arbitrary s gives
    d.hom.app (op Point) = 0.

The minimal dependency chain is therefore

    N3_POINT_COEFFICIENT_EQUALITY
    → FINITE_COEFFICIENT_FAMILY_RECONSTRUCTION
    → FINITE_MEASURE_SECTION_REALIZATION
    → GLOBAL_LIMIT_COVERAGE
    → APPLIED_D_COMPATIBILITY
    → POINT_COMPONENT_VANISHING.

FINITE_MEASURE_MORPHISM_REALIZATION is skippable packaging; quotient compatibility is already protected in the weighted construction and ordinary functoriality.

## Assumptions beyond bootstrap

None.

N3 is assumed exactly as instructed. The argument uses only the protected finite dual transports, weighted finite quotient compatibility, weightedFiniteBooleanMeasureLimitLift_fac, measureFunctorMapConeIsLimit X, the canonical measureProfiniteSolidNatIso, and the definitions/protected interfaces for kernelProductSection and kernelProductFunctional.

The displayed finite one-point section realization is a theorem obligation, not an added assumption. It is the first unprotected Lean-sized arrow identified by this work package.

## Verification / falsification hooks

1. Type-check weightedFiniteBooleanMeasureSection_allTrue_realizes_pushforward exactly as displayed, expanding namespace abbreviations only as required.
2. After transporting both sides through finiteMeasurePresheafFamilyIso.hom and finiteFamilyInternalHomIso.hom, the goal should reduce pointwise in q to N3, with only the finite source-family coordinate-extraction specialization remaining.
3. Derive the older finite-stage morphism equality from the section theorem using injectivity of freeHomSectionsEquiv. If an independent theorem stronger than this is required, the claimed minimality is falsified.
4. Use exactly one (measureFunctorMapConeIsLimit X).hom_ext to obtain global one-point coverage from the finite-stage equalities.
5. Expand kernelProductFunctional_apply after postcomposition with E_X ≫ d; the resulting scalar must be the value at PUnit.unit of the Point component.
6. With kernelProductFunctional X d = 0, verify Point-component vanishing by extensionality only. Do not invoke coefficient_hom_ext_point, because that would promote the conclusion beyond the authorized target.

## Claim boundary

This proves a reduction to Point-component vanishing only.

It does not assert d = 0, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion. It also does not require global all-true weighted measure coverage as an independently packaged theorem beyond the one-point limit identity used in the derivation.

## Next residual

Formalize the single finite-section lemma weightedFiniteBooleanMeasureSection_allTrue_realizes_pushforward.

Its substantive content is finite coordinate extraction for the pushed arbitrary Point measure section. After that lemma, the remaining route is protected transport plus one limit hom-ext and a short Point/ULift extensionality argument.
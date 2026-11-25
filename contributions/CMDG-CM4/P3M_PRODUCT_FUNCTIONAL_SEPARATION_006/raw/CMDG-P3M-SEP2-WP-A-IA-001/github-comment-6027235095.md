GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-SEP2-WP-A-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-P3M-SEP2-A
assignment: CMDG-P3M-SEP2-WP-A
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

At protected Programme commit `1a086db26b8f383d6d320edc545df9581fe6a72f`, vanishing of

`kernelProductFunctional X d`

reduces Point recovery to one exact separation statement for the canonical weighted-measure probes.

For each weight `a : IntegralBasisIndex X → ℤ`, let the corresponding canonical probe be the morphism

`(Condensed.profiniteFree R).map (basisBooleanPointProbe X (fun _ => true)) ≫ weightedFiniteBooleanMeasureLimitLift X a ≫ measureProfiniteSolidNatIso.hom.app X`

from the one-point free object into `(Condensed.profiniteSolid R).obj X`.

If

`kernelProductFunctional X d = 0`,

then every such probe composes with `d` to zero. Therefore the requested implication

`kernelProductFunctional X d = 0 → d.hom.app (op Point) = 0`

will follow from the following Lean-sized missing separator lemma:

```lean
theorem weightedMeasurePointProbes_separate
    (X : Profinite.{u})
    (d :
      (Condensed.profiniteSolid R).obj X ⟶ coefficientObject)
    (h :
      ∀ a : IntegralBasisIndex X → ℤ,
        (Condensed.profiniteFree R).map
            (basisBooleanPointProbe X (fun _ => true)) ≫
          weightedFiniteBooleanMeasureLimitLift X a ≫
          CMDG.CondensedCM4P2E.CanonicalRightKanUniqueness
            .measureProfiniteSolidNatIso.hom.app X ≫ d = 0) :
    d.hom.app (op Point) = 0
```

Equivalently, at the Point component, the elements represented by the all-true weighted-measure probes must span/generate a separating family for maps to the discrete coefficient object.

This statement is strictly targeted at the Point component and is the weakest missing bridge needed before applying the already protected `coefficient_hom_ext_point`.

## Derivation

By definition,

`kernelProductFunctional X d a`

is the `ULift.down` of the all-true value of

`kernelProductSection X d a`.

Thus `kernelProductFunctional X d = 0` gives, for every `a`, zero at the unique all-true Point evaluation. The coefficient section over the one-point profinite source is a locally constant function on `PUnit`; hence zero at its unique point makes the whole one-point section zero.

Using the protected `freeHomSectionsEquiv` and its injectivity, this turns the scalar equality into the morphism equality

```text
(profiniteFree R).map (basisBooleanPointProbe X allTrue)
  ≫ weightedFiniteBooleanMeasureLimitLift X a
  ≫ measureProfiniteSolidNatIso.hom.app X
  ≫ d
= 0.
```

So the functional loses no information *within each canonical probe*: the only remaining issue is whether the family of those probes sees every Point-component element on which `d.hom.app (op Point)` could be nonzero.

The protected evaluation-weight/Dirac identity provides an important consistency check. For `a = integralBasisEvaluationWeight X x`, the probe becomes the ordinary point probe through `measureSolidification`, and after the protected comparison isomorphism this lands through `profiniteSolidification`. Hence the reduction contains the already-known lower/free point tests, but the packet contains no theorem showing that the full weighted family spans the extra Point sections of `profiniteSolid X`.

The protected `measurePointProjection_zero_reflects` theorem does not by itself close this gap. It says that a one-point *measure section* is determined by its enriched-Hom projection. What is still needed here is a generation/surjectivity statement connecting arbitrary Point sections of `profiniteSolid X` to the canonical weighted-measure probe family before applying `d`.

## Assumptions beyond bootstrap

None.

I used only the four protected files named by the immutable launch artifact at Programme commit `1a086db26b8f383d6d320edc545df9581fe6a72f`.

No later branch state, external mathematics, or sibling-worker result is used as authority.

## Verification / falsification hooks

1. Formalize the probe family above as a Point-component subset/submodule.
2. Prove that its span is `⊤`, or equivalently prove the displayed `weightedMeasurePointProbes_separate` theorem directly.
3. A counterexample is decisive: exhibit a nonzero
   `z : ((Condensed.profiniteSolid R).obj X).obj.obj (op Point)`
   outside the span detected by all weighted probes, together with a coefficient-valued linear map nonzero on `z` and zero on every probe element.
4. If the separator lemma is proved, combine it immediately with `coefficient_hom_ext_point` (taking the comparison morphism against zero) to obtain `d = 0`.
5. The evaluation-weight specialization should replay to the protected global Dirac identity; failure indicates a type/orientation error in the probe formulation.

## Claim boundary

This return does **not** prove coefficient-object solidity, P3 completion, CM4 completion, or the full implication requested in WP-A.

It proves a reduction of WP-A to one explicit Point-generation/separation lemma for the already constructed weighted-measure probes. No canonical mutation or certification is claimed.

## Next residual

Prove or refute `weightedMeasurePointProbes_separate`.

Concretely: determine whether the Point-component images of

`(profiniteFree R).map (basisBooleanPointProbe X allTrue) ≫ weightedFiniteBooleanMeasureLimitLift X a ≫ measureProfiniteSolidNatIso.hom.app X`

as `a` varies generate enough of `((Condensed.profiniteSolid R).obj X).obj.obj (op Point)` to force every coefficient-valued map annihilating them to be zero on the Point component.
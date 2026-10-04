GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-COV-WP-D-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-COV-D
assignment: CMDG-P3M-COV-WP-D
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Write
`Lμ := measurePointIntegralFunctional X μ`,
`aμ i := Lμ (integralBasis X i)`,
`P := Profinite.of PUnit`,
`qtrue := basisBooleanPointProbe X (fun _ => true)`, and
`μHom := (freeHomSectionsEquiv P (CMDG.CondensedCM4P2D.measureFunctor.obj X)).symm μ`
using the definitional identification of `Sections P (measureFunctor.obj X)` with
`(measurePresheafObj X).obj (op Point)`.

The finite-stage realization is:
```
∀ j : DiscreteQuotient X,
  μHom ≫ CMDG.CondensedCM4P2D.measureFunctor.map (finiteQuotientMap X j) =
    (Condensed.profiniteFree R).map qtrue ≫
      weightedFiniteBooleanMeasureHom X aμ j.
```

The scalar core is the generic basis-coordinate identity
```
∀ (L : LocallyConstant X ℤ →ₗ[ℤ] ℤ) (v : LocallyConstant X ℤ),
  weightedBasisBooleanPairing X
      (fun i => L (integralBasis X i)) v (fun _ => true) =
    L v.
```
Specializing `L = Lμ` gives, for every finite quotient point `q`,
```
weightedFiniteBooleanCoefficient X aμ j q (fun _ => true) =
  measurePointFunctional X μ (finiteDeltaPullbackR X j q).
```

Consequently the protected limit yields the global all-true coverage identity
```
μHom =
  (Condensed.profiniteFree R).map qtrue ≫
    weightedFiniteBooleanMeasureLimitLift X aμ.
```

## Derivation

For the generic scalar identity, define
`lhs := (LocallyConstant.evalₗ ℤ (fun _ => true)).comp
  (weightedBasisBooleanPairing X (fun i => L (integralBasis X i)))`.
Apply `(integralBasis X).ext`. On a basis vector, `Module.Basis.repr_self` and the protected weighted Boolean coordinate formula reduce the left side to
`L (integralBasis X i)`; hence `lhs = L`, and evaluation at arbitrary `v` proves the identity.

For `Lμ`, unfold `measurePointIntegralFunctional` and `liftedIntFunctionalDown`. Applying the identity to
`locallyConstantIntegralDownEquiv X (finiteDeltaPullbackR X j q)` and lifting back through `ULift` gives the displayed coefficient formula.

Now project `μ` along `finiteQuotientMap X j`. By the protected definition of `measurePresheafFunctor.map`, this is precomposition of the internal-Hom functional by pullback from the finite quotient. On the finite delta at `q`, its value is therefore exactly
`measurePointFunctional X μ (finiteDeltaPullbackR X j q)`.
The weighted finite section, pulled to `qtrue`, has the same coordinate by the preceding formula. The protected finite family/internal-Hom and measure/family isomorphisms are isomorphisms, so equality on every finite delta coordinate gives equality of the finite measure sections. Applying `freeHomSectionsEquiv` gives the stated finite morphism equality.

The requested dependency ledger is therefore:
```
FINITE_STAGE_COORDINATE_RECONSTRUCTION          [basis extensionality; justified]
→ FINITE_STAGE_WEIGHTED_REALIZATION             [finite delta coordinates + protected finite isomorphisms; justified]
→ QUOTIENT_PUSHFORWARD_COMPATIBILITY            [weightedFiniteBooleanMeasureHom_pushforward]
→ LIMIT_HOM_EXT                                 [measureFunctorMapConeIsLimit X]
→ GLOBAL_ALL_TRUE_POINT_COVERAGE                [hom_ext + weightedFiniteBooleanMeasureLimitLift_fac]
```

For the last step, compose both candidate global morphisms with every cone projection. The left composite is the finite projection of `μHom`; the right composite reduces by associativity and `weightedFiniteBooleanMeasureLimitLift_fac` to the weighted finite morphism. Finite-stage realization identifies these composites, and `(measureFunctorMapConeIsLimit X).hom_ext` identifies the global morphisms.

## Assumptions beyond bootstrap

None. The argument uses only the protected definitions/theorems and standard module-basis extensionality. No additional separation, solidity, injectivity, or mapping-out hypothesis is introduced.

## Verification / falsification hooks

1. Check `weightedFiniteBooleanCoefficient`: it is the weighted basis pairing applied to `finiteDeltaPullbackR`.
2. Check `weightedFiniteBooleanMeasureSection`: it is obtained from the coefficient family by the two protected inverse finite transport isomorphisms.
3. Check `weightedFiniteBooleanMeasureHom`: it is exactly `freeHomSectionsEquiv.symm` of that section.
4. Check `weightedFiniteBooleanMeasureSection_pushforward` and `weightedFiniteBooleanMeasureHom_pushforward`: quotient compatibility is already proved, not missing.
5. Check `weightedFiniteBooleanMeasureLimitLift` and `weightedFiniteBooleanMeasureLimitLift_fac`: the global object is the protected limit lift and recovers each finite weighted morphism.
6. Direct falsification target for finite realization: find `j,q` for which the projected `μ` and the all-true weighted section differ on the finite delta at `q`. The scalar basis-extensionality calculation rules this out.
7. Formalization hook: first materialize the generic `weightedBasisBooleanPairing` functional-weight/all-true lemma; then the finite realization theorem above should reduce to finite-delta extensionality through the already-protected transport isomorphisms.

## Claim boundary

This is a mathematical/typed reduction, not a claim that the two displayed packaging lemmas have already been compiled as new Lean declarations. It establishes the finite-stage route and the resulting global one-point coverage statement only. It does not assert `d = 0`, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion. The parent target remains only `d.hom.app (op Point) = 0`.

## Next residual

Materialize the finite realization equality as a Lean theorem, using the generic functional-weight/all-true basis lemma and finite-delta extensionality. Then materialize the global coverage theorem by the one-line `measureFunctorMapConeIsLimit X` hom-ext argument with `weightedFiniteBooleanMeasureLimitLift_fac`.
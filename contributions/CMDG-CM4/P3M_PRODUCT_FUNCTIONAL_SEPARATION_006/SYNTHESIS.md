# CMDG P3-M product-functional separation — protected cohort synthesis

Status: synthesis of protected WP-B/WP-C/WP-D evidence only.

WP-A is excluded. Its issue comment was made without an active worker reservation and is terminally disposed as `INVALID_UNLEASED_RETURN__NOT_ADMITTED`.

## Convergent result

The three admitted independent returns converge on the same substantially narrower residual.

The remaining coefficient-solidity route does not require the stronger `CoefficientFiniteStageMappingOut` statement. It is enough to prove Point reconstruction for the weighted global measure family.

Define the Point section represented by a weight vector `a` by pulling `weightedFiniteBooleanMeasureLimitLift X a` along the all-true Boolean point and identifying the resulting map with a Point section of `measurePresheafObj X`.

For a Point measure section `μ`, use the canonical weight code

```lean
fun i => measurePointIntegralFunctional X μ (integralBasis X i)
```

The smallest common target is:

```lean
theorem weightedPointMeasureSection_reconstruct
    (X : Profinite.{u})
    (μ : (measurePresheafObj X).obj (op Point)) :
    weightedPointMeasureSection X
      (fun i =>
        measurePointIntegralFunctional X μ (integralBasis X i)) = μ
```

Equivalently, the weighted Point-section map is surjective.

## Why this is enough

Protected `kernelProductFunctional_eq_zero_of_solidification_kernel` already supplies the upstream implication from the solidification kernel to zero product functional.

If Point reconstruction holds, vanishing `kernelProductFunctional X d` annihilates every Point measure section after transport through `measureProfiniteSolidNatIso`. Hence `d.hom.app (op Point) = 0`.

Protected `coefficient_hom_ext_point` then upgrades Point-component vanishing to `d = 0`.

So the proof chain is:

```text
solidification-kernel hypothesis
    -> kernelProductFunctional X d = 0
    -> weighted Point reconstruction
    -> d.hom.app (op Point) = 0
    -> coefficient_hom_ext_point
    -> d = 0
```

## Smallest proof decomposition

1. `measurePointFunctional_ext`: equality of `measurePointFunctional` determines the Point measure section, using singleton-Point extensionality plus protected `measurePointProjection_zero_reflects`.
2. Finite-delta spanning: finite quotient delta functions span locally constant functions after finite-quotient factorization.
3. Global/finite compatibility: use protected `weightedFiniteBooleanCoefficient_measurePoint_allTrue` and `weightedFiniteBooleanMeasureLimitLift_fac` to show the reconstructed weighted Point section agrees with `μ` on every finite delta pullback.
4. Apply `measurePointFunctional_ext` to obtain `weightedPointMeasureSection_reconstruct`.
5. Derive `kernelProductFunctional_zero_reflects_point`, then close with `coefficient_hom_ext_point`.

## Adversarial read

WP-D found no protected-type counterexample. Its strongest negative check is that the Nöbeling-basis weight code itself is injective; any remaining information loss must therefore occur in the reconstruction/image of the global weighted family, not in the coding of Point measures.

This does not prove reconstruction. It localizes the only remaining possible failure mode to the global weighted-limit assembly.

## Claim boundary

This synthesis is an internal research reduction, not certification. It does not prove the reconstruction lemma, coefficient solidity, P3 completion, or CM4 completion.

The next native GCL proof/falsification target is `weightedPointMeasureSection_reconstruct`.

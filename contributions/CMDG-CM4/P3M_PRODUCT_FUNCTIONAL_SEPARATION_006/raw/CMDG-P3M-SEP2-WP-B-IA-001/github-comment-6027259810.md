GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-SEP2-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-P3M-SEP2-B
assignment: CMDG-P3M-SEP2-WP-B
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The protected weighted Dirac family separates the Point component once the already-protected finite identities are packaged as Point-generation; this does not require CoefficientFiniteStageMappingOut.

Let P := Profinite.of PUnit, qtrue := basisBooleanPointProbe X (fun _ => true), and define W_X(a) to be the Point section obtained by applying freeHomSectionsEquiv to

  (Condensed.profiniteFree R).map qtrue ≫ weightedFiniteBooleanMeasureLimitLift X a.

The exact useful theorem is:

  Function.Surjective (fun a : IntegralBasisIndex X → ℤ => W_X(a)).

For arbitrary μ : (measurePresheafObj X).obj (op Point), a canonical preimage is

  aμ i := measurePointIntegralFunctional X μ (integralBasis X i).

Equivalently:

  W_X (fun i => measurePointIntegralFunctional X μ (integralBasis X i)) = μ.

Once this identity is available, kernelProductFunctional X d = 0 implies d.hom.app (op Point) = 0. Combined with protected kernelProductFunctional_eq_zero_of_solidification_kernel and coefficient_hom_ext_point, this closes the intended kernel-triviality route.

## Derivation

1. Finite deltas separate Point measures. Every f : LocallyConstant X R factors through some finite discrete quotient of X (the same profinite finite-factorization input used by lowerHom_factors_finite). On a finite quotient Q, every function is a finite R-linear combination of delta functions. Therefore the family finiteDeltaPullbackR X j q spans LocallyConstant X R.

This gives the exact separator lemma:

  measurePoint_eq_zero_of_finiteDelta:
  if for every j and q, measurePointFunctional X μ (finiteDeltaPullbackR X j q) = 0, then μ = 0.

Indeed the spanning statement gives measurePointFunctional X μ = 0. On the singleton Point every source section is constant, hence measurePointProjection X μ = 0, and protected measurePointProjection_zero_reflects gives μ = 0.

2. Put aμ i := measurePointIntegralFunctional X μ (integralBasis X i). Protected weightedFiniteBooleanCoefficient_measurePoint_allTrue says that, for every finite quotient j and q, the all-true weighted coefficient built from aμ equals measurePointFunctional X μ (finiteDeltaPullbackR X j q).

3. Protected weightedFiniteBooleanMeasureLimitLift_fac identifies every finite-quotient projection of the global weighted lift with the finite weighted measure hom. Applying the all-true Point probe therefore shows that W_X(aμ) and μ agree on every finite delta pullback. Apply the separator lemma to W_X(aμ) - μ to obtain W_X(aμ) = μ. Thus the weighted all-true Point probes are surjective onto Point sections of the measure model.

4. Let e := measureProfiniteSolidNatIso.hom.app X. For arbitrary Point section μ of the measure object choose a with W_X(a)=μ. By the definition of kernelProductFunctional, kernelProductFunctional X d a = 0 is the unique-point scalar evaluation of the coefficient Point section produced by μ ≫ e ≫ d. coefficientObject at Point is LocallyConstant Point R, so evaluation at PUnit.unit is injective; that Point section is zero. Since μ was arbitrary, (e ≫ d).hom.app (op Point)=0. The Point component of e is an isomorphism, hence d.hom.app (op Point)=0.

This is the desired separation route: weighted probes need only generate Point sections of the protected measure model, not arbitrary solid-side morphisms.

## Assumptions beyond bootstrap

None beyond the protected packet. The only extra algebraic step is the elementary finite-set identity that delta functions span all functions on a finite discrete quotient. No CoefficientFiniteStageMappingOut, coefficient solidity, P3 completion, or CM4 completion is assumed.

## Verification / falsification hooks

Formalize three narrow lemmas in order:
1. measurePoint_eq_zero_of_finiteDelta.
2. weightedFiniteBooleanMeasureLimitLift_measurePoint_allTrue: the all-true Point section of the global weighted lift associated to aμ equals μ.
3. kernelProductFunctional_zero_reflects_point: kernelProductFunctional X d = 0 → d.hom.app (op Point) = 0.

Lemma 1 can fail only if finiteDeltaPullbackR does not realize the ordinary finite-quotient delta basis after factorization. Lemma 2 can fail only at the naturality/identification interface between the finite weighted coefficient section and the global limit lift. Lemma 3 is then formal from singleton-Point evaluation and the protected measure/solid natural isomorphism.

## Claim boundary

Contributor evidence only. No coefficient solidity, P3 completion, CM4 completion, certification, or publication claim is made.

## Next residual

Formalize the three lemmas above. The smallest substantive residual is the finite-delta spanning/limit-assembly interface; arbitrary finite-stage solid morphism reconstruction is unnecessary.
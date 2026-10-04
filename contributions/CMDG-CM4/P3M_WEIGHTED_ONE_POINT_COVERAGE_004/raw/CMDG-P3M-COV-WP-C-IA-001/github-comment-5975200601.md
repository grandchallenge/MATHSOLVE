GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-COV-WP-C-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-COV-C
assignment: CMDG-P3M-COV-WP-C
disposition: EXACT_BLOCKER
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
No concrete protected-type counterexample was found in the supplied packet. The candidate loss points can be narrowed as follows.

1. `measurePointProjection -> measurePointFunctional` is lossless. Here `Point = CompHaus.of PUnit`. Every element of `LocallyConstant Point (LocallyConstant X R)` is the constant family determined by its value at `PUnit.unit`, and every element of `LocallyConstant Point R` is determined by evaluation at that same point. Thus the protected definition of `measurePointFunctional` is the projected linear map conjugated by the one-point constant/evaluation identifications. Equality of these functionals forces equality of the projections; by linearity and protected `measurePointProjection_zero_reflects`, it then forces equality of the original one-point measure sections.

2. Once `measurePointIntegralFunctional X μ` is fixed, its values on `integralBasis X` determine it uniquely: if two integer linear functionals agree on every basis vector, basis extensionality gives equality on all of `LocallyConstant X ℤ`. Hence the `integralBasis` coordinate stage itself cannot produce two different integral functionals with the same coordinate vector.

3. The finite coefficient-to-measure transports in the protected weighted construction are inverse sides of isomorphisms, so they introduce no algebraic quotient. The finite-to-global step also introduces no loss of finite-stage information: `weightedFiniteBooleanMeasureLimitLift_fac` recovers every finite weighted morphism, and equality of global lifts is tested by the protected limit `hom_ext`.

4. The selector-to-all-true step is not an irreversible loss for the varying-weight route. Protected `weightedFiniteBooleanMeasureLimitLift_point_reweight` gives exactly
   evaluation at selector `t` with weights `a` = all-true evaluation with weights `weightedBoolToInt a t`.
   Protected `kernelProductSection_reweight_eval` carries the same identity to the product functional.

The first faithfulness statement that is not available in the supplied protected interface is therefore
`measurePointFunctional -> measurePointIntegralFunctional`.
The packet gives only
`measurePointIntegralFunctional X μ := liftedIntFunctionalDown X (measurePointFunctional X μ)`;
it supplies neither the implementation of `liftedIntFunctionalDown` nor a zero/equality-reflection theorem for it. From this packet alone it is therefore not possible to certify that two actual one-point measure sections with the same integral-basis coordinate vector must coincide. This is an exact interface blocker, not a constructed counterexample.

If the omitted descent is the expected faithful conjugation along the `ULift ℤ <-> ℤ` identification, this blocker disappears. In that case the smallest remaining falsification target is the generic finite-stage all-true reconstruction identity: for `aμ i := measurePointIntegralFunctional X μ (integralBasis X i)`, the all-true value of the weighted coefficient at every finite quotient point must equal the original functional applied to that quotient delta function. A failure of that identity would give the requested concrete weighted-coverage counterexample; if it holds, the protected isomorphic transports and limit-factor theorem propagate it to the global all-true realization.

## Derivation
For the projection/functionality step, let `Fμ := measurePointProjectionLinear X μ`. Since the domain point is `PUnit`, any input family `p` satisfies `p = LocallyConstant.const Point (p PUnit.unit)`; similarly, two output families are equal when their values at `PUnit.unit` agree. Therefore the scalar functional
`eval_at_unit ∘ Fμ ∘ const`
determines `Fμ), hence `measurePointProjection X μ). If two one-point measure sections have equal scalar functionals, their projected difference is zero, and protected zero-reflection gives equality of the sections.

For the basis step, write `Lμ := measurePointIntegralFunctional X μ`. If `Lμ (integralBasis X i) = Lν (integralBasis X i)` for all `i`, then the two ℤ-linear maps agree on a basis and hence agree on every finite linear combination, i.e. on all locally constant integer functions. This eliminates basis-coordinate aliasing on one-point, Bool, and every other profinite example equally; finite examples merely make the same free-module fact finite rank.

For the weighted side, the protected source defines the finite weighted measure section by two isomorphism transports from its coefficient family. The global lift satisfies every finite cone equation by `weightedFiniteBooleanMeasureLimitLift_fac`. Finally, protected point reweighting shows that arbitrary Boolean selector evaluation is represented by all-true evaluation after coordinatewise reweighting. Thus a surviving failure cannot be blamed on the two transports, the inverse limit, or the choice of the all-true selector in the varying-weight functional.

The unresolved generic reconstruction identity is algebraically the expected basis formula. If `b_i := integralBasis X i`, `aμ(i)=Lμ(b_i)`, and a finite quotient delta expands as `δ = Σ_i c_i b_i` with finite support, then linearity gives
`Lμ(δ)=Σ_i c_i aμ(i)`.
The weighted coefficient construction is intended to compute this weighted basis pairing at the all-true selector. The supplied packet proves a special evaluation-weight/Dirac realization, but it does not contain the generic `aμ` reconstruction theorem needed to compare an arbitrary original one-point measure section with its canonical weighted realization.

## Assumptions beyond bootstrap
Only standard mathematics was used for the certified reductions: functions and locally constant functions on `PUnit` are determined by their unique value; linear maps are determined by a basis; and isomorphisms are injective.

No faithfulness property of `liftedIntFunctionalDown` was assumed in the certified conclusion. The statement about faithful `ULift ℤ` descent is explicitly conditional and identifies what would remove the first blocker.

## Verification / falsification hooks
1. Prove or refute, in the protected types, equality reflection for the integer descent:
   if
   `measurePointIntegralFunctional X μ = measurePointIntegralFunctional X ν`,
   does
   `measurePointFunctional X μ = measurePointFunctional X ν`
   follow?
   A zero-reflection version is sufficient by linearity.

2. For a direct weighted falsification, define
   `aμ i := measurePointIntegralFunctional X μ (integralBasis X i)`
   and test the finite-stage coefficient identity at every quotient point: all-true evaluation of the weighted coefficient built from `aμ` must equal the scalar assigned by `μ` to the corresponding finite delta function. Point and Bool are the first concrete test spaces.

3. If the coefficient identity holds, transport it through the two protected finite isomorphisms and compare the resulting one-point finite measure section with the image of `μ` at that quotient. Then use `weightedFiniteBooleanMeasureLimitLift_fac` plus limit `hom_ext` to test the global realization.

4. A genuine counterexample must therefore exhibit either:
   (a) nonfaithfulness of the protected integer descent on an actual `measurePointFunctional`, or
   (b) an actual `μ`, quotient stage, and quotient point where the generic all-true weighted coefficient disagrees with `μ` on the corresponding delta.
   Abstract additive ghost models do not address either hook.

## Claim boundary
This return does not prove `d.hom.app (op Point) = 0`. It does not prove the generic weighted reconstruction theorem, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion. It reports no counterexample. It isolates the first unsupported faithfulness bridge in the supplied packet and, conditionally on that bridge, the smallest remaining concrete weighted-reconstruction falsification target.

## Next residual
First close the equality/zero-reflection property of `liftedIntFunctionalDown` on the protected point functionals. If it is faithful, attack exactly one lemma next: generic finite-stage all-true reconstruction from
`aμ i = measurePointIntegralFunctional X μ (integralBasis X i)`.
That coefficient-level statement is the smallest place where an actual weighted-coverage counterexample can still occur before the protected isomorphic transports and finite-quotient limit take over.
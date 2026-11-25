GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-SEP-WP-D-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-D
assignment: CMDG-P3M-SEP-WP-D
disposition: EXACT_BLOCKER
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
From the protected packet alone, the requested information-preservation chain is not justified already at its first substantive arrow, from a one-point measure section through `measurePointProjection`. The packet protects existence of `measurePointProjection` and the downstream conversion interfaces, but it protects no injectivity, left inverse, reconstruction equation, extensionality theorem, or even zero-reflection theorem for `measurePointProjection`. Consequently zero downstream scalar/product-functional data cannot, on the supplied interface alone, be pulled back to vanishing of the original one-point measure section.

Typed ledger, writing `S₀` for the one-point measure-section type and `S₁ := codomain(measurePointProjection)`:
1. `S₀ → S₁` via `measurePointProjection`: **only a map, with no protected injectivity**. This is the FIRST unjustified information-preservation arrow.
2. `measurePointProjection → measurePointProjectionLinear`: **type/coefficient change requiring a named lemma**. The packet gives both interfaces but no theorem saying that the linear object has exactly the same underlying function as the projection, nor a reconstruction equivalence.
3. `measurePointProjectionLinear → measurePointFunctional`: **type/coefficient change requiring a named lemma**. No protected injectivity or evaluation-compatibility equation is supplied.
4. `measurePointFunctional → measurePointIntegralFunctional`: **type/coefficient change requiring a named lemma**. No protected injectivity or theorem identifying the two representations extensionally is supplied.
5. `measurePointIntegralFunctional → Nöbeling-basis coordinates`: at the abstract algebraic level, restriction of a genuine additive/ℤ-linear functional on `LocallyConstant X ℤ` to all elements of the basis `integralBasis X` is **proved injective by standard mathematics**: every locally constant function has a unique finite integer linear combination of basis elements, so equality on basis elements implies equality on every finite linear combination. However, the packet does not state the exact type of `measurePointIntegralFunctional` or a lemma identifying its coordinate map with evaluation on `integralBasis X`; therefore the concrete campaign arrow still requires that named typing/extensionality lemma before this abstract injectivity can be applied.
6. `Nöbeling-basis coordinates → weighted-Boolean realization / kernelProductFunctional`: **only a map, with no protected injectivity**. Protected finite-coordinate dependence for `kernelProductFunctional` establishes dependence, not separation or reconstruction. No protected theorem states that the weighted-Boolean family distinguishes all basis-coordinate families.

Thus the chain does not reach the “all arrows through basis coordinates are injective” case. The earliest gap is strictly earlier than the weighted-family comparison.

## Derivation
Information preservation of a map `f : A → B` means at minimum injectivity for arbitrary information, equivalently
`∀ a b, f a = f b → a = b`.
A left inverse or an equivalence would imply this. None is protected for `measurePointProjection`.

The packet states only that the named one-point interfaces “turn a one-point measure section into an ordinary scalar/integral functional.” Existence of a map gives no implication from equality of outputs to equality of inputs. In particular, from
`measurePointProjection s = measurePointProjection t`
one cannot derive `s = t` without an additional theorem. For the zero-separation use case, even the weaker implication
`measurePointProjection s = 0 → s = 0`
is not protected.

For basis coordinates, the standard proof is finite expansion. If `B = integralBasis X` is a ℤ-basis and `F,G` are additive/ℤ-linear maps out of `LocallyConstant X ℤ` with `F (B i)=G (B i)` for every basis index `i`, write arbitrary `v` uniquely as a finite sum `v = Σ_i n_i • B i`. Additivity and integer-linearity give
`F v = Σ_i n_i • F(B i) = Σ_i n_i • G(B i) = G v`.
Hence the abstract coordinate-restriction map on such functionals is injective. This does not by itself identify the concrete `measurePointIntegralFunctional` with that typed functional space.

The admitted theorem `kernelProductFunctional_eq_zero_of_solidification_kernel` supplies only the forward implication from the solidification-kernel hypothesis to zero product-functional data. Finite-coordinate dependence also supplies no converse. Therefore neither statement closes any earlier noninjective or unproved interface.

## Assumptions beyond bootstrap
NONE. The basis-coordinate injectivity argument is conditional only on the concrete object having the ordinary additive/ℤ-linear functional type required to apply the protected Nöbeling basis; that typing is explicitly not assumed as an established campaign fact.

## Verification / falsification hooks
1. Inspect the protected declarations for a theorem of the form `Function.Injective measurePointProjection`, an extensionality theorem, a left inverse, or a reconstruction identity. Any such theorem would falsify the claimed first blocker.
2. Check whether `measurePointProjectionLinear` is definitionally the bundled form of `measurePointProjection`; if so, arrow 2 can be upgraded to definitional equivalence, but arrow 1 remains the first blocker unless projection injectivity is separately proved.
3. Check the exact type of `measurePointIntegralFunctional`. If it is an additive/ℤ-linear functional on `LocallyConstant X ℤ`, prove an extensionality lemma using `integralBasis X`; this would certify the abstract basis-coordinate injectivity argument at the campaign type.
4. Search specifically for a separating/reconstruction theorem for the weighted-Boolean family. Finite-coordinate dependence alone is insufficient.

## Claim boundary
What follows: the supplied protected interface does not justify information preservation from the one-point measure section past `measurePointProjection`; therefore the downstream zero product-functional theorem cannot by itself establish vanishing of the one-point component.

What does not follow: this is not a counterexample to injectivity, not a proof that `measurePointProjection` loses information in the actual implementation, not a proof or disproof of the successor separation theorem, and not any certification or downstream CM4 claim.

## Next residual
The smallest information-preservation theorem closing the first arrow is `Function.Injective measurePointProjection` at its exact campaign type, equivalently an extensionality theorem `measurePointProjection s = measurePointProjection t → s = t`. If only the zero-separation goal is needed, the strictly smaller goal-specific lemma is `measurePointProjection s = 0 → s = 0`.
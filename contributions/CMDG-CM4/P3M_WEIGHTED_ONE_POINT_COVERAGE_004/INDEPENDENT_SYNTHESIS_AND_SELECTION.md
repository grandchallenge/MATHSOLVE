# CMDG P3-M weighted one-point coverage — independent synthesis and native-node selection

Date: 2026-10-03

## Protected inputs

Protected Programme predecessor and current Programme `main`:
`MATH-PROGRAMME@fdd7a3fe3df7b2d699753347080c1cbc2127e02d`.

Protected Solve evidence base:
`MATHSOLVE@5ffb289251267ffc7dde9be3ad5ff7e54f2a34e1`.

Blind-cohort reconciliation and closure:
`MATHSOLVE@99124f075018afc4042fb5e0cc3e4e6e35a96746`.

Protected contributor returns:

- WP-A, issue #800, comment `5975205950`, declared `PROVED_REDUCTION`.
- WP-B, issue #801, comment `5975185050`, declared `PROVED_REDUCTION`.
- WP-C, issue #802, comment `5975200601`, declared `EXACT_BLOCKER`.
- WP-D, issue #803, comment `5975223026`, declared `PROVED_REDUCTION`.

These returns are evidence only. The comparison below is a fresh GCL-owned synthesis against the exact protected source. Contributor dispositions are not adopted as authority.

## Synthesis disposition

`REDUCED_TO_SMALLEST_MISSING_LEMMA`.

No concrete protected-type refutation survived source replay. The complete weighted coverage bridge is not yet admitted as a compiled theorem. The blind evidence and protected definitions instead isolate one smaller algebraic normalization lemma as the first genuinely unprotected arrow.

## Comparison of the four returns

### WP-A — canonical weighted reconstruction

WP-A correctly identifies the reconstruction shape. For

```lean
aμ i := measurePointIntegralFunctional X μ (integralBasis X i)
```

it reduces global reconstruction to the statement that the all-true weighted realization has the prescribed integral-basis coordinates.

Its proposed `ALLTRUE-BASIS` condition is sufficient for equality of `measurePointProjection`, and protected N1 then upgrades zero projection of the difference to equality of one-point measure sections.

This is mathematically useful, but it is stronger and later than the first missing algebraic step. It packages the weighted construction all the way back into a global one-point measure section before checking the core coordinate identity.

### WP-B — weakest operational vanishing bridge

WP-B correctly sharpens the end goal. To prove only

```lean
d.hom.app (op Point) = 0
```

one does not need full section reconstruction if one can prove, for every `μ`, equality after applying the Point component of `d` between `μ` and its canonical weighted all-true representative.

Combined with the already protected reweight/evaluation theorems and

```lean
kernelProductFunctional X d = 0
```

that applied equality is sufficient to close the Point component directly.

This is the preferred terminal bridge once weighted coverage has been established. It is not the first theorem to formalize because it is `d`-dependent and still presupposes the same unproved weighted-coordinate normalization.

### WP-C — adversarial concrete coverage attack

WP-C found no concrete counterexample. Its packet-local blocker was possible information loss in

```text
measurePointFunctional
→ measurePointIntegralFunctional
```

because the bootstrap did not expose the implementation of `liftedIntFunctionalDown`.

Exact protected-source replay removes that blocker. At
`MATH-PROGRAMME@fdd7a3fe3df7b2d699753347080c1cbc2127e02d`,
`liftedIntFunctionalDown` is defined by transport through

```lean
locallyConstantIntegralLiftEquiv X :
  LocallyConstant X ℤ ≃+* LocallyConstant X R
```

with `R = ULift ℤ`, followed by `ULift.down` on the output. Both transports are equivalences. Thus the integer descent does not create the ghost degree of freedom WP-C was required to seek.

WP-C therefore supplies no surviving refutation. Its conditional next falsification target agrees with WP-D: the generic all-true weighted reconstruction calculation.

### WP-D — finite-stage realization and limit route

WP-D supplies the strongest constructive reduction. Its scalar core is:

```lean
∀ (L : LocallyConstant X ℤ →ₗ[ℤ] ℤ) (v : LocallyConstant X ℤ),
  weightedBasisBooleanPairing X
      (fun i => L (integralBasis X i)) v (fun _ => true) =
    L v
```

From that identity it derives the expected finite-delta coefficient equality, then finite weighted-measure realization, quotient compatibility, and finally global coverage through `measureFunctorMapConeIsLimit X`.

Protected-source replay supports the structure of this route:

- `weightedBasisBooleanPairing` is defined from `(integralBasis X).repr` and a weighted linear combination;
- the protected source already proves the special evaluation-weight all-true theorem;
- the finite coefficient-to-measure transports are isomorphisms;
- quotient pushforward compatibility is protected;
- `weightedFiniteBooleanMeasureLimitLift_fac` and the limit `hom_ext` are protected;
- selector reweighting and `kernelProductSection_reweight_eval` are protected.

However, the generic arbitrary-functional all-true identity above is not presently a protected named theorem at the pinned Programme head, and WP-D explicitly returned a typed mathematical reduction rather than a newly compiled Lean declaration. Its later packaging claims therefore must not be promoted before this scalar core is materialized and replayed.

## Independent protected-source replay

The exact protected source establishes the following boundaries.

### Already discharged

1. `measurePointProjection_zero_reflects` is protected at the Programme predecessor.
2. The singleton restriction/evaluation used by `measurePointFunctional` is concrete at `Point = CompHaus.of PUnit`.
3. `liftedIntFunctionalDown` uses an actual locally-constant `ULift` ring equivalence; WP-C's packet-local faithfulness concern is not a live mathematical blocker.
4. `integralBasis X` is a basis, so equality on basis coordinates determines an integer linear functional.
5. Finite coefficient/measure transports, quotient pushforward, the global weighted limit factorization, and selector reweighting are protected.

### First unprotected arrow

What is not yet protected is the generic normalization that says: if the external weight attached to basis index `i` is exactly `L (integralBasis X i)`, then all-true evaluation of the weighted Boolean pairing reconstructs `L` on every vector.

That is the first missing arrow in

```text
integral functional
→ basis-coordinate weight vector
→ all-true weighted basis pairing
→ finite weighted coefficient realization
→ finite measure realization
→ global weighted coverage
→ applied-d compatibility
→ Point-component vanishing
```

## Selected native node

`CMDG-P3M-COV-N2 — WEIGHTED_BASIS_FUNCTIONAL_ALLTRUE`

### Exact target

In namespace `CMDG.CondensedCM4P3G.BasisBooleanPairing`, prove:

```lean
theorem weightedBasisBooleanPairing_functionalWeight_allTrue
    (X : Profinite.{u})
    (L : LocallyConstant X ℤ →ₗ[ℤ] ℤ)
    (v : LocallyConstant X ℤ) :
    weightedBasisBooleanPairing X
        (fun i => L (integralBasis X i)) v
        (fun _ => true) =
      L v
```

Equivalent formulations are acceptable only if they are definitionally or immediately propositionally equivalent at the protected types.

### Native proof route to test first

Treat both sides as linear functionals in `v`.

1. Compose `weightedBasisBooleanPairing X (fun i => L (integralBasis X i))` with evaluation at the all-true Boolean vector.
2. Apply `(integralBasis X).ext`.
3. On a basis vector, use `Module.Basis.repr_self`.
4. Unfold the weighted Boolean linear combination.
5. At the all-true selector, the unique surviving coordinate evaluates to its external weight, namely `L (integralBasis X i)`.
6. Conclude equality of the two linear functionals, then evaluate at arbitrary `v`.

No compactness, limit, measure, solidification, or `d` hypothesis should be needed.

### Falsification requirement

A refutation must occur at the actual protected types and exhibit `X`, `L`, and `v` for which the displayed equality fails. An abstract additive toy model is insufficient.

Given the protected definition through a genuine basis representation, such a refutation would indicate a concrete normalization/sign/evaluation defect in the weighted Boolean construction.

## Why this is the smallest theorem-grade next target

- It is the first unprotected equality common to the constructive WP-A/WP-D routes and WP-C's remaining falsification target.
- It is strictly smaller than global `ALLTRUE-BASIS`, finite-measure reconstruction, projection equality, or WP-B's `d`-applied compatibility.
- It is independent of `d`, solidification, inverse limits, and the measure transport stack.
- It can be proved or refuted entirely inside the already protected Nöbeling-basis/weighted-pairing interface.
- If proved, the next finite coefficient identity should be a short specialization rather than a new conceptual theorem.

## Advancement rule

If N2 is proved:

1. specialize it to
   `L := measurePointIntegralFunctional X μ`
   and to the integral-down form of `finiteDeltaPullbackR X j q`;
2. materialize the finite all-true coefficient reconstruction theorem;
3. transport through the already protected finite measure isomorphisms;
4. use quotient compatibility and `measureFunctorMapConeIsLimit X` to obtain global weighted coverage;
5. prefer WP-B's weaker equality-after-applying-`d` endpoint if it closes
   `d.hom.app (op Point) = 0` without unnecessary full section reconstruction.

If N2 is refuted concretely, stop the weighted-coverage route and classify the exact normalization defect before any successor.

If N2 reduces further, preserve only the exact missing basis/linear-combination lemma and attack that lemma.

## Claim boundary

This synthesis closes the blindness barrier and selects one native proof/falsification node.

It does **not** admit:

- the generic N2 identity itself;
- finite-stage weighted reconstruction;
- global weighted one-point coverage;
- `d.hom.app (op Point) = 0`;
- `d = 0`;
- mapping-out injectivity;
- coefficient solidity;
- P3 completion;
- CM4 completion.

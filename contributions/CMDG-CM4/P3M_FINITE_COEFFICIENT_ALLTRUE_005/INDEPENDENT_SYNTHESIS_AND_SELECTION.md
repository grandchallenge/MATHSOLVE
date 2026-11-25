# CMDG CM4 P3-M — N3 blind-cohort synthesis

STATUS: SYNTHESIS_COMPLETE__N3_REDUCED_TO_N3A
CAMPAIGN: CMDG-CM4
TRANCHE: P3-M-FINITE-COEFFICIENT-ALLTRUE-005
COHORT: CMDG-P3M-N3-BLIND-COHORT-001

## Protected evidence

Blind cohort closure:
`MATHSOLVE@3651d0efd07d451f81c35a65706ea983a6616621`.

Evidence base:
`MATHSOLVE@55e7d34c49c784a408c71f1f899a8ad6c34e5d53`.

All four first valid returns are protected and unadjudicated at that evidence base:

- WP-A: `PROVED_REDUCTION`
- WP-B: `FORMAL_LEMMA_PROVED` as contributor disposition only; no native compilation is inferred
- WP-C: `PROVED_REDUCTION`
- WP-D: `PROVED_REDUCTION`

This synthesis is the first authorized cross-return comparison after cohort closure.

## Protected source replay

Protected Programme predecessor:
`a2897a270c477ac95ba3d18dd068a13b07d3b853`.

Current Programme main at synthesis:
`fceda552485562bfb6210e520a10d3d62314a6f0`.

The current main advance is unrelated to CMDG. The five N3-relevant CMDG blobs are byte-identical between the protected predecessor and current main:

- `CMDGCondensedCM4P3G.lean`: `57c876025d7fac3b1fabcaca87a4a84ed0ffd584`
- `CMDGCondensedCM4P3GBasisBooleanPairing.lean`: `c54c506be4fde0f7aa92d83ab8e84d757520fcd7`
- `CMDGCondensedCM4P3GBasisBooleanPairingR.lean`: `3e580ac2648ed9166f332bac994a6b3763b660c0`
- `CMDGCondensedCM4P3GPointFunctional.lean`: `1cefae23baacf758680763203abc1a748fe46733`
- `CMDGCondensedCM4P3MFiniteQuotientBridge.lean`: `2ecf7b6fc546417828fbd7cc9473526042e5a511`

No source drift affects the synthesis.

## Cross-return synthesis

### WP-A

WP-A gives the direct N3 proof shape:

1. expose `weightedBasisBooleanPairing` through `weightedFiniteBooleanCoefficient` and `weightedBasisBooleanPairingR`;
2. apply protected N2;
3. reduce the remaining goal to the inverse law for `liftedIntFunctionalDown`;
4. close the final `ULift.up ((...).down)` normalization.

It independently identifies one optional helper:
`liftedIntFunctionalDown_integralDown`.

### WP-B

WP-B isolates the generic form of exactly the same helper:

```lean
theorem liftedIntFunctionalDown_apply_inverse
    (X : Profinite.{u})
    (F : LocallyConstant X R →ₗ[R] R)
    (v : LocallyConstant X R) :
    ULift.up
        (liftedIntFunctionalDown X F
          ((locallyConstantIntegralLiftEquiv X).symm v)) =
      F v
```

The contributor proposes the compact proof
`by simpa [liftedIntFunctionalDown]`.

That proposed proof is mathematically consistent with the protected definition, but contributor disposition `FORMAL_LEMMA_PROVED` is evidence only. Native Lean compilation is still required.

### WP-C

WP-C adversarially tests the five intended failure modes and finds no concrete protected-type counterexample.

It independently reduces N3 to the same generic coefficient-transport identity. In particular it eliminates the need for:

- a separate Boolean-cube identification theorem;
- a separate finite-delta integral-descent theorem;
- a sign/order correction;
- any basis-coordinate theorem beyond protected N2.

No adversarial obstruction survives protected-source replay.

### WP-D

WP-D works downstream under the assumption that N3 holds. Its strongest useful result is architectural:

- full finite measure-morphism realization is probably unnecessary;
- the preferred endpoint remains equality only after applying the Point component of `d`;
- after N3, the first proposed downstream missing theorem is
  `weightedFiniteBooleanMeasureSection_allTrue_realizes_pushforward`.

That theorem is strictly downstream of N3 and therefore is not the current native target.

## Selection

Disposition:

`REDUCED_TO_SMALLEST_MISSING_LEMMA`

Selected node:

`CMDG-P3M-COV-N3A — LIFTED_INT_FUNCTIONAL_DOWN_APPLY_INVERSE`

Exact target:

```lean
theorem liftedIntFunctionalDown_apply_inverse
    (X : Profinite.{u})
    (F : LocallyConstant X R →ₗ[R] R)
    (v : LocallyConstant X R) :
    ULift.up
        (liftedIntFunctionalDown X F
          ((locallyConstantIntegralLiftEquiv X).symm v)) =
      F v
```

Why N3A is selected:

1. it is strictly smaller than N3;
2. A, B, and C independently converge on it;
3. the protected definition of `liftedIntFunctionalDown` shows no hidden topology or measure dependency;
4. it is independent of finite quotients, Boolean coordinates, measure sections, limits, and `d`;
5. once compiled, N3 should reduce to protected N2 plus one application of N3A;
6. WP-D's finite-section theorem is downstream and should not be attempted before N3 itself is protected.

## Native proof route

Preferred first attempt:

```lean
by
  simpa [liftedIntFunctionalDown]
```

If simplifier transparency is insufficient, use the expanded exact proof:

1. unfold `liftedIntFunctionalDown`;
2. rewrite
   `(locallyConstantIntegralLiftEquiv X).apply_symm_apply v`;
3. close
   `ULift.up ((F v).down) = F v`
   by constructor/projection normalization.

No theorem weakening is authorized.

## Advancement after N3A

If N3A is native-compiled and protected-admitted:

1. materialize `weightedFiniteBooleanCoefficient_measurePoint_allTrue`;
2. unfold only `weightedFiniteBooleanCoefficient` / `weightedBasisBooleanPairingR`;
3. apply protected N2;
4. apply N3A with
   `F := measurePointFunctional X μ`
   and
   `v := finiteDeltaPullbackR X j q`;
5. protect N3 with exact-head validation and required independent review.

Only after protected N3 admission should the WP-D downstream finite-section bridge be selected or discarded.

## Claim boundary

This synthesis does not prove N3A or N3. It does not establish finite/global weighted reconstruction, Point-component vanishing, `d = 0`, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion.

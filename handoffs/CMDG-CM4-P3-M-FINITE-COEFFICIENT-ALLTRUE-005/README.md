# CMDG CM4 P3-M — N3 finite coefficient all-true reconstruction

STATUS: DRAFTED_NOT_ACTIVATED
CAMPAIGN: CMDG-CM4
TRANCHE: P3-M-FINITE-COEFFICIENT-ALLTRUE-005
PARENT_PROGRAMME_ISSUE: 1162

## Protected authority

- Programme protected baseline: `grandchallenge/MATH-PROGRAMME@a2897a270c477ac95ba3d18dd068a13b07d3b853`.
- Solve planning baseline: `grandchallenge/MATHSOLVE@6f5e7e921a5d0c21515a2aff85530fde7da51286`.
- N1 is protected-admitted: `measurePointProjection_zero_reflects`.
- N2 is protected-admitted: `weightedBasisBooleanPairing_functionalWeight_allTrue`.
- N2 direct axiom readback: `[propext, Classical.choice, Quot.sound]`; no `sorryAx`.
- Current parent target remains only `d.hom.app (op Point) = 0`.

No file in this handoff activates an external agent, creates a claim, or authorizes canonical mutation.

## Native target

`CMDG-P3M-COV-N3 — FINITE_COEFFICIENT_ALLTRUE_RECONSTRUCTION`

Preferred exact theorem:

```lean
theorem weightedFiniteBooleanCoefficient_measurePoint_allTrue
    (X : Profinite.{u})
    (μ : (measurePresheafObj X).obj (op Point))
    (j : DiscreteQuotient X)
    (q : (FiniteQuotientObject X j).obj) :
    weightedFiniteBooleanCoefficient X
        (fun i => measurePointIntegralFunctional X μ (integralBasis X i))
        j q (fun _ => true) =
      measurePointFunctional X μ (finiteDeltaPullbackR X j q)
```

Equivalent theorem names are acceptable only when the statement is definitionally or immediately propositionally equivalent at the protected types.

## Core mathematical reduction

N3 should decompose into two independent algebraic facts.

### A. N2 specialization

For
```lean
L := measurePointIntegralFunctional X μ
v := locallyConstantIntegralDownEquiv X (finiteDeltaPullbackR X j q)
```
protected N2 gives

```lean
weightedBasisBooleanPairing X
    (fun i => L (integralBasis X i)) v (fun _ => true) =
  L v.
```

The definition of `weightedBasisBooleanPairingR` lifts this integer equality back into
`R = ULift ℤ`.

### B. Coefficient transport

The remaining scalar identity is expected to be the generic transport lemma

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

or an immediately equivalent statement.

This follows from the fact that
`locallyConstantIntegralLiftEquiv X : LocallyConstant X ℤ ≃+* LocallyConstant X R`
is an actual ring equivalence, not a lossy map.

Specializing `F := measurePointFunctional X μ` should close the right-hand side of N3.

## Attack order

1. **Direct native N3 proof.** Try the exact theorem immediately. Do not wait for external returns.
2. **Isolate the ULift bridge if Lean resists.** If the direct proof does not normalize, prove the generic coefficient-transport identity separately rather than expanding the entire measure construction.
3. **Adversarial falsification in actual protected types.** Search for a real mismatch in the `ULift`, Boolean-cube, finite-delta, or evaluation chain. Abstract additive ghost models do not count.
4. **Resolve the shortest downstream closure.** Assuming N3, determine whether existing reweight/evaluation theorems already permit equality only after applying `d.hom.app (op Point)`. Prefer that endpoint over full global measure reconstruction.
5. **Only if necessary**, materialize the longer packaging chain:
   `finite coefficient family → finite measure section → finite measure morphism → quotient compatibility → global limit coverage → applied-d equality`.

## Work-package architecture

The proposed auxiliary blind cohort is `CMDG-P3M-N3-BLIND-COHORT-001`.

It contains four non-duplicative assignments:

- **WP-A — direct formal N3 closure.** Prove the exact theorem or return the first Lean-sized blocker.
- **WP-B — coefficient-transport bridge.** Prove the generic `liftedIntFunctionalDown` inverse identity independently of the weighted pairing.
- **WP-C — adversarial protected-type falsification.** Attack N3 for a concrete type/topology/coercion defect.
- **WP-D — minimal downstream closure.** Assuming N3, find the weakest exact theorem needed to reach Point-component vanishing and determine whether finite/global reconstruction can be shortened.

The cohort, if activated, is auxiliary evidence. Native GCL proof work continues independently and is not blocked by external returns.

## Reconciliation rule

If the cohort is activated, sibling returns remain blind until all terminal valid returns are protected and the cohort is explicitly reconciled.

After reconciliation:

- a native compiled proof outranks narrative reductions;
- a concrete protected-type counterexample outranks a positive heuristic;
- packet-local blockers that disappear under protected-source replay are discarded;
- the next node is the first genuinely unprotected theorem common to the surviving route.

## Advancement rule

If N3 is protected-admitted:

1. try the weakest applied-`d` route first;
2. if that does not type-check, materialize finite coefficient-family reconstruction;
3. use the already protected finite transport isomorphisms to obtain finite measure realization;
4. use quotient compatibility and `measureFunctorMapConeIsLimit X` only if global coverage is actually required;
5. close only `d.hom.app (op Point) = 0`;
6. do not promote to `d = 0`, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion without separate proof.

If N3 is refuted, stop the weighted-coverage route and classify the exact failing transport or normalization identity.

If N3 reduces further, preserve the smallest exact helper theorem and attack that theorem natively.

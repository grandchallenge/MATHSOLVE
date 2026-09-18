# YM-D002-R001 — algebraic OS limit closure

## Metadata

- Campaign: YM-001.
- Parent debt: YM-D002.
- Work package: YM-D002-OS-ALGEBRAIC-LIMIT-CLOSURE.
- Protected Solve baseline: 4eb3c242ddb87631175ee74c3ca91f42f910d995.
- Protected Programme authority: 7c8b351cc74bcb6ac2ccd4009eb6dff99913bc19.
- Current Programme routing gate: campaigns/yang_mills/YM_CURRENT_ROUTING_GATE.json.
- Imported theorem interface: YM-T-120 — Osterwalder-Schrader reconstruction interface.
- Certification: none; MATHCERT remains the sole certification authority.

## 18-field restricted-target contract

1. target_id: YM-D002-R001.
2. campaign: YM-001.
3. parent_debt: YM-D002.
4. repository: grandchallenge/MATHSOLVE.
5. solve_baseline: 4eb3c242ddb87631175ee74c3ca91f42f910d995.
6. programme_authority: 7c8b351cc74bcb6ac2ccd4009eb6dff99913bc19.
7. imported_source_authority: protected YM-WP00 normalization plus protected YM-T-120 interface.
8. mathematical_object: a common Euclidean observable/test algebra with reflection, Euclidean and gauge actions, and a sequence of normalized Schwinger functionals converging pointwise on that common algebra.
9. dimension: abstract closure theorem intended for the selected four-dimensional limit; it does not construct that limit.
10. gauge_scope: any target gauge scope for which the common gauge-invariant observable algebra and actions are already defined.
11. regulator_volume_scope: arbitrary sequence of regulated or approximate hierarchies after they have been transported to one common comparison algebra; no regulator or infinite-volume limit is proved here.
12. imported_interfaces: YM-T-120 and the YM-D002 complete-OS-profile debt only.
13. target_statement: determine which exact algebraic/closed-cone parts of the protected OS input profile survive a common-domain pointwise limit without an additional uniform analytic estimate.
14. proof_method: pointwise passage of linear equalities and closedness of the nonnegative real cone for reflection-positive quadratic forms.
15. falsification_condition: an algebraic OS property listed as inherited below fails for a sequence satisfying the stated common-domain convergence and that property at every stage.
16. success_criterion: prove inheritance of normalization, linearity, exact permutation symmetry, Euclidean covariance, gauge invariance, and reflection positivity; isolate the hypotheses not supplied by this closure argument.
17. forbidden_promotions: existence of a four-dimensional limiting hierarchy, regularity/growth, clustering/vacuum uniqueness, OS reconstruction, local-observable construction, mass gap, confinement, novelty, priority, or certification.
18. successor_boundary: YM-D002-R002 — SELECTED_4D_LIMIT_HIERARCHY_AND_NONALGEBRAIC_OS_PROFILE.

## Why this target is material

The protected debt says that reflection positivity alone is insufficient: every selected OS axiom and reconstruction hypothesis must hold for one four-dimensional limiting hierarchy.

That statement leaves two logically distinct burdens:

1. **closure burden:** if a common limiting hierarchy already exists, determine which exact OS properties automatically pass to it from approximants;
2. **construction/analytic burden:** construct the actual four-dimensional limiting hierarchy on one route and prove the properties that require topology, uniform estimates, or large-distance control.

R001 resolves the first burden for the algebraic/closed-cone core. This prevents future work from reproving exact invariances one-by-one after a legitimate common-domain limit, while equally preventing those inherited properties from being mistaken for the complete OS profile.

## Common-domain hypothesis

Let `A` be one complex Euclidean observable/test algebra and `A_+ subset A` its positive-time subalgebra. Let

- `theta` be the Euclidean time-reflection operation used by the selected OS profile;
- `alpha_g` denote the relevant Euclidean transformations on their admitted common domain;
- `beta_h` denote gauge transformations whenever gauge invariance is represented as an exact action on `A`;
- `omega_n : A -> C` be the Schwinger functional induced by the n-th hierarchy.

Assume that for every fixed `F in A`,

`omega_n(F) -> omega(F)`.

The point is the word **common**. If regulator-dependent observable spaces have not been transported to one identified algebra, this theorem cannot be invoked. Constructing those comparison maps belongs to the selected continuum route, not to R001.

## Result

Under the common-domain pointwise-convergence hypothesis, the following properties pass from every `omega_n` to `omega`:

- linearity;
- normalization `omega_n(1)=1`;
- every exact permutation/symmetry equality represented on `A`;
- Euclidean covariance/invariance equalities;
- gauge-invariance equalities on the common physical observable algebra;
- Osterwalder-Schrader reflection positivity:
  `omega_n(theta(F) F) >= 0` for every `F in A_+`, equivalently all finite reflection-positive Gram quadratic forms.

The proof uses only passage of equalities through pointwise limits and the fact that the limit of nonnegative real numbers is nonnegative.

## What does not follow

R001 does **not** infer:

- existence of the limit `omega`;
- continuity, temperedness, regularity, or the full selected growth bounds unless separately supplied by the convergence topology or uniform estimates;
- clustering, vacuum uniqueness, or a positive uniform decay scale;
- locality or any other condition not already encoded as one of the exact common-domain equalities covered by the theorem;
- construction or identification of the physical gauge-invariant observable hierarchy;
- reconstruction of a Hilbert-space QFT.

In particular, clustering is not closed under bare pointwise convergence in the approximation index. The scalar family

`C_n(t) = exp(-|t|/n)`

satisfies `C_n(t) -> 0` as `|t| -> infinity` for every fixed `n`, but for every fixed `t` one has `C_n(t) -> 1` as `n -> infinity`. The pointwise limiting correlation therefore does not cluster to zero. Uniform large-distance control is a separate obligation.

## Reduced D002 frontier

The remaining D002 work is no longer an undifferentiated instruction to “prove all OS axioms again after taking the limit.”

A selected four-dimensional route must still:

1. construct or identify one limiting gauge-invariant Schwinger hierarchy on a controlled common domain;
2. prove enough convergence/comparison structure to invoke R001 for the inherited algebraic OS core;
3. prove the nonalgebraic/topological part of the selected OS profile, including the required regularity/growth conditions;
4. prove the selected cluster/vacuum conditions with the uniformity needed to survive the continuum and infrared limits;
5. bind the same hierarchy to the physical observable construction required by D004 before invoking YM-T-120.

That successor is `YM-D002-R002 — SELECTED_4D_LIMIT_HIERARCHY_AND_NONALGEBRAIC_OS_PROFILE`.

## Claim boundary

This package proves a closure theorem conditional on a common-domain pointwise limit.

It does not construct four-dimensional Yang-Mills Schwinger functions, prove the complete OS profile, perform OS reconstruction, establish continuum existence, or establish a mass gap.

GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-COV-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-COV-B
assignment: CMDG-P3M-COV-WP-B
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Let (P := d.hom.app (op Point)). For an arbitrary one-point measure section (mu), define
[
a_mu(i) := measurePointIntegralFunctional X mu (integralBasis X i).
]
Let (W_mu) denote the Point section obtained from (weightedFiniteBooleanMeasureLimitLift X a_mu) using the all-true selector (basisBooleanPointProbe X (fun _ => true)) and the protected point-reweight construction.

Relative to the protected theorems (weightedFiniteBooleanMeasureLimitLift_point_reweight) and (kernelProductSection_reweight_eval), the parent target
[
d.hom.app (op Point)=0
]
follows from the single pointwise compatibility statement
[
orall mu,qquad P(mu)=P(W_mu).
]

Indeed the protected reweight/evaluation chain gives
[
P(W_mu)=kernelProductFunctional X d, a_mu.
]
Hence, if
[
hk : kernelProductFunctional X d = 0,
]
then for every (mu),
[
P(mu)=P(W_mu)=kernelProductFunctional X d,a_mu=0.
]
Pointwise extensionality therefore gives (P=0).

Thus the smallest new weighted one-point bridge is equality only after applying the Point component of (d). Full reconstruction of (mu), and even equality after (measurePointProjection), are not required for the vanishing argument.

## Derivation

Fix arbitrary (mu) and form its coordinate vector (a_mu) from the protected Nöbeling basis.

Construct the canonical weighted all-true Point section (W_mu) from (weightedFiniteBooleanMeasureLimitLift X a_mu).

Assume only the operational compatibility
[
h_{mathrm{apply}}(mu): P(mu)=P(W_mu).
]

By (weightedFiniteBooleanMeasureLimitLift_point_reweight), the all-true reweighted Point value of the weighted lift is the one used by the protected kernel-product section. By (kernelProductSection_reweight_eval), applying (P) to that value evaluates (kernelProductFunctional X d) on the same weight vector (a_mu). Therefore
[
P(mu)=kernelProductFunctional X d,a_mu.
]

From (hk), evaluation at (a_mu) is zero, so (P(mu)=0). Since (mu) was arbitrary, extensionality yields (P=0).

No use of (measurePointProjection_zero_reflects) is needed in this reduction.

## Assumptions beyond bootstrap

Exactly one additional compatibility lemma is required:

For every one-point measure section (mu), if (W_mu) is the all-true Point section of (weightedFiniteBooleanMeasureLimitLift X a_mu), then
[
d.hom.app (op Point),mu
=
d.hom.app (op Point),W_mu.
]

No equality (mu=W_mu) is assumed. No equality of their (measurePointProjection) values is assumed. No extra injectivity statement is assumed.

## Verification / falsification hooks

1. Full section reconstruction: sufficient but strictly stronger than required. If one proves (mu=W_mu), the needed applied equality follows immediately, but the reconstruction theorem carries unused information.

2. Equality only after (measurePointProjection): also stronger than the operational need. Together with zero-reflection, an additive difference argument can recover section equality and hence the applied equality, but that detour is unnecessary here.

3. Equality only after applying the Point component of (d): sufficient and is the minimal new compatibility statement exposed by this reduction.

4. Direct equality with (kernelProductFunctional X d a_mu): sufficient, but modulo the already protected point-reweight and kernel-product evaluation lemmas it is exactly the consequence of item 3. Therefore it is not a smaller new bridge; it merely fuses item 3 with protected evaluation.

A falsification attempt should therefore target item 3 directly: find (mu) for which its canonical weighted all-true representative (W_mu) has the same prescribed coordinates (a_mu) but (P(mu)
eq P(W_mu)). Such a counterexample would block the route even though the weighted representative itself is annihilated by (hk).

## Claim boundary

This proves only the reduction of the Point-component target to the stated applied compatibility lemma. It does not prove that lemma from the protected packet.

It does not claim equality of measure sections, mapping-out injectivity, coefficient solidity, (d=0), P3 completion, or CM4 completion.

The predecessor zero-reflection theorem is not consumed by the minimal route.

## Next residual

Prove or refute the single compatibility statement
[
orall mu,quad
d.hom.app (op Point),mu
=
d.hom.app (op Point),W_mu,
]
where (W_mu) is the all-true weighted Point section built from the basis coordinates (a_mu).

If it holds, the parent target (d.hom.app (op Point)=0) follows immediately from (hk) and the two protected reweight/evaluation theorems.
GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-SEP-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-B
assignment: CMDG-P3M-SEP-WP-B
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
For the singleton `Point := CompHaus.of PUnit`, the locally-constant-function layer is canonically one-dimensional: evaluation at the unique point and the constant-function map are mutually inverse. Consequently any scalar-valued linear functional `L` on locally constant functions on `Point` is determined by `L(1)), and `L = 0` iff `L(1) = 0`.

Applied to the protected measure-point chain, this proves the following exact reduction. Suppose the protected definitions satisfy the expected normalization
`measurePointFunctional X μ (const 1) = measurePointProjection X μ`
(respectively the identical statement for `measurePointIntegralFunctional`, after the protected integral/scalar identification). Then
`measurePointFunctional X μ = 0`
implies
`measurePointProjection X μ = 0`.
Moreover, under that normalization, injectivity of
`μ ↦ measurePointFunctional X μ`
is equivalent to injectivity of
`μ ↦ measurePointProjection X μ`; the singleton geometry itself supplies no further injectivity before the projection.

Thus the weakest sufficient one-point separation theorem is not a basis-separation statement. It is: the protected `measurePointProjection` must be faithful on the one-point measure-section type (equivalently, it must admit a left inverse there). Once this is proved, vanishing of the relevant measure-point functional forces the original one-point section to vanish.

## Derivation
Let `*` denote the unique element of `PUnit`. Define
`ev(f) := f(*)`
and
`const(a)(_) := a`.
Every function on `PUnit` is constant, hence for every locally constant `f`,
`const(ev(f)) = f`,
while plainly
`ev(const(a)) = a`.
Therefore `ev` and `const` are inverse linear identifications between locally constant scalar-valued functions on `Point` and the scalar module.

For any linear functional `L` on that locally constant function module and any `f`,
`f = const(ev(f)) = ev(f) • const(1)`.
By linearity,
`L(f) = ev(f) • L(const(1))`.
Hence `L` is completely determined by `L(const(1))), and `L=0` iff `L(const(1))=0).

Now take a one-point measure section `μ`. Under the protected normalization
`measurePointFunctional X μ (const 1) = measurePointProjection X μ`,
zero of `measurePointFunctional X μ` gives zero of `measurePointProjection X μ` by evaluation at `const 1`. If `measurePointProjection` is injective, this yields `μ=0`. Conversely, if `measurePointProjection` is not injective, choose nonzero `μ` in its kernel. The displayed formula makes the associated singleton functional zero, so no theorem using only that functional can recover `μ`. Thus projection injectivity is both sufficient and necessary for this route.

For the successor implication, `kernelProductFunctional X d = 0` can supply the separation hypothesis only through the protected construction that identifies its zero weighted-Boolean/product data with zero of the relevant `measurePointFunctional` or `measurePointIntegralFunctional` attached to the one-point component of `d`. On a singleton, once that functional is known to be zero, no further function-space argument is needed: evaluating at constant `1` gives zero projection, and projection faithfulness gives zero one-point section/component.

The packet does not expose the definition of `measurePointProjection` or a left-inverse theorem, so it is not logically valid from the supplied information alone to assert that this projection is injective. It also does not expose the exact definitional equation turning `kernelProductFunctional X d = 0` into vanishing of the relevant measure-point functional. Those are construction-level facts, not consequences of singleton geometry.

## Assumptions beyond bootstrap
NONE.

## Verification / falsification hooks
1. Check directly in the protected definitions that evaluation of `measurePointFunctional X μ` at the constant-one locally constant function reduces to `measurePointProjection X μ`; do the analogous check for `measurePointIntegralFunctional`.
2. Search for or prove a left inverse to `measurePointProjection X` on the exact one-point measure-section type. A left inverse immediately proves injectivity; a nonzero kernel element falsifies the proposed separation route.
3. Unfold `kernelProductFunctional` only far enough to verify that its zero equality entails zero of the relevant measure-point functional for the one-point component. If it yields only zero on a proper subfamily of tests, that remaining coverage statement must be proved separately.

## Claim boundary
This proves the singleton linear-algebra reduction and identifies the exact information bottleneck: all locally constant tests on `PUnit` collapse to the constant-one test, so functional separation is equivalent to faithfulness of the preceding projection. It does not prove `measurePointProjection` injective from the packet, does not prove the kernel-product-to-measure-point compatibility equation, and does not infer `d = 0`. No certification claim is made.

## Next residual
Prove or refute `measurePointProjection` injective by exhibiting its protected left inverse (or a nonzero kernel element), and verify the single definitional bridge from zero `kernelProductFunctional` data to zero of the associated one-point measure functional. If both hold, the successor implication `d.hom.app (op Point) = 0` follows by the constant-one evaluation argument above.
GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-SEP-WP-C-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-C
assignment: CMDG-P3M-SEP-WP-C
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
The protected packet alone does not imply separation of enriched one-point sections by the currently used scalar, integral, basis-coordinate, or weighted-Boolean/Nöbeling observables. There is a smallest explicit additive countermodel in which every later interface is faithful on the scalar information it receives, but the initial enriched-section projection has a nontrivial kernel.

Take the one-point enriched section group to be M := ℤ ⊕ ℤ and define the protected projection by
p : M → ℤ,  p(a,b) := a.
Let μ := (0,1). Then μ ≠ 0 but p(μ)=0. Interpret every downstream observable through p. For X a one-point profinite space, identify LocallyConstant X ℤ with ℤ and define the integral functional of (a,b) by
I_(a,b)(n) := a n.
Then I_μ=0 as a function, so in particular every integralBasis coordinate and every weighted-Boolean/Nöbeling probe vanishes. Thus the desired implication
(all currently used observables vanish) ⇒ μ=0
fails in a model satisfying every interface property stated in the protected packet.

The earliest nontrivial invisible direction is therefore allowed at interface (1), the projection from the enriched one-point section. A proof of actual separation needs an additional theorem excluding ker(measurePointProjection), or an equivalent left-inverse/extensionality statement.

## Derivation
Adversarial coverage, in the required order:

1. Projection from the enriched one-point section.
Set M=ℤ² and p(a,b)=a. Its kernel is {0}⊕ℤ, so μ=(0,1) is a concrete nonzero invisible vector. No injectivity, left inverse, or section-extensionality property for this projection is included in the protected packet.

2. Restriction to constant families on PUnit.
This stage need not create any kernel. For any abelian group A, let
c : A → (PUnit → A),  c(a)(*)=a,
and ev : (PUnit → A) → A,  ev(f)=f(*).
Then ev∘c=id_A, and c∘ev=id because two functions on PUnit agree once they agree at the unique point. Hence constant-family restriction can be modeled as an isomorphism.

3. Evaluation at the unique point.
The same equations show evaluation on PUnit is an isomorphism. Therefore the counterexample does not depend on loss of information at unique-point evaluation.

4. Lifted-integer descent.
Model this stage by id_ℤ. It is injective, so again no additional invisible direction is needed. This demonstrates that the failure can occur strictly before descent. The protected packet itself states no injectivity theorem for the real descent interface, so it cannot repair the earlier loss.

5. Basis-coordinate observation.
For one-point X, LocallyConstant X ℤ ≅ ℤ, with the single basis generator e=1. Define I_(a,b)(n)=an. Then the basis coordinate is I_(a,b)(e)=a. Thus basis observation is faithful on the scalar a supplied by p: if this basis coordinate vanishes, then a=0. For μ=(0,1), it vanishes because p(μ)=0.

6. Weighted-family realization.
On one-point X every Boolean locally constant function is 0 or 1, and every integer-weighted combination is an integer multiple of e. Its probe is therefore I_(a,b)(n)=an for some n∈ℤ. All such probes vanish for μ because a=0. Thus the weighted family can be fully realized without detecting the second coordinate.

Consequently, all downstream observations may be jointly faithful on im(p) while still being jointly non-faithful on M. Categorically, any observable family {q_j : ℤ → T_j} composed with p has common kernel containing ker(p). The protected predecessor statement that kernelProductFunctional X d=0 constrains only such downstream data and, absent an injectivity/extensionality theorem for the map from enriched one-point sections into that data, cannot force the enriched section itself to vanish.

No code is required; the model is checked by the displayed homomorphisms and the equality p(0,1)=0.

## Assumptions beyond bootstrap
NONE for the logical countermodel. The construction is not asserted to be the concrete implementation of measurePresheafObj; it shows that the stated protected interfaces do not rule out such a kernel.

## Verification / falsification hooks
1. Verify directly that ker(p)={0}⊕ℤ and μ=(0,1) is nonzero.
2. Verify c and ev on PUnit are mutual inverses by function extensionality.
3. Verify I_μ(n)=0 for every n∈ℤ, hence for the Nöbeling basis generator and every integer-weighted Boolean combination.
4. Falsify this countermodel as relevant to the concrete implementation by producing a protected theorem that measurePointProjection is injective, has a left inverse, or is jointly monic with another already-used observable. Any such theorem must act before the scalar/integral factorization.

## Claim boundary
This is a counterexample to derivability of one-point separation from the protected packet as stated, not a claim that the concrete Lean object measurePresheafObj actually contains a ℤ ghost summand. It proves that later PUnit evaluation, basis completeness, and weighted-family completeness cannot recover information already discarded by a noninjective enriched-section projection. It makes no certification, merge, or theorem-promotion claim.

## Next residual
Determine the concrete kernel of measurePointProjection at op Point. The smallest sufficient positive result is injectivity (or an explicit left inverse/extensionality theorem) for that projection; the smallest sufficient negative result is one actual nonzero section in its kernel.
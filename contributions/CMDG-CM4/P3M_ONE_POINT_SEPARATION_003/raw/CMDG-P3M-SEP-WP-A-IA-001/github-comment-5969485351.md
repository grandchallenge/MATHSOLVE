GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-SEP-WP-A-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-A
assignment: CMDG-P3M-SEP-WP-A
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Let (S := (measurePresheafObj X).obj (op Point)), and let
[
L:S	o operatorname{Hom}_{mathbb Z}(operatorname{LocallyConstant}(X,mathbb Z),mathbb Z),
qquad
L(mu):=measurePointIntegralFunctional,X,mu.
]
Let (B_i:=integralBasis,X,i), and (a_mu(i):=L(mu)(B_i)). Then the coordinate family (a_mu) determines (L(mu)) exactly, because (B) is a basis.

Consequently, any reconstruction procedure whose input is only (a_mu), including the stated all-true weighted-Boolean construction, can reconstruct every one-point section (mu) only if (L) is injective. More precisely, if (W(mu)) denotes the all-true weighted-Boolean section built from the weights (a_mu), then:

1. If the construction-side identity (L(W(mu))=L(mu)) holds for all (mu), and
2. the single lemma
[
measurePointIntegralFunctional_injective:
quad L(mu)=L(
u)Longrightarrow mu=
u
]
holds,

then (W(mu)=mu) for every (mu).

Conversely, if (W(mu)=mu) for every (mu), then (L) must be injective, because (L(mu)=L(
u)) implies (a_mu=a_
u), hence the weighted-Boolean inputs are identical and therefore (W(mu)=W(
u)), so (mu=
u).

Thus universal reconstruction from the basis-coordinate weights is equivalent, after the construction-side functional identity is checked, to the one named missing separation lemma: injectivity of (measurePointIntegralFunctional) on one-point measure sections. The protected packet does not supply that injectivity, so reconstruction of the section itself cannot be concluded from the admitted functional data alone.

## Derivation

Because (integralBasis,X) is a (mathbb Z)-basis of (LocallyConstant,X,mathbb Z), every (f) has a unique finite expansion
[
f=sum_i c_i B_i.
]
For any two (mathbb Z)-linear functionals (F,G), equality (F(B_i)=G(B_i)) for all (i) gives
[
F(f)=sum_i c_iF(B_i)=sum_i c_iG(B_i)=G(f),
]
so (F=G). Hence (a_mu=a_
u) if and only if (L(mu)=L(
u)).

Now define (W(mu)) to be the protected weighted-Boolean one-point section using weights (a_mu) and the all-true selector. The input to (W) depends only on (a_mu). Therefore if (L(mu)=L(
u)), then (a_mu=a_
u), so (W(mu)=W(
u)).

Necessity: if (W(eta)=eta) for every section (eta), then from (L(mu)=L(
u)) we obtain
[
mu=W(mu)=W(
u)=
u.
]
Thus (L) is injective.

Sufficiency: suppose the construction-side functional identity (L(W(mu))=L(mu)) is verified. If (L) is injective, then this equality immediately gives (W(mu)=mu).

This also isolates the falsification hooks. Since (L) is a composite through the protected projection/linear-functional/downward-lift interfaces, noninjectivity of any information-losing stage that survives into the composite gives distinct one-point sections with the same (L), and then no coordinate-only reconstruction can recover both. In particular, the Nöbeling basis solves only the linear-functional reconstruction problem; it does not by itself prove section reconstruction.

## Assumptions beyond bootstrap

NONE. The statement is a reduction: it does not assume the missing injectivity lemma or the construction-side identity. It proves exactly that these are the remaining logical requirements, and that injectivity is necessary for any reconstruction depending only on the coordinate vector.

## Verification / falsification hooks

1. Verify basis extensionality directly: two (mathbb Z)-linear maps on (LocallyConstant,X,mathbb Z) agreeing on every (integralBasis,X,i) must be equal.
2. For the protected all-true weighted-Boolean constructor, compute its integral functional on each basis vector. If the value is (a_mu(i)) for every (i), basis extensionality yields (L(W(mu))=L(mu)).
3. Test injectivity of (measurePointIntegralFunctional) directly. Any (mu
eq
u) with equal integral functionals is an immediate counterexample to universal coordinate reconstruction. Equivalently, inspect whether (measurePointProjection), the restriction implicit in (measurePointProjectionLinear), (measurePointFunctional), or (liftedIntFunctionalDown) has a nontrivial kernel that produces such a pair.
4. If injectivity is proved, combine it with hook 2 to obtain the desired reconstruction identity in one line.

## Claim boundary

The basis-coordinate vector reconstructs the protected integral functional exactly. It does not, from the supplied packet alone, reconstruct an arbitrary one-point measure section. Universal section reconstruction requires and in fact forces injectivity of (measurePointIntegralFunctional); after the weighted-Boolean constructor is shown to reproduce the same integral functional, that injectivity is sufficient. No certification or campaign-level claim is made.

## Next residual

Prove or refute (measurePointIntegralFunctional_injective) on one-point sections. Independently check the all-true constructor on basis vectors; if both checks pass, the full reconstruction theorem follows immediately.
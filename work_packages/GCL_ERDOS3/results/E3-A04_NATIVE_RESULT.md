# E3-A04 — native common-core no-go for synchronized counterexamples

Disposition: **ADVERSARIAL_CLASS_RULED_OUT__MISALIGNMENT_REQUIRED**.

This is a native adversarial result. It uses only the exact D01 vertical carry-free family and elementary set theory.

## Strongest exact statement

Let
[
N=2^n,qquad r=r_4(N),qquad a_n=r/N.
]

Suppose four fibres
[
B_0,B_1,B_2,B_3subseteq[0,N-1]
]
form a globally 4-AP-free four-block gluing
[
A=igcup_{i=0}^3(iN+B_i).
]

Assume there exists a common reference set
[
Rsubseteq[0,N-1],qquad |R|=r,
]
such that
[
|Rsetminus B_i|le h
qquad	ext{for every }i.
]

Then necessarily
[
oxed{hge r/4.}
]

In particular this applies when every (B_i) is obtained from one common local extremizer (R) by deleting at most (h) points.

Since (r=Na_n),
[
hge rac14 Na_n.
]

Therefore for every fixed (0<	heta<1),
[
hge rac14 Na_n
ge
rac14 Na_n^{1+	heta},
]
because (0<a_nle1).

Thus **the entire synchronized common-core deletion class satisfies a stronger deficit bound than the tranche-04 target and cannot furnish a counterexample to the (L=2) route.**

## Proof

The D01 family
[
F_{16}=(i,q,	ext{carry})=(0,1,0000)
]
contains the vertical progressions
[
(u,N+u,2N+u,3N+u),
qquad 0le u<N.
]

Therefore global 4-AP-freeness forces
[
B_0cap B_1cap B_2cap B_3=arnothing.
]

Inside the common reference set (R),
[
Rsetminus(B_0cap B_1cap B_2cap B_3)
=
igcup_{i=0}^3(Rsetminus B_i).
]

Hence
[
r
=
|R|
le
sum_{i=0}^3|Rsetminus B_i|
le4h.
]

Thus
[
hge r/4.
]

No estimate on the other 16 carry families is needed.

## Corollary — synchronized recursive products are not the adversarial route

Any recursive/no-carry construction in which the four child fibres retain all but (h) points of one common parent extremizer must pay
[
hge r_4(N)/4.
]

Consequently, a counterexample with
[
h=o!left(Na_n^{1+	heta}ight)
]
cannot arise from a common-core deletion recursion.

The same obstruction applies to any proposed construction for which a set (R) of size (r_4(N)) is contained in all four fibres up to at most (h) missing points per fibre, even if the fibres also contain additional points outside (R).

## What is not ruled out

The theorem does **not** control deliberately misaligned near-extremizers.

In particular it does not rule out:
- distinct affine/Freiman images of a large 4-AP-free set;
- independently translated near-extremizers with small four-way intersection;
- quadratic level sets with different phases;
- recursive constructions whose child fibres are structurally related but have no large common pointwise core.

Those are now the only serious adversarial directions among the originally listed synchronized/product families.

## Adversarial significance

The easiest way to evade cross-fibre APs would have been to inherit nearly the same local extremizer in all four blocks and make a small number of repairs. The vertical carry-free family alone forbids this at the required scale.

Indeed it forces a deficit of order
[
Na_n,
]
whereas the target theorem asks only for order
[
Na_n^{1+	heta}.
]

For small (a_n), the synchronized-class lower bound is parametrically stronger.

## First unresolved adversarial direction

The counterexample search must now break pointwise synchronization.

A genuine threat to the (L=2) route must construct four individually near-extremal fibres whose common intersection is already small while simultaneously arranging all nonvertical carry families.

The smallest remaining adversarial question is:

> Can four affine/Freiman/quadratically misaligned near-extremizers make every D01 carry family compatible while each fibre loses only (o(Na_n^{1+	heta})) points for some (	heta<1)?

No such family is constructed here.

## Frontier effect

- No counterexample to E3-B-FOUR-FIBRE-DEFICIT is found.
- Common-core deletion/product recursion is **ruled out as a counterexample mechanism**.
- E3-Q4-DENSITY-LOSS remains **OPEN**.
- The adversarial lane narrows to deliberately misaligned structured fibres.

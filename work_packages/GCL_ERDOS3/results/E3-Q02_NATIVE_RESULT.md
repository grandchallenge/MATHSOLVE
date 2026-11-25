# E3-Q02 — native labelled U3 forcing lemma

Disposition: **PROVED_NATIVE_LABELLED_FORCING**.

This result uses the protected E3-S04 carry-to-cyclic embedding and an elementary generalized von Neumann inequality for the four-term progression system.

## Statement

Fix (N=2^n) and any valid cross-fibre D01 carry template for (m=4).

Let the physical fibres be
[
B_0,B_1,B_2,B_3subseteq[0,N-1],
]
and suppose every physical fibre used by the template has density at least
[
|B_j|ge eta N.
]

For the template
[
j_t=i+tq+c_t,qquad t=0,1,2,3,
]
define, exactly as in protected E3-S04,
[
C_t:=c_tN+B_{j_t}.
]

Choose a prime
[
8N<P<16N
]
and regard each (C_t) as a subset of (G=mathbb Z/Pmathbb Z).

Write
[
ho_t:=|C_t|/P,
qquad
g_t:=1_{C_t}-ho_t.
]

If the four-fibre gluing is globally 4-AP-free, then the mixed labelled 4-AP average vanishes:
[
Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})
:=
mathbb E_{x,din G}
prod_{t=0}^{3}1_{C_t}(x+td)
=0.
]

Then
[
oxed{
max_{0le tle3}|g_t|_{U^3(G)}
ge
rac{ho_0ho_1ho_2ho_3}{15}
}
]
and therefore, since (P<16N),
[
oxed{
max_t|g_t|_{U^3(G)}
>
rac{eta^4}{15cdot16^4}.
}
]

Thus **every valid D01 cross-fibre template in a globally 4-AP-free gluing of (eta)-dense fibres forces labelled quadratic nonuniformity at an explicit polynomial scale (ceta^4)**.

This is stronger, at the norm-forcing stage, than the (eta^{16})/(eta^{32})-scale degree-uniformity thresholds recorded in the older Gowers formulation used by E3-S04.

It does not by itself imply any deletion or gluing-radius lower bound.

## Lemma — generalized von Neumann for labelled 4-APs

Let (G=mathbb Z/Pmathbb Z) with (P>3) prime. For functions
[
f_0,f_1,f_2,f_3:G	omathbb C,
qquad |f_i|le1,
]
define
[
Lambda(f_0,f_1,f_2,f_3)
=
mathbb E_{x,d}
f_0(x)f_1(x+d)f_2(x+2d)f_3(x+3d).
]

Then, for every (jin{0,1,2,3}),
[
|Lambda(f_0,f_1,f_2,f_3)|
le
|f_j|_{U^3(G)}.
]

### Derivation

Apply Cauchy-Schwarz three times, each time eliminating one of the other three bounded factors. After invertible linear changes of variables in (G), the eighth power of the remaining expression is bounded by the (3)-dimensional multiplicative cube average
[
mathbb E_{x,h_1,h_2,h_3}
prod_{omegain{0,1}^3}
mathcal C^{|omega|}
f_j(x+omegacdot h),
]
which is exactly
[
|f_j|_{U^3(G)}^8.
]

The coefficients (1,2,3) are invertible because (P>3). Relabelling the four forms gives the inequality for any chosen factor.

This is the standard complexity-two generalized von Neumann argument; no one-set replacement is used.

## Proof of the forcing bound

Expand
[
1_{C_t}=ho_t+g_t.
]

Then
[
0
=
Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})
=
ho_0ho_1ho_2ho_3
+
sum_{arnothing
e Ssubseteq{0,1,2,3}}
left(prod_{t
otin S}ho_tight)
Lambda_S,
]
where (Lambda_S) is the labelled progression correlation with (g_t) in positions (tin S) and the constant function (1) elsewhere.

For every nonempty (S), choose any (jin S). By the generalized von Neumann lemma,
[
|Lambda_S|
le
|g_j|_{U^3}
le
eta,
qquad
eta:=max_t|g_t|_{U^3}.
]

Since every (ho_tle1) and there are (2^4-1=15) nonempty subsets,
[
ho_0ho_1ho_2ho_3
le15eta.
]

Therefore
[
etagerac{ho_0ho_1ho_2ho_3}{15}.
]

The S04 embedding preserves cardinality:
[
|C_t|=|B_{j_t}|geeta N.
]
Because (P<16N),
[
ho_t>eta/16.
]

Hence
[
eta
>
rac{(eta/16)^4}{15}
=
rac{eta^4}{15cdot16^4}.
]

## Carry-template coverage

The argument applies to **every** valid cross-fibre D01 template, including templates in which two labelled positions use the same physical fibre.

The multilinear inequality is four-**labelled**-function, not four-distinct-set. If two terms arise from the same (B_j), their translated sets (C_t=c_tN+B_j) are still legitimate separate labelled factors.

The protected S04 mapping proves that a mixed modular 4-AP across the (C_t) pulls back to an ordinary integer 4-AP in the original gluing. Choosing (P>8N) prevents modular wrap. S04 also checks that the degenerate modular progression does not create a spurious contribution for a genuinely cross-block template.

Therefore zero global cross-fibre AP count gives exactly the zero mixed average used above.

## Relation to E3-S04

E3-S04 already established, from Gowers 2001, that zero mixed count forces degree-1 or degree-2 nonuniformity at polynomial scale. In its parameterization, taking (gammaasympeta^4) yields uniformity thresholds of orders (eta^{16}) and (eta^{32}).

The present native derivation changes coordinates to the normalized (U^3) norm and uses the four-function generalized von Neumann inequality directly. At this level the forced norm is already order
[
eta^4.
]

No contradiction exists: the two statements use different uniformity parameters/definitions. The new result simply records the sharper norm-level interface relevant for the next structural step.

## First defect

The remaining gap is no longer “prove dense compatible fibres are quadratically nonuniform.”

That is now explicit:
[
max_t|1_{C_t}-ho_t|_{U^3}
ge ceta^4.
]

The first missing theorem is:

> **near-extremal quadratic structure to deletion.** Convert the forced (U^3) mass (ceta^4), together with the fact that each physical fibre is internally 4-AP-free and near the extremal density (a_n), into a carry-transversal/deletion cost
> [
> gtrsim eta^{1+	heta}N
> ]
> for some (	heta<1).

A generic inverse theorem alone does not provide that exponent conversion.

## Quantitative implication for tranche 04

The forcing stage loses exponent (4) in the density:
[
etamapsto ceta^4
]
at the (U^3)-norm level.

Therefore any successful T01 route must exploit **near-extremality or repeated carry-template structure** to gain back exponent before converting structure to point deletions.

A generic “large (U^3) implies one quadratic correlation, then count edges, divide by maximum degree” route is not enough: it reproduces the already-known exponent obstruction.

## Frontier effect

- E3-Q02 is **PROVED_NATIVE_LABELLED_FORCING**.
- E3-Q4-DENSITY-LOSS remains **OPEN**.
- E3-Q4-GLUING-RADIUS remains **unpromoted**.
- E3-B-FOUR-FIBRE-DEFICIT remains **OPEN**.
- Tranche 04 is reduced to two live mathematical questions:
  1. can the finite L01 motif be amplified at scale;
  2. can forced (U^3) structure be converted to a subquadratic-exponent carry-transversal deficit?

## Protected basis

- E3-S04 result blob: `30f24cff18d14ac197695e272868786b0e77cd0c`.
- E3-D01 result blob: `fa48b4dca2e575d639cd6ca3cae7d9064063c3cb`.
- No sibling tranche-04 return was used.

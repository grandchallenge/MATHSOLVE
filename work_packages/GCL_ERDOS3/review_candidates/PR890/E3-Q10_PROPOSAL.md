# E3-Q10 — de-windowed geometry-bias versus joint-correlation dichotomy

Disposition: **PROVED_NATIVE_DEWINDOWED_CANCELLATION_DICHOTOMY**.

This is native GCL work. It refines protected E3-Q09 by retaining the exact cancellation terms after local de-windowing rather than only their individual (U^3) consequence.

## Strongest exact statement

Fix one family (F) in the exact ten-family L01 core. Use the Q09 notation
[
C_t=c_tN+B_{j_t},qquad
I_t=c_tN+[0,N-1],qquad
alpha_t=rac{|B_{j_t}|}{N}geeta,
]
and
[
h_t:=1_{C_t}-alpha_t1_{I_t}.
]

Let
[
Lambda_F(f_0,f_1,f_2,f_3)
:=
mathbb E_{x,dinmathbb Z/Pmathbb Z}
prod_{t=0}^{3}f_t(x+td).
]

Protected Q09 proves that the pure-window baseline
[
W_F
:=
Lambda_F(
alpha_01_{I_0},
alpha_11_{I_1},
alpha_21_{I_2},
alpha_31_{I_3})
]
satisfies
[
W_F>rac{eta^4}{16^4}.
]

Because the global gluing is 4-AP-free,
[
0
=
W_F+
sum_{arnothing
e Ssubseteq{0,1,2,3}}T_{F,S},
]
where (T_{F,S}) is obtained by using (h_t) in positions (tin S) and (alpha_t1_{I_t}) in the other positions.

Define
[
delta_eta:=rac{eta^4}{15cdot16^4}.
]

Then for every L01 core family (F),

[
oxed{
max_{arnothing
e Ssubseteq{0,1,2,3}}
|T_{F,S}|>delta_eta.
}
]

Consequently every family satisfies exactly one of the following two nonexclusive branches.

### Branch G — singleton geometry bias

For some labelled position (j),
[
|T_{F,{j}}|>delta_eta.
]

Define the deterministic carry-section weight
[
w_{F,j}(y)
:=
mathbb E_d
prod_{t
e j}
1_{I_t}igl(y+(t-j)digr).
]

Then
[
T_{F,{j}}
=
left(prod_{t
e j}alpha_tight)
mathbb E_y h_j(y)w_{F,j}(y).
]

Since
[
mathbb E_y h_j(y)=0,
]
we may subtract any constant. In particular, with
[
overline w_{F,j}
:=
rac1Nsum_{yin I_j}w_{F,j}(y),
]
we have
[
mathbb E_y h_j(y)w_{F,j}(y)
=
mathbb E_y h_j(y)
igl(w_{F,j}(y)-overline w_{F,j}igr).
]

Because every (alpha_tle1),
[
oxed{
left|
mathbb E_y h_j(y)
igl(w_{F,j}(y)-overline w_{F,j}igr)
ight|
>
delta_eta.
}
]

Thus a large singleton term is an explicit correlation of the locally centered fibre fluctuation with a deterministic nonconstant support/carry geometry weight.

### Branch J — genuine multi-fluctuation correlation

For some set (S) with
[
|S|ge2,
]
[
oxed{
|T_{F,S}|>delta_eta.
}
]

Every function in the multilinear average is bounded by (1). The generalized von Neumann inequality used in Q02/Q09 therefore gives, for every (jin S),
[
|T_{F,S}|
le
|h_j|_{U^3}.
]

Hence
[
oxed{
|h_j|_{U^3}>delta_eta
qquad
	ext{for every labelled }jin S.
}
]

So this branch retains an actual large multilinear correlation involving at least two de-windowed fluctuations, rather than merely concluding that one factor has large (U^3).

## All-distinct-family strengthening

Protected Q07 records that both
[
F_{15},F_{16}
]
have physical block word
[
(0,1,2,3).
]

Therefore every two distinct labelled positions in either family correspond to two distinct physical fibres.

For each of (F_{15}) and (F_{16}), Q10 therefore gives the sharper dichotomy:

> either one physical fibre has a singleton geometry-bias correlation larger than (delta_eta), or there is a de-windowed multilinear correlation larger than (delta_eta) involving fluctuations from at least two distinct physical fibres.

Thus the all-distinct core cannot hide every cancellation inside a repeated copy of one structured fibre.

## Proof

The proof is elementary.

From
[
0=W_F+sum_{arnothing
e S}T_{F,S}
]
and
[
W_F>rac{eta^4}{16^4},
]
we have
[
sum_{arnothing
e S}|T_{F,S}|
ge W_F
>
rac{eta^4}{16^4}.
]

There are exactly
[
2^4-1=15
]
nonempty subsets (S). Therefore at least one satisfies
[
|T_{F,S}|
>
rac{eta^4}{15cdot16^4}
=
delta_eta.
]

If (|S|=1), the change of variables
[
y=x+jd
]
gives
[
T_{F,{j}}
=
left(prod_{t
e j}alpha_tight)
mathbb E_{y,d}
h_j(y)
prod_{t
e j}
1_{I_t}igl(y+(t-j)digr),
]
which is exactly the stated deterministic weight correlation.

Also
[
sum_y h_j(y)
=
|C_j|-alpha_j|I_j|
=
|B_{j_j}|-rac{|B_{j_j}|}{N}N
=0.
]
So subtracting (overline w_{F,j}) changes nothing.

If (|S|ge2), Q02's generalized von Neumann inequality applies to the same four-term progression form. Every window factor (alpha_t1_{I_t}) has modulus at most (1), and every (h_t) has modulus at most (1). Choosing any (jin S) as the controlling factor gives
[
|T_{F,S}|le|h_j|_{U^3}.
]
This holds for every (jin S).

No inverse theorem or external quantitative input is used.

## What Q10 changes

Q09 proved that each L01 family contains at least one de-windowed (U^3)-structured labelled factor.

Q10 identifies the precise mechanism that must cancel the positive support-window baseline:

1. **geometry branch:** one locally centered fibre correlates with a deterministic carry-section weight; or
2. **joint branch:** at least two labelled fluctuations participate in one genuinely large de-windowed multilinear correlation.

For the two all-distinct families (F_{15},F_{16}), the joint branch automatically involves at least two different physical fibres.

This is narrower than the previous residual because a future proof no longer needs to start from arbitrary large (U^3) mass. It may attack the explicit geometry weights in Branch G and the explicit multi-fluctuation correlations in Branch J separately.

## Claim boundary

Q10 does **not** prove:
- that Branch G is impossible;
- that Branch J produces aligned Fourier or quadratic witnesses;
- that either branch forces a deletion cost;
- that all four physical fibres are intrinsically structured;
- or that the four-fibre deficit theorem holds.

A singleton geometry-bias term may in principle be large for a near-extremal AP-free fibre. A multi-fluctuation term may also fail to align with the corresponding term from another carry family.

## First defect

The quadratic/de-windowed residual reduces to:

> **E3-B-DEWINDOWED-GEOMETRY-OR-JOINT-INCOMPATIBILITY.**  
> Across the L01 core, prove that the deterministic singleton geometry-bias correlations and the genuine multi-fluctuation correlations supplied by Q10 cannot all be realized by four near-extremal internally 4-AP-free fibres without deleting
> [
> gtrsimeta^{1+	heta}N
> ]
> points for some (0<	heta<1).

Two concrete sub-lanes are now exposed:

1. **geometry-weight lane:** compute/compare the exact weights (w_{F,j}) and show that the required large signed biases are incompatible with near-extremality or internal 4-AP-freeness;
2. **joint-correlation lane:** on (F_{15},F_{16}) and then the remaining core, align the large multi-(h) correlations into shared derivative-frequency or quadratic witnesses.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-DEWINDOWED-U3-FORCING`: remains **PROVED_NATIVE**.
- New lemma `E3-B-DEWINDOWED-CANCELLATION-DICHOTOMY`: **PROVED_NATIVE**.
- `E3-B-DEWINDOWED-JOINT-WITNESS`: **REDUCED**.
- New smallest de-windowed residual: `E3-B-DEWINDOWED-GEOMETRY-OR-JOINT-INCOMPATIBILITY`.
- The linear residual `E3-B-LINEAR-WITNESS-APFREE-INTERVAL-AMPLIFICATION` remains open.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q09 native result: de-windowed (U^3) forcing and exact positive window baseline.
- E3-Q02 native result: generalized von Neumann inequality on the labelled 4-AP form.
- E3-Q07 native result: physical block words, including all-distinct (F_{15},F_{16}).

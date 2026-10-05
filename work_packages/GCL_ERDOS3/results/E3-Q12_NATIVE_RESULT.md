# E3-Q12 — exact carry-localized cancellation dichotomy

Disposition: **PROVED_NATIVE_CARRY_LOCALIZED_CANCELLATION**.

This is native GCL work. It implements the localization demanded by Q11 directly in the original D01 integer variables, before the unrestricted cyclic averaging step.

## Strongest exact statement

Let
[
N=2^n,qquad nge4,
]
and let
[
B_0,B_1,B_2,B_3subseteq[0,N-1]
]
be physical fibres whose translated union in ([0,4N)) is globally 4-AP-free.

Assume every physical fibre used below has density at least
[
eta:
qquad
|B_j|geeta N.
]

Fix one family
[
F=(i,q,c)
]
in the exact ten-family L01 core, with carry vector
[
c=(c_0,c_1,c_2,c_3).
]

Define the exact D01 carry cell
[
Omega_c(N)
:=
left{
(u,v)in[0,N-1]^2:
leftlfloorrac{u+tv}{N}ightfloor=c_t
	ext{ for }t=0,1,2,3
ight}.
]

The physical block label at position (t) is
[
j_t=i+tq+c_t,
]
and the corresponding local residue is
[
r_t(u,v):=u+tv-c_tNin[0,N-1].
]

Write
[
alpha_t:=rac{|B_{j_t}|}{N}geeta,
qquad
h_t(r):=1_{B_{j_t}}(r)-alpha_t.
]

Define the normalized exact carry-localized progression functional
[
Lambda_F^{mathrm{loc}}(f_0,f_1,f_2,f_3)
:=
rac1{N^2}
sum_{(u,v)inOmega_c(N)}
prod_{t=0}^{3}f_t(r_t(u,v)).
]

Because every point of (Omega_c(N)) generates an ordinary integer 4-AP in the four-fibre gluing and the gluing is globally 4-AP-free,
[
Lambda_F^{mathrm{loc}}
(1_{B_{j_0}},1_{B_{j_1}},1_{B_{j_2}},1_{B_{j_3}})
=0.
]

Protected Q09 gives, for every carry vector appearing in the ten-family L01 core,
[
|Omega_c(N)|gerac{N^2}{256}.
]

Therefore the pure density baseline satisfies
[
W_F^{mathrm{loc}}
:=
rac{|Omega_c(N)|}{N^2}
prod_{t=0}^{3}alpha_t
ge
rac{eta^4}{256}.
]

Expanding
[
1_{B_{j_t}}=alpha_t+h_t
]
inside the exact localized functional gives
[
0
=
W_F^{mathrm{loc}}
+
sum_{arnothing
e Ssubseteq{0,1,2,3}}
T_{F,S}^{mathrm{loc}},
]
where
[
T_{F,S}^{mathrm{loc}}
:=
rac1{N^2}
sum_{(u,v)inOmega_c(N)}
left(prod_{tin S}h_t(r_t(u,v))ight)
left(prod_{t
otin S}alpha_tight).
]

There are exactly 15 nonempty subsets (S). Hence

[
oxed{
max_{arnothing
e S}
|T_{F,S}^{mathrm{loc}}|
ge
rac{eta^4}{15cdot256}
=
rac{eta^4}{3840}.
}
]

This is an exact family-specific localized witness. It does not pass through the Q02 unrestricted cyclic quotient and therefore does not identify gauge-distinct families such as (F_{15}) and (F_{16}).

## Singleton branch — exact carry geometry bias

Suppose the large term has
[
S={j}.
]

Define
[
m_{F,j}(r)
:=
rac1N
#left{
(u,v)inOmega_c(N):
r_j(u,v)=r
ight}.
]

For fixed (r), there are at most (N) pairs ((u,v)), so
[
0le m_{F,j}(r)le1.
]

Then
[
T_{F,{j}}^{mathrm{loc}}
=
left(prod_{t
e j}alpha_tight)
rac1N
sum_{r=0}^{N-1}
h_j(r)m_{F,j}(r).
]

Because
[
rac1Nsum_r h_j(r)=0,
]
let
[
overline m_{F,j}
:=
rac1Nsum_r m_{F,j}(r).
]

Then
[
rac1Nsum_r h_j(r)m_{F,j}(r)
=
rac1Nsum_r
h_j(r)
igl(m_{F,j}(r)-overline m_{F,j}igr).
]

Since every (alpha_tle1), a large singleton term implies
[
oxed{
left|
rac1Nsum_r
h_j(r)
igl(m_{F,j}(r)-overline m_{F,j}igr)
ight|
ge
rac{eta^4}{3840}.
}
]

Thus the singleton branch is now an exact correlation with a **family-specific D01 carry-cell section weight**, not a support-window artifact.

## Multi-fluctuation branch

If the large set satisfies
[
|S|ge2,
]
then
[
oxed{
left|
rac1{N^2}
sum_{(u,v)inOmega_c(N)}
prod_{tin S}h_t(r_t(u,v))
ight|
ge
rac{eta^4}{3840}.
}
]

Here we used only
[
prod_{t
otin S}alpha_tle1.
]

This is a genuine exact carry-localized correlation of at least two labelled fluctuations.

Unlike Q10, no unrestricted cyclic generalized von Neumann step is applied here. The carry-cell restriction is retained because Q11 proves that dropping it can erase family identity.

## All-distinct strengthening

For protected L01 families
[
F_{15}=(0,0,0123),
qquad
F_{16}=(0,1,0000),
]
the physical block word is
[
(0,1,2,3).
]

Therefore any localized multi-fluctuation term with
[
|S|ge2
]
in either family automatically contains fluctuations from at least two distinct physical fibres.

Moreover, unlike in the unrestricted cyclic formulation, the two exact cells are different:
[
Omega_{0123}(N)

e
Omega_{0000}(N).
]

Thus Q12 restores precisely the family distinction lost in Q11.

## Quantitative improvement over Q09/Q10

Q09/Q10 use the cyclic embedding with
[
8N<P<16N
]
and obtain the scale
[
rac{eta^4}{15cdot16^4}.
]

Q12 works directly on the integer carry cell and obtains
[
rac{eta^4}{15cdot256}.
]

The ratio is
[
rac{16^4}{256}=256.
]

So exact carry localization improves the retained cancellation scale by a factor of (256) while preserving family identity.

This factor is not yet the exponent gain needed for the four-fibre deficit theorem; the key advance is structural, not merely constant-level.

## Relation to Q11

Q11 proves that the unrestricted cyclic average is invariant under
[
qmapsto q+s,
qquad
c_tmapsto c_t-ts.
]

Q12 does not average over all cyclic steps. It restricts to the exact integer cell
[
Omega_c(N).
]

That restriction is not invariant under the Q11 gauge transformation. Hence the family-specific information survives.

The distinction between (F_{15}) and (F_{16}) is therefore restored exactly where L01 needs it.

## Claim boundary

Q12 does not prove:
- a lower bound on the number of independent localized witnesses;
- alignment of localized multi-fluctuation correlations across families;
- incompatibility of the singleton carry-section weights with near-extremal AP-free fibres;
- a deletion cost;
- or the four-fibre deficit theorem.

It also does not assert a (U^3) bound for the restricted multi-fluctuation term; a localized inverse/counting theorem would be an additional step.

## First defect

The live residual reduces to:

> **E3-B-CARRY-LOCALIZED-GEOMETRY-OR-MULTICORRELATION.**  
> Across the ten-family L01 core, use the exact Q12 carry-section weights and localized multi-fluctuation correlations to prove that four near-extremal internally 4-AP-free fibres cannot satisfy all family constraints without deleting
> [
> gtrsimeta^{1+	heta}N
> ]
> points for some (0<	heta<1).

The immediate concrete subproblems are now:

1. compute and compare the exact section weights (m_{F,j}), especially across mandatory/core families;
2. determine whether the localized multi-fluctuation forms admit a useful Fourier/derivative decomposition without reintroducing the Q11 gauge quotient;
3. amplify the family-specific localized witnesses using near-extremality or repeated scale structure.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- New lemma `E3-B-CARRY-LOCALIZED-CANCELLATION`: **PROVED_NATIVE**.
- `E3-B-CARRY-LOCALIZED-JOINT-WITNESS`: **REDUCED**.
- New smallest de-windowed/carry residual: `E3-B-CARRY-LOCALIZED-GEOMETRY-OR-MULTICORRELATION`.
- The linear residual `E3-B-LINEAR-WITNESS-APFREE-INTERVAL-AMPLIFICATION` remains open.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-D01 exact carry compiler.
- E3-L01 ten-family core.
- E3-Q09 exact carry-cell lower bounds.
- E3-Q11 coarse-step/carry gauge equivalence.

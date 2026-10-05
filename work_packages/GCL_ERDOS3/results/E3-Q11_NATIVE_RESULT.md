# E3-Q11 — singleton carry kernel forces a boundary density increment

Disposition: **PROVED_NATIVE_SINGLETON_BOUNDARY_DENSITY_INCREMENT**.

This is native GCL work. It sharpens the positional branch exposed by Q10. It uses only the exact universal singleton kernel, discrete summation by parts, and the protected Q10 threshold.

## Strongest exact statement

Let
[
N=2^n,qquad nge4,
]
and let
[
Bsubseteq[0,N-1]
]
be one physical fibre with density
[
alpha=rac{|B|}{N}.
]

Write
[
h(u):=1_B(u)-alpha
qquad(0le ule N-1),
]
so
[
sum_{u=0}^{N-1}h(u)=0.
]

Let
[
P>8N
]
be the Q02 prime cyclic ambient size, and let
[
K_j(u)
=
mathbb E_{dinmathbb Z/Pmathbb Z}
prod_{t
e j}
1_{[0,N-1]}igl(u+(t-j)digr),
qquad
jin{0,1,2,3}.
]

By Q10, these are exactly the physical-coordinate singleton kernels for both all-distinct L01 families (F_{15}) and (F_{16}).

Set
[
delta_eta
:=
rac{eta^4}{15cdot16^4}.
]

Assume
[
Neta^4>15360.
]

Then:

### 1. Endpoint singleton witnesses are impossible

For
[
jin{0,3},
]
one has the deterministic bound
[
oxed{
left|
mathbb E_{uinmathbb Z/Pmathbb Z}
h(u)K_j(u)
ight|
<
rac1{64N}
<
delta_eta.
}
]

Therefore a Q10 Alternative-A singleton witness at scale (>delta_eta) cannot occur in labelled position (0) or (3).

### 2. A middle singleton witness gives a boundary density increment

Suppose
[
jin{1,2}
]
and
[
left|
mathbb E h(u)K_j(u)
ight|
>
delta_eta.
]

Then there exists a nonempty proper boundary interval
[
Jsubsetneq[0,N-1]
]
which is either a prefix
[
J=[0,m]
]
or a suffix
[
J=[m+1,N-1],
]
such that
[
oxed{
|Bcap J|-alpha|J|
>
rac{eta^4}{30720},N.
}
]

In particular
[
oxed{
rac{|Bcap J|}{|J|}
>
alpha+rac{eta^4}{30720}.
}
]

Since (Bcap J) is itself 4-AP-free,
[
oxed{
rac{r_4(|J|)}{|J|}
>
alpha+rac{eta^4}{30720}.
}
]

Thus every surviving Q10 singleton witness produces a genuine density increment on a strictly smaller boundary interval.

## Proof

Put
[
M:=N-1.
]

Because all four points of the relevant modular progression lie in an interval of length (N) and
[
P>8N,
]
there is no modular-wrap ambiguity. After choosing the unique consecutive difference representative in ((-(N-1),N-1)), the singleton kernel is exactly
[
K_j(u)=rac{L_j(u)}P,
]
where
[
L_j(u)
=
#left{
dinmathbb Z:
0le u+(t-j)dle M
	ext{ for every }t=0,1,2,3
ight}.
]

### 1. Exact endpoint kernel

For (j=0), the four points are
[
u, u+d, u+2d, u+3d.
]

The endpoint conditions are equivalent to
[
-rac u3le dlerac{M-u}3.
]

Hence
[
L_0(u)
=
leftlfloorrac{M-u}{3}ightfloor
+
leftlfloorrac u3ightfloor
+1.
]

Writing
[
M=3q+r,
qquad
u=3a+s,
qquad
r,sin{0,1,2},
]
shows
[
L_0(u)in{q,q+1}.
]

Therefore
[
max_uL_0(u)-min_uL_0(u)le1.
]

By reversal,
[
L_3(u)=L_0(M-u),
]
so the same bound holds for (j=3).

Since
[
sum_{u=0}^{M}h(u)=0,
]
subtract any constant value (c) between the two possible endpoint-kernel values:
[
sum_uh(u)L_j(u)
=
sum_uh(u)(L_j(u)-c).
]

Thus
[
left|
sum_uh(u)L_j(u)
ight|
le
sum_u|h(u)|
le N.
]

Using the normalized averages,
[
left|
mathbb E hK_j
ight|
=
rac1{P^2}
left|
sum_uh(u)L_j(u)
ight|
le
rac N{P^2}
<
rac1{64N}.
]

The condition
[
Neta^4>15360
]
is exactly
[
rac1{64N}
<
rac{eta^4}{15cdot16^4}
=
delta_eta.
]

This proves endpoint exclusion.

### 2. Exact middle kernel

For (j=1), the conditions are
[
0le u-dle M,
qquad
0le u+dle M,
qquad
0le u+2dle M.
]

Therefore
[
L_1(u)
=
U(u)-V(u)+1,
]
where
[
U(u)
=
min!left(
u,leftlfloorrac{M-u}{2}ightfloor
ight)
]
and
[
V(u)
=
max!left(
u-M,-leftlfloorrac u2ightfloor
ight).
]

Each of (U) and (V) changes by at most (1) when (u) increases by (1). Hence
[
|L_1(u+1)-L_1(u)|le2.
]

By reversal,
[
L_2(u)=L_1(M-u),
]
so the same estimate holds for (j=2).

Consequently the discrete total variation obeys
[
operatorname{TV}(L_j)
:=
sum_{u=0}^{M-1}
|L_j(u+1)-L_j(u)|
<
2N
]
for (j=1,2).

### 3. Summation by parts

Define the prefix discrepancy
[
D(m):=sum_{u=0}^{m}h(u),
qquad
0le mle M.
]

Since
[
D(M)=0,
]
discrete summation by parts gives
[
sum_{u=0}^{M}h(u)L_j(u)
=
-sum_{m=0}^{M-1}
D(m)igl(L_j(m+1)-L_j(m)igr).
]

Therefore
[
left|
sum_uh(u)L_j(u)
ight|
le
max_{0le m<M}|D(m)|,
operatorname{TV}(L_j)
<
2Nmax_{m<M}|D(m)|.
]

A Q10 singleton witness satisfies
[
left|mathbb E hK_jight|
=
rac1{P^2}
left|sum_uh(u)L_j(u)ight|
>
delta_eta.
]

Hence
[
max_{m<M}|D(m)|
>
rac{delta_eta P^2}{2N}.
]

Since
[
P>8N,
]
we get
[
max_{m<M}|D(m)|
>
32delta_eta N
=
rac{eta^4}{30720}N.
]

Choose (m<M) attaining this strict bound.

If
[
D(m)>0,
]
take
[
J=[0,m].
]

If
[
D(m)<0,
]
then because the total discrepancy is zero,
[
sum_{u=m+1}^{M}h(u)=-D(m)>0,
]
so take
[
J=[m+1,M].
]

In either case (J) is nonempty and proper, and
[
|Bcap J|-alpha|J|
>
rac{eta^4}{30720}N.
]

Since
[
|J|le N,
]
division by (|J|) yields
[
rac{|Bcap J|}{|J|}
>
alpha+rac{eta^4}{30720}.
]

Finally (Bcap J) is 4-AP-free, so
[
r_4(|J|)
ge
|Bcap J|,
]
which proves the extremal-density increment.

## Asymptotic applicability

Protected E3-A03 gives
[
a_n
ge
2^{-(C_*+o(1))sqrt n}.
]

In the near-extremal regime relevant to the four-fibre deficit target one may take, for example,
[
etagerac12a_n.
]

Then
[
Neta^4
ge
2^ncdot2^{-4(C_*+o(1))sqrt n-4}
	oinfty.
]

Therefore the explicit condition
[
Neta^4>15360
]
holds eventually.

So endpoint singleton exclusion and the boundary-density-increment conclusion apply asymptotically on the campaign's near-extremal scale.

## What this accomplishes

Q10 split the de-windowed cancellation into:
1. singleton positional discrepancy; or
2. genuinely joint multi-fibre correlation.

Q11 reduces the singleton lane further:

> asymptotically, every singleton branch is a middle-position witness, and every such witness produces a strict density increment of size at least (eta^4/30720) on a smaller boundary interval.

Thus the singleton lane is no longer an abstract Fourier/correlation problem. It is a concrete extremal-density-increment problem.

## Claim boundary

Q11 does not show that such density increments are impossible.

In particular it does not prove:
- a fixed-fraction reduction in interval length;
- enough repeated increments before the scale collapses;
- a (eta^{1+	heta}) deletion exponent;
- the four-fibre deficit theorem;
- or the density-loss frontier.

The increment size is order (eta^4), still quantitatively weaker than the desired exponent below (2).

## First defect

The positional branch reduces to:

> **E3-B-BOUNDARY-DENSITY-INCREMENT-AMPLIFICATION.**  
> Show that repeated Q11 boundary density increments, together with internal 4-AP-freeness and near-extremality, either terminate in a contradiction before the physical scale collapses or accumulate enough loss to imply
> [
> gtrsimeta^{1+	heta}N
> ]
> deletions for some (	heta<1).

The genuinely joint Q10 branch remains separately open as
[
	exttt{E3-B-DEWINDOWED-MULTIFIBRE-WITNESS-ALIGNMENT}.
]

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-DEWINDOWED-POSITIONAL-DISCREPANCY`: **REDUCED**.
- New lemma `E3-B-SINGLETON-BOUNDARY-DENSITY-INCREMENT`: **PROVED_NATIVE**.
- New positional residual `E3-B-BOUNDARY-DENSITY-INCREMENT-AMPLIFICATION`: **OPEN_NATIVE_RESIDUAL**.
- `E3-B-DEWINDOWED-MULTIFIBRE-WITNESS-ALIGNMENT`: unchanged and open.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q10 all-distinct de-windowed correlation dichotomy and universal singleton-kernel identity.
- E3-A03 pointwise lower construction, used only to verify eventual applicability of the explicit condition (Neta^4>15360).

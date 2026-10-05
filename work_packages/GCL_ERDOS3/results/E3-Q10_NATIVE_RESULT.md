# E3-Q10 — all-distinct de-windowed correlation dichotomy

Disposition: **PROVED_NATIVE_DEWINDOWED_CORRELATION_DICHOTOMY**.

This is native GCL work. It composes the protected L01 family identities with Q09's local-window centering. It does not use an inverse theorem and does not claim a deletion estimate.

## Strongest exact statement

Let
[
N=2^n,qquad nge4,
]
and let
[
B_0,B_1,B_2,B_3subseteq[0,N-1]
]
be four physical fibres whose translated union in ([0,4N)) is globally 4-AP-free.

Assume
[
|B_j|ge eta N
qquad(j=0,1,2,3).
]

For a labelled occurrence in a D01 carry family define, as in Q09,
[
C_t=c_tN+B_{j_t},
qquad
I_t=c_tN+[0,N-1],
qquad
alpha_t=rac{|B_{j_t}|}{N},
]
and the de-windowed fluctuation
[
h_t:=1_{C_t}-alpha_t1_{I_t}.
]

Consider the two L01 core families

[
F_{15}=(i,q,c)=(0,0,0123),
]
and
[
F_{16}=(i,q,c)=(0,1,0000).
]

For both families the physical block word is exactly
[
(j_0,j_1,j_2,j_3)=(0,1,2,3),
]
so the four labelled positions use four distinct physical fibres.

Define
[
delta_eta:=rac{eta^4}{15cdot16^4}.
]

Then for each
[
Fin{F_{15},F_{16}}
]
at least one of the following two alternatives holds.

### Alternative A — positional discrepancy witness

There is one labelled position
[
jin{0,1,2,3}
]
such that
[
oxed{
left|
mathbb E_{yin G}
h_j(y),K_{F,j}(y)
ight|
>
delta_eta,
}
]
where
[
G=mathbb Z/Pmathbb Z
]
is the Q02 cyclic ambient group and
[
K_{F,j}(y)
:=
mathbb E_{din G}
prod_{t
e j}
1_{I_t}igl(y+(t-j)digr).
]

The kernel (K_{F,j}) is deterministic: it depends only on the four support intervals of the carry family and not on any fibre set (B_i).

Thus a singleton fluctuation term can only cancel the window baseline if one physical fibre has a large positional discrepancy against this explicit carry-marginal kernel.

### Alternative B — genuinely joint de-windowed correlation

There is a subset
[
Ssubseteq{0,1,2,3},
qquad
|S|ge2,
]
such that
[
oxed{
|T_{F,S}|>delta_eta,
}
]
where
[
T_{F,S}
:=
Lambda!left(
f_0,f_1,f_2,f_3
ight)
]
with
[
f_t=
egin{cases}
h_t,&tin S,\
alpha_t1_{I_t},&t
otin S.
end{cases}
]

Because the physical block word of (F_{15}) and (F_{16}) is ((0,1,2,3)), the factors (h_t) for (tin S) belong to at least two distinct physical fibres.

Moreover, for every
[
jin S,
]
the generalized von Neumann inequality used in Q02/Q09 gives
[
oxed{
|h_j|_{U^3(G)}
>
delta_eta.
}
]

Hence Alternative B is already a genuinely multi-fibre arithmetic-structure witness after deterministic interval support has been removed.

## Combined two-family consequence

Applying the theorem to both (F_{15}) and (F_{16}), one obtains the exact dichotomy:

> Either at least one of the two all-distinct L01 families supplies a genuinely joint de-windowed correlation involving at least two distinct physical fibres at scale (delta_eta), or both families supply a singleton positional-discrepancy witness against their respective deterministic carry-marginal kernels.

The two singleton witnesses arise from different labelled carry representations, although the next section proves that their physical-coordinate kernels are exactly equivalent:

- (F_{15}) uses carry (0123), so
  [
  (I_0,I_1,I_2,I_3)
  =
  ([0,N-1],,N+[0,N-1],,2N+[0,N-1],,3N+[0,N-1]);
  ]
- (F_{16}) uses carry (0000), so all four support windows are
  [
  I_t=[0,N-1].
  ]

Thus the remaining de-windowed problem splits into a finite deterministic positional-discrepancy lane and a genuinely joint multi-fibre correlation lane.

## Exact singleton-kernel equivalence for F15 and F16

The two carry families have different labelled windows, but after pulling them back to the common physical coordinate (uin[0,N-1]), their singleton kernels are exactly the same.

For (F_{16}), all four windows are ([0,N-1]). If the singleton factor is at physical position (j), then
[
K^{16}_j(u)
=
mathbb E_{din G}
prod_{t
e j}
1_{[0,N-1]}igl(u+(t-j)digr).
]

For (F_{15}), the (j)-th labelled window is (jN+[0,N-1]). Write
[
y=jN+u.
]
Then
[
K^{15}_j(jN+u)
=
mathbb E_{din G}
prod_{t
e j}
1_{tN+[0,N-1]}igl(jN+u+(t-j)digr).
]

Make the bijective change of variable
[
d=N+s
]
in (G). The (t)-th condition becomes
[
jN+u+(t-j)(N+s)
=
tN+igl(u+(t-j)sigr)
in
tN+[0,N-1],
]
which is equivalent to
[
u+(t-j)sin[0,N-1].
]

Therefore, exactly,
[
oxed{
K^{15}_j(jN+u)=K^{16}_j(u)
}
]
for every (j) and (u).

So the two all-distinct families do **not** amplify the singleton lane by furnishing two independent positional kernels. Any amplification must come from repeated locations/scales, internal AP-free constraints, or the genuinely joint Alternative B.

## Proof

Fix
[
Fin{F_{15},F_{16}}.
]

Q09 proves that the pure-window baseline satisfies
[
B_F
:=
Lambda(
alpha_01_{I_0},
alpha_11_{I_1},
alpha_21_{I_2},
alpha_31_{I_3}
)
>
rac{eta^4}{16^4}.
]

Since the global gluing is 4-AP-free, the Q02 embedding gives
[
Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})=0.
]

Using
[
1_{C_t}=alpha_t1_{I_t}+h_t
]
and expanding,
[
0
=
B_F
+
sum_{arnothing
e Ssubseteq{0,1,2,3}}
T_{F,S}.
]

There are exactly (15) nonbaseline terms. Therefore
[
sum_{arnothing
e S}|T_{F,S}|
>
rac{eta^4}{16^4},
]
so at least one nonempty (S) satisfies
[
|T_{F,S}|
>
rac{eta^4}{15cdot16^4}
=
delta_eta.
]

If (|S|ge2), Alternative B holds.

Now suppose
[
S={j}.
]
Then
[
T_{F,{j}}
=
left(prod_{t
e j}alpha_tight)
mathbb E_{y,d}
h_j(y)
prod_{t
e j}
1_{I_t}igl(y+(t-j)digr).
]

Therefore
[
T_{F,{j}}
=
left(prod_{t
e j}alpha_tight)
mathbb E_y h_j(y)K_{F,j}(y).
]

Because
[
0<alpha_tle1,
]
we have
[
prod_{t
e j}alpha_tle1.
]

Thus
[
left|
mathbb E_y h_j(y)K_{F,j}(y)
ight|
ge
|T_{F,{j}}|
>
delta_eta.
]

This proves Alternative A.

Finally, in Alternative B every (h_j), (jin S), is bounded by (1) in magnitude and every remaining window factor is also bounded by (1). The same generalized von Neumann inequality used in Q02 and Q09 therefore gives, for each (jin S),
[
|T_{F,S}|
le
|h_j|_{U^3(G)}.
]

Hence
[
|h_j|_{U^3(G)}
>
delta_eta
]
for every (jin S).

Because the physical block word is all-distinct, this is structure in at least two distinct physical fibres.

## Why this advances Q09

Q09 forced genuine de-windowed (U^3) structure in at least two fibres globally, but did not preserve a joint correlation carrying the same family identity.

Q10 retains the actual cancellation term for the two all-distinct core families.

It shows that the obstruction cannot hide in an unspecified one-fibre (U^3) witness unless that fibre has a large correlation with an explicit deterministic carry-marginal kernel.

Thus a successful continuation may attack exactly two smaller objects:

1. **positional discrepancy amplification:** show that a near-extremal internally 4-AP-free fibre cannot support the required large (K_{F,j})-correlation across the relevant carry families without paying the desired deficit; or
2. **joint de-windowed witness alignment:** exploit the genuinely multi-fibre large correlation from Alternative B to obtain aligned derivative-frequency/quadratic witnesses and a deletion cost.

Because the F15/F16 singleton kernels coincide after physical pullback, comparing those two families alone cannot create a singleton-kernel incompatibility.

## Claim boundary

Q10 does not prove:

- that Alternative A is impossible;
- that the two singleton witnesses, if both occur, fall on the same physical fibre;
- a quadratic inverse theorem;
- a carry-transversal lower bound;
- a deletion estimate;
- the four-fibre deficit theorem;
- or the density-loss frontier.

The kernels (K_{F,j}) are defined exactly by the carry-window geometry. No asymptotic smoothness or piecewise-polynomial property of those kernels is used here.

## First defect

The current quadratic residual can be split exactly into:

> **E3-B-DEWINDOWED-POSITIONAL-DISCREPANCY.**  
> Control the singleton carry-marginal correlations
> [
> mathbb E h_jK_{F,j}
> ]
> for (F_{15},F_{16}) using internal 4-AP-freeness, near-extremality, or recursive interval structure.

and

> **E3-B-DEWINDOWED-MULTIFIBRE-WITNESS-ALIGNMENT.**  
> Starting from a large (T_{F,S}) with (|S|ge2) in an all-distinct family, extract aligned derivative-frequency or quadratic witnesses strong enough to imply a (eta^{1+	heta}N) deletion cost.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-DEWINDOWED-U3-FORCING`: remains **PROVED_NATIVE**.
- New lemma `E3-B-DEWINDOWED-CORRELATION-DICHOTOMY`: **PROVED_NATIVE**.
- `E3-B-DEWINDOWED-JOINT-WITNESS`: **REDUCED** into the two exact residuals above.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-L01 exact family identities, including
  [
  F_{15}=(0,0,0123),qquad F_{16}=(0,1,0000).
  ]
- E3-Q02 labelled cyclic embedding and generalized von Neumann inequality.
- E3-Q09 local-window centering and window-baseline lower bound.

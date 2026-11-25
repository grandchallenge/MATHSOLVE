# E3-Q09 — de-windowed U3 forcing on the L01 core

Disposition: **PROVED_NATIVE_DEWINDOWED_U3_FORCING**.

This is native GCL work. It refines Q02/Q03 by subtracting the deterministic short-interval support window before measuring structure.

## Motivation

In Q02/Q03 a labelled fibre occurrence is embedded as
[
C_t=c_tN+B_{j_t}subseteq mathbb Z/Pmathbb Z,
qquad 8N<P<16N,
]
and globally centered by
[
g_t=1_{C_t}-|C_t|/P.
]

Because every (C_t) lies inside an interval of length (Nll P), (g_t) may have substantial low-frequency structure caused solely by the support window. Thus large (U^3(g_t)) need not by itself isolate arithmetic structure of the fibre.

Q09 removes that artifact.

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
|B_j|geeta N
qquad(j=0,1,2,3).
]

For a labelled occurrence in a D01 carry family, write
[
C_t=c_tN+B_{j_t},
qquad
I_t=c_tN+[0,N-1],
]
and define the physical density
[
alpha_t:=rac{|B_{j_t}|}{N}geeta.
]

Define the **de-windowed fluctuation**
[
h_t:=1_{C_t}-alpha_t1_{I_t}.
]

Then for every family in the exact ten-family L01 core
[
K={F_1,F_2,F_3,F_4,F_6,F_7,F_9,F_{10},F_{15},F_{16}},
]
at least one labelled factor in that family satisfies
[
oxed{
|h_t|_{U^3(mathbb Z/Pmathbb Z)}
>
rac{eta^4}{15cdot16^4}.
}
]

Because (h_t) is a translate of the corresponding physical fluctuation
[
h_j^{mathrm{phys}}
=
1_{B_j}-alpha_j1_{[0,N-1]},
]
the same lower bound is translation-invariant at the physical-fibre level.

Consequently at least **two distinct physical fibres** among
[
B_0,B_1,B_2,B_3
]
satisfy
[
oxed{
left|
1_{B_j}-rac{|B_j|}{N}1_{[0,N-1]}
ight|_{U^3(mathbb Z/Pmathbb Z)}
>
rac{eta^4}{15cdot16^4}.
}
]

Thus at least two fibres carry genuine local fluctuation structure after the interval-window contribution has been removed.

This does not yet prove a deletion bound or a joint quadratic witness.

## Proof

### 1. Exact carry-cell lower bound for every L01 core family

For one D01 carry vector
[
c=(c_0,c_1,c_2,c_3),
]
let
[
W_c
:=
#left{
(u,v)in[0,N-1]^2:
leftlfloorrac{u+tv}{N}ightfloor=c_t
	ext{ for }t=0,1,2,3
ight}.
]

The ten L01 families use only the carry vectors
[
0000, 0001, 0011, 0111, 0112, 0123.
]

Since (16mid N), each of the following rectangles consists entirely of valid lattice points for the displayed carry:

[
egin{array}{c|c|c|c}
	ext{carry}
&
u	ext{-range}
&
v	ext{-range}
&
	ext{rectangle size}
\ hline
0000
&
[0,N/4)
&
[0,N/4)
&
N^2/16
\
0001
&
[0,N/16)
&
[3N/8,7N/16)
&
N^2/256
\
0011
&
[0,N/8)
&
[N/2,9N/16)
&
N^2/128
\
0111
&
[3N/4,13N/16)
&
[N/4,5N/16)
&
N^2/256
\
0112
&
[N/2,5N/8)
&
[N/2,9N/16)
&
N^2/128
\
0123
&
[3N/4,N)
&
[3N/4,N)
&
N^2/16.
end{array}
]

The carry inequalities are checked directly:

- (0000): (u+3v<N);
- (0001): (u+2v<Nle u+3v<2N);
- (0011): (u+v<Nle u+2v) and (u+3v<2N);
- (0111): (Nle u+v) and (u+3v<2N);
- (0112): (Nle u+v, u+2v<2Nle u+3v<3N);
- (0123): (Nle u+v<2N, 2Nle u+2v<3N, 3Nle u+3v<4N).

Therefore every core family satisfies
[
oxed{
W_cgerac{N^2}{256}.
}
]

### 2. Window baseline is uniformly positive

For the labelled support intervals
[
I_t=c_tN+[0,N-1],
]
every admissible carry-cell pair ((u,v)) produces a modular progression
[
u, u+v, u+2v, u+3v
]
through
[
I_0,I_1,I_2,I_3.
]

Hence
[
Lambda(1_{I_0},1_{I_1},1_{I_2},1_{I_3})
ge
rac{W_c}{P^2}.
]

Using
[
W_cgerac{N^2}{256},
qquad
P<16N,
]
gives
[
Lambda(1_{I_0},1_{I_1},1_{I_2},1_{I_3})
>
rac1{16^4}.
]

Therefore the pure-window baseline term obeys
[
Lambda(
alpha_01_{I_0},
alpha_11_{I_1},
alpha_21_{I_2},
alpha_31_{I_3}
)
>
rac{eta^4}{16^4}.
]

### 3. Expand around the local window, not the global constant

By definition
[
1_{C_t}
=
alpha_t1_{I_t}+h_t.
]

Global 4-AP-freeness and the protected Q02 embedding give
[
Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})=0.
]

Expanding around the four window baselines gives
[
0
=
Lambda(
alpha_01_{I_0},
alpha_11_{I_1},
alpha_21_{I_2},
alpha_31_{I_3}
)
+
sum_{arnothing
e Ssubseteq{0,1,2,3}}
T_S,
]
where each (T_S) contains (h_t) in the positions (tin S) and (alpha_t1_{I_t}) in the remaining positions.

There are exactly (15) nonbaseline terms.

Every function in every term is bounded by (1):
[
|h_t|le1,
qquad
0lealpha_t1_{I_t}le1.
]

The same generalized von Neumann inequality used in Q02 therefore gives, for every nonempty (S) and every (jin S),
[
|T_S|
le
|h_j|_{U^3}.
]

Let
[
M_F
:=
max_{0le tle3}
|h_t|_{U^3}
]
for the chosen family.

Then
[
rac{eta^4}{16^4}
<
left|
Lambda(
alpha_01_{I_0},
alpha_11_{I_1},
alpha_21_{I_2},
alpha_31_{I_3}
)
ight|
le
sum_{arnothing
e S}|T_S|
le
15M_F.
]

Hence
[
oxed{
M_F>
rac{eta^4}{15cdot16^4}.
}
]

So every core family forces at least one genuinely de-windowed structured labelled factor.

### 4. At least two physical fibres are genuinely structured

The physical block supports of three core families are:

[
F_1:{0,1},
qquad
F_3:{1,2},
qquad
F_6:{2,3}.
]

Let
[
S
=
left{
j:
left|
1_{B_j}-alpha_j1_{[0,N-1]}
ight|_{U^3}
>
rac{eta^4}{15cdot16^4}
ight}.
]

Because translations preserve (U^3), Q09's per-family conclusion says (S) must intersect the physical support of every core family, in particular the three sets above.

But
[
{0,1}cap{1,2}cap{2,3}
=
arnothing.
]

Thus no single physical fibre can hit all three.

Therefore
[
|S|ge2.
]

The minimum two-fibre hitting sets for these three adjacent supports are
[
{0,2},
qquad
{1,2},
qquad
{1,3}.
]

So at least two fibres are genuinely structured beyond the support window.

## Relation to Q03

Q03 proves that all four globally centered functions
[
1_{C_t}-|C_t|/P
]
have large (U^3) along the adjacent (0011) chain.

Q09 shows that part of that statement can be deterministic support-window structure. After subtracting the correct local mean
[
alpha_t1_{I_t},
]
we can presently force genuine (U^3) structure in at least two physical fibres, not all four.

Therefore:

- Q03 remains an exact theorem about the globally centered cyclic functions;
- Q09 identifies and removes a possible support-window artifact;
- future quadratic-witness arguments must not silently identify Q03's global (U^3) mass with intrinsic arithmetic structure of all four fibres.

## Relation to Q04/Q06

Q04 and Q06 are exact correlation identities and remain valid.

However their globally centered Fourier/derivative witnesses may contain deterministic interval-window components.

A theorem using Q04/Q06 to obtain the required deletion exponent must therefore do at least one of:

1. repeat the witness extraction after local de-windowing;
2. explicitly subtract and control all window contributions;
3. prove that the relevant witness lies outside the window-generated spectrum;
4. or combine the global witnesses with near-extremality in a way that cannot be explained by support geometry alone.

## First defect

The quadratic lane reduces to:

> **E3-B-DEWINDOWED-JOINT-WITNESS.**  
> Starting from the Q09 locally centered fluctuations, prove that the genuinely structured physical fibres admit aligned derivative-frequency or quadratic witnesses across enough L01 carry families to force
> [
> gtrsimeta^{1+	heta}N
> ]
> deletions for some (	heta<1).

The current theorem forces only a two-fibre hitting set of genuine de-windowed structure. It does not yet align witnesses or force all four fibres to be intrinsically structured.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- Q03 remains **PROVED_NATIVE** as a globally centered statement.
- New lemma `E3-B-DEWINDOWED-U3-FORCING`: **PROVED_NATIVE**.
- `E3-B-DERIVATIVE-SPECTRAL-ALIGNMENT`: **REDUCED/QUALIFIED** by the support-window issue.
- New smallest quadratic residual: `E3-B-DEWINDOWED-JOINT-WITNESS`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-D01 exact carry compiler.
- E3-L01 exact ten-family core.
- E3-Q02 labelled cyclic embedding and generalized von Neumann inequality.
- E3-Q03 globally centered all-fibre forcing.
- E3-Q04 aligned Fourier-or-fourfold witness dichotomy.
- E3-Q06 derivative-overlap amplification.

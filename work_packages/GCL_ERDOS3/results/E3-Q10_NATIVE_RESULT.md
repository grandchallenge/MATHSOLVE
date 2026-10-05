# E3-Q10 — de-windowed low-order versus all-fibre structure dichotomy

Disposition: **PROVED_NATIVE_DEWINDOWED_ORDER_DICHOTOMY**.

This is native GCL work. It composes the protected Q09 local-window expansion with the exact adjacent `0011` chain already used in Q03/Q04. No inverse theorem and no external source is used.

## Strongest exact statement

Let
[
N=2^n,qquad nge4,
]
and let
[
B_0,B_1,B_2,B_3subseteq[0,N-1]
]
be physical fibres of a globally 4-AP-free four-fibre gluing. Assume
[
|B_j|geeta N
qquad(j=0,1,2,3).
]

Use the three adjacent `0011` L01 families
[
F_1:(B_0,B_0,B_1,B_1),qquad
F_4:(B_1,B_1,B_2,B_2),qquad
F_7:(B_2,B_2,B_3,B_3).
]

For one such family, let
[
C_t=c_tN+B_{j_t},qquad
I_t=c_tN+[0,N-1],
]
with carry vector (0011), and put
[
alpha_t:=rac{|B_{j_t}|}{N},
qquad
w_t:=alpha_t1_{I_t},
qquad
h_t:=1_{C_t}-w_t.
]

Define
[
delta_eta
:=
rac{eta^4}{15cdot16^4}.
]

Then for each adjacent family, at least one of the following holds.

### A. Singleton carry-kernel witness

For some labelled position (t),
[
left|
mathbb E_{yin G}
h_t(y),kappa_{F,t}(y)
ight|
>
delta_eta,
]
where
[
kappa_{F,t}(y)
:=
mathbb E_{din G}
prod_{s
e t}
1_{I_s}igl(y+(s-t)digr).
]

Thus one de-windowed physical fibre has a nontrivial correlation with an explicit deterministic carry-extension kernel.

### B. Pair carry-kernel witness

For some two labelled positions (a<b),
[
left|
mathbb E_{y,zin G}
h_a(y)h_b(z),
kappa_{F,a,b}(y,z)
ight|
>
delta_eta,
]
where, writing
[
d(y,z):=rac{z-y}{b-a},
qquad
x(y,z):=y-a,d(y,z),
]
the deterministic kernel is
[
kappa_{F,a,b}(y,z)
:=
prod_{s
otin{a,b}}
1_{I_s}igl(x(y,z)+s,d(y,z)igr).
]

Since (P>3) is prime and (1le b-ale3), the map
[
(x,d)longleftrightarrow
(x+ad,x+bd)
]
is a bijection on (G^2), so this is an exact reformulation of the corresponding pair term.

### C. High-order de-windowed witness

There is a subset
[
Ssubseteq{0,1,2,3},
qquad |S|ge3,
]
such that the local-window expansion term
[
T_S
=
Lambdaigl(
f_0,f_1,f_2,f_3
igr),
]
with (f_t=h_t) for (tin S) and (f_t=w_t) otherwise, obeys
[
|T_S|>delta_eta.
]

In this case **both physical fibres used by the adjacent family** satisfy
[
oxed{
left|
1_{B_j}
-rac{|B_j|}{N}1_{[0,N-1]}
ight|_{U^3(G)}
>
delta_eta.
}
]

Consequently, across the three adjacent families (F_1,F_4,F_7), one has the global dichotomy:

> **Either** at least one adjacent family supplies an explicit singleton or pair carry-kernel witness at scale (>delta_eta),  
> **or** all four physical fibres satisfy
> [
> oxed{
> left|
> 1_{B_j}
> -rac{|B_j|}{N}1_{[0,N-1]}
> ight|_{U^3(G)}
> >
> delta_eta
> qquad(j=0,1,2,3).
> }
> ]

Thus Q09's unconditional “at least two physical fibres are intrinsically structured” statement sharpens to:

- either an explicit low-order carry-kernel correlation already exists; or
- all four fibres are intrinsically de-windowed (U^3)-structured.

This does not yet align the high-order witnesses or prove a deletion bound.

## Proof

### 1. Q09 supplies a positive local-window baseline

For every L01 core family, Q09 proves
[
Lambda(w_0,w_1,w_2,w_3)
>
rac{eta^4}{16^4}.
]

Global 4-AP-freeness gives
[
Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})=0.
]

Since
[
1_{C_t}=w_t+h_t,
]
expansion gives
[
0
=
Lambda(w_0,w_1,w_2,w_3)
+
sum_{arnothing
e Ssubseteq{0,1,2,3}}
T_S.
]

There are exactly (15) nonbaseline terms. Hence
[
sum_{arnothing
e S}|T_S|
>
rac{eta^4}{16^4},
]
so for at least one nonempty (S),
[
|T_S|
>
rac{eta^4}{15cdot16^4}
=
delta_eta.
]

This is the only pigeonhole step.

### 2. Singleton terms are exact deterministic carry-kernel correlations

Take (S={t}). Then
[
T_{{t}}
=
left(prod_{s
e t}alpha_sight)
mathbb E_{x,d}
h_t(x+td)
prod_{s
e t}
1_{I_s}(x+sd).
]

Set
[
y=x+td.
]
For each fixed (d), the map (xmapsto y) is a bijection of (G). Therefore
[
T_{{t}}
=
left(prod_{s
e t}alpha_sight)
mathbb E_y
h_t(y)
mathbb E_d
prod_{s
e t}
1_{I_s}igl(y+(s-t)digr).
]

Thus
[
T_{{t}}
=
left(prod_{s
e t}alpha_sight)
mathbb E_y h_t(y)kappa_{F,t}(y).
]

Because every (alpha_sle1),
[
|T_{{t}}|>delta_eta
quadLongrightarrowquad
left|
mathbb E_yh_t(y)kappa_{F,t}(y)
ight|
>
delta_eta.
]

This proves alternative A.

### 3. Pair terms are exact deterministic bilinear carry-kernel correlations

Take (S={a,b}) with (a<b). Then
[
T_{{a,b}}
=
left(prod_{s
otin{a,b}}alpha_sight)
mathbb E_{x,d}
h_a(x+ad)h_b(x+bd)
prod_{s
otin{a,b}}
1_{I_s}(x+sd).
]

Since (P>3) is prime, (b-a) is invertible in (G). Put
[
y=x+ad,qquad z=x+bd.
]
Then
[
d=(z-y)/(b-a),qquad x=y-ad,
]
so ((x,d)mapsto(y,z)) is a bijection on (G^2).

Hence
[
T_{{a,b}}
=
left(prod_{s
otin{a,b}}alpha_sight)
mathbb E_{y,z}
h_a(y)h_b(z)kappa_{F,a,b}(y,z).
]

Again the density prefactor is at most (1), so
[
|T_{{a,b}}|>delta_eta
]
implies alternative B.

### 4. Any high-order term forces every fluctuation appearing in it

Suppose (|S|ge3) and
[
|T_S|>delta_eta.
]

Every (h_t) and every (w_t) is bounded in magnitude by (1). The generalized von Neumann inequality used in Q02/Q09 therefore gives, for **every** (jin S),
[
|T_S|
le
|h_j|_{U^3(G)}.
]

Thus
[
|h_j|_{U^3(G)}
>
delta_eta
qquad(jin S).
]

For an adjacent `0011` family the physical pattern is
[
(A,A,B,B).
]

Every subset of at least three labelled positions contains at least one (A)-position and at least one (B)-position. Therefore both underlying physical fluctuations satisfy
[
left|
1_A-rac{|A|}{N}1_{[0,N-1]}
ight|_{U^3}
>
delta_eta,
]
[
left|
1_B-rac{|B|}{N}1_{[0,N-1]}
ight|_{U^3}
>
delta_eta,
]
because translation preserves (U^3).

This proves alternative C.

### 5. Chain the three adjacent families

The three adjacent `0011` families use physical pairs
[
(B_0,B_1),qquad
(B_1,B_2),qquad
(B_2,B_3).
]

If any family lands in A or B, the first arm of the global dichotomy holds.

Otherwise every family lands in C. Then:

- (F_1) forces (B_0,B_1);
- (F_4) forces (B_1,B_2);
- (F_7) forces (B_2,B_3).

Hence all four physical fibres have de-windowed (U^3) norm (>delta_eta).

## Why this is new relative to Q09

Q09 retained only the scalar consequence
[
max_t|h_t|_{U^3}>delta_eta
]
for each core family and then used a hitting-set argument to force at least two physical fibres.

Q10 retains the **order of the expansion term** responsible for that norm:

- order (1): an explicit one-fibre carry-extension correlation;
- order (2): an explicit two-fibre carry-kernel correlation;
- order (3) or (4): both fibres in an adjacent pair are intrinsically structured.

The adjacent-chain composition then forces all four fibres in the high-order-only regime.

## Claim boundary

Q10 does not prove:

- that alternatives A or B imply a density increment or deletion cost;
- that all-four de-windowed (U^3) structure yields aligned quadratic witnesses;
- that the low-order kernels have enough independent translates to beat the target exponent;
- or that
  [
  H_{2,n}gtrsim Na_n^{1+	heta}
  ]
  for any (	heta<1).

The scale remains
[
delta_etaasympeta^4,
]
which is quantitatively too weak by itself.

## First defect

The de-windowed quadratic lane reduces to the following two-arm residual:

> **E3-B-DEWINDOWED-CARRY-KERNEL-OR-ALLFIBRE-ALIGNMENT.**
>
> Starting from Q10, prove either:
>
> 1. a singleton/pair carry-kernel witness at scale (eta^4) amplifies, using near-extremality or repeated carry locations/scales, to a deletion cost
>    [
>    gtrsim eta^{1+	heta}N
>    ]
>    for some (	heta<1); or
> 2. in the all-four de-windowed (U^3) arm, the four intrinsic structures admit sufficiently aligned derivative-frequency/quadratic witnesses to force the same deletion cost.

This is strictly narrower than the Q09 residual because the support-window artifact is removed and the low-order obstruction is now explicit.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-DEWINDOWED-U3-FORCING`: remains **PROVED_NATIVE**.
- New lemma `E3-B-DEWINDOWED-ORDER-DICHOTOMY`: **PROVED_NATIVE**.
- `E3-B-DEWINDOWED-JOINT-WITNESS`: **REDUCED**.
- New smallest quadratic residual: `E3-B-DEWINDOWED-CARRY-KERNEL-OR-ALLFIBRE-ALIGNMENT`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-D01 exact carry compiler.
- E3-L01 exact ten-family core.
- E3-Q02 cyclic embedding and generalized von Neumann inequality.
- E3-Q09 de-windowed local-window expansion and baseline.

# E3-Q10 — de-windowed low-order discrepancy versus all-fibre structure

Disposition: **PROVED_NATIVE_DEWINDOWED_CORRELATION_DICHOTOMY**.

This is native GCL work. It sharpens Q09 on the adjacent D01 `0011` chain by retaining the order of the de-windowed correlation that cancels the deterministic carry-window baseline.

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

Choose the Q02 prime
[
8N<P<16N,
qquad G=mathbb Z/Pmathbb Z.
]

For each of the three adjacent D01 families
[
F_1=(0,0,0011),qquad
F_4=(1,0,0011),qquad
F_7=(2,0,0011),
]
the labelled physical pattern is respectively
[
(B_0,B_0,B_1,B_1),qquad
(B_1,B_1,B_2,B_2),qquad
(B_2,B_2,B_3,B_3).
]

For one such family write
[
C_t=c_tN+B_{j_t},
qquad
I_t=c_tN+[0,N-1],
qquad
alpha_t=rac{|B_{j_t}|}{N},
]
and define the locally centered fluctuation
[
h_t:=1_{C_t}-alpha_t1_{I_t}.
]

Put
[
oxed{
	au_eta
:=
rac{2eta^4}{15cdot16^4}.
}
]

Then every adjacent `0011` family satisfies at least one of the following two alternatives.

### A. Low-order carry-window discrepancy

There exists a nonempty
[
Ssubseteq{0,1,2,3},
qquad |S|le2,
]
such that
[
oxed{
left|
Lambda!left(
f_0^{(S)},f_1^{(S)},f_2^{(S)},f_3^{(S)}
ight)
ight|
>
	au_eta,
}
]
where
[
f_t^{(S)}
=
egin{cases}
h_t,&tin S,\
alpha_t1_{I_t},&t
otin S.
end{cases}
]

Thus a singleton or pair of locally centered fibre fluctuations has polynomial-size correlation against an explicit deterministic carry-window marginal.

### B. High-order de-windowed joint correlation

There exists
[
Ssubseteq{0,1,2,3},
qquad |S|in{3,4},
]
with the same bound
[
oxed{
left|
Lambda!left(
f_0^{(S)},f_1^{(S)},f_2^{(S)},f_3^{(S)}
ight)
ight|
>
	au_eta.
}
]

In this case **both physical fibres used by the adjacent family** satisfy
[
oxed{
left|
1_{B_j}-rac{|B_j|}{N}1_{[0,N-1]}
ight|_{U^3(G)}
>
	au_eta.
}
]

Consequently, for the full adjacent chain (F_1,F_4,F_7), one has the exact global dichotomy:

> **Either**
> at least one of the three adjacent carry families has a low-order carry-window discrepancy of magnitude (>	au_eta);
>
> **or**
> every physical fibre (B_0,B_1,B_2,B_3) has de-windowed (U^3) norm (>	au_eta).

This does not yet align quadratic witnesses or imply a deletion bound.

## Proof

### 1. The `0011` carry cell has twice the uniform Q09 lower mass

For carry vector
[
0011
]
the exact D01 inequalities are
[
u+v<Nle u+2v,
qquad
u+3v<2N.
]

Because (16mid N), the rectangle
[
0le u<rac N8,
qquad
rac N2le v<rac{9N}{16}
]
contains exactly
[
rac N8cdotrac N{16}
=
rac{N^2}{128}
]
lattice pairs, and every one satisfies the `0011` inequalities.

Hence, with
[
W_{0011}
]
the full number of admissible ((u,v)) pairs,
[
W_{0011}gerac{N^2}{128}.
]

For the support windows
[
I_0=I_1=[0,N-1],
qquad
I_2=I_3=N+[0,N-1],
]
these pairs produce genuine modular four-term progressions through the four labelled windows. Therefore
[
Lambda(1_{I_0},1_{I_1},1_{I_2},1_{I_3})
ge
rac{W_{0011}}{P^2}.
]

Since (P<16N),
[
rac{W_{0011}}{P^2}
>
rac{1}{128cdot16^2}
=
rac{2}{16^4}.
]

As every (alpha_tgeeta), the deterministic baseline
[
B_F
:=
Lambda(
alpha_01_{I_0},
alpha_11_{I_1},
alpha_21_{I_2},
alpha_31_{I_3}
)
]
satisfies
[
oxed{
B_F>rac{2eta^4}{16^4}.
}
]

### 2. Exact local-mean expansion

For every labelled position,
[
1_{C_t}
=
alpha_t1_{I_t}+h_t.
]

Global 4-AP-freeness and the protected Q02 embedding give
[
Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})=0.
]

Expanding around the local window means,
[
0
=
B_F
+
sum_{arnothing
e Ssubseteq{0,1,2,3}}T_S,
]
where
[
T_S
:=
Lambda(
f_0^{(S)},f_1^{(S)},f_2^{(S)},f_3^{(S)}
).
]

There are exactly
[
2^4-1=15
]
nonbaseline terms.

Therefore
[
B_F
le
sum_{arnothing
e S}|T_S|.
]

If every nonbaseline term had
[
|T_S|le	au_eta
=
rac{2eta^4}{15cdot16^4},
]
then
[
B_F
le
15	au_eta
=
rac{2eta^4}{16^4},
]
contradicting the strict baseline lower bound.

Hence at least one nonempty (S) satisfies
[
|T_S|>	au_eta.
]

Splitting by (|S|le2) or (|S|ge3) proves the two alternatives.

### 3. High-order terms force both physical fibres

All functions appearing in (T_S) are bounded by (1):
[
|h_t|le1,
qquad
0lealpha_t1_{I_t}le1.
]

The same generalized von Neumann inequality used in Q02/Q09 gives, for every (jin S),
[
|T_S|
le
|h_j|_{U^3(G)}.
]

For an adjacent `0011` family the labelled physical word is
[
(A,A,B,B).
]

Every subset of three labelled positions contains at least one occurrence of (A) and at least one occurrence of (B). The four-position set obviously does also.

Thus if (|S|in{3,4}), the high-order bound
[
|T_S|>	au_eta
]
forces
[
|h_A|_{U^3}>	au_eta,
qquad
|h_B|_{U^3}>	au_eta.
]

Translation invariance identifies these with the physical de-windowed fluctuations
[
1_A-rac{|A|}{N}1_{[0,N-1]},
qquad
1_B-rac{|B|}{N}1_{[0,N-1]}.
]

### 4. Chain consequence

If none of (F_1,F_4,F_7) lies in the low-order alternative, then all three lie in the high-order alternative.

Therefore:
- (F_1) forces (B_0,B_1);
- (F_4) forces (B_1,B_2);
- (F_7) forces (B_2,B_3).

Hence all four physical fibres have de-windowed (U^3) norm (>	au_eta).

This proves the chain dichotomy.

## Why this improves Q09

Q09 proves unconditionally that at least two physical fibres carry genuine de-windowed (U^3) structure.

Q10 identifies the sole obstruction to upgrading that statement to all four fibres along the adjacent chain:

[
oxed{
	ext{a polynomial-size singleton/pair carry-window discrepancy.}
}
]

Thus the support-window issue is no longer an undifferentiated caveat.

Either:
1. low-order interaction with the exact carry geometry is already large and must be exploited directly; or
2. all four fibres possess genuine higher-order de-windowed structure.

## Interpretation of the low-order alternative

A singleton term has the form
[
Lambda(
h_t,
alpha_11_{I_1},
alpha_21_{I_2},
alpha_31_{I_3}
)
]
up to permutation.

It is a weighted discrepancy of one fibre against the explicit marginal of the `0011` carry cell.

A pair term similarly measures a bilinear discrepancy of two physical fibre fluctuations against the remaining two deterministic window factors.

These are not generic Fourier artifacts. They encode nonuniformity relative to the actual digit/carry geometry.

A useful next theorem may therefore attack them by:
- explicit marginal kernels;
- interval-density concentration;
- recursive subinterval decomposition;
- or near-extremal stability.

## Claim boundary

Q10 does **not** prove:
- that the low-order alternative is impossible;
- that all four fibres are always intrinsically (U^3)-structured;
- any common derivative-frequency or quadratic phase;
- a transversal/deletion bound;
- E3-B-FOUR-FIBRE-DEFICIT;
- E3-Q4-DENSITY-LOSS;
- E3-Q4-SERIES;
- or Erdős Problem 3.

## First defect

The de-windowed quadratic lane now splits into two smaller exact residuals.

> **E3-B-CARRY-WINDOW-DISCREPANCY.**  
> Convert a singleton/pair de-windowed `0011` carry-window correlation of size (gtrsimeta^4) into interval-density concentration, recursive loss, or a direct deletion cost.

and

> **E3-B-DEWINDOWED-HIGHORDER-ALIGNMENT.**  
> In the absence of the low-order discrepancy alternative, all four physical fibres have de-windowed (U^3) mass (gtrsimeta^4). Retain and align the actual triple/fourfold de-windowed witnesses across the L01 core strongly enough to force (gtrsimeta^{1+	heta}N) deletions for some (	heta<1).

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-DEWINDOWED-U3-FORCING`: **PROVED_NATIVE**.
- New lemma `E3-B-DEWINDOWED-CORRELATION-DICHOTOMY`: **PROVED_NATIVE**.
- `E3-B-DEWINDOWED-JOINT-WITNESS`: **REDUCED** to the two residuals above.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-D01 exact carry compiler.
- E3-L01 exact ten-family core.
- E3-Q02 labelled cyclic embedding and generalized von Neumann inequality.
- E3-Q09 de-windowed U3 forcing.

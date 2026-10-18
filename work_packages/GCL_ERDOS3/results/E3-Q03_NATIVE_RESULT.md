# E3-Q03 — all-fibre U3 forcing from the adjacent 0011 chain

Disposition: **PROVED_NATIVE_ALL_FIBRE_U3_FORCING**.

This is native GCL work. It strengthens the scalar conclusion of E3-Q02 by using the exact cancellation structure of the labelled 4-AP expansion. It uses only the protected Q02 result and the exact D01 family geometry.

## Strongest exact statement

Let
[
N=2^n,qquad nge2,
]
and let
[
B_0,B_1,B_2,B_3subseteq[0,N-1]
]
be four physical fibres whose translated union in ([0,4N)) is 4-AP-free.

Assume
[
|B_j|ge eta N
qquad (j=0,1,2,3).
]

Choose a prime
[
8N<P<16N
]
as in E3-Q02, and for each translated labelled occurrence (C) of a physical fibre write
[
g_C:=1_C-|C|/P.
]

Then for each of the three adjacent D01 (0011) families
[
F_1=(0,0,0011),qquad
F_4=(1,0,0011),qquad
F_7=(2,0,0011),
]
the two physical fibres used by that family both satisfy
[
oxed{
|g|_{U^3(mathbb Z/Pmathbb Z)}
ge
rac{eta^4}{5cdot16^4}.
}
]

Consequently **all four physical fibres** satisfy the same lower bound:
[
oxed{
min_{0le jle3}
|1_{B_j+s_j}-|B_j|/P|_{U^3(mathbb Z/Pmathbb Z)}
ge
rac{eta^4}{5cdot16^4},
}
]
for any translations (s_j) used to place the fibres in the Q02 cyclic model.

The value is translation-invariant, so the choice of (s_j) does not matter.

This improves the scalar forcing stage from “at least one structured labelled factor per carry family” to “every physical fibre is structured at polynomial scale.”

It does **not** identify compatible quadratic phases/factors, and it does not prove a deletion bound.

## Proof

### 1. Only triple and quadruple balanced terms survive

For one valid labelled 4-AP system write
[
Lambda(f_0,f_1,f_2,f_3)
=
mathbb E_{x,dinmathbb Z/Pmathbb Z}
f_0(x)f_1(x+d)f_2(x+2d)f_3(x+3d).
]

Let
[
1_{C_t}=ho_t+g_t,qquad mathbb E g_t=0.
]

Because the physical gluing is globally 4-AP-free, E3-Q02 gives
[
Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})=0.
]

Expanding:
[
0
=
ho_0ho_1ho_2ho_3
+
sum_{arnothing
e Ssubseteq{0,1,2,3}}
left(prod_{t
otin S}ho_tight)Lambda_S,
]
where (Lambda_S) has (g_t) in positions (tin S) and (1) elsewhere.

If (|S|=1), then
[
Lambda_S=mathbb E g_t=0.
]

If (S={a,b}) with (a
e b), the map
[
(x,d)mapsto(x+ad,x+bd)
]
is a bijection of (G^2), because (b-ain{pm1,pm2,pm3}) is invertible modulo the prime (P>3). Hence
[
Lambda_S
=
(mathbb E g_a)(mathbb E g_b)
=
0.
]

Therefore only the four triple terms and the one quadruple term survive:
[
ho_0ho_1ho_2ho_3
le
sum_{|S|=3}
ho_{{0,1,2,3}setminus S}|Lambda_S|
+
|Lambda_{{0,1,2,3}}|.
]

There are five terms, and each density coefficient is at most (1). Hence at least one surviving (S), with (|S|in{3,4}), satisfies
[
|Lambda_S|
ge
rac{ho_0ho_1ho_2ho_3}{5}.
]

### 2. Every labelled factor in the large term has large U3 norm

The generalized von Neumann inequality used in E3-Q02 applies with constants in the omitted positions:
[
|Lambda_S|
le
|g_j|_{U^3}
qquad	ext{for every }jin S.
]

Therefore for the large surviving term,
[
|g_j|_{U^3}
ge
rac{ho_0ho_1ho_2ho_3}{5}
qquadorall jin S.
]

Since (P<16N) and every physical fibre used by the family has size at least (eta N),
[
ho_t>eta/16.
]
Thus
[
|g_j|_{U^3}
>
rac{eta^4}{5cdot16^4}
qquadorall jin S.
]

### 3. The adjacent 0011 families force both physical fibres

For (F_1=(0,0,0011)), the four labelled physical block indices are
[
(0,0,1,1).
]

Every subset of three of these four labelled positions contains at least one occurrence of physical fibre (0) and at least one occurrence of physical fibre (1). The same is obviously true of the four-position set.

Therefore whichever surviving triple/quadruple term is large, it contains labelled occurrences of **both** physical fibres. Translation invariance of (U^3) then gives
[

u_0,
u_1
ge
rac{eta^4}{5cdot16^4}.
]

Likewise:
- (F_4) has labelled pattern ((1,1,2,2)), so it forces fibres (1) and (2);
- (F_7) has labelled pattern ((2,2,3,3)), so it forces fibres (2) and (3).

Combining the three families forces fibres (0,1,2,3) all above the same (U^3) threshold.

## Relation to E3-T01

E3-T01 correctly showed that the **weaker per-family statement**
[
max_{jin J(F)}
u_jgeeta
]
can be satisfied by only two structured physical fibres, with minimum covers
[
{0,2},quad{1,2},quad{1,3}.
]

Q03 proves that this weaker scalar abstraction discards usable information from the Q02 expansion.

The stronger surviving-correlation statement forces all four fibres to be structured.

The part of T01 that remains decisive is its second diagnosis:

> scalar (U^3) magnitudes do not record the identity of the quadratic correlation/factor witness.

Q03 therefore supersedes T01 only on the question “how many physical fibres are forced to be structured?” It does **not** repair the witness-alignment gap.

## Quantitative improvement over Q02

E3-Q02 used all (15) nonempty expansion terms and obtained
[
etagerac{ho_0ho_1ho_2ho_3}{15}.
]

Q03 observes that the ten terms of size one or two vanish exactly. Hence
[
etagerac{ho_0ho_1ho_2ho_3}{5}.
]

This improves the constant by a factor of three and, more importantly, preserves the fact that a large surviving term contains at least three labelled factors.

## First defect

The first missing theorem is now sharper.

We no longer need to prove that every near-extremal physical fibre has degree-2 structure: Q03 gives that directly at scale
[
ceta^4.
]

What is missing is a **joint witness theorem**:

> select quantitative derivative-frequency / quadratic witnesses for all four structured physical fibres and use the large mixed triple/quadruple correlations associated with the 10-family L01 core to show that those witnesses cannot satisfy all carry translations without a deletion cost
> [
> gtrsim eta^{1+	heta}N,qquad 	heta<1.
> ]

A generic scalar (U^3) inverse theorem applied independently to each fibre does not supply the required joint compatibility information.

## Frontier effect

- E3-Q4-DENSITY-LOSS remains **OPEN**.
- E3-B-FOUR-FIBRE-DEFICIT remains **OPEN_NATIVE_SUBTARGET**.
- E3-B-QUADRATIC-MOTIF-AMPLIFICATION remains open but is sharpened:
  the live residual is now **joint correlation-witness incompatibility**, not scalar structure forcing.
- E3-Q4-GLUING-RADIUS remains **FORMULATED_PENDING_VERIFY**.
- No theorem/frontier promotion is authorized.

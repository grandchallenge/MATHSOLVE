# E3-Q16 — bridge-family derivative-or-three-fibre dichotomy

Disposition: **PROVED_NATIVE_BRIDGE_FAMILY_DICHOTOMY**.

This is native GCL work. It extends the de-windowed order analysis to the two L01 core bridge families
\[
F_9=(0,0,0112),\qquad
F_{10}=(1,0,0112),
\]
which connect three consecutive physical fibres.

No inverse theorem and no external source is used.

## Strongest exact statement

Let
\[
N=2^n,\qquad n\ge4,
\]
and let
\[
B_0,B_1,B_2,B_3\subseteq[0,N-1]
\]
be the physical fibres of a globally 4-AP-free four-fibre gluing, with
\[
|B_j|\ge\beta N.
\]

Use the Q09 local-window decomposition
\[
1_{C_t}=w_t+h_t,
\qquad
w_t=\alpha_t1_{I_t},
\]
and put
\[
\delta_\beta:=\frac{\beta^4}{15\cdot16^4}.
\]

The physical block patterns of the two bridge families are
\[
F_9:(B_0,B_1,B_1,B_2),
\]
\[
F_{10}:(B_1,B_2,B_2,B_3).
\]

For either family, at least one nonbaseline expansion term
\[
T_S,\qquad \varnothing\ne S\subseteq\{0,1,2,3\},
\]
satisfies
\[
|T_S|>\delta_\beta.
\]

If a large term has \(|S|\le2\), one has the same explicit singleton/pair carry-kernel witness as in Q10.

Assume instead
\[
|S|\ge3.
\]

Let \(Y\) denote the interior physical fibre repeated in positions \(1,2\):
\[
Y=B_1\quad\text{for }F_9,
\qquad
Y=B_2\quad\text{for }F_{10}.
\]

Then exactly one of the following two high-order alternatives holds.

### B1. Interior derivative-product alternative

If
\[
\{1,2\}\subseteq S,
\]
then the repeated interior fibre contributes a complete de-windowed derivative:
\[
\Delta_d h_Y(y)=h_Y(y)h_Y(y+d).
\]

After affine relabelling,
\[
T_S
=
\mathbb E_d J_d,
\]
where
\[
J_d
=
\mathbb E_y
\Delta_d h_Y(y)\,
u_d(y+\lambda d),
\]
and \(u_d\) is the product of the two outer labelled factors, each chosen from its local fluctuation/window pair, with at least one outer factor de-windowed.

There is a signed good-shift set
\[
D
=
\{d:\sigma J_d\ge\delta_\beta/2\}
\]
with
\[
\boxed{|D|\ge(\delta_\beta/2)P}.
\]

For every \(d\in D\),
\[
\sum_{\xi}
\left|\widehat{\Delta_d h_Y}(\xi)\right|
\left|\widehat{u_d}(-\xi)\right|
\ge
\delta_\beta/2.
\]

Thus:

- high-order derivative \(F_9\) forces \(B_1\) as the complete derivative side;
- high-order derivative \(F_{10}\) forces \(B_2\) as the complete derivative side.

### B2. Three-physical-fibre bridge alternative

If
\[
\{1,2\}\not\subseteq S,
\]
then because \(|S|\ge3\), necessarily
\[
|S|=3
\]
and exactly one of positions \(1,2\) is omitted.

Hence both outer physical fibres appear as de-windowed fluctuations, exactly one repeated-interior occurrence appears as a de-windowed fluctuation, and the other repeated-interior occurrence remains as its deterministic local window.

For \(F_9\), the large term is therefore one of
\[
\Lambda(h_{B_0},w_{B_1},h_{B_1},h_{B_2}),
\]
\[
\Lambda(h_{B_0},h_{B_1},w_{B_1},h_{B_2}),
\]
up to the fixed carry translations, and has magnitude
\[
>\delta_\beta.
\]

For \(F_{10}\), the same statement holds with
\[
(B_0,B_1,B_2)\mapsto(B_1,B_2,B_3).
\]

Thus a non-derivative high-order bridge term is an explicit **three-physical-fibre mixed-window witness**:
- \(F_9\) directly couples \(B_0,B_1,B_2\);
- \(F_{10}\) directly couples \(B_1,B_2,B_3\).

Moreover, writing such a term as
\[
T_S=\mathbb E_d K_d
\]
with \(|K_d|\le1\), the same averaging argument gives a signed good-shift set
\[
D_{\rm br}
=
\{d:\sigma K_d\ge\delta_\beta/2\}
\]
with
\[
\boxed{|D_{\rm br}|\ge(\delta_\beta/2)P}.
\]

So the three-fibre bridge is present on a positive-density family of common shifts, not merely as one global scalar correlation.

## Proof

### 1. Q09 supplies a large nonbaseline term

For every L01 core family, Q09 gives
\[
0
=
\Lambda(w_0,w_1,w_2,w_3)
+
\sum_{\varnothing\ne S}T_S
\]
with
\[
\Lambda(w_0,w_1,w_2,w_3)
>
\frac{\beta^4}{16^4}.
\]

There are 15 nonbaseline terms. Therefore some \(S\ne\varnothing\) satisfies
\[
|T_S|>\delta_\beta.
\]

If \(|S|\le2\), the Q10 singleton/pair change-of-variables applies verbatim because it uses only the labelled progression positions and invertibility of \(1,2,3\) modulo \(P\).

Assume \(|S|\ge3\).

### 2. Classify the high-order subsets

The repeated interior fibre occupies exactly labelled positions \(1\) and \(2\).

If both belong to \(S\), alternative B1 holds.

Suppose not. Since there are four labelled positions and \(|S|\ge3\), one must have
\[
|S|=3.
\]

The unique omitted position is then either \(1\) or \(2\).

Therefore positions \(0\) and \(3\) both belong to \(S\), and exactly one of positions \(1,2\) belongs to \(S\).

This is precisely alternative B2.

No other high-order case exists.

### 3. Derivative-product representation in B1

If
\[
\{1,2\}\subseteq S,
\]
then the two repeated labelled factors are translates of the same physical de-windowed fluctuation \(h_Y\):
\[
h_Y(z+d)h_Y(z+2d).
\]

Put
\[
y=z+d.
\]

Then
\[
h_Y(y)h_Y(y+d)
=
\Delta_dh_Y(y).
\]

The two remaining labelled factors form
\[
u_d(y+\lambda d)
\]
for a fixed integer \(\lambda\), and because \(|S|\ge3\), at least one of those two outer factors is de-windowed.

Thus
\[
T_S
=
\mathbb E_d
\mathbb E_y
\Delta_dh_Y(y)u_d(y+\lambda d).
\]

The Q12 good-shift argument applies verbatim:
\[
|D|\ge(\delta_\beta/2)P.
\]

Fourier expansion at a good shift gives
\[
J_d
=
\sum_{\xi}
\widehat{\Delta_dh_Y}(\xi)
\widehat{u_d}(-\xi)
e_P(\mu\xi d)
\]
for a fixed integer \(\mu\), hence
\[
\sum_\xi
|\widehat{\Delta_dh_Y}(\xi)|
|\widehat{u_d}(-\xi)|
\ge\delta_\beta/2.
\]

### 4. Three-fibre bridge representation in B2

If position \(1\) is omitted, the four labelled factors have the form
\[
h_{\rm left},
\quad
w_Y,
\quad
h_Y,
\quad
h_{\rm right}.
\]

If position \(2\) is omitted, they have the form
\[
h_{\rm left},
\quad
h_Y,
\quad
w_Y,
\quad
h_{\rm right}.
\]

Thus all three physical fibres represented in the bridge family contribute genuine de-windowed fluctuations, while the second occurrence of the interior fibre contributes only its explicit deterministic support window.

The term remains larger than \(\delta_\beta\) by hypothesis.

Writing
\[
T_S=\mathbb E_d K_d,
\]
all factors are bounded by \(1\), so
\[
|K_d|\le1.
\]

Choose
\[
\sigma T_S=|T_S|>\delta_\beta.
\]

The same threshold argument used in Q12 yields
\[
\left|
\{d:\sigma K_d\ge\delta_\beta/2\}
\right|
\ge
(\delta_\beta/2)P.
\]

This proves B2.

### 5. Identify the physical fibres

D01/L01 give
\[
F_9=(0,0,0112)
\]
with block pattern
\[
(0,1,1,2),
\]
hence physical pattern
\[
(B_0,B_1,B_1,B_2).
\]

Likewise
\[
F_{10}=(1,0,0112)
\]
has block pattern
\[
(1,2,2,3),
\]
hence
\[
(B_1,B_2,B_2,B_3).
\]

The stated derivative and three-fibre identities follow.

## Composition with Q15

Q15 proves:
- high-order \(F_2\) and \(F_3\) force \(B_1\) as complete derivative side;
- high-order \(F_6\) forces \(B_2\) as complete derivative side.

Q16 adds the bridge families.

Therefore, in a regime where
\[
F_2,F_3,F_6,F_9,F_{10}
\]
are all high-order, one has a finite exact case split:

1. if \(F_9,F_{10}\) both take derivative alternatives, then
   - \(B_1\) is the complete derivative side in \(F_2,F_3,F_9\);
   - \(B_2\) is the complete derivative side in \(F_6,F_{10}\);

2. if either bridge family takes B2, there is instead an explicit positive-density three-physical-fibre correlation spanning
   \[
   B_0,B_1,B_2
   \]
   or
   \[
   B_1,B_2,B_3.
   \]

Thus the high-order core is no longer an undifferentiated collection of U3-large functions.

It reduces to:
- repeated interior derivative compatibility; or
- an explicit three-fibre bridge witness.

## Claim boundary

Q16 does not prove:

- that the derivative good-shift sets from different families intersect;
- that the bridge witness has one large Fourier frequency;
- that the bridge witness integrates to a common quadratic phase;
- that either branch yields an exponent below \(2\);
- or any gluing-deficit/deletion theorem.

The positive-density shift sets have density only \(O(\beta^4)\), so raw finite-set intersection remains insufficient.

## First defect

The high-order residual reduces to:

> **E3-B-INTERIOR-DERIVATIVE-OR-THREEFIBRE-BRIDGE-COMPATIBILITY.**
>
> In the all-high-order regime for \(F_2,F_3,F_6,F_9,F_{10}\), prove that either:
>
> 1. the repeated derivative constraints on \(B_1,B_2\) align across their distinct carry geometries to a common quadratic witness; or
> 2. a positive-density three-fibre mixed-window bridge from \(F_9\) or \(F_{10}\) forces an exponent-\(<2\) density/deletion gain.
>
> If any of the five families has a low-order term, route that evidence to the separate low-order exponent-upgrade residual.

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\`: **OPEN**.
- \`E3-B-FOUR-FIBRE-DEFICIT\`: **OPEN_NATIVE_SUBTARGET**.
- \`E3-B-REPEATED-TRIPLET-DERIVATIVE-FORCING\`: remains **PROVED_NATIVE**.
- New lemma \`E3-B-BRIDGE-FAMILY-DICHOTOMY\`: **PROVED_NATIVE**.
- \`E3-B-INTERIOR-DERIVATIVE-COMPATIBILITY\`: **REDUCED**.
- New high-order residual: \`E3-B-INTERIOR-DERIVATIVE-OR-THREEFIBRE-BRIDGE-COMPATIBILITY\`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-D01 exact carry compiler.
- E3-L01 ten-family core.
- E3-Q09 de-windowed local-window expansion.
- E3-Q10 order dichotomy.
- E3-Q12 derivative-product overlap.
- E3-Q15 repeated-triplet derivative forcing.

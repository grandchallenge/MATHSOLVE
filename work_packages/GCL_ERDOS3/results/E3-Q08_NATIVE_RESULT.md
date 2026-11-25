# E3-Q08 — Boolean cyclic realizability does not close the linear witness lane

Disposition: **PROVED_NATIVE_BOOLEAN_REALIZABILITY_INSUFFICIENT**.

This is native GCL work. It composes the protected Q04/Q05/Q07 finite-harmonic witness scale with the protected A03 pointwise lower construction. No external theorem beyond elementary Hoeffding concentration is required.

## Strongest exact statement

Let
[
G=mathbb Z/Pmathbb Z
]
with (P>6) prime, and let (r
e0) be such that
[
pm r, pm2r, pm3r
]
are six distinct nonzero frequencies.

Fix
[
0<etale1,
qquad
lambda_eta:=rac{eta^3}{20cdot16^3}.
]

For each physical label
[
jin{0,1,2,3},
]
fix a target density
[
rac{eta}{16}leho_jlerac18
]
and arbitrary target phases
[
	heta_{j,1},	heta_{j,2},	heta_{j,3}inmathbb R/2pimathbb Z.
]

Define
[
eta_j:=rac{ho_j}{24},
qquad
z_{j,k}:=eta_j e^{i	heta_{j,k}}
quad(k=1,2,3).
]

If
[
Plambda_eta^2>log 56,
]
then there exist four genuine Boolean subsets
[
C_jsubseteq G
]
such that, simultaneously for every (j),

[
left|rac{|C_j|}{P}-ho_jight|lelambda_eta
]
and for (k=1,2,3),
[
left|
widehat{1_{C_j}}(kr)-z_{j,k}
ight|
lelambda_eta.
]

Consequently every selected coefficient satisfies
[
left|widehat{1_{C_j}}(kr)ight|
ge
eta_j-lambda_eta
>
lambda_eta,
]
and its phase differs from the arbitrarily prescribed phase (	heta_{j,k}) by at most
[
arcsin!left(rac{lambda_eta}{eta_j}ight)
le
arcsin!left(rac{3}{640}eta^2ight).
]

Thus, whenever the concentration condition holds, **arbitrary Q07-type finite phase data at the harmonics (r,2r,3r) are approximately realizable by actual (0/1) indicators, at coefficient magnitudes far above the Q04 threshold.**

This is stronger than the abstract phase-surjectivity statement of Q07 in one respect: Booleanity and Parseval are both enforced.

It is weaker in another essential respect: the constructed (C_j) are arbitrary subsets of the cyclic ambient group. They are not asserted to be translated interval-supported fibres, internally 4-AP-free, near-extremal, or mutually carry-compatible.

Therefore Boolean realizability alone is not the missing incompatibility.

## Proof

### 1. A bounded probability profile with arbitrary phases

For each (j), define
[
p_j(x)
=
ho_j+
sum_{k=1}^3
left(
z_{j,k}e_P(krx)
+
overline{z_{j,k}}e_P(-krx)
ight),
]
where
[
e_P(t):=e^{2pi i t/P}.
]

This is real-valued. Also
[
|p_j(x)-ho_j|
le
2sum_{k=1}^3|z_{j,k}|
=
6eta_j
=
rac{ho_j}{4}.
]

Hence
[
rac34ho_j
le
p_j(x)
le
rac54ho_j
le
rac5{32}<1.
]

Therefore
[
0<p_j(x)<1
]
for every (x).

By orthogonality of the six distinct harmonics,
[
mathbb E_x p_j(x)=ho_j
]
and
[
mathbb E_x p_j(x)e_P(-krx)=z_{j,k},
qquad k=1,2,3.
]

### 2. Independent Bernoulli rounding

For every (j) and (xin G), independently choose
[
X_{j,x}simoperatorname{Bernoulli}(p_j(x))
]
and put
[
C_j:={x:X_{j,x}=1}.
]

Then
[
mathbb Erac{|C_j|}{P}=ho_j
]
and
[
mathbb Ewidehat{1_{C_j}}(kr)=z_{j,k}.
]

For a fixed real linear statistic
[
rac1Psum_x (X_{j,x}-p_j(x))a_x,
qquad |a_x|le1,
]
Hoeffding gives
[
Pr(|S|ge t)le2e^{-2Pt^2}.
]

For one complex Fourier coefficient, require its real and imaginary deviations each to be at most
[
lambda_eta/sqrt2.
]
Then
[
Prleft(
left|
widehat{1_{C_j}}(kr)-z_{j,k}
ight|>lambda_eta
ight)
le
4e^{-Plambda_eta^2}.
]

The density deviation contributes at most
[
2e^{-2Plambda_eta^2}
le
2e^{-Plambda_eta^2}.
]

Thus for one fibre, all three complex coefficients plus the density fail with probability at most
[
14e^{-Plambda_eta^2}.
]

For four fibres, the union bound gives total failure probability at most
[
56e^{-Plambda_eta^2}.
]

If
[
Plambda_eta^2>log56,
]
this is strictly below (1). Hence at least one simultaneous Boolean realization exists.

### 3. The realized coefficients remain well above Q04 scale

Because
[
ho_jgerac{eta}{16},
]
we have
[
eta_jgerac{eta}{384}.
]

Also
[
lambda_eta
=
rac{eta^3}{81920}.
]

Therefore
[
rac{lambda_eta}{eta_j}
le
rac{384}{81920}eta^2
=
rac3{640}eta^2
<
rac12.
]

In particular,
[
eta_j-lambda_eta>lambda_eta.
]

The elementary geometry of a disk of radius (lambda_eta) about the nonzero target (z_{j,k}) gives
[
|arg widehat{1_{C_j}}(kr)-	heta_{j,k}|
le
arcsin!left(rac{lambda_eta}{eta_j}ight),
]
which yields the displayed phase error.

### 4. The concentration condition holds in the relevant dyadic near-extremal regime

Protected E3-A03 records the pointwise lower construction
[
a_n:=rac{r_4(2^n)}{2^n}
ge
2^{-(C_*+o(1))sqrt n},
qquad
C_*approx2.666539.
]

In a hypothetical failure of the desired four-fibre deficit bound, the fibre densities are asymptotically comparable to (a_n). In particular it is enough here to assume
[
etagerac12a_n
]
for all sufficiently large (n).

The Q02 cyclic embedding has
[
P>8N,
qquad N=2^n.
]

Hence
[
Plambda_eta^2
gg
Neta^6
ge
2^ncdot 2^{-6(C_*+o(1))sqrt n-6},
]
which tends to (+infty).

Therefore the Boolean realizability condition
[
Plambda_eta^2>log56
]
holds eventually in the asymptotic near-extremal regime relevant to the campaign.

## What this rules out

Q05 showed that finite one-scale large-spectrum cardinality is compatible with Parseval.

Q07 showed that the full ten-family finite phase algebra is surjective.

Q08 now adds:

> Even the requirement that the prescribed finite harmonic data come from genuine (0/1) functions on the cyclic ambient group does not create a robust asymptotic contradiction.

The finite harmonic data can be realized with:
- exact Boolean values;
- approximately prescribed densities;
- all twelve prescribed (r,2r,3r) phases;
- magnitudes much larger than the Q04 witness threshold.

Thus the next linear-lane proof cannot rely only on:
1. finite support;
2. Parseval;
3. finite phase equations; or
4. Booleanity in the ambient cyclic model.

## Claim boundary

This is a proof-strategy no-go, not a construction of admissible four-fibre gluings.

The Bernoulli-rounded sets are **not** proved to satisfy:
- support inside one length-(N) interval before Q02 translation;
- internal 4-AP-freeness;
- near-extremality for (r_4(N));
- the full D01 carry system;
- or cross-fibre compatibility.

Those are now the surviving sources of rigidity.

The A03 lower construction is used only to show that the concentration condition eventually holds at the Q04 witness scale; it is not used as an inter-scale extremizer theorem.

## First defect

The linear residual reduces further to:

> **E3-B-LINEAR-WITNESS-APFREE-INTERVAL-AMPLIFICATION.**  
> Starting from Q04/Q05/Q07, exploit at least one genuinely arithmetic constraint absent from Q08:
> - interval support inherited from a physical fibre;
> - internal 4-AP-freeness and near-extremality;
> - full simultaneous carry compatibility;
> - or repeated/multi-scale witness amplification;
> to force a deletion cost or more than the Parseval capacity of independent witnesses.

A contradiction based only on finite Boolean Fourier realizability is insufficient.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-LINEAR-WITNESS-REALIZABILITY-OR-AMPLIFICATION`: **REDUCED**.
- New smallest linear residual: `E3-B-LINEAR-WITNESS-APFREE-INTERVAL-AMPLIFICATION`.
- `E3-B-DERIVATIVE-SPECTRAL-ALIGNMENT`: unchanged and still open.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q04 native result: aligned Fourier-or-fourfold witness dichotomy.
- E3-Q05 native result: Parseval capacity / one-scale support no-go.
- E3-Q07 native result: ten-family finite phase algebra surjectivity.
- E3-A03 protected result: pointwise lower construction (a_nge2^{-(C_*+o(1))sqrt n}).

# E3-Q06 — positive-density joint derivative overlap in the fourfold branch

Disposition: **PROVED_NATIVE_DERIVATIVE_OVERLAP_AMPLIFICATION**.

This is native GCL work. It refines the Q04 joint-fourfold alternative without invoking a \(U^3\) inverse theorem.

## Strongest exact statement

Fix one adjacent D01 \(0011\) family. In the Q02 cyclic model its labelled physical pattern is
\[
(A,A,B,B),
\]
up to translation of the second physical fibre.

Let
\[
a=1_A-\alpha,\qquad b=1_B-\gamma
\]
be the corresponding real balanced functions on
\[
G=\mathbb Z/P\mathbb Z,
\qquad P>8N.
\]

Assume this adjacent family lies in the Q04 **fourfold** alternative:
\[
\left|
\Lambda(a,a,b,b)
\right|
\ge
\delta,
\]
where
\[
\delta
:=
\frac{\alpha^2\gamma^2}{5}
>
\frac{\beta^4}{5\cdot16^4}.
\]

For \(d\in G\), define the real multiplicative derivatives
\[
\Delta_d a(x):=a(x)a(x+d),
\qquad
\Delta_d b(x):=b(x)b(x+d),
\]
and define
\[
I_d
:=
\mathbb E_x
\Delta_d a(x)\,
\Delta_d b(x+2d).
\]

Then exactly
\[
\Lambda(a,a,b,b)
=
\mathbb E_d I_d.
\]

Let
\[
\sigma\in\{-1,+1\}
\]
be the sign of the real number \(\Lambda(a,a,b,b)\), and set
\[
D
:=
\left\{
d\in G:
\sigma I_d\ge \delta/2
\right\}.
\]

Then
\[
\boxed{
\frac{|D|}{P}
\ge
\frac{\delta/2}{1-\delta/2}
\ge
\frac{\delta}{2}
>
\frac{\beta^4}{10\cdot16^4}.
}
\]

Thus the joint-fourfold branch produces not one isolated structural witness but a **positive-density family of shifts**:
\[
|D|
>
\frac{\beta^4}{10\cdot16^4}\,P.
\]

For every \(d\in D\), Fourier expansion gives
\[
I_d
=
\sum_{\xi\in G}
\widehat{\Delta_d a}(\xi)\,
\widehat{\Delta_d b}(-\xi)\,
e_P(-2\xi d).
\]

Hence every good shift satisfies the signed joint spectral-overlap inequality
\[
\boxed{
\operatorname{Re}
\left[
\sigma
\sum_{\xi\in G}
\widehat{\Delta_d a}(\xi)\,
\widehat{\Delta_d b}(-\xi)\,
e_P(-2\xi d)
\right]
\ge
\delta/2.
}
\]

In particular,
\[
\sum_{\xi\in G}
\left|
\widehat{\Delta_d a}(\xi)
\right|
\left|
\widehat{\Delta_d b}(-\xi)
\right|
\ge
\delta/2.
\]

This is a quantitative **joint derivative-frequency witness**. It retains the same shift \(d\), the same physical pair \((A,B)\), and the full aligned derivative spectra before any lossy selection of an individual quadratic phase.

It does not yet imply a point-deletion lower bound.

## Proof

### 1. Derivative identity

By definition,
\[
\Lambda(a,a,b,b)
=
\mathbb E_{x,d}
a(x)a(x+d)b(x+2d)b(x+3d).
\]

For fixed \(d\),
\[
a(x)a(x+d)=\Delta_d a(x),
\]
and
\[
b(x+2d)b(x+3d)=\Delta_d b(x+2d).
\]

Therefore
\[
\Lambda(a,a,b,b)
=
\mathbb E_d
\mathbb E_x
\Delta_d a(x)\Delta_d b(x+2d)
=
\mathbb E_d I_d.
\]

Because \(a,b\) are real-valued, every \(I_d\) is real.

### 2. Positive-density set of good shifts

Since \(|a|,|b|\le1\),
\[
|I_d|\le1.
\]

Let
\[
Q:=\Lambda(a,a,b,b)
\]
and choose \(\sigma\) so that
\[
\sigma Q=|Q|\ge\delta.
\]

Write
\[
p:=|D|/P.
\]

On \(D\),
\[
\sigma I_d\le1.
\]
Outside \(D\),
\[
\sigma I_d<\delta/2.
\]

Therefore
\[
\delta
\le
\mathbb E_d(\sigma I_d)
<
p+(1-p)\delta/2.
\]

Rearranging,
\[
p
\ge
\frac{\delta/2}{1-\delta/2}.
\]

Since \(0<\delta\le1\),
\[
p\ge\delta/2.
\]

Using
\[
\delta>
\frac{\beta^4}{5\cdot16^4}
\]
gives
\[
p>
\frac{\beta^4}{10\cdot16^4}.
\]

### 3. Exact derivative spectral overlap

Use normalized Fourier transform
\[
\widehat f(\xi)=\mathbb E_x f(x)e_P(-\xi x).
\]

Write
\[
\Delta_d a(x)
=
\sum_{\xi}
\widehat{\Delta_d a}(\xi)e_P(\xi x),
\]
\[
\Delta_d b(x+2d)
=
\sum_{\eta}
\widehat{\Delta_d b}(\eta)e_P(\eta x)e_P(2\eta d).
\]

Averaging in \(x\) forces
\[
\eta=-\xi.
\]

Hence
\[
I_d
=
\sum_{\xi}
\widehat{\Delta_d a}(\xi)
\widehat{\Delta_d b}(-\xi)
e_P(-2\xi d).
\]

For \(d\in D\),
\[
\sigma I_d\ge\delta/2.
\]

Taking real parts gives the signed joint spectral-overlap inequality. Taking absolute values termwise gives
\[
\sum_\xi
|\widehat{\Delta_d a}(\xi)|
|\widehat{\Delta_d b}(-\xi)|
\ge
|I_d|
\ge
\delta/2.
\]

## Why this is stronger than separate U3 witnesses

Q03 proves every physical fibre has large \(U^3\) norm.

A separate \(U^3\) inverse theorem applied to \(A\) and \(B\) may select unrelated quadratic witnesses.

Q06 keeps the original joint correlation and proves that, for a positive-density set of **the same derivative shifts \(d\)**, the derivative spectra of \(A\) and \(B\) already have large phase-corrected overlap.

Thus the genuinely quadratic lane can be attacked before integrating derivative frequencies into global quadratic phases.

## What Q06 does not prove

The overlap
\[
\sum_\xi
|\widehat{\Delta_d a}(\xi)|
|\widehat{\Delta_d b}(-\xi)|
\ge\delta/2
\]
does not by itself force a single Fourier mode to carry polynomial mass independent of \(P\). The overlap may be spectrally diffuse.

Therefore Q06 does not yet produce:
- a common derivative frequency map \(d\mapsto\xi_d\);
- an approximate Freiman-linear frequency map;
- a common quadratic phase;
- or a deletion/transversal lower bound.

## First defect

The live fourfold residual becomes:

> **E3-B-DERIVATIVE-SPECTRAL-ALIGNMENT.**  
> Given a set of at least
> \[
> c\beta^4P
> \]
> shifts \(d\) on which two adjacent physical fibres have signed derivative spectral overlap at least
> \[
> c\beta^4,
> \]
> prove either:
> 1. concentration on a coherent derivative-frequency graph \(d\mapsto\xi_d\) with enough additive structure to integrate to a joint quadratic witness; or
> 2. spectral diffuseness strong enough to force a point-deletion cost
> \[
> \gtrsim \beta^{1+\theta}N
> \]
> for some \(\theta<1\).

This is a strictly earlier witness-retaining interface than independent quadratic inverse theorems.

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\` remains **OPEN**.
- \`E3-B-FOUR-FIBRE-DEFICIT\` remains **OPEN_NATIVE_SUBTARGET**.
- \`E3-B-ADJACENT-WITNESS-DICHOTOMY\` remains **PROVED_NATIVE**.
- In the Q04 fourfold branch, positive-density derivative overlap is now **PROVED_NATIVE**.
- The fourfold lane is reduced to derivative-spectral alignment/diffuseness.
- No parent theorem or gluing-radius candidate is promoted.

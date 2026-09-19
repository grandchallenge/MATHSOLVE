# NS-CI-R014-A2-L5-42 — intrinsic one-sided direction-compression cost

## Disposition

- Campaign: \`NS-CI-001\`
- Restricted target: \`NS-CI-R014-A2\`
- Tracker: \`MATHSOLVE#59\`
- Protected mathematical predecessor:
  \`a75e8d7ac74c051d1b57580156712122fac7272b\` (L5-41)
- Protected integration base:
  \`e5aae5f07492562da0edb4d9d9b35f0e01afa6d6\`
- Result class: exact factorization-gauge audit plus one-sided stopped-flow theorem
- Result:
  \`RECIPROCAL_AMPLITUDE_PRODUCT_NOT_INTRINSIC__COMPRESSION_EXIT_CONTROLLED_BY_GAUGE_FREE_NEGATIVE_DIRECTION_VARIATION\`
- A2 theorem: open
- L5: active
- L3/L4: closed
- MATHCERT adjudication: absent

L5-41 proves a useful sufficient estimate in one chosen direction
factorization

\`\`\`math
v(s,Y)=\beta(s)B(s,Y).
\`\`\`

With

\`\`\`math
D_b=\int_0^S\int |\partial_Y b|^2\,dY\,ds
\`\`\`

and

\`\`\`math
A_\beta=\int_0^S\int \frac{|\beta(s)|^2}{|b(s,Y)|^2}\,dY\,ds,
\`\`\`

that estimate gives a two-sided distortion-exit bound proportional to

\`\`\`math
D_b^{1/2}A_\beta^{1/2}.
\`\`\`

This tranche audits whether that product can itself be the durable
equation-level quantity.

It cannot without an additional normalization convention.

The characteristic geometry depends only on the actual direction transport
field \`v\`, while the split \`v=\beta B\` has a scale gauge.  The intrinsic
first-order compression quantity is instead the negative variation of
\`\partial_Yv\`.

The key one-sided theorem is

\`\`\`math
\boxed{
\left|
\left\{
Z:
\inf_{0\le s\le S}\log J(s,Z)\le-K
\right\}
\right|
\le
\frac{e^K}{K}
\mathcal V_v^-,
}
\`\`\`

where

\`\`\`math
\mathcal V_v^-
=
\int_0^S\int
(-\partial_Yv(s,Y))_+
\,dY\,ds.
\`\`\`

Unlike the L5-41 two-sided stopping argument, this theorem does not stop
expansion.  For the reciprocal-Jacobian problem, only a lower bound on \`J\`
is needed before the first compression hit.

## 1. Direction characteristic

Let

\`\`\`math
\partial_s\chi(s,Z)
=
v(s,\chi(s,Z)),
\qquad
\chi(0,Z)=Z,
\`\`\`

be an orientation-preserving one-dimensional periodic characteristic flow.

Write

\`\`\`math
J(s,Z)=\partial_Z\chi(s,Z)>0.
\`\`\`

Then

\`\`\`math
\boxed{
\partial_s\log J(s,Z)
=
\partial_Yv(s,\chi(s,Z)).
}
\`\`\`

This identity is intrinsic.  It contains no choice of factorization of \`v\`.

## 2. Factorization gauge

Suppose

\`\`\`math
v(s,Y)=\beta(s)B(s,Y).
\`\`\`

For any positive scalar function \`c(s)\`, define

\`\`\`math
\widetilde\beta(s)
=
c(s)\beta(s),
\qquad
\widetilde B(s,Y)
=
c(s)^{-1}B(s,Y).
\`\`\`

Then exactly

\`\`\`math
\widetilde\beta\,\widetilde B
=
\beta B
=
v.
\`\`\`

Therefore the following objects are unchanged:

- the characteristic map \`\chi\`;
- the Jacobian \`J\`;
- the tangent cocycle \`\log J\`;
- every compression or expansion event of the frame.

If the protected chart condition is

\`\`\`math
|\partial_YB|
\le
|\partial_Ye|,
\qquad
e=b/|b|,
\`\`\`

then every constant rescaling with \`c\ge1\` preserves that inequality because

\`\`\`math
|\partial_Y\widetilde B|
=
c^{-1}|\partial_YB|
\le
|\partial_Ye|.
\`\`\`

Thus the protected hypotheses do not fix the scale of the factorization.

## 3. Why the L5-41 product is not intrinsic

Under a constant rescaling \`c>0\`,

\`\`\`math
\widetilde A_\beta
=
c^2 A_\beta.
\`\`\`

The raw carrier-gradient quantity \`D_b\` is unchanged.

Hence

\`\`\`math
\boxed{
D_b^{1/2}
\widetilde A_\beta^{1/2}
=
c
D_b^{1/2}
A_\beta^{1/2}.
}
\`\`\`

For every admissible factorization, choosing a larger constant \`c\` produces
the same \`v,\chi,J\` but an arbitrarily larger L5-41 sufficient product.

Therefore

\`\`\`text
small D_b^(1/2) A_beta^(1/2)
\`\`\`

cannot be an invariant necessary property of the actual direction geometry.

L5-41 remains correct as a sufficient estimate after a factorization has been
fixed.  The present result only rejects promoting that factorization-dependent
quantity to the intrinsic equation-level frontier.

## 4. A gauge-invariant mixed factorization cost

Define at each time

\`\`\`math
d_B(s)
=
\int
|b(s,Y)|^2
|\partial_YB(s,Y)|^2
\,dY
\`\`\`

and

\`\`\`math
a_\beta(s)
=
\int
\frac{|\beta(s)|^2}{|b(s,Y)|^2}
\,dY.
\`\`\`

Set

\`\`\`math
\boxed{
\mathcal C_{B,\beta}
=
\int_0^S
d_B(s)^{1/2}
a_\beta(s)^{1/2}
\,ds.
}
\`\`\`

Under an arbitrary positive time-dependent gauge \`c(s)\`,

\`\`\`math
d_{\widetilde B}(s)
=
c(s)^{-2}d_B(s),
\qquad
a_{\widetilde\beta}(s)
=
c(s)^2a_\beta(s).
\`\`\`

Therefore

\`\`\`math
\boxed{
\mathcal C_{\widetilde B,\widetilde\beta}
=
\mathcal C_{B,\beta}.
}
\`\`\`

This time-local mixed product is fully factorization-gauge invariant.

## 5. Relation to the intrinsic variation of v

Since

\`\`\`math
\partial_Yv
=
\beta\,\partial_YB,
\`\`\`

spatial Cauchy--Schwarz at each time gives

\`\`\`math
\begin{aligned}
\int
|\partial_Yv|
\,dY
&=
|\beta(s)|
\int
|\partial_YB|
\,dY
\\
&\le
\left(
\int
|b|^2|\partial_YB|^2
\,dY
\right)^{1/2}
\left(
\int
\frac{|\beta|^2}{|b|^2}
\,dY
\right)^{1/2}.
\end{aligned}
\`\`\`

Hence, with

\`\`\`math
\mathcal V_v
=
\int_0^S\int
|\partial_Yv|
\,dY\,ds,
\`\`\`

one has

\`\`\`math
\boxed{
\mathcal V_v
\le
\mathcal C_{B,\beta}.
}
\`\`\`

Thus the exact amplitude/direction factorization has an invariant
interpretation: it is one sufficient upper bound for the total Eulerian
variation of the actual direction transport field.

If

\`\`\`math
D_B=\int_0^S d_B(s)\,ds,
\qquad
A_\beta=\int_0^S a_\beta(s)\,ds,
\`\`\`

then Cauchy--Schwarz in time also gives

\`\`\`math
\mathcal C_{B,\beta}
\le
D_B^{1/2}A_\beta^{1/2}.
\`\`\`

Because

\`\`\`math
D_B
\le
D_b
\`\`\`

by L5-38 chart domination, L5-41 is recovered as the coarser sufficient chain

\`\`\`math
\mathcal V_v
\le
\mathcal C_{B,\beta}
\le
D_B^{1/2}A_\beta^{1/2}
\le
D_b^{1/2}A_\beta^{1/2}.
\`\`\`

The first two quantities retain the actual factorization correlation that the
last replacement discards.

## 6. One-sided compression stopping time

Fix \`K>0\`.

Define the first compression time

\`\`\`math
\tau_K^-(Z)
=
\inf
\left\{
s\in[0,S]:
\log J(s,Z)=-K
\right\}
\wedge S.
\`\`\`

Define the compression-exit set

\`\`\`math
\mathcal C_K^-
=
\left\{
Z:
\inf_{0\le s\le S}
\log J(s,Z)
\le
-K
\right\}.
\`\`\`

For every label in \`\mathcal C_K^-\`,

\`\`\`math
K
\le
\int_0^{\tau_K^-(Z)}
\left(
-\partial_Yv(s,\chi(s,Z))
\right)_+
\,ds.
\`\`\`

Before the first compression hit,

\`\`\`math
J(s,Z)\ge e^{-K}.
\`\`\`

No upper bound on \`J\` is required.

## 7. Exact one-sided compression theorem

Integrating the preceding inequality over compression-exit labels gives

\`\`\`math
K|\mathcal C_K^-|
\le
\int
\int_0^{\tau_K^-(Z)}
(-\partial_Yv(s,\chi(s,Z)))_+
\,ds\,dZ.
\`\`\`

At each time, change variables only over labels not yet compressed past
\`e^{-K}\`.

Because

\`\`\`math
dZ
=
J^{-1}dY
\le
e^K dY,
\`\`\`

one obtains

\`\`\`math
K|\mathcal C_K^-|
\le
e^K
\int_0^S\int
(-\partial_Yv(s,Y))_+
\,dY\,ds.
\`\`\`

Define

\`\`\`math
\boxed{
\mathcal V_v^-
=
\int_0^S\int
(-\partial_Yv)_+
\,dY\,ds.
}
\`\`\`

Then

\`\`\`math
\boxed{
|\mathcal C_K^-|
\le
\frac{e^K}{K}
\mathcal V_v^-.
}
\`\`\`

This is the intrinsic one-sided compression theorem.

It depends only on the actual vector field \`v\).

It does not require:

- a choice of \`\beta,B\` gauge;
- a prior upper bound on \`J\`;
- an expansion stopping time;
- reciprocal-amplitude smallness as a separate hypothesis.

## 8. Why the one-sided theorem is sharper for L5-40

The L5-40 obstruction contains

\`\`\`math
J^{-1}.
\`\`\`

The dangerous geometry is therefore compression:

\`\`\`math
J\ll1.
\`\`\`

Large expansion

\`\`\`math
J\gg1
\`\`\`

makes \`J^{-1}\` smaller rather than larger.

L5-41 stopped both compression and expansion because it bounded the full
two-sided event

\`\`\`math
|\log J|\ge K.
\`\`\`

For the reciprocal-occupation denominator, that symmetry is unnecessary.

The one-sided theorem keeps exactly the relevant sign.

## 9. Periodic mean-zero strain does not solve compression

On one periodic direction coordinate,

\`\`\`math
\int
\partial_Yv(s,Y)
\,dY
=
0
\`\`\`

at every time.

Therefore

\`\`\`math
\int
(\partial_Yv)_+
\,dY
=
\int
(-\partial_Yv)_+
\,dY
=
\frac12
\int
|\partial_Yv|
\,dY.
\`\`\`

Consequently,

\`\`\`math
\boxed{
\mathcal V_v^-
=
\frac12\mathcal V_v
}
\`\`\`

for the full periodic coordinate.

This gives an exact warning:

\`\`\`text
zero Eulerian signed mean strain
does not imply
small compression cost.
\`\`\`

Any useful cancellation beyond the factor \`1/2\` must be genuinely
Lagrangian, packet-weighted, or correlated with the critical observable.

A scalar statement such as

\`\`\`math
\int\partial_Yv\,dY=0
\`\`\`

cannot close the route.

## 10. Relation to reciprocal amplitude

The gauge-invariant chain gives

\`\`\`math
\boxed{
\mathcal V_v^-
\le
\mathcal V_v
\le
\mathcal C_{B,\beta}.
}
\`\`\`

Thus reciprocal amplitude remains useful only through its correlation with the
angular profile inside the invariant mixed cost.

The raw replacement

\`\`\`math
D_B
\le
D_b
\`\`\`

forgets that correlation.

This is exactly where L5-41 becomes a sufficient but potentially very coarse
criterion.

The improved equation-level question is not

\`\`\`text
is A_beta small?
\`\`\`

by itself.

It is

\`\`\`text
is the actual compressive variation of the extracted direction transport
small on the packet mass that carries the critical observable?
\`\`\`

## 11. Compression calibration revisited

Take the L5-41 geometric separator

\`\`\`math
B(Y)=\sin Y,
\qquad
\beta=-\kappa/S.
\`\`\`

Then

\`\`\`math
v(Y)
=
-\frac{\kappa}{S}\sin Y,
\qquad
\partial_Yv
=
-\frac{\kappa}{S}\cos Y.
\`\`\`

The signed spatial mean vanishes exactly:

\`\`\`math
\int\partial_Yv\,dY=0.
\`\`\`

Nevertheless the fixed label \`Z=0\` obeys

\`\`\`math
J(s,0)
=
e^{-\kappa s/S}.
\`\`\`

Thus exact Eulerian sign cancellation coexists with exponential pathwise
compression.

This is the simplest separator against replacing the intrinsic negative
variation by a signed spatial average.

It is still a geometric normal-form calibration, not a selected whole-space
NSE counterexample.

## 12. What selected NSE currently supplies

Protected L5-38 gives equation-level A2/Leray control of far-low **raw
velocity** derivatives.

It does not identify the present \`v\` with a raw velocity component.

The extracted direction field still inherits normalization and packet
geometry.

Therefore no protected theorem currently gives

\`\`\`math
\mathcal V_v^-<\infty
\`\`\`

or, more importantly, the scale-small packet-weighted version needed to make
the compression-exit set negligible for the critical observable.

Likewise, periodic incompressibility of the physical velocity cannot simply be
transferred to \`v\`: the direction-coordinate flow is a frame flow, not the
physical incompressible particle flow.

Thus the intrinsic compression cost is now identified, but not yet controlled
by selected whole-space active-band NSE.

## 13. Observable-weighted successor form

Let \`q_h(Z)dZ\` be the critical-observable label density.

The quantity actually needed downstream is smaller than a uniform full-label
bound.

A viable successor may prove directly that

\`\`\`math
\int_{\mathcal C_K^-}
q_h(Z)\,dZ
\to0
\`\`\`

for a fixed useful \`K\`, even when the unweighted set
\`\mathcal C_K^-\` is not small.

This can arise from:

1. packet-weighted control of negative Lagrangian strain;
2. anti-correlation between critical mass and compressive labels;
3. equation-derived depletion of \`(-\partial_Yv)_+\` on the active packet;
4. a selector/dissipation charge whenever persistent compressive direction
   variation overlaps the critical packet.

This is strictly weaker than a uniform frame theorem.

## 14. Hard rejection tests

Reject any successor that:

- treats \`D_b^{1/2}A_\beta^{1/2}\` as an intrinsic necessary quantity without
  fixing a factorization gauge;
- changes \`\beta,B\` while claiming the characteristic geometry changed when
  the product \`\beta B\` did not;
- uses the Eulerian signed mean
  \`\int\partial_Yv\,dY=0\` as a compression bound;
- stops expansion when only reciprocal-Jacobian compression is being audited,
  unless another downstream estimate genuinely requires two-sided distortion;
- identifies the frame flow \`v\` with the physical incompressible velocity
  without an equation-derived reconstruction theorem;
- claims the present intrinsic reduction already bounds the critical
  observable mass on compressed labels;
- controls only \`\Omega_1\` while silently promoting \`U_2,U_3,U_4\`;
- reopens L3 or L4 without their protected reopening conditions.

## 15. Claim boundary

The bounded result sought is exactly

\`\`\`text
RECIPROCAL_AMPLITUDE_PRODUCT_NOT_INTRINSIC
__COMPRESSION_EXIT_CONTROLLED_BY_GAUGE_FREE_NEGATIVE_DIRECTION_VARIATION.
\`\`\`

It proves:

- the protected split \`v=\beta B\` has an unfixed positive scalar gauge;
- \`D_b^{1/2}A_\beta^{1/2}\` changes under that gauge while the actual
  characteristic geometry remains identical;
- the time-local mixed cost
  \`\mathcal C_{B,\beta}\` is gauge invariant;
- \`\mathcal V_v\le\mathcal C_{B,\beta}\`;
- the dangerous one-sided reciprocal-Jacobian event obeys
  \`|\mathcal C_K^-|\le e^K K^{-1}\mathcal V_v^-\`;
- expansion need not be stopped for this compression theorem;
- on a periodic coordinate, full-space signed strain cancellation gives only
  \`\mathcal V_v^-=\mathcal V_v/2\`, not a smallness mechanism;
- existing A2/Leray results do not yet control the intrinsic direction
  compression variation on the critical packet.

It does not prove a whole-space NSE compression bound.

It does not prove that large intrinsic compression variation pays selector
charge.

It does not control \`U_2,U_3,U_4\`.

It does not prove A2.

No MATHCERT, novelty, priority, publication, patent, product, or commercial
claim is asserted.

## 16. Next live obligation

The smallest safe successor is
\`C2-MIX-DIRECTION-INTRINSIC-COMPRESSION-COST\`:

> Can selected whole-space active-band dynamics control the packet-weighted
> negative variation of the actual extracted direction transport
> \`(-\partial_Yv)_+\`, or does persistent overlap between that compressive
> variation and the critical packet force a selector/dissipation charge?

Audit the tangent component first.  Higher normalized jets remain downstream.

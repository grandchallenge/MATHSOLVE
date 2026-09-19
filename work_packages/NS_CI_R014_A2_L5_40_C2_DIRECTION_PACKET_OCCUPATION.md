# NS-CI-R014-A2-L5-40 — packet-weighted direction occupation bridge

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected predecessor / integration base:
  `6195e86539971dab55e3819b8126a606b901e9a9` (L5-39)
- Result class: conditional first-order packet-occupation theorem plus exact calibration
- Result:
  `RECIPROCAL_PACKET_OCCUPATION_CONTROLS_TANGENT_COCYCLE_AE__RECIPROCAL_AMPLITUDE_NOT_CONTROLLED_BY_COARSE_A2_LERAY`
- A2 theorem: open
- L5: active
- L3/L4: closed
- MATHCERT adjudication: absent

L5-38 proved the amplitude-weighted first angular-strain estimate

```math
|b|^2 |\partial_Y(b/|b|)|^2
\le
|\partial_Y b|^2.
```

L5-39 then proved that this does not yield a uniform all-streamline
unweighted direction bound from the existing coarse A2/Leray envelopes.

This tranche identifies the exact missing first-order packet quantity.
The obstruction factorizes into:

```text
weighted angular-energy trace
x
reciprocal amplitude / metric occupation.
```

The first factor is controlled by L5-38 and Leray-type raw gradient energy.
The second is new information.

## 1. Direction characteristic and tangent cost

Let

```math
\partial_s\chi(s,Z)
=
v(s,\chi(s,Z)),
\qquad
\chi(0,Z)=Z,
```

be an orientation-preserving one-dimensional characteristic map and write

```math
J(s,Z)=\partial_Z\chi(s,Z)>0.
```

Assume the principal direction coefficient has the form

```math
v(s,Y)=\beta(s) B(s,Y),
```

where `B` is extracted from a normalized carrier direction
`e=b/|b|` in a chart satisfying

```math
|\partial_Y B|
\le
|\partial_Y e|.
```

The absolute tangent-strain cost on one label is

```math
\Omega_{\rm abs}(Z)
=
\int_0^S
|\beta(s)|
|\partial_Y B(s,\chi(s,Z))|
\,ds.
```

The signed L5-37 tangent cocycle obeys

```math
|\Omega_1(s,Z)|
\le
\Omega_{\rm abs}(Z)
```

for every `s\le S`.

## 2. Exact occupation factorization

Define

```math
E(Z)
=
\int_0^S
J(s,Z)
|b(s,\chi(s,Z))|^2
|\partial_Y B(s,\chi(s,Z))|^2
\,ds
```

and

```math
R_\beta(Z)
=
\int_0^S
\frac{|\beta(s)|^2}
{J(s,Z)|b(s,\chi(s,Z))|^2}
\,ds.
```

On labels where the carrier is nonzero almost everywhere along the path,
Cauchy--Schwarz gives exactly

```math
\boxed{
\Omega_{\rm abs}(Z)^2
\le
E(Z)R_\beta(Z).
}
```

This is the packet-occupation factorization.

The Jacobian weight is the one used here to return the first factor to
physical coordinates without assuming the frame is already uniformly
bi-Lipschitz.

## 3. Eulerian control of the weighted factor

Because

```math
dY=J(s,Z)\,dZ,
```

one has

```math
\int E(Z)\,dZ
=
\int_0^S\int
|b(s,Y)|^2
|\partial_Y B(s,Y)|^2
\,dY\,ds.
```

By the chart domination and L5-38,

```math
|b|^2|\partial_Y B|^2
\le
|b|^2|\partial_Y e|^2
\le
|\partial_Y b|^2.
```

Hence

```math
\boxed{
\int E(Z)\,dZ
\le
\int_0^S\int
|\partial_Y b|^2
\,dY\,ds.
}
```

Thus the weighted numerator is an ordinary raw-gradient energy quantity.

## 4. Packet-averaged tangent theorem

Assume

```math
D_b
:=
\int_0^S\int
|\partial_Y b|^2
\,dY\,ds
<\infty
```

and

```math
\mathcal R_\beta
:=
\int
R_\beta(Z)
\,dZ
<\infty.
```

Applying Cauchy--Schwarz in label space gives

```math
\boxed{
\int
\Omega_{\rm abs}(Z)
\,dZ
\le
D_b^{1/2}
\mathcal R_\beta^{1/2}.
}
```

Consequently, for every `K>0`,

```math
\boxed{
\left|
\{Z:\Omega_{\rm abs}(Z)>K\}
\right|
\le
\frac{D_b^{1/2}\mathcal R_\beta^{1/2}}{K}.
}
```

Therefore finite reciprocal packet occupation implies first-order tangent
cocycle control on all but a quantitatively small set of labels.

On the good-label set `\Omega_{\rm abs}\le K`,

```math
e^{-K}
\le
J(s,Z)
\le
e^K
```

for all `0\le s\le S`.

This is an almost-everywhere / packet-mass conclusion.  It is intentionally
weaker than the uniform frame contract assumed in L5-35.

## 5. Interface with the L5-35 observable

Let `q_h(Z)dZ` denote a nonnegative label-space density representing the
portion of a critical observable under consideration.

If a family `q_h` is uniformly integrable in label space and carries a fixed
positive total critical contribution, then the preceding bad-label measure
bound allows one to choose `K` so that the high-strain labels carry
arbitrarily small `q_h`-mass.

Thus a sufficient first-order route to preserve critical mass is:

1. a uniform bound on `D_b`;
2. a uniform reciprocal occupation bound `\mathcal R_\beta`;
3. uniform integrability of the relevant critical-observable densities.

This tranche proves only the analytic reduction.  It does not derive items 2
or 3 from selected whole-space NSE.

## 6. Exact L5-39 calibration of the reciprocal-amplitude component

Return to the protected periodic shear

```math
b_{k,\varepsilon}(t,x)
=
A_0e^{-\nu k^2t}
(0,\varepsilon\cos(kx),\sin(kx)).
```

Its physical `x` labels are invariant, so the physical-flow Jacobian in
that label is one.  Using unit sampling weight isolates the reciprocal-amplitude
component

```math
\mathcal R_{\rm amp}
=
\int_I\int
\frac{1}{|b_{k,\varepsilon}(t,x)|^2}
\,dx\,dt.
```

This is not asserted to be the full L5-37 functional
`\mathcal R_\beta`: the factor `|\beta|^2/J` there belongs to the
direction-flow geometry and requires its own equation-level analysis.

For the protected shear,

```math
|b|^2
=
A_0^2 e^{-2\nu k^2t}
(
\varepsilon^2\cos^2(kx)+\sin^2(kx)
).
```

On one normalized spatial period,

```math
\frac{1}{2\pi}
\int_0^{2\pi}
\frac{dx}
{\varepsilon^2\cos^2x+\sin^2x}
=
\frac1\varepsilon.
```

Therefore on the parabolic interval
`I=[0,c/(\nu k^2)]`,

```math
\boxed{
\mathcal R
=
\frac{e^{2c}-1}
{2\nu k^2 A_0^2}
\frac1\varepsilon
}
```

up to the chosen normalized spatial-volume convention.

Thus the exact family from L5-39 has:

```text
coarse annular supremum:       uniformly controlled
energy/dissipation envelopes:  uniformly controlled
Lambda^2 occupancy:            uniformly controlled
reciprocal amplitude occupation: diverges like 1/epsilon.
```

Therefore the amplitude denominator appearing inside the full packet
occupation functional is genuinely new information.  This calibration does
not rule out a compensating correlation in the direction-flow factor
`|beta|^2/J`; deriving or refuting such a correlation is part of the next
occupation-cost tranche.

## 7. What has and has not been gained

Gained:

- the first normalized-direction denominator is no longer an unspecified
  "nondegeneracy problem";
- it is represented by the exact reciprocal occupation functional
  `\mathcal R_\beta`;
- the amplitude-weighted numerator is already controlled by raw gradient
  energy;
- finite `\mathcal R_\beta` gives quantitative almost-everywhere tangent
  cocycle control.

Not gained:

- no proof that selected A2 dynamics make `\mathcal R_\beta` finite;
- no uniform all-label frame theorem;
- no control of `U_2,U_3,U_4`;
- no top active-band raw-jet closure;
- no proof that the critical observable densities are uniformly integrable
  before the remaining geometry is controlled;
- no A2 theorem.

## 8. Hard rejection tests

Reject any successor that:

- drops the reciprocal amplitude factor;
- replaces packet occupation by an annular supremum lower bound;
- removes the Jacobian factor without supplying a valid change-of-variables
  argument;
- claims almost-everywhere tangent control is already the full L5-35 smooth
  frame contract;
- assumes the critical observable automatically avoids the bad-label set;
- treats the L5-39 periodic family as a whole-space A2 counterexample;
- differentiates the selector;
- reopens L3 or L4 without their protected reopening conditions.

## 9. Claim boundary

The bounded result sought is exactly

```text
RECIPROCAL_PACKET_OCCUPATION_CONTROLS_TANGENT_COCYCLE_AE
__COARSE_A2_LERAY_DOES_NOT_CONTROL_OCCUPATION.
```

It proves a sufficient first-order packet-occupation interface and shows that
the protected L5-39 calibration diverges precisely in that new interface.

A2 remains open.  No MATHCERT, novelty, priority, publication, patent,
product, or commercial claim is asserted.

## 10. Next live obligation

The smallest safe successor is
`C2-MIX-DIRECTION-OCCUPATION-COST`:

> Can selected whole-space active-band dynamics bound the reciprocal occupation
> functional on the packet mass contributing to the critical observable, or
> does failure of that bound itself force a selector/dissipation charge?

Audit the tangent component first.  Higher normalized jets remain downstream.

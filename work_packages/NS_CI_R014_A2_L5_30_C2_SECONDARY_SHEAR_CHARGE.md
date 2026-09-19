# NS-CI-R014-A2-L5-30 — polarization defect as an exact secondary shear charge

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `ae74d9572ea615248df87dd0a175bf054e300338`
- Result:
  `EXACT_SECONDARY_SHEAR_CHARGE_PROVED__R_SQUARED_DELTA_DIVERGENCE_FORCES_C_OVER_NU`
- A2 theorem: open
- L5: active
- C2-MIX-ALIGN-TIME: resolved positively in an exact polarization subfamily
- MATHCERT adjudication: absent
- Evidence class: exact smooth unforced periodic 2.5D NSE calibration;
  not the selected whole-space A2 class

L5-29 shows that the same-band polarization defect can range from zero to
order one while scalar shell data remain fixed.

A one-parameter subfamily of that exact polarization family is itself an exact
unforced 2.5D Navier--Stokes trajectory.

Let

```math
\delta\in(0,1],
\qquad
R=\frac{A}{\nu N},
\qquad
\rho=R\delta.
```

The parameter `\delta` is exactly the L5-29 projected polarization null
factor.

In the exact trajectory, `A\delta` is the amplitude of a decaying horizontal
shear and `A` is the amplitude of a vertical carrier.

The effective shear Reynolds number is

```math
\rho
=
\frac{A\delta}{\nu N}.
```

Two regimes together give a stronger dynamic conclusion.

### Bounded effective shear

If `\rho` stays in a fixed bounded range, a short parabolic-time Duhamel
expansion gives a generated neighboring coefficient of size

```math
c\rho A.
```

It violates the viscous threshold whenever

```math
R\rho
=
R^2\delta
\to\infty.
```

The violating neighboring shell persists on a fixed fraction of a parabolic
interval and therefore contributes selector charge `c/\nu`.

### Large effective shear

If `\rho\to\infty`, the protected L5-26 critical shear analysis applies with
`\rho` in place of `R`. It produces a threshold-violating front at

```math
N\rho^{1/3}
```

and again contributes selector charge `c/\nu`.

Consequently, for this exact family,

```math
\boxed{
R^2\delta\to\infty
\quad\Longrightarrow\quad
\int_{I_R}\Lambda(t)^2\,dt
\ge
\frac c\nu
}
```

for a suitable interval `I_R` and all sufficiently large `R`.

Thus persistent polarization defect is not merely a failure of the L5-28
residual hypothesis. In this calibration it can become a **secondary principal
mixing channel** and pay the critical selector cost itself.

The regime not resolved by this calibration theorem is only

```math
R^2\delta=O(1),
```

that is,

```math
\delta=O(R^{-2}).
```

This is much narrower than the `R^{-2/3}` corridor required to ignore the
channel as an NF4 residual at the primary critical scale.

## 1. Exact polarization subfamily

Use the L5-29 source frequencies

```math
k_1=(N,0,0),
\qquad
k_2=(0,N,0).
```

Take

```math
\alpha=\frac\pi2
```

and choose `\beta\in[0,\pi/2)` so that

```math
\delta=\cos\beta.
```

Then the unit source polarizations are

```math
a=e_3,
\qquad
b=
\left(
\delta,
0,
\sqrt{1-\delta^2}
\right).
```

Since

```math
\sin(\alpha+\beta)
=
\cos\beta
=
\delta,
```

L5-29 gives the initial projected sum-frequency interaction magnitude

```math
\frac{A^2N}{2}\delta.
```

## 2. Exact 2.5D NSE embedding

Define the horizontal shear

```math
U(t,Y)
=
A\delta
e^{-\nu N^2t}
\cos Y,
\qquad
Y=Nx_2.
```

Let

```math
v=(U,0).
```

Then

```math
(v\cdot\nabla)v=0,
\qquad
\partial_t v=\nu\Delta v.
```

Let the vertical component be

```math
w=z
+
A\sqrt{1-\delta^2}
e^{-\nu N^2t}
\cos Y,
```

where `z` solves

```math
\partial_t z
+
U(t,Y)\partial_{x_1}z
=
\nu\Delta z,
\qquad
z(0,x)=A\cos(Nx_1).
```

The added `Y\)-only vertical heat mode has zero `x_1\) derivative and does
not couple to the shear transport.

Therefore

```math
u=(U,0,w)
```

is an exact smooth unforced 3D Navier--Stokes solution in the periodic 2.5D
class.

At time zero it is exactly the two-mode L5-29 polarization field for this
\((\alpha,\beta)\).

## 3. Effective shear parameter

Set

```math
B=A\delta.
```

Then

```math
\rho
=
\frac{B}{\nu N}
=
R\delta.
```

Normalize the carrier by

```math
z=A\theta.
```

For `\rho>0`, introduce shear-turnover time

```math
\tau=BNt.
```

Then

```math
\boxed{
\partial_\tau\theta
+
e^{-\tau/\rho}
\cos Y\,\partial_X\theta
=
\rho^{-1}\Delta\theta,
\qquad
\theta(0)=\cos X.
}
```

This is exactly the protected L5-23 shear-chain equation with effective
Reynolds number `\rho`.

The carrier amplitude `A` factors out of the normalized scalar dynamics.

## 4. Parabolic normalization for bounded \(\rho\)

For the bounded-`\rho` regime, set

```math
\sigma=\nu N^2t.
```

For the complex carrier

```math
z
=
A\operatorname{Re}
[
e^{iX}\psi_\rho(\sigma,Y)
],
```

the exact scalar equation is

```math
\boxed{
\partial_\sigma\psi_\rho
+
i\rho e^{-\sigma}\cos Y\,\psi_\rho
=
(\partial_Y^2-1)\psi_\rho,
\qquad
\psi_\rho(0)=1.
}
```

Write

```math
\psi_\rho
=
\sum_n a_n^\rho(\sigma)e^{inY}.
```

Then

```math
(a_n^\rho)'
=
-(1+n^2)a_n^\rho
-
\frac{i\rho e^{-\sigma}}2
(a_{n-1}^\rho+a_{n+1}^\rho).
```

## 5. First neighboring coefficient

At `\rho=0`,

```math
a_0^0=e^{-\sigma},
\qquad
a_n^0=0
\quad(n\ne0).
```

The first Duhamel iterate for `a_1` is exact at first order in `\rho`:

```math
\boxed{
a_{1,\mathrm{lin}}^\rho(\sigma)
=
-\frac{i\rho\sigma}{2}
e^{-2\sigma}.
}
```

Indeed, both the forcing product and the \(n=1\) heat semigroup carry total
decay \(e^{-2\sigma}\).

## 6. Uniform short-time lower bound for bounded \(\rho\)

Fix one finite constant `M\ge1`.

The scalar semigroup is contractive in `L^2`, and multiplication by
`\cos Y` has norm one.

Duhamel therefore gives on `0\le\sigma\le1`

```math
\|\psi_\rho(\sigma)-e^{-\sigma}\|_2
\le
C\rho\sigma
```

and the error in the first neighboring coefficient relative to the linear
iterate is

```math
|a_1^\rho-a_{1,\mathrm{lin}}^\rho|
\le
C\rho^2\sigma^2.
```

Choose a fixed

```math
\sigma_M
=
\frac{c}{M}
```

with \(c>0\) sufficiently small.

Then for every

```math
0<\rho\le M
```

and every

```math
\frac{\sigma_M}{2}
\le
\sigma
\le
\sigma_M,
```

the error is at most one half of the linear term.

Hence

```math
\boxed{
|a_1^\rho(\sigma)|
\ge
c_M\rho,
}
```

where `c_M>0` depends only on the fixed `M`.

## 7. Bounded-\(\rho\) threshold and charge

The neighboring physical frequency

```math
N(1,1,0)
```

has magnitude comparable to `N`.

Finite LP overlap gives one neighboring block with

```math
\|u_p\|_\infty
\ge
c_M A\rho.
```

Thus

```math
\boxed{
\lambda_p^{-1}\|u_p\|_\infty
\ge
c_M\nu R\rho.
}
```

Since

```math
R\rho
=
R^2\delta,
```

this block violates the fixed campaign threshold for all sufficiently large
`R` whenever

```math
R^2\delta\to\infty.
```

The lower bound holds throughout a fixed \(\sigma\)-interval of length
comparable to \(1/M\).

Because

```math
dt
=
\frac{d\sigma}{\nu N^2},
```

the corresponding selector charge satisfies

```math
\boxed{
\int_{I_{\rm bd}}\Lambda(t)^2\,dt
\ge
\frac{c_M}{\nu}.
}
```

This covers all effective shear parameters \(\rho\le M\).

## 8. Large-\(\rho\) critical mixing

For large `\rho`, apply the protected L5-26 critical theorem to the exact
normalized shear equation.

Set

```math
h_\rho=\rho^{-1/3}.
```

On one fixed critical interval the normalized carrier has positive Fourier
mass at

```math
|n|
\asymp
h_\rho^{-1}
=
\rho^{1/3}.
```

One coefficient has magnitude at least

```math
c h_\rho^{1/2}.
```

Restoring the physical carrier amplitude \(A\), one LP block at

```math
\lambda_p
\asymp
N\rho^{1/3}
```

satisfies

```math
\lambda_p^{-1}\|u_p\|_\infty
\ge
c
\frac{A}{N}
\rho^{-1/2}
=
c\nu
\frac{R}{\sqrt\rho}.
```

Since

```math
\rho=R\delta\le R,
```

one has

```math
\frac{R}{\sqrt\rho}
\ge
\sqrt R.
```

Hence the block is threshold violating for all sufficiently large `R`.

The selector lower bound is

```math
\Lambda
\ge
cN\rho^{1/3}.
```

The critical physical time element is

```math
dt
=
\frac{\rho^{-2/3}}{\nu N^2}\,ds.
```

Therefore

```math
\boxed{
\int_{I_{\rm crit}}
\Lambda(t)^2\,dt
\ge
\frac c\nu.
}
```

Choose one fixed \(M\) sufficiently large for the protected L5-26 asymptotic
lower bound to hold for every \(\rho\ge M\).

## 9. Combined charge theorem

The bounded-\(\rho\) and large-\(\rho\) regimes cover every \(\rho>0\).

Let

```math
R_j\to\infty,
\qquad
0<\delta_j\le1,
\qquad
\rho_j=R_j\delta_j.
```

If

```math
\boxed{
R_j\rho_j
=
R_j^2\delta_j
\to\infty,
}
```

then for all sufficiently large \(j\) there is a physical interval \(I_j\)
such that

```math
\boxed{
\int_{I_j}
\Lambda_j(t)^2\,dt
\ge
\frac{c_*}{\nu},
}
```

where \(c_*>0\) is independent of \(j\).

This is the exact secondary-shear charge theorem.

## 10. Power-law interpretation

Suppose

```math
\delta_R
=
R^{-a}.
```

Then

```math
R^2\delta_R
=
R^{2-a}.
```

Therefore every exponent

```math
a<2
```

lies in the charged regime.

In particular, the L5-29 NF4 corridor scale

```math
\delta_R
=
R^{-2/3}
```

has

```math
R^2\delta_R
=
R^{4/3}\to\infty.
```

Thus a channel small enough to be ignored as an \(O(h^2)\) residual at the
**primary** critical scale can still generate its own nonvanishing charge on
its **secondary** mixing scale.

The calibration theorem leaves unresolved only the scale

```math
\delta_R
=
O(R^{-2})
```

up to constants.

This is a sufficient-condition statement, not a claim that every
\(\delta=O(R^{-2})\) trajectory avoids charge.

## 11. Meaning for the bridge programme

The result changes how nonprincipal interactions should be treated.

A nonprincipal channel need not be made \(R^{-2/3}\)-small merely so that one
principal bridge survives.

If that channel has coherent shear structure, it may be promoted to a
secondary principal bridge with its own effective Reynolds number.

This suggests a multi-channel decomposition:

```text
large coherent channel
    -> promote to principal mixing channel

tiny channel
    -> retain in residual

incoherent channel
    -> must be charged by a different dynamic mechanism
```

The exact calibration handles the first case.

## 12. Relation to L5-29

L5-29 proves only a pointwise symbol statement.

L5-30 supplies an actual unforced NSE trajectory for the one-parameter
subfamily

```math
\alpha=\pi/2,
\qquad
\cos\beta=\delta.
```

It therefore converts persistent non-null polarization into a genuine
time-correlated mixing result.

The proof does not say that a generic whole-space interaction with the same
instantaneous symbol remains a coherent shear channel.

That coherence is the next whole-space obligation.

## 13. Next live obligation: C2-MIX-MULTICHANNEL

The smallest safe successor is:

> Can a selected whole-space active packet be decomposed into finitely many
> coherent transport channels plus a residual, so that every channel with
> \(R^2\delta\gg1\) pays a \(c/\nu\) selector charge and the remainder is below
> the critical residual scale?

The first audit should determine whether a frequency/polarization
decomposition can identify such secondary channels without assuming temporal
coherence.

If coherence itself must be assumed, isolate the exact persistence norm and do
not call the decomposition automatic.

## 14. Hard rejection tests

Reject any successor that:

- treats every instantaneous L5-29 interaction as a coherent secondary shear;
- imports the periodic 2.5D trajectory into the selected whole-space theorem;
- assumes a nonprincipal channel persists for parabolic time;
- interprets \(\delta=O(R^{-2})\) as proved charge-free;
- adds charges from overlapping channels without disjointness or another
  justified ledger;
- differentiates the moving selector.

## 15. Claim boundary

The protected claim sought from this tranche is exactly

```text
EXACT_SECONDARY_SHEAR_CHARGE_PROVED
__R_SQUARED_DELTA_DIVERGENCE_FORCES_C_OVER_NU.
```

It proves, for an exact smooth unforced periodic 2.5D NSE polarization
subfamily:

- the L5-29 defect \(\delta\) is an exact secondary shear amplitude fraction;
- the effective shear Reynolds number is \(\rho=R\delta\);
- bounded-\(\rho\) Duhamel generation produces a neighboring coefficient
  \(c\rho A\);
- large-\(\rho\) critical mixing is governed by protected L5-26;
- \(R^2\delta\to\infty\) forces a selector-charge lower bound \(c_*/\nu\);
- the unresolved calibration regime is narrowed to
  \(R^2\delta=O(1)\).

It does not prove coherent secondary-channel extraction for selected
whole-space solutions.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.

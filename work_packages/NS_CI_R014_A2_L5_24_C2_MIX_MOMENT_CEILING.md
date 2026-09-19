# NS-CI-R014-A2-L5-24 — shear-chain mixing-diffusion moment ceiling

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base: `d4d2e218ab9d42726f27de1b368531159f628dc4`
- Protected predecessor: `NS-CI-R014-A2-L5-23`
- Result:
  `SHEAR_CHAIN_R_ONE_THIRD_MOMENT_CEILING_PROVED__SUBCUBIC_TURNOVER_SELECTOR_CHARGE_VANISHES`
- A2 theorem: open
- L5: active
- C2-MIX: upper-reach side proved in the exact shear calibration
- MATHCERT adjudication: absent
- Evidence class: exact theorem for the smooth unforced periodic 2.5D shear
  calibration protected in L5-23; not the selected whole-space A2 class

L5-23 leaves amplitude transport versus viscosity as the live calibration
question. The exact shear chain admits an all-time Sobolev-moment barrier that
identifies a cubic-root mixing scale without importing inviscid Bessel lower
bounds.

For every fixed integer `s>=0`,

```math
\sup_{\tau>=0}
\|\partial_Y^s\phi_\varepsilon(\tau)\|_2
\le
C_s\varepsilon^{-s/3},
\qquad
0<\varepsilon\le1.
```

Here `\phi_\varepsilon` is the exact complex vertical shear-chain solution
after factoring the fixed `e^{iX}` mode.

The campaign LP threshold then gives, for normalized shell scale
`L_p=\lambda_p/N`,

```math
\lambda_p^{-1}\|u_p\|_\infty
\le
C_s\nu
\varepsilon^{-(1+s/3)}
L_p^{-(s+1/2)}.
```

Therefore every threshold-violating shell satisfies

```math
\frac{\lambda_p}{N}
\le
C_s R^{\alpha_s},
\qquad
\alpha_s
=
\frac{1+s/3}{s+1/2}
=
\frac13+\frac5{6s+3}.
```

In particular, `s=5` gives

```math
\alpha_5=\frac{16}{33}<\frac12.
```

Hence the exact shear calibration cannot have threshold reach of order
`sqrt(R)`. More strongly, for every fixed `\delta>0`,

```math
\Lambda(t)
\le
C_\delta N R^{1/3+\delta}
```

for all time in this calibration.

On a turnover window `0<=\tau<=T_R` this implies

```math
\int\Lambda(t)^2\,dt
\le
\frac{C_\delta}{\nu}
T_R R^{-1/3+2\delta}.
```

Thus for every `\eta>0`, all windows

```math
T_R
\le
R^{1/3-\eta}
```

have vanishing selector charge as `R\to\infty` after choosing
`\delta<\eta/2`.

This does not prove a lower bound at the cubic-root window. It proves that
subcubic turnover windows are too short to produce order-one A2 charge in this
exact calibration. The next live question is therefore a finite-viscosity
lower-amplitude theorem on the growing `tau~R^{1/3}` scale.

## 1. Exact scalar equation from L5-23

Retain the exact L5-23 shear calibration. After factoring the fixed
`e^{iX}` Fourier mode, write

```math
\phi_\varepsilon(\tau,Y)
=
\sum_{n\in\mathbb Z}a_n(\tau)e^{inY}.
```

Then

```math
\boxed{
\partial_\tau\phi_\varepsilon
+
i e^{-\varepsilon\tau}\cos Y\,\phi_\varepsilon
=
\varepsilon
(\partial_Y^2-1)
\phi_\varepsilon,
}
```

with

```math
\phi_\varepsilon(0,Y)=1.
```

The Fourier chain is exactly

```math
a_n'
=
-\frac i2 e^{-\varepsilon\tau}
(a_{n-1}+a_{n+1})
-
\varepsilon(1+n^2)a_n.
```

No truncation is used.

## 2. Zeroth-order energy

Set

```math
X_s(\tau)
=
\|\partial_Y^s\phi_\varepsilon(\tau)\|_2^2.
```

Because multiplication by
`i e^{-\varepsilon\tau}\cos Y` is skew-adjoint,

```math
\frac12 X_0'
+
\varepsilon X_1
+
\varepsilon X_0
=
0.
```

Hence

```math
\boxed{
X_0(\tau)\le X_0(0)
}
```

for every `\tau>=0`.

Normalize the torus measure so that `X_0(0)=1`.

## 3. Differentiated energy inequality

For integer `s>=1`, differentiate the equation `s` times in `Y`.

The principal multiplication term remains skew-adjoint. Only the commutator

```math
[\partial_Y^s,\cos Y]\phi_\varepsilon
```

contributes to the real energy identity.

Since every derivative of `\cos Y` is bounded,

```math
\big\|
[\partial_Y^s,\cos Y]\phi_\varepsilon
\big\|_2
\le
C_s
\sum_{r=0}^{s-1}
\|\partial_Y^r\phi_\varepsilon\|_2.
```

Therefore

```math
\boxed{
\frac12X_s'
+
\varepsilon X_{s+1}
+
\varepsilon X_s
\le
C_s
X_s^{1/2}
\sum_{r=0}^{s-1}X_r^{1/2}.
}
```

The factor `e^{-\varepsilon\tau}` is at most one and causes no loss.

## 4. Fourier interpolation

By Hölder on the Fourier sequence,

```math
X_s
=
\sum_n |n|^{2s}|a_n|^2
\le
X_0^{1/(s+1)}
X_{s+1}^{s/(s+1)}.
```

Using `X_0<=1`,

```math
\boxed{
X_{s+1}
\ge
X_s^{1+1/s}.
}
```

This is the nonlinear damping term that closes the moment barrier.

## 5. Inductive cubic-root moment barrier

We prove by induction on `s` that

```math
\boxed{
X_s(\tau)
\le
B_s\varepsilon^{-2s/3}
}
```

for every `\tau>=0`, with `B_s` independent of
`\varepsilon\in(0,1]`.

The case `s=0` was proved above.

Assume the result for all `r<s`. Since `\varepsilon<=1`,

```math
\sum_{r=0}^{s-1}X_r^{1/2}
\le
C_s
\varepsilon^{-(s-1)/3}.
```

The differentiated energy inequality and interpolation give

```math
X_s'
\le
C_s
\varepsilon^{-(s-1)/3}
X_s^{1/2}
-
c_s\varepsilon
X_s^{1+1/s}.
```

At the barrier

```math
X_s
=
B_s\varepsilon^{-2s/3},
```

the positive term has scale

```math
B_s^{1/2}
\varepsilon^{-(2s-1)/3},
```

while the negative term has scale

```math
B_s^{1+1/s}
\varepsilon^{-(2s-1)/3}.
```

Choose `B_s` large enough that the negative term dominates at the first
possible barrier crossing.

Since `X_s(0)=0` for `s>=1`, no crossing occurs. Thus

```math
\boxed{
\sup_{\tau>=0}
\|\partial_Y^s\phi_\varepsilon(\tau)\|_2
\le
C_s\varepsilon^{-s/3}.
}
```

The exponent `1/3` comes from exact balance between one derivative of shear
production and two derivatives of viscous damping.

## 6. Convert moments to dyadic L-infinity tails

Let

```math
L_p=\frac{\lambda_p}{N}.
```

For all sufficiently large `L_p`, the horizontal shear mode is absent from
the block. The vertical Fourier support in that shell has fixed
`X`-index `+/-1` and `Y`-indices satisfying

```math
|n|\asymp L_p.
```

A fixed-width two-dimensional LP annulus therefore intersects this one-chain
support in only

```math
O(L_p)
```

Fourier modes.

Cauchy--Schwarz and the moment bound give

```math
\|\Delta_p u\|_\infty
\le
C A
L_p^{1/2}
\left(
\sum_{|n|\asymp L_p}
|a_n|^2
\right)^{1/2}
```

and hence

```math
\boxed{
\|\Delta_p u\|_\infty
\le
C_s A
\varepsilon^{-s/3}
L_p^{1/2-s}.
}
```

This is uniform in turnover time.

## 7. Threshold-reaching exponent

Use

```math
A=R\nu N,
\qquad
R=\varepsilon^{-1},
\qquad
\lambda_p=NL_p.
```

Then

```math
\boxed{
\lambda_p^{-1}
\|\Delta_pu\|_\infty
\le
C_s\nu
\varepsilon^{-(1+s/3)}
L_p^{-(s+1/2)}.
}
```

Thus every sufficiently high shell satisfying

```math
L_p
>
K_s
\varepsilon^{-\alpha_s},
```

with

```math
\boxed{
\alpha_s
=
\frac{1+s/3}{s+1/2}
=
\frac{2(s+3)}{3(2s+1)}
=
\frac13+\frac5{6s+3},
}
```

is strict-high throughout the whole evolution.

By the dissipation-index definition,

```math
\boxed{
\Lambda(t)
\le
C_s
N R^{\alpha_s}.
}
```

No selector continuity is assumed.

## 8. Explicit square-root separation

At `s=5`,

```math
\alpha_5
=
\frac{16}{33}.
```

Since

```math
\frac{16}{33}
<
\frac12,
```

every threshold-violating shell in this exact calibration lies below

```math
C N R^{16/33}.
```

Therefore `sqrt(R)` threshold reach is excluded.

This conclusion is independent of the L5-20 cellular-flow argument. It comes
from the exact shear-chain mixing/diffusion moment balance.

## 9. Arbitrarily close to cubic-root reach

Because

```math
\alpha_s
=
\frac13+\frac5{6s+3},
```

for every fixed `\delta>0` one may choose a finite integer `s` such that

```math
\alpha_s
<
\frac13+\delta.
```

Then

```math
\boxed{
\Lambda(t)
\le
C_\delta
N R^{1/3+\delta}
}
```

for all time.

This is an upper reach theorem. It does not assert the existence of
threshold-sized modes near `R^{1/3}`.

## 10. Selector charge on a growing turnover window

Physical time and turnover time satisfy

```math
dt
=
\frac{d\tau}{AN}
=
\frac{d\tau}{R\nu N^2}.
```

Therefore, on any normalized interval

```math
0\le\tau\le T_R,
```

the selector bound gives

```math
\int_0^{T_R/(AN)}
\Lambda(t)^2\,dt
\le
\frac{C_\delta}{\nu}
T_R
R^{-1/3+2\delta}.
```

Hence, for every fixed `\eta>0`, choose `\delta<\eta/2`. If

```math
T_R
\le
R^{1/3-\eta},
```

then

```math
\boxed{
\int_0^{T_R/(AN)}
\Lambda(t)^2\,dt
\longrightarrow
0
}
```

as `R\to\infty`.

In particular every fixed turnover-time window has vanishing selector charge.

## 11. Meaning of the cubic-root window

The result identifies a precise new calibration boundary.

Subcubic turnover windows

```math
\tau
\ll
R^{1/3}
```

cannot generate order-one A2 charge through threshold propagation in the exact
shear chain.

This does not prove that the `R^{1/3}` window does generate such charge.
The upper estimate alone cannot distinguish among:

- genuine threshold-sized propagation to the moment ceiling;
- early amplitude depletion;
- enhanced dissipation before threshold reach;
- concentration of energy below the ceiling.

Thus the next theorem must be a lower-amplitude or decay theorem at a growing
turnover scale.

## 12. Relation to the inviscid Bessel chain

L5-23 records

```math
a_n(\tau)=(-i)^nJ_n(\tau)
```

when `\varepsilon=0`.

Those amplitudes suggest ballistic chain transport in the inviscid problem,
but they are not used in this proof.

The present theorem is fully finite-viscosity and all-time.

In particular, it does not replace

```math
a_n^\varepsilon(\tau)
```

by

```math
(-i)^nJ_n(\tau)
```

on a growing `\tau`-window.

That replacement remains unauthorized until a uniform growing-window
remainder estimate is proved.

## 13. Next live obligation: C2-MIX-LOWER

The smallest safe successor is now:

> On a turnover window of order `R^{1/3}`, can one prove a finite-viscosity
> lower bound for amplitudes at chain index of order `R^{1/3}`, or instead
> prove that viscous/enhanced dissipation suppresses them before the campaign
> threshold is reached?

A useful positive result must control finite-`\varepsilon` amplitudes on the
growing window. Candidate tools include:

- Duhamel comparison with the inviscid Bessel propagator with an explicit
  growing-window remainder;
- a Feynman--Kac representation for the one-dimensional complex potential;
- hypocoercive/enhanced-dissipation estimates specialized to the exact cosine
  shear;
- weighted-chain energy estimates localized near the moving front.

The result must distinguish amplitude damping from phase decoherence, which
L5-23 already excludes.

## 14. Hard rejection tests

Reject any successor that:

- treats the `R^{1/3}` upper ceiling as a lower propagation theorem;
- imports the inviscid Bessel profile at growing time without a finite-
  viscosity error bound;
- infers selector violation from nonzero support;
- ignores the `\varepsilon n^2` diagonal near growing chain index;
- treats this periodic 2.5D theorem as the selected whole-space result;
- assumes selector continuity;
- reopens L3 from turnover residence;
- reopens L4 from generic signed conservation.

## 15. Claim boundary

The protected claim sought from this tranche is exactly

```text
SHEAR_CHAIN_R_ONE_THIRD_MOMENT_CEILING_PROVED
__SUBCUBIC_TURNOVER_SELECTOR_CHARGE_VANISHES.
```

It proves, in the exact L5-23 shear calibration:

- all-time derivative moments
  `\|\partial_Y^s\phi_\varepsilon\|_2<=C_sR^{s/3}`;
- threshold reach
  `\Lambda<=C_sNR^{\alpha_s}` with
  `\alpha_s=1/3+5/(6s+3)`;
- explicit `s=5` reach exponent `16/33<1/2`;
- arbitrary `R^{1/3+\delta}` selector upper reach;
- vanishing selector charge on every turnover window
  `T_R<=R^{1/3-\eta}`.

It does not prove A2.

It does not prove threshold-sized amplitude at the cubic-root front.

It does not prove enhanced-dissipation decay.

It does not prove the selected whole-space result.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.

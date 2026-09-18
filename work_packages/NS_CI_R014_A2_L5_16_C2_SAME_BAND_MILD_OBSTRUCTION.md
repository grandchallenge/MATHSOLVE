# NS-CI-R014-A2-L5-16 — same-band projected forcing and the mild-route obstruction

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base: `ac3796ad1a96b734616ad304c577de05668ca3e0`
- Predecessor: `NS-CI-R014-A2-L5-15`
- Result:
  `SAME_BAND_LERAY_FORCING_ATTAINS_LAMBDA_A_SQUARED__ABSOLUTE_MILD_ROUTE_STOPS_AT_TURNOVER_SCALE`
- A2 theorem: open
- L5: active
- C2-OVR-DYN: active, narrowed again
- MATHCERT adjudication: absent
- Evidence class: exact Fourier-algebra fixture plus route reduction;
  not an NSE trajectory and not a whole-space counterexample

L5-15 isolated the continuation-relevant residual

```math
\Omega(t)
=
\sup_{\lfloor 4Q/5\rfloor<p\le Q}
\lambda_p
\big(
\|u_p\|_\infty-c_0\nu\lambda_p
\big)_+.
```

It also proved that a full nonlinear-turnover residence time is too weak to
make `Omega` integrable from A2 and the Leray scalar budgets.

The first C2-OVR-DYN question is therefore whether the fixed-shell NSE mild
formula itself forces a longer, parabolic-scale residence time for a large
upper-band overshoot.

This tranche gives a negative answer for the **bare absolute-forcing route**.

The reason is exact: incompressibility, Leray projection, and localization to
one fixed-width frequency band do not reduce the nonlinear forcing below the
usual

```math
\lambda A^2
```

scale.

At overshoot ratio

```math
R
=
\frac{A}{\nu\lambda},
```

that scale is `R` times the representative viscous scale
`nu lambda^2 A`.  Therefore an absolute mild estimate controls amplitude
variation only on the nonlinear-turnover interval

```math
(\lambda A)^{-1}
=
(R\nu\lambda^2)^{-1},
```

not on the longer parabolic interval `(nu lambda^2)^-1`.

No statement is made that an NSE overshoot actually decays on turnover time.
The result is a proof-route obstruction: any improvement must use additional
dynamic depletion, cancellation, or coherence that is absent from the bare
pointwise algebra.

## 1. Protected predecessor

L5-15 gives

```math
f(t)
\lesssim
(U_0+c_0\nu)\Lambda(t)^2
+
\Omega(t).
```

Hence A2 reduces continuation to

```math
\Omega\in L^1_t.
```

The exact turnover fixture in L5-15 then shows

```text
A2 + Leray scalar budgets + turnover-time residence
do not force
Omega in L1.
```

Accordingly, a persistence-based reopening has to beat the turnover scale.

The most direct possible source of such a gain would be a fixed-shell mild
estimate in which viscosity dominates the nonlinear forcing of a large
overshoot for a parabolic amount of time.

The calculation below rules out obtaining that dominance from
incompressibility, Leray projection, and finite-band support alone.

## 2. Exact same-band divergence-free fixture

Work first with an exact trigonometric Fourier-algebra fixture.

This is used only to test the NSE bilinear symbol.  It is not asserted to be a
Leray--Hopf trajectory in the selected whole-space class.

Let

```math
k_1=(N,0,0),
\qquad
k_2=(0,N,0),
```

and choose polarizations

```math
a=(0,1,1),
\qquad
b=(1,0,1).
```

Then

```math
k_1\cdot a=0,
\qquad
k_2\cdot b=0.
```

Define

```math
u(x)
=
A a\cos(Nx_1)
+
A b\cos(Nx_2).
```

Therefore

```math
\nabla\cdot u=0.
```

The two input frequencies have magnitude `N`.

Their sum is

```math
k_3
=
k_1+k_2
=
(N,N,0),
```

with

```math
|k_3|
=
\sqrt2 N.
```

Thus all three frequencies lie in one factor-two frequency band.  In a smooth
Littlewood--Paley decomposition this is a single fixed-width annular
interaction up to the usual harmless overlap of neighboring projectors.

## 3. Exact projected nonlinear interaction

Write

```math
x=Nx_1,
\qquad
y=Nx_2.
```

The vector field is

```math
u
=
A(
\cos y,
\cos x,
\cos x+\cos y
).
```

Since there is no `x_3` dependence,

```math
(u\cdot\nabla)u
=
u_1\partial_1u
+
u_2\partial_2u.
```

A direct calculation gives

```math
(u\cdot\nabla)u
=
-A^2N
\begin{pmatrix}
\cos x\sin y\\
\cos y\sin x\\
\cos y\sin x+\cos x\sin y
\end{pmatrix}.
```

The coefficient of the target phase

```math
\sin(x+y)
```

is therefore

```math
-A^2N
\begin{pmatrix}
1/2\\
1/2\\
1
\end{pmatrix}.
```

At `k_3=(N,N,0)`, the Leray projector is

```math
\mathbb P_{k_3}
=
I
-
\frac{k_3\otimes k_3}{|k_3|^2}.
```

Applying it to the coefficient above removes exactly the horizontal component:

```math
\mathbb P_{k_3}
\begin{pmatrix}
1/2\\
1/2\\
1
\end{pmatrix}
=
\begin{pmatrix}
0\\
0\\
1
\end{pmatrix}.
```

Hence the target projected interaction is exactly

```math
\boxed{
\mathbb P_{k_3}(u\cdot\nabla u)_{k_3}
=
-A^2N e_3\sin(Nx_1+Nx_2).
}
```

In particular, its physical mode amplitude is

```math
\boxed{
A^2N.
}
```

There is no cancellation of the derivative factor and no small factor from
incompressibility or Leray projection.

## 4. Consequence for the generic band forcing scale

Let `lambda` denote a representative frequency of this fixed-width band.
Here

```math
\lambda\simeq N.
```

The exact fixture realizes

```math
\|P_\lambda\mathbb P(u\cdot\nabla u)\|_\infty
\gtrsim
\lambda A^2
```

at the Fourier-symbol level.

Therefore no pointwise algebraic argument based only on

- divergence freedom;
- Leray projection;
- all interacting frequencies lying in one fixed-width band; and
- a band amplitude scale `A`

can replace the nonlinear scale `lambda A^2` by a uniformly viscous-sized
quantity

```math
C\nu\lambda^2A
```

for arbitrarily large

```math
R
=
\frac{A}{\nu\lambda}.
```

Indeed,

```math
\frac{\lambda A^2}
{\nu\lambda^2A}
=
R.
```

For the exact target frequency `|k_3|=sqrt(2)N`, the corresponding ratio to
`nu |k_3|^2 A` differs only by the fixed factor `1/2`.

The obstruction is therefore scale-robust.

## 5. Bare mild estimate

A frequency-localized mild formula has the schematic form

```math
u_p(t+h)
=
e^{-\nu h\lambda_p^2}u_p(t)
-
\int_t^{t+h}
e^{-\nu(t+h-s)\lambda_p^2}
P_p\mathbb P\nabla\cdot(u\otimes u)(s)
\,ds.
```

Suppose a proof treats the nonlinear term absolutely and has only the generic
band estimate

```math
\|P_p\mathbb P\nabla\cdot(u\otimes u)\|_\infty
\lesssim
\lambda_p A^2
```

during an overshoot episode whose relevant shell amplitude is `A`.

Then the nonlinear contribution over a time interval of length `h` is at
best bounded by

```math
C h\lambda_pA^2.
```

To guarantee that this contribution is only a fixed fraction of `A`, one
must impose

```math
h
\lesssim
\frac{1}{\lambda_pA}.
```

This is the nonlinear turnover scale.

## 6. Overshoot normalization

Write

```math
A
=
R\nu\lambda_p.
```

Then

```math
\boxed{
(\lambda_pA)^{-1}
=
(R\nu\lambda_p^2)^{-1}.
}
```

The parabolic scale is

```math
(\nu\lambda_p^2)^{-1}.
```

Therefore

```math
\boxed{
\frac{
(\lambda_pA)^{-1}
}{
(\nu\lambda_p^2)^{-1}
}
=
\frac1R.
}
```

For a large overshoot, the turnover interval is shorter than the parabolic
interval by the full factor `R`.

Equivalently, over one parabolic interval, the absolute nonlinear forcing
scale permits a change of size

```math
\lambda_pA^2
\cdot
\frac{1}{\nu\lambda_p^2}
=
R A.
```

Thus a parabolic persistence conclusion cannot follow from this absolute bound
uniformly in large `R`.

## 7. Relation to L5-15

L5-15 showed that even if each overshoot episode persists for the full
turnover time

```math
(R\nu\lambda^2)^{-1},
```

the A2 charge per excursion can still be only

```math
R^{-1},
```

while the `Omega` charge remains order one.

Therefore the present result and L5-15 compose exactly:

```text
bare fixed-shell absolute mild estimate
          |
          v
turnover-scale persistence only
          |
          v
insufficient against A2 scalar budgets.
```

This closes the bare fixed-shell absolute-mild persistence route.

## 8. What the fixture does not prove

The exact field in Section 2 is not claimed to be an NSE trajectory.

The result does not prove that a large overshoot must change on turnover time.

It does not prove that a real Leray--Hopf solution realizes the displayed
triad coherently for an interval.

It does not exclude a parabolic residence theorem obtained from additional
dynamic information.

In particular, the calculation does not address possible:

- time-integrated cancellation;
- depletion of the same-band interaction along actual solutions;
- phase decoherence among active modes;
- cross-shell conservation constraints;
- geometric depletion of the nonlinear term;
- signed flux information;
- coherence forced by the moving dissipation scale.

Those are precisely the kinds of ingredients that remain admissible.

## 9. Reopening requirement after L5-16

After this tranche, a persistence proof cannot merely write the mild formula
and apply an absolute bilinear estimate.

A genuine reopening must establish at least one additional statement of the
form

```math
\int_I
\|P_p\mathbb P\nabla\cdot(u\otimes u)\|_\infty
\,dt
\ll
\int_I
\lambda_p A(t)^2
\,dt
```

on large overshoot episodes, or an equivalent signed/coherent law.

Examples include:

1. **same-band dynamic depletion**:
   the projected interaction is smaller than `lambda A^2` by a
   non-summable function of the overshoot ratio;

2. **parabolic coherence**:
   a large overshoot forces correlated activity over a parabolic interval,
   not merely a turnover interval;

3. **cross-level cost**:
   rapid change of the active shell forces comparable energy or dissipation
   into neighboring strict-high shells, creating a non-summable A2 cost;

4. **signed time-correlated flux control**:
   cancellation over the episode directly controls the integral of
   `Omega`.

Without one of these additions, the mild route returns to the closed
turnover-scale boundary.

## 10. Next live obligation: C2-COH

The preferred next tranche is no longer another residence estimate from an
absolute forcing bound.

The next question is:

> Does an actual large upper-band overshoot force time-correlated same-band or
> neighboring-band structure that depletes the projected nonlinear forcing,
> or charges rapid overshoot variation to a non-summable cross-level budget?

A useful first audit is to pair the exact shell energy identity with the
upper-fifth overshoot decomposition and ask whether a rapid change of
`Omega` necessarily creates either:

- a signed flux event of comparable size; or
- strict-high activity that contradicts the defining dissipation threshold
  unless it is short in a quantitatively stronger sense than turnover time.

If the estimate collapses back to the protected L4 weighted column, the old
L3 exit charge, or an unsigned absolute forcing bound, record that reduction
and do not reopen those lanes.

## 11. Hard rejection tests

Reject any successor that:

- treats the trigonometric fixture as an NSE trajectory;
- imports periodic dynamics into the selected whole-space theorem class;
- claims the nonlinear term always has size `lambda A^2`;
- claims actual overshoots necessarily decay on turnover time;
- uses strict-high control at `p=Q`;
- derives parabolic residence from the bare absolute mild bound without an
  additional depletion/coherence estimate;
- reopens L3 using only the already-separated turnover residence scale;
- reopens L4 through the unsigned active diagonal.

## 12. Claim boundary

The protected claim sought from this tranche is exactly

```text
SAME_BAND_LERAY_FORCING_ATTAINS_LAMBDA_A_SQUARED
__ABSOLUTE_MILD_ROUTE_STOPS_AT_TURNOVER_SCALE.
```

It proves a sharp algebraic obstruction for the bare fixed-shell
absolute-forcing route.

It does not prove A2.

It does not prove or disprove a dynamic parabolic residence theorem.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.

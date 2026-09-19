# NS-CI-R014-A2-L5-17 — instantaneous cross-level coherence audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base: `c3b933c2a5ded75733d33d1f56c4633141c10ac0`
- Predecessor: `NS-CI-R014-A2-L5-16`
- Result:
  `SAME_BAND_NSE_RHS_ALLOWS_TURNOVER_RATE_WITH_STRICT_HIGH_INPUT_EMPTY__INSTANTANEOUS_CROSS_LEVEL_REPAIR_BLOCKED`
- A2 theorem: open
- L5: active
- C2-COH: active, narrowed to time-correlated coherence
- MATHCERT adjudication: absent
- Evidence class: exact Fourier-algebra snapshot of the NSE right-hand side;
  not a selected whole-space trajectory or counterexample

L5-16 closed the bare fixed-shell absolute-mild persistence route.  The next
possible repair was cross-level coherence: perhaps a rapid change of a large
upper-band overshoot must force activity into strict-high shells, where the
dissipation-wavenumber definition supplies a smallness threshold.

This tranche shows that no such implication is available **instantaneously**
from the NSE Fourier algebra.

A large active target mode can have a turnover-size time derivative generated
entirely by modes at or below the target frequency while every strict-high
input mode is zero.  Reversing one source phase flips the nonlinear target
contribution without changing Fourier support or modal energies.

Therefore any useful cross-level theorem must be time-correlated.  It must
show that sustained or repeated active-band variation eventually creates
strict-high cost, depletion, or signed coherence.  A pointwise-in-time
algebraic implication is false.

## 1. Protected inputs

L5-15 isolated

```math
\Omega(t)
=
\sup_{\lfloor4Q/5\rfloor<p\le Q}
\lambda_p
\big(
\|u_p\|_\infty-c_0\nu\lambda_p
\big)_+,
```

and proved

```math
f(t)
\lesssim
(U_0+c_0\nu)\Lambda(t)^2
+
\Omega(t).
```

L5-16 then showed that same-band projected forcing can attain the full scale

```math
\lambda A^2,
```

so an absolute fixed-shell mild estimate only gives the nonlinear-turnover
time

```math
(R\nu\lambda^2)^{-1}
```

for overshoot ratio `R=A/(nu lambda)`.

Since L5-15 already separated turnover residence as insufficient, the first
remaining repair was:

> perhaps fast active-shell variation must excite strict-high modes.

The present calculation tests exactly that pointwise implication.

## 2. Three-mode active-band snapshot

Let

```math
k_1=(N,0,0),
\qquad
k_2=(0,N,0),
\qquad
k_3=(N,N,0).
```

Choose divergence-free polarizations

```math
a=(0,1,1),
\qquad
b=(1,0,1),
\qquad
e_3=(0,0,1).
```

Indeed,

```math
k_1\cdot a
=
k_2\cdot b
=
k_3\cdot e_3
=
0.
```

For a phase sign `sigma in {+1,-1}`, define

```math
u_\sigma(x)
=
A a\cos(Nx_1)
+
\sigma A b\cos(Nx_2)
+
C e_3\sin(Nx_1+Nx_2).
```

All initial Fourier support is contained in the three frequency pairs

```math
\pm k_1,
\qquad
\pm k_2,
\qquad
\pm k_3.
```

The source frequencies have magnitude `N`; the target has magnitude

```math
K
=
|k_3|
=
\sqrt2 N.
```

Thus there is no input Fourier frequency above the target frequency.

In a smooth Littlewood--Paley decomposition the three modes occupy one fixed
neighboring annular cluster.  If the target shell is the active threshold
shell, all sufficiently higher shells are exactly zero in this algebraic
snapshot.

No claim is made that this finite periodic field is itself a solution in the
selected whole-space class.  It is used to test a proposed instantaneous
Fourier-algebra implication.

## 3. Target coefficient of the nonlinear term

L5-16 already computed the source-source interaction for `sigma=+1`.

With the phase sign retained, the coefficient of the target phase

```math
\sin(Nx_1+Nx_2)
```

in the projected convection term is

```math
\boxed{
\mathbb P(u_\sigma\cdot\nabla u_\sigma)_{k_3}
=
-\sigma A^2N e_3.
}
```

Adding the target mode `C e_3 sin(Nx_1+Nx_2)` does not change this target
coefficient.

The reason is elementary:

- the target mode has only an `e_3` velocity component;
- there is no `x_3` dependence;
- target-source products generate phases `k_3 plus/minus k_1` and
  `k_3 plus/minus k_2`, not `k_3` itself;
- target self-advection vanishes.

Hence the target nonlinear coefficient remains exactly the source-source
coefficient above.

## 4. Exact NSE right-hand-side coefficient

For unforced NSE,

```math
\partial_t u
+
\mathbb P(u\cdot\nabla u)
=
\nu\Delta u.
```

The target coefficient therefore obeys, at this snapshot,

```math
\dot C
=
-\nu K^2 C
+
\sigma A^2N.
```

Since `K^2=2N^2`,

```math
\boxed{
\dot C
=
-2\nu N^2 C
+
\sigma A^2N.
}
```

This formula uses no strict-high input.

## 5. Large overshoot normalization

Set

```math
A=C=R\nu N.
```

The target threshold ratio is

```math
\frac{C}{\nu K}
=
\frac{R}{\sqrt2}.
```

Thus for any fixed threshold constant `c_0`, the target is a large
threshold overshoot once `R` is sufficiently large.

The exact target derivative becomes

```math
\boxed{
\dot C
=
\nu^2N^3
\big(
-2R+\sigma R^2
\big).
}
```

Dividing by `C=R nu N` gives

```math
\boxed{
\frac{\dot C}{C}
=
\nu N^2
\big(
-2+\sigma R
\big).
}
```

For `R>=4`:

- with `sigma=+1`,
  ```math
  \dot C/C
  =
  (R-2)\nu N^2
  \ge
  (R/2)\nu N^2;
  ```
- with `sigma=-1`,
  ```math
  \dot C/C
  =
  -(R+2)\nu N^2.
  ```

Therefore the target coefficient can have either growth or decay at a rate of
order

```math
R\nu N^2,
```

which is the nonlinear-turnover rate up to the fixed annular constants.

## 6. Strict-high input remains empty

At the same instant, the Fourier support contains no mode above `K=sqrt(2)N`.

Thus the calculation realizes simultaneously:

```text
large active target overshoot;
turnover-size target derivative;
zero strict-high input support.
```

Moreover, changing `sigma` from `+1` to `-1`:

- preserves the frequency support;
- preserves all three modal amplitudes and modal energies;
- preserves the target overshoot;
- preserves the absence of strict-high input;
- reverses the nonlinear contribution to the target derivative.

Hence neither the **magnitude** nor the **sign** of instantaneous target
variation forces strict-high activity from the Fourier algebra alone.

## 7. Consequence for the cross-level repair

The following pointwise implication is therefore unavailable:

```text
large/rapid upper-band overshoot variation
    =>
strict-high activity at the same instant.
```

This does not close every cross-level mechanism.

It closes only an instantaneous algebraic repair in which the strict-high
threshold is expected to be charged directly by the current target derivative.

The active band can internally redistribute amplitude at the full turnover
rate before any time-correlated consequence is considered.

## 8. Relation to the selector

The selected dissipation wavenumber controls shells strictly above `Q`.

The present fixture is compatible with the key orientation of that definition:

- the target mode can violate the threshold;
- all modes above the target frequency are initially zero;
- the source modes are below the target and are not required to satisfy the
  strict-high smallness condition.

Thus one cannot use the strict-high condition as an instantaneous bound on
the source-source interaction driving the target shell.

This is the same logical reason that strict-high may not be applied at
`p=Q`, now made explicit at the level of an active-band dynamical
coefficient.

## 9. What remains live

The result does **not** show that strict-high modes stay zero under evolution.

Indeed, the same nonlinear dynamics can generate additional frequencies at
later times.

That observation is precisely the remaining opportunity.

A viable C2-COH theorem must be genuinely time-correlated, for example:

1. **delayed strict-high charge**:
   repeated or sustained turnover-size variation forces enough activity above
   the moving threshold to create a non-summable A2 cost;

2. **active-band phase decoherence**:
   the phase relations required for repeated full-size internal transfer
   cannot persist on too many turnover intervals without depletion;

3. **signed cumulative flux**:
   the time integral of internal active-band transfer has cancellation or
   telescoping unavailable pointwise;

4. **cross-level cascade coherence**:
   repeated large overshoots at increasing threshold levels cannot be
   independent because the newly generated neighboring frequencies have to be
   transported through the selector.

These are temporal statements.  None follows from the instantaneous fixture.

## 10. Relation to closed lanes

This tranche does not reopen L3.

The old inverse-frequency exit charge and turnover residence remain
insufficient.

It does not reopen L4.

No unsigned active-diagonal estimate or weighted positive column is claimed.

It also does not repeat the L5-13 sign fixture.  L5-13 showed no universal sign
for a localized energy-flux expression.  L5-17 addresses a different proposed
repair: whether rapid active-shell amplitude variation itself forces
strict-high input.  The answer is no at one instant.

## 11. Next live obligation: C2-TIME

The smallest safe successor is now:

> Can repeated same-band turnover-size forcing remain coherent over a sequence
> of overshoot episodes without creating a time-integrated strict-high,
> dissipation, or signed-flux cost that is non-summable under A2?

The first useful calculation should retain a fixed target shell over a short
time window and split the nonlinear Duhamel term into:

- internal active-band interactions;
- interactions involving strict-high modes;
- already-controlled far-low interactions.

The goal is not another pointwise estimate.  It is to identify a
time-integrated quantity that cannot repeatedly saturate the same-band
`lambda A^2` scale while keeping the strict-high/dissipation charge summable.

If that reduction returns only:

- the L3 inverse-frequency exit charge;
- turnover-time residence;
- the L4 active diagonal;
- selector variation without a new bound; or
- an unsigned absolute forcing estimate,

record the exact reduction and do not reopen those routes.

## 12. Hard rejection tests

Reject any successor that:

- treats this periodic Fourier snapshot as a selected whole-space trajectory;
- concludes strict-high modes remain empty for positive time;
- applies strict-high smallness at the target shell;
- infers a sign from modal energy or support alone;
- uses the phase-reversal fixture as a global NSE counterexample;
- repeats the absolute `lambda A^2` mild estimate as a new mechanism;
- calls turnover residence a reopening of L3;
- calls the unsigned active diagonal a reopening of L4.

## 13. Claim boundary

The protected claim sought from this tranche is exactly

```text
SAME_BAND_NSE_RHS_ALLOWS_TURNOVER_RATE_WITH_STRICT_HIGH_INPUT_EMPTY
__INSTANTANEOUS_CROSS_LEVEL_REPAIR_BLOCKED.
```

It proves an instantaneous Fourier-algebra obstruction to one cross-level
repair.

It does not prove A2.

It does not exclude delayed or time-integrated cross-level coherence.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.

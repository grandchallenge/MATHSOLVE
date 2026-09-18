# NS-CI-R014-A2-L5-15 — C2 overshoot and persistence audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor: `ab8dccfdb861086a7d6137e92494bd3e82eec102`
- Exact replay base after unrelated protected-main drift: `3bd2a2722df603143f832c0da5b18983213e8ced`
- Predecessor: `NS-CI-R014-A2-L5-14`
- Result:
  `A2_LOW_COEFFICIENT_BELOW_FOUR_FIFTH_CONTROLLED__RESIDUAL_IS_UPPER_FIFTH_THRESHOLD_OVERSHOOT__TURNOVER_TIME_PERSISTENCE_INSUFFICIENT`
- A2 theorem: open
- L5: active
- C2-DYN: active, narrowed
- MATHCERT adjudication: absent
- Evidence class: exact analytic reduction plus algebraic/scaling excursion
  separator; not an NSE counterexample

This tranche starts the equation-facing C2-DYN audit after L5-14.

It proves two positive reductions and one negative persistence result.

First, the protected low-mode continuation coefficient is already A2-integrable
for every shell below the relative cutoff `4Q/5`.

Second, after subtracting the defining threshold scale in the remaining upper
fifth, the whole continuation problem reduces to one scalar overshoot
functional.

Third, even granting each large overshoot excursion a lifetime comparable to
its natural nonlinear turnover time is still insufficient: the present A2,
energy, and Leray dissipation budgets permit infinitely many order-one
overshoot charges at that timescale.

Thus the next dynamic theorem must give a stronger scale cost than ordinary
turnover-time persistence, or else provide cross-excursion/signed coherence.

## 1. Protected inputs

Write

```math
a_p(t)=\|u_p(t)\|_\infty,
\qquad
\Lambda(t)=\lambda_{Q(t)},
```

and retain the protected low-mode coefficient

```math
f(t)
=
\sup_{p\le Q(t)}
\lambda_p a_p(t).
```

The campaign already has the continuation implication

```text
f in L1_t  =>  regular continuation.
```

The selected A2 hypothesis is

```math
\int_0^T\Lambda(t)^2dt<\infty.
```

The dissipation-index definition gives strict-high control only for `p>Q`.
At the active threshold shell there is instead the lower relation

```math
a_Q\ge c_0\nu\Lambda.
```

No threshold upper bound at `Q` is available.

L5-14 showed that the packet quantity below `2Q/3` is automatically
A2-integrable.  The present tranche asks a different question: how much of the
actual continuation coefficient `f` is already A2 controlled before any new
dynamic theorem is invoked?

## 2. Four-fifths reduction for the continuation coefficient

For `Q\ge5`, define

```math
R_Q
=
\left\lfloor\frac{4Q}{5}\right\rfloor.
```

Split

```math
f
=
\max\{f_{\mathrm{far}},f_{\mathrm{upper}}\},
```

where

```math
f_{\mathrm{far}}
=
\sup_{p\le R_Q}\lambda_pa_p,
qquad
f_{\mathrm{upper}}
=
\sup_{R_Q<p\le Q}\lambda_pa_p.
```

The finitely many small values of `Q` are harmless.

### Lemma 2.1 — lower four-fifths are already A2 controlled

Bernstein and the energy supremum give, shell by shell,

```math
a_p
\lesssim
\lambda_p^{3/2}\|u_p\|_2
\lesssim
U_0\lambda_p^{3/2}.
```

Hence

```math
\lambda_pa_p
\lesssim
U_0\lambda_p^{5/2}.
```

For `p\le R_Q`,

```math
\lambda_p^{5/2}
\le
\lambda_{R_Q}^{5/2}.
```

Since

```math
5R_Q\le4Q,
```

one has exactly

```math
\lambda_{R_Q}^{5/2}
=
2^{5R_Q/2}
\le
2^{2Q}
=
\Lambda^2.
```

Therefore

```math
\boxed{
f_{\mathrm{far}}(t)
\lesssim
U_0\Lambda(t)^2.
}
```

In particular,

```math
\int_0^T f_{\mathrm{far}}(t)dt<\infty
```

under A2.

The same calculation, using the geometric shell sum, also gives

```math
\sum_{p\le R_Q}\lambda_pa_p
\lesssim
U_0\Lambda^2.
```

Thus the low-deformation contribution from the lower four-fifths of the active
logarithmic range is A2-integrable as well.  This does not close the standard
direct-L6 route because the upper band remains.

### Criticality of four-fifths for this energy-only argument

At a general relative cutoff `p\le\alpha Q`, the same estimate gives

```math
f_{\le\alpha Q}
\lesssim
U_0\Lambda^{5\alpha/2}.
```

A2 controls this directly precisely when

```math
\frac{5\alpha}{2}\le2.
```

Hence

```math
\boxed{
\alpha\le\frac45.
}
```

The value `4/5` is therefore the largest relative cutoff reachable by this
plain energy-plus-Bernstein estimate for `f`.

This is distinct from the L5-14 packet cutoff `2/3`: the packet sum and the
continuation coefficient have different Bernstein powers.

## 3. Threshold overshoot functional

For the upper relative band define

```math
b_p(t)
=
\big(a_p(t)-c_0\nu\lambda_p\big)_+,
```

and

```math
\boxed{
\Omega(t)
=
\sup_{R_Q<p\le Q}
\lambda_pb_p(t).
}
```

This does not assert strict-high control for any `p\le Q`.  It is merely the
exact positive-part decomposition

```math
a_p
\le
c_0\nu\lambda_p+b_p.
```

Therefore, for `R_Q<p\le Q`,

```math
\lambda_pa_p
\le
c_0\nu\lambda_p^2+\lambda_pb_p
\le
c_0\nu\Lambda^2+\Omega.
```

Combining with Lemma 2.1 gives

```math
\boxed{
f(t)
\lesssim
(U_0+c_0\nu)\Lambda(t)^2
+
\Omega(t).
}
```

### Corollary 3.1 — overshoot criterion

Under A2,

```math
\Omega\in L^1(0,T)
```

is sufficient for regular continuation.

A terminal-local version is sufficient as usual.

### Corollary 3.2 — necessary overshoot signature of any A2 singularity

If a solution satisfying A2 were singular at `T`, then for every
`\delta>0`,

```math
\boxed{
\int_{T-\delta}^{T}\Omega(t)dt=\infty.
}
```

Again, this is a necessary condition only.  It does not assert that such a
trajectory exists.

## 4. Relation to the L5-14 packet target

Let

```math
S_{\mathrm{upper}}
=
\sum_{R_Q<p\le Q}a_p^2.
```

Pointwise,

```math
\Omega
\le
\sup_{R_Q<p\le Q}\lambda_pa_p
\le
\Lambda S_{\mathrm{upper}}^{1/2}.
```

Hence

```math
\int\Omega
\le
\left(\int\Lambda^2\right)^{1/2}
\left(\int S_{\mathrm{upper}}\right)^{1/2}.
```

Thus the L5-14 packet theorem would automatically imply the L5-15 overshoot
criterion.

The converse is not assumed.  The purpose of `Omega` is to isolate a smaller
continuation-relevant object on which a dynamic persistence or coherence
argument can focus.

## 5. Why threshold logic alone does not control the overshoot

The defining threshold gives a fixed amplitude scale

```math
c_0\nu\lambda_p.
```

It does not bound the positive excess for `p\le Q`.

The active shell itself may satisfy

```math
a_Q
\gg
\nu\Lambda.
```

Ordinary Bernstein only gives

```math
a_Q^2
\lesssim
\Lambda^3\|u_Q\|_2^2,
```

which is compatible with arbitrarily large normalized overshoot as
`Lambda\to\infty`.

Therefore a proof of `Omega in L1` has to use equation dynamics, not the
selector definition alone.

## 6. Turnover-time persistence is still insufficient

A natural first dynamic hope is:

> a shell whose amplitude overshoots the viscous threshold by a factor `R`
> cannot disappear on a time shorter than its nonlinear turnover scale
> `(lambda a)^{-1}`.

The next exact scaling fixture shows that **even granting that residence scale**
does not close A2.

This fixture is not an NSE solution.  It tests the strength of the proposed
scale cost against the protected scalar budgets.

Take `nu=1` and any fixed `0<c_0<1`.  Let

```math
R_n=2^n,
\qquad
\lambda_n=R_n^4,
```

and use one active shell on a disjoint interval `I_n` with

```math
a_n
=
R_n\lambda_n,
```

```math
E_n
=
\|u_n\|_2^2
=
\frac{R_n^2}{\lambda_n}
=
R_n^{-2},
```

and

```math
|I_n|
=
\frac{1}{R_n\lambda_n^2}.
```

The shell saturates the Bernstein scaling exactly:

```math
a_n^2
=
\lambda_n^3E_n.
```

The normalized threshold ratio is

```math
\frac{a_n}{\lambda_n}=R_n\to\infty,
```

so it is an arbitrarily large active-shell overshoot.

The interval length is precisely

```math
|I_n|
=
(\lambda_na_n)^{-1},
```

the nonlinear turnover time.

### 6.1 A2 charge

With `Q=n` interpreted at the selected shell scale,

```math
\lambda_n^2|I_n|
=
\frac1{R_n}.
```

Therefore

```math
\sum_n\lambda_n^2|I_n|
=
\sum_n2^{-n}
<\infty.
```

### 6.2 Energy and dissipation charges

The energy levels satisfy

```math
E_n=R_n^{-2},
```

so the energy supremum is bounded.

The shell dissipation charge is

```math
\lambda_n^2E_n|I_n|
=
\frac{R_n}{\lambda_n}
=
R_n^{-3}.
```

Hence

```math
\sum_n\lambda_n^2E_n|I_n|<\infty.
```

### 6.3 Overshoot charge

The overshoot functional on `I_n` is

```math
\Omega_n
=
\lambda_n(a_n-c_0\lambda_n)
=
(R_n-c_0)\lambda_n^2.
```

Therefore

```math
\Omega_n|I_n|
=
1-\frac{c_0}{R_n}.
```

Thus

```math
\boxed{
\sum_n\Omega_n|I_n|
=
\infty.
}
```

The current scalar budgets are therefore compatible with infinitely many
large overshoot excursions, each lasting a full nonlinear turnover time, while
the total A2 and dissipation charges remain finite.

## 7. Meaning of the persistence separator

The fixture does **not** prove that NSE can realize such excursions.

It proves a narrower statement:

```text
TURNOVER-TIME RESIDENCE + A2 + LERAY SCALAR BUDGETS
DO NOT FORCE
Omega in L1.
```

The reason is exact.  At overshoot ratio `R`,

```math
\text{A2 charge per turnover excursion}
\asymp
R^{-1},
```

while

```math
\text{Omega charge per excursion}
\asymp
1.
```

Large overshoots can therefore make the A2 cost summable without reducing the
overshoot charge.

A persistence theorem at the parabolic scale

```math
\lambda^{-2}
```

would be qualitatively different: its A2 charge per excursion would be order
one, independent of `R`.  Proving such a lower residence time for large
overshoots would be a genuine L3 reopening theorem.

Other possible repairs are:

1. an overshoot-dependent residence cost whose A2 charge does not decay
   summably in `R`;
2. cross-excursion coherence preventing independent arbitrarily large
   overshoots;
3. signed flux cancellation that controls the time integral of `Omega`
   without a residence lower bound;
4. a PDE-derived active-volume lower bound suppressing Bernstein saturation
   before the overshoot ratio becomes arbitrarily large.

## 8. Direct relation to the old low-strain blocker

The standard direct-L6 audit produced the low-deformation coefficient

```math
G_Q
=
\|\nabla u_{\le Q-2}\|_\infty
```

up to harmless LP constants.

L5-15 changes that state in one precise way.  The portion generated by

```math
p\le\frac45Q
```

is already A2-integrable.

The only possible nonintegrable low-strain contribution lies in the relative
upper fifth.

If one estimates that remaining band absolutely, the relevant sum is

```math
\sum_{4Q/5<p\le Q}
\lambda_p
\big(a_p-c_0\nu\lambda_p\big)_+,
```

which is stronger than the supremum `Omega` needed by the protected
low-mode continuation criterion.

Therefore this tranche does not reopen the already-closed standard absolute
direct-L6 route.  It instead identifies the weaker continuation-relevant
overshoot functional as the preferred dynamic target.

## 9. Field-development cross-check

Cheskidov--Peng (2026) define intermittency through saturation of Bernstein's
inequality and use time-averaged dissipation to control a determining
wavenumber on the periodic forced problem.

Cheskidov--Shvydkoy's dissipation-wavenumber programme likewise separates
viscous high modes from the low modes and proves regularity from an integrable
low-mode coefficient.

The present reduction is compatible with both mechanisms but imports neither
as an A2 theorem.

Its new content is campaign-specific:

```text
A2 controls the continuation coefficient below relative frequency 4Q/5;
only upper-fifth threshold overshoot remains.
```

## 10. Next live obligation: C2-OVR-DYN

Do not seek a global intermittency dimension or a pointwise bound on every
`chi_q`.

The first live dynamic question is now:

> Can NSE evolution force a non-summable A2 cost, parabolic-scale residence,
> cross-level coherence, or signed depletion whenever `Omega` becomes large?

The most discriminating first audit is a fixed-shell mild/energy analysis of a
large overshoot episode, keeping its ratio

```math
R
=
\frac{a_p}{\nu\lambda_p}
```

explicit.

A successful theorem must beat the scalar cost

```math
\Lambda^2\Delta t
\sim
R^{-1}
```

associated with ordinary turnover-time residence.

If the fixed-shell Duhamel estimate yields only a turnover-scale lifetime,
record the exact reduction and do not reopen L3.

If it yields parabolic residence, a non-summable scale cost, or coherent
coupling across successive active shells, that satisfies the protected L3
reopening requirement and should be pursued immediately.

## 11. Hard rejection tests

Reject any successor that:

- assumes `Omega in L1` or bounded overshoot;
- uses strict-high at `p=Q`;
- treats a nonlinear-turnover residence bound as sufficient after Section 6;
- differentiates the moving `4Q/5` cutoff without selector control;
- replaces the residual by the closed unsigned `lambda_QD_Q` column;
- imports periodic/forced intermittency conclusions into the selected
  whole-space unforced class;
- treats the excursion fixture as an NSE trajectory;
- introduces constants depending on a terminal frequency cutoff.

## 12. Claim boundary

The protected result sought from this tranche is exactly

```text
A2_LOW_COEFFICIENT_BELOW_FOUR_FIFTH_CONTROLLED
__RESIDUAL_IS_UPPER_FIFTH_THRESHOLD_OVERSHOOT
__TURNOVER_TIME_PERSISTENCE_INSUFFICIENT.
```

It does not prove A2.

It does not prove any overshoot residence theorem for NSE.

It does not reopen L3 or L4.

It proves the `4/5` A2 reduction, the exact overshoot continuation criterion,
and the insufficiency of turnover-time residence against the current scalar
budgets.

No MATHCERT, novelty, priority, or publication claim is asserted.

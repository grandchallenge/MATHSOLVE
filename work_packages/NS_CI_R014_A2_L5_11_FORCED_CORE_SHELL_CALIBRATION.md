# NS-CI-R014-A2-L5-11 — Forced core-shell Littlewood--Paley calibration

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base: `5b31fda9c4836454d957c4cb9e8ed8cfdb72cf0b`
- Predecessor: `NS-CI-R014-A2-L5-10`
- Result: `FORCED_CORE_SHELL_LP_LOWER_BOUND_PROVED__CALIBRATION_FORCES_LAMBDA_NOT_L2`
- A2 theorem: open
- L5: active
- MATHCERT adjudication: absent
- Evidence category: theorem about a different forcing class, used only as calibration for the selected unforced A2 observable

This package executes C1 from
`work_packages/NS_CI_R014_A2_L5_10_FIELD_CALIBRATION_FREQUENCY_SCALE_HANDOFF.md`.
It proves the missing Littlewood--Paley shell lower bound for the explicit September 2026
forced singular construction.  It does **not** convert that construction into an unforced
solution and does **not** falsify or prove A2.

## 1. Sources and fixed conventions

The singular construction is:

OpenAI, *Finite Time Blowup for Navier--Stokes*, released 8 September 2026.

- announcement: `https://openai.com/index/navier-stokes-solution/`
- paper: `https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf`

The paper constructs, for every `nu>0`, a smooth solution on `[0,1)` with zero initial
velocity and a smooth compactly supported external force.  The velocity has uniformly
bounded kinetic energy and becomes unbounded as `t -> 1`.

The campaign uses the fixed inhomogeneous Cheskidov--Shvydkoy Littlewood--Paley
partition:

```math
lambda_p=2^p,
\qquad
u_p=\Delta_p u,
```

with a fixed low ball and fixed smooth annuli for `p>=0`.  Its dissipation index is

```math
Q(t)=\min\left\{q\ge0:
  \lambda_p^{-1}\|u_p(t)\|_\infty<c_0\nu
  \text{ for every }p>q
\right\},
\qquad
\Lambda(t)=\lambda_{Q(t)}.
```

Only the ordinary smooth dyadic-partition properties are used below: the annular kernels
are Schwartz, have zero mean, are obtained from one fixed kernel by dyadic dilation, and
telescope with the associated low-pass operators.  No terminal-frequency-dependent
constant is introduced.

## 2. Source scales and the normalized core profile

Write

```math
\tau=1-t,
\qquad
A=\frac12+h,
\qquad
D=\frac12-h,
\qquad
0<h<\frac1{100}.
```

For viscosity one, the source similarity variables satisfy

```math
z=q^D\eta,
\qquad
\tau=q(1-\eta^2),
\qquad
X=\frac{r^2}{2q}.
```

The leading azimuthal component is

```math
u_\theta^{(0)}=q^{-A}E_0(X,\eta).
```

The paper proves that `E_0(X,eta)/sqrt(2X)` is smooth at the axis, that
`E_0(X,eta)>0` for `X>0` in the inner profile, and that for some fixed
`X_in in (0,X_a)`

```math
u_\theta(\sqrt{2X_{in}\tau},0,0,1-\tau)
=
\tau^{-A}\left(e_0+O(\tau^{2h})\right),
\qquad e_0=E_0(X_{in},0)>0.
```

At this inner point all annular wave/mean corrections vanish.  More generally, on every
fixed set in the isotropically rescaled variables `y=x/sqrt(tau)`, the source construction
has the following consequence.

### Lemma 2.1 — isotropic-core profile limit

Let `u` denote the viscosity-one whole-space field constructed in the paper and define

```math
U_\tau(y)=\tau^A u(\sqrt\tau\,y,1-\tau).
```

There is a bounded smooth vector field `V(y_h)`, independent of `y_3`, such that

```math
U_\tau \longrightarrow V
```

locally uniformly on `R^3` as `tau -> 0`.  For the second Cartesian component,

```math
V_2(0,0)=0,
\qquad
V_2(\sqrt{2X_{in}},0)=e_0>0.
```

Moreover

```math
\sup_{0<\tau<\tau_0}\|U_\tau\|_\infty<\infty
```

for some `tau_0>0`.

#### Proof

Fix bounded `y=(y_h,y_3)` and put `x=sqrt(tau)y`.  Since

```math
z=\sqrt\tau\,y_3=q^D\eta,
\qquad
\tau=q(1-\eta^2),
```

one has uniformly on bounded `y`

```math
\eta=O(\tau^h),
\qquad
q=\tau(1+O(\tau^{2h})),
\qquad
X=\frac{|y_h|^2}{2}+O(\tau^{2h}).
```

The leading azimuthal and axial fields therefore converge after multiplication by
`tau^A` to their fixed profiles at `eta=0`.  The leading radial velocity is only
`O(tau^{-1/2})`, so its `tau^A` normalization is `O(tau^h)` and vanishes.

The background correction hierarchy is in positive powers `q^{2h}`.  The cumulative wave
and mean corrections of Proposition 9.4/9.9 have positive normalized orders (in particular
the velocity wave correction is in `W_{1/2}` and the listed mean corrections have still
higher positive order).  Because `epsilon=q^h`, these corrections tend to zero in normalized
amplitude on each fixed rescaled compact set.  The summation cutoffs preserve those bounds.
The final localization cutoffs equal one near `(0,1)`, hence on each fixed rescaled compact
set for all sufficiently small `tau`.

On the positive `x_1` axis the second Cartesian component is exactly the azimuthal
component.  Smoothness at the axis gives zero azimuthal velocity there, while the displayed
inner asymptotic gives the value `e_0` at `y_h=(sqrt(2X_in),0)`.  Thus the limiting second
component is nonconstant.

For the global normalized bound, note first that `q>=tau`.  Every background and corrected
velocity term in the active similarity region has physical velocity factor at worst `q^{-A}`
times a uniformly bounded normalized coefficient (positive powers of `q^h`, including the
logarithmic factors in the correction classes, remain bounded as `q -> 0`).  Hence those
terms are `O(tau^{-A})`.  In the exact exterior, Theorem 3.1 gives

```math
K(r,\tau)=r^{-1-2h}H_{ext}(\tau/r^2)
```

with bounded `H_ext`; the exterior condition `X>=X_ext` implies `r>=c sqrt(tau)`, so
`|K|<=C tau^{-A}`.  Finally, cutoff-transition terms stay away from `(0,1)` and are uniformly
bounded by the endpoint regularity part of Theorem 3.1.  This proves the global bound. `square`

The key point is that the isotropic radial scale `sqrt(tau)` sees the much longer axial
scale `tau^D` as asymptotically constant: `eta=O(tau^h)`.  Thus the three-dimensional
Littlewood--Paley operator at radial core frequency has a well-defined nonconstant limiting
profile to detect.

## 3. A uniform finite-shell capture lemma

Let `Delta_p` be any annular block of the fixed campaign partition, and write its kernel as

```math
K_p(x)=\lambda_p^3 K(\lambda_p x),
```

where `K` is Schwartz and has zero integral.  Let `T_b` denote the same annular convolution
at continuous frequency parameter `b>0`:

```math
T_bF(y)=\int b^3K(b(y-w))F(w)\,dw.
```

### Lemma 3.1 — dyadic-phase-uniform capture

For the limiting scalar profile `V_2` in Lemma 2.1 there are a finite set of integer offsets
`J`, and constants `c_*>0`, `tau_*>0`, such that the following holds.

For every `0<tau<tau_*`, choose an integer `p_0(tau)` with

```math
1\le \lambda_{p_0}\sqrt\tau<2.
```

Then for at least one `j in J`,

```math
\|\Delta_{p_0+j}u(1-\tau)\|_\infty
\ge c_*\tau^{-A}.
```

#### Proof

Set

```math
y_0=0,
\qquad
y_1=(\sqrt{2X_{in}},0,0),
\qquad
d=V_2(y_1)-V_2(y_0)=e_0>0.
```

For `a in [1,2]`, the shifted dyadic family `T_{a2^j}` telescopes with its low-pass
operators.  Hence the difference `d` is the sum over `j in Z` of

```math
T_{a2^j}V_2(y_1)-T_{a2^j}V_2(y_0).
```

The two tails are uniform in `a`.

For low frequencies `b=a2^j -> 0`, differentiating the convolution kernel gives

```math
|T_bV_2(y_1)-T_bV_2(y_0)|
\le C|y_1-y_0|\,b\,\|V_2\|_\infty.
```

For high frequencies `b -> infinity`, zero mean and smoothness give

```math
\|T_bV_2\|_\infty
\le Cb^{-1}\|\nabla V_2\|_\infty.
```

Both tails are geometric.  Choose `M` so that their total contribution for `|j|>M` is less
than `d/2`, uniformly for `a in [1,2]`, and put

```math
J=\{-M,\ldots,M\}.
```

Then some `j in J` has

```math
|T_{a2^j}V_2(y_1)-T_{a2^j}V_2(y_0)|
\ge \frac{d}{2|J|}.
```

Now set `a_tau=lambda_{p_0}sqrt(tau)`.  Rescaling the physical convolution gives exactly

```math
\tau^A
(\Delta_{p_0+j}u)_2(\sqrt\tau\,y,1-\tau)
=
T_{a_\tau2^j}(U_\tau)_2(y).
```

For the finitely many `j in J`, the parameters `a_tau 2^j` remain in one compact subset of
`(0,infinity)`.  Lemma 2.1 gives local uniform convergence `U_tau -> V` and a global uniform
`L^infinity` bound.  Uniform Schwartz tails of this compact kernel family therefore imply,
by splitting each convolution into a fixed ball and its complement,

```math
T_{a_\tau2^j}(U_\tau)_2(y_i)
-
T_{a_\tau2^j}V_2(y_i)
\longrightarrow0
```

uniformly over `j in J`, `i in {0,1}`, and the dyadic phase `a_tau in [1,2]`.
For sufficiently small `tau`, the preceding finite-shell difference remains at least
`d/(4|J|)`.  At least one of its two endpoint values has magnitude at least
`d/(8|J|)`.  Taking the spatial supremum proves the claim with a fixed `c_*>0`. `square`

This finite-offset statement is stronger than a subsequential shell observation.  It holds
for every sufficiently late time and is uniform in the unavoidable phase between the
continuous core frequency and the discrete dyadic lattice.

## 4. Viscosity-rescaled shell theorem

The paper passes from viscosity one to arbitrary fixed `nu>0` by

```math
u_\nu(x,t)=\sqrt\nu\,u(x/\sqrt\nu,t).
```

Therefore the normalized rescaling

```math
\frac{\tau^A}{\sqrt\nu}
 u_\nu(\sqrt{\nu\tau}\,y,1-\tau)
```

is exactly `U_tau(y)`.  Repeating Lemma 3.1 with the physical core length
`sqrt(nu tau)` proves the main calibration theorem.

### Theorem 4.1 — core-shell Littlewood--Paley lower bound

For each fixed `nu>0` there exist `c,C,tau_0>0` and a finite integer set `J`, independent
of `tau`, such that for every `0<tau<tau_0` there is an annular shell `p=p(tau)` satisfying

```math
c(\nu\tau)^{-1/2}
\le \lambda_p
\le C(\nu\tau)^{-1/2}
```

and

```math
\|u_{\nu,p}(1-\tau)\|_\infty
\ge c\sqrt\nu\,\tau^{-1/2-h}.
```

All constants may depend on the fixed construction, `nu`, and the fixed campaign partition,
but not on `tau` or a terminal frequency cutoff.

## 5. Consequences for the campaign observables

For the shell in Theorem 4.1,

```math
\lambda_p^{-1}\|u_{\nu,p}\|_\infty
\ge c\nu\tau^{-h}.
```

Since `h>0`, for every fixed threshold constant `c_0` this eventually exceeds `c_0 nu`.
Thus the campaign strict-high inequality fails at this shell.  By the exact minimality
property in the definition of `Q`, the shell cannot lie above `Q(1-tau)`.  Hence

```math
p(\tau)\le Q(1-\tau)
```

for all sufficiently small `tau`, and therefore

```math
\boxed{
\Lambda_\nu(1-\tau)
\ge c(\nu\tau)^{-1/2}.
}
```

It follows immediately that

```math
\int_{1-\delta}^1\Lambda_\nu(t)^2\,dt
\ge
\frac{c}{\nu}\int_0^\delta\frac{d\tau}{\tau}
=\infty.
```

So the explicit forced singular solution lies outside the A2 hypothesis
`Lambda in L^2_t`.

The same shell belongs to the low/active packet, so the established observables also obey

```math
f(1-\tau)
\ge
\lambda_p\|u_{\nu,p}\|_\infty
\ge c\tau^{-1-h},
```

and

```math
S_1(1-\tau)
\ge
\|u_{\nu,p}\|_\infty^2
\ge c\nu\tau^{-1-2h}.
```

Consequently

```math
\int_{1-\delta}^1 f(t)\,dt=\infty,
\qquad
\int_{1-\delta}^1 S_1(t)\,dt=\infty.
```

Since `Lambda(t)->infinity` along the terminal interval by the displayed lower bound, for
every finite `R` there is a smaller `delta_R>0` for which

```math
(1-\delta_R,1)\subset\{t:\Lambda(t)>R\},
```

and hence

```math
\int_{\{\Lambda>R\}}S_1(t)\,dt=\infty.
```

This is a calibration result of the intended kind: the L5-10 high-`Lambda` packet-tail
successor rejects the explicit forced singularity for a theorem-grade frequency reason,
not merely by similarity-scale intuition.

No lower bound for `W_{<=Q}` or `Z_{>Q}` is asserted here.  An `L^infinity` shell lower
bound does not by itself supply the spatial-volume information needed for an `L^2` shell
lower bound.

## 6. What was actually gained

Before this tranche, the statement

```math
\Lambda(t)\gtrsim(1-t)^{-1/2}
```

for the forced construction was only a calibration conjecture because pointwise velocity
growth does not automatically imply a dyadic shell lower bound.  The missing step is now
supplied by the dyadic-phase-uniform capture lemma:

1. the construction yields a nonconstant normalized radial-core profile;
2. low normalized frequencies cannot reproduce its fixed core-scale difference;
3. arbitrarily high normalized frequencies contribute a summable tail because the limiting
   profile is smooth;
4. therefore one shell from a fixed finite offset set must retain a fixed fraction of the
   normalized amplitude;
5. the source correction hierarchy converges to the leading profile strongly enough for
   that finite-shell statement to persist in the exact whole-space field.

The argument uses the actual construction and the actual campaign selector.  It does not
assume the shell lower bound that it is meant to prove.

## 7. Claim boundary

The force in the OpenAI construction is nonzero, smooth, and compactly supported.  The
selected A2 theorem is an unforced whole-space Leray--Hopf criterion.  Therefore:

```text
THIS RESULT DOES NOT FALSIFY A2.
```

What is proved is narrower and useful:

```text
FOR THE EXPLICIT FORCED SINGULAR CONSTRUCTION,
A CORE-SCALE LITTLEWOOD--PALEY SHELL VIOLATES THE STRICT-HIGH THRESHOLD
AT EVERY SUFFICIENTLY LATE TIME, SO LAMBDA IS NOT IN L2_t.
```

This is evidence category 4 in the L5-10 handoff: theorem-grade calibration on the explicit
forced singular construction.  It is not a PDE theorem for the selected unforced A2 class,
not MATHCERT certification, and not a novelty or priority claim.

## 8. Successor

C1 is closed positively.  The next live tranche is C3 from L5-10: retain dyadic frequency
`q` and backward physical scale `k` as independent indices in a localized energy/pressure
estimate and seek a two-sided summable kernel in `q-k`.  The scale `k` must not be bound to
`Q(t)` until after the gain is established.

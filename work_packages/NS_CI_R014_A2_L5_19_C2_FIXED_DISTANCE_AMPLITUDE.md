# NS-CI-R014-A2-L5-19 — fixed-distance threshold leakage in the exact 2.5D calibration

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected base: `762e560dc5b9c234461f311aabf403fbec7d4691`
- Protected predecessor: `NS-CI-R014-A2-L5-18`
- Result:
  `FIXED_DISTANCE_THRESHOLD_LEAKAGE_PROVED_IN_2P5D_CALIBRATION__FIXED_DISTANCE_CHARGE_CERTIFICATE_REMAINS_R_INVERSE`
- A2 theorem: open
- L5: active
- C2-AMP: advanced, not closed
- MATHCERT adjudication: absent
- Evidence class: exact theorem in the same smooth unforced periodic 2.5D
  calibration used by L5-18; not the selected whole-space A2 class

L5-18 proved nonzero temporal leakage at every fixed finite lattice distance,
but stopped before a finite-time amplitude lower bound.

This tranche closes that missing calibration step.

For every fixed sufficiently separated lattice distance `r_*`, depending
only on the fixed Littlewood--Paley annulus width, there is a fixed
dimensionless turnover-time interval on which the generated Fourier
coefficient stays uniformly nonzero as the overshoot ratio `R` tends to
infinity.  Since the physical amplitude scale is `A=R nu N`, the generated
mode eventually violates the campaign threshold in a dyadic shell that did
not meet the initial Fourier support.

Thus **threshold-sized temporal leakage is real in the exact 2.5D
calibration**, not merely support leakage.

However, the selector-charge certificate obtained from any one fixed spectral
distance over a fixed turnover-time interval scales only like

```math
\frac{C_{r_*}}{R\nu}.
```

Therefore fixed-distance leakage alone retains the inverse-overshoot
summability defect already exposed by L5-15.  The next question is no longer
whether threshold leakage occurs, but how far in frequency threshold-sized
leakage can propagate as a function of `R`, or whether another cumulative
flux/decoherence cost replaces that distance growth.

## 1. L5-18 calibration

Use the exact periodic 2.5D solution from L5-18:

```math
v(t,x_1,x_2)
=
A e^{-\nu N^2t}
\big(
\cos(Nx_2),
\cos(Nx_1)
\big),
```

and

```math
\partial_t w+v\cdot\nabla w
=
\nu\Delta w,
```

with

```math
w(0)
=
A\cos(Nx_1)
+
A\cos(Nx_2)
+
A\sin(Nx_1+Nx_2).
```

The choice `C=A` is the large-overshoot calibration relevant below.

Then

```math
u=(v_1,v_2,w)
```

is an exact smooth unforced periodic Navier--Stokes solution.

This remains a calibration theorem only.  The selected A2 target is
whole-space and is not changed by this tranche.

## 2. Turnover scaling

Set

```math
X=Nx_1,
\qquad
Y=Nx_2,
\qquad
\tau=ANt,
```

and normalize

```math
w(t,x)=A\theta_\varepsilon(\tau,X,Y).
```

Define the overshoot ratio

```math
R
=
\frac{A}{\nu N},
qquad
\varepsilon
=
\frac{\nu N}{A}
=
\frac1R.
```

The vertical equation becomes

```math
\partial_\tau\theta_\varepsilon
+
e^{-\varepsilon\tau}
V\cdot\nabla\theta_\varepsilon
=
\varepsilon\Delta\theta_\varepsilon,
```

where

```math
V(X,Y)
=
(\cos Y,\cos X),
```

and

```math
\theta_\varepsilon(0)
=
\cos X+\cos Y+\sin(X+Y).
```

Thus the large-overshoot limit `R to infinity` is the regular
small-diffusivity limit

```math
\varepsilon\to0.
```

The limiting equation is the smooth transport problem

```math
\partial_\tau\theta_0
+
V\cdot\nabla\theta_0
=
0.
```

## 3. Uniform finite-time convergence to the transport limit

Fix a finite dimensionless horizon `T>0` and an integer Sobolev order
`s>=4`.

Because `V` is smooth and divergence free, standard commutator energy
estimates for

```math
\partial_\tau\theta_\varepsilon
+
e^{-\varepsilon\tau}V\cdot\nabla\theta_\varepsilon
=
\varepsilon\Delta\theta_\varepsilon
```

give

```math
\sup_{0\le\tau\le T}
\|\theta_\varepsilon(\tau)\|_{H^{s+2}}
\le
C_{s,T},
```

uniformly for `0 <= epsilon <= 1`.

Let

```math
z_\varepsilon
=
\theta_\varepsilon-\theta_0.
```

Then

```math
\partial_\tau z_\varepsilon
+
V\cdot\nabla z_\varepsilon
=
(1-e^{-\varepsilon\tau})
V\cdot\nabla\theta_\varepsilon
+
\varepsilon\Delta\theta_\varepsilon.
```

The transport term is skew in `L^2`.  Using

```math
0
\le
1-e^{-\varepsilon\tau}
\le
\varepsilon\tau
```

and the uniform Sobolev bound gives

```math
\frac{d}{d\tau}
\|z_\varepsilon(\tau)\|_2
\le
C_T\varepsilon.
```

Since `z_\varepsilon(0)=0`,

```math
\boxed{
\sup_{0\le\tau\le T}
\|\theta_\varepsilon(\tau)-\theta_0(\tau)\|_2
\le
C_T\varepsilon.
}
```

Every individual Fourier coefficient therefore converges uniformly on
`[0,T]` at rate `O(1/R)`.

This is the finite-time remainder control missing from L5-18.

## 4. A fixed generated mode has a nonzero transport coefficient

For each integer `r>=1`, let

```math
k_r=(r+1,1).
```

L5-18 proved that the normalized Fourier coefficient
`\widehat\theta_{0,k_r}` satisfies

```math
\frac{d^j}{d\tau^j}
\widehat\theta_{0,k_r}(0)
=
0,
\qquad
0\le j<r,
```

and

```math
\boxed{
\frac{d^r}{d\tau^r}
\widehat\theta_{0,k_r}(0)
=
\frac{(-i)^{r+1}}{2^{r+1}}.
}
```

Hence this coefficient is not identically zero.

For every fixed `r`, choose one time

```math
\tau_r>0
```

sufficiently small that

```math
\left|
\widehat\theta_{0,k_r}(\tau_r)
\right|
>0.
```

By continuity there are constants

```math
b_r>0,
\qquad
\eta_r>0
```

such that on the closed interval

```math
I_r
=
[\tau_r-\eta_r,\tau_r+\eta_r]
\subset(0,T)
```

one has

```math
\left|
\widehat\theta_{0,k_r}(\tau)
\right|
\ge
2b_r.
```

The uniform convergence from Section 3 now implies that there exists
`R_r<infinity` such that for every `R>=R_r`,

```math
\boxed{
\left|
\widehat\theta_{1/R,k_r}(\tau)
\right|
\ge
b_r
\quad
\text{for every }\tau\in I_r.
}
```

This is a genuine finite-time amplitude lower bound.  It is no longer only a
Taylor-jet statement.

## 5. Bind to the fixed Littlewood--Paley partition

The campaign fixed one smooth inhomogeneous dyadic partition.

For the annular blocks `q>=0`, choose fixed constants

```math
0<a_{LP}<b_{LP}<\infty
```

such that every multiplier `\psi_q` is supported inside

```math
a_{LP}\lambda_q
\le
|\xi|
\le
b_{LP}\lambda_q.
```

Let `J_{LP}<infinity` be a uniform upper bound on the number of annular
multipliers nonzero at one nonzero frequency.

Choose `N` large enough that all frequencies used below lie outside the
inhomogeneous base ball.

The initial Fourier support has maximal magnitude

```math
K_0
=
\sqrt2 N.
```

The generated mode has magnitude

```math
K_r
=
N\sqrt{(r+1)^2+1}.
```

Choose once and for all a finite integer `r_*` such that

```math
\boxed{
\frac{K_{r_*}}{K_0}
>
\frac{b_{LP}}{a_{LP}}.
}
```

Such an `r_*` exists because the left side tends to infinity.

Let `q_{init}` be the largest annular index whose multiplier meets the
initial Fourier support.

If a shell `p<=q_{init}` met `K_{r_*}`, then

```math
K_{r_*}
\le
b_{LP}\lambda_{p_*}
\le
b_{LP}\lambda_{q_{init}}
\le
\frac{b_{LP}}{a_{LP}}K_0,
```

contradicting the choice of `r_*`.

Therefore every dyadic shell meeting the generated frequency satisfies

```math
\boxed{
p>q_{init}.
}
```

The generated mode is separated from every shell that sees the initial
support.

## 6. One generated dyadic block becomes threshold violating

At the fixed generated frequency, the partition identity gives

```math
\sum_p\psi_{p_*}(K_{r_*})=1.
```

At most `J_{LP}` terms are nonzero, so one fixed shell `p_*`, depending
only on the partition and the generated frequency, satisfies

```math
|\psi_{p_*}(K_{r_*})|
\ge
\frac1{J_{LP}}.
```

For the physical vertical velocity `w=A\theta_{1/R}`, the Fourier
coefficient of the block `\Delta_{p_*} w` at `K_{r_*}` has magnitude at least

```math
\frac{A b_{r_*}}{J_{LP}}.
```

A Fourier coefficient is bounded above by the `L^\infty` norm of the
corresponding periodic function. Hence

```math
\|u_{p_*}(t)\|_\infty
\ge
\frac{A b_{r_*}}{J_{LP}}.
```

Because `p_*` meets `K_{r_*}`,

```math
\lambda_{p_*}
\le
\frac{K_{r_*}}{a_{LP}}.
```

Therefore

```math
\lambda_{p_*}^{-1}\|u_{p_*}(t)\|_\infty
\ge
\frac{
A a_{LP} b_{r_*}
}{
J_{LP}K_{r_*}
}.
```

Using

```math
A=R\nu N,
\qquad
K_{r_*}
=
N\sqrt{(r_*+1)^2+1},
```

gives

```math
\boxed{
\lambda_{p_*}^{-1}\|u_{p_*}(t)\|_\infty
\ge
R\nu
\frac{
a_{LP}b_{r_*}
}{
J_{LP}\sqrt{(r_*+1)^2+1}
}.
}
```

Consequently, for

```math
R
\ge
R_*
:=
\frac{
c_0J_{LP}\sqrt{(r_*+1)^2+1}
}{
a_{LP}b_{r_*}
},
```

the generated block, which is strict-high at the initial time because `p_*>q_{init}>=Q(0)`, becomes threshold violating:

```math
\boxed{
\lambda_{p_*}^{-1}\|u_{p_*}(t)\|_\infty
\ge
c_0\nu.
}
```

This holds for every dimensionless time `\tau\in I_{r_*}`, after increasing
`R_*` if necessary to include the transport-limit convergence threshold.

Thus a shell that lies strictly above every block meeting the initial support
becomes threshold violating during the exact NSE evolution.

This proves quantitative threshold leakage in the calibration class.

## 7. Selector consequence

Because a threshold-violating shell `p_*` cannot lie strictly above the current
dissipation index,

```math
Q(t)\ge p_*.
```

The fixed shell `p_*` also satisfies

```math
\lambda_{p_*}
\ge
\frac{K_{r_*}}{b_{LP}}.
```

Therefore on the physical-time interval corresponding to `I_{r_*}`,

```math
\boxed{
\Lambda(t)
\ge
\frac{
N\sqrt{(r_*+1)^2+1}
}{
b_{LP}
}.
}
```

No assumption that the selector stays fixed is used.  The conclusion allows
the selector to advance before, during, or after the displayed leakage.

## 8. The guaranteed charge still has inverse-overshoot scale

The dimensionless interval `I_{r_*}` has fixed length

```math
\ell_*
=
|I_{r_*}|
>0.
```

Since

```math
\tau=ANt,
```

its physical length is

```math
|I_{r_*}^{phys}|
=
\frac{\ell_*}{AN}
=
\frac{\ell_*}{R\nu N^2}.
```

Combining this with the selector lower bound gives

```math
\int_{I_{r_*}^{phys}}
\Lambda(t)^2\,dt
\ge
\frac{
N^2((r_*+1)^2+1)
}{
b_{LP}^2
}
\frac{
\ell_*
}{
R\nu N^2
}.
```

Hence

```math
\boxed{
\int_{I_{r_*}^{phys}}
\Lambda(t)^2\,dt
\ge
\frac{
\ell_*((r_*+1)^2+1)
}{
b_{LP}^2R\nu
}.
}
```

For the fixed `r_*` selected above, the certified charge is proportional to

```math
R^{-1}.
```

This is the same overshoot dependence that L5-15 already proved can be
summable across a sequence of increasingly large excursions.

The theorem therefore has a deliberately two-sided interpretation:

1. **positive:** threshold-sized higher-frequency leakage really occurs in the
   exact NSE calibration;
2. **negative for closure:** one fixed leakage distance supplies only an
   inverse-`R` guaranteed `Lambda^2` charge over the natural turnover-time
   window.

This does not upper-bound the actual selector charge.  Farther generated
modes, longer persistence, or signed transfer may force more.  The result says
only that the fixed-distance certificate by itself is not the missing
non-summable cost.

## 9. Required frequency growth for a charge-only repair

At lattice distance `r`, the same turnover-window scaling would produce a
certificate of order

```math
\frac{(r+1)^2+1}{R\nu}.
```

To obtain an order-`1/nu` charge from this mechanism alone requires

```math
(r+1)^2
\gtrsim
R,
```

or equivalently

```math
\boxed{
r
\gtrsim
\sqrt R.
}
```

Thus the next quantitative question is not fixed-distance leakage.

It is whether threshold-sized leakage can reach spectral distance comparable
to `sqrt(R)` on the turnover scale, or whether another temporal mechanism
produces an equivalent non-summable charge.

L5-18 already signals difficulty: the first Taylor coefficient at distance
`r` has factorial suppression.  L5-19 does not turn that heuristic into a
uniform upper bound in `r`; that is the next live boundary.

## 10. What has and has not been proved

Proved in the exact periodic 2.5D calibration:

- finite-time amplitude leakage, not merely a nonzero temporal jet;
- after a finite LP-partition-dependent spectral separation, a generated block
  becomes threshold violating for all sufficiently large `R`;
- the selector must reach the generated frequency scale on a fixed
  dimensionless time interval;
- the resulting fixed-distance `Lambda^2` charge certificate scales like
  `1/R`.

Not proved:

- any corresponding theorem for the selected whole-space A2 class;
- a lower bound at a distance growing with `R`;
- an upper bound on how far the selector actually advances;
- a non-summable A2 charge;
- a bound on the overshoot integral `Omega`;
- a signed cumulative flux theorem;
- phase decoherence for general Leray--Hopf solutions.

## 11. Next live obligation: C2-DIST

The smallest safe successor is now quantitative **distance versus overshoot**.

In the exact 2.5D calibration, determine the largest spectral distance at which
a threshold-sized coefficient can be guaranteed on a fixed turnover-time
window as `R\to\infty`.

Two outcomes are useful.

### Positive closure direction

If one can prove threshold leakage to

```math
r(R)
\gtrsim
\sqrt R
```

with a fixed dimensionless residence interval, the induced selector charge is
no longer inverse-`R) summable and the mechanism becomes relevant to an A2
reopening.

### Negative calibration direction

If analytic/Gevrey control shows instead that every threshold-reaching
distance satisfies, for example,

```math
r(R)
=
o(\sqrt R),
```

then the exact 2.5D calibration demonstrates that temporal spectral leakage
alone does not supply the needed charge; the live route must move to cumulative
signed flux, repeated-event coherence, or another genuinely nonlinear
whole-space mechanism.

Either outcome materially sharpens C2-AMP.

## 12. Hard rejection tests

Reject any successor that:

- treats the periodic 2.5D theorem as a theorem in the selected whole-space
  A2 class;
- uses a Fourier coefficient without binding it to the fixed smooth dyadic
  partition;
- assumes the selector `Q(t)` stays fixed while leakage occurs;
- calls a shell strict-high at the same time it violates the threshold;
- converts the fixed-distance `1/R` charge certificate into a
  non-summable cost;
- infers `r(R)\gtrsim\sqrt R` from support leakage alone;
- uses the first Taylor jet without a finite-time remainder estimate;
- reopens L3 using only turnover residence;
- reopens L4 through the unsigned active diagonal.

## 13. Claim boundary

The protected claim sought from this tranche is exactly

```text
FIXED_DISTANCE_THRESHOLD_LEAKAGE_PROVED_IN_2P5D_CALIBRATION
__FIXED_DISTANCE_CHARGE_CERTIFICATE_REMAINS_R_INVERSE.
```

It proves threshold-sized finite-time leakage after a fixed spectral
separation in the exact periodic 2.5D calibration.

It does not prove A2.

It does not prove a non-summable selector charge.

It does not prove a distance growing with `R`.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.

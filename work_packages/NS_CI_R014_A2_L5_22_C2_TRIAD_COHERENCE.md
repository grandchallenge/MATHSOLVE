# NS-CI-R014-A2-L5-22 — turnover-scale signed transfer coherence calibration

## Disposition

- Campaign: \`NS-CI-001\`
- Restricted target: \`NS-CI-R014-A2\`
- Tracker: \`MATHSOLVE#59\`
- Protected base: \`30bd26d970b1e25a42424aeec959e851c4158652\`
- Protected predecessor: \`NS-CI-R014-A2-L5-21\`
- Result:
  \`TURNOVER_SCALE_SIGNED_TRANSFER_COHERENCE_PERSISTS_IN_EXACT_2P5D_NSE__SUBTURNOVER_DECOHERENCE_NOT_GENERIC\`
- A2 theorem: open
- L5: active
- C2-TRIAD: narrowed from generic phase decoherence to repeated-event /
  genuinely three-dimensional coherence
- MATHCERT adjudication: absent
- Evidence class: exact theorem for the smooth unforced periodic 2.5D
  Navier--Stokes calibration admitted in L5-18/L5-19; not the selected
  whole-space A2 class

L5-21 terminated the generic complete-band energy-flux route at shell-ledger
level.  The next possible repair was more equation-specific:

> perhaps the phase/correlation needed for turnover-size active-band transfer
> must decohere substantially faster than one nonlinear turnover.

This tranche tests that proposal on an actual Navier--Stokes trajectory rather
than on an isolated Galerkin triad.

The exact 2.5D periodic solution from L5-18 has a turnover-variable limit in
which the target signed nonlinear transfer is strictly positive at the initial
time.  The L5-19 uniform Sobolev bounds imply strong convergence of the
finite-\`R\` solution to that inviscid turnover limit on every fixed turnover
window.  Continuity therefore gives one fixed positive turnover interval on
which both the target amplitude and its signed nonlinear forcing stay bounded
away from zero uniformly for all sufficiently large \`R\`.

Consequently the physical signed nonlinear energy transfer into the active
target remains of order

\`\`\`math
A^3N
\`\`\`

for a physical time of order

\`\`\`math
(AN)^{-1},
\`\`\`

and transfers an order-\`A^2\` amount of energy.  Viscous loss over the same
interval is smaller by the factor \`1/R\`.

Thus actual NSE triadic transfer can remain coherently signed for a fixed
fraction of one turnover time while the L5-20 selector charge on that same
fixed turnover scale tends to zero.  A universal **subturnover**
phase-decoherence theorem cannot be the missing C2 mechanism.

The result does not address repeated overshoot episodes, long-time recycling,
or genuinely three-dimensional triad networks.

## 1. Protected exact 2.5D calibration

Use the L5-18/L5-19 exact periodic solution with

\`\`\`math
A=R\nu N,
\qquad
\tau=ANt,
\qquad
\varepsilon=\frac{\nu N}{A}=\frac1R.
\`\`\`

The vertical component is

\`\`\`math
w(t,x)
=
A\theta_\varepsilon(\tau,X,Y),
\qquad
X=Nx_1,\quad Y=Nx_2,
\`\`\`

where

\`\`\`math
\partial_\tau\theta_\varepsilon
+
e^{-\varepsilon\tau}
V\cdot\nabla\theta_\varepsilon
=
\varepsilon\Delta\theta_\varepsilon,
\qquad
V(X,Y)=(\cos Y,\cos X),
\`\`\`

with initial datum

\`\`\`math
\theta_\varepsilon(0,X,Y)
=
\cos X+\cos Y+\sin(X+Y).
\`\`\`

The horizontal velocity is the exact decaying two-mode field from L5-18.
The system is an exact smooth unforced 3D Navier--Stokes solution in the
periodic 2.5D class.

## 2. Target amplitude and signed nonlinear forcing

Let \`c_\varepsilon(\tau)\` be the real Fourier coefficient of
\`\sin(X+Y)\` in \`\theta_\varepsilon(\tau)\`.

Let \`g_\varepsilon(\tau)\` be the \`\sin(X+Y)\` coefficient of the nonlinear
transport contribution

\`\`\`math
-e^{-\varepsilon\tau}
V\cdot\nabla\theta_\varepsilon.
\`\`\`

Because

\`\`\`math
\Delta\sin(X+Y)
=
-2\sin(X+Y),
\`\`\`

the target coefficient obeys the exact identity

\`\`\`math
\boxed{
c_\varepsilon'
=
g_\varepsilon
-
2\varepsilon c_\varepsilon.
}
\`\`\`

At the initial time,

\`\`\`math
c_\varepsilon(0)=1.
\`\`\`

A direct trigonometric calculation gives

\`\`\`math
V\cdot\nabla
(\cos X+\cos Y+\sin(X+Y))
\`\`\`

with \`\sin(X+Y)\` coefficient \`-1\`.  Indeed,

\`\`\`math
-\cos Y\sin X
-\cos X\sin Y
\`\`\`

contributes exactly \`-\sin(X+Y)\`, while the remaining terms have different
Fourier phases.

Therefore

\`\`\`math
\boxed{
g_\varepsilon(0)=1
}
\`\`\`

for every \`\varepsilon\`, and hence

\`\`\`math
\boxed{
c_\varepsilon'(0)=1-2\varepsilon.
}
\`\`\`

This is the turnover-normalized form of the L5-17 target derivative.

## 3. Inviscid turnover limit

Set \`\varepsilon=0\`.  Then

\`\`\`math
\partial_\tau\theta_0
+
V\cdot\nabla\theta_0
=
0.
\`\`\`

The vector field \`V\` and the initial datum are smooth, so
\`\theta_0\`, \`c_0\`, and \`g_0\` are smooth on every finite time interval.

At \`\tau=0\`,

\`\`\`math
c_0(0)=1,
\qquad
g_0(0)=1.
\`\`\`

By continuity there exists a number

\`\`\`math
\tau_*>0
\`\`\`

depending only on this fixed normalized initial datum such that

\`\`\`math
\boxed{
c_0(\tau)\ge\frac34,
\qquad
g_0(\tau)\ge\frac34
}
\`\`\`

for all

\`\`\`math
0\le\tau\le\tau_*.
\`\`\`

Consequently the inviscid-limit signed target-transfer correlation

\`\`\`math
\mathcal T_0(\tau)
=
c_0(\tau)g_0(\tau)
\`\`\`

satisfies

\`\`\`math
\mathcal T_0(\tau)
\ge
\frac9{16}
\`\`\`

throughout that fixed turnover interval.

No explicit numerical value of \`\tau_*\` is required.

## 4. Strong convergence on the fixed turnover interval

L5-19 proved uniform finite-time Sobolev bounds: for every fixed integer
\`s>=4\` and fixed \`T\`,

\`\`\`math
\sup_{0\le\varepsilon\le1}
\sup_{0\le\tau\le T}
\|\theta_\varepsilon(\tau)\|_{H^{s+2}}
\le
C_{s,T}.
\`\`\`

The L5-19 argument recorded \`L^2\` convergence to the inviscid turnover limit.
For the present transfer observable we need one fixed positive Sobolev order.
That follows from the same equation with no new hypothesis.

Let

\`\`\`math
z_\varepsilon
=
\theta_\varepsilon-\theta_0.
\`\`\`

Subtracting the two equations gives

\`\`\`math
\partial_\tau z_\varepsilon
+
V\cdot\nabla z_\varepsilon
=
\varepsilon\Delta\theta_\varepsilon
+
\big(
1-e^{-\varepsilon\tau}
\big)
V\cdot\nabla\theta_\varepsilon.
\`\`\`

On \`[0,T]\`,

\`\`\`math
0
\le
1-e^{-\varepsilon\tau}
\le
\varepsilon T.
\`\`\`

A standard \`H^s\` transport estimate for the fixed smooth divergence-free
field \`V\`, together with the protected uniform \`H^{s+2}\` bound, gives

\`\`\`math
\frac d{d\tau}
\|z_\varepsilon\|_{H^s}
\le
C_{s,T}
\|z_\varepsilon\|_{H^s}
+
C_{s,T}\varepsilon.
\`\`\`

Since \`z_\varepsilon(0)=0\`, Gronwall yields

\`\`\`math
\boxed{
\sup_{0\le\tau\le T}
\|\theta_\varepsilon(\tau)-\theta_0(\tau)\|_{H^s}
\le
C_{s,T}\varepsilon.
}
\`\`\`

Thus the convergence is strong enough to control the fixed target coefficient
and its transport forcing.

## 5. Uniform convergence of the signed transfer observable

The map

\`\`\`math
\theta
\longmapsto
\operatorname{coeff}_{\sin(X+Y)}(\theta)
\`\`\`

is a bounded linear functional on \`L^2\`.

The map

\`\`\`math
\theta
\longmapsto
\operatorname{coeff}_{\sin(X+Y)}
\big(
-V\cdot\nabla\theta
\big)
\`\`\`

is a bounded linear functional on \`H^1\`.

Using the strong convergence above and

\`\`\`math
e^{-\varepsilon\tau}
=
1+O_T(\varepsilon),
\`\`\`

one obtains

\`\`\`math
\boxed{
\sup_{0\le\tau\le T}
|c_\varepsilon(\tau)-c_0(\tau)|
\le
C_T\varepsilon,
}
\`\`\`

and

\`\`\`math
\boxed{
\sup_{0\le\tau\le T}
|g_\varepsilon(\tau)-g_0(\tau)|
\le
C_T\varepsilon.
}
\`\`\`

Take \`T=\tau_*\`.  For all sufficiently large \`R=1/\varepsilon\`,

\`\`\`math
\boxed{
c_{1/R}(\tau)\ge\frac12,
\qquad
g_{1/R}(\tau)\ge\frac12
}
\`\`\`

for every

\`\`\`math
0\le\tau\le\tau_*.
\`\`\`

Therefore

\`\`\`math
\boxed{
\mathcal T_{1/R}(\tau)
=
c_{1/R}(\tau)g_{1/R}(\tau)
\ge
\frac14
}
\`\`\`

uniformly throughout one fixed positive turnover interval.

## 6. Physical signed transfer scale

The physical target sine amplitude is

\`\`\`math
C_{\rm phys}(t)
=
A c_{1/R}(\tau).
\`\`\`

The nonlinear contribution to its coefficient derivative is

\`\`\`math
A^2N g_{1/R}(\tau).
\`\`\`

Up to the fixed Fourier normalization constant, the signed nonlinear energy
transfer into that target sine component is therefore

\`\`\`math
\Pi_{\rm target}(t)
=
A^3N
c_{1/R}(\tau)g_{1/R}(\tau).
\`\`\`

On the interval found above,

\`\`\`math
\boxed{
\Pi_{\rm target}(t)
\ge
c_*A^3N
}
\`\`\`

for one fixed \`c_*>0\`.

The physical interval length is

\`\`\`math
\frac{\tau_*}{AN}.
\`\`\`

Hence

\`\`\`math
\boxed{
\int_0^{\tau_*/(AN)}
\Pi_{\rm target}(t)\,dt
\ge
c_*\tau_* A^2.
}
\`\`\`

The coherently signed nonlinear transfer therefore moves an order-\`A^2\`
amount of energy over a fixed fraction of one turnover time.

## 7. Viscosity is lower order on this interval

The target viscous coefficient term is

\`\`\`math
-2\nu N^2 A c_{1/R}.
\`\`\`

Its target-energy loss scale is therefore \`O(\nu N^2A^2)\`.

Over the turnover interval \`\tau_*/(AN)\` the total viscous target-energy loss
is at most

\`\`\`math
C
\nu N^2 A^2
\frac1{AN}
=
C
\frac{\nu N}{A}
A^2
=
C\frac{A^2}{R}.
\`\`\`

Thus the ratio

\`\`\`math
\frac{
\text{viscous target-energy loss}
}{
\text{coherent nonlinear target transfer}
}
\`\`\`

is \`O(1/R)\`.

For large overshoot ratio, viscosity does not destroy the fixed-turnover
coherent transfer interval.

## 8. The target remains large relative to the threshold scale

Throughout the same interval,

\`\`\`math
|C_{\rm phys}(t)|
\ge
\frac A2.
\`\`\`

Its physical frequency is \`\sqrt2N\`.  Hence the squared threshold ratio is

\`\`\`math
\left(
\frac{|C_{\rm phys}|}{\nu\sqrt2N}
\right)^2
\ge
\frac{R^2}{8}.
\`\`\`

For every fixed campaign threshold constant \`c_0\`, the target remains a
large threshold-violating mode for all sufficiently large \`R\`.

This does not assert that it remains the defining shell \`Q(t)\`; L5-18/L5-19
show that additional modes are generated.  Only overshoot persistence of this
specific target mode is claimed.

## 9. Relation to L5-20

L5-20 proves that, on every fixed turnover horizon in this same exact
calibration,

\`\`\`math
\int\Lambda(t)^2\,dt
\le
C\nu^{-1}R^{-1/2}
\`\`\`

using the explicit inherited order \`s=4\`.

The present result gives, on a fixed positive subinterval of such a turnover
horizon,

\`\`\`math
\Pi_{\rm target}
\gtrsim
A^3N
\`\`\`

with fixed sign, and an integrated nonlinear transfer of order \`A^2\`.

Thus the calibration realizes simultaneously:

\`\`\`text
large threshold overshoot;
order-turnover signed nonlinear transfer;
fixed positive turnover-time coherence;
generated higher frequencies;
vanishing fixed-window A2 selector charge.
\`\`\`

Therefore the missing C2 mechanism cannot be a universal statement that strong
triadic transfer must lose sign coherence on a time scale
\`o((AN)^-1)\`.

## 10. What remains live

This tranche does not show that coherent transfer can be recycled through
infinitely many overshoot episodes.

It does not prove that a general 3D upper active band can sustain the same
coherence.

It does not exclude:

- cumulative phase drift over many turnover times;
- anti-fragmentation across repeated episodes;
- genuinely 3D triad-network constraints;
- a frequency-weighted transfer law;
- a selector-aware theorem that avoids differentiating the selector.

The result only removes **subturnover phase decoherence** as a generic
equation-level repair.

## 11. Next live obligation: C2-REPEAT

The smallest safe successor is repeated-event coherence.

The precise question is:

> Can a selected whole-space solution realize infinitely many increasing
> upper-band overshoot episodes, each with order-turnover coherent signed
> transfer, while the A2 selector charge and ordinary dissipation remain
> summable?

A viable theorem must connect distinct episodes or scale levels.  Candidate
mechanisms include:

- a non-summable cost for resetting the transfer phase;
- a lower bound on cross-scale memory carried by newly generated modes;
- an anti-fragmentation theorem preventing arbitrarily short separated
  coherent episodes;
- a genuinely three-dimensional interaction constraint absent from the 2.5D
  calibration.

If the argument uses only one-episode turnover coherence, it is already
separated by L5-15 and the present tranche.

## 12. Hard rejection tests

Reject any successor that:

- treats the periodic 2.5D calibration as a selected whole-space theorem;
- asserts that the target mode remains the defining shell;
- infers repeated-event coherence from one fixed turnover interval;
- discards generated modes and replaces the full NSE by an isolated invariant
  triad without proof;
- assumes a frequency-weighted transfer budget;
- differentiates the selector;
- reopens L3 from turnover residence;
- reopens L4 from generic signed conservation.

## 13. Claim boundary

The protected claim sought from this tranche is exactly

\`\`\`text
TURNOVER_SCALE_SIGNED_TRANSFER_COHERENCE_PERSISTS_IN_EXACT_2P5D_NSE
__SUBTURNOVER_DECOHERENCE_NOT_GENERIC.
\`\`\`

It proves, in the exact smooth unforced periodic 2.5D NSE calibration, a fixed
positive turnover interval on which:

- the target remains a large threshold overshoot;
- its signed nonlinear forcing remains bounded away from zero;
- the signed target energy transfer remains order \`A^3N\`;
- its integrated coherent transfer is order \`A^2\`;
- viscosity is smaller by \`O(1/R)\`.

It does not prove A2.

It does not prove repeated-event coherence.

It does not prove the same theorem in the selected whole-space class.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.

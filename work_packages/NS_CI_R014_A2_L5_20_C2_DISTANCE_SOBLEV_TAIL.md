# NS-CI-R014-A2-L5-20 — Sobolev tail bound on threshold-reaching distance

## Disposition

- Campaign: \`NS-CI-001\`
- Restricted target: \`NS-CI-R014-A2\`
- Tracker: \`MATHSOLVE#59\`
- Protected base: \`412ff863035881207ad340608c2fc93f29d9becc\`
- Protected predecessor: \`NS-CI-R014-A2-L5-19\`
- Result:
  \`C2_DIST_SQRT_R_THRESHOLD_REACH_EXCLUDED_IN_2P5D_CALIBRATION__TURNOVER_SELECTOR_CHARGE_VANISHES\`
- A2 theorem: open
- L5: active
- C2-DIST: closed for the exact periodic 2.5D calibration
- MATHCERT adjudication: absent
- Evidence class: exact upper bound in the same smooth unforced periodic 2.5D
  calibration used by L5-18/L5-19; not the selected whole-space A2 class

L5-19 proved that threshold-sized spectral leakage reaches every sufficiently
separated **fixed** distance in the exact periodic 2.5D calibration, but the
resulting guaranteed selector charge is only proportional to \`R^{-1}\`.

That tranche isolated the next question:

> can threshold-sized leakage reach distance comparable to \`sqrt(R)\` on a
> fixed turnover-time window, so that the selector charge becomes order one?

For this calibration the answer is no.

No Gevrey theorem is needed. The uniform finite-time Sobolev estimate already
proved in L5-19, combined with the fact that the solution is supported on the
two-dimensional frequency plane \`k_3=0\`, gives a dyadic \`L^\infty\` tail
bound. At Sobolev order \`s\` it forces every threshold-violating generated
shell to lie below normalized frequency \`C_{s,T} R^{1/s}\`.

In particular, with \`s=4\`,

\`\`\`math
\frac{\lambda_p}{N}
\lesssim
R^{1/4}
\`\`\`

for every threshold-violating shell on a fixed turnover-time interval. This is
strictly smaller than the \`sqrt(R)\` distance required by the L5-19
charge-only mechanism.

Moreover the **actual** selector in this calibration satisfies

\`\`\`math
\Lambda(t)
\lesssim
N R^{1/s},
\`\`\`

and hence over any fixed turnover-time horizon

\`\`\`math
\int \Lambda(t)^2\,dt
\lesssim
\frac{1}{\nu}R^{2/s-1}.
\`\`\`

For \`s=4\` this is \`O(R^{-1/2}/\nu)\`; it tends to zero.

Thus fixed-time spectral propagation in this exact 2.5D calibration cannot
supply the missing non-summable A2 charge. The live C2 route must move away
from charge generated solely by propagation distance and toward cumulative
signed flux, repeated-event coherence, phase decoherence, or another
whole-space dynamic mechanism.

## 1. Protected L5-19 input

Use the exact periodic 2.5D solution in turnover variables

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

with

\`\`\`math
\varepsilon=\frac1R,
\qquad
A=R\nu N,
\qquad
\tau=ANt.
\`\`\`

The physical vertical velocity is

\`\`\`math
w(t,x)=A\theta_{1/R}(\tau,Nx_1,Nx_2).
\`\`\`

The horizontal velocity contains only the original frequency scale \`N\`.

L5-19 proved that for every fixed finite \`T\` and every fixed integer
Sobolev order \`s>=4\` one has a uniform bound

\`\`\`math
\boxed{
\sup_{0\le\varepsilon\le1}
\sup_{0\le\tau\le T}
\|\theta_\varepsilon(\tau)\|_{H^{s+2}(\mathbb T^2)}
\le
C_{s,T}.
}
\`\`\`

Only the weaker inherited consequence

\`\`\`math
\sup_{\varepsilon,\tau}
\|\theta_\varepsilon(\tau)\|_{H^s}
\le
C_{s,T}
\`\`\`

is needed below.

## 2. Normalize the campaign dyadic shell scale

Retain the fixed smooth Littlewood--Paley partition used in L5-19.

For an annular shell \`p\`, set

\`\`\`math
L_p
=
\frac{\lambda_p}{N}.
\`\`\`

The annular support constants give

\`\`\`math
a_{LP}L_p
\lesssim
|k|
\lesssim
b_{LP}L_p
\`\`\`

for normalized lattice frequencies \`k=(m,n)\in\mathbb Z^2\` contributing to
that block.

Because the calibration is independent of \`x_3\`, all nonzero Fourier
frequencies lie in the plane \`k_3=0\`. Therefore the number of normalized
lattice points in one fixed-width annulus at radius \`L_p>=1\` is bounded by

\`\`\`math
\#\mathcal A_p
\le
C_{LP}L_p^2.
\`\`\`

The square root of the frequency count is therefore only order \`L_p\`, not
\`L_p^{3/2}\`.

This two-dimensional counting is a property of this calibration class. It is
not imported into the selected general whole-space problem.

## 3. Uniform dyadic L-infinity tail

Let \`\Delta_p^{(N)}\` denote the normalized block induced by the campaign
multiplier at physical frequency \`Nk\`.

For every \`\tau\in[0,T]\`,

\`\`\`math
\|\Delta_p^{(N)}\theta_\varepsilon(\tau)\|_\infty
\le
\sum_{k\in\mathcal A_p}
|\widehat{\theta_\varepsilon}(k,\tau)|.
\`\`\`

By Cauchy--Schwarz,

\`\`\`math
\|\Delta_p^{(N)}\theta_\varepsilon\|_\infty
\le
(\#\mathcal A_p)^{1/2}
\left(
\sum_{k\in\mathcal A_p}
|\widehat{\theta_\varepsilon}(k)|^2
\right)^{1/2}.
\`\`\`

On the annulus, \`|k|\gtrsim L_p\`, so the uniform \`H^s\` bound gives

\`\`\`math
\left(
\sum_{k\in\mathcal A_p}
|\widehat{\theta_\varepsilon}(k)|^2
\right)^{1/2}
\le
C_{s,T}L_p^{-s}.
\`\`\`

Combining the two estimates,

\`\`\`math
\boxed{
\|\Delta_p^{(N)}\theta_\varepsilon(\tau)\|_\infty
\le
C_{s,T,LP}
L_p^{1-s}.
}
\`\`\`

This estimate is uniform in \`R>=1\`, \`\tau\in[0,T]\`, and the terminal
frequency.

## 4. Convert the tail bound to the campaign threshold

Above the fixed finite set of shells meeting the horizontal source modes, the
full velocity block is vertical. Hence

\`\`\`math
\|u_p(t)\|_\infty
\le
A C_{s,T,LP}L_p^{1-s}.
\`\`\`

Since

\`\`\`math
\lambda_p
=
NL_p,
\qquad
A=R\nu N,
\`\`\`

one obtains

\`\`\`math
\boxed{
\lambda_p^{-1}\|u_p(t)\|_\infty
\le
C_{s,T,LP}
R\nu
L_p^{-s}.
}
\`\`\`

Therefore there is a constant \`K_{s,T}<infinity\`, depending only on the
fixed horizon, Sobolev order, LP partition, and threshold constant \`c_0\`,
such that

\`\`\`math
L_p
>
K_{s,T}R^{1/s}
\`\`\`

implies

\`\`\`math
\lambda_p^{-1}\|u_p(t)\|_\infty
<
c_0\nu
\`\`\`

for every \`\tau\in[0,T]\`.

Equivalently, every threshold-violating shell on the fixed turnover window
satisfies

\`\`\`math
\boxed{
\frac{\lambda_p}{N}
\le
K_{s,T}R^{1/s}.
}
\`\`\`

No selector continuity or selector residence is assumed.

## 5. The sqrt(R) distance required by L5-19 is excluded

Take \`s=4\`. Then every threshold-violating shell satisfies

\`\`\`math
\boxed{
\frac{\lambda_p}{N}
\le
K_{4,T}R^{1/4}.
}
\`\`\`

But L5-19 showed that the propagation-distance charge mechanism would need
threshold-sized leakage at distance comparable to

\`\`\`math
R^{1/2}.
\`\`\`

Since

\`\`\`math
R^{1/4}
=
o(R^{1/2}),
\`\`\`

the required \`sqrt(R)\` threshold reach is impossible in this exact
calibration on every fixed turnover-time horizon.

More generally, because the inherited Sobolev bound is available at every
fixed integer order, for every fixed \`\delta>0\` one may choose
\`s>1/\delta\` and obtain

\`\`\`math
\frac{\lambda_p}{N}
\le
C_{\delta,T}R^\delta
\`\`\`

for every threshold-violating shell.

Thus the threshold-reaching scale in this calibration is sub-polynomial in the
sense of arbitrary fixed positive powers. No analyticity or Gevrey input is
required for the present separation from \`sqrt(R)\`.

## 6. Direct selector upper bound

Choose a dyadic index \`q_R\` whose normalized shell scale satisfies

\`\`\`math
\frac{\lambda_{q_R}}N
\ge
K_{s,T}R^{1/s}
\`\`\`

with only the fixed dyadic-factor overhead.

Every shell \`p>q_R\` then satisfies the strict-high threshold throughout the
turnover window. By the definition of the dissipation index,

\`\`\`math
Q(t)
\le
q_R.
\`\`\`

Therefore

\`\`\`math
\boxed{
\Lambda(t)
\le
C_{s,T}N R^{1/s}
}
\`\`\`

for all

\`\`\`math
0\le t\le\frac{T}{AN}.
\`\`\`

This is an upper bound on the actual selector in the calibration, not merely an
upper bound on one chosen leakage certificate.

It is compatible with L5-19: fixed sufficiently separated shells do become
threshold violating as \`R\to\infty\`, while the farthest possible
threshold-violating shell still grows much more slowly than \`sqrt(R)\`.

## 7. Turnover-window selector charge vanishes

The physical length of the fixed turnover horizon is

\`\`\`math
\frac{T}{AN}
=
\frac{T}{R\nu N^2}.
\`\`\`

Using the selector upper bound,

\`\`\`math
\int_0^{T/(AN)}
\Lambda(t)^2\,dt
\le
C_{s,T}
N^2R^{2/s}
\frac{T}{R\nu N^2}.
\`\`\`

Hence

\`\`\`math
\boxed{
\int_0^{T/(AN)}
\Lambda(t)^2\,dt
\le
\frac{C_{s,T}}{\nu}
R^{2/s-1}.
}
\`\`\`

For every \`s>2\` the exponent is negative.

At the explicit inherited order \`s=4\`,

\`\`\`math
\boxed{
\int_0^{T/(AN)}
\Lambda(t)^2\,dt
\le
\frac{C_T}{\nu\sqrt R}
\longrightarrow
0.
}
\`\`\`

Thus the exact 2.5D calibration does not merely fail to **prove** an order-one
charge from spectral propagation. Its actual selector charge on any fixed
turnover-time horizon is bounded above by a quantity tending to zero.

## 8. Relation to the fixed-distance lower bound

L5-19 proved a fixed-distance lower certificate

\`\`\`math
\int_{I_{r_*}^{phys}}
\Lambda(t)^2\,dt
\ge
\frac{c_{r_*}}{R\nu}.
\`\`\`

The present upper bound with \`s=4\` is

\`\`\`math
\int_0^{T/(AN)}
\Lambda(t)^2\,dt
\le
\frac{C_T}{\nu R^{1/2}}.
\`\`\`

These are consistent:

\`\`\`math
R^{-1}
\ll
R^{-1/2}.
\`\`\`

The lower and upper estimates leave room for additional threshold-violating
modes beyond the fixed L5-19 witness, but they rule out enough distance growth
to make the charge-only propagation mechanism non-summable.

## 9. Consequence for C2-DIST

The bounded question posed by L5-19 is resolved negatively in the exact
periodic 2.5D calibration:

\`\`\`text
sqrt(R)-scale threshold reach:
    excluded on fixed turnover windows.

actual selector charge from this calibration:
    tends to zero on fixed turnover windows.
\`\`\`

Therefore spectral-distance propagation by itself is not the missing C2
mechanism in this calibration.

This does **not** prove an analogous upper bound for the selected whole-space
Leray--Hopf class. The proof uses the special 2.5D reduction and its uniform
high-Sobolev control.

Its role is diagnostic: the first exact temporal calibration that realizes the
L5-17 turnover forcing, L5-18 spectral leakage, and L5-19 threshold leakage
still fails to generate the scale cost required by A2.

## 10. Next live obligation: C2-FLUX

The smallest safe successor is no longer another spectral-distance estimate in
this calibration.

Return to the selected whole-space upper active band and ask for a genuinely
cumulative temporal quantity.

Preferred first target:

> On a maximal interval over which one upper-band shell remains a threshold
> overshoot, can the signed shell-energy identity convert repeated
> turnover-size internal forcing into either a telescoping energy change, a
> neighboring-shell flux cost, or a depletion factor that controls the
> overshoot integral?

The calculation must keep internal active-band transfer signed until after
time integration. It must separate:

- flux across the upper-band boundary;
- viscous dissipation;
- far-low deformation, already controlled below the relative cutoff;
- selector changes, without differentiating \`1_{\{Q=q\}}\`;
- same-band internal exchange, which should cancel only when the complete
  retained band is summed.

A valid advance would be a time-integrated identity or inequality whose cost is
not the already-closed turnover residence, L3 exit charge, or L4 active
diagonal.

## 11. Hard rejection tests

Reject any successor that:

- treats the periodic 2.5D upper bound as a theorem for the selected whole-space
  A2 class;
- applies three-dimensional frequency counting to this plane-supported
  calibration and thereby changes the proved exponent;
- calls a block strict-high while it violates the threshold;
- assumes \`Q(t)\` is constant;
- converts the L5-19 fixed-distance lower certificate into an order-one cost;
- claims the present selector upper bound closes A2;
- repeats support leakage or fixed-distance threshold leakage as a new
  mechanism;
- reopens L3 from turnover residence;
- reopens L4 from unsigned active-diagonal control.

## 12. Claim boundary

The protected claim sought from this tranche is exactly

\`\`\`text
C2_DIST_SQRT_R_THRESHOLD_REACH_EXCLUDED_IN_2P5D_CALIBRATION
__TURNOVER_SELECTOR_CHARGE_VANISHES.
\`\`\`

It proves that, in the exact periodic 2.5D calibration and on every fixed
turnover-time horizon:

- every threshold-violating shell lies below \`C_{s,T}NR^{1/s}\`;
- in particular \`sqrt(R)\` threshold reach is excluded;
- the actual selector charge is at most
  \`C_{s,T}\nu^{-1}R^{2/s-1}\`;
- at \`s=4\` that charge is \`O(R^{-1/2}/\nu)\`.

It does not prove A2.

It does not prove the same distance bound for general whole-space solutions.

It does not establish cumulative signed flux or phase decoherence.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.

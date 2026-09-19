# NS-CI-R014-A2-L5-6 — Direct L6 tail-transport audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Predecessor: `NS_CI_R014_A2_L5_B1_COUPLED_ENSTROPHY.md`
- Result: `DIRECT_L6_STANDARD_COMMUTATOR_ROUTE_REDUCED_TO_LOW_DEFORMATION`
- A2 theorem: open
- L5: active

The B1 coupled-enstrophy candidate reduces exactly to the closed L4 weighted
column. This tranche returns to B3 through a different mechanism: direct `L6`
energy of a fixed high tail. The unprojected low--high transport has an exact
`L6` cancellation, but the actual high-pass solenoidal equation leaves a
projection/pressure residual. The standard shellwise absolute-value commutator
estimate for that residual is scale-neutral and leaves the same low deformation
coefficient `||grad L_q||_infinity` that blocked the H1 parabolic route. The
standard commutator-estimate family is therefore terminated. A signed identity
inside the projection/pressure residual remains explicitly open.

## 1. Fixed-cutoff tail

For fixed `q`, set

```math
V_q=P_{>q}u,
\qquad
L_q=P_{\le q-2}u,
\qquad
\Phi(V)=|V|^4V.
```

After eliminating pressure with the Leray projector `mathbb P`, the fixed-tail
equation contains

```math
P_{>q}\mathbb P(L_q\cdot\nabla V_q)
```

as its principal low--high transport contribution.

Without the projection, incompressibility gives exactly

```math
\langle L_q\cdot\nabla V_q,\Phi(V_q)\rangle
=
\frac16\int L_q\cdot\nabla |V_q|^6dx
=0.
```

Thus a direct `L6` test does remove the bare transport term.

## 2. The actual projected residual

Because `P_{>q}` and `mathbb P` are self-adjoint Fourier multipliers and commute
with each other, the projected contribution can be written as

```math
I_q
=
\langle
P_{>q}\mathbb P(L_q\cdot\nabla V_q),
\Phi(V_q)
\rangle.
```

Subtracting the exactly vanishing bare transport gives

```math
I_q
=
\langle
(P_{>q}\mathbb P-I)(L_q\cdot\nabla V_q),
\Phi(V_q)
\rangle.
```

Equivalently one may move the self-adjoint multiplier to `Phi(V_q)`. The key
point is that the cancellation converts the problem into a projection/pressure
residual; it does not make that residual identically zero. In particular,
`Phi(V_q)` is neither divergence-free nor spectrally confined above the cutoff.

This section does **not** assert that no further signed cancellation exists
inside `I_q`. The next section audits only the standard absolute commutator
estimate.

## 3. Standard shellwise commutator scale

For a smooth dyadic projector `P_p` with `p>q+O(1)`, the transport commutator has
kernel representation

```math
[P_p,L_q\cdot\nabla]V_p(x)
=
\int K_p(x-y)
\bigl(L_q(x)-L_q(y)\bigr)
\cdot\nabla V_p(y)dy.
```

The mean-value theorem contributes
`lambda_p^{-1} ||grad L_q||_infinity`; frequency localization contributes
`||grad V_p||_r lesssim lambda_p ||V_p||_r`. These factors cancel, yielding

```math
\|[P_p,L_q\cdot\nabla]V_p\|_r
\lesssim
G_q\|V_p\|_r,
```

where

```math
G_q(t)=\|\nabla L_q(t)\|_\infty.
```

The low--high pressure source likewise contains a derivative of the low field;
Riesz transforms are order zero. Consequently the standard paraproduct/
commutator estimate for the projected residual has the schematic form

```math
|I_q|
\lesssim
G_q\|V_q\|_6^6
+
\text{finite-neighbour / strictly-high terms}.
```

The obstruction is the absence of any negative high-frequency power after the
commutator estimate. No claim is made that this absolute-value estimate is
sharp with respect to sign.

## 4. Why this standard route does not close

For `q=Q(t)`, the defining strict-high bound applies only to shells `p>Q` and
gives no upper bound on

```math
G_Q
=\|\nabla u_{\le Q-2}\|_\infty.
```

Replacing `G_Q` by an imported integrable low-mode coefficient would reproduce
the excluded `f in L1_t` route. Localizing the fixed-`q` estimate to `{Q=q}`
recreates selector variation; keeping `q` fixed globally loses strict-high
absorption on `{Q>q}` and returns to the bad-time/residence interface.

Therefore the standard absolute commutator estimate does not provide a new B3
bridge from `Lambda in L2_t`.

## 5. B3 disposition

The bounded candidate has the reduction

```text
UNPROJECTED_LOW_HIGH_TRANSPORT
    -> exact L6 cancellation;

ACTUAL_HIGH_PASS_SOLENOIDAL_TRANSPORT
    -> signed projection / pressure residual;

STANDARD ABSOLUTE COMMUTATOR ESTIMATE
    -> scale-neutral low deformation G_q
    -> no control from Lambda in L2_t;

ACTIVE LOCALIZATION
    -> B4 selector variation;

FIXED-q GLOBALIZATION
    -> bad set {Q>q} and protected residence/depletion interface.
```

Therefore

```text
DIRECT_L6_STANDARD_COMMUTATOR_ROUTE_REDUCED_TO_LOW_DEFORMATION.
```

This terminates only the standard absolute commutator-estimate family. It does
not exclude:

- a signed projection/pressure identity cancelling `I_q` before absolute
  values;
- a genuine low-deformation depletion theorem;
- an intermittency/packet theorem controlling the strict-tail H2 endpoint.

## Successor

The smallest live successor is the signed residual itself: expand the
high-pass/Leray projection term before absolute values and test whether pressure
and high-pass pieces have a structural cancellation not visible to the standard
commutator bound. If that fails, the remaining distinct frontier is an
equation-specific packet/intermittency depletion theorem for `Z_{>Q}`.

Do not repeat moving-tail H1 energy, fixed-tail bad-set splitting,
threshold-residence Duhamel, the standard direct-L6 commutator estimate, or the
closed L4 weighted column.

## Claim boundary

A2 remains unproved. No regularity, `f in L1_t`, signed commutator cancellation,
L4 reopening, MATHCERT certification, or theorem promotion is asserted.
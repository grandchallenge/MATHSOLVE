# NS-CI-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

This is delegated MATHSOLVE mathematical campaign execution. MATHSOLVE may
develop and integrate bounded mathematical results but may not certify them.
MATHCERT retains certification authority.

## Purpose

Continue restricted target `NS-CI-R014-A2` without weakening `Lambda in L2_t`
or importing a regularity criterion that already implies the conclusion.

## Acceptance criteria

- derive `integral ||u||_6^4` from the selected hypothesis and valid
  Leray--Hopf/PDE structure, or terminate each bounded candidate at its first
  exact blocker;
- preserve strict-high use only for `p>Q`;
- keep shell/time constants uniform in terminal frequency;
- do not multiply unrelated `L1_t` quantities, assume selector variation,
  import `f in L1_t`, uniform `H1`, or an LPS norm;
- do not reopen L3 or L4 without satisfying their protected reopening
  conditions.

## Current substantive state

Selected target: `NS-CI-R014-A2`, unproved.

L5 remains active. MATHCERT remains `qualified_interface_only`; this is not
certification of A2 or of any analytic L5 estimate.

### Pointwise L5 reduction

Protected L5-4 merge `14aad98fbbbcf9f0ed780b9aea5b244f189c3947` proved

```text
ZERO_GAP_REDUCTION_PROVED__STATIC_B1_ENDPOINT_SEPARATED__PARABOLIC_B3_ROUTE_REDUCED.
```

The exact pointwise split is

```math
u=u_{\le Q}+u_{>Q},
```

with

```math
||u||_6^4
lesssim
U_0^2 W_{<=Q}
+
c_0^(8/3) nu^(8/3) Z_{>Q}^{2/3}
+
fixed-base remainder,
```

where

```math
W_{<=Q}=sum_{p<=Q} lambda_p^2 A_p,
qquad
Z_{>Q}=sum_{p>Q} lambda_p^2 A_p.
```

The standalone B2 near-threshold cluster is removed from this pointwise L5
representation. B1 and B3 remain the analytic endpoints.

### B1 dynamic audit

`work_packages/NS_CI_R014_A2_L5_B1_COUPLED_ENSTROPHY.md` records

```text
B1_DIRECT_DYNAMIC_ROUTE_REDUCED__SELECTOR_FREE_REPAIR_EQUALS_CLOSED_L4_COLUMN.
```

Moving low enstrophy hits B4 selector variation. Finite complementary coupling
cancels selector variation algebraically, but the unbounded actual selector
retains the terminal active-set issue. Even granting the limiting step, the
surviving low coefficient is exactly the protected L4 weighted-column
quantity, including the active diagonal. No L4 reopening theorem is supplied.

### B3 direct-L6 and signed-projection audits

The standard absolute direct-L6 commutator route reduces to low deformation
`G_Q=||grad u_{<=Q-2}||_infinity` with no high-frequency gain. Subsequent exact
signed-projection/pressure audit showed that high-pass/Leray algebra alone does
not provide a universal exact or sign-definite cancellation. Those routes are
closed as bounded families; they do not exhaust equation-specific nonlinear
mechanisms.

### L5-8 packet/intermittency bridge

Protected merge `b05c3e6ec996a2191b7084a2438147958a58be1d` admitted

```text
PACKET_D1_DIMENSIONALLY_NORMALIZED_CONDITIONAL_BRIDGE_PROVED__D1_NOT_IMPLIED_BY_STATIC_A2_BUDGETS.
```

See `work_packages/NS_CI_R014_A2_L5_B3_PACKET_INTERMITTENCY_D1.md`.

For `U0=||u0||_2`, define

```math
lambda_E=(nu/U0)^2,
qquad
S_D(t)=sum_{q<=Q(t)} lambda_q^(D-1)||u_q(t)||_infinity^2.
```

The conditional packet estimate

```math
PI_D^*:
integral S_D
<=
C_D lambda_E^D
integral sum_q lambda_q^2||u_q||_2^2
```

is scale-covariant and dimensionally consistent. Pointwise,

```math
f^2 <= Lambda^(3-D) S_D,
qquad
f=sup_{q<=Q} lambda_q||u_q||_infinity.
```

At `D=1`, `PI_1^*` plus `Lambda in L2_t` would imply `f in L1_t`. A
threshold-compatible static fixture separates the present A2 scalar budgets
from `PI_1^*`, so the missing estimate must use genuinely dynamic information.

### L5-9 critical H1/2 dynamic audit

Protected merge `7d72d4f8aec2019a8eefb4db4fe151e4f14b1211` admitted

```text
PI1_CRITICAL_H12_ROUTE_REDUCED_TO_SUPERLINEAR_RICCATI__GLOBAL_CRITICAL_TRANSFER_HAS_NO_SIGN.
```

See `work_packages/NS_CI_R014_A2_L5_B3_PI1_CRITICAL_ENERGY_AUDIT.md`.

With

```math
X=sum_q lambda_q||u_q||_2^2,
qquad
Y=sum_q lambda_q^3||u_q||_2^2,
```

Bernstein gives `S_1 <= C Y`, but the standard low-mode-controlled critical
energy candidate uses

```math
f <= C Lambda^2 X^(1/2),
```

and therefore reduces to

```math
X' <= C Lambda^2 X^(3/2).
```

An exact scalar comparison remains blow-up compatible even with `Lambda^2 in
L1_t` and the Leray-compatible `X in L2_t`. An exact real divergence-free
three-mode Fourier triad has zero total `L2` transfer but critical weighted
transfer `-8`, with a phase reversal giving `+8`. Hence the complete critical
nonlinear transfer has no universal sign. Active-set-specific depletion or
selected-transfer coherence remains live.

### L5-10 field-calibration and frequency--scale successor

The durable successor plan is

`work_packages/NS_CI_R014_A2_L5_10_FIELD_CALIBRATION_FREQUENCY_SCALE_HANDOFF.md`.

It records one new elementary but strategically important reduction:

```text
A global PI_1^* estimate is not required.
```

For any fixed finite `R`, the known source envelope makes the set
`{Lambda<=R}` harmless because

```math
f <= C U0 Lambda^(5/2)
   <= C U0 R^(1/2) Lambda^2.
```

On `{Lambda>R}`, L5-8 gives

```math
f^2 <= C Lambda^2 S_1,
qquad
S_1=sum_{q<=Q}||u_q||_infinity^2.
```

Therefore it is sufficient to prove the strictly weaker high-activity tail
condition

```math
integral_{ {Lambda>R} } S_1(t) dt < infinity
```

for some finite `R`. A terminal-local version near each putative singular time
is also sufficient.

The same work package incorporates three recent field developments as bounded
research inputs:

1. **September 2026 forced blow-up construction.** The explicit OpenAI
   construction has core scales `ell_r~(1-t)^(1/2)` and angular/axial speed
   `~(1-t)^(-1/2-h)`. It is a valuable singularity calibration object, but it
   is forced while A2 is unforced. It cannot directly falsify A2. The first
   legitimate task is an exact dyadic lower bound at the core scale, not a
   similarity-scale inference.
2. **Cheskidov--Peng 2026 intermittency framework.** Its active-shell
   Bernstein-saturation weights structurally align with `S_D`; use it to
   formulate high-`Lambda` depletion, not to import a periodic/forced theorem
   into the whole-space unforced target.
3. **Guo--Wang--Xiong arXiv:2609.03877.** Their frequency--scale matching keeps
   dyadic frequency and physical observation scale separate until a summable
   two-sided kernel is obtained. This is a genuinely distinct analytic route
   from the already-closed global commutator estimate, provided the `(q,k)`
   indices are not collapsed prematurely.


### L5-11 forced core-shell calibration

`work_packages/NS_CI_R014_A2_L5_11_FORCED_CORE_SHELL_CALIBRATION.md`,
together with its source/capture audit, closes C1 positively:

```text
FORCED_CORE_SHELL_LP_LOWER_BOUND_PROVED__CALIBRATION_FORCES_LAMBDA_NOT_L2.
```

For the explicit September 2026 **forced** singular construction, a shell at
`lambda_p comparable to (nu(1-t))^-1/2` carries
`||u_p||_infinity >= c sqrt(nu)(1-t)^(-1/2-h)` at every sufficiently late
time. Hence that shell violates the strict-high threshold, so

```math
Lambda(t) >= c(nu(1-t))^{-1/2},
```

and the construction has divergent terminal `integral Lambda^2`, `integral
f`, and `integral S_1`. This is theorem-grade calibration in a different
forcing class; it does not falsify unforced A2.

### L5-12 frequency--scale transplant boundary

`work_packages/NS_CI_R014_A2_L5_12_FREQUENCY_SCALE_TRANSPLANT_BOUNDARY.md`
confirms the Guo--Wang--Xiong two-index mechanism but rejects its direct source
hypothesis as an A2 consequence:

```text
SOURCE_TWO_INDEX_KERNEL_CONFIRMED__DIRECT_CHEMIN_LERNER_IMPORT_BLOCKED_BY_ACTIVE_DIAGONAL.
```

The off-diagonal kernel has genuine summable gain,

```math
K_{k-j}
\sim
2^{-(k-j)/m} \quad (j\ll k),
\qquad
K_{k-j}\sim2^{-(j-k)} \quad (j\gg k),
```

while the central band has unit size. A2 and Leray leave an exact
`lambda_j^(1/2)` deficit in the source critical coefficient, and a protected
packet fixture shows that even finite `integral S_1` does not imply the
source Chemin--Lerner `ell^1` sequence. C3 was therefore narrowed to
`C3-DIAG`.

### L5-13 C3 diagonal audit

`work_packages/NS_CI_R014_A2_L5_13_C3_DIAGONAL_AUDIT.md` executes the three
generic C3-DIAG repairs.

Its bounded disposition is

```text
C3_DIAGONAL_GENERIC_REPAIRS_TERMINATED
__STRICT_HIGH_NO_ELL1
__UNSIGNED_RENORMALIZATION_RETURNS_L4
__LOCAL_SIGN_NOT_UNIVERSAL.
```

The exact conclusions are:

1. A fixed observation-scale shift cannot absorb the half derivative. A linear
   shift `k-j=alpha j+O(1)` must satisfy `alpha>m/2` even to make the
   Leray-weighted source coefficient summable. Moving one active source that
   far off the diagonal does not remove the new unit diagonal at frequency
   `k`.
2. Strict-high control does not repair that new diagonal. A static annular
   packet fixture keeps `Q=0`, satisfies strict-high at arbitrarily large
   frequencies and finite A2/energy/dissipation budgets, yet has a nonsummable
   source critical coefficient sequence.
3. Unsigned Bernstein/dissipation control of the active shell gives exactly
   `||u_Q||_infinity^2 <= C nu^-1 lambda_Q D_Q`, returning the protected L4
   active diagonal.
4. An exact finite-band divergence-free Fourier fixture gives nonzero localized
   total convection-plus-pressure energy flux, with the sign reversed by
   `u -> -u`. Thus incompressibility, pressure algebra, finite-band support,
   and positive localization do not supply a universal instantaneous signed
   cancellation.

These statements do not exclude PDE-specific time-correlated cancellation or
dynamic active-band anti-concentration.


### L5-14 C2 active-band reduction

`work_packages/NS_CI_R014_A2_L5_14_C2_ACTIVE_BAND_REDUCTION.md` records

```text
A2_FAR_LOW_PACKET_REGION_CONTROLLED__SINGULARITY_REQUIRES_TOP_THIRD_D1_CONCENTRATION.
```

For `R_Q=floor(2Q/3)`, ordinary Bernstein and the Leray energy supremum give

```math
sum_{q<=R_Q} ||u_q||_infinity^2
lesssim
U0^2 lambda_{R_Q}^3
lesssim
U0^2 Lambda^2.
```

Thus A2 already controls the lower two-thirds of the active logarithmic
frequency range. The only possible packet obstruction is

```math
B(t)={q: floor(2Q(t)/3)<q<=Q(t)}.
```

It is sufficient to prove, terminal-locally on high-`Lambda` times,

```math
integral sum_{q in B(t)} ||u_q||_infinity^2 dt < infinity.
```

Consequently any hypothetical A2 singularity must have this top-band integral
diverge on every terminal interval and every finite high-`Lambda` cutoff.

With `lambda_E=(nu/U0)^2`, define

```math
chi_q
=
||u_q||_infinity^2
/
(lambda_E lambda_q^2 ||u_q||_2^2),
qquad
d_q=nu lambda_q^2||u_q||_2^2.
```

Then exactly

```math
||u_q||_infinity^2=(lambda_E/nu) chi_q d_q.
```

The residual is therefore a dissipation-weighted concentration factor on the
top active band, not ordinary dissipation. At the threshold shell, the selector
gives the orientation

```math
V_Q=||u_Q||_2^2/||u_Q||_infinity^2
<=
c0^-2 lambda_E^-1 Lambda^-2,
```

so the missing theorem must prevent substantially stronger concentration in a
time-averaged/dissipation-weighted sense; it must not simply assert that the
active shell is concentrated.

The `r=infinity,D=1` Cheskidov--Peng intermittency expression has the same
Bernstein-saturation structure on the periodic forced problem. It is used only
as language and mechanism guidance, not imported as a theorem for the selected
whole-space unforced class.


### L5-15 C2 overshoot/persistence reduction

`work_packages/NS_CI_R014_A2_L5_15_C2_OVERSHOOT_PERSISTENCE_AUDIT.md`
records

```text
A2_LOW_COEFFICIENT_BELOW_FOUR_FIFTH_CONTROLLED
__RESIDUAL_IS_UPPER_FIFTH_THRESHOLD_OVERSHOOT
__TURNOVER_TIME_PERSISTENCE_INSUFFICIENT.
```

Let

```math
f(t)=sup_{p<=Q(t)} lambda_p ||u_p||_infinity
```

and `R_Q=floor(4Q/5)`. Energy plus Bernstein gives

```math
sup_{p<=R_Q} lambda_p ||u_p||_infinity
lesssim U0 Lambda^2,
```

so A2 already controls the lower four-fifths of the continuation coefficient.
The same exponent controls the corresponding far-low strain contribution.

For the remaining upper fifth define

```math
Omega(t)
=
sup_{R_Q<p<=Q}
lambda_p (||u_p||_infinity-c0 nu lambda_p)_+.
```

Then

```math
f(t)
lesssim
(U0+c0 nu)Lambda(t)^2 + Omega(t).
```

Hence `Omega in L1_t` is sufficient for continuation; any hypothetical A2
singularity must have divergent terminal `integral Omega`.

The reduction is sharper than the L5-14 packet target. Pointwise,

```math
Omega
<=
Lambda S_upper^(1/2),
```

so A2 plus the L5-14 packet estimate would imply the overshoot criterion.

A new exact scaling separator shows that ordinary nonlinear-turnover residence
still does not close the gap. With overshoot ratio `R`, frequency
`lambda=R^4`, amplitude `a=R lambda`, Bernstein-saturating energy
`E=R^2/lambda`, and duration

```math
Delta t=(lambda a)^(-1)=(R lambda^2)^(-1),
```

the A2 charge is `R^-1`, the dissipation charge is `R^-3`, but the
`Omega` charge tends to one. Therefore infinitely many increasing overshoot
excursions can have finite A2/energy/dissipation scalar budgets while
`integral Omega` diverges, even if each lasts a full turnover time. This is a
scaling fixture, not an NSE trajectory.

A successful dynamic persistence route must therefore beat turnover-time
cost, for example by proving parabolic-scale residence, a non-summable
overshoot-dependent A2 cost, cross-level coherence, or signed depletion.


### L5-16 same-band projected-forcing obstruction

`work_packages/NS_CI_R014_A2_L5_16_C2_SAME_BAND_MILD_OBSTRUCTION.md`
records

```text
SAME_BAND_LERAY_FORCING_ATTAINS_LAMBDA_A_SQUARED
__ABSOLUTE_MILD_ROUTE_STOPS_AT_TURNOVER_SCALE.
```

The exact divergence-free Fourier-algebra fixture

```math
u(x)
=
A(0,1,1)cos(Nx_1)
+
A(1,0,1)cos(Nx_2)
```

has input frequencies of magnitude `N` and target frequency
`(N,N,0)` of magnitude `sqrt(2)N`. Thus all participating modes lie in one
fixed-width frequency band.

The `sin(Nx_1+Nx_2)` coefficient of the raw convection term is

```math
-A^2N(1/2,1/2,1).
```

Leray projection at the target frequency removes exactly the horizontal
component and leaves

```math
-A^2N e_3.
```

Hence incompressibility, Leray projection, and same-band localization do not
supply any algebraic gain over the full nonlinear forcing scale

```math
lambda A^2.
```

For overshoot ratio

```math
R=A/(nu lambda),
```

the nonlinear scale is `R` times the representative viscous scale
`nu lambda^2 A`. A bare absolute mild estimate therefore controls amplitude
variation only on

```math
(lambda A)^(-1)
=
(R nu lambda^2)^(-1),
```

the nonlinear turnover scale. Over one parabolic interval
`(nu lambda^2)^(-1)`, the absolute nonlinear bound permits an `O(R A)`
change.

Combined with L5-15, which already proves turnover-time residence insufficient
against the A2 scalar budgets, this closes the bare fixed-shell
absolute-forcing persistence route.

The fixture is a Fourier-symbol/algebra obstruction, not an NSE trajectory.
It does not exclude parabolic residence obtained from genuinely dynamic
same-band depletion, phase decoherence, cross-level coherence, or signed
time-correlated flux information.


### L5-17 instantaneous cross-level coherence audit

`work_packages/NS_CI_R014_A2_L5_17_C2_INSTANTANEOUS_CROSS_LEVEL.md`
records

```text
SAME_BAND_NSE_RHS_ALLOWS_TURNOVER_RATE_WITH_STRICT_HIGH_INPUT_EMPTY
__INSTANTANEOUS_CROSS_LEVEL_REPAIR_BLOCKED.
```

Extend the L5-16 source pair by an active target mode:

```math
u_sigma
=
A(0,1,1)cos(Nx_1)
+
sigma A(1,0,1)cos(Nx_2)
+
C e_3 sin(Nx_1+Nx_2),
```

with `sigma=+/-1`. All initial Fourier support lies at frequencies
`N,N,sqrt(2)N`; there is no input frequency above the target.

The target projected nonlinear coefficient remains exactly

```math
-sigma A^2 N e_3.
```

Hence the exact target NSE coefficient derivative is

```math
Cdot
=
-2 nu N^2 C
+
sigma A^2 N.
```

Setting `A=C=R nu N` gives

```math
Cdot/C
=
nu N^2(-2+sigma R).
```

For large `R`, the target is a genuine threshold overshoot and can have
either growth or decay at turnover rate while every strict-high input mode is
zero. Flipping `sigma` changes the nonlinear target derivative sign without
changing support or modal energies.

Therefore rapid active-shell variation does not instantaneously force
strict-high activity. Any valid cross-level repair must be time-correlated:
delayed strict-high charge, repeated-transfer decoherence, cumulative signed
flux, or another non-summable temporal cost.


### L5-18 exact 2.5D temporal leakage calibration

work_packages/NS_CI_R014_A2_L5_18_C2_TEMPORAL_LEAKAGE.md records

EXACT_2P5D_NSE_EMBEDDING_PROVED__FINITE_DISTANCE_TEMPORAL_SPECTRAL_LEAKAGE_PROVED__LEAKAGE_AMPLITUDE_NOT_THRESHOLD_CHARGE.

The sigma=+1 L5-17 snapshot embeds into an exact smooth unforced periodic
2.5D NSE trajectory.  The horizontal flow

$
v(t)=A e^{-\nu N^2 t}(\cos(Nx_2),\cos(Nx_1))
$

has projected horizontal convection zero, while the vertical component obeys
linear advection-diffusion.

If W_{m,n} denotes its vertical Fourier coefficient on N(m,n,0), then

$
\dot W_{m,n}
=
-\nu N^2(m^2+n^2)W_{m,n}
-\frac{iNa(t)}2
[
m(W_{m,n-1}+W_{m,n+1})
+
n(W_{m-1,n}+W_{m+1,n})
].
$

Starting from the active target W_{1,1}(0)=-iC/2, the mode
N(r+1,1,0) has no nonzero derivative before order r and satisfies

$
W_{r+1,1}^{(r)}(0)
=
(-i)^{r+1}\frac{C(NA)^r}{2^{r+1}}.
$

Thus every fixed finite spectral distance has a nonzero first-possible
temporal jet in an actual NSE calibration.  However, the corresponding leading
physical Taylor term is

$
C\frac{(NAt)^r}{2^r r!},
$

so at the nominal turnover scale its leading coefficient carries the factorial
penalty 1/(2^r r!).  Nonzero support therefore does not by itself yield a
strict-high shell lower bound, a threshold violation, or a non-summable A2
charge.

The temporal-coherence frontier is narrowed from support leakage to
quantitative amplitude leakage.


### L5-19 fixed-distance threshold leakage calibration

`work_packages/NS_CI_R014_A2_L5_19_C2_FIXED_DISTANCE_AMPLITUDE.md`
records

```text
FIXED_DISTANCE_THRESHOLD_LEAKAGE_PROVED_IN_2P5D_CALIBRATION
__FIXED_DISTANCE_CHARGE_CERTIFICATE_REMAINS_R_INVERSE.
```

L5-18's nonzero temporal jets can be upgraded to a genuine finite-time
amplitude statement at every fixed spectral distance.  With
`A=R nu N`, turnover variables

```math
tau=ANt,
qquad
epsilon=nu N/A=1/R
```

reduce the vertical equation to

```math
partial_tau theta_epsilon
+
e^{-epsilon tau} V dot grad theta_epsilon
=
epsilon Delta theta_epsilon.
```

On every fixed turnover-time interval, `theta_epsilon` converges in `L2`
to the smooth inviscid transport solution at rate `O(1/R)`.  Since the
transport coefficient at every fixed lattice distance `r` has a nonzero
first possible derivative, one obtains a fixed interval `I_r` and
`b_r>0` on which the corresponding finite-`R` coefficient is bounded
below by `b_r` for all sufficiently large `R`.

Choose one finite `r_*`, depending only on the fixed LP annulus width, so
that the generated frequency lies beyond every dyadic shell meeting the
initial three-mode support.  Finite LP overlap then forces one generated block
to satisfy

```math
lambda_p^{-1} ||u_p||_infinity >= c_r R nu,
```

and hence to violate the campaign threshold for sufficiently large `R`.
Thus threshold-sized temporal leakage is proved in the exact periodic 2.5D
calibration.

However, the guaranteed selector charge over that fixed turnover-time
interval is only

```math
integral Lambda^2 dt
>=
C_{r_*}/(R nu).
```

For fixed `r_*` this retains the inverse-overshoot summability defect.
A charge-only repair from spectral propagation would require threshold-sized
distance `r(R) comparable to at least sqrt(R)`, or an equivalent cumulative
flux/decoherence cost.  No such growing-distance theorem is claimed here.


### L5-20 Sobolev tail bound on threshold-reaching distance

`work_packages/NS_CI_R014_A2_L5_20_C2_DISTANCE_SOBLEV_TAIL.md`
records

```text
C2_DIST_SQRT_R_THRESHOLD_REACH_EXCLUDED_IN_2P5D_CALIBRATION
__TURNOVER_SELECTOR_CHARGE_VANISHES.
```

L5-19 asked whether threshold-sized leakage in the exact periodic 2.5D
calibration could reach distance comparable to `sqrt(R)`, which would be
needed for an order-one charge from propagation distance alone.

The uniform finite-time Sobolev estimate already available in L5-19 answers
this negatively.  Because the calibration is independent of `x_3`, one
dyadic annulus contains only `O(L^2)` normalized lattice modes.  For every
fixed Sobolev order `s>=4`,

```math
||Delta_p theta_{1/R}||_infinity
lesssim
L_p^(1-s),
```

where `L_p=lambda_p/N`.  Since `A=R nu N`,

```math
lambda_p^(-1)||u_p||_infinity
lesssim
R nu L_p^(-s).
```

Hence every threshold-violating shell on a fixed turnover-time interval obeys

```math
lambda_p/N
lesssim
R^(1/s).
```

Taking `s=4` gives only fourth-root reach, strictly below the required
square-root scale.  The selector itself satisfies

```math
Lambda(t)
lesssim
N R^(1/s),
```

so over a fixed turnover-time horizon

```math
integral Lambda^2 dt
lesssim
nu^(-1) R^(2/s-1).
```

At `s=4` this is `O(nu^(-1)R^(-1/2))` and tends to zero.

Thus spectral-distance propagation is closed as the missing charge mechanism
inside this exact calibration.  This is not a whole-space A2 theorem.


### L5-21 cumulative upper-band flux obstruction

\`work_packages/NS_CI_R014_A2_L5_21_C2_CUMULATIVE_FLUX_OBSTRUCTION.md\`
records

\`\`\`text
C2_FLUX_GENERIC_BAND_ENERGY_ROUTE_TERMINATED
__OVERSHOOT_DIVERGES_WITH_SUMMABLE_BOUNDARY_FLUX.
\`\`\`

The first selector-free cumulative-flux repair is insufficient even after
granting exact complete-band telescoping.

A conservative nearest-neighbour shell-and-packet ledger uses the protected
L5-15 episode scaling

\`\`\`math
R_n=2^n,\qquad
lambda_n=R_n^4,\qquad
E_n=R_n^{-2},\qquad
delta_n=R_n^{-9}.
\`\`\`

On each disjoint episode, the active-shell energy obeys an exact shell balance
with a reservoir and one signed boundary flux. Internal band edges telescope
exactly. The net boundary flux equals the episode dissipation and scales like

\`\`\`math
R_n^{-3}.
\`\`\`

Even the absolute unweighted boundary-flux variation is only

\`\`\`math
O(R_n^{-2}+R_n^{-3}),
\`\`\`

and remains summable after multiplying by the number \`q_n=4n\` of
nearest-neighbour edges.

At the same time the A2 occupancy charge is \`O(R_n^{-1})\`, total dissipation
is summable, total energy is bounded, and the turnover-scale energy-transfer
rate is respected. But on the plateau,

\`\`\`math
integral_{I_n} Omega(t) dt
gtrsim
1-c_0/R_n,
\`\`\`

so the overshoot integral diverges.

Thus exact fixed-band energy conservation, signed cumulative boundary flux,
and even finite absolute unweighted flux variation do not control the L5-15
overshoot residual from the selected scalar budgets.

This does not exclude an equation-specific triadic coherence or
frequency-weighted flux theorem. The fixture is an exact conservative shell
ledger, not a Navier--Stokes trajectory.


### L5-22 turnover-scale signed transfer coherence calibration

\`work_packages/NS_CI_R014_A2_L5_22_C2_TRIAD_COHERENCE.md\`
records

\`\`\`text
TURNOVER_SCALE_SIGNED_TRANSFER_COHERENCE_PERSISTS_IN_EXACT_2P5D_NSE
__SUBTURNOVER_DECOHERENCE_NOT_GENERIC.
\`\`\`

The exact unforced periodic 2.5D NSE calibration from L5-18/L5-19 also
separates a generic phase-decoherence repair.

In turnover variables,

\`\`\`math
partial_tau theta_epsilon
+
e^{-epsilon tau} V dot grad theta_epsilon
=
epsilon Delta theta_epsilon,
\qquad
epsilon=1/R.
\`\`\`

Let \`c_epsilon\` be the target \`sin(X+Y)\` coefficient and
\`g_epsilon\` its signed nonlinear transport forcing.  Exactly,

\`\`\`math
c_epsilon'
=
g_epsilon-2epsilon c_epsilon,
\qquad
c_epsilon(0)=g_epsilon(0)=1.
\`\`\`

The L5-19 uniform high-Sobolev bounds upgrade the inviscid-limit convergence to

\`\`\`math
sup_{tau<=T}
||theta_epsilon-theta_0||_{H^s}
lesssim
epsilon.
\`\`\`

Since the inviscid target amplitude and forcing are both positive at
\`tau=0\`, continuity gives one fixed \`tau_*>0\` such that for all
sufficiently large \`R\`,

\`\`\`math
c_{1/R}(tau)>=1/2,
\qquad
g_{1/R}(tau)>=1/2
\`\`\`

throughout \`0<=tau<=tau_*\`.

Thus the signed nonlinear transfer into the target sine component remains
order \`A^3N\` for physical time \`tau_*/(AN)\`, giving an order-\`A^2\`
coherent transfer.  The corresponding viscous target loss is smaller by
\`O(1/R)\`.

Combined with L5-20, the same calibration can therefore have fixed-turnover
signed transfer coherence while its fixed-window selector charge tends to
zero.  Universal subturnover phase decoherence is not the missing C2
mechanism.

This remains a periodic 2.5D calibration theorem.  It does not prove repeated
episode coherence or a selected whole-space statement.


### L5-23 exact viscous shear-chain phase locking

\`work_packages/NS_CI_R014_A2_L5_23_C2_SHEAR_PHASE_LOCK.md\`
records

\`\`\`text
EXACT_VISCOUS_SHEAR_CHAIN_QUADRATURE_LOCKING_PROVED
__PHASE_DECOHERENCE_ABSENT_IN_CALIBRATION.
\`\`\`

A second exact unforced periodic 2.5D calibration removes generic phase-reset
cost more strongly.

For the decaying shear

\`\`\`math
v=(A e^{-nu N^2t}\cos(Nx_2),0),
\`\`\`

the vertical component obeys passive advection-diffusion.  In turnover
variables, the complex \`X\)-frequency-one chain satisfies

\`\`\`math
a_n'
=
-\frac{i}{2}e^{-epsilon tau}(a_{n-1}+a_{n+1})
-
epsilon(1+n^2)a_n.
\`\`\`

The phase sector

\`\`\`math
a_n=(-i)^n b_n,\qquad b_n\in R
\`\`\`

is exactly invariant, because the \`b_n\` satisfy a real nearest-neighbour
system.

Hence every adjacent nonzero pair remains exactly in quadrature:

\`\`\`math
Re(conj(a_n)a_{n+1})=0,
\qquad
|Im(conj(a_n)a_{n+1})|
=
|a_n||a_{n+1}|.
\`\`\`

Viscosity damps amplitudes but does not rotate this phase lattice.  Transfer
direction may reverse when a real amplitude crosses zero, without gradual
phase decorrelation.

At \`epsilon=0\` the chain is explicit:

\`\`\`math
a_n(tau)=(-i)^n J_n(tau).
\`\`\`

Thus the repeated-event residual cannot be charged generically to phase
decoherence itself.  Any remaining cost must arise from amplitude decay,
enhanced dissipation, rebuilding amplitudes after zero crossings, memory in
generated modes, or genuinely three-dimensional interactions.


### L5-24 shear-chain mixing-diffusion moment ceiling

`work_packages/NS_CI_R014_A2_L5_24_C2_MIX_MOMENT_CEILING.md`
records

```text
SHEAR_CHAIN_R_ONE_THIRD_MOMENT_CEILING_PROVED
__SUBCUBIC_TURNOVER_SELECTOR_CHARGE_VANISHES.
```

The exact L5-23 shear chain admits an all-time finite-viscosity moment barrier.
After factoring the fixed `X\)-frequency-one mode, its scalar equation is

```math
partial_tau phi_epsilon
+
i e^{-epsilon tau} cos(Y) phi_epsilon
=
epsilon (partial_Y^2-1) phi_epsilon.
```

For every fixed integer `s>=0`,

```math
sup_{tau>=0}
||partial_Y^s phi_epsilon||_2
<=
C_s epsilon^{-s/3}.
```

The proof uses the exact differentiated energy identity, the commutator with
`cos Y`, Fourier interpolation
`X_{s+1}>=X_s^(1+1/s)`, and an inductive barrier. The cubic-root exponent is
the balance between one derivative of shear production and two derivatives of
viscous damping.

The one-chain Fourier support intersects a dyadic annulus of normalized radius
`L=lambda_p/N` in only `O(L)` modes. Consequently

```math
lambda_p^{-1}||u_p||_infinity
<=
C_s nu
epsilon^{-(1+s/3)}
L^{-(s+1/2)}.
```

Every threshold-violating shell therefore satisfies

```math
lambda_p/N
<=
C_s R^{alpha_s},
\qquad
alpha_s
=
1/3+5/(6s+3).
```

At `s=5`, `alpha_5=16/33<1/2`. More generally, for every fixed
`delta>0`,

```math
Lambda(t)
<=
C_delta N R^{1/3+delta}
```

for all time in this calibration.

On a normalized turnover window `0<=tau<=T_R`,

```math
integral Lambda^2 dt
<=
C_delta nu^{-1}
T_R R^{-1/3+2delta}.
```

Thus every subcubic window `T_R<=R^{1/3-eta}` has vanishing selector charge
for fixed `eta>0` after choosing `delta<eta/2`.

This is an upper-reach theorem only. It does not prove threshold-sized
amplitude near the cubic-root front.


### L5-25 subcritical cubic-root threshold propagation

`work_packages/NS_CI_R014_A2_L5_25_C2_MIX_SUBCRITICAL_LOWER.md`
records

```text
SHEAR_CHAIN_SUBCRITICAL_CUBIC_ROOT_THRESHOLD_PROPAGATION_PROVED
__CRITICAL_WINDOW_REMAINS_OPEN.
```

L5-24 gives the upper threshold-reach exponent. L5-25 proves the matching
lower reach below the exact cubic-root scale.

For every fixed

```math
0<beta<1/3,
\qquad
T_R=R^beta,
```

the exact finite-viscosity shear chain has a fixed positive amount of Fourier
mass in

```math
tau/2<=|n|<=2tau
```

uniformly for every `tau\in[T_R,2T_R]`, once `R` is sufficiently large.

The proof uses:

- exact inviscid moments
  `sum n^2|J_n|^2=tau^2/2` and
  `sum n^4|J_n|^2=tau^2/2+3tau^4/8`;
- Paley--Zygmund plus Markov, giving inviscid band mass at least
  `15/896`;
- finite-time derivative bounds
  `||partial_Y^s phi_epsilon||_2<=C_s(1+tau)^s`;
- the growing-window comparison
  `||phi_epsilon-phi_0||_2<=C epsilon(1+tau)^3`,
  which is `o(1)` uniformly for `tau<=2R^beta` whenever `beta<1/3`.

Since the band contains only `O(tau)` modes, one coefficient has magnitude at
least `c tau^{-1/2}`. A nearby LP block therefore satisfies

```math
lambda_p^{-1}||u_p||_infinity
>=
c nu R tau^{-3/2},
```

so it violates the threshold throughout the moving interval. Consequently

```math
Lambda(t)
>=
c N R^beta
```

there, and

```math
integral Lambda^2 dt
>=
c nu^{-1}R^{3beta-1}.
```

The charge still tends to zero for every fixed `beta<1/3`.

Together with L5-24, threshold reach in this calibration is pinned in
power-law exponent to `R^{1/3+o(1)}`. The exact critical
`tau~R^{1/3}` window remains unresolved because the elementary viscous-to-
inviscid comparison error becomes order one precisely there.


### L5-26 critical shear-chain semiclassical mass survival

`work_packages/NS_CI_R014_A2_L5_26_C2_MIX_CRITICAL_SEMICLASSICAL.md`
records

```text
SHEAR_CHAIN_CRITICAL_SEMICLASSICAL_MASS_SURVIVAL_PROVED
__UNIFORM_POSITIVE_SELECTOR_CHARGE_LOWER_BOUND.
```

L5-26 resolves the exact cubic-root window left open by L5-24/L5-25.

Set

```math
h=R^{-1/3},
\qquad
epsilon=h^3,
\qquad
s=h tau.
```

After exact removal of the rapid shear phase,

```math
Phi_h
=
e^{-iq_h(s)cosY}A_h,
\qquad
q_h=h^{-3}(1-e^{-h^2s}),
```

the demodulated amplitude converges strongly on fixed critical intervals to

```math
A_0(s,Y)
=
exp(-s^3 sin^2Y/3).
```

The limit has nondegenerate scaled second and fourth Fourier moments. On the
fixed interval `1<=s<=2`, Paley--Zygmund and Markov applied to the normalized
finite-`h` Fourier distribution therefore give fixed positive mass in

```math
c_-<=|hn|<=c_+.
```

Since this band contains only `O(h^{-1})` modes, one coefficient satisfies

```math
|a_n|>=c h^{1/2}.
```

A nearby LP block at physical frequency `NR^{1/3}` then violates the
strict-high threshold by a factor growing like `h^{-3/2}`. Thus

```math
Lambda(t)
>=
c N R^{1/3}
```

throughout the whole critical interval.

Because

```math
dt=h^2 (nu N^2)^{-1} ds,
```

the interval carries the uniform positive selector charge

```math
integral Lambda^2 dt
>=
c_*/nu.
```

This is a calibration theorem only. It shows that the exact phase-locked shear
mechanism produces a genuine nonvanishing critical scale cost, but it does not
show that every selected whole-space upper-band overshoot contains such a
mixing packet.


### L5-27 critical shear-packet normal-form bridge

`work_packages/NS_CI_R014_A2_L5_27_C2_MIX_BRIDGE_NORMAL_FORM.md`
records

```text
CRITICAL_SHEAR_PACKET_NORMAL_FORM_BRIDGE_PROVED
__WHOLE_SPACE_DERIVATION_REMAINS_OPEN.
```

L5-26's critical charge is structurally stable under a selector-free local
packet normal form.  After critical normalization, suppose one packet
component obeys

```math
partial_s Phi_h
+
i h^{-1} a_h(s) g(Y) Phi_h
=
h^2(partial_Y^2-1)Phi_h
+
r_h,
```

with:

- a fixed smooth transverse phase `g` whose gradient is nonzero on initial
  packet mass;
- `a_h=1+O(h^2)`;
- `O(h)` demodulated initial perturbation;
- `O(h)` demodulated residual in fixed-window `L^2_s H^k`;
- uniform physical reconstruction of packet coefficients into LP blocks.

Exact phase removal gives the universal critical limit

```math
A_0(s,Y)
=
A_in(Y)
exp(-s^3 |g'(Y)|^2/3).
```

Its scaled second moment is uniformly positive on compact positive critical
intervals.  Strong demodulated convergence therefore yields fixed positive
finite-`h` mass at `|n|\asymp h^{-1}`, a threshold-violating physical block
at `NR^{1/3}`, and

```math
integral Lambda^2 dt
>=
c_*/nu.
```

Thus the critical mixing cost does not depend on the cosine profile, exact
phase locking, zero residual, or an exact passive-scalar reduction.

The theorem remains conditional: the normal-form hypotheses have not been
derived from an arbitrary selected whole-space upper-band overshoot.


### L5-28 semiclassical residual weakening and NF4 depletion scale

`work_packages/NS_CI_R014_A2_L5_28_C2_MIX_SEMICLASSICAL_RESIDUAL.md`
records

```text
SEMICLASSICAL_BRIDGE_RESIDUAL_WEAKENING_PROVED
__ABSOLUTE_NF4_DERIVATION_REQUIRES_R_TWO_THIRDS_DEPLETION.
```

The ordinary demodulated `H^k` residual in L5-27 is stronger than the
critical moment argument intrinsically needs.  Introduce

```math
||f||_{H_h^2}^2
=
sum_{j=0}^2||(h partial_Y)^j f||_2^2.
```

Using the covariant operator

```math
C_h=h partial_Y-i p_h g',
\qquad
L_h=C_h^2-h^2,
```

the L5-27 stability argument closes with `O(h)` initialization and residual
only in the semiclassical `H_h^2` norm.  The scaled second and fourth Fourier
moments still converge, so the conditional critical `c_*/nu` selector charge
is unchanged.

This eliminates rapid demodulation frequency as the material bridge
obstruction.

Under active-scale normalization the turnover equation has an order-one
quadratic nonlinearity.  Critical time `s=h tau` makes a generic
nonprincipal same-band interaction order `h^{-1}`, while NF4-sc requires an
`O(h)` residual.  Thus the actual required relative depletion is

```math
h^2=R^{-2/3}.
```

Protected L5-16 proves that incompressibility, Leray projection, fixed-width
same-band localization, and amplitude information alone permit the full
physical forcing scale `A^2N`.  Hence those absolute algebraic ingredients
cannot supply the required `R^{-2/3}` factor.

The residual derivation problem is therefore now a genuine dynamic/geometric
depletion problem, not a Sobolev bookkeeping problem.


### L5-29 exact same-band polarization corridor

`work_packages/NS_CI_R014_A2_L5_29_C2_POLARIZATION_CORRIDOR.md`
records

```text
SAME_BAND_POLARIZATION_NULL_FACTOR_EXACT
__R_TWO_THIRDS_ALIGNMENT_NOT_FORCED_POINTWISE.
```

For orthogonal source frequencies and unit divergence-free polarizations

```math
a_alpha=(0,cos(alpha),sin(alpha)),
\qquad
b_beta=(cos(beta),0,sin(beta)),
```

the exact Leray-projected sum-frequency interaction is

```math
P_{k_1+k_2}(u dot grad u)
=
-(A^2N/2) sin(alpha+beta) e_3
```

at the target phase.

The source support, source modal amplitudes, and source shell energies are
independent of `alpha,beta`, while the projected forcing ranges continuously
from exact zero to the full order-`A^2N` scale and reverses sign.

Combining with L5-28, if this interaction belongs to the nonprincipal bridge
residual then NF4 requires

```math
|sin(alpha+beta)|
lesssim
h^2
=
R^{-2/3}.
```

Near the null set this is an `O(R^{-2/3})` polarization corridor.

Thus A2, shell energy, support, and amplitude data cannot force the required
pointwise alignment.  Any successful depletion route must be time-correlated
or use genuinely additional geometric information.


### L5-30 polarization defect as an exact secondary shear charge

`work_packages/NS_CI_R014_A2_L5_30_C2_SECONDARY_SHEAR_CHARGE.md`
records

```text
EXACT_SECONDARY_SHEAR_CHARGE_PROVED
__R_SQUARED_DELTA_DIVERGENCE_FORCES_C_OVER_NU.
```

A one-parameter subfamily of the L5-29 polarization fixture is an exact smooth
unforced periodic 2.5D NSE trajectory.

Let `delta` be the L5-29 polarization defect and

```math
rho=R delta.
```

Then `A delta` is exactly the amplitude of a decaying horizontal shear acting
on a vertical carrier of amplitude `A`.

For bounded effective shear `rho`, a short parabolic-time Duhamel estimate
produces a neighboring Fourier coefficient of size `c rho A`.  It violates
the threshold whenever

```math
R rho=R^2 delta -> infinity,
```

and persists on a fixed fraction of a parabolic interval, giving selector
charge `c/nu`.

For large `rho`, protected L5-26 applies with `rho` as the effective shear
Reynolds number.  Its critical front at `N rho^(1/3)` again gives charge
`c/nu`.

Therefore

```math
R^2 delta -> infinity
\quad=>\quad
integral Lambda^2 dt >= c/nu
```

in this exact calibration family.

Thus a channel too large to ignore need not be depleted; if it has coherent
shear structure it can be promoted to a secondary principal mixing channel and
pay the critical cost itself.  The exact calibration leaves unresolved only
`R^2 delta=O(1)`, i.e. `delta=O(R^-2)`, as a sufficient-condition boundary.


### L5-31 finite coherent transverse shear family

`work_packages/NS_CI_R014_A2_L5_31_C2_GENERAL_SHEAR_PROFILE.md`
records

```text
FINITE_COHERENT_SHEAR_FAMILY_COLLAPSES_TO_ONE_PROFILE
__R_SQUARED_DELTA_CHARGE_PERSISTS.
```

Any fixed finite family of same-direction transverse Fourier shears is exactly
one real trigonometric profile `G(Y)` evolving by the one-dimensional heat
semigroup.

For a horizontal shear amplitude fraction `delta`, define

```math
rho=R delta.
```

An exact vertical carrier under this generalized shear obeys passive
advection-diffusion.

For bounded `rho`, any fixed nonzero Fourier coefficient of `G` generates a
neighboring carrier coefficient of order `rho` on a fixed parabolic-time
interval. Thus `R^2 delta->infinity` gives a threshold violation and
`c_G/nu` selector charge.

For large `rho`, set `h=rho^-1/3` and `s=h tau`. The heat-evolving profile
freezes critically:

```math
G_h(s)=G+O(h^2).
```

Exact time-dependent phase removal yields the limit

```math
A_0(s,Y)
=
exp(-s^3 |G'(Y)|^2/3).
```

Every nonconstant fixed profile has positive scaled critical Fourier variance,
so positive mass reaches `|n|\asymp rho^(1/3)` and again pays
`c_G/nu` selector charge.

Therefore

```math
R^2 delta->infinity
\quad=>\quad
integral Lambda^2 dt >= c_G/nu
```

for every fixed nonconstant coherent profile.

Finite coherent same-direction channels do not need separate overlapping
charge ledgers; they collapse to one generalized phase. The remaining
whole-space issue is extracting a coherent profile over the critical interval.


### L5-32 time-dependent transverse-profile bridge

`work_packages/NS_CI_R014_A2_L5_32_C2_ACCUMULATED_PHASE.md`
records

```text
TIME_DEPENDENT_TRANSVERSE_PROFILE_BRIDGE_PROVED
__ACCUMULATED_PHASE_GRADIENT_IS_CRITICAL_INVARIANT.
```

For the critical normal form

```math
Phi_s+i h^{-1}G_h(s,Y)Phi
=
h^2(D_Y^2-1)Phi+r_h,
```

define the accumulated transverse phase

```math
F_h(s,Y)=int_0^s G_h(sigma,Y) dsigma.
```

Exact phase removal by `exp(-iF_h/h)` cancels the entire fast potential.
The demodulated equation depends on `F_h`, not directly on the instantaneous
profile `G_h`.

If

```math
F_h=F_0+O(h)
```

in a fixed spatial smooth norm, with the L5-28 `O(h)` semiclassical residual,
then

```math
A_h->A_0,
\qquad
A_0
=
exp(
-int_0^s |(F_0)_Y(sigma,Y)|^2 dsigma
)
```

at `O(h)` in `H_h^2`.

The scaled moments satisfy

```math
h^2 sum n^2|c_n|^2
->
||(F_0)_Y A_0||_2^2,
```

and

```math
h^4 sum n^4|c_n|^2
->
||(F_0)_Y^2 A_0||_2^2.
```

Thus any fixed critical interval on which
`||(F_0)_Y A_0||_2` is uniformly positive has positive critical-band mass and
the same `c/nu` selector charge.

Small instantaneous profile drift is not required.  For example,

```math
G_h=G_0+sin(s/h)H
```

has order-one instantaneous drift but only `O(h)` accumulated-phase error.

The remaining coherence problem is therefore directional: extract one common
transport direction/transverse coordinate and a nondegenerate accumulated
phase from selected whole-space active-band dynamics.


### L5-33 transverse direction-defect corridor

`work_packages/NS_CI_R014_A2_L5_33_C2_DIRECTION_DEFECT.md`
records

```text
TRANSVERSE_DIRECTION_DEFECT_AS_RESIDUAL_REQUIRES_H_CUBED
__LARGER_DEFECT_MUST_BE_PROMOTED_OR_CHARGED.
```

Model a transport-direction defect in the critical packet equation by the
transverse derivative leakage

```math
D_h Phi_h
=
h^{-1} theta_h(s) B_h(s,Y) partial_Y Phi_h.
```

After the L5-32 phase removal,

```math
widetilde D_h
=
h^{-1}theta_hB_h partial_Y A_h
-
i h^{-2}theta_h B_h(F_h)_Y A_h.
```

Define

```math
Z_h
=
hB_h partial_Y A_h
-
iB_h(F_h)_Y A_h.
```

Then exactly

```math
widetilde D_h
=
h^{-2}theta_h Z_h.
```

If the direction term is assigned to the protected NF4 residual, its L2
component must satisfy

```math
||theta_h Z_h||_{L2_{s,Y}}
=
O(h^3).
```

Under uniform nondegenerate limiting coupling

```math
inf_s ||B_0(F_0)_Y A_0||_2
>=
c_dir>0,
```

L5-32 gives `inf_s||Z_h(s)||_2>=c_dir/2` for small `h`. Hence

```math
||theta_h||_{L2_s}
=
O(h^3).
```

For a persistent approximately constant direction error,

```math
|theta_h|
lesssim
h^3
=
rho^{-1}.
```

Thus a nondegenerately coupled direction defect larger than the
`rho^{-1}` corridor cannot be hidden inside the L5-28 residual.  It must be
promoted into principal critical dynamics, shown to cancel by additional
structure, or charged independently.

This tranche does not yet prove that larger direction drift pays a selector
charge.


### L5-34 uniform direction motion as principal moving-frame dynamics

`work_packages/NS_CI_R014_A2_L5_34_C2_DIRECTION_MOVING_FRAME.md`
records

```text
UNIFORM_DIRECTION_MOTION_REMOVED_BY_EXACT_MOVING_FRAME
__LAGRANGIAN_ACCUMULATED_PHASE_CONTROLS_CHARGE.
```

L5-33's `h^3=rho^-1` direction corridor applies only when a transverse
direction term is assigned to the protected residual.

For principal spatially uniform direction motion,

```math
partial_s Phi_h
+
h^-1 theta_h(s) partial_Y Phi_h
+
i h^-1 G_h(s,Y) Phi_h
=
h^2(partial_Y^2-1)Phi_h
+
r_h,
```

define

```math
Gamma_h(s)
=
h^-1 int_0^s theta_h(sigma) dsigma.
```

The translation

```math
Psi_h(s,Y)
=
Phi_h(s,Y+Gamma_h(s))
```

removes the derivative term exactly, preserves `H_h^2`, and preserves every
Fourier coefficient magnitude.

The resulting L5-32 phase is the moving-frame accumulated phase

```math
Fcal_h(s,Y)
=
int_0^s
G_h(sigma,Y+Gamma_h(sigma))
dsigma.
```

If `Fcal_h=Fcal_0+O(h)` in the protected smooth norm and the limiting
accumulated phase gradient is nondegenerate, the L5-32 critical band and
`c/nu` selector-charge theorem survive with no smallness assumption on the
rigid direction speed.

Direction magnitude alone does not imply mixing.  For
`G=cos Y` and constant nonzero `theta`,

```math
Fcal_h
=
(h/theta)
[
sin(Y+theta s/h)-sin Y
]
=
O(h),
```

so the limiting accumulated phase is zero and the protected critical moment
lower mechanism degenerates.

For nonuniform principal direction motion
`h^-1 theta_h B_h(s,Y) partial_Y`, the characteristic Jacobian satisfies

```math
partial_s J_h
=
h^-1 theta_h
(partial_Y B_h)(s,chi_h)
J_h.
```

Thus the moving frame is no longer automatically isometric and diffusion
acquires a variable metric.  This is the next direction-coherence boundary.


### L5-35 bounded nonuniform direction-frame deformation

`work_packages/NS_CI_R014_A2_L5_35_C2_DIRECTION_DEFORMED_FRAME.md`
records

```text
BOUNDED_NONUNIFORM_FRAME_DEFORMATION_PRESERVES_CRITICAL_MIXING
__ABSOLUTE_DIRECTION_STRAIN_BUDGET_IS_H_SCALE.
```

L5-34 removes rigid direction motion exactly.  L5-35 extends the principal
moving-frame theorem to one-dimensional nonuniform direction fields whose
characteristic maps remain uniformly smooth and bi-Lipschitz.

For

```math
partial_s Phi_h
+
h^-1 theta_h(s) B_h(s,Y) partial_Y Phi_h
+
i h^-1 G_h(s,Y) Phi_h
=
h^2(partial_Y^2-1)Phi_h+r_h,
```

let `chi_h` be the direction-flow map and `J_h=partial_Z chi_h`.
Pullback gives the exact diffusion metric

```math
partial_Y^2
->
J_h^-2 partial_Z^2
-
J_h^-3 (J_h)_Z partial_Z.
```

After exact accumulated-phase removal along characteristics, the leading
critical damping is

```math
-
J_h^-2 |(Fcal_h)_Z|^2.
```

Under uniform smooth bi-Lipschitz frame bounds, `O(h)` convergence of the
metric and Lagrangian accumulated phase, and the protected `O(h)`
semiclassical residual, the limiting amplitude is

```math
A_0
=
exp(
-
int J_0^-2 |(Fcal_0)_Z|^2 ds
).
```

The physical scaled Fourier moments satisfy

```math
h^2 sum n^2 |c_n|^2
->
int J_0^-1 |(Fcal_0)_Z A_0|^2 dZ
```

and

```math
h^4 sum n^4 |c_n|^2
->
int J_0^-3 |(Fcal_0)_Z|^4 |A_0|^2 dZ.
```

Metric-weighted second-moment nondegeneracy therefore preserves positive
physical critical-band mass and the `c/nu` selector charge.

The exact Jacobian equation is

```math
J_s
=
h^-1 theta_h B_Y(s,chi_h) J.
```

Hence the absolute budget

```math
h^-1
int
|theta_h|
||B_h||_{W^{4,infinity}}
ds
<=
C
```

is a sufficient route to bounded finite-order frame geometry.  For persistent
order-one spatial direction gradients this asks for the sufficient scale
`|theta_h|=O(h)=O(rho^-1/3)`, much wider than L5-33's residual
`O(h^3)` corridor.

This scale is not claimed necessary.  Signed or oscillatory characteristic
strain may cancel.

The exact separator `B(Y)=sin Y`, constant positive `theta`, has
`J_h(s,0)=exp(theta s/h)`, showing that order-one nonuniform direction strain
can create exponential critical-time frame distortion.


### L5-36 separable direction strain and signed flow time

`work_packages/NS_CI_R014_A2_L5_36_C2_DIRECTION_SIGNED_FLOW_TIME.md`
records

```text
SEPARABLE_DIRECTION_STRAIN_REDUCES_TO_SIGNED_FLOW_TIME
__ABSOLUTE_H_SCALE_NOT_NECESSARY.
```

For separable principal direction fields

```math
h^-1 theta_h(s) B(Y) partial_Y,
```

the full characteristic geometry factors through one signed flow clock

```math
kappa_h(s)
=
h^-1 int_0^s theta_h(sigma) dsigma.
```

If `varphi_kappa` is the autonomous flow of `B`, then exactly

```math
chi_h(s,Z)
=
varphi_{kappa_h(s)}(Z).
```

Thus bounded signed flow time gives bounded finite-order characteristic
geometry, and `kappa_h=kappa_0+O(h)` gives the O(h) metric convergence
required by L5-35.  Smooth Eulerian phase convergence then gives the same O(h)
Lagrangian accumulated-phase convergence.

This sharply improves the absolute L5-35 sufficient budget.

For

```math
theta_h(s)=sin(s/h^2),
```

one has

```math
kappa_h(s)
=
h[1-cos(s/h^2)]
=
O(h),
```

while

```math
h^-1 int_0^S |theta_h(s)| ds
asymp
h^-1
->
infinity.
```

Hence order-one rapidly oscillating direction strain can produce an
O(h)-near-identity frame and remain compatible with the protected critical
charge theorem for a fixed nondegenerate scalar phase.

For `B(Y)=sin Y`, the autonomous flow is explicit:

```math
tan(varphi_kappa(Z)/2)
=
e^kappa tan(Z/2),
```

with fixed-point Jacobians

```math
partial_Z varphi_kappa(0)=e^kappa,
\qquad
partial_Z varphi_kappa(pi)=e^-kappa.
```

Thus signed flow time directly controls exponential deformation in this
separator.

The unresolved geometry is genuinely time-dependent
`B_h=B_h(s,Y)`, where different spatial vector fields need not commute and
no single scalar signed clock captures the time-ordered flow.

## Residual blockers

- B1 low core: moving enstrophy hits B4; selector-free complementary coupling
  returns the closed L4 weighted column.
- B2 near threshold: no standalone blocker in the pointwise L5 decomposition;
  dynamic finite-neighbour terms can still occur.
- B3 packet frontier: global `PI_1^*` is sufficient but stronger than needed;
  the live target is high-`Lambda` packet-tail finiteness. Static interpolation
  and the straight global critical `H^(1/2)` route are separated.
- B4 selector motion: unchanged unless a genuine active-set variation or
  selector-free limiting theorem is supplied.

## Smallest safe next tranche

The live obligation is now **C2-MIX-DIRECTION-PATHORDER**.

L5-36 closes the separable signed-strain case.  The next problem is genuinely
time-dependent spatial direction geometry:

> For `B_h=B_h(s,Y)`, what path-ordered strain observable replaces the
> separable signed clock, and which part of it must remain controlled for the
> L5-35 metric theorem?

The first audit must compare:

1. cancellation in the scalar coefficient `theta_h`;
2. noncommuting time-dependent vector fields;
3. the characteristic Jacobian exponent along actual trajectories;
4. higher characteristic metric derivatives.

Any positive invariant must reduce exactly to `kappa_h` when the spatial
profile is time-independent.

## Authoritative pointers

- `grandchallenge/INTELLECT:CONSTITUTION.md`
- `grandchallenge/INTELLECT:governance/constitutional_authority_schedule.json`
- `grandchallenge/INTELLECT:governance/handoffs/README.md`
- `grandchallenge/MATHSOLVE:AGENTS.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_RESTART.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_PRETRIANGLE_STRICT_TAIL.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_ZERO_GAP_DYNAMIC_AUDIT.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_B1_COUPLED_ENSTROPHY.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_B3_L6_TRANSPORT_AUDIT.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_B3_SIGNED_PRESSURE_FIXTURE.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_B3_PACKET_INTERMITTENCY_D1.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_B3_PI1_CRITICAL_ENERGY_AUDIT.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_10_FIELD_CALIBRATION_FREQUENCY_SCALE_HANDOFF.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_11_FORCED_CORE_SHELL_CALIBRATION.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_11_SOURCE_AND_CAPTURE_AUDIT.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_12_FREQUENCY_SCALE_TRANSPLANT_BOUNDARY.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_13_C3_DIAGONAL_AUDIT.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_14_C2_ACTIVE_BAND_REDUCTION.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_15_C2_OVERSHOOT_PERSISTENCE_AUDIT.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_16_C2_SAME_BAND_MILD_OBSTRUCTION.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_17_C2_INSTANTANEOUS_CROSS_LEVEL.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_18_C2_TEMPORAL_LEAKAGE.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_19_C2_FIXED_DISTANCE_AMPLITUDE.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_20_C2_DISTANCE_SOBLEV_TAIL.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_21_C2_CUMULATIVE_FLUX_OBSTRUCTION.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_22_C2_TRIAD_COHERENCE.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_23_C2_SHEAR_PHASE_LOCK.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_24_C2_MIX_MOMENT_CEILING.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_25_C2_MIX_SUBCRITICAL_LOWER.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_26_C2_MIX_CRITICAL_SEMICLASSICAL.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_27_C2_MIX_BRIDGE_NORMAL_FORM.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_28_C2_MIX_SEMICLASSICAL_RESIDUAL.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_29_C2_POLARIZATION_CORRIDOR.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_30_C2_SECONDARY_SHEAR_CHARGE.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_31_C2_GENERAL_SHEAR_PROFILE.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_32_C2_ACCUMULATED_PHASE.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_33_C2_DIRECTION_DEFECT.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_34_C2_DIRECTION_MOVING_FRAME.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_35_C2_DIRECTION_DEFORMED_FRAME.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_36_C2_DIRECTION_SIGNED_FLOW_TIME.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L4_WEIGHTED_COLUMN.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L4_SIGNED_DECORRELATION.md`
- `grandchallenge/MATHSOLVE:campaign_manifests/NS-CI-001.json`
- `grandchallenge/MATHSOLVE#24`
- `grandchallenge/MATHSOLVE#59`

## Material dependencies and boundaries

L3 is closed. Reopening requires actual parabolic residence at the defining
threshold, a non-summable equation-derived scale cost, cross-level coherence,
anti-fragmentation, or an equivalent protected theorem.

L4 is closed. Reopening requires selected-transfer cancellation, active-set
variation, active-diagonal depletion, commutator closure, or dynamic
decorrelation.

The active Cert scope qualifies only the exact target/interface boundary. It is
not proof of A2 or of any analytic L5 estimate.

The September 2026 explicit singular construction uses a smooth external force;
it is not a solution in the selected unforced A2 class. It may calibrate the
observable but may not be used as a direct A2 counterexample.

## Reserved stop conditions

Stop for proof of A2; a proved material bridge with a precise next residual; a
rigorous bounded route termination; an exact L5 exhaustion theorem; a material
change to the selected target or hypothesis; a reserved constitutional or
certification transition; authentication or safety failure; or a materially
changed protected mathematical predecessor.

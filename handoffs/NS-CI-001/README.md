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

Do not repeat fixed-distance threshold leakage as though it supplied a
non-summable selector cost.

The first live obligation is now **C2-DIST**: quantify threshold-reaching
spectral distance as a function of the overshoot ratio `R`.

The fixed-distance certificate scales like

```math
r^2/R.
```

Therefore a charge-only reopening needs threshold-sized leakage to spectral
distance at least comparable to

```math
r(R) >= c sqrt(R)
```

on a turnover-scale interval, or another temporal mechanism with equivalent
non-summable cost.

Use the exact 2.5D calibration to decide this bounded question.  A positive
result at `sqrt(R)` scale would materially reopen cross-level charging.  A
rigorous analytic/Gevrey upper bound `r(R)=o(sqrt(R))` would instead close
spectral-distance leakage as the missing mechanism in this calibration and
move the live route to cumulative signed flux, repeated-event coherence, or
phase decoherence.

Do not infer growing distance from nonzero support, and do not assume selector
regularity while generated modes appear.

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
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_18_C2_TEMPORAL_LEAKAGE.md`\n- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L5_19_C2_FIXED_DISTANCE_AMPLITUDE.md`
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

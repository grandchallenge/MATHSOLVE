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

Do not repeat C1, the direct Chemin--Lerner transplant, a fixed or purely
absolute shifted observation scale, unsigned active-diagonal renormalization,
or an instantaneous universal signed central-flux cancellation. Those bounded
families are now characterized.

The first live obligation is **C2-DIAG**: prove an equation-derived
high-`Lambda` active-band depletion/anti-concentration statement, or a
genuinely time-correlated signed central-flux theorem.

The most concrete anti-concentration target is a dimension-one improvement of
Bernstein on the high-activity central band. With
`lambda_E=(nu/U0)^2`, seek a time-integrated estimate comparable to

```math
||u_q||_infinity^2
<=
C lambda_E lambda_q^2 ||u_q||_2^2
```

for `q=Q(t)+O(1)` on high-`Lambda` times, or any weaker statement sufficient
to make the terminal high-`Lambda` packet tail finite. Do not assume an
intermittency dimension; derive the depletion from NSE dynamics.

A second legitimate route is to retain the signed central convection-pressure
flux over nested backward cylinders and prove cancellation only after time
integration. The L5-13 fixture rules out a universal instantaneous identity or
sign but not a dynamical coherence theorem.

A selector/physical-scale coherence theorem could also reopen the shifted-scale
route, but that is an explicit L3/B4 reopening obligation.

Reject any successor that merely returns `lambda_Q D_Q`, assumes strict-high
at `Q`, assumes Bernstein non-saturation, differentiates the selector without
control, or imports a periodic/forced intermittency conclusion into the
unforced whole-space target.

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

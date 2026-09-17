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

Do not repeat static packet interpolation, moving-tail H1 energy, fixed-tail
bad-set splitting, threshold-residence Duhamel, the standard direct-L6
absolute commutator estimate, signed projection/pressure algebra alone, the L4
weighted column, or the straight global critical-energy comparison.

Proceed in this order:

1. **Protect the high-`Lambda` tail reduction** with focused regression tests.
2. **Calibrate the explicit forced singular solution** by proving or rejecting
   a Littlewood--Paley shell lower bound at `lambda~(1-t)^(-1/2)`. If it
   succeeds, compute `Lambda`, `f`, `S_1`, `W_{<=Q}`, and `Z_{>Q}` asymptotics.
   Keep the forced/unforced claim boundary explicit.
3. **Launch frequency--scale matching** in a backward local-energy cylinder.
   Retain dyadic frequency `q` and physical scale `k` separately. Seek a
   summable kernel in `q-k`; bind `k` to `Q` only after obtaining the gain.
4. Express any successful active-set depletion in the Cheskidov--Peng
   intermittency language after the PDE estimate is proved, not before.

A useful theorem-grade successor is any estimate implying

```math
integral_{(T-delta,T) intersect {Lambda>R}} S_1(t) dt < infinity
```

for each putative singular time `T`, with finite `R,delta`. This is enough for
the established `f in L1` continuation route when combined with A2.

Reject a candidate immediately if it reduces to `G_Q`, `S_Q`, selector
variation, a new residence assumption, or `Lambda^2 X^(3/2)` without an
independent reopening theorem.

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

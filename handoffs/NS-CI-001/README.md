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

Protected L5-4 merge `14aad98fbbbcf9f0ed780b9aea5b244f189c3947`
proved

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

For `U0=||u0||_2`, define the intrinsic whole-space energy wavenumber

```math
lambda_E=(nu/U0)^2
```

and

```math
S_D(t)=sum_{q<=Q(t)} lambda_q^(D-1)||u_q(t)||_infinity^2.
```

The conditional packet estimate is

```math
PI_D^*:
integral S_D
<=
C_D lambda_E^D
integral sum_q lambda_q^2||u_q||_2^2.
```

This normalization is Navier--Stokes scale-covariant and physically
dimensionally consistent. Pointwise,

```math
f^2 <= Lambda^(3-D) S_D,
qquad
f=sup_{q<=Q} lambda_q||u_q||_infinity.
```

Thus every `D>=1`, together with `PI_D^*`, the selected `Lambda in L2_t`
hypothesis, and Leray dissipation, gives `f in L1_t` and closes the already
established low-mode criterion. At `D=1`,

```math
integral f
lesssim
C_1^(1/2) nu^(1/2) ||Lambda||_L2.
```

A threshold-compatible static fixture separates the current A2 scalar budgets
from `PI_1^*`. It is not a Navier--Stokes trajectory. Hence the missing packet
estimate must use genuinely dynamic information.

The exact-merge replay on `b05c3e6e...` completed green for formal targets,
ledgers, Ubuntu, Windows, and security analysis. Later protected-main movement
was unrelated and retained `b05c3e6e...` in ancestry.

### L5-9 critical H1/2 dynamic audit

`work_packages/NS_CI_R014_A2_L5_B3_PI1_CRITICAL_ENERGY_AUDIT.md` records

```text
PI1_CRITICAL_H12_ROUTE_REDUCED_TO_SUPERLINEAR_RICCATI__GLOBAL_CRITICAL_TRANSFER_HAS_NO_SIGN.
```

Define

```math
X=sum_q lambda_q||u_q||_2^2,
qquad
Y=sum_q lambda_q^3||u_q||_2^2.
```

Bernstein gives

```math
S_1 <= C Y_{<=Q} <= C Y,
```

so the critical `H^(1/2) -> H^(3/2)` energy balance is a genuine candidate for
manufacturing the packet endpoint. However the exact low-mode estimate is

```math
f <= C Lambda^2 X^(1/2).
```

The standard low-mode-controlled critical-energy candidate therefore reduces
to the superlinear comparison

```math
X' <= C Lambda^2 X^(3/2),
```

rather than linear Gronwall. Leray also gives `X in L2_t`, but an explicit
scalar profile has `a in L1`, `x in L2`, `x'=a x^(3/2)`, and finite-time
blow-up, so these abstract data do not close the comparison. Its terminal
coefficient tail has exactly the Riccati threshold scaling; shrinking the
terminal interval alone does not repair it.

An exact real divergence-free three-mode Fourier triad has zero total `L2`
nonlinear transfer but `dot H^(1/2)`-weighted pairing `-8`; a phase reversal
gives `+8`. Thus the complete critical nonlinear transfer has no universal
sign. This excludes a second generic escape from the straight critical-energy
candidate.

The scalar fixture is not an NSE trajectory; the triad is an algebraic sign
fixture. This bounded result does not exclude active-set-specific depletion or
selected-transfer cancellation.

## Residual blockers

- B1 low core: moving enstrophy hits B4; selector-free complementary coupling
  returns the closed L4 weighted column.
- B2 near threshold: no standalone blocker in the pointwise L5 decomposition;
  dynamic finite-neighbour terms can still occur.
- B3 strict tail / packet frontier: `PI_1^*` is sufficient but not proved from
  A2. Static interpolation is separated. The straight global critical
  `H^(1/2)` route reduces to a superlinear Riccati comparison, and the complete
  critical transfer has no universal sign.
- B4 selector motion: unchanged unless a genuine active-set variation or
  selector-free limiting theorem is supplied.

## Smallest safe next tranche

Do not repeat static packet interpolation, moving-tail H1 energy, fixed-tail
bad-set splitting, threshold-residence Duhamel, the standard direct-L6
absolute commutator estimate, signed projection/pressure algebra alone, the L4
weighted column, or the straight global critical-energy comparison.

The smallest live dynamic proposition is now an **active-set-specific packet
depletion theorem**. Test whether the defining threshold and NSE transfer
identity force, on high-`Lambda` times, a quantitative improvement over

```math
f <= C Lambda^2 X^(1/2)
```

or an equivalent selected-shell estimate sufficient to make the L5-8
Cauchy--Schwarz bridge finite. A valid advance must produce one of:

1. a coefficient linear in the critical state whose time integral is
   controlled by A2/Leray budgets;
2. active-shell depletion/anti-concentration with a summable frequency gain;
3. selected-transfer cancellation/coherence unavailable to the complete
   critical pairing;
4. a different dimensionally and scale-covariant packet estimate that closes
   `f in L1_t` without recreating L3, L4, or B4.

If a candidate reduces to `G_Q`, `S_Q`, selector variation, a residence
assumption, or the superlinear `Lambda^2 X^(3/2)` comparison, record that exact
reduction rather than reopening its closed lane.

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

## Reserved stop conditions

Stop for proof of A2; a proved material bridge with a precise next residual; a
rigorous bounded route termination; an exact L5 exhaustion theorem; a material
change to the selected target or hypothesis; a reserved constitutional or
certification transition; authentication or safety failure; or a materially
changed protected mathematical predecessor.

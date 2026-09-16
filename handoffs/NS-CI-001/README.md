# NS-CI-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

INTELLECT work-package phase: not applicable; this is delegated MATHSOLVE
mathematical campaign execution. MATHSOLVE may develop and integrate bounded
mathematical results but may not certify them. MATHCERT retains certification
authority.

## Purpose

Continue the selected restricted target `NS-CI-R014-A2` without weakening the
hypothesis `Lambda in L2_t` or importing a regularity criterion that already
implies the desired conclusion.

## Primary deliverable

Advance the active L5 direct critical-integral route through exact
square-function, correlation, cancellation, depletion, commutator, or dynamic
estimates that act on the remaining blockers.

## Material acceptance criteria

- derive the target `integral ||u||_6^4` from the selected hypothesis and valid
  Leray--Hopf/PDE structure, or rigorously terminate the current bounded
  candidate at its first exact blocker;
- preserve the strict-high restriction `p>Q` exactly;
- keep every shell/time constant uniform in terminal frequency;
- do not multiply unrelated `L1_t` quantities, assume selector variation,
  import `f in L1_t`, uniform `H1`, or an LPS norm;
- do not reopen L3 or L4 without satisfying their protected reopening
  conditions.

## Current substantive state

Selected target: `NS-CI-R014-A2`, unproved.

Protected L5-4 predecessor: merge
`14aad98fbbbcf9f0ed780b9aea5b244f189c3947`, result

```text
ZERO_GAP_REDUCTION_PROVED__STATIC_B1_ENDPOINT_SEPARATED__PARABOLIC_B3_ROUTE_REDUCED
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

The first equation-specific B1 successor has result

```text
B1_DIRECT_DYNAMIC_ROUTE_REDUCED__SELECTOR_FREE_REPAIR_EQUALS_CLOSED_L4_COLUMN
```

and is recorded in
`work_packages/NS_CI_R014_A2_L5_B1_COUPLED_ENSTROPHY.md`.

For fixed low cutoff, the low enstrophy balance has viscous density comparable
to `W_{<=q}`. Localizing it to the moving active selector produces both a
selected, non-conservative enstrophy-production term and B4 selector variation.

Coupling the complementary high enstrophy balance cancels selector variation
exactly. The remaining low-mode coefficient is

```math
f(t)=sup_{p<=Q(t)} lambda_p ||u_p(t)||_infinity.
```

Define

```math
D_3(t)
=
sum_{p<=Q}
(lambda_p/Lambda)^3 A_p.
```

Then

```math
f^2 lesssim Lambda^3 D_3,
```

so Leray gives only `D_3^(1/2) in L2_t`, while `Lambda in L2_t` would require
`D_3^(1/2) in L4_t` to close this product directly.

More decisively,

```math
nu Lambda D_3
=
sum_{p<=Q}
(lambda_p/Lambda)^2 lambda_p D_p
=S_Q,
qquad D_p=nu A_p.
```

This is exactly the protected L4 weighted-column quantity, including its
`p=Q` active diagonal. The selector-free B1 repair therefore does not furnish a
new L4 reopening theorem and is terminated.

### B3 direct L6 transport audit

The next distinct B3 candidate has result

```text
DIRECT_L6_TRANSPORT_ROUTE_REDUCED_TO_LOW_DEFORMATION_COMMUTATOR
```

and is recorded in
`work_packages/NS_CI_R014_A2_L5_B3_L6_TRANSPORT_AUDIT.md`.

For fixed `q`, with

```math
V_q=P_{>q}u,
qquad
L_q=P_{<=q-2}u,
```

the unprojected low--high transport cancels exactly against `|V_q|^4 V_q`.
But the actual equation contains `P_{>q} mathbb P(L_q dot grad V_q)`. The exact
transport cancellation leaves a high-pass/Leray projection residual. Shellwise
commutator localization contributes a kernel moment `lambda_p^-1` and a
high-shell derivative `lambda_p`; these cancel, leaving

```math
G_q=||grad L_q||_infinity
```

with no decaying high-frequency gain. Thus direct projected `L6` transport does
not escape the same low-deformation interface that blocked the first H1
parabolic route.

Residual blockers:

- B1 low core: no surviving direct moving-enstrophy route; the selector-localized
  version hits B4 and the selector-free coupled version is exactly closed L4
  `S_Q`;
- B2 near threshold: no standalone blocker in the pointwise L5 decomposition;
- B3 strict tail: control
  `integral (sum_{p>Q} lambda_p^2 A_p)^(2/3) dt` or find a signed/nonlinear
  identity avoiding it. Moving-tail H1, fixed-tail bad-set, residence-Duhamel,
  and direct projected-L6 transport are now characterized;
- B4 selector motion: avoidable only when complementary moving balances are
  coupled; otherwise unchanged.

MATHCERT remains `qualified_interface_only`; A2 and universal critical
integrability are unproved.

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
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L4_WEIGHTED_COLUMN.md`
- `grandchallenge/MATHSOLVE:work_packages/NS_CI_R014_A2_L4_SIGNED_DECORRELATION.md`
- `grandchallenge/MATHSOLVE:campaign_manifests/NS-CI-001.json`
- `grandchallenge/MATHSOLVE#24`
- `grandchallenge/MATHSOLVE#59`

## Smallest safe next tranche

B3 remains the only non-closed pointwise endpoint with room for a genuinely new
mechanism. Do not repeat moving-tail H1 energy, fixed-tail bad-set splitting,
threshold-residence Duhamel, direct projected-L6 transport, or the L4 weighted
column.

The smallest admissible next proposition must act on one of:

1. a signed projection/pressure commutator identity that cancels the low
   deformation coefficient before absolute values;
2. an equation-specific packet/intermittency depletion theorem that controls
   `Z_{>Q}` or `Z_{>Q}^{2/3}` from the selected hypothesis;
3. a new nonlinear quantity whose evolution couples the strict-high threshold
   to `Z_{>Q}` without selector variation or parabolic residence.

If each bounded candidate reduces to `G_Q`, `S_Q`, selector variation, or a
residence assumption, record the exact reduction rather than reopening the
corresponding closed lane.

## Material dependencies and boundaries

L3 is closed. Reopening requires actual parabolic residence at the defining
threshold, a non-summable equation-derived scale cost, cross-level coherence,
an anti-fragmentation budget, or an equivalent protected reopening theorem.

L4 is closed. Reopening requires an actual selected-transfer cancellation,
active-set variation theorem, active-diagonal depletion, commutator closure, or
dynamic decorrelation result.

The active Cert scope qualifies only the exact target/interface boundary. It is
not proof of A2 or of any analytic L5 estimate.

## Reserved authority / stop conditions

Stop for proof of A2; a proved material bridge with a precise next residual; a
rigorous bounded route termination; an exact L5 exhaustion theorem; a material
change to the selected target or hypothesis; a reserved constitutional or
certification transition; authentication or safety failure; or a materially
changed protected mathematical predecessor.

## Notes intentionally omitted

This handoff intentionally omits constitutional doctrine, generic handoff
instructions, CI logs, and certification ceremony already controlled by their
authoritative records.
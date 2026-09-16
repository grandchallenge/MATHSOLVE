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

Current B1 disposition:

```text
B1_DIRECT_DYNAMIC_ROUTE_REDUCED__SELECTOR_FREE_REPAIR_EQUALS_CLOSED_L4_COLUMN
```

recorded in
`work_packages/NS_CI_R014_A2_L5_B1_COUPLED_ENSTROPHY.md`.

For fixed low cutoff, low enstrophy has viscous density comparable to
`W_{<=q}`. Localizing it to the actual moving selector produces selected
non-conservative enstrophy production plus B4 selector variation.

On a genuinely finite Galerkin system with its own finite-spectrum selector
`Q_N`, coupling the complementary finite high block cancels selector variation
algebraically. This does **not** establish the corresponding cancellation for
the actual unbounded selector: truncating the actual selector at `q<=N` leaves
`1_{Q<=N}` and its terminal boundary. No B4 reopening theorem is claimed.

Even granting a justified selector-free limiting step, the surviving low
coefficient

```math
f(t)=sup_{p<=Q(t)} lambda_p ||u_p(t)||_infinity
```

obeys, for

```math
D_3(t)=sum_{p<=Q}(lambda_p/Lambda)^3 A_p,
```

```math
f^2 lesssim Lambda^3 D_3.
```

Leray gives only `D_3^(1/2) in L2_t`; direct Holder with `Lambda in L2_t`
would require `D_3^(1/2) in L4_t`.

More decisively,

```math
nu Lambda D_3
=
sum_{p<=Q}(lambda_p/Lambda)^2 lambda_p D_p
=S_Q,
qquad D_p=nu A_p.
```

This is exactly the protected L4 weighted-column quantity, including the
`p=Q` active diagonal. Thus the optimistic selector-free B1 repair still lands
on closed L4 and does not furnish a reopening theorem.

### B3 direct L6 transport audit

Current B3 bounded-family disposition:

```text
DIRECT_L6_STANDARD_COMMUTATOR_ROUTE_REDUCED_TO_LOW_DEFORMATION
```

recorded in
`work_packages/NS_CI_R014_A2_L5_B3_L6_TRANSPORT_AUDIT.md`.

For fixed `q`, set

```math
V_q=P_{>q}u,
qquad
L_q=P_{<=q-2}u.
```

The unprojected low--high transport cancels exactly against `|V_q|^4V_q`.
The actual equation contains `P_{>q} mathbb P(L_q dot grad V_q)`, leaving a
signed high-pass/Leray projection residual. Under the standard absolute
shellwise commutator estimate, the projector kernel moment `lambda_p^-1` and a
high-shell derivative `lambda_p` cancel in scale and leave

```math
G_q=||grad L_q||_infinity
```

with no decaying high-frequency gain. Active localization then reintroduces B4;
fixed-`q` globalization reintroduces the bad-time/residence interface.

This terminates only the standard absolute commutator-estimate family. A signed
projection/pressure cancellation inside the residual remains live.

## Residual blockers

- B1 low core: direct moving enstrophy hits B4; even granting selector-free
  complementary coupling, the remaining factor is exactly closed L4 `S_Q`.
- B2 near threshold: no standalone blocker in the pointwise L5 decomposition;
  dynamic finite-neighbour terms may still occur.
- B3 strict tail: control
  `integral (sum_{p>Q} lambda_p^2 A_p)^(2/3) dt` or avoid it by a new signed or
  nonlinear identity. Moving-tail H1, fixed-tail bad-set splitting,
  threshold-residence Duhamel, and the standard direct-L6 absolute commutator
  estimate are characterized. The signed projection/pressure residual itself
  remains open.
- B4 selector motion: unchanged for the actual moving selector unless a genuine
  limiting/variation theorem is supplied.

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

B3 is the remaining pointwise endpoint with room for a genuinely new mechanism.
Do not repeat moving-tail H1 energy, fixed-tail bad-set splitting,
threshold-residence Duhamel, the standard direct-L6 absolute commutator
estimate, or the L4 weighted column.

The smallest live proposition is now the signed projection/pressure residual:
expand the high-pass and Leray pieces before absolute values and test whether a
structural cancellation removes `G_Q`. If it does not, the remaining distinct
frontier is an equation-specific packet/intermittency depletion theorem for
`Z_{>Q}` or `Z_{>Q}^{2/3}`.

If a candidate reduces to `G_Q`, `S_Q`, selector variation, or a residence
assumption, record that exact reduction rather than reopening its closed lane.

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
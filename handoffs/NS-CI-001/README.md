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

Protected L5 predecessor: merge
`e58e92265e895ff560e542bc78ab0ffd853fb1e8`, result
`L5_CANDIDATE_ROUTE_TERMINATED__CHARACTERIZED_BLOCKER` for the buffered
pre-triangle strict-tail candidate.

Current candidate result:

```text
ZERO_GAP_REDUCTION_PROVED__STATIC_B1_ENDPOINT_SEPARATED__PARABOLIC_B3_ROUTE_REDUCED
```

The pre-triangle strict-tail estimates in fact require no fixed gap `K`.
Because the defining threshold is valid for every `p>Q`, one may use the exact
two-block decomposition

```math
u=u_{\le Q}+u_{>Q}.
```

The strict tail satisfies

```math
||u_{>Q}||_4^4
lesssim
c_0^2 nu^2 sum_{p>Q} A_p,
```

and

```math
||u_{>Q}||_6^4
lesssim
c_0^(8/3) nu^(8/3)
(sum_{p>Q} lambda_p^2 A_p)^(2/3).
```

Together with the protected low estimate this gives

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
W_{<=Q}=sum_{r<=Q} lambda_r^2 A_r,
qquad
Z_{>Q}=sum_{p>Q} lambda_p^2 A_p.
```

The standalone B2 near-threshold blocker is therefore removed from this
pointwise L5 norm representation: `p=Q` stays low and every `p>Q` is strict
high. This does not remove near-neighbour terms from other dynamic PDE
identities.

A threshold-compatible static shell fixture has finite `Lambda L2` occupancy,
finite Leray shell dissipation, and bounded kinetic energy while

```math
integral W_{<=Q} dt = infinity.
```

Thus the exact low endpoint also requires equation-specific correlation; it is
not recoverable by another scalar occupancy/Holder rearrangement.

The first parabolic attempt on the high endpoint was audited at `H1` level.
The low--high transport leaves the unavoidable deformation coefficient

```math
G_q=||grad u_{<=q-2}||_infinity.
```

Localizing a fixed-cutoff tail to the active set recreates the uncontrolled
selector-boundary ledger; keeping the cutoff fixed loses strict-high absorption
on `{Q>q}`; a backward Duhamel window requires defining-threshold parabolic
residence. Hence the first viscosity/maximal-regularity B3 family reduces to a
new low-mode input plus the already protected B4/L3 interfaces rather than
closing autonomously.

Residual blockers:

- B1 low core: control
  `sum_r lambda_r^2 integral_{Q>=r} A_r dt` by an actual Navier--Stokes
  correlation/depletion mechanism;
- B2 near threshold: no standalone blocker in the current pointwise L5
  decomposition; retained only as a possible dynamic finite-neighbour term;
- B3 strict tail: control
  `integral (sum_{p>Q} lambda_p^2 A_p)^(2/3) dt` or find a signed/nonlinear
  identity avoiding it;
- B4 selector motion: unchanged whenever a dynamic argument differentiates or
  localizes the moving cutoff.

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
- `grandchallenge/MATHSOLVE:campaign_manifests/NS-CI-001.json`
- `grandchallenge/MATHSOLVE#24`
- `grandchallenge/MATHSOLVE#59`

## Smallest safe next tranche

B1-first. Test one genuine Navier--Stokes correlation/depletion estimate for

```math
sum_r lambda_r^2
integral_{Q>=r} A_r(t) dt.
```

Do not return to static Holder, occupancy, energy-floor, or packet-counting
rearrangements; the new low-core fixture separates those. A viable candidate
must use the equation to decorrelate shell dissipation from the superlevel event
`Q>=r` without importing `f in L1`, uniform `H1`, an LPS norm, or an L4
active-diagonal hypothesis.

If the B1 candidate fails, record the first exact PDE term that prevents the
correlation estimate. Only then reconsider B3 through a mechanism genuinely
different from moving-tail `H1` energy, fixed-tail bad-set splitting, or
threshold-residence Duhamel.

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
instructions, L3/L4 history beyond their live reopening conditions, CI logs,
and certification ceremony already controlled by their authoritative records.

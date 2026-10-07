# ERDOS-OPEN-001 reconnaissance packs

Status: `STAGED_NOT_ACTIVATED`.

This directory materializes the first reconnaissance tranche selected by `MATH-PROGRAMME/ERDOS-OPEN-TRIAGE-001` as eight bounded zero-context packs. Each pack has three lanes:

- **R** — protected-packet mathematical reconnaissance;
- **S** — primary-source interface audit;
- **A** — protected-packet adversarial falsification/route attack.

The selected problems are `593, 595, 241, 470, 1052, 99, 101, 138`. There are therefore **24 proposed assignments**.

These artifacts are intentionally not executable. They have no bound GitHub return issue, dispatch ID, agent reference, lease identity, or active campaign registration. A later protected activation transaction must create those bindings and must preserve blind-return separation.

## Activation contract

For any pack selected for execution:

1. Re-read protected MATH-PROGRAMME triage and MATHFORGE intake.
2. Verify that the problem remains eligible and is not newly status-held or already active elsewhere.
3. Re-read the exact protected formalization blob named in the pack.
4. Create one immutable launch artifact per lane.
5. Bind one issue, dispatch ID, agent reference, and lease identity per launch.
6. Record `execution_authorized: true` only in that later protected launch/lease record, never by editing the staged pack's historical meaning.
7. Preserve the first valid RESULT/1 return and keep sibling returns blind until the synthesis gate.
8. Synthesis normally requires at least R + A evidence; literature-dependent promotion additionally requires S. If an accepted R/A return carries a machine-readable source/formal semantic blocker, the matching S lane becomes a hard precondition for synthesis itself.
9. Contributor returns are evidence only. Native theorem/falsification work is a separate protected transaction.

## Authority boundary

The present state authorizes work-package **design only**. It does not authorize external execution, repository mutation by contributors, mathematical claim promotion, campaign activation, publication, or MATHCERT certification.


## Additive cohort closure overlay

The activation cohort records under `contributions/ERDOS-OPEN-001/RECON_TRANCHE_001/cohorts/`
remain historical blind-collection records and are not reclassified in place.

When protected R1 and A1 evidence satisfy the Programme synthesis minimum, cohort
closure is represented additively under:

`contributions/ERDOS-OPEN-001/RECON_TRANCHE_001/closures/`

A valid closure overlay may set `blind_cohort_closed=true` and
`synthesis_allowed=true` only while retaining
`mathematical_correctness_adjudicated=false`,
`canonical_claim_effect=false`, `certification_effect=false`, and
`claim_promotion_effect=false`.

S1 is not normally required to open synthesis. If S1 is not protected at
closure, the closure must explicitly retain the literature-dependent source gate
as unsatisfied. A later S1 return may satisfy that source prerequisite for later
adjudication; it does not retroactively alter the completed blind R1+A1
comparison.

### Semantic source gate

A RESULT/1 in an ERDOS R1/A1 lane may declare an exact machine-readable blocker:

```text
GCL-SEMANTIC-BLOCKER/1
blocker_id: <stable-id>
kind: SOURCE_FORMAL_CONFLICT
requires_dispatch_id: ERDOS-<problem>-S1-IA-001
```

The controlled intake records that declaration in the evidence receipt. Additive
protected policy may also pre-register a blocker for an already-immutable
dispatch; this is used when a known source/formal discrepancy must remain gated
without rewriting dispatch history or protected RESULT/1 bytes.

If an effective blocker is present, R1+A1 no longer suffice to close the cohort:
the matching protected S1 return is required before `synthesis_allowed=true`.
An S1 return with disposition `EXACT_BLOCKER` does not discharge the gate.
The source return remains evidence only; satisfying this gate does not adjudicate
the mathematics, certify the source interpretation, or create MATHCERT effect.

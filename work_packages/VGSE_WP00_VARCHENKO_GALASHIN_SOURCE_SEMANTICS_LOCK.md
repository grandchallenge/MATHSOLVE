# VGSE-WP00 — Varchenko–Galashin Source and Semantics Lock

## Metadata

- Campaign: `VGSE-001`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#170`
- Solve tracker: `grandchallenge/MATHSOLVE#84`
- Work Package number: `VGSE-WP00`
- Primary type: `SOURCE_NORMALIZATION_AND_EXACT_REPLAY`
- Global theorem-spine node: `VGSE-S0-SOURCE-AND-SEMANTICS-LOCK`
- Incoming dependencies: Grand Challenge Work Package Standard; Claim Boundary Doctrine; Galashin Appendix B
- Claim status: `COMPUTED_EXACTLY` for the arrangement count; `NEEDS_AUDIT` for the numerical critical-point witnesses
- Certification target: independent MATHCERT replay of the exact arrangement certificate and saturated polynomial fixture
- Foundational profile: present

## 1. Result-status box

| Field | Value |
|---|---|
| Result status | WP00 candidate with executable `(3,6)` replay |
| Conditional on | Correct transcription of the pinned source and the selected regular-hexagon boundary fixture |
| Strongest supported claim | The Example B.1 arrangement has `beta(C)=5`; the supplied saturated replay produces five divisor-excluding numerical witnesses that pass the encoded residual, orthogonality, adjacent-minor, and winding checks |
| Not claimed | Certified genericity or exact isolation of the five witnesses; internal face reconstruction; rendered t-embeddings; continuous rigid foldability; collision freedom; finite-thickness realization; manufacturability; product performance; novelty; priority; patentability; or commercial value |
| Support-route class | `EXACT_FINITE_VERIFICATION` plus `REGRESSION_AUDIT` |
| Certification state | `UNSUBMITTED_TO_MATHCERT` |
| First executable step | Reconstruct and render the five internal t-embeddings for an explicit weighted planar bipartite graph realizing the pinned matrix `C` |

## 2. Foundational profile

```yaml
foundational_profile:
  carrier_type: complex_projective_parameter_space
  ambient_structure:
    - affine_hyperplane_arrangement_over_Q
    - complex_master_function_critical_locus
    - real_two_planes_in_R6
  regularity:
    - generic_boundary_polygon_for_the_counting_theorem
    - arrangement_divisor_excluded
    - isolated_critical_points
  axiom_profile:
    base: classical_mathematics
    choice_usage: none_in_replay
    excluded_middle: ordinary_finite_computation
    large_cardinal_usage: none
    determinacy_usage: none
  witness_policy:
    existence_claim: explicit_numeric_witnesses_with_residual_checks
    witness_location: work_packages/VGSE_WP00/artifacts/data/expected_replay.json
  certification_target:
    - exact_arrangement_certificate
    - saturated_polynomial_replay
    - independent_numeric_root_replay
  pathology_risk:
    level: high
    notes: "Resultants contain divisor-supported roots; algebraic pairs need not be positive t-immersions; physical foldability is a separate problem."
```

## 3. Lay executive companion

### The object

Galashin fixes a positive Grassmannian matrix `C` and a planar boundary polygon. A master-function system then enumerates algebraic pairs compatible with that boundary. For the published `(k,n)=(3,6)` example, a two-dimensional line arrangement has five bounded regions.

### The obstruction

The word “solution” has several non-equivalent meanings. A root of the polynomial system can lie on a forbidden denominator. A valid algebraic pair can fail the sign conditions needed for a t-immersion. A planar t-embedding does not establish a continuous rigid-panel motion. A rigid mechanism does not establish a finite-thickness manufacturable product.

### The restricted target

Lock the source and reproduce only the first bounded layers:

1. the exact bounded-region count;
2. five divisor-excluding numerical critical-point witnesses for a pinned regular-hexagon boundary;
3. numerical sign, winding, residual, denominator, and orthogonality checks for those witnesses.

### What this package achieved

The replay computes nine distinct finite intersections of the five affine lines and obtains

```text
beta(C) = 1 - 5 + 9 = 5.
```

It removes the denominator-supported resultant factor `25*x - 24`, solves the remaining degree-five polynomial numerically, and retains five witnesses. Each retained witness passes the encoded residual, divisor-exclusion, orthogonality, adjacent-minor, and winding tests.

### What this package did not achieve

It does not certify the selected boundary fixture's genericity or isolate the roots with interval or exact algebra. It does not reconstruct the internal dual-graph geometry shown in Galashin Figure 16. It does not prove a rigid-folding path, handle panel collisions or thickness, fabricate a prototype, or support a commercial claim.

## 4. Formal problem statement

### Source lock

Candidate source:

- Pavel Galashin, *Amplituhedra and Origami, I: Tree Level*.
- Author-hosted PDF: `https://www.math.ucla.edu/~galashin/papers/t_embeddings_v2.pdf`.
- PDF date printed in source: `2026-06-03`.
- File size: `1,317,147` bytes.
- SHA-256: `e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de`.
- Target: Appendix B, Example B.1, Proposition B.2, Example B.3, Figure 16.

The author PDF is used because Appendix B in this dated revision contains the prescribed-boundary result and the five-pattern example. The arXiv identity is `2410.09574`; source-version concordance remains an external-audit item.

### Fixed matrix

```text
C = [[1, 1, 0, -6, 0,  3],
     [0, 1, 1,  7, 0, -2],
     [0, 0, 0,  2, 1,  3]].
```

In the projective chart `a=(1,x,y)`, the six linear forms are

```text
alpha_1 = 1
alpha_2 = 1+x
alpha_3 = x
alpha_4 = -6+7x+2y
alpha_5 = y
alpha_6 = 3-2x+3y.
```

The projectivized arrangement is

```text
x=-1,
x=0,
7x+2y=6,
y=0,
-2x+3y=-3.
```

### Exact target statement

For the line arrangement above, verify `beta(C)=5`. For the unit-circumradius regular hexagonal kami boundary, transcribe the master-function critical equations in the chart `a_1=1`, remove all arrangement-divisor factors, and produce five numerical witnesses for the remaining degree-five fixture.

For every retained witness, form `zeta_i=alpha_i(a)` and `tilde_zeta_i=z_i/zeta_i`, orient the real plane `lambda` positively, and check numerically:

```text
lambda perpendicular to tilde_lambda,
adjacent minors of lambda are positive,
adjacent minors of tilde_lambda are positive,
wind(lambda)=2*pi,
wind(tilde_lambda)=4*pi.
```

These checks establish only numerically sign-compatible pair data for the selected fixture. They do not certify exact roots or render the internal t-embedding.

## 5. Object and obstruction

The unsaturated resultant contains the factor

```text
25*x - 24.
```

At `x=24/25`, the companion solution is `y=-9/25`, and

```text
alpha_6 = 3 - 2x + 3y = 0.
```

This point lies on the deleted arrangement divisor. Counting it would produce six roots and falsely contradict `beta(C)=5`. The smallest exact obstruction is therefore denominator contamination during elimination.

## 6. Known terrain and source audit

| Source or result | Claim used here | Audit state | Spine dependency |
|---|---|---|---|
| Galashin, Appendix B | Prescribed-boundary algebraic pair count equals `beta(C)` | Source pinned; theorem proof not independently reconstructed | `VGSE-S1` |
| Galashin, Example B.1 | Matrix `C`, five affine lines, and `beta(C)=5` | Transcribed and exactly replayed | `VGSE-S2` |
| Galashin, Example B.3 / Figure 16 | Five t-embeddings are displayed for a fixed boundary | Source observed; internal geometry not reproduced | `VGSE-S3` |
| Varchenko 1995; Orlik–Terao 1995 | Generic master-function critical-point count | Literature-derived; primary-paper audit pending | `VGSE-S1` |
| Zaslavsky arrangement theorem | Bounded-region count from the characteristic polynomial | Standard route; replay uses direct rank-two incidence count | `VGSE-S2` |

## 7. Claim ledger summary and trust quartet

| Claim ID | Statement | Status | Evidence | Certification state |
|---|---|---|---|---|
| `VGSE-C00` | The pinned Example B.1 arrangement has five bounded regions | `COMPUTED_EXACTLY` | Exact rational intersection enumeration | Unsubmitted |
| `VGSE-C01` | The selected saturated regular-hexagon replay produces five divisor-excluding numerical witnesses | `NEEDS_AUDIT` | Deterministic standard-library root replay and residual checks | Unsubmitted |
| `VGSE-C02` | Each retained witness passes encoded sign, winding, denominator, residual, and orthogonality checks | `NEEDS_AUDIT` | Floating-point machine-readable output and tests | Unsubmitted |
| `VGSE-C03` | The five internal t-embeddings of Figure 16 have been reconstructed | `NEEDS_AUDIT` | No internal graph reconstruction in this package | Blocked |
| `VGSE-C04` | Any retained design is rigidly deployable or manufacturable | `REFUTED` | Refuted only as an inference from current evidence; no physical lift has been performed | Not eligible |
| `VGSE-C05` | A commercial claim follows from the replay | `REFUTED` | Refuted as an inference and prohibited by the claim boundary | Prohibited |

### What is proved or exact?

The arrangement count `beta(C)=5` is an exact finite computation over rational line data.

### What is checked?

Five numerical critical-point witnesses and their encoded residual, sign, winding, divisor-exclusion, and orthogonality conditions.

### What remains open?

Fixture genericity, certified isolation or exact quotient dimension, internal t-embedding reconstruction, rigid deployment, collision analysis, finite thickness, mechanics, manufacturing, and commercial qualification.

### What requires external verification?

Primary-source concordance across revisions; the Varchenko–Orlik–Terao theorem chain; the exact graph and weight realization used for Figure 16; an independent certified solver replay.

## 8. Theorem-spine slice and dependency DAG

| Node ID | Role | Statement | Status | Dependencies | Discharge criterion |
|---|---|---|---|---|---|
| `VGSE-S0` | Source lock | Pin the exact Appendix B revision and semantics | Candidate complete | None | Independent source review |
| `VGSE-S1` | Literature bridge | Prescribed-boundary solutions are counted by `beta(C)` | Literature-derived | `VGSE-S0` | Primary theorem audit |
| `VGSE-S2` | Exact fixture | Example B.1 has `beta(C)=5` | Complete | `VGSE-S0` | Exact replay passes |
| `VGSE-S3` | Algebraic replay | Produce five retained numerical critical-point witnesses | Numerical replay complete; exact certification open | `VGSE-S1`, `VGSE-S2` | Certified genericity and exact or interval root count |
| `VGSE-S4` | Geometric reconstruction | Render five internal t-embeddings | Open | `VGSE-S3` | Coordinates, faces, and injectivity checks |
| `VGSE-S5` | Mechanical lift | Establish continuous collision-free rigid deployment | Gated | `VGSE-S4` | Certified path and collision checks |
| `VGSE-S6` | Product lift | Establish finite-thickness manufacturability and performance | Gated | `VGSE-S5` | Prototype and benchmark evidence |

## 9. Proofs and classified computations

### Exact arrangement computation

Pedagogical class: `EXACT_FINITE_VERIFICATION`.

The five lines have one parallel pair and nine distinct finite pairwise intersections. No finite intersection is triple. For an essential affine line arrangement in the plane,

```text
beta = 1 - number_of_lines + sum_p (multiplicity(p)-1).
```

Every finite intersection has multiplicity two, so `beta=1-5+9=5`.

### Critical-point replay

Pedagogical class: `REGRESSION_AUDIT`.

The script uses a fixed regular hexagon, encodes the two chart equations, and solves the divisor-filtered degree-five polynomial using deterministic Durand–Kerner iteration. For each `x` root it solves the quadratic chart equation for `y` and selects the branch minimizing both critical-equation residuals. It rejects any witness with a small arrangement denominator.

Replay:

```bash
python work_packages/VGSE_WP00/artifacts/code/replicate_b3.py \
  --check \
  --output /tmp/vgse_b3.json
python work_packages/VGSE_WP00/artifacts/code/test_replicate_b3.py
```

The expected machine-readable record is `work_packages/VGSE_WP00/artifacts/data/expected_replay.json`.

### Numerical limitation

The degree-five roots are floating-point witnesses. The exact root count for the selected fixture is not yet certified by interval isolation or quotient-algebra computation. MATHCERT should certify fixture genericity and either isolate all roots or certify the saturated quotient dimension and divisor exclusion.

## 10. Failure and negative-result analysis

### Attempted route

Treat every resultant root as a valid branch.

### Why it was plausible

Elimination returns a degree-six factorization before divisor filtering.

### Smallest exact obstruction

The extra factor gives `alpha_6=0`, where the master function is undefined.

### What the obstruction rules out

Unsaturated resultant degree may not be used as the algebraic solution count.

### What remains viable

Saturate by the product of all arrangement forms, or explicitly filter and separately certify all denominator-supported factors.

## 11. Proof-debt register

| Debt ID | Category | Blocked node | Current evidence | Discharge condition | Route or owner |
|---|---|---|---|---|---|
| `VGSE-D00` | `EXTERNAL_SOURCE` | `VGSE-S0` | Author PDF pinned by hash | Independent revision and bibliography audit | Axiomatist / Cartographer |
| `VGSE-D01` | `UNPROVED_BRIDGE` | `VGSE-S1` | Galashin proof cites Varchenko–Orlik–Terao | Reconstruct theorem hypotheses and projective reduction | Formalist |
| `VGSE-D02` | `COMPUTATIONAL_REPLAY` | `VGSE-S3` | Floating-point replay | Certified genericity plus root isolation or exact quotient-dimension certificate | MATHCERT |
| `VGSE-D03` | `SEMANTIC_CORRESPONDENCE` | `VGSE-S4` | Pair-level data only | Pin explicit graph, weights, Kasteleyn/discrete-holomorphic reconstruction, and render all five interiors | Verifier |
| `VGSE-D04` | `MISSING_LEMMA` | `VGSE-S5` | None | Continuous rigid-folding and collision-free path proof | Mechanical lane |
| `VGSE-D05` | `MISSING_LEMMA` | `VGSE-S6` | None | Finite-thickness conversion and manufacturing evidence | Engineering lane |

## 12. Certification boundary and MATHCERT handoff

### Pencil-and-paper claims

- The projectivized line equations follow from the pinned matrix.
- The exact rational incidence count gives `beta(C)=5`.
- The denominator-supported factor must be excluded.

### Machine-checked or replayed claims

- Five numerical critical-point witnesses for the regular-hexagon fixture.
- Floating-point residual, denominator, orthogonality, adjacent-minor, and winding checks.

### Exact certificate candidates

- canonical list of rational line equations and rational intersections;
- characteristic polynomial or intersection-poset certificate;
- exact derivation of the divisor-filtered resultant and saturated quotient-ring dimension;
- isolating rectangles for five complex roots;
- interval residual and nonzero-denominator bounds;
- genericity certificate for the selected boundary fixture.

### Formalization blockers

No current formal library is selected for complex root isolation, affine arrangement characteristic polynomials, or the t-embedding reconstruction theorem.

### First item for MATHCERT

Certify that the selected regular-hexagon fixture is generic for the invoked count and that its saturated chart ideal has exactly five isolated solutions away from `alpha_1...alpha_6=0`.

## 13. First executable step

- Input: the pinned matrix `C`, the five retained `(a_2,a_3)` witnesses, and an explicit reduced planar bipartite graph with positive weights realizing `C`.
- Operation: implement the discrete-holomorphic / Kenyon–Smirnov reconstruction for every retained pair and export face and edge coordinates.
- Output artifact: five deterministic SVG or JSON planar t-embedding records with convex-face, angle, edge-weight gauge, simple-boundary, and injectivity checks.
- Completion test: exactly five distinct internal geometries pass the t-embedding checks and reproduce one fixed kami boundary.
- Spine node advanced: `VGSE-S4`; debt discharged: `VGSE-D03`.

## 14. Escalation gate

- [x] The theorem-spine slice has been recorded.
- [x] Dependencies are named.
- [x] The proof-debt register is current.
- [x] The trust quartet is complete.
- [x] The foundational profile is present.
- [x] The first executable step is explicit.
- [x] The next package names the spine node it advances.
- [ ] Independent source audit complete.
- [ ] MATHCERT algebraic root-count certificate complete.
- [ ] Internal five-pattern reconstruction complete.

`VGSE-WP01` is not authorized as a commercial-design package. The only authorized continuation is the bounded geometric reconstruction of `VGSE-S4`.
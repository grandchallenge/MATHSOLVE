# VGSE-WP00 — Varchenko–Galashin Source, Semantics, and Five-Pattern Replication

## Metadata

- Campaign: `VGSE-001`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#170`
- Solve tracker: `grandchallenge/MATHSOLVE#84`
- Draft implementation: `grandchallenge/MATHSOLVE#85`
- Forge source intake: `grandchallenge/MATHFORGE#32`
- Cert intake: `grandchallenge/MATHCERT#41`
- Work Package number: `VGSE-WP00`
- Primary type: `SOURCE_NORMALIZATION_AND_BOUNDED_REPLICATION`
- Claim status: `COMPUTED_EXACTLY` for the arrangement count; `NEEDS_AUDIT` for the algebraic witnesses and source-vector geometry
- Foundational profile: present

## 1. Result-status box

| Field | Value |
|---|---|
| Result status | WP00 candidate with executable algebraic and geometric Figure 16 replays |
| Exact result | The Example B.1 projectivized arrangement has nine distinct finite intersections and `beta(C)=5` |
| Numerical algebraic result | The extracted Figure 16 boundary yields five divisor-excluding critical-point witnesses under the pinned labeling; each passes encoded residual, sign, winding, and orthogonality checks |
| Source-geometric result | The five Figure 16 vector drawings have been extracted into face-coordinate fixtures, validated at PDF precision, and rendered deterministically |
| Principal unresolved bridge | No algebraic witness has yet been matched to a source-vector pattern through the discrete-holomorphic and Kenyon–Smirnov construction |
| Not claimed | Certified genericity; exact root isolation; independent recovery of boundary measurement `C`; rigid foldability; collision freedom; finite thickness; manufacturability; product performance; novelty; priority; patentability; or commercial value |
| Certification state | Algebraic certificate candidate routed to MATHCERT #41; source-vector extraction review pending |
| Next executable step | Establish or refute the witness-to-pattern bijection by reconstructing all five Kenyon–Smirnov primitives |

## 2. Foundational profile

```yaml
foundational_profile:
  carrier_type: complex_projective_parameter_space_and_planar_piecewise_linear_geometry
  ambient_structure:
    - affine_hyperplane_arrangement_over_Q
    - complex_master_function_critical_locus
    - real_two_planes_in_R6
    - colored_planar_cell_complexes
  regularity:
    - generic_boundary_required_by_proposition_B2
    - arrangement_divisor_excluded
    - isolated_critical_points_required_for_exact_count
    - convex_non_degenerate_faces
  axiom_profile:
    base: classical_mathematics
    choice_usage: none_in_replay
    large_cardinal_usage: none
  witness_policy:
    algebraic: floating_point_witnesses_with_fail_closed_checks
    geometric: source_vector_coordinates_pinned_to_pdf_hash_and_drawing_indices
  pathology_risk:
    level: high
    notes: >-
      Unsaturated elimination contains divisor-supported roots. Source-vector
      geometry is rounded illustration data. Algebraic pairs, planar
      t-embeddings, rigid mechanisms, and manufactured products are distinct.
```

## 3. Source lock

Candidate primary source:

- Pavel Galashin, *Amplituhedra and Origami, I: Tree Level*.
- Author-hosted PDF dated `2026-06-03`.
- File size: `1,317,147` bytes.
- SHA-256: `e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de`.
- Target: Appendix B, Example B.1, Proposition B.2, Example B.3, Remark B.4, and Figure 16 on printed page 75.
- ArXiv identity: `2410.09574`; revision concordance remains a Forge audit item.

Figure 16 is embedded as PDF vector paths. The provenance utility
`artifacts/code/extract_figure16.py` refuses any PDF whose SHA-256 differs from the pinned value and extracts only the five expected eight-face components from page index 74.

## 4. Formal object

The pinned matrix is

```text
C = [[1, 1, 0, -6, 0,  3],
     [0, 1, 1,  7, 0, -2],
     [0, 0, 0,  2, 1,  3]].
```

In the chart `a=(1,x,y)`, the arrangement forms are

```text
alpha_1 = 1
alpha_2 = 1+x
alpha_3 = x
alpha_4 = -6+7x+2y
alpha_5 = y
alpha_6 = 3-2x+3y.
```

The five projectivized affine lines are

```text
x=-1,
x=0,
7x+2y=6,
y=0,
-2x+3y=-3.
```

For boundary increments `z_i`, the master equation is

```text
sum_i z_i C_i / alpha_i(a) = 0.
```

The Figure 16 boundary is extracted from the first source-vector pattern. Coordinates are translated, the PDF y-axis is inverted, and values are rounded to `1e-6` PDF point. The algebraic fixture keeps source vertex 0 as anchor and traverses the polygon counterclockwise. The printed figure does not label its boundary vertices, so this cyclic-label convention is an explicit campaign choice rather than a source fact.

## 5. Exact arrangement replay

The five lines contain one parallel pair and nine distinct finite intersections. No finite intersection is triple. For an essential affine line arrangement in rank two,

```text
beta = 1 - number_of_lines + sum_p (multiplicity(p)-1).
```

Therefore

```text
beta(C) = 1 - 5 + 9 = 5.
```

This is an exact finite computation over rational line data.

## 6. Figure 16 boundary algebraic replay

Exact rational/Gaussian-integer elimination for the rounded Figure 16 boundary produces an unsaturated resultant with factor degrees

```text
1, 1, 1, 3, 3, 5.
```

The factors outside the quintic are arrangement-divisor contamination:

| Factor | Divisor support |
|---|---|
| `x^3` | `alpha_3=0` |
| `(x+1)^3` | `alpha_2=0` |
| `2x-3`, companion `y=0` | `alpha_5=alpha_6=0` |
| `7x-6`, companion `y=0` | `alpha_4=alpha_5=0` |
| `25x-24`, companion `y=-9/25` | `alpha_4=alpha_6=0` |

After these factors are excluded, the retained factor has degree five. The standard-library replay uses deterministic Durand–Kerner iteration and quadratic recovery of `y`. It records five witnesses with:

- scaled quintic and chart-equation residuals;
- positive distance from every arrangement divisor;
- numerical `lambda perpendicular to tilde_lambda` checks;
- positive adjacent minors;
- winding values `2*pi` and `4*pi`.

These are numerical witnesses. Genericity, exact quotient dimension, root separation, and interval residual bounds remain certification debts.

## 7. Five-pattern source-vector replication

The source-vector fixture records five patterns, each with:

- one common six-vertex boundary, with maximum cross-pattern discrepancy `3.1e-5` PDF point;
- eight convex faces: four black and four white;
- nine dual vertices, including three interior vertices;
- sixteen dual edges;
- a reconstructed bipartite primal topology with eight interior vertices, six boundary vertices, ten internal edges, and sixteen total edges.

The validator checks:

1. nonzero straight edges;
2. convex consistently oriented faces;
3. identity gauge after assigning each reconstructed primal edge its observed geometric length;
4. Kawasaki black and white angle sums at interior vertices to a `0.04` radian PDF-precision tolerance;
5. strict boundary angle conditions;
6. exact edge incidence and bipartite coloring;
7. face-area partition of the simple common boundary;
8. deterministic SVG rendering of all five patterns.

The largest Kawasaki residual is about `0.03524` radians. This is accepted only as an illustration-precision check. It is not an exact theorem certificate.

Galashin labels these drawings as the five t-embeddings of Example B.3. The campaign has replicated that source geometry, but it has not independently shown that the reconstructed weighted graphs have boundary measurement `C`.

## 8. Required level distinction

The pipeline is fail-closed across four levels:

| Level | Current state |
|---|---|
| Algebraic solutions | Exact arrangement count; five uncertified numerical witnesses for the Figure 16 boundary |
| Real planar t-embeddings | Five literature-identified source-vector patterns replicated and checked at PDF precision; independent `C` correspondence still open |
| Rigidly deployable mechanisms | Not assessed |
| Manufacturable products | Not assessed |

The present evidence does not permit promotion from one row to the next.

## 9. Claim ledger summary

| Claim | Status |
|---|---|
| `beta(C)=5` for Example B.1 | `COMPUTED_EXACTLY` |
| Five Figure 16 boundary witnesses | `NEEDS_AUDIT` |
| Numerical sign, winding, divisor, and orthogonality checks | `NEEDS_AUDIT` |
| Five source-vector geometries reproduced | `NEEDS_AUDIT` |
| Witness-to-pattern bijection reconstructed | Open |
| Rigid deployment or manufacturability follows | Refuted as an inference |
| Commercial promotion is authorized | Refuted as an inference and prohibited |

The machine-readable authority is `work_packages/VGSE_WP00/claim_ledger.json`.

## 10. Theorem-spine slice

| Node | Role | Status | Discharge criterion |
|---|---|---|---|
| `VGSE-S0` | Pin source and semantics | Candidate complete | Independent Forge review |
| `VGSE-S1` | Audit Varchenko–Orlik–Terao bridge | Open | Primary-source hypothesis audit |
| `VGSE-S2` | Exact arrangement count | Complete | Independent replay |
| `VGSE-S3` | Five Figure 16 boundary witnesses | Numerical replay complete | MATHCERT genericity and exact root-count certificate |
| `VGSE-S4A` | Replicate five source-vector geometries | Candidate complete | Independent extractor and tolerance review |
| `VGSE-S4B` | Match witnesses to patterns | Open | Five Kenyon–Smirnov reconstructions and bijective match |
| `VGSE-S5` | Continuous collision-free rigid deployment | Gated | Kinematic path, layer order, and collision certificate |
| `VGSE-S6` | Finite-thickness manufactured structure | Gated | Prototype, tolerance, mechanics, process, and economics evidence |

## 11. Failure analysis

### Failure F1 — unsaturated root counting

Counting every resultant factor gives false extra solutions on deleted hyperplanes. The replay explicitly records and rejects all divisor-supported factors.

### Failure F2 — substituting a convenient boundary

The initial provisional replay used a regular hexagon. That fixture was replaced by the actual Figure 16 vector boundary. A regular polygon may remain a separate conjectural test lane, but it is not the Example B.3 replication boundary.

### Failure F3 — treating figure extraction as inverse reconstruction

Extracting the five vector drawings demonstrates source fidelity, not that the algebraic solver generated those drawings. The correspondence node `VGSE-S4B` remains open.

### Failure F4 — promoting planar geometry to physical structure

A flat planar t-embedding does not establish a continuous rigid-folding path, collision freedom, finite panel thickness, hinge design, fatigue life, or manufacturing cost.

## 12. Proof-debt register

| Debt | Category | State | Discharge condition |
|---|---|---|---|
| `VGSE-D00` | Source | Open | Independent revision, theorem, figure, and bibliography audit |
| `VGSE-D01` | Literature bridge | Open | Verify all hypotheses of Proposition B.2 and its cited theorem chain |
| `VGSE-D02` | Algebraic certification | Open | Certify labeling, genericity, saturation, and exactly five isolated roots |
| `VGSE-D03` | Source geometry | Partially discharged | Independent extractor replay and precision-tolerance review |
| `VGSE-D04` | Semantic correspondence | Open | Recover graph, Kasteleyn data, weights, holomorphic extensions, and five primitives |
| `VGSE-D05` | Mechanical lift | Gated | Continuous collision-free rigid deployment evidence |
| `VGSE-D06` | Product lift | Gated | Finite-thickness prototype and application benchmark |

The machine-readable authority is `work_packages/VGSE_WP00/proof_obligations.json`.

## 13. Reproduction

The governed CI path uses only the Python standard library after checkout:

```bash
python work_packages/VGSE_WP00/artifacts/code/replicate_b3.py \
  --check \
  --output /tmp/vgse_b3.json
python work_packages/VGSE_WP00/artifacts/code/test_replicate_b3.py
python work_packages/VGSE_WP00/artifacts/code/validate_figure16.py \
  work_packages/VGSE_WP00/artifacts/data/figure16_source_vectors.json \
  --report /tmp/vgse_figure16_validation.json \
  --svg-dir /tmp/vgse_figure16_svg
python work_packages/VGSE_WP00/artifacts/code/test_figure16.py
```

The provenance extractor is deliberately outside the ordinary CI dependency set:

```bash
python work_packages/VGSE_WP00/artifacts/code/extract_figure16.py \
  /path/to/pinned/t_embeddings_v2.pdf \
  --output /tmp/figure16_source_vectors.json
```

It requires PyMuPDF 1.26.7 and the exact pinned PDF hash.

## 14. Certification boundary

MATHCERT may presently certify only:

- the exact arrangement incidence certificate;
- the exact elimination and divisor saturation for the rounded boundary fixture;
- boundary-label genericity;
- five isolated roots and nonzero denominator bounds;
- interval or exact versions of the encoded pair checks.

A separate certificate would be required for:

- source-vector extraction fidelity;
- boundary measurement `C` of a reconstructed graph;
- the discrete-holomorphic witness-to-pattern correspondence;
- rigid foldability or product engineering.

## 15. Next executable obligation

`VGSE-S4B` is authorized.

Required operation:

1. recover an explicit planar bipartite graph and boundary labeling compatible with the five source patterns;
2. recover or solve for Kasteleyn signs and positive edge weights realizing the pinned `C`;
3. extend each witness's boundary data to discrete holomorphic functions;
4. integrate the five Kenyon–Smirnov primitives;
5. match the resulting face coordinates to the source-vector patterns modulo the declared equivalence group;
6. record a bijection, ambiguity class, or precise failure.

Completion requires five independently generated geometries and a machine-checkable correspondence. Source-vector copying alone does not discharge this node.

## 16. Commercial promotion gate

No commercial claim is authorized. Promotion requires, in order:

```text
certified algebraic branch
-> independently reconstructed planar t-embedding
-> continuous collision-free rigid mechanism
-> finite-thickness manufactured prototype
-> application-specific performance and economic evidence.
```

Novelty, priority, patentability, and freedom-to-operate require separate prior-art and legal review.
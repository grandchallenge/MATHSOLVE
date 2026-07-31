# VGSE-WP00 — Varchenko–Galashin Source, Semantics, and Five-Pattern Replication

## Metadata

- Campaign: `VGSE-001`
- Programme tracker: `grandchallenge/MATH-PROGRAMME#170`
- Solve tracker: `grandchallenge/MATHSOLVE#84`
- Draft implementation: `grandchallenge/MATHSOLVE#85`
- Forge source intake: `grandchallenge/MATHFORGE#32`
- Cert intake: `grandchallenge/MATHCERT#41`
- Work Package: `VGSE-WP00`
- Primary type: `SOURCE_NORMALIZATION_AND_BOUNDED_REPLICATION`
- Disposition: `CANDIDATE_COMPLETE_PENDING_REVIEW_AND_CERTIFICATION`
- Claim status: `COMPUTED_EXACTLY` for the arrangement count; `NEEDS_AUDIT` for numerical roots, weights, and reconstructed t-embeddings

## 1. Result-status box

| Field | Value |
|---|---|
| Exact result | The Example B.1 projectivized arrangement has nine distinct finite intersections and `beta(C)=5` |
| Numerical algebraic result | The extracted Figure 16 boundary yields five divisor-excluding critical-point witnesses |
| Source-replication result | The five vector drawings in Figure 16 have been extracted, normalized, validated at PDF precision, and rendered deterministically |
| Independent reconstruction result | A positive weighted reduced graph numerically reproduces `C`; the five witnesses extend through that graph to five distinct convex Kenyon–Smirnov t-embeddings with the prescribed boundary |
| Certification state | Root, weight, boundary-measurement, and reconstruction certificates remain open under MATHCERT #41 |
| Not claimed | Continuous rigid foldability, collision freedom, finite thickness, manufacturability, product performance, novelty, priority, patentability, or commercial value |
| Next governed obligation | `VGSE-WP00-CERT-001`, followed by a generated-to-source equivalence record; the mechanical lane remains gated |

## 2. Foundational profile

```yaml
foundational_profile:
  carrier_type:
    - complex_projective_parameter_space
    - weighted_planar_bipartite_graph
    - colored_planar_cell_complex
  ambient_structure:
    - affine_hyperplane_arrangement_over_Q
    - complex_master_function_critical_locus
    - positive_grassmannian_boundary_measurement
    - discrete_holomorphic_extension
    - Kenyon_Smirnov_primitive
  regularity:
    - generic_boundary_required_by_Proposition_B2
    - arrangement_divisor_excluded
    - isolated_critical_points
    - positive_edge_weights
    - convex_non_degenerate_faces
  axiom_profile:
    base: classical_mathematics
    choice_usage: none_in_replay
    large_cardinal_usage: none
  witness_policy:
    algebraic: floating_point_witnesses_with_fail_closed_checks
    graph: positive_numerical_weight_representative
    geometry: independently_generated_numeric_coordinates
  pathology_risk:
    level: high
    notes: >-
      Unsaturated elimination contains divisor-supported roots. The graph
      weights and roots are numerical. Algebraic solutions, planar
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
`artifacts/code/extract_figure16.py` rejects any PDF whose SHA-256 differs from the pinned value and extracts only the five expected eight-face components from zero-based page 74.

## 4. Formal object

The pinned matrix is

```text
C = [[1, 1, 0, -6, 0,  3],
     [0, 1, 1,  7, 0, -2],
     [0, 0, 0,  2, 1,  3]].
```

In the projective chart `a=(1,x,y)`, the arrangement forms are

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

The Figure 16 boundary is extracted from the first source-vector pattern. Coordinates are translated, the PDF y-axis is inverted, and values are rounded to `1e-6` PDF point. The algebraic fixture fixes source vertex 0 and traverses the polygon counterclockwise. The printed figure does not label boundary vertices, so this cyclic-label convention is an explicit campaign choice.

## 5. Exact arrangement replay

The five affine lines contain one parallel pair and nine distinct finite intersections. No finite intersection is triple. For an essential rank-two affine arrangement,

```text
beta = 1 - number_of_lines + sum_p (multiplicity(p)-1).
```

Therefore

```text
beta(C) = 1 - 5 + 9 = 5.
```

This is an exact finite computation over rational line data.

## 6. Figure 16 boundary algebraic replay

Exact rational and Gaussian-integer elimination for the rounded Figure 16 boundary produces an unsaturated resultant with factor degrees

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

## 7. Figure 16 source-vector replication

The source-vector fixture records five patterns. Each has:

- one common six-vertex boundary, with maximum cross-pattern discrepancy `3.1e-5` PDF point;
- eight convex faces, four black and four white;
- nine dual vertices, including three interior vertices;
- sixteen dual edges;
- the same reconstructed bipartite primal topology, with eight interior vertices, six boundary vertices, ten internal edges, and sixteen total edges.

The source validator checks nonzero edges, convexity, incidence, bipartite coloring, area partition, strict boundary angles, and deterministic SVG rendering. It also checks the black and white Kawasaki angle sums at the three interior vertices to a `0.04` radian illustration-precision tolerance. The largest source-drawing residual is about `0.03524` radians. This is source fidelity evidence, not an exact t-embedding certificate.

## 8. Reconstructed graph and boundary measurement

The reduced graph topology is inferred from the common Figure 16 face incidence. Its ten internal and six boundary edges are assigned the positive numerical representative recorded in
`artifacts/data/graph_weight_fixture.json`.

The replay enumerates all almost-perfect matchings and obtains:

```text
almost-perfect matchings: 31
nonzero Plucker coordinates: 19
common normalization scale: 0.03219543143791925
maximum absolute coordinate residual: 7.105427357601002e-15
maximum relative coordinate residual: 6.661338147750939e-16
Kasteleyn sign residual: 0
```

The support and all nineteen nonzero Plücker coordinates agree with the pinned matrix `C` up to one common projective scale. The agreement is numerical. Exact or interval-certified weights have not been produced.

## 9. Independent five-pattern reconstruction

For each of the five algebraic witnesses, the replay:

1. forms `zeta_i=alpha_i(a)` and `tilde_zeta_i=z_i/zeta_i`;
2. applies the boundary restriction maps;
3. solves the two discrete-holomorphic extension systems on the reconstructed weighted graph;
4. forms each oriented dual-edge increment
   `F(white) K(white,black) F_tilde(black)`;
5. integrates the Kenyon–Smirnov primitive;
6. fixes the translation by the first prescribed boundary vertex;
7. reconstructs all dual vertices and eight colored faces;
8. checks convexity, the prescribed boundary, primitive closure, area partition, Kawasaki sums, and boundary-angle inequalities.

The governed summary records five distinct generated patterns. Across them:

- generated pattern count: `5`;
- minimum pairwise maximum internal-coordinate distance: `21.439643306067115`;
- maximum prescribed-boundary residual: below `2e-12`;
- maximum primitive-closure residual: below `2e-12`;
- maximum Kawasaki residual: below `2e-14`;
- every pattern has eight strictly convex faces;
- every boundary-angle margin is positive;
- every generated pattern is assigned status `NUMERICALLY_RECONSTRUCTED_T_EMBEDDING_NEEDS_AUDIT`.

This discharges the prior structural gap at the numerical-replay level: the five master-function witnesses now generate five independent planar t-embeddings through an explicit weighted graph. It does not convert the result into an exact proof.

A separate equivalence matcher between the generated coordinate sets and the rounded Figure 16 source drawings remains open. The mathematical five-pattern replication does not depend on copying the source coordinates, but source-figure concordance should still be recorded.

## 10. Required level distinction

The pipeline remains fail-closed:

| Level | Current state |
|---|---|
| Algebraic solutions | Exact generic branch target `beta(C)=5`; five uncertified numerical Figure 16 boundary witnesses |
| Real planar t-embeddings | Five independently generated numerical t-embeddings with convex faces, prescribed boundary, positive boundary-angle margins, and machine-scale closure/Kawasaki residuals |
| Rigidly deployable mechanisms | Not assessed; no mountain-valley, layer-order, motion-path, actuation, or collision certificate |
| Manufacturable products | Not assessed; no finite-thickness conversion, hinge design, material model, prototype, process, durability, cost, or application benchmark |

No evidence from an earlier row may be promoted into a later row without its separate gate.

## 11. Claim ledger summary

| Claim | Status |
|---|---|
| `beta(C)=5` for Example B.1 | `COMPUTED_EXACTLY` |
| Five Figure 16 boundary witnesses | `NEEDS_AUDIT` |
| Numerical sign, winding, divisor, and orthogonality checks | `NEEDS_AUDIT` |
| Five source-vector geometries reproduced | `NEEDS_AUDIT` |
| Positive weighted graph numerically reproduces `C` | `NEEDS_AUDIT` |
| Five independent numerical Kenyon–Smirnov t-embeddings reconstructed | `NEEDS_AUDIT` |
| Generated-to-source equivalence bijection | Open |
| Rigid deployment or manufacturability follows | Refuted as an inference |
| Commercial promotion is authorized | Refuted as an inference and prohibited |

The machine-readable authority is `work_packages/VGSE_WP00/claim_ledger.json`.

## 12. Theorem-spine slice

| Node | Role | Status | Discharge criterion |
|---|---|---|---|
| `VGSE-S0` | Pin source and semantics | Candidate complete | Independent Forge review |
| `VGSE-S1` | Audit Varchenko–Orlik–Terao bridge | Open | Primary-source hypothesis audit |
| `VGSE-S2` | Exact arrangement count | Complete | Independent replay |
| `VGSE-S3` | Five Figure 16 boundary witnesses | Numerical replay complete | MATHCERT genericity and exact root-count certificate |
| `VGSE-S4A` | Replicate five source-vector geometries | Candidate complete | Independent extractor and tolerance review |
| `VGSE-S4B` | Recover weighted graph and boundary measurement `C` | Numerical replay complete | Independent positive-weight solve and exact or interval certification |
| `VGSE-S4C` | Generate five t-embeddings from the five witnesses | Numerical replay complete | Certified linear solves, primitive integration, and geometric inequalities |
| `VGSE-S4D` | Match generated and source-vector patterns | Open | Admitted permutation and geometric-equivalence record |
| `VGSE-S5` | Continuous collision-free rigid deployment | Gated | Mountain-valley, layer-order, kinematic path, actuation, and collision certificate |
| `VGSE-S6` | Finite-thickness manufactured structure | Gated | Prototype, tolerance, mechanics, process, durability, and economics evidence |

## 13. Failure analysis

### F1 — unsaturated root counting

Counting every resultant factor gives false extra solutions on deleted hyperplanes. The replay records and rejects all divisor-supported factors.

### F2 — substituting a convenient boundary

The initial provisional replay used a regular hexagon. That fixture was replaced by the actual Figure 16 vector boundary.

### F3 — treating figure extraction as inverse reconstruction

Source-vector extraction demonstrates source fidelity only. The independent graph, boundary-measurement, discrete-holomorphic, and primitive pipeline was therefore implemented separately.

### F4 — treating numerical agreement as certification

Machine-scale residuals do not replace exact root isolation, exact or interval weights, or certified geometric inequalities. All such claims retain `NEEDS_AUDIT` status.

### F5 — promoting planar geometry to physical structure

A planar t-embedding does not establish a continuous rigid-folding path, collision freedom, finite panel thickness, hinge design, fatigue life, production feasibility, or customer value.

## 14. Proof-debt register

| Debt | Category | State | Discharge condition |
|---|---|---|---|
| `VGSE-D00` | Source | Open | Independent revision, theorem, figure, and bibliography audit |
| `VGSE-D01` | Literature bridge | Open | Verify all hypotheses of Proposition B.2 and its cited theorem chain |
| `VGSE-D02` | Algebraic certification | Open | Certify labeling, genericity, saturation, and exactly five isolated roots |
| `VGSE-D03` | Source geometry | Partially discharged | Independent extractor replay and precision-tolerance review |
| `VGSE-D04` | Graph and weights | Partially discharged | Independent weight solve and exact or interval-certified boundary measurement |
| `VGSE-D05` | T-embedding reconstruction | Partially discharged | Certify extensions, primitive closure, convexity, Kawasaki, and boundary inequalities; admit generated-to-source equivalence record |
| `VGSE-D06` | Mechanical lift | Gated | Continuous collision-free rigid deployment evidence |
| `VGSE-D07` | Product lift | Gated | Finite-thickness prototype and application benchmark |

The machine-readable authority is `work_packages/VGSE_WP00/proof_obligations.json`.

## 15. Reproduction

The governed CI path uses only the Python standard library after checkout:

```bash
python work_packages/VGSE_WP00/artifacts/code/replicate_b3.py \
  --check \
  --output /tmp/vgse_b3.json
python work_packages/VGSE_WP00/artifacts/code/test_replicate_b3.py

python work_packages/VGSE_WP00/artifacts/code/validate_figure16.py \
  work_packages/VGSE_WP00/artifacts/data/figure16_source_vectors.json \
  --report /tmp/vgse_figure16_validation.json \
  --svg-dir /tmp/vgse_figure16_source_svg
python work_packages/VGSE_WP00/artifacts/code/test_figure16.py

python work_packages/VGSE_WP00/artifacts/code/reconstruct_b3.py \
  work_packages/VGSE_WP00/artifacts/data/figure16_source_vectors.json \
  work_packages/VGSE_WP00/artifacts/data/expected_replay.json \
  work_packages/VGSE_WP00/artifacts/data/graph_weight_fixture.json \
  --check \
  --output /tmp/vgse_reconstructed.json \
  --svg-dir /tmp/vgse_reconstructed_svg
python work_packages/VGSE_WP00/artifacts/code/test_reconstruct_b3.py
```

The source-provenance extractor is deliberately outside the ordinary CI dependency set:

```bash
python work_packages/VGSE_WP00/artifacts/code/extract_figure16.py \
  /path/to/pinned/t_embeddings_v2.pdf \
  --output /tmp/figure16_source_vectors.json
```

It requires PyMuPDF 1.26.7 and the exact pinned PDF hash.

## 16. Certification boundary

MATHCERT may presently certify:

- the exact arrangement incidence certificate;
- the exact elimination and divisor saturation for the rounded boundary fixture;
- boundary-label genericity;
- exactly five isolated roots and nonzero denominator bounds;
- interval or exact versions of the pair checks;
- the reduced graph's almost-perfect-matching enumeration;
- positive weights and boundary measurement `C`;
- the discrete-holomorphic extension systems;
- primitive closure and prescribed boundary;
- convexity, Kawasaki, and boundary-angle inequalities for five generated patterns.

Separate evidence remains required for source-vector equivalence, rigid deployment, and product engineering.

## 17. WP00 disposition and next obligation

`VGSE-WP00` is candidate-complete within its bounded scope. It now contains:

1. a source and claim-semantics lock;
2. an exact `beta(C)=5` arrangement replay;
3. five Figure 16 boundary algebraic witnesses;
4. five source-vector pattern records;
5. a reduced positive weighted graph numerically reproducing `C`;
6. five independently generated numerical t-embeddings.

The next authorized obligation is `VGSE-WP00-CERT-001`: independently certify the roots, weights, boundary measurement, discrete-holomorphic extensions, primitives, and geometric inequalities, then admit the generated-to-source equivalence record.

`VGSE-S5`, the mechanical lane, remains gated until WP00 review and certification. `VGSE-S6`, the finite-thickness and product lane, remains gated behind `VGSE-S5`.

## 18. Commercial promotion gate

No commercial claim is authorized. Promotion requires, in order:

```text
certified algebraic branch
-> certified planar t-embedding
-> continuous collision-free rigid mechanism
-> finite-thickness manufactured prototype
-> application-specific performance and economic evidence.
```

Novelty, priority, patentability, and freedom-to-operate require separate prior-art and legal review.
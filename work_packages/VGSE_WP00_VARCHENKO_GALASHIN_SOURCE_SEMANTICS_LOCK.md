# VGSE-WP00 — Candidate Source, Semantics, and Five-Pattern Replay

## Authority and lifecycle

- Candidate: `VGSE-001`.
- Lifecycle: `candidate`; not an active Programme or MATHSOLVE campaign.
- Protected candidate work package: merged.
- Reviewed Solve head: `0d66a75412543e534b81c21a51a6ad88c035b55b`.
- Solve merge commit: `709c7d3f388b8df75c87a247f80424e560c31e72`.
- Programme candidate authority: MATH-PROGRAMME merge `d56edc23152f3ccde4c7db272b7af37f6cf698b9`.
- Candidate registry: `governance/campaign_admission_registry.json`, blob `a6bffaa197aa3921e3eb9d4f8a02b5dc2bbded24`.
- Runtime contract: `governance/umbrella_runtime_contract_v4.json`, blob `02cdfabb04f5d273fcb7531c515a73baab2bc52d`.
- Programme mirrors: candidate tracker #170, current governance #175, completed governance #172.
- Forge mirror: #32, provider manifest pending.
- Solve work-package mirror: issue #84; implementation PR #85 is merged.
- Cert mirror: #41, state `pre_route_candidate`; no route exists.

The machine-readable local authority is `work_packages/VGSE_WP00/candidate_admission.json`. GitHub issues and this document are navigation and explanation mirrors. They cannot admit the campaign, verify the source, create a Cert route, or promote a claim.

## Provenance state

The working source is a candidate copy of Pavel Galashin, *Amplituhedra and Origami, I: Tree Level*, printed date `2026-06-03`.

- Candidate byte length: `1,317,147`.
- Candidate SHA-256: `e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de`.
- Target scope: Appendix B, Examples B.1 and B.3, Proposition B.2, Remark B.4, and Figure 16.
- Current state: `unverified_candidate`.
- Provider manifest: none.
- Revision and arXiv concordance: open under MATHFORGE #32.

The checksum is a candidate reproducibility lock. It is not provider verification. The legacy generated-report field `source.author_pdf_sha256` carries this candidate checksum only and must not be interpreted as a verified source identity. The extractor rejects a different input so that the candidate replay remains reproducible while Forge review is pending.

The merged package uses a candidate extraction of the Figure 16 vector boundary. It does not use the earlier provisional regular-hexagon fixture.

## Bounded result-status box

| Layer | Current status |
|---|---|
| Five-line arrangement and `beta(C)=5` | `COMPUTED_EXACTLY` for the recorded rational fixture |
| Five divisor-excluding critical-point witnesses | Numerical replay; `NEEDS_AUDIT` |
| Five source-vector geometries | Deterministic candidate extraction and PDF-precision checks; `NEEDS_AUDIT` |
| Positive weighted graph reproducing `C` | Numerical replay; `NEEDS_AUDIT` |
| Five generated planar t-embeddings | Numerical reconstruction; `NEEDS_AUDIT` |
| Genericity, exact root count, weights, and geometric inequalities | Open certification debt |
| Generated-to-source equivalence bijection | Open |
| Continuous rigid deployment | Not assessed |
| Finite-thickness manufacture | Not assessed |
| Novelty, priority, patentability, or commercial value | Not authorized |

MATHCERT #41 is a pre-route candidate mirror. It is not a certification intake, adjudication, or certificate output. A certification route may be proposed only after protected Programme admission and a content-addressed Solve handoff.

## Formal fixture

The recorded matrix is

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

The five affine lines are

```text
x=-1
x=0
7x+2y=6
y=0
-2x+3y=-3.
```

They have one parallel pair, nine distinct finite intersections, and no finite triple intersection. For this rank-two affine fixture,

```text
beta = 1 - 5 + 9 = 5.
```

This is an exact finite arrangement computation. Source identity and theorem-chain concordance remain separate obligations.

## Algebraic replay

For the rounded candidate Figure 16 boundary, elimination produces factor degrees

```text
1, 1, 1, 3, 3, 5.
```

The non-quintic factors are rejected as arrangement-divisor contamination. The retained quintic yields five floating-point witnesses. The replay checks scaled residuals, divisor separation, numerical orthogonality, positive adjacent minors, and winding values. It does not certify genericity, quotient dimension, root isolation, or separation.

## Source-vector and independent geometry lanes

The source-vector lane extracts five eight-face drawings from the candidate PDF and checks common boundary, incidence, convexity, area partition, boundary angles, and approximate Kawasaki sums. This is candidate-source fidelity evidence, not a formal t-embedding certificate.

The independent lane reconstructs a reduced bipartite topology, records positive numerical weights, enumerates 31 almost-perfect matchings, and numerically reproduces the support and nineteen nonzero Plücker coordinates of `C` up to one projective scale. It extends the five algebraic witnesses through numerical discrete-holomorphic solves and Kenyon–Smirnov primitives to five distinct planar coordinate sets.

The generated patterns satisfy machine-scale closure and boundary residuals and positive numerical geometric margins in the recorded fixture. Exact or interval-certified weights, solves, convexity, Kawasaki equalities, and generated-to-source equivalence remain open.

## Required separation of levels

1. Candidate source checksum and extracted vectors.
2. Exact finite arrangement computation.
3. Numerical algebraic witnesses.
4. Numerical weighted-graph and planar t-embedding reconstruction.
5. Certified algebraic and geometric claims.
6. Continuous collision-free rigid mechanism.
7. Finite-thickness manufactured structure.
8. Application performance, economics, novelty, priority, patentability, or commercial claims.

No earlier level implies a later level.

## Fail-closed post-merge boundary

The bounded candidate code, data, ledgers, rendered artifacts, and tests are merged. That merge may not create:

- `campaign_manifests/VGSE-001.json`;
- `cert_handoffs/VGSE-001.json`;
- a MATHCERT route or adjudication;
- an active Programme or Solve route;
- a promotion record;
- provider-verified source status.

The candidate-admission tests reject any such inflation.

## Remaining proof debt

- `VGSE-D00`: Forge source identity, revision, theorem, figure, and bibliography audit.
- `VGSE-D01`: Varchenko–Orlik–Terao hypothesis and implication audit.
- `VGSE-D02`: genericity, saturation, exact root count, and root isolation.
- `VGSE-D03`: independent extractor and source-precision review.
- `VGSE-D04`: exact or interval-certified positive weights and boundary measurement.
- `VGSE-D05`: certified discrete-holomorphic solves, primitive integration, convexity, Kawasaki, and boundary inequalities.
- `VGSE-D06`: generated-to-source equivalence record.
- `VGSE-D07`: continuous rigid-folding and collision analysis.
- `VGSE-D08`: finite-thickness prototype, process, durability, performance, and economics.

## Claim boundary

`VGSE-001` remains a pre-admission candidate. The source remains unverified. No Cert route exists. The package does not establish a certified five-root theorem, certified t-embedding equivalence, rigid foldability, collision freedom, finite thickness, manufacturability, novelty, priority, patentability, or commercial value.

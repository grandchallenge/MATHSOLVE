# OM26-H1 formal and replay environment

**State:** `BASELINE_CONCORDANCE_PASS`

## Exact internal scorer

The independent scorer is implemented at `kobon_scorer.py` with integer normalization, determinant predicates and `fractions.Fraction` exact intersections. No floating-point predicate is trusted.

The locked baseline `baseline/solution.json` has SHA-256:

`fee1fa08e700ba5849c3d1849cc10d2d3a50a44b3d838d560cd08f9a0de2b271`

Independent result:

- `n = 18`;
- `triangles = 16`;
- 153 arrangement vertices;
- 288 bounded arrangement edges;
- supporting-line triples exactly `[i,i+1,i+2]` for `i=0,...,15`;
- six bounded adversarial/unit cases PASS.

Receipt: `BASELINE_INTERNAL_RECEIPT.json`.

## AutoLab evaluator cross-check

Authenticated AutoLab acquisition succeeded using the repository Actions secret without exposing it. The public hill pull identified:

- hill: `alejandrozu/kobon-triangles`;
- public snapshot: `7d3f1d91dcb8`;
- manifest: `kobon-triangles 0.1.0`;
- hill spec: `2`.

The public package omits `private/` regression fixtures. Accordingly, the Hills CLI marks a working-tree local score as unofficial. The source lock already states that those fixtures validate the evaluator and are not hidden target data.

The identical baseline was evaluated with:

```sh
uv tool run --from hills==0.11.0 hills eval baseline \
  -H kobon-triangles --current --json
```

Observed AutoLab/Hills result:

```text
PASSED triangles=16 (max)
unofficial dirty-tree
```

Workflow evidence: run `36354367463`, job `108719011813`.

Receipt: `BASELINE_AUTOLAB_RECEIPT.json`.

## Gate disposition

The independent scorer and authenticated AutoLab public evaluator agree exactly at **16** on the same `solution.json`. H1-01 is PASS and bounded construction search may proceed.

This does not convert the local AutoLab report into an official competition score. Candidate promotion still requires H1-07 independent adversarial replay, and final submission still requires H1-11 live hill concordance.

## Reproducibility outputs

Retain the exact `solution.json`, scorer commit, normalized line identities, counted supporting-line triples, AutoLab public snapshot identity, evaluator package version, reports/receipts, and workflow run/job identities.

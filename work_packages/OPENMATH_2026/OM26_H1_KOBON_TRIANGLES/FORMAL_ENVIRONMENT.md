# OM26-H1 formal and replay environment

**State:** `GCL_EXACT_PASS__AUTOLAB_REPLAY_BLOCKED_AUTH`

## Exact internal scorer

The independent scorer is implemented at `kobon_scorer.py`. It uses:

- Python 3;
- integer normalization and determinant predicates;
- `fractions.Fraction` for exact intersections;
- no floating-point predicate in the trusted scoring path.

The exact source-reported baseline in `baseline/solution.json` has SHA-256:

`fee1fa08e700ba5849c3d1849cc10d2d3a50a44b3d838d560cd08f9a0de2b271`

Independent replay result:

- `n = 18`;
- `triangles = 16`;
- 153 arrangement vertices;
- 288 bounded arrangement edges;
- counted supporting-line triples exactly `[i,i+1,i+2]` for `i=0,...,15`.

The bounded adversarial/unit suite passes six cases covering ordinary triangles, concurrency, parallelism, subdivision, the exact baseline pattern, and proportional duplicate rejection.

Durable receipt: `BASELINE_INTERNAL_RECEIPT.json`.

## AutoLab reference evaluator

The captured hill displays:

```sh
autolab hills check kobon-triangles
uv tool run --from hills==0.11.0 hills eval <submission-directory> -H kobon-triangles
```

The dedicated GitHub Actions gate installed the official AutoLab CLI successfully and then attempted the official hill-pull path. Three bounded attempts established the current boundary:

1. run `36327965999`, job `108644289208`: no local hill materialized;
2. run `36328034870`, job `108644483691`: official `autolab hills pull` required login;
3. run `36328112782`, job `108644696152`: workflow failed closed because `AUTOLAB_TOKEN` is unavailable.

The AutoLab/Hills evaluator has therefore **not run** against the baseline. There is no score discrepancy to adjudicate because there is no external score result yet.

## Gate rule

Construction search remains forbidden until the exact same `baseline/solution.json` receives `triangles = 16` from the AutoLab/Hills evaluator. If a different score is returned, stop and reconcile the evaluator semantics before any search.

## Authentication boundary

Provision `AUTOLAB_TOKEN` only through GitHub Actions repository/organization secrets with access to `grandchallenge/MATHSOLVE`. Do not paste the token into chat, commit it, echo it, or store it in repository files.

## Reproducibility outputs

Retain `solution.json`, normalized line identities, intersection/incidence digest, counted supporting-line triples, exact score, scorer commit, evaluator output, and runtime metadata. Search runtime is diagnostic only.

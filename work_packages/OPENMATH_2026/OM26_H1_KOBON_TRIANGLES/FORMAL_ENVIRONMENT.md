# OM26-H1 formal and replay environment

**State:** `SPECIFIED__BASELINE_REPLAY_PENDING`

## Exact internal scorer

Preferred first implementation is deliberately small and auditable:

- Python 3;
- integer arithmetic for line normalization and determinant predicates;
- `fractions.Fraction` or equivalent exact rational representation where division is required;
- no floating-point predicate in the trusted scoring path.

Every counted face should be exportable as the zero-based triple of supporting line indices, matching the inspection surface described by the hill.

## AutoLab reference evaluator

The captured hill displays:

```sh
autolab hills check kobon-triangles
uv tool run --from hills==0.11.0 hills eval <submission-directory> -H kobon-triangles
```

These are source-bound reference commands, not yet recorded here as successfully executed by GCL. The `hills==0.11.0` token is treated as the displayed package pin, not as a durable hill-version identifier.

## Two-path replay rule

A promoted score requires the GCL exact scorer, the AutoLab/local hill evaluator when available, score agreement, and an adversarial check of the GCL scorer logic before it becomes the trusted internal oracle.

## Reproducibility outputs

Retain `solution.json`, normalized line identities, intersection/incidence digest, counted supporting-line triples, exact score, scorer commit, evaluator output, and runtime metadata. Search runtime is diagnostic only.

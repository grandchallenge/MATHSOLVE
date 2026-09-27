# OM26-H1 next action

The independent exact half of H1-01 has passed:

- exact GCL score: **16**;
- baseline SHA-256: `fee1fa08e700ba5849c3d1849cc10d2d3a50a44b3d838d560cd08f9a0de2b271`;
- exact support triples: `[i,i+1,i+2]` for `i=0,...,15`;
- bounded scorer tests: PASS.

The AutoLab half has **not run**. The official CLI installation and hill-pull path were exercised, but the public hill pull requires authentication and the GitHub Actions secret `AUTOLAB_TOKEN` is unavailable.

The deterministic next transition is therefore:

> Provision `AUTOLAB_TOKEN` securely as a GitHub Actions repository or organization secret exposed to `grandchallenge/MATHSOLVE`, rerun `.github/workflows/openmath-kobon-baseline-gate.yml`, and require the AutoLab/Hills evaluator to return `triangles = 16` for the identical `baseline/solution.json`.

If AutoLab returns any other score, stop and reconcile semantics. If it returns 16, close H1-01 and only then authorize construction search.

Do not paste the token into chat or commit it. Until the cross-check returns, construction search and candidate promotion remain forbidden.

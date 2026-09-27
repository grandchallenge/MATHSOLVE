# OPENMATH-2026 next action

OM26-H1 (`alejandrozu/kobon-triangles`) is source-locked and its independent exact baseline replay has passed at score 16.

The H1-01 gate is not complete: the official AutoLab CLI requires authentication to pull the public hill bundle, and the GitHub Actions secret `AUTOLAB_TOKEN` is unavailable. Therefore no AutoLab evaluator score has been returned and there is no score discrepancy to compare yet.

The deterministic next H1 transition is:

> Provision `AUTOLAB_TOKEN` securely as a GitHub Actions repository or organization secret available to `grandchallenge/MATHSOLVE`, rerun the dedicated Kobon baseline workflow, and require `triangles = 16` from the AutoLab/Hills evaluator on the identical baseline `solution.json`.

Until that returns concordantly:

- no Kobon construction search may begin;
- no H1 candidate may be promoted;
- PR #458 remains unmerged;
- OM26-H2 through OM26-H6 may continue organizer-authoritative source acquisition independently;
- no CEI dispatch may issue until the standing conformance audit passes.

Programme tracker: `grandchallenge/MATH-PROGRAMME#1072`  
Forge tracker: `grandchallenge/MATHFORGE#282`  
Solve tracker: `grandchallenge/MATHSOLVE#454`

# OPENMATH-2026 CEI dispatch template

Use only after the target sub-obligation is completely specified.

```text
GCL DISPATCH / OPENMATH-2026

Dispatch ID:
Hill/source-lock identity:
Bounded obligation:

Problem world:
  [all definitions, notation, hypotheses, permitted imported facts]

Target contribution class:
  [proof / counterexample / reduction / missing-hypothesis diagnosis / formalization repair]

Explicit exclusions:
  [claims or assumptions the contributor may not import]

Falsification/rejection conditions:
  [what would make the returned argument unusable]

Authority boundary:
  The contributor supplies evidence only. Receipt is not admission, certification,
  novelty determination, or campaign promotion.

Return contract:
  Return exactly one GCL-CONTRIBUTION-RESULT/1 object through the declared intake surface.
  Do not depend on attachments, hidden files, repository context, or side-channel notes.
```

The dispatch must be executable without repository immersion. If hidden GCL context is required, the obligation is not ready for CEI dispatch.

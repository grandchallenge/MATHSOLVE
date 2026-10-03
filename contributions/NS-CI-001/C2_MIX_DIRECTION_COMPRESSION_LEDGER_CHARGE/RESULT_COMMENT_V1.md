# GCL-CONTRIBUTION-RESULT/1

This is the only accepted contributor-originated result format for the bounded NS-CI GitHub intake pilot.

A valid result is exactly one GitHub issue comment on the dispatch issue.

Required preamble, in this exact order:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: <dispatch id>
assignment: A | B | C | D | E
disposition: PROVED | REFUTED | REDUCED | BLOCKED
context_class: ZERO_CONTEXT
external_sources: NONE
timebox_observed: YES | NO
```

Required level-2 sections, in this exact order:

1. `## Strongest exact statement`
2. `## Derivation`
3. `## Assumptions beyond bootstrap`
4. `## Verification / falsification hooks`
5. `## Claim boundary`
6. `## Next residual`

No other level-2 headings are allowed.

Each section must contain non-whitespace text.

`## Next residual` must contain at most three sentences.

The initial pilot rejects:

- attachments;
- images;
- Markdown links;
- raw URLs;
- HTML image or anchor tags;
- supplementary files;
- references to an external artifact as a substitute for derivation;
- any dispatch id or assignment that does not match the protected dispatch record;
- any result posted to an issue other than the protected issue bound to that dispatch.

A result comment is research evidence only. Intake does not determine mathematical correctness, semantic duplication, plagiarism, or independence strength.

If a comment is mechanically invalid, the original GitHub comment remains the historical event. The contributor may submit one complete replacement comment. The contributor must not edit the rejected comment to create a new evidentiary state.

The first schema-valid result comment admitted for a dispatch is the only mathematical result accepted by version 1. Later schema-valid comments do not replace it.

# OPENMATH-2026 zero-context dispatch template

Use this template only after the target obligation is fully source-locked and can be made self-contained.

A dispatch must make repository reading unnecessary.

## Target

Exact bounded mathematical obligation.

## Definitions and notation

Include every definition needed to reason about the obligation.

## Imported facts

List the exact facts that may be used without proof.

## Excluded assumptions

State tempting but unavailable implications explicitly.

## Permitted contribution

Examples:

- proof of the exact lemma;
- counterexample satisfying the stated hypotheses;
- reduction to a named sub-obligation;
- exact construction;
- proof-critical missing hypothesis.

## Falsification / rejection conditions

State conditions that make the contribution unusable or false.

## Resource bounds

Specify computation or search limits where applicable.

## Return contract

Return exactly one `GCL-CONTRIBUTION-RESULT/1` object through the registered CEI surface.

No extra attachments, hidden files, or side-channel evidence.

## Authority boundary

The contribution is external evidence. Receipt does not mean acceptance; acceptance does not imply MATHCERT certification.

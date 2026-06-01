# Failure Analysis

## Resolved Setup Failures

- The initial scaffold lacked a pinned toolchain and mathlib dependency.
- The first package build reported zero jobs because no root module was wired
  into the default target.
- The original `Finset` import was too thin for `card` and `biUnion`.

## Resolved Proof Failures

- The proof sketches assumed convenience lemmas that mathlib did not expose
  directly.
- Top-union membership required explicit finite induction.
- Powerset sharpness required an explicit erase/insert pairing.

## Lesson

Formalization exposed real interface decisions without changing the
mathematics. Dependencies and recovery maps are now explicit and replayable.

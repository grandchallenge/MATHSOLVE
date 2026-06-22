# WP07 Functional-Preorder Bridge Assessment

Date: 2026-06-22

## Purpose

WP07 opens the functional-preorder branch recorded in `UC-WP03-C007`, but only
as an assessment package. It does not promote the external theorem, does not
import the external Lean repository, and does not claim that the WP06
ideal-family bridge already covers functional-preorder order ideals.

The immediate output is a semantic boundary and next-target selection:
functional-preorder order ideals are finite and averaging-compatible, but they
are not generally `IsIdealFamilyOn` families because preorder-downward closure
is not the same as arbitrary subset-downward closure below proper members.

## Package Map

- `01_RESULT_STATUS.md` records the current certification and source status.
- `02_FUNCTIONAL_PREORDER_BRIDGE_ASSESSMENT.md` gives the semantic assessment.
- `03_PROOF_DEBT_REGISTER.md` lists the proof and audit obligations.
- `04_CLAIM_LEDGER.yaml` records presentation-layer WP07 claims.
- `05_NEXT_EXECUTABLE_STEP.md` selects the next executable target.

## Current Boundary

WP06 supplies a checked local theorem for complements of local ideal families.
WP07 studies a different source theorem: average rarity for order ideals of
functional preorders. The bridge is deferred until either:

1. a separate local predicate and theorem are built for functional-preorder
   order ideals; or
2. a semantic translation theorem proves that a specific finite
   functional-preorder family satisfies a predicate already consumed by
   MATHCERT.


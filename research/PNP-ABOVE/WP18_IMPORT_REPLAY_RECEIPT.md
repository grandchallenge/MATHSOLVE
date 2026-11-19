# PNP-ABOVE WP18 — exact-source Lean replay receipt

**Date:** 18 November 2026 Vancouver local (UTC completion 19 November).
**Scientific disposition:** WP18_NATIVE_NONDIAGONAL_SAMPLER_BOUNDED_VERIFIER_NO_GAP_PASS.
This is an original MIPRE source replay, not P-versus-NP resolution or public mathematical certification.

## Source identity and reproduction

- Original pinned upstream: vidick/MIPRE-formalization revision 5926bdff5db621f44682a101007ef2fe3ae8d970, Lean 4.35.0-rc3.
- Protected MATHSOLVE source parent: 7c999a2f31f6580e8f8e7459818dd04a9bd9d8e2.
- [Full source replay](WP18_REPLAY.sh) individually pins original WP08–WP17 Git blobs; [new-source manifest](WP18_SOURCE_LOCK.json) and [guard](WP18_SOURCE_GUARD.py) verify each of nine new WP18 module Git blobs and SHA-256.
- Scratch replay root: /tmp/gcl-pnp-wp18-full-replay-20261118; 19 original Lean module object files; compiler logs, lock.txt and WP18_AxiomAudit.log retained locally.
- Replay wrapper SHA-256: c41df7838d77c7e1c808433e0ea2970051b9b5dfcea347783cf80fe0d3fb3d18; [axiom audit](WP18_AXIOM_AUDIT.py) SHA-256: ed070cbf3d7f815fb302f0932ce2b5bd525791b034a97a9c0cd1ef9f96cae699.

## Complete native replay output

    WP18_NEW_SOURCE_LOCK_PASS modules=9
    CHECKING_ORIGINAL_SOURCE_WP08
    CHECKING_ORIGINAL_SOURCE_WP09
    CHECKING_ORIGINAL_SOURCE_WP10
    CHECKING_ORIGINAL_SOURCE_WP11
    CHECKING_ORIGINAL_SOURCE_WP12
    CHECKING_ORIGINAL_SOURCE_WP13
    CHECKING_ORIGINAL_SOURCE_WP14
    CHECKING_ORIGINAL_SOURCE_WP15
    CHECKING_ORIGINAL_SOURCE_WP16
    CHECKING_ORIGINAL_SOURCE_WP17
    CHECKING_ORIGINAL_SOURCE_WP18
    CHECKING_ORIGINAL_SOURCE_WP18Sampler
    CHECKING_ORIGINAL_SOURCE_WP18Query
    CHECKING_ORIGINAL_SOURCE_WP18Final
    CHECKING_ORIGINAL_SOURCE_WP18Runs
    CHECKING_ORIGINAL_SOURCE_WP18Native
    CHECKING_ORIGINAL_SOURCE_WP18Bound
    CHECKING_ORIGINAL_SOURCE_WP18Value
    CHECKING_ORIGINAL_SOURCE_WP18NoGap
    WP18_STANDARD_AXIOMS_ONLY_PASS modules=9 theorems=36
    WP18_NATIVE_NONDIAGONAL_SAMPLER_BOUNDED_VERIFIER_NO_GAP_PASS
    process exit 0

All 19 modules compiled from source on the pinned upstream. Five nonfatal simp/deprecation lint warnings occurred in the Bob-query helper; no theorem failed. The original Lean axiom reports for all 36 new theorems were restricted to standard propext, Classical.choice, Quot.sound, or no axioms. Neither a replacement verifier interpreter nor finite-only inference substitutes for original-source proof.

## Scientific acceptance boundary

The original native Sampler 9 implements the full source player-aware query interface, exactly-on partition, raw halting and cost bounds. A seed with bit zero false and bit one true induces positive source CL distribution mass at an unequal Alice/Bob pair. The original bounded Verifier 9 has source static coefficient 53, sampler description size 24,221, verifier description size 145,459, and explicit bound parameter 145,469.

The original synchronous, tensor-product quantum and commuting game values for the unchanged identity decider all equal 1 for every positive index and answer budget. This is a rigorous **no-gap negative control**, not evidence of a hard game.

## Admission and research status

This receipt certifies only the local source-locked replay and theorem-axiom inspection. Protected source merge, exact admitted-head readback, public editorial projection and MATHCERT independent certification are distinct gates requiring separately recorded evidence.

Next: source-native answer-sensitive decider and truly nonlocal question support with a proved positive quantum/classical gap. The present off-diagonal support is sparse and may itself have a stronger no-gap obstruction not yet proved. Positive-parameter compression, Theorem 12.1 reconciliation, uniform succinct SAT-to-classical transfer, and PNP-001 definition equivalences remain open. Keep MATHSOLVE #1136 and MATH-PROGRAMME PNP-001 #162 open.

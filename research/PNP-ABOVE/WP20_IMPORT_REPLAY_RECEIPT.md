# PNP-ABOVE WP20 — original-source Lean replay and claim-boundary receipt

**Execution date:** 19 November 2026. **Proof grade:** exact original-source formal source mathematics, not external MATHCERT certification, a complete answer-sensitive Cost.Prog verifier, or a P-versus-NP theorem.

## Pinned identities and integrity

- Original upstream `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean `v4.35.0-rc3`.
- Admitted parent MATHSOLVE `0780909e5a31c8fb7ff882a25b1ccad5bf31dd51`, including WP08–WP19 and all their predecessor source locks.
- Seventeen new WP20 Lean modules, Git blob SHA-1 + SHA-256 + exact public theorem inventories: [WP20_SOURCE_LOCK.json](WP20_SOURCE_LOCK.json).
- Fail-closed guard [WP20_SOURCE_GUARD.py](WP20_SOURCE_GUARD.py) verifies all 17 source bytes against both hashes, rejects duplicate/missing paths and theorem-ledger drift, then stages exact source files. It independently passed with `WP20_SOURCE_LOCK_PASS modules=17 theorems=107`.
- Original source theorem compiler: `lake env lean` under pinned original upstream; all 17 modules first individually compiled to OLEANs with exit 0 under `/tmp/gcl-pnp-wp20-20261119`. No source module includes `sorry`, a custom axiom or `native_decide`.

## Clean all-predecessor replay and second exact-head replay

The complete [WP20_REPLAY.sh](WP20_REPLAY.sh) runs the existing source-locked [WP19_REPLAY.sh](WP19_REPLAY.sh), which itself replays WP18 and WP08–WP17 and both predecessor axiom audits, then compiles all 17 WP20 source modules and inspects 107 new `#print axioms` declarations. Allowed axioms are exactly `propext`, `Classical.choice`, `Quot.sound` or none.

First full run directory: `/tmp/gcl-pnp-wp20-full-replay`; log `/tmp/gcl-pnp-wp20-full-source.log`; exit record `/tmp/gcl-pnp-wp20-full-source.exit`. **Full original-source replay: PASS, exit 0.** Actual log `/tmp/gcl-pnp-wp20-full-source.log` and exit `/tmp/gcl-pnp-wp20-full-source.exit` report `WP18_NATIVE_NONDIAGONAL_SAMPLER_BOUNDED_VERIFIER_NO_GAP_PASS`, `WP19_STANDARD_AXIOMS_ONLY_PASS modules=8 theorems=36`, `WP20_SOURCE_LOCK_PASS modules=17 theorems=107`, successful compilation of all 17 new WP20 modules, `WP20_STANDARD_AXIOMS_ONLY_PASS modules=17 theorems=107`, and terminal `WP20_EXACT_NATIVE_CYCLIC_SAMPLER_SOURCE_GAME_POSITIVE_BELL_GAP_PASS`. All 27 predecessor original source modules and their inherited source locks were replayed. No nonstandard axioms or compilation failures were reported. This first replay precedes exact immutable PR-head verification.

A second independent full replay bound to the exact immutable committed PR head is required before protected admission. Protected GitHub required CI, merge-group checks and exact protected main readback are independent subsequent gates. The scientific report [WP20_RESULT.md](WP20_RESULT.md) is not a substitute for any of those receipts.

## Exactly proved and deliberately not claimed

- Original source-native `Sampler 9` has two different nine-stage CL presentations with all nine occupied singleton registers, exact 512 ordered source question pairs, and 128 independent CHSH squares.
- The original Cost.Prog sampler has all four quantified query contracts, complete raw-input termination and polynomial source runtime; the original CL distribution is identical to the game law used in the proofs.
- Original mathematical synchronous CHSH predicate is answer-sensitive, including rejection of unequal answers on equal questions.
- Every independent deterministic classical response pair has game value at most `3/4`, attained by the two constant-false functions, hence `classicalValue = 3/4`.
- The explicit original normalized-projective measurement family defines a real two-dimensional `MIPRE.SyncStrategy` of value `81/100`, and upstream embeddings give `quantumValue ≥ 81/100`, `commValue ≥ 81/100`. Hence the strict separation is at least `3/50`.
- **OPEN:** a source-executable original `Cost.Prog` answer-sensitive decider, original full bounded `Verifier 9`, precise source-game equivalence for all accepted answer formats, compression implementation, classical complexity lower bounds, and MATHCERT public certification.

**Proposed next tranche WP21:** construct and replay that decider and complete verifier. The protected research trackers remain OPEN for those obligations.

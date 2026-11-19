# PNP-ABOVE WP19 — source-locked original MIPRE Lean replay receipt

**Execution date:** 19 November 2026 (Vancouver). **Claim grade:** source-native kernel-checked universal star-support no-advantage theorem, not independent mathematical certification, an executable quantum hard game, or a P-versus-NP result.

## Exact source locks

- Upstream original: vidick/MIPRE-formalization revision 5926bdff5db621f44682a101007ef2fe3ae8d970, Lean 4.35.0-rc3 and its original dependency lock.
- Admitted original WP18 source: MATHSOLVE revision 760d30d74672309ae58f015b0f511c062f431e08.
- WP19 current protected parent: 21f3e9edb946ae2ab4f4a312663f1e5559214a6b.
- Nine imported source WP18 modules have their own exact original source manifest and complete predecessor WP08–WP17 hash locks, verified and replayed by [WP18_REPLAY.sh](WP18_REPLAY.sh).
- Eight new WP19 theorem modules are locked individually with Git blob SHA-1 and SHA-256 in [WP19_SOURCE_LOCK.json](WP19_SOURCE_LOCK.json), checked and staged by [WP19_SOURCE_GUARD.py](WP19_SOURCE_GUARD.py).

## Formal replay and axiom inspection

The [full native replay script](WP19_REPLAY.sh) runs the existing original MIPRE WP08–WP18 chain in a clean source replay directory, and then compiles each of the eight WP19 modules against exact imported OLEANs and the pinned original upstream MIPRE. It does not substitute a Python interpreter, simulated game, alternate quantum strategy model, or finite-case extrapolation.

The [WP19 axiom audit](WP19_AXIOM_AUDIT.py) enumerates **36 distinct public WP19 theorem names** and queries the pinned original Lean kernel with `#print axioms`. Only `propext`, `Classical.choice`, `Quot.sound`, or no axioms are allowed. A new theorem declaration, missing output, unexpected axiom or source byte drift fails the replay closed.

**Original candidate-source replay:** local work directory `/tmp/gcl-pnp-wp19-full-replay-20261119`, stdout log `/tmp/gcl-pnp-wp19-full-20261119.log`, exit receipt `/tmp/gcl-pnp-wp19-full-20261119.exit`. **Result: PASS** (exit 0) on the complete native 27-module chain. Output recorded without truncation:

    WP18_NEW_SOURCE_LOCK_PASS modules=9
    CHECKING_ORIGINAL_SOURCE_WP08 ... WP18NoGap [19 exact source modules]
    WP18_STANDARD_AXIOMS_ONLY_PASS modules=9 theorems=36
    WP18_NATIVE_NONDIAGONAL_SAMPLER_BOUNDED_VERIFIER_NO_GAP_PASS
    WP19_SOURCE_LOCK_PASS modules=8
    CHECKING_ORIGINAL_SOURCE_WP19Support
    CHECKING_ORIGINAL_SOURCE_WP19Law
    CHECKING_ORIGINAL_SOURCE_WP19Choice
    CHECKING_ORIGINAL_SOURCE_WP19Scalar
    CHECKING_ORIGINAL_SOURCE_WP19Envelope
    CHECKING_ORIGINAL_SOURCE_WP19Global
    CHECKING_ORIGINAL_SOURCE_WP19Strategies
    CHECKING_ORIGINAL_SOURCE_WP19Native
    WP19_STANDARD_AXIOMS_ONLY_PASS modules=8 theorems=36
    WP19_UNIVERSAL_STAR_SUPPORT_SOURCE_NATIVE_NO_GAP_PASS
    exit 0

The replay root contains the exact staged source files, 27 compiled OLEANs, per-module Lean compiler logs, WP18 and WP19 original Lean axiom reports and the combined source lock.txt. There are no compiler errors. The Python guards hash original Git blobs, not merely locally formatted text. The original WP00–WP17 72-artifact inventory verifier also independently passed against its immutable pinned snapshot.

**Exact committed PR-head replay:** to be recorded only after commit, push and independent fresh full replay from that exact immutable Git head.

## Bounded theorem conclusion

The exact original WP18 source sampler has 512 supported equally weighted question pairs. Alice's conditional CL question is the seed or the zero question depending on bit zero; Bob's original unconditional CL question is the seed. The source graph comprises a star and isolated equal-question edges, with no cycles.

The complete original source proof establishes: for any finite synchronous game with this support form, every normalized nonnegative no-signalling correlation is dominated by a convex combination of actual dimension-one deterministic synchronous strategies. Original upstream tensor-product Born-rule and commuting tracial probabilities satisfy the hypotheses. Therefore **for every source parameter n, answer budget T and mathematical synchronous replacement decision predicate D**, original synchronous, tensor-product quantum and tracial commuting game values are exactly equal. Their common value need not be one.

The theorem does not claim that an arbitrary replacement predicate is executable under original `Cost.Prog`; its quantification is over all mathematical synchronous predicates. This makes the negative conclusion stronger than testing finitely many executable deciders. No harder two-sided sampler, actual positive value gap, positive-parameter compression, classical SAT cost transfer, P versus NP conclusion or MATHCERT public certification has been obtained.

## Protected admission and public projection

**Source-level evidence now established:** all eight WP19 modules individually compile, original source digest guard and mathematical Markdown gates pass, and the complete 27-module WP08–WP19 original-source replay and both standard-axiom audits PASS with exit 0. **Governance remains separate:** the exact committed-head second replay, protected source CI/merge/readback, six-page public Pages publication and independent MATHCERT certification are distinct gates and must not be inferred until their own results are recorded.

**Next WP20:** a genuinely richer two-sided conditional-linear law with a sampled graph containing interacting question choices, a source-native bounded executable answer-sensitive decider, and an independently proved nonzero original quantum/classical game-value gap. Branching from existing WP19 is not a substitute for that construction. Governing research issues remain OPEN.

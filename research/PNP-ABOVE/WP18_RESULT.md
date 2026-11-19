# PNP-ABOVE WP18 — original source-native asymmetric nine-stage sampler

**Scientific disposition:** `NONDIAGONAL_SAMPLER_CONSTRUCTED_AND_SOURCE_BOUNDED__ORIGINAL_DECIDER_VALUE_GAP_ZERO`.

**Programme:** PNP-ABOVE, [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136), parent [MATH-PROGRAMME PNP-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/162). This WP18 is a bounded *positive sampler construction plus exact negative-control theorem*, **not** a hard-game solution, source compressor, classical-complexity separation, or certified theorem.

## Original model and input

The source is the original `vidick/MIPRE-formalization` pinned at `5926bdff5db621f44682a101007ef2fe3ae8d970`, using Lean 4.35.0-rc3 and the original imported `MIPRE.CL.CLFun`, `MIPRE.CL.clDist`, `MIPRE.Sampler`, `MIPRE.Verifier`, `MIPRE.Cost.Prog`/`Eval`, and the original synchronous/tensor-product/commuting strategy values.

The nine-bit shared seed has field `𝔽₂`. Alice uses WP14's **full-depth genuinely conditional** nine-stage CL presentation: coordinate zero always survives, and every remaining coordinate survives only when seed bit zero equals one. Bob uses an **unconditionally active nine-stage** presentation, with every one of the nine singleton factors nonempty and distinct. Thus Bob's question is the original seed; Alice's question may differ.

For the explicit seed `(false, true, false, false, false, false, false, false, false)`, the original CL evaluation sends unequal questions. The new proof `original_cl_dist_positive` establishes **strictly positive original conditional-linear mass** for that pair, not merely a sampled finite histogram. The original finite seed space has 512 elements. The mathematical support of this first construction is *very sparse*: when the first seed bit is zero, Alice outputs zero and Bob outputs that seed; when it is one, both questions coincide. Hence this witness satisfies necessary non-diagonality but does **not** supply a Bell-nonlocal question graph or prove it could support any quantum advantage under a redesigned predicate. The precise support-shape obstruction deserves its own next theorem.

## Verified executable query interface

The new program `asymmetricSamplerProg` actually parses the original source's binary-encoded `Player` field and dispatches independently to Bob's prefix-copy and stage-linear source routines, correctly accounting for de-Bruijn offsets. Original-source quantified Lean proofs establish:

- the dimension query for every index;
- marginal queries for **both players**, every legal stage and every canonical nine-bit input;
- prefix-dependent stage-linear source queries for both players and every valid original input;
- factor queries for both players and every legal stage;
- original well-scoped source syntax, loop freedom and halting on **every raw query input**, including malformed data.

These are installed into a real `MIPRE.Sampler 9` record (`asymmetricSampler`), not an abstract oracle or an independent simulated interpreter. The original `Sampler.dist` is proved positive on an unequal question pair.

An original `MIPRE.Verifier 9` record uses the **same** source-native WP08/14 identity-decider contract. The original `Verifier.IsBounded` proof holds with:

| Source quantity | Exact value |
| --- | ---: |
| Number of occupied CL stages and input coordinates | 9 |
| Static original source runtime-build coefficient | 53 |
| Original sampler description size | 24,221 |
| Original verifier description size | 145,459 |
| Conservative verifier polynomial bound parameter | 145,469 |

The degree-one input-size runtime has an explicit parameter-dependent source coefficient. The `n^10` envelope and original verifier bound follow from the source evaluator's actual constructor and environment costs.

## Exact game-value result: a second obstruction

The *original* `asymmetricVerifier.syncGame n T` at every positive index `n` and answer budget `T` has genuinely off-diagonal question support, yet accepts empty answers for **every** valid question pair because its executable decision predicate is unchanged.

The original `SyncStrategy` has a dimension-one deterministic strategy returning the empty answer everywhere. By original lower/upper bounds, the exact values are:

```text
syncValue (asymmetricGame n T) = 1
quantumValue (asymmetricGame n T).toGame = 1
commValue (asymmetricGame n T) = 1
quantumValue - syncValue = 0
```

WP17 proved that changing *only* the decision predicate while retaining WP14's diagonal sampler cannot help. WP18 proves the complementary negative control: changing *only* the sampler while retaining WP14's always-accepting decider cannot help either.

These theorems show that **both** a suitably rich pair-question law and a genuinely answer-sensitive source decider are necessary. They do **not** assert that the current star-shaped law becomes hard simply by replacing its decider.

## Replay, provenance and claim boundaries

Nine source modules and their individual SHA-256/Git blob digests are fixed in [WP18_SOURCE_LOCK.json](WP18_SOURCE_LOCK.json). [WP18_REPLAY.sh](WP18_REPLAY.sh) verifies the original upstream, exact protected MATHSOLVE WP08–WP17 predecessor Git blobs, all nine new WP18 source files, and rebuilds the native Lean dependency chain. [WP18_AXIOM_AUDIT.py](WP18_AXIOM_AUDIT.py) checks **36 distinct WP18 theorem axiom reports**, permitting only standard `propext`, `Classical.choice`, `Quot.sound`. No generated axiom, `sorry`, or unproven mathematical assumption is authorized. Exact-head replay, protected checks, merge/readback and public documentation are distinct admission steps, recorded in [WP18_IMPORT_REPLAY_RECEIPT.md](WP18_IMPORT_REPLAY_RECEIPT.md).

**Still open:** a rich nonlocal source distribution (the first asymmetric support is sparse), a source-native **answer-sensitive** bounded decision predicate, a rigorous nonzero classical/quantum or soundness gap, valid positive-parameter introspection and compression, source Theorem 12.1 quantitative reconciliation, full uniform succinct SAT/classical transfer, separate PNP-001 machine/NP/endpoint equivalences and MATHCERT certification. P versus NP is not resolved. Do not close the parent tickets.

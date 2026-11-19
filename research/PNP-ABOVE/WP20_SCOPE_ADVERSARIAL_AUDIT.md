# WP20 adversarial scope and mathematical validity audit

**Review grade:** internal source-semantic adversarial review notes. Not a claimed separate human identity, independent MATHCERT attestation, or certification of the P-versus-NP question. Bind the conclusions to the exact admitted source manifest and original pinned Lean revision.

## Potentially fatal objections examined

**1. The question graph might still be one star.** The original joint source map is two-sided: Alice reads bit 0, Bob reads bit 8, and both read the seven middle bits. [WP20_CyclicQuestionMaps.lean](WP20_CyclicQuestionMaps.lean) proves a complete sampled four-cycle; [WP20_SharedSquareDecomposition.lean](WP20_SharedSquareDecomposition.lean) proves 128 disjoint four-edge components, with distinct left and right vertices. [WP20_ExactQuestionLaw.lean](WP20_ExactQuestionLaw.lean) proves exact original source mass of 1/512 per edge. WP19's star obstruction does not apply.

**2. A Bell inequality for one illustrative square is not a global game bound.** [WP20_OriginalCLPushforward.lean](WP20_OriginalCLPushforward.lean) establishes the exact original CL distribution pushforward to 512 uniform source seeds. [WP20_GlobalClassicalBound.lean](WP20_GlobalClassicalBound.lean) applies the four-edge contradiction on **each** of 128 components; [WP20_ExactClassicalValue.lean](WP20_ExactClassicalValue.lean) gives equality at 3/4. There is no probabilistic extrapolation or assumption that the other 508 edges have zero mass.

**3. One common answer function artificially restricts classical strategies.** The actual global bound quantifies separately over `fA : Questions → Bool` and `fB : Questions → Bool`, and classicalValue takes the nested supremum over both functions. It is at least as permissive as any single-function synchronous deterministic strategy. Shared randomness cannot exceed the deterministic maximum of a linear payoff. The original source game has binary mathematical answers; original `Verifier.Answers T` equivalence for arbitrary T is **not** yet proved.

**4. A hand-written probability table is not a quantum strategy.** The rational matrices in [WP20_RationalQubitWitness.lean](WP20_RationalQubitWitness.lean) have kernel-checked self-adjointness, idempotence and projective normalization. [WP20_OriginalQuantumStrategy.lean](WP20_OriginalQuantumStrategy.lean) constructs an actual original `MIPRE.SyncStrategy`, computes its value from the original normalized-trace formula, and uses *upstream* embeddings into the original tensor-product and commuting strategy classes. Thus no alternate or fabricated quantum semantics are substituted.

**5. Synchrony might fail on off-support equal questions.** [WP20_CHSHParityPredicate.lean](WP20_CHSHParityPredicate.lean) explicitly rejects unequal outputs on *every* diagonal pair, not merely the sampled support. On sampled equal questions, both private setting bits vanish, preserving CHSH's required equality parity.

**6. A mathematical predicate is not an executable source decider.** This objection **remains valid** and is an explicit WP21 obligation. Only the sampler has a fully executable original `Cost.Prog` with all four query families, raw halting, and polynomial source bounds. The new answer-sensitive acceptance rule is a mathematical `SynchronousGame.D`, not a proven `MIPRE.Decider.Accepts`. No `Verifier 9`, accepted-answer-length comparison, normal-form bound, positive-parameter compressor, or complexity lower bound follows automatically. The preceding WP18 identity decider is **not** silently reused.

**7. Unchecked axioms or source drift could contaminate the proof.** Each of 17 modules is fixed by immutable Git blob SHA-1 and SHA-256 in [WP20_SOURCE_LOCK.json](WP20_SOURCE_LOCK.json); the guard rejects even a one-byte mutation. All **107 new public theorem declarations** were checked with the original Lean `#print axioms`, with only standard `propext`, `Classical.choice`, `Quot.sound` (or none). The full clean 44-module predecessor-plus-WP20 replay passed exit 0 with an original Lean axiom audit of all 107 WP20 theorem declarations. A fresh replay on the final immutable PR-head and protected main admission are separate gates and are not inferred from the clean replay.

## Verdict and next obligation

**Qualified mathematical claim:** the explicit original-native sampled *mathematical* game has local classical value exactly 3/4, original quantum value at least 81/100, and a positive gap at least 3/50. The stronger source-native compiler/normal-form-verifier, positive-parameter compression, uniform succinct SAT transfer and independent MATHCERT public claim are not certified.

**Next WP21:** original answer-sensitive `Cost.Prog` decider, exact source-level semantic correspondence, normalized/length-checked acceptance, source runtime/size envelope, native `Verifier 9` and corresponding gap, including all extra answer forms.

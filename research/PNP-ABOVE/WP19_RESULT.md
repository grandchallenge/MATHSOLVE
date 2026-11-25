# PNP-ABOVE WP19 — universal no-advantage theorem for the WP18 sampler

**Scientific disposition:** UNIVERSAL_STAR_SUPPORT_ORIGINAL_SOURCE_NO_GAP_PROVED. The original MIPRE WP18 question distribution admits **no tensor-product quantum or tracial commuting advantage over the deterministic synchronous optimum for any synchronous decision predicate**. This is a rigorous negative result, not an executable hard game, a classical complexity lower bound or a P-versus-NP proof.

## Original model and exact question law

- Upstream: vidick/MIPRE-formalization revision 5926bdff5db621f44682a101007ef2fe3ae8d970, original Lean 4.35.0-rc3.
- Original source-native WP18 sampler/verifier: protected MATHSOLVE revision 760d30d74672309ae58f015b0f511c062f431e08.
- WP19 source parent: 21f3e9edb946ae2ab4f4a312663f1e5559214a6b. Eight new Lean files individually locked in [WP19_SOURCE_LOCK.json](WP19_SOURCE_LOCK.json).
- Governing research trackers: MATHSOLVE #1136, MATH-PROGRAMME PNP-001 #162; both remain OPEN.

The new [exact-support proof](WP19_ExactStarQuestionSupport.lean) establishes for every shared nine-bit seed z that Alice(z) is z if its first bit equals 1 and is otherwise the zero vector; Bob(z) is z. [Exact original-source probability](WP19_ExactOriginalQuestionProbability.lean) shows that each supported pair has probability exactly **1/512** and every unsupported pair has probability zero.

The bipartite question graph is a **256-edge star** with Alice's zero question at the center and 256 Bob leaf questions whose first bit is zero (including the center-center edge), plus **256 isolated diagonal edges** on questions whose first bit is one. It contains no cycles. This structure is proven for the original conditional-linear distribution, not inferred from simulation.

## General theorem and constructive proof

The source-independent [star support predicate and selector](WP19_DeterministicStarResponseChoice.lean) describe any finite synchronous game G with a distinguished center c satisfying

    StarMatching G c :=
      forall x y, mu(x,y) != 0 ->
        x = c or (x = y and mu(c,x) = 0).

For each proposed central answer a, a dimension-one deterministic single-question strategy gives answer a at the center, chooses an accepted Bob-leaf answer where possible, and independently chooses an accepted equal answer on each isolated diagonal where possible. These choices are legitimate even if some sampled questions have no winning response.

[The scalar inequality](WP19_PositiveCorrelationUpperBounds.lean), [no-signalling star envelope](WP19_StarNoSignallingEnvelope.lean), and [convex finite-sum theorem](WP19_StarConvexCorrelationTheorem.lean) prove that **every correlation whose probabilities are nonnegative, sum to one for each question pair and have Alice's central marginal independent of Bob's question has payoff no greater than the original synchronous value**. The upper bound is a convex combination of actual dimension-one deterministic strategies. No assumption that the optimum equals one is used.

[The original-model strategy bridge](WP19_OriginalTensorAndCommutingBridge.lean) verifies these correlation hypotheses directly for upstream MIPRE.TensorProductStrategy and MIPRE.CommutingStrategy, using their actual normalized projective measurements, Born rule, tracial states and exact strategy-value formulas. It then proves the original quantum and commuting values are at most the synchronous value. The already-proved upstream synchronous embeddings give the reverse inequalities.

[WP19's native final theorem](WP19_ArbitraryPredicateSourceNoGap.lean) proves for **every** index n, answer budget T and mathematical synchronous predicate D (unequal answers on identical questions are rejected):

    syncValue (wp18WithDecision n T D hSync)
      = quantumValue (wp18WithDecision n T D hSync).toGame
      = commValue (wp18WithDecision n T D hSync).

The two quantum-minus-classical and commuting-minus-classical differences are exactly zero. Values may be less than one. There is no diagonal-feasibility hypothesis and no requirement that D be the old identity predicate. The arbitrary D is a mathematical replacement predicate; its executable source compiler is **not** assumed or claimed. The theorem covers the actual original finite-dimensional tensor-product and tracial commuting strategy models, not a separately certified larger commuting-operator model.

## Implications and remaining work

WP17 ruled out a predicate-only repair of WP14's diagonal sampler. WP18 supplied a genuinely non-diagonal source-native sampler and bounded verifier, but with its old universal identity decider all three values were one. WP19 proves that **no alternative synchronous decision predicate can make the exact WP18 sampling law quantum-advantaged**: its star-plus-isolated-diagonal support is itself an obstruction.

The intuition is that Alice has only one possible question at the center of the nontrivial star. Her answer can be fixed first, and Bob can preselect an optimal answer independently for each leaf. Isolated equal-question components can also be optimized separately. Entanglement cannot improve this task.

**Next WP20:** build a richer, original Cost.Prog-executable, two-sided conditionally linear sampler with overlapping question choices and a nonforest bipartite support (cycles are a useful necessary design signal, not sufficient for a gap). Prove all original four source query contracts and bounds. Then build an actual answer-sensitive bounded source decision predicate and prove a strict original quantum/synchronous value or soundness gap. Subsequent obligations remain positive-parameter compression, Theorem 12.1 source-bound reconciliation, uniform succinct SAT/classical transfer, separate PNP-001 machine/NP/endpoint bridges and MATHCERT independent public certification. No P=NP or P!=NP theorem is claimed.

## Evidence boundaries

[Full WP19 original-source replay](WP19_REPLAY.sh) first replays WP08–WP18 under their own exact protected source locks, then verifies all eight WP19 Git blobs/SHA-256 digests and compiles their eight modules. [The WP19 axiom audit](WP19_AXIOM_AUDIT.py) inspects all **36 distinct public WP19 theorems** in the original Lean kernel and permits only propext, Classical.choice, Quot.sound (or no axioms). No sorry, custom axiom or native_decide axiom is included.

Source replay result, exact candidate head, protected CI/merge, public projection and any future certification are separate obligations; record their actual evidence in [WP19_IMPORT_REPLAY_RECEIPT.md](WP19_IMPORT_REPLAY_RECEIPT.md). Do not interpret a local compilation as protected admission or independent mathematical certification.

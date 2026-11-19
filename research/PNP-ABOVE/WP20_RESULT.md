# PNP-ABOVE WP20 — original-source cyclic sampler and strict quantum/classical gap

**Disposition:** `WP20_MATHEMATICAL_BELL_GAP_AND_EXECUTABLE_SAMPLER_PROVED`. An actual original MIPRE `Sampler 9` now uses two nine-stage conditionally linear source maps with interacting two-player questions. For the mathematically specified synchronous, answer-sensitive CHSH predicate, the original game has **exact local classical value 3/4**, an explicit original two-dimensional quantum strategy of value **81/100**, and a strict advantage of **at least 3/50**. This is a finite, concrete quantum/nonlocal game result, **not a P-versus-NP resolution**.

## Source identities and scope

- Original upstream: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, pinned original Lean 4.35.0-rc3.
- Protected predecessor: MATHSOLVE `0780909e5a31c8fb7ff882a25b1ccad5bf31dd51`, containing all admitted WP08–WP19 dependencies and the WP19 star-support impossibility theorem.
- Seventeen new Lean source modules; **107 distinct public theorem statements**, individually locked by Git blob SHA-1, SHA-256 and declaration inventory in [WP20_SOURCE_LOCK.json](WP20_SOURCE_LOCK.json). The [fail-closed source replay](WP20_REPLAY.sh) recompiles all 27 predecessor modules and 17 new WP20 modules, then queries their original Lean kernel axioms through [WP20_AXIOM_AUDIT.py](WP20_AXIOM_AUDIT.py).

The two source-native nine-stage conditional-linear question maps on a uniform nine-bit seed z are:

    Alice(z) = (z[0], z[1], ..., z[7], 0)
    Bob(z)   = (0,    z[1], ..., z[7], z[8])

Every stage occupies its actual singleton register, even when its linear map is zero. The joint question map is injective; the original `clDist` is exactly uniform on **512 distinct ordered pairs**, each of probability `1/512`, and zero elsewhere. The seven common middle bits label **128 complete four-edge bipartite squares**. These are formal theorems of the actual `CLFun`, not numerical sampling claims.

The source-native [Cost.Prog sampler](WP20_SourceSamplerProg.lean) and [all-source-query proofs](WP20_AllSourceQueryProofs.lean) compile against original MIPRE. They establish, for all valid index/stage/question parameters, the dimension, marginal, linear and factor query contracts for **both players**, with [native `Sampler 9` packaging](WP20_OriginalNativeSampler.lean), correct bit representation and raw-input halting. The native source code is closed, loop-free, has an exact static build constant 51, and [a polynomial `Sampler.TimeBoundAt n (n^10) 10` bound](WP20_BoundedNativeSampler.lean) for every n at least 2. This proves the **sampler** source bound, not a decider bound.

## Answer-sensitive game and value separation

The mathematical binary-answer predicate is:

    Accept(x,y,a,b) :=
       (a XOR b = (x[0] AND y[8])) AND
       ((x != y) OR (a = b)).

The synchrony clause rejects unequal answers on identical questions, including unsampled pairs. On every sampled original pair this reduces to CHSH parity. The [Lean classical upper bound](WP20_GlobalClassicalBound.lean) quantifies over **two independently chosen, arbitrary deterministic local response functions**. The four parity checks on each shared-register component are inconsistent, so at most three of its four sampled edges can be won. A kernel-checked [source pushforward](WP20_OriginalCLPushforward.lean) handles **all 512 original seeds**. The all-false response strategy wins exactly three on every square. Hence [the exact classical optimum](WP20_ExactClassicalValue.lean) is `classicalValue = 3/4`; shared randomness cannot improve this linear-payoff optimum.

The explicit original quantum strategy uses real-rational rank-one projectors:

    P_center = [[1,    0  ], [0,    0  ]]
    P_Alice  = [[4/5,  2/5], [2/5,  1/5]]
    P_Bob    = [[4/5, -2/5], [-2/5, 1/5]]

Lean proves their self-adjointness, idempotence and completeness as binary `ProjectiveMeasurement`s. The four original tracial winning probabilities are `1, 4/5, 4/5, 16/25`, with mean **81/100**. The [original MIPRE.SyncStrategy witness](WP20_OriginalQuantumStrategy.lean) is dimension 2 and wins exactly that proportion across the full 512-seed distribution, not just one selected square. Original upstream strategy embeddings transport this lower bound to its actual tensor-product quantum and tracial commuting values. The [strict theorem](WP20_SourceGameBellGap.lean) proves `quantumValue - classicalValue ≥ 3/50 > 0` (and the analogous commuting inequality), for every original source index. We **do not** assert that 81/100 is the *optimal* quantum value.

## Exact remaining boundary

**The CHSH acceptance predicate is mathematical, not yet an executable original `MIPRE.Cost.Prog` decider.** Consequently this tranche does not claim that a complete source-native original `Verifier 9` with this CHSH decider exists, that an original `Verifier.game n T` is already equivalent to the mathematical synchronous game for every answer-length budget, or that full `Verifier.IsBounded` has been proved. Existing original bounded identity-decider code is not silently substituted for the new CHSH predicate.

**Next obligation WP21:** implement and replay an answer-sensitive canonical-question/binary-answer `Cost.Prog` decider, establish the complete `Decider.Accepts` semantics, sound canonical and synchronous rejection, halt/time/size bounds, assemble a native bounded `Verifier 9`, and connect its original bounded answer space and quantum/classical payoffs to this WP20 gap. Positive-parameter gap compression, original Theorem 12.1 constants and uniform succinct SAT classical strategy-cost transfer remain OPEN. No MATHCERT independent public certification or P=NP/P≠NP conclusion is claimed.

See [WP20_IMPORT_REPLAY_RECEIPT.md](WP20_IMPORT_REPLAY_RECEIPT.md) for replay, source identity and eventual protected admission evidence; do not infer protected/public promotion merely from this local theorem report.

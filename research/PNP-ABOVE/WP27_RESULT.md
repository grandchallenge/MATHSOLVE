# PNP-ABOVE WP27 — total raw-input verifier, bounded source and compression

Scientific status: original Lean-kernel candidate; full uncached exact-head replay and protected admission remain separate gates.

Original pinned source: vidick/MIPRE-formalization at 5926bdff5db621f44682a101007ef2fe3ae8d970, Lean v4.35.0-rc3. Original WP26 protected admission: MATHSOLVE PR #1264 at 1ff6a4a0d94e0ea773fe6f77ebda4f712ff00446. PNP-001 MATH-PROGRAMME #162 OPEN.

## Actual prior blocker resolved

WP26 proved an original formula-dependent Verifier 7 with exact native SAT/UNSAT quantum values and a source-polynomial formula-to-decider-program compiler. However, its typed Cost.PolyTimeFun.computes theorem did not establish original Decider.TimeBoundAt on ALL malformed raw Data, making source IsBounded and compressor consequences conditional.

WP27_RawNormalizer.lean constructs a TOTAL original Cost.PolyTimeFun Data (Nat x BitStr x BitStr x BitStr x BitStr) using original readNat, readBits, treeHead and treeTail. Every arbitrary raw Data becomes a valid tuple in polynomial time; canonical original encodings are reproduced exactly. A fixed Cost.PolyTimeFun (Fml x Data) Bool evaluates the original SAT witness on normalized inputs. The actual source Cost.PolyTimeFun.smn then emits a closed Cost.Prog for every original SAT formula f; source hardcode_time and hardcode_time_rev prove it accepts precisely satisfying matching answers.

WP27_TotalCost.lean proves an ORIGINAL PolyCost bound on the size of (f, Data.cons (encode n) d) for ALL n and ALL arbitrary Data d. Its explicit coefficient depends on original esize f and 4*Nat.size n+5. Composition with the genuine original rawCore.timeBound and Prog.hasPolyCost_of_polyCost yields an unrestricted kernel theorem

    (robustSourceGenerator f).HasPolyCost

for every original source formula f, with no type or well-formedness hypothesis on raw Data. This is NOT inferred from typed source runtime alone; the proof explicitly uses arbitrary Data runs and the original hardcoded programme execution cost.

WP27_RobustVerifier.lean constructs an ACTUAL original MIPRE.Verifier 7 with a real original CL.Sampler 7, Cost.UniversalMachine, and the robust source decider. The original source proves exact Decider.Accepts semantics, SAT HasPerfectPCC, SAT valStar=1 with adequate answer budget, scoped UNSAT valStar=0 at every index/budget, and classical bounded winning-answer iff SAT witness for any source question pair. The original source GapCompression sampler runtime/dimension bound plus NEW global HasPolyCost are fed to original Verifier.ofSamplerDecider_isBounded to produce

    exists lam, (robustVerifier U (G.sampler 0) f).IsBounded lam

WITHOUT any assumed runtime bound. Actual original GapCompression.completeness and soundness then prove the native compressed SAT PCC and UNSAT value-at-most-one-half promises WITHOUT an IsBounded input premise. They retain the original index G.C0<=k and witness-size m<=(2^k)^lam conditions.

## Exact remaining complexity boundary

Per-formula HasPolyCost and IsBounded existence are proved, but the derived lambda is existential and may depend on the hardcoded formula size. No fixed compression exponent independent of f, efficient algorithm to compute lambda, polynomial bound on all emitted compressed descriptions, or complete original-source polynomial SAT-to-compressed-game reduction is established. Composing the 3CNF-to-Fml source translator, Fml-to-Prog source compiler and compressor parameters with ONE polynomially bounded source index remains open. Original G:GapCompression and U:Cost.UniversalMachine are quantified as source-native constructed types; direct concrete constructor import is separate.

Accepted classical response pairs contain satisfying assignments. This is an exact witness equivalence, not an efficient SAT search algorithm or a classical runtime lower bound. A full-assignment one-question game does not by itself imply P differs from NP. No P=NP, P!=NP or external MATHCERT certification is claimed.

Next: WP28_FIXED_LAMBDA_AND_POLYNOMIAL_SOURCE_INDEX and WP28_CLASSICAL_STRATEGY_RUNTIME_TRANSFER.

# PNP-ABOVE WP11 — cost-indexed native interpreter completeness

**Parent:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136). **Classification:** bounded Lean proof candidate; not independent mathematical certification, full quantum compression, classical lower bound or a P-versus-NP result.

## Source and mathematical result

Source: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean 4.35.0-rc3 and pinned dependencies. Protected MATHSOLVE ancestor: `b447809368083cdab92395dd1f64654388b2aa64` (WP10). The [Lean file](WP11_EvalFuelCompleteness.lean) imports the source-native WP08–WP10 chain, not a copied `Eval` model.

**Generic semantic adequacy:** For every environment, native `Prog`, result and timed evaluation cost, source-native `Eval env p r t` is equivalent to independent `WP09.runFuel (t+1) env p = some (r,t)`. The new direction is proved by induction on the upstream `Eval` derivation, including all three looping cases. The opposite direction was proven by WP09. This does **not** assert that every arbitrary source program halts, or that the cost index is computable without an evaluation.

**Native finite decider:** A structural proof shows that WP08's identity-game decider has no source loop or unbounded data-copy (`var`) operation. It always terminates, even on arbitrary malformed raw `Data`. A source-derivation cost induction yields a fixed worst-case upper bound of **89 native cost units**, independent of raw input size; a Lean finite guard checks the cost definition's value 89. Thus fuel **90** is sufficient for all raw inputs. An independent output-shape proof establishes that the output is always a canonical encoded Boolean.

**Exact acceptance and rejection:** For every typed tuple `(n,x,y,a,b)`, upstream `MIPRE.Decider.Accepts` is equivalent to existence of a true-output interpreter run at fuel 90; its negation is equivalent to a false-output run at fuel 90. Unlike WP10's two concrete examples, these statements quantify over all typed tuples. They establish *operational-semantic completeness*. They do **not** prove that the positive cases coincide with the intended nine-bit length/empty-answer predicate; that parser-correctness theorem is separately required.

## Reproduction and claim restrictions

The [exact-head replay harness](WP11_REPLAY.sh) checks the upstream commit, original protected WP08, WP09 and WP10 Git blob identities, committed WP11 source, and source-native Lean elaboration for all four modules. The [axiom audit](WP11_AXIOM_AUDIT.py) checks all 18 new theorem declarations and rejects nonstandard axioms, including generated `native_decide` or `sorryAx`. Reproducible results, exact-source hashes and execution receipts belong in [WP11 receipt](WP11_IMPORT_REPLAY_RECEIPT.md) after exact-head replay. GitHub CI admission/readback is a separate operation.

**Still open:** (1) all-input parser predicate correspondence including malformed raw data; (2) full source-native nine-level sampler with `CLFun.ExactlyOn`, four run conditions, uniform halting, and verifier boundedness; (3) positive-parameter three-stage quantum compression; (4) a succinct uniform SAT-to-classical-resource transfer with polynomial bit/time overhead; (5) the Theorem 12.1 source quantitative discrepancy and the original PNP Formal Conjectures encoding concordance. No PNP-001 claim promotion.

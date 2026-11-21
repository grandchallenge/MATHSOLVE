# WP28B1 internal source Verifier / Adversary / Referee scope

Verifier: The source modules use ORIGINAL SAT.Fml, Cost.Data,
Cost.PolyTimeFun, Cost.Prog.serProg/parseProg via OracleDecider.parseF,
Nat.bits binary encoding and source Data.stackRun. The index
programme is a single source code object. The decoder is also
fixed-code and source executable for all typed Nat indices.

Adversary: The final sentinel bit is necessary. Without it the
canonical Nat.bits representation can erase high-order zero bits
and fail to roundtrip arbitrary source trees. This is proved by
an explicit induction and original source Data parser, not assumed.
Input size means binary representation size, NOT numeric magnitude.
The source code does not embed the formula. The exact index is
injective and its bit length is esize f + 1.

Referee scope:
ADMIT_FIXED_POLYNOMIAL_ORIGINAL_SAT_FORMULA_INDEX_ENCODER_DECODER_AND_SEMANTIC_3CNF_TRANSFER.

Do not claim the independent fixed-code original MIPRE.Verifier 7
was constructed. The source Fml data decoding into a runtime
formula evaluator, raw input bounds, universal lambda, source
3CNF-program compiler, compressed game complexity reduction and
classical search lower bounds remain separate obligations.
No source-index sample-size numerics are substituted for
original source kernel proofs. No public certification.

# PNP-ABOVE WP31: every lossless numeric SAT encoding has exponential worst-case index

## Original-source mathematical result

Original pinned source `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`, Lean v4.35.0-rc3. Protected predecessor `MATHSOLVE@290d2fd2bb5861aaa9155a1549aee4f72946862f` (WP30 PR #1282). Ten new theorem declarations in `WP31_EncodingBarrier.lean`. All proofs target actual original `MIPRE.SAT.Fml`, `MIPRE.Cost.esize` source encoding and the existing complete WP08–WP30 original Lean lineage.

Define `signedConjunction : List Bool → MIPRE.SAT.Fml` by interpreting each bit as input x0 or negated input x0, joining these as a nested conjunction with a terminal Boolean constant true. The Lean kernel proves:

- **Exact formula-family injectivity:** two different bitstrings yield syntactically different original source SAT formulas. For every `r`, `formulaFamily r` embeds ALL `2^r` functions `Fin r → Bool` into the original SAT source language.
- **Linearly bounded actual source representation:** `(signedConjunction s).size ≤ 3*s.length + 1` and `esize (signedConjunction s) ≤ (esize (MIPRE.SAT.Fml.inp 0) + 19)*s.length + esize (MIPRE.SAT.Fml.const true)`. Hence ALL `2^r` distinct formulas have original encoded length at most a fixed linear function of `r`; this is not just abstract syntax-tree size.
- **Finite information-counting obstruction:** for ANY function `enc : (Fin r → Bool) → Nat` that is injective, some output satisfies `2^r ≤ enc xs + 1`. This follows from a genuine finite-cardinality injection contradiction `2^r ≤ 2^r-1` in original Lean via Mathlib `Fintype.card_le_of_injective`, not a paper-only pigeonhole claim.
- **All lossless source encodings:** for ANY `enc : SAT.Fml → Nat` that is injective, one of the r-bit-sized SAT source formulas satisfies `2^r ≤ enc (formulaFamily r xs)+1`; an explicit decoder `decode(enc f)=f` yields injectivity and the same result. This works for every lossless single-number serializer, not merely WP29's original source binary serializer.

The ten theorem declarations also include an instructive **counterexample to overclaiming**: `satisfiableLabel m f` is a NONCOMPUTABLE Boolean label, encoded by the numeral 0 or 1, with `satisfiableLabel m f = 1 ↔ WP24.Satisfiable m f` and `satisfiableLabel m f ≤ 1`. This is NOT a polynomial-time original `Cost.Prog` and is not a SAT algorithm. It shows that two semantic SAT classes can be labelled by one bit if one is allowed to assume the computationally difficult SAT decision during compilation. The counting obstruction applies to **lossless formula recovery**, NOT to a hypothetical efficient many-to-one SAT-preserving transformation. The algorithmic difficulty of the latter remains the open computational issue.

## Classical/quantum complexity consequence and precise limit

WP29 proves `k≥2^q` numerically for its own q-clause serializer. WP31 proves the stronger representation-INDEPENDENT obstruction: any exact formula-recovering single numeric game-index scheme for all linearly encoded source formulas requires numerical values ≥`2^r−1` on some size-`O(r)` formula. Therefore a change of lossless index serializer alone cannot force numeric k to be polynomial in original SAT source length.

The original `MIPRE.GapCompression` resource bound `B(k,lam)=G.bound.eval(k+lam)` is in numeric k, rather than `Nat.size k` or original `esize f`. The existence of exponentially large indices does NOT show the actual compressed verifier uses its upper resource bound, nor that its game cannot be evaluated efficiently through its succinct representation. It shows that an original polynomial-IN-NUMERIC-k theorem cannot, without additional structural proof, certify polynomial-IN-SAT-source-length explicit-game cost.

For classical algorithms, original WP30 remains the exact conditional chain: a separately supplied original polynomial-time oracle that solves the actual compressed-game one-versus-at-most-half promise at its fixed answer budget yields a genuinely original polynomial-time SAT decider (with threshold/budget hypotheses). Neither WP30 nor WP31 constructs or excludes that oracle. A hypothetical classical polynomial-time SAT solver is compatible with every theorem in this tranche.

**Remaining substantive boundary:** `PNP_WP31_ALL_LOSSLESS_NUMERIC_ENCODINGS_EXPONENTIAL_INDEX__BINARY_LENGTH_AWARE_GAME_COMPLEXITY_AND_CLASSICAL_LOWER_BOUND_OPEN`. To proceed, one must either (1) obtain stronger compressor-cost bounds measured in the binary index/source length, (2) replace the lossless single-numeric-index interface with a separate source-data interface whose complexity is fully accounted, or (3) find a new independently proved classical lower-bound mechanism. None is established by counting.

PNP-001 remains open; no P=NP, P≠NP, full polynomial explicit-game reduction or MATHCERT certification is claimed. Full original uncached replay, exact source-byte/Git-blob lock, source axiom audit, protected CI and merge readback are separate admission obligations, not inferred from local Lean compilation.

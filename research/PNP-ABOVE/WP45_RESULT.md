# WP45 — Native total budget selector

WP45 continues the computational-capacity lane WP41, separate from the
already-admitted algebraic WP42–44 source. Pinned upstream
vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970;
Lean 4.35.0-rc3.

## Construction

For any encoded input type and fixed native polynomial witness verifier V,
enumerate the positive integers through 2B using a unary countdown, convert
each to its binary bit string and parse a raw data tree. A canonical program
tree c with encoded size l has a postorder serialization of l bits. Append a
true sentinel at the high end; the resulting integer is positive and less
than 2^(l+1). The parser ignores the sentinel on the singleton stack. Hence
every program with 2^l <= B occurs among the at most 2B entries.

For every raw tree d, including malformed program encodings, simulate the
fixed, scoped clocked universal interpreter under an outer unary clock equal
to its overhead polynomial evaluated at the size of the whole raw input.
This produces a total native PolyTimeFun on every raw input. For a valid
program and inner clock B, the outer clock is sufficient for the documented
universal-machine run. Thus every successful run of cost at most B of every
enumerated valid program produces its exact witness bits in this construction.
Decode all returned raw data as bit strings and run V; retain an accepted
candidate if there is one. A malformed description or a failed clock can
produce a candidate that passes V; this is harmless, because it is itself
a valid witness. The construction does not assert exact weighted-budget
acceptance, unlike WP41's finite specification. A zero budget is allowed
and has an empty enumeration.

If each input admitting a witness has some scoped successful run c,t of
weighted score 2^esize(c)*(t+1) <= p(esize(input)), then both 2^esize(c) and
t are bounded by the polynomial p. Compute that polynomial in unary using
the original Horner source code, then use the above selector. All operations
are native polynomial-time combinators, including the nested clock.
Conversely any fixed polynomial witness solver supplies a bound using its
constant code size and its time polynomial. Therefore existence of a
polynomial weighted bound is equivalent to existence of a single total
polynomial witness solver for the fixed verifier.

## Connection to WP41

Specialize V to WP35.denseWitnessVerifier on Fml. WP35 soundness/completeness
identifies HasWitness with WP38.Sat; WP41.capacity_achieved and capacity_le
identify polynomial weighted bounds with polynomial bounds on WP41.capacity
over YES instances. WP38.native_decision_iff_witness then identifies the
solver with native polynomial SAT decision. The generic construction does
not require importing the long WP35/38/41 proof chain. This last specialization
is a direct mathematical corollary of those protected results; a single
Lean declaration importing them is not included in this generic tranche.

This is a native Levin-style universal-search construction, not a new
general complexity principle or proof of a superpolynomial lower bound.
The weighted capacity lower bound and the standard-machine concordance
remain separate mathematical obligations.

## Verification status

Development compilation passed on all three modules on a replacement authorized Colab CPU runner. The previous session expired, CHAD managed SSD mounts are absent, and no HDD fallback was used. Selective cache recovery required the full pinned mathlib cache; unnecessary OracularDecider and DetypingClock imports were removed. The narrower native parser and clock correctness proof avoid their unrelated game-library dependency chain. Finite controls passed (197 canonical trees, 255 acceptance patterns, 11 budget boundaries). Fresh exact-source replay and standard-axiom audit remain separate gates. No independent certification.

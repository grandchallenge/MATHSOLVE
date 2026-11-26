# WP41: Description-weighted computational capacity and exact budget search

Protected predecessor: WP40 merge b5e94ad38a5f705da99906620f431cc9336c383d.
Pinned upstream: MIPRE-formalization 5926bdff5db621f44682a101007ef2fe3ae8d970;
Lean 4.35.0-rc3.

## Mathematical result

For a satisfiable native Boolean formula f define K(f) as the least natural
number 2^esize(c)*(t+1) over all well-scoped native programs c and actual
charged runs c(encode(f))=encode(w) at cost t, where the WP35 verifier accepts
w. Set K(f)=0 on NO inputs; the zero convention is not a search certificate.
The minimum exists because a short witness can be hardcoded. No uniform
correctness requirement is imposed on c. This measure is a native variant of
Levin-style description-weighted search complexity, not claimed as a new
general complexity principle.

Additive charging cannot overcome the instance-specific hardcoding
obstruction: on every YES input there is an accepted run with
esize(c)+t <= 8*esize(f)+16. The exponential description factor prevents
that particular linear hardcoding estimate from collapsing K. It does not
by itself prove that K grows superpolynomially.

Every fixed polynomial witness program A bounds K on its successful inputs
by 2^esize(A.code)*(A.timeBound(esize(f))+1). Consequently a single
superpolynomial lower bound on K over YES formulas excludes every total
native polynomial witness solver. By WP38, this would also exclude native
polynomial SAT decision. No such lower bound is established here.

## Charged transport law

Suppose actual scoped program c transforms f into a formula g in charged
time s, g is satisfiable, and each dense witness accepted for g is accepted
for f without further decoding. Compose c with an optimal witness program d
for g. The native let construction has exact encoded code size
esize(c)+esize(d)+11, and its run cost is s+t+1. Thus

    K(f) <= 2^(esize(c)+11)*(s+2)*K(g).

The lifting hypothesis is explicit: arbitrary equisatisfiable formulas
with changed witness encodings need a separately charged decoder. For the
WP40 witness-carrying tag, that hypothesis holds for every payload, since
the ordered support and witness verifier are unchanged. The inequality
therefore charges the actual production of the tagged representation,
including any information already present in the transformation's code.
It does not identify equally true formulas as equally easy.

## Exact finite budget search

For a positive budget B, enumerate binary code strings of lengths
0 through floor(log2 B). There are 2^(floor(log2 B)+1)-1 < 2B entries.
For each length n allocate floor(B/2^n)-1 native charged time units,
ignoring zero allowances. Test canonical program encoding and scoping,
run the exact bounded semantics, require canonical encoded output, and
check the witness. The clock allowance including the +1 is at most B at
each length, hence at most B*(floor(log2 B)+1) across all levels.

The two directions are proved for the exact finite search specification:
the candidate list is nonempty iff f is satisfiable and K(f)<=B.
Every returned candidate is an accepted witness. Malformed programs,
invalid scopes and noncanonical results cannot provide false witnesses.
The upstream clocked universal machine provides polynomial overhead for
each valid simulation, but this tranche does not yet compile the complete
enumeration, validation and selection into one native PolyTimeFun in
the unary budget and encoded formula. The sum-of-clocks bound is not a
claim about the runtime of the entire search implementation.

## Next concrete obligation

Implement that bounded uniform selector, with the polynomial budget
provided in unary, canonical code parsing and native verified witness
checking. Its existence would close the converse: a polynomial upper
bound on K over satisfiable formulas yields a polynomial witness solver.
The substantive hardness problem is then to establish a superpolynomial
lower bound on K, not to repeat reductions or count representations.
No general classical lower bound, separation or independent certification
is claimed. The standard-machine concordance is a separate lane.

## Verification

Development compilation of both new modules passed via the approved
native Linux alternate runner. Fresh guarded source-lock replay and
axiom audit, protected checks and merge/readback are separate gates.

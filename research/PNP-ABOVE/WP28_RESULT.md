# PNP-ABOVE WP28A — no fixed source lambda for the hardcoded SAT verifier family

Scientific scope: narrow original-source negative theorem, NOT a claim
that uniform SAT verification or general P-versus-NP lower bounds are
impossible. Exact candidate full uncached replay and protected admission
are separate gates.

Protected mathematical parent: grandchallenge/MATHSOLVE
6182a58097b759119767dc78255e0c38d9f21e03 (WP27 admitted).
Pinned original: vidick/MIPRE-formalization
5926bdff5db621f44682a101007ef2fe3ae8d970,
Lean v4.35.0-rc3. PNP-001 MATH-PROGRAMME issue #162 OPEN.

## Exact source mathematics

WP27 proves for each *fixed* formula f that its original seven-level
robustVerifier admits SOME source-bound exponent lambda. It does not
supply one lambda that works for ALL f.

WP28 constructs original formulas longFormula n = n iterated NOT gates
on true. Their original size is at least n. The pinned source's
hardcode_size theorem gives the exact equality

    esize (robustSourceGenerator f)
      = esize rawCore.code + esize f + 35.

An original-source wrapper-size lemma proves the actual native
Verifier 7 contains its embedded decider data. Then the original
Verifier.IsBounded condition V.size <= lambda yields, for every
actual Cost.UniversalMachine U and source CL.Sampler 7 S,

    NOT (EXISTS lam, FORALL f : MIPRE.SAT.Fml,
      (WP27.robustVerifier U S f).IsBounded lam).

The explicit counterexample for any lam is longFormula (lam + 1).
The eight new public original Lean theorem declarations in
WP28_UniformExponentObstruction.lean have a local kernel compilation
and must pass source lock, new axiom audit and full uncached replay
before protected admission.

## Correct scientific interpretation

This is a quantified **representation-boundary** theorem, not a
complexity lower bound. The source-hardcoding implementation cannot
have one globally fixed native boundedness exponent because the
source description necessarily grows without bound with its input
formula. A fixed-code verifier with variable runtime input can
avoid this particular obstruction. Existence of efficient SAT
verification is not challenged.

Still OPEN: original-source polynomial instance-to-index encoding,
fixed-code runtime bounds, quantitative uniform lambda selection,
compressor input/output program and description-size accounting,
machine/NP-endpoint equivalences, deterministic classical SAT-search
lower bounds, P=NP/P!=NP and MATHCERT certification.

Next: WP28B_VARIABLE_INSTANCE_SOURCE_INDEX_AND_UNIFORM_RUNTIME_ACCOUNTING.

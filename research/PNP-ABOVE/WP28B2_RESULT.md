# PNP-ABOVE WP28B2 — one fixed native SAT verifier with uniform source bound

Disposition: original Lean-kernel-checked mathematical SOURCE CANDIDATE.
Full uncached independent source replay, protected-source lock and protected
admission remain required. This is NOT P-versus-NP certification.

Exact protected parent for this candidate: MATHSOLVE/main at
d41eb5f2af9856080fa10a7a093d1ea5d0672e08, incorporating
independent WP28B1 protected merge b9006e1a3dc11e55d2c900d71b375231f3074042
(PR #1271) and a subsequent unrelated Erdős #602 CI workflow
repair. The pinned original WP28B1 candidate
was 1e4208f40cdc73a541929b28a5a46a5bd25f63de.
Original pinned source vidick/MIPRE-formalization at
5926bdff5db621f44682a101007ef2fe3ae8d970, Lean v4.35.0-rc3.

## Unconditional fixed-source theorem

Four original Lean modules implement 22 theorem declarations against
the ORIGINAL pinned MIPRE hierarchy, including source Cost.PolyTimeFun,
Cost.Prog, CL.Sampler 7, Verifier 7, Decider.Accepts,
Verifier.IsBounded and Verifier.valStar.

1. WP28B2_NodeReader.lean builds a SINGLE fixed, polynomial source
   program parsing arbitrary source Data nodes into original SAT.Fml.Node,
   including malformed-input defaults, and proves exact source-list
   reconstruction at every original formula encoding.

2. WP28B2_Evaluator.lean composes the original indexed decoder from
   WP28B1 with the admitted source RPN evaluator from WP25, and source
   answer equality. It proves that source-prog result at index
   formulaIndex f and arbitrary answer strings equals
   f.eval(answer) AND equality(Alice,Bob). An ACTUAL ORIGINAL
   Cost.PolyTimeFun machine is constructed with a polynomial run
   certificate, not a SAT oracle.

3. WP28B2_RawVerifier.lean composes the admitted WP27 robust
   malformed-input raw-tuple normalizer with the indexed source
   evaluator, yielding ONE fixed
   indexedRawChecker : PolyTimeFun Data Bool.
   Its CODE does not depend on any SAT formula. It proves actual
   ORIGINAL Prog.HasPolyCost for ALL raw Data inputs using original
   PolyCost. The original Verifier.ofSamplerDecider wrapper provides
   native Verifier 7 with original question-length checks.
   The exact source acceptance predicate is proved for every
   formula at its index and all question and answer strings.
   The original upstream genuine G.sampler 0 and HasPolyCost imply
   that there exists a ONE FIXED exponent lambda with
   fixedIndexedVerifier.IsBounded lambda; lambda is independent of f.

4. WP28B2_NativeValues.lean proves original
   Verifier.HasPerfectPCC for SAT with witness answer budget T >= m,
   unconditional rejection of all answer pairs for UNSAT with
   scoped source variables, exact original tensor Verifier.valStar
   values 1 for SAT and 0 for UNSAT, source synchrony, and
   equivalence with original SAT.Cnf3 satisfiability.
   Accepted answers contain an actual classical SAT witness;
   a SAT witness produces accepted source answers. This is
   classical WITNESS transfer, not an algorithm to find witnesses.

## Exact source complexity and remaining boundary

The index contains exactly esize f + 1 bits, but its NUMERIC VALUE
satisfies the formally proved inequality

    2 ^ (esize f) <= formulaIndex f.

Thus native Verifier.IsBounded lambda in NUMERIC index n does not,
on its own, establish a classical polynomial bound in SAT formula
description length. Formula indexing and source evaluator are
genuine original source programs polynomial in binary encoding
length; the source sampler's questions and answer budgets
may grow as polynomials in numeric n (potentially exponential
in SAT input size). Their full-game cost is not established
polynomial in source SAT input length.

Second interface mismatch: original MIPRE GapCompression transfers
promises at the special input index 2^k, whereas the proved game
encodes formula f at formulaIndex f. No 2^k compatibility theorem
exists, so do not silently apply source compression to the
arbitrary encoded SAT instance.

Third remaining obligation: source finite 3CNF list-to-Fml
compiler is semantic only, not yet an original PolyTimeFun
(List Clause3) Fml, and the set-valued Cnf3 is not itself
an original source encoding.

Not proved: an actual polynomial-time SAT-to-compressed-game
reduction; any classical SAT search lower bound; P=NP, P!=NP,
or public MATHCERT certification.

Next boundary:
PNP_FIXED_VERIFIER_NATIVE_01_UNIFORM_LAMBDA_PROVED
__SAT_LENGTH_POLYNOMIAL_COMPRESSED_REDUCTION_OPEN.

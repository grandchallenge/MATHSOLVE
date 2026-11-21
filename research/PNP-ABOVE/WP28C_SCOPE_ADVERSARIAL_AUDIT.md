# WP28C — internal Verifier / Adversary / Referee source scope

Verifier: The original source Cost.PolyTimeFun computes an index
transformation 2^k -> k, and the exact original source five-field
normal verifier accepts iff the decoded original SAT formula is
satisfied and two answers are equal, with native dimension checks.
A genuine original CL.Sampler 7 and original source GapCompression
structure are used, not a surrogate game or imported oracle.

Adversary: The 2^k interface is now matched correctly, rather than
the invalid replacement 2^k = formulaIndex f. However the
NUMERIC compressed game index k may be exponential in SAT
formula source length, so G.bound(k+lam) is not certified
polynomial in SAT input length. Threshold G.C0 <= k and
witness-budget m <= (2^k)^lam are not silently omitted.
Finite original 3CNF list-to-Fml source compiler remains open.
No downstream classical complexity separation is entailed.

Referee restricted scope after exact full uncached original
source lock, all new kernel axioms and protected checks:
ADMIT_NATIVE_FIXED_SAT_INDEX_POWER_COMPRESSOR_PROMISES_ONLY.

PNP-001 remains OPEN on source-length polynomial full-game
reduction, witness and threshold normalization, explicit original
3CNF compiler, and any classical hardness endpoint.
Internal multi-role logical audit is not external MATHCERT.

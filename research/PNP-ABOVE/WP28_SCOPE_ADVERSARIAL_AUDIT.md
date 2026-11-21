# WP28A internally scoped Verifier, Adversary and Referee review

Verifier: Eight source Lean statements use original MIPRE.SAT.Fml,
original Cost.hardcode_size, actual source verifier wrapper code,
the actual original Verifier 7.size, and the required IsBounded source
size clause. No theorem merely assumes source code length constraints.

Adversary: An existential lambda for each f can coexist with absence
of a single lambda for all f. The explicit witness is a family of
trivial iterated negation formulas; the proof uses code description
growth, NOT SAT hardness, game value, or a quantum argument. The
result does not preclude a fixed verifier receiving a formula as
runtime input, nor claim any complexity-class separation.

Referee restricted disposition:
NO_FIXED_ORIGINAL_ISBOUNDED_LAMBDA_FOR_WP27_HARDCODED_SAT_FAMILY.
Admission requires separate full source-locked uncached replay,
eight original kernel standard-axiom audits and protected branch CI.
No external certification.

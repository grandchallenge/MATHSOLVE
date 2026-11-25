# PNP-ABOVE WP23B — native source verifier to succinct 3SAT

Scientific disposition (PENDING exact replay and protected admission):
WP23B_ORIGINAL_COOK_LEVIN_BRIDGE_AND_FIXED_GAME_SAT_MASK__SAT_HARDNESS_NOT_TRANSFERRED.

Protected predecessor: MATHSOLVE c6a3bb4c389baa093a4acbd644284b343e42d08c.
Original source: vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970, Lean v4.35.0-rc3.
Active research: MATH-PROGRAMME #162 (OPEN).

## Actual mathematical claims

The original pinned MIPRE formalization contains a CONSTRUCTED succinct
Cook-Levin instance SAT.succinctCookLevin in MIPRE/TM/CookLevin/Assemble.lean,
not only an uninhabited theorem interface.

WP23B instantiates the original polynomial-time source circuit describer with
the actual WP21 Cost.Prog native CHSH decider, not an abstract game predicate.
For all original valid n,T,Q,sigma,x,y and tape blocks A,B, the generated
original 3SAT formula admits an assignment extending A,B iff these are the
original two-bit encoded answer tapes for original source-machine responses
accepted within cost T. Existential satisfiability is exactly existence of
bounded accepted responses; the source execution bound is explicit.

An independent kernel-checked original-source Eval lemma gives an explicit
instruction-count upper bound to every original native acceptance, and
nativeTimeParameter is computable from input/source lengths and costs and
dominates the original Cook-Levin validity conditions. Thus acceptance gives
a satisfying assignment for the actual describer.

## Negative complexity-transfer result

At the canonical explicit time parameter, the real generated succinct 3SAT
formula of this fixed Bell verifier is satisfiable iff all conditions hold:
n is nonzero, x.length=9, y.length=9, x[8]=false, y[0]=false.
The converse constructs a native original one-bit response: Alice's bit
is x[0] AND y[8], Bob's bit is false. This is a very restricted and
easily recognizable class of SAT circuits.

Cook-Levin in this direction is verifier-acceptance-to-SAT. It does not
encode arbitrary SAT instances into a hard source game; it does not yield
a deterministic lower bound or solve P versus NP. The seven-level
compression value-one PCC / quantum-at-most-one-half promise requirements
remain unmatched for this fixed nine-level CHSH verifier.

## Exact local proof evidence

The imported original MIPRE.TM.CookLevin.Assemble source was built from
the pinned original upstream by the original Lake build (3,707 build jobs,
exit 0). The five new Lean source modules establish 20 public theorem
declarations; the local exact source SHA-256/Git blob lock passed, and every
declaration's original pinned Lean kernel axiom report shows only propext,
Classical.choice, Quot.sound or no axioms.

These are LOCAL original-source compilation, axiom, and source-lock results.
The complete independent-from-cache inherited WP08–WP23B exact-candidate
replay, GitHub protected checks and merge readback remain separate evidence
conditions, not implied by the local work.

## Technical and governance boundaries

The new source modules must be compiled against original upstream Lean,
exact source locks, standard-axiom audit, and full inherited WP08–WP23B
protected-admission replay. The PNP development cache may accelerate
preliminary edits but cannot be used as evidence for protected admission.

Next research target: an original source-native SAT-INSTANCE-DEPENDENT verifier
family with an exact compatible compression interface and substantive
classical strategy to SAT runtime transfer. These steps and independent
MATHCERT certification remain OPEN.

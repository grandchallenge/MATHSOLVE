# PNP-ABOVE WP08 — Native nine-bit identity decider execution receipt

**Disposition:** finite executable source-native decider component with imported type closure proof, exact code hash, exhaustive diagonal-sample checks, and explicit claim boundaries. Not a full nine-level sampler, normal-form verifier, positive-parameter introspection run, or P-versus-NP result.

## Source and execution identity

- Parent: [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136).
- Upstream pin: [vidick/MIPRE-formalization commit 5926bdff5db621f44682a101007ef2fe3ae8d970](https://github.com/vidick/MIPRE-formalization/tree/5926bdff5db621f44682a101007ef2fe3ae8d970).
- Actual imported source types: `MIPRE.Cost.Prog`, `MIPRE.Cost.Data`, `MIPRE.Cost.SizedEncoding`, `MIPRE.Decider`, from `MIPRE.Foundations.Verifier`.
- Toolchain: pinned upstream Lean 4.35.0-rc3 and Mathlib lock. The real upstream modules had previously been built.
- GCL source: [WP08_NineBitDecider.lean](WP08_NineBitDecider.lean). Exact Git blob SHA-1 `45b9fa687fad92bf1b1d4be2809473e0c4f9957d`; source SHA-256 `027384e4a0b7de9551b69d2b5a22ad8589c1707367de96f5caa4956e364715a9`. The source was retrieved from the GitHub research branch, and the local `git hash-object` returned that same blob SHA-1.
- Executed: `lake env lean /tmp/gcl-pnp-wp08/NineBitDecider.lean` from the pinned upstream checkout.
- Clean final run: process exit code **0**, no Lean warnings or errors; its log SHA-256 `bae83ce00f1ca53ef45d2340a020bde40cb1685df59c9262b1e9d8412d9858e9`. GCL CONTROL launch capture `3d4c621b87a1456d8bbfd57ef8638b87`, exit/log readback `5a50a25ea1eb4b51bf8220afabb207cb`. These are **local OS** execution captures, not independent mathematical certification.

## Constructed native source program

The file defines a `Prog` which consumes the source's canonical **right-nested five-field input** `encode (n,x,y,a,b)`. For well-typed inputs it returns the encoded Boolean `true` precisely when the binary index is positive, both question bit strings have length **nine**, and both answer strings are empty. Its finite unrolled `checkBits` parser rejects malformed bit-tree heads and other bit-string lengths.

The input bit-list recognition is encoded entirely through source `Prog.elim`, `Prog.let_`, and `Prog.const`, with explicit de Bruijn variable indices. A structurally inductive Lean theorem `checkBits_wellScoped` establishes binding correctness, and `identityDecider` constructs the **actual upstream `MIPRE.Decider`** with a Lean-checked `WellScoped 1` witness.

The value of `esize identityDeciderProg` was evaluated by Lean as **145,459 nodes** in the source's size-aware program encoding. This is a fixed finite description length, not a claimed globally minimized encoding or compressed output size.

## Finite execution checks

A separate `runFuel` interpreter implements the seven native `Prog` evaluation clauses and the source cost arithmetic; it runs directly on the actual imported `Prog` datatype. The file checks:

- Three ordinary positive-index acceptances with nine-bit question strings and empty answers.
- Rejection for zero index, lengths eight and ten on either question, and nonempty answers on either side.
- Direct malformed raw input rejection and insufficient recursion fuel.
- **All 512 diagonal question pairs** `(z,z)` for nine-bit vectors `z`. The reference input game has exactly these 512 supported pairs. This does not exhaust the 512-squared off-diagonal question pairs, nor assert anything about the compressed game.
- A specially malformed bit-tree head with a nominal nine-element list shape, confirming that the parser checks **canonical element encodings**, not only list depth.

Lean passed all guards. The example `runFuel 96 [encode (2,zeroNine,alternatingNine,[],[])] identityDeciderProg` printed `some (MIPRE.Cost.Data.cons MIPRE.Cost.Data.nil MIPRE.Cost.Data.nil, 63)`, so it returned canonical encoded `true` at **63 source-model time units**.

**Verification boundary:** `runFuel` computes source-style costs, but WP08 has **not** proved a general `runFuel_sound` theorem connecting every successful interpreter result to imported `MIPRE.Cost.Eval`. The evidence here is executable finite checks and a genuine kernel-checked program scoping theorem; a universal `Decider.Accepts` equivalence theorem and a formal running-time bound remain open. The parser only requires the *raw* binary-index subtree to be nonempty; on the well-typed `encode n` inputs this means `n>0`, while some noncanonical raw index subtrees may pass. Consequently **no raw-data canonicality theorem is claimed**.

## Remaining obligations

1. Construct the true nine-level `MIPRE.CL.Sampler 9`: canonical `Sampler.Query` input, dimension 9, identity marginals, factor indicators, linear maps, termination proof, and `CLFun.ExactlyOn`.
2. Prove the imported `Decider.Accepts` contract, uniform `TimeBoundAt` and the `Verifier.accepts_length` obligation, including malformed inputs.
3. Produce an actual `MIPRE.Verifier 9` and a positive `IsBounded λ` witness. The size 145,459 is a concrete description-size input to that budget, not a complete bound.
4. Instantiate the formalized `ClockedUniversalMachine` and **execute** the positive-parameter `DecisionCompiler.compute` on the real sampler/decider pair. Do not conflate successful compilation of the module with execution of its transformation.
5. Complete source-faithful answer reduction and repetition, and establish or refute a separately proved uniform SAT-to-classical-cost transfer. Schmidt-rank growth does not imply classical time hardness.

**No full quantum compression, classical resource lower bound, general SAT transfer or P != NP result is claimed.**

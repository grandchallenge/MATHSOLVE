# WP36B — native valid-index quadratic lower bound

Pinned original source: `vidick/MIPRE-formalization@5926bdff5db621f44682a101007ef2fe3ae8d970`. Protected parent `bd8daf39ffc2d9f7b3a1ce1a7c192912b29450c7` contains WP36A; WP35 is protected at #1288.

The previous candidate's unqualified `encode_fml` has been corrected to `Fml.encode_fml`. The complete source, including the genuine WP34 compressed YES/NO connection and all 14 theorem declarations, compiled against the pinned source and retained exact prior replay dependencies. All 14 kernel axiom reports are subsets of {propext, Classical.choice, Quot.sound}. Development audit SHA256: `41950441a995cd638f3952d8c07218694194c2b0546491a553108c2a4877fab1`.

## Mathematical result

For every fixed original program p correct on all valid compressed promise indices, for every r >= max(G.C₀,1), the two genuine indices for WP32.padTrue r (.const true/false) have source encoding length at most 64r+41, with actual runs of costs t and u. Both satisfy 9r² < H(p)(t+3r) and 9r² < H(p)(u+3r). H(p) is the original WP36A constructor-count function named height, not a bound on dynamic iterations. Thus the native model has an unrestricted-over-fixed-programs quadratic worst-case lower bound for this restricted valid-index family. No polynomial assumption on p or bound on its space is required. Native verifier boundedness remains explicit. The proof uses exact YES/NO promises, not an unrelated abstract game.

The coefficient is program-dependent. The hard inputs have empty variable support. This establishes charged-copy input-access overhead, not intrinsic SAT hardness, not a uniform lower bound for growing nonuniform descriptions, and not a standard multitape Turing-machine lower bound. It does not exclude polynomial algorithms of degree two or more. The superpolynomial target is open.

## Replay and review

WP36B_REPLAY.py stages the exact previously replayed WP08–WP35 and WP36A source modules and compiled dependency objects, verifies source identities against protected source, then freshly compiles the new module in an isolated directory and audits all 14 theorem axioms. The prior complete WP35 and separate fresh WP36A replay evidence must be supplied. This is incremental verification against retained local dependencies, not a second fresh reconstruction of all 97 predecessors. To reconstruct the full dependency chain, first run the existing WP35_REPLAY.sh and WP36A_REPLAY.py in fresh directories, then the WP36B entry point with those results. No skip flag, source mutation, or new axioms are allowed.

Internal scope audit: the prefix length, sentinel, exact source cost, threshold and native compressed YES/NO premises are proved in the original model. No standard machine equivalence, independent external verification or certification is inferred. Protected admission is a separate step.

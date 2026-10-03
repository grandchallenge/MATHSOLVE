# OM26-H1 MATHCERT handoff — H1-02 and H1-07

**State:** `PREPARED__PROTECTED_SOLVE_BIND_PENDING`

## Claim A — exact face criterion

Requested Cert object: adjudicate the theorem in `FACE_CRITERION.md` that counted triangular faces are exactly the nondegenerate arrangement-graph 3-cycles, including the allowed parallel/concurrent/vertex-touch degeneracies.

Evidence surfaces:

- Forge source/evaluator lock at `grandchallenge/MATHFORGE@73f1890387eec56eb6be31f8c00f10b6a5a56383`;
- `FACE_CRITERION.md`;
- `H1_02_PROOF_RECEIPT.json`;
- independent direct oracle `kobon_direct_oracle.py`;
- falsification ledger and property tests;
- GitHub Actions run `36356017300`, job `108723788668`.

## Claim B — concrete n=18 construction

Requested Cert object: independently replay the exact candidate `RD_LOCAL_MUTATION_086/solution.json` and adjudicate only the statement that it has 86 counted triangular faces under the locked hill semantics.

Evidence surfaces:

- candidate Git blob `17f8355b484bacf115bafd413de9a0be8f8e3385`;
- candidate SHA-256 `05a5f519433a0787a96a3f6c5a8cef17fc7f8ab093ccf0c9ab45a2d564ad11d5`;
- proposal-generator receipt;
- independent direct-oracle replay = 86;
- authenticated AutoLab public evaluator replay = 86;
- `H1_07_REPLAY_RECEIPT.json`.

## Explicit exclusions

Do not adjudicate or infer that 86 is best known, optimal, novel, prior, officially accepted by AutoLab, or publication-ready. Those are separate questions with separate evidence requirements.

After this PR is protected, bind this packet to the exact protected Solve commit in MATHCERT #339.

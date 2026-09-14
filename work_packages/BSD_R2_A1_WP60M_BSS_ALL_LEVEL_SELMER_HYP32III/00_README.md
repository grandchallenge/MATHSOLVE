# BSD-R2-A1 WP60M — all-level Selmer-restricted replacement for BSS Hypothesis 3.2(iii)

## Status

Bounded mathematical work package under `grandchallenge/MATHSOLVE#235`.

Protected base:

`a055313fce7f1cbe28d5f7db4b7e42a21f9eca8e`.

## Objective

Protected WP60K proves the unchanged finite BSS Hypothesis 3.2(iii) fails already at `E[4]`. Protected WP60L proves its unique mod-4 defect is extraneous to every canonical modified primal and dual Selmer group.

WP60M determines whether that repair persists uniformly through every finite coefficient level `E[2^m]` required by the BSS inverse-limit architecture.

## Result

For every `m>=2`, put

`G_m=GL_2(Z/2^m)` and `V_m=(Z/2^m)^2`.

WP60M proves

`H^1(G_m,V_m) ~= Z/2`.

The unique nonzero class is the top-2-torsion inflation of the protected WP60K class. At the primitive upper unipotent `U`, it has value

`(0,2^(m-1))`,

so it restricts nontrivially to the fixed protected odd multiplicative inertia group.

For the BSS finite auxiliary field at coefficient level `E[2^m]`, the same order-two group is the full restriction kernel. The fixed odd-depth prime has odd Tamagawa factor; the propagated canonical local condition there is the self-dual local Kummer image. Hence the unique defect lies in neither the primal nor dual canonical condition at every level.

Therefore restriction to the BSS finite auxiliary field is injective on every canonical modified primal and dual Selmer group for every `m>=2`.

Record

`BSS_LITERAL_P2_SELECTED_ALL_LEVEL_HYP32III_DEFECT_SELMER_EXTRANEOUS`.

This removes the Hypothesis-3.2(iii) contribution from the selected all-level finite coefficient-reduction chain. The independent literal-`2` simultaneous-localization/core-vertex connectivity problem remains open.

## Files

- `01_ALL_LEVEL_SELMER_RESTRICTED_THEOREM.md` — theorem and proof.
- `02_ALL_LEVEL_COHOMOLOGY_CERTIFICATE.py` — exact finite certificate for the residual representation-theoretic lemmas and the protected mod-4 seed.
- `03_CLAIM_LEDGER.yaml` — bounded claim state.
- `04_PROOF_DEPENDENCY_NOTE.md` — proof architecture and BSS dependency boundary.
- `handoffs/BSD-001/WP60M_FRONTIER.md` — successor frontier.

## Claim firewall

WP60M does not establish:

- full BSS Hypothesis 3.2(iii) at any `m>=2`; those global groups are nonzero;
- simultaneous one-primal/one-dual localization under unchanged BSS Lemma 3.9 at `p=2`;
- the WP60H three-term-relation exclusion or core-vertex connectivity;
- BSS Theorem 5.20, 5.2, 5.25, or Corollary 6.15 at literal `p=2`;
- R5-LIFT, R5-PRIM, `BSD-R2-A1`, or MATHCERT certification.

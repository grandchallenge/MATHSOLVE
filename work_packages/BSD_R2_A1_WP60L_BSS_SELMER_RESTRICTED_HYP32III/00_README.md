# BSD-R2-A1 WP60L — Selmer-restricted mod-4 replacement for BSS Hypothesis 3.2(iii)

## Status

Bounded mathematical work package under `grandchallenge/MATHSOLVE#233`.

Protected base:

`303c5662a62c9dda62e9c9f0ba1abae8e27f3b16`.

## Question

Protected WP60K proves that the unchanged BSS II Hypothesis 3.2(iii) is false already for

`A=E[4]`.

WP60L asks the narrower question actually relevant to the BSS modified-Selmer proof chain:

> Does the nonzero global restriction-kernel class occur inside the canonical modified Selmer spaces on which the Chebotarev and coefficient-reduction arguments operate?

## Result

WP60L proves that it does not.

At coefficient level `E[4]`:

1. the full BSS finite auxiliary cohomology group has order exactly `2`;
2. its unique nonzero class restricts nontrivially to inertia at the protected odd-depth multiplicative prime;
3. the propagated canonical local condition there is the local Kummer image and is self-annihilating under Tate local duality;
4. hence the unique defect lies in neither the primal nor dual canonical local condition;
5. every BSS modified primal and dual Selmer group retains that local condition at the original bad prime, so restriction to the finite BSS auxiliary field is injective on all of those modified Selmer groups.

This gives a literal-`2`, mod-`4`, Selmer-restricted replacement for the **restriction-injectivity use** of Hypothesis 3.2(iii). It also permits the one-class Chebotarev step used inside the proof of BSS Lemma 3.10 for free submodules contained in these modified Selmer groups.

## Files

- `01_SELECTED_MOD4_SELMER_RESTRICTED_THEOREM.md` — theorem and proof.
- `02_MOD4_LOCAL_DEFECT_CERTIFICATE.py` — exact finite certificate for the obstruction class, inertia restriction, and residual invariants.
- `03_CLAIM_LEDGER.yaml` — bounded claim state.
- `04_SOURCE_AND_DEPENDENCY_NOTE.md` — exact BSS dependency trace and local-duality interface.
- `handoffs/BSD-001/WP60L_FRONTIER.md` — successor frontier.

## Claim firewall

WP60L does **not** prove:

- full BSS Hypothesis 3.2(iii) at `E[4]`; WP60K proves it is false;
- the analogous Selmer-restricted injectivity for every `E[2^m]`;
- a literal-`2` replacement for simultaneous one-primal/one-dual localization at mod `4`;
- the WP60H three-term-relation exclusion or core-vertex connectivity;
- BSS Theorem 5.20, Theorem 5.2, Theorem 5.25, or Corollary 6.15 at `p=2`;
- R5-LIFT, R5-PRIM, `BSD-R2-A1`, or MATHCERT certification.

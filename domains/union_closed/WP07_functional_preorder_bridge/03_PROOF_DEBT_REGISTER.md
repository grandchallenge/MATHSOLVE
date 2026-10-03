# WP07 Proof Debt Register

Date: 2026-09-24

| Debt ID | Obligation | Status | Evidence / remaining gate |
|---|---|---|---|
| WP07-D001 | Reconcile, independently build, and audit the selected `kashiwabarakenji/avg-rare` revision. | Closed | Exact selected revision built and audited; source provenance protected in MATHFORGE. |
| WP07-D002 | Formalize the finite functional-chain obstruction to direct `IsIdealFamilyOn` reuse. | Closed | `functional_three_chain_not_IsIdealFamilyOn`; exact four-member family checked by `chain_idealFamily_eq_expected`. |
| WP07-D003 | Define a local functional-preorder order-ideal family predicate over `Family α`. | Closed | `IsFunctionalPreorderIdealFamilyOn`; explicit finite carrier and extensional family equality. |
| WP07-D004 | Prove average rarity for the exact D003 predicate. | Closed locally | `sourceShapedMainNDS` and `d004_averageRarity`; explicit audited semantic transport. |
| WP07-D005 | Connect D004 average rarity to complement abundance. | Closed and independently qualified | Local theorem surface protected in MATHSOLVE; bounded MATHCERT disposition `QUALIFIED` at merge `245a2f395c358a8d11941e7085512a2e53751619`. |

## D005 proof boundary

D005 uses only the exact D003 hypothesis plus D004 average rarity.

```text
functional-preorder order ideals
  -> intersection closure
  -> carrier-relative complements are union-closed

D004 average rarity
  -> incidence double counting
  -> one rare carrier element
  -> exact complement frequency identity
  -> one abundant supported complement element
  -> restricted Frankl abundance
```

This is not a reuse of `IsIdealFamilyOn`; D002 remains the checked reason that
such a reuse would be invalid.

## Remaining campaign debt outside WP07

The former exact universal representation subroute has been refuted in WP08:

```text
arbitrary finite union-closed family
  -/-> exact complement of a D003 functional-preorder ideal family
```

The obstruction is formal: exact D003 complements are intersection-closed, but
a concrete three-point union-closed family need not be.

This negative result does not close `UC-P04`. It sharpens it.

The successor obligation is to extend the rare-element mechanism from the
functional-preorder subclass toward broader finite closure systems and to build
an incidence-preserving interface to the WP05 lattice spine.

```text
UC-P04 = OPEN
UC-FRANKL = OPEN_PROBLEM
```

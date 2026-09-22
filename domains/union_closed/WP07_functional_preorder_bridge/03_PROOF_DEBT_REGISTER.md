# WP07 Proof Debt Register

Date: 2026-09-21

| Debt ID | Obligation | Status | Evidence / remaining gate |
|---|---|---|---|
| WP07-D001 | Reconcile, independently build, and audit the selected `kashiwabarakenji/avg-rare` revision. | Closed | Exact selected revision built and audited; source provenance protected in MATHFORGE. |
| WP07-D002 | Formalize the finite functional-chain obstruction to direct `IsIdealFamilyOn` reuse. | Closed | `functional_three_chain_not_IsIdealFamilyOn`; exact four-member family checked by `chain_idealFamily_eq_expected`. |
| WP07-D003 | Define a local functional-preorder order-ideal family predicate over `Family α`. | Closed | `IsFunctionalPreorderIdealFamilyOn`; explicit finite carrier and extensional family equality. |
| WP07-D004 | Prove average rarity for the exact D003 predicate. | Closed locally | `sourceShapedMainNDS` and `d004_averageRarity`; explicit audited semantic transport. |
| WP07-D005 | Connect D004 average rarity to complement abundance. | Closed locally | `functionalPreorderIdealFamily_inter_closed`, `complementFamilyOn_unionClosed_of_functionalPreorder`, `exists_rare_of_averageRare`, `d005_complement_averageAbundant`, and `d005_complement_frankl`. |

## D005 proof boundary

D005 uses only the exact D003 hypothesis plus D004 average rarity.

The closure chain is:

```text
functional-preorder order ideals
  -> intersection closure
  -> carrier-relative complements are union-closed

D004 average rarity
  -> incidence double counting
  -> one rare carrier element
  -> exact complement frequency identity
  -> one abundant supported complement element
  -> restricted Frankl abundance.
```

This is not a reuse of `IsIdealFamilyOn`; D002 remains the checked reason that
such a reuse would be invalid in general.

## Remaining campaign debt outside WP07

WP07's restricted local obligations are complete. The campaign still has the
universal representation boundary:

```text
arbitrary finite union-closed family
  ?-> complement of an exact D003 functional-preorder ideal family.
```

No such bridge is proved. Therefore `UC-P04` and `UC-FRANKL` remain open.
Independent MATHCERT adjudication of the new D005 restricted theorem is also a
separate governance step, not part of local theorem closure.

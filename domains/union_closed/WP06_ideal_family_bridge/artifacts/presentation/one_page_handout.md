# WP06 One-Page Handout: Ideal Families To Union-Closed Abundance

## One Sentence

MATHCERT proves that every finite local ideal family is average-rare, and
therefore its complement family is union-closed and Frankl-abundant.

## The Picture

```text
downward-closed ideal family
  -> average rarity
  -> take complements in the ground set
  -> union-closed family with an abundant element
```

## The Obstruction

Having one rare element is not enough to prove average rarity. Average rarity
is a global incidence-counting statement over all elements.

## The Mechanism

The proof uses NDS, trace, and contraction:

- NDS measures the global imbalance;
- trace removes one ground element;
- contraction records members that contained that element;
- the exact trace-difference formula makes the induction close.

## The Checked Theorems

- `localIdealFamily_port_nds_nonpos`
- `localIdealFamily_averageRare`
- `localIdealFamily_complement_frankl`

## Claim Boundary

This proves a restricted ideal-family corridor. It is not a proof of Frankl's
conjecture for arbitrary union-closed families.

## What To Read Next

- `02_LAY_COMPANION.md` for the object;
- `03_OBJECT_AND_OBSTRUCTION.md` for the key obstruction;
- `06_DEPENDENCY_DAG.md` for the proof spine;
- `09_CLAIM_LEDGER.yaml` for the claim boundary.


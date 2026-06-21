# Failure And Negative Results

## Failed Route: Rare Vertex Implies Average Rarity

The first natural shortcut is false:

```text
there exists a rare element
  therefore the whole family is average-rare
```

MATHCERT records the failure with:

```lean
existsRare_not_sufficient_for_averageRare
```

The reason is structural. A single rare element controls one column of the
incidence table. Average rarity controls the total incidence count across all
columns.

## Failed Trust Route: Import Upstream As Proof

The external ideal-family Lean development is useful source material, but the
audited proof surface contained active placeholders at the recorded commit and
did not become a clean trusted dependency for this package.

WP06 therefore uses it only as provenance. The theorem promoted here is the
local MATHCERT proof.

## What These Failures Rule Out

They rule out:

- using rare-vertex existence as a proof of average rarity for arbitrary
  finite families;
- promoting the upstream NDS theorem as a trusted local theorem without a
  placeholder-free, reproducible upstream build;
- presenting the complement theorem as progress on arbitrary union-closed
  families.

## What They Leave Viable

They leave viable:

- average-rarity proofs using global incidence/NDS invariants;
- local ports of external source ideas into MATHCERT when the proof boundary is
  rebuilt and checked;
- restricted Frankl-facing results for families known to arise as complements
  of local ideal families.


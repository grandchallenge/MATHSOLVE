# Theorem Spine

## Definitions

| Name | Role |
|---|---|
| `Family alpha` | Public finite-family representation, `Finset (Finset alpha)` |
| `IsIdealFamilyOn F U` | Local ideal-family hypotheses on a finite ground |
| `IsAverageRareOn F U` | Average rarity inequality for local families |
| `toPortIdeal F U h` | Translation to the predicate-style ideal surface |
| `nds` | Normalized-degree sum on the ported surface |
| `complementFamilyOn F U` | Family of complements `U \ S` for `S in F` |
| `IsFranklAbundant` | Local Frankl half-frequency conclusion |

## Spine Nodes

| Node | Role | Checked theorem |
|---|---|---|
| `WP06-S1` | Representation bridge | `toPortIdeal_carrier_eq`, `toPortIdeal_degreeNat_eq_freq`, `toPortIdeal_nds_eq` |
| `WP06-S2` | Rare-vertex source | `localIdealFamily_exists_rare` |
| `WP06-S3` | Average-rarity boundary | `existsRare_not_sufficient_for_averageRare`, `isAverageRareOn_iff_sum_freq_on` |
| `WP06-S4` | NDS support layer | `IdealFamily.SetFamily.sum_normalizedDegree_over_ground_eq_nds` |
| `WP06-S5` | Trace and contraction | `IdealFamily.Ideal.trace_carrier_eq_del_union_contr`, `IdealFamily.Ideal.contrIdeal` |
| `WP06-S6` | Exact trace difference | `IdealFamily.Ideal.nds_diff_trace_as_normdeg` |
| `WP06-S7` | Induction endgame | `IdealFamily.Ideal.port_nds_nonpos` |
| `WP06-S8` | Local bridge theorem | `localIdealFamily_port_nds_nonpos`, `localIdealFamily_averageRare` |
| `WP06-S9` | Union-closed duality | `localIdealFamily_complement_frankl` |

## Main Checked Statements

```lean
theorem localIdealFamily_port_nds_nonpos
    {F : Family alpha} {U : Finset alpha}
    (h : IsIdealFamilyOn F U) :
    (toPortIdeal F U h).toSetFamily.nds <= 0
```

```lean
theorem localIdealFamily_averageRare
    {F : Family alpha} {U : Finset alpha}
    (h : IsIdealFamilyOn F U) :
    IsAverageRareOn F U
```

```lean
theorem localIdealFamily_complement_frankl
    {F : Family alpha} {U : Finset alpha}
    (h : IsIdealFamilyOn F U) :
    IsFranklAbundant (complementFamilyOn F U)
```

## Spine Position

WP06 does not replace the lattice-minimal-counterexample spine in WP05. It
adds a second checked corridor:

```text
WP02 finite family substrate
  -> WP06 ideal-family bridge
  -> restricted Frankl-facing complement theorem
```

The source-roadmap branch for broader Frankl progress remains open.


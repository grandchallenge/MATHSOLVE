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

## Chaidez v2 node controls

Global spine: `UC-IDEAL-FAMILY-COMPLEMENT-SPINE`. Local node advanced: `WP06-S9`.
The two future-boundary nodes are not prerequisites of the checked restricted result.
The machine-readable companion is `chaidez_v2_conformance.json`.

| node_id | role | status | dependencies | support_route_class | discharge_criterion | proof_debt_ids |
|---|---|---|---|---|---|---|
| WP02-FAMILY | EXTERNAL_DEPENDENCY | CHECKED | none | FORMAL_PROOF | Public finite-family representation; existing local Lean imports compile. | none |
| WP06-S1 | BRIDGE | CHECKED | WP02-FAMILY | FORMAL_PROOF | Carrier, degree, and NDS equivalences checked. | WP06-PD-003 |
| WP06-S2 | LEMMA | CHECKED | WP06-S1 | FORMAL_PROOF | localIdealFamily_exists_rare checked under the local ideal hypotheses. | none |
| WP06-S3 | OBSTRUCTION | CHECKED | WP02-FAMILY | FORMAL_PROOF | Rare-vertex existence is separated from the frequency-sum average inequality. | none |
| WP06-S4 | LEMMA | CHECKED | WP06-S1 | FORMAL_PROOF | Normalized-degree sum and finite support lemmas checked. | none |
| WP06-S5 | LEMMA | CHECKED | WP06-S4 | FORMAL_PROOF | Trace and contraction preserve the stated ideal hypotheses on smaller ground. | none |
| WP06-S6 | LEMMA | CHECKED | WP06-S5 | FORMAL_PROOF | Exact trace-difference identity checked. | none |
| WP06-S7 | THEOREM | CHECKED | WP06-S6, WP06-S4 | FORMAL_PROOF | Trace/contraction induction proves port_nds_nonpos. | WP06-PD-004 |
| WP06-S8 | BRIDGE | CHECKED | WP06-S7, WP06-S1 | FORMAL_PROOF | localIdealFamily_averageRare follows under IsIdealFamilyOn. | WP06-PD-002 |
| WP06-S9 | THEOREM | CHECKED | WP06-S8, WP06-S2 | FORMAL_PROOF | localIdealFamily_complement_frankl checked for complement families only. | WP06-PD-005 |
| WP06-FUTURE-CLASS | BRIDGE | OPEN | WP06-S9 | FORMAL_PROOF | Separately prove the target class has an ideal-complement representation. | WP06-PD-006 |
| WP06-UPSTREAM-REUSE | EXTERNAL_DEPENDENCY | OPEN | none | FORMAL_PROOF | A newer exact upstream source must be audited and replayed before trusted reuse. | WP06-PD-001, WP06-PD-007 |


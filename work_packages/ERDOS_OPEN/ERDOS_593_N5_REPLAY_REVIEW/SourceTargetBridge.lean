import ProtectedInterface
import StatementFidelityAudit

open Cardinal
namespace GCLSourceTargetBridge
open Erdos593

def toSource {V : Type} (H : ProtectedSnapshot.ThreeUniformHypergraph V) : Hypergraph V :=
  ⟨{s | ∃ e ∈ H.edges, (↑e : Set V) = s}⟩

def finiteSnapshot (F : FTS) : ProtectedSnapshot.ThreeUniformHypergraph F.V :=
  ⟨{e | e ∈ F.edges}, F.card3⟩

theorem snapshot_ext {V : Type} {F G : ProtectedSnapshot.ThreeUniformHypergraph V}
    (he : F.edges = G.edges) : F = G := by
  cases F
  cases G
  cases he
  rfl

noncomputable def sourceFinite {V : Type} [Fintype V]
    (F : ProtectedSnapshot.ThreeUniformHypergraph V) : FTS where
  V := V
  decV := Classical.decEq V
  edges := (Set.toFinite F.edges).toFinset
  card3 := by
    classical
    intro e he
    exact F.uniform e (by simpa using he)

theorem finite_roundtrip {V : Type} [Fintype V]
    (F : ProtectedSnapshot.ThreeUniformHypergraph V) :
    finiteSnapshot (sourceFinite F) = F := by
  classical
  apply snapshot_ext
  ext e
  simp [finiteSnapshot, sourceFinite]
  rfl

def hostSnapshot {V : Type} (H : Hypergraph V) (htri : H.IsTripleSystem) :
    ProtectedSnapshot.ThreeUniformHypergraph V where
  edges := {e | (↑e : Set V) ∈ H.edges}
  uniform := by
    intro e he
    simpa using htri (↑e : Set V) he

theorem toSource_triples {V : Type} (H : ProtectedSnapshot.ThreeUniformHypergraph V) :
    (toSource H).IsTripleSystem := by
  rintro s ⟨e, he, rfl⟩
  simpa using H.uniform e he

theorem proper_iff {V C : Type} (H : ProtectedSnapshot.ThreeUniformHypergraph V) (c : V → C) :
    (toSource H).ProperColoring c ↔ H.IsProperColoring c := by
  constructor
  · intro h e he
    simpa using h (↑e : Set V) ⟨e, he, rfl⟩
  · rintro h s ⟨e, he, rfl⟩
    simpa using h e he

theorem embeds_iff (F : FTS) {V : Type} [DecidableEq V]
    (H : ProtectedSnapshot.ThreeUniformHypergraph V) :
    F.Embeds (toSource H) ↔ (finiteSnapshot F).Appears H := by
  classical
  constructor
  · rintro ⟨f, hf, h⟩
    refine ⟨f, hf, ?_⟩
    intro e he
    obtain ⟨d, hd, hdf⟩ := h e he
    have hdEq : d = e.image f := by
      apply Finset.coe_injective
      simpa using hdf
    simpa [hdEq] using hd
  · rintro ⟨f, hf, h⟩
    refine ⟨f, hf, ?_⟩
    intro e he
    exact ⟨e.image f, h e he, by simp⟩

theorem host_roundtrip {V : Type} [DecidableEq V] (H : Hypergraph V) (htri : H.IsTripleSystem) :
    toSource (hostSnapshot H htri) = H := by
  have he : (toSource (hostSnapshot H htri)).edges = H.edges := by
    ext s
    constructor
    · rintro ⟨e, he, rfl⟩
      exact he
    · intro hs
      obtain ⟨a, b, c, hab, hac, hbc, rfl⟩ := Set.ncard_eq_three.mp (htri s hs)
      refine ⟨{a, b, c}, ?_, ?_⟩
      · change (↑({a, b, c} : Finset V) : Set V) ∈ H.edges
        simpa using hs
      · simp
  exact congrArg (fun s : Set (Set V) => (⟨s⟩ : Hypergraph V)) he

theorem colorable_iff {V : Type} (H : ProtectedSnapshot.ThreeUniformHypergraph V) (k : Cardinal) :
    (toSource H).ColorableBy k ↔
      ∃ C : Type, #C = k ∧ ∃ c : V → C, H.IsProperColoring c := by
  constructor
  · rintro ⟨c, hc⟩
    exact ⟨k.out, Cardinal.mk_out k, c, (proper_iff H c).mp hc⟩
  · rintro ⟨C, hk, c, hc⟩
    obtain ⟨e⟩ := Cardinal.eq.mp (hk.trans (Cardinal.mk_out k).symm)
    refine ⟨e ∘ c, (proper_iff H _).mpr ?_⟩
    intro edge hedge
    obtain ⟨a, ha, b, hb, hab⟩ := hc edge hedge
    exact ⟨a, ha, b, hb, fun h => hab (e.injective h)⟩

theorem palette_mono {V : Type} (H : Hypergraph V) {k l : Cardinal} (hkl : k ≤ l)
    (hc : H.ColorableBy k) : H.ColorableBy l := by
  obtain ⟨f, hf⟩ := (Cardinal.le_def k.out l.out).mp (by simpa using hkl)
  obtain ⟨c, hcol⟩ := hc
  refine ⟨f ∘ c, ?_⟩
  intro edge hedge
  obtain ⟨a, ha, b, hb, hab⟩ := hcol edge hedge
  exact ⟨a, ha, b, hb, fun h => hab (hf h)⟩

theorem uncountable_iff {V : Type} (H : ProtectedSnapshot.ThreeUniformHypergraph V) :
    (toSource H).UncountablyChromatic ↔ ℵ₀ < H.chromaticCardinal := by
  classical
  let palettes : Set Cardinal := {k | ∃ C : Type, #C = k ∧ ∃ c : V → C, H.IsProperColoring c}
  have hne : palettes.Nonempty := by
    refine ⟨#V, V, rfl, id, ?_⟩
    intro e he
    obtain ⟨a, ha, b, hb, hab⟩ := Finset.one_lt_card.mp (show 1 < e.card by rw [H.uniform e he]; decide)
    exact ⟨a, ha, b, hb, hab⟩
  have hbdd : BddBelow palettes := ⟨0, fun _ _ => Cardinal.zero_le _⟩
  change ¬ (toSource H).ColorableBy ℵ₀ ↔ ℵ₀ < sInf palettes
  constructor
  · intro hn
    have hsucc : Order.succ (ℵ₀ : Cardinal) ≤ sInf palettes := by
      apply le_csInf hne
      intro k hk
      apply Order.succ_le_of_lt
      by_contra h
      exact hn (palette_mono _ (le_of_not_gt h) ((colorable_iff H k).mpr hk))
    exact lt_of_lt_of_le (Order.lt_succ _) hsucc
  · intro h hc
    exact (not_lt_of_ge (csInf_le hbdd ((colorable_iff H ℵ₀).mp hc))) h

theorem obligatory_iff (F : FTS) :
    ProtectedSnapshot.IsObligatory (finiteSnapshot F) ↔ FTS.Obligatory.{0} F := by
  classical
  constructor
  · intro h V H htri huc
    have hs : ProtectedSnapshot.IsObligatory (finiteSnapshot F) := h
    have hc : ℵ₀ < (hostSnapshot H htri).chromaticCardinal := by
      apply (uncountable_iff _).mp
      simpa [host_roundtrip H htri] using huc
    have hem := (embeds_iff F _).mpr (hs V (hostSnapshot H htri) hc)
    simpa [host_roundtrip H htri] using hem
  · intro h V _ H hc
    exact (embeds_iff F H).mp (h (toSource H) (toSource_triples H) ((uncountable_iff H).mpr hc))

theorem snapshot_classification (F : FTS) :
    ProtectedSnapshot.IsObligatory (finiteSnapshot F) ↔ Bclass F :=
  (obligatory_iff F).trans (obligatory_iff_bclass_unconditional F)

theorem protected_conjectural_sufficient_direction_false :
    ∃ F : FTS, (finiteSnapshot F).IsTwoColorable ∧
      ¬ ProtectedSnapshot.IsObligatory (finiteSnapshot F) := by
  refine ⟨GCLStatementFidelityAudit.overlap, ?_, ?_⟩
  · exact GCLStatementFidelityAudit.overlap_two_colorable
  · intro h
    exact GCLStatementFidelityAudit.overlap_not_obligatory ((obligatory_iff _).mp h)

#print axioms obligatory_iff
#print axioms finite_roundtrip
#print axioms snapshot_classification
#print axioms protected_conjectural_sufficient_direction_false
end GCLSourceTargetBridge

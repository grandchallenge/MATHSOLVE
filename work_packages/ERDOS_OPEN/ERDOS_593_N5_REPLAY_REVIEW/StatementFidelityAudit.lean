import RequestProject.PublicationCertificate

namespace GCLStatementFidelityAudit
open Erdos593

def overlap : FTS where
  V := Fin 4
  edges := {({0, 1, 2} : Finset (Fin 4)), {0, 1, 3}}
  card3 := by
    intro e he
    simp only [Finset.mem_insert, Finset.mem_singleton] at he
    rcases he with rfl | rfl <;> decide

theorem overlap_two_colorable :
    ∃ c : overlap.V → Fin 2,
      ∀ e ∈ overlap.edges, ∃ a ∈ e, ∃ b ∈ e, c a ≠ c b := by
  exact ⟨fun x => if x.val < 2 then 0 else 1, by decide⟩

theorem overlap_not_linear : ¬ overlap.Linear := by
  intro h
  have hbad := h ({0, 1, 2} : Finset (Fin 4)) (by decide)
    ({0, 1, 3} : Finset (Fin 4)) (by decide) (by decide)
  have hcard : (({0, 1, 2} : Finset (Fin 4)) ∩ {0, 1, 3}).card = 2 := by decide
  rw [hcard] at hbad
  omega

theorem overlap_not_bclass : ¬ Bclass overlap := by
  intro h
  exact overlap_not_linear (bclass_intrinsic h).1

theorem overlap_not_obligatory : ¬ FTS.Obligatory.{0} overlap := by
  intro h
  exact overlap_not_bclass ((obligatory_iff_bclass_unconditional overlap).mp h)

-- Source-backed counterexample to the protected Property-B sufficient direction.
-- This theorem's interpretation still requires correspondence of the host interfaces.
#print axioms overlap_not_obligatory
#print axioms overlap_two_colorable

end GCLStatementFidelityAudit

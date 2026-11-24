import PNPAbove.WP37Parity
import Mathlib.Data.Finset.Prod

namespace PNPAbove.WP37
open Finset
open scoped BigOperators
universe u
variable {V : Type u} [DecidableEq V] [Fintype V]

/-- Ordered pairs label independent parallel edges. Diagonal variables
are ignored, which leaves the parity contradiction unchanged. -/
def completeInc (v : V) (e : V × V) : Prop :=
  e.1 ≠ e.2 ∧ (v = e.1 ∨ v = e.2)

instance : DecidableRel (completeInc (V := V)) := fun _ _ => inferInstanceAs (Decidable (_ ∧ _))

theorem complete_edge_pair : EdgePair (completeInc (V := V)) := by
  intro ⟨x,y⟩
  by_cases hxy : x = y
  · exact Or.inl (fun v h => h.1 hxy)
  · exact Or.inr ⟨x,y,hxy,fun v => by simp [completeInc,hxy]⟩

theorem complete_reachable (root r : V) : Reach completeInc root r := by
  by_cases h : root = r
  · subst r
    exact .self
  · exact .step (root,r) .self h (fun v => by simp [completeInc,h])

theorem complete_cross_boundary (S : Finset V) {x y : V} (hx : x ∈ S) (hy : y ∉ S) :
    Boundary completeInc S (x,y) := by
  have hxy : x ≠ y := fun h => hy (h ▸ hx)
  refine ⟨x,hx,⟨hxy,Or.inl rfl⟩,?_⟩
  intro w hw hi
  exact hi.2.elim id (fun h => False.elim (hy (by simpa only [h] using hw)))

theorem complete_boundary_card (S : Finset V) (F : Finset (V × V))
    (hF : ∀ e, Boundary completeInc S e → e ∈ F) :
    S.card * (Fintype.card V - S.card) ≤ F.card := by
  classical
  have hs : S ×ˢ (Finset.univ \ S) ⊆ F := by
    intro e he
    obtain ⟨hx,hy⟩ := Finset.mem_product.mp he
    exact hF e (complete_cross_boundary S hx (Finset.mem_sdiff.mp hy).2)
  have hc := Finset.card_le_card hs
  rw [Finset.card_product,Finset.card_sdiff,Finset.inter_univ,Finset.card_univ] at hc
  exact hc

theorem complete_quadratic_width (root : V) (k : Nat) (hk : 1 ≤ k)
    (hV : 3*k ≤ Fintype.card V) :
    ¬ Derivation (ParityConstraint completeInc (charge root)) (k*k) (fun _ => False) := by
  apply connected_odd_parity_width completeInc root (complete_reachable root) hk (by omega : k < Fintype.card V)
  intro S hl hu F hF
  have hc := complete_boundary_card S F hF
  have hm : k ≤ Fintype.card V - S.card := by omega
  have h1 : (k+1)*k ≤ S.card * (Fintype.card V - S.card) :=
    Nat.mul_le_mul (by omega) hm
  rw [Nat.add_mul,one_mul] at h1
  omega

theorem complete_unsat (root : V) :
    ¬ ∃ a : Assignment (V × V), ∀ v, ParityConstraint completeInc (charge root) v a :=
  odd_charge_unsat completeInc complete_edge_pair _ (charge_total root)

/-- Every proper subsystem is satisfiable, although the full system is not. -/
theorem complete_proper_sat (root : V) (S : Finset V) (h : S.card < Fintype.card V) :
    ∃ a, ∀ v ∈ S, ParityConstraint completeInc (charge root) v a :=
  proper_subsystem_sat completeInc root (complete_reachable root) S h

/-- This family is an explicit semantic counterexample to identifying large
proof-line support with computational intractability: the contradiction
is witnessed by a single additive identity over all equations. -/
theorem complete_parity_obstruction (root : V) (k : Nat) (hk : 1 ≤ k)
    (hV : 3*k ≤ Fintype.card V) :
    (∀ a : Assignment (V × V), ∑ v, parity completeInc a v = 0) ∧
    (∑ v, charge root v = 1) ∧
    (∀ S : Finset V, S.card < Fintype.card V →
      ∃ a, ∀ v ∈ S, ParityConstraint completeInc (charge root) v a) ∧
    ¬ Derivation (ParityConstraint completeInc (charge root)) (k*k) (fun _ => False) :=
  ⟨parity_total_zero completeInc complete_edge_pair,charge_total root,
    complete_proper_sat root,complete_quadratic_width root k hk hV⟩

end PNPAbove.WP37

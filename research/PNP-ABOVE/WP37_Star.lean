import PNPAbove.WP37Complete

namespace PNPAbove.WP37
open Finset
open scoped BigOperators
universe u
variable {V : Type u} [DecidableEq V] [Fintype V]

/-- Explicit witness on a complete graph for arbitrary charges: only
the edges directed out of one fixed root need to be set. -/
def starAssignment (root : V) (c : V → ZMod 2) : Assignment (V × V) :=
  fun e => decide (e.1 = root ∧ e.2 ≠ root ∧ c e.2 = 1)

theorem bit_decide_one : ∀ z : ZMod 2, bit (decide (z = 1)) = z := by
  decide

theorem star_nonroot (root v : V) (c : V → ZMod 2) (hv : v ≠ root) :
    parity completeInc (starAssignment root c) v = c v := by
  classical
  unfold parity
  rw [Fintype.sum_prod_type]
  have hterm : ∀ x y : V,
      (if completeInc v (x,y) then bit (starAssignment root c (x,y)) else 0) =
      (if x = root ∧ y = v then c v else 0) := by
    intro x y
    by_cases hx : x = root
    · subst x
      by_cases hy : y = v
      · subst y
        simp [completeInc,starAssignment,hv,Ne.symm hv,bit_decide_one]
      · by_cases hz : y = root <;> simp [completeInc,hv,Ne.symm hv,hy,Ne.symm hy,hz]
    · simp [starAssignment,hx,bit]
  simp_rw [hterm]
  simp_rw [ite_and]
  simp

theorem star_even_sat (root : V) (c : V → ZMod 2) (hc : ∑ v, c v = 0) :
    ∀ v, ParityConstraint completeInc c v (starAssignment root c) := by
  classical
  intro v
  by_cases hv : v = root
  · subst v
    have htotal := parity_total_zero completeInc complete_edge_pair (starAssignment root c)
    have hh : (∑ x ∈ (Finset.univ : Finset V).erase root,
        parity completeInc (starAssignment root c) x) =
        ∑ x ∈ (Finset.univ : Finset V).erase root, c x := by
      apply Finset.sum_congr rfl
      intro x hx
      exact star_nonroot root x c (Finset.mem_erase.mp hx).1
    have h1 := Finset.sum_erase_add (Finset.univ : Finset V)
      (fun x => parity completeInc (starAssignment root c) x) (Finset.mem_univ root)
    have h2 := Finset.sum_erase_add (Finset.univ : Finset V) c (Finset.mem_univ root)
    rw [htotal,hh] at h1
    rw [hc] at h2
    exact add_left_cancel (h1.trans h2.symm)
  · exact star_nonroot root v c hv

/-- The full varying-charge family has an exact elementary algebraic
decision rule. Its high-width odd instances do not make the family hard
for an unrestricted solver given its incidence/charge representation. -/
theorem complete_sat_iff_even (root : V) (c : V → ZMod 2) :
    (∃ a : Assignment (V × V), ∀ v, ParityConstraint completeInc c v a) ↔
    ∑ v, c v = 0 := by
  constructor
  · rintro ⟨a,ha⟩
    have heq : (∑ v, parity completeInc a v) = ∑ v, c v :=
      Finset.sum_congr rfl (fun v _ => ha v)
    rw [parity_total_zero completeInc complete_edge_pair a] at heq
    exact heq.symm
  · intro hc
    exact ⟨starAssignment root c,star_even_sat root c hc⟩

end PNPAbove.WP37

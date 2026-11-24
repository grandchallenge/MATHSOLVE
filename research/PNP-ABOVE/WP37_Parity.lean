import PNPAbove.WP37Semantic
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

namespace PNPAbove.WP37
set_option linter.unusedSectionVars false
open Finset
open scoped BigOperators
universe u v
variable {V : Type u} {E : Type v} [DecidableEq V] [DecidableEq E]
variable [Fintype V] [Fintype E]

def bit (b : Bool) : ZMod 2 := if b then 1 else 0

theorem bit_not (b : Bool) : bit (!b) = bit b + 1 := by cases b <;> decide

theorem zmod_two_shift : ∀ x y : ZMod 2, x + 1 = y ↔ x ≠ y := by decide

def parity (I : V → E → Prop) [DecidableRel I] (a : Assignment E) (v : V) : ZMod 2 :=
  ∑ e : E, if I v e then bit (a e) else 0

def ParityConstraint (I : V → E → Prop) [DecidableRel I] (c : V → ZMod 2)
    (v : V) (a : Assignment E) : Prop := parity I a v = c v

theorem parity_flip (I : V → E → Prop) [DecidableRel I]
    (a : Assignment E) (v : V) (e : E) :
    parity I (flip a e) v = parity I a v + (if I v e then 1 else 0) := by
  classical
  unfold parity
  calc
    _ = ∑ f : E, ((if I v f then bit (a f) else 0) +
        (if f = e then (if I v e then 1 else 0) else 0)) := by
      apply Finset.sum_congr rfl
      intro f _
      by_cases hf : f = e
      · subst f
        by_cases hi : I v e <;> simp [flip, hi, bit_not]
      · simp [flip, hf]
    _ = _ := by rw [Finset.sum_add_distrib]; simp

theorem parity_flip_law (I : V → E → Prop) [DecidableRel I] (c : V → ZMod 2) :
    FlipLaw I (ParityConstraint I c) := by
  intro v e a
  constructor
  · intro h
    unfold ParityConstraint
    rw [parity_flip, if_pos h]
    exact zmod_two_shift _ _
  · intro h
    unfold ParityConstraint
    rw [parity_flip, if_neg h, add_zero]

/-- The endpoint condition deliberately allows parallel edges; every edge
appears in exactly two distinct equations, or is an unused variable. -/
def EdgePair (I : V → E → Prop) : Prop :=
  ∀ e, (∀ v, ¬ I v e) ∨ ∃ x y : V, x ≠ y ∧ ∀ v, I v e ↔ v = x ∨ v = y

theorem parity_total_zero (I : V → E → Prop) [DecidableRel I]
    (hI : EdgePair I) (a : Assignment E) :
    ∑ v : V, parity I a v = 0 := by
  classical
  unfold parity
  rw [Finset.sum_comm]
  apply Finset.sum_eq_zero
  intro e _
  rcases hI e with hz | ⟨x,y,hxy,hI⟩
  · simp [hz]
  · have hsum : (∑ v : V, if I v e then bit (a e) else 0) =
        ∑ v : V, ((if v = x then bit (a e) else 0) +
          (if v = y then bit (a e) else 0)) := by
      apply Finset.sum_congr rfl
      intro v _
      by_cases hx : v = x
      · subst v
        simp [hI,hxy]
      · by_cases hy : v = y
        · subst v
          simp [hI,hx]
        · simp [hI,hx,hy]
    rw [hsum, Finset.sum_add_distrib]
    simp
    cases a e <;> decide

theorem odd_charge_unsat (I : V → E → Prop) [DecidableRel I]
    (hI : EdgePair I) (c : V → ZMod 2) (hc : ∑ v, c v = 1) :
    ¬ ∃ a : Assignment E, ∀ v, ParityConstraint I c v a := by
  rintro ⟨a,ha⟩
  have heq : (∑ v, parity I a v) = ∑ v, c v :=
    Finset.sum_congr rfl (fun v _ => ha v)
  rw [parity_total_zero I hI a,hc] at heq
  exact (by decide : (0 : ZMod 2) ≠ 1) heq

def charge (root : V) (v : V) : ZMod 2 := if v = root then 1 else 0

theorem charge_total (root : V) : ∑ v, charge root v = 1 := by
  classical
  simp [charge]

def Defect (I : V → E → Prop) [DecidableRel I] (c : V → ZMod 2) (r : V)
    (a : Assignment E) : Prop :=
  ∀ v, ParityConstraint I c v a ↔ v ≠ r

theorem zero_single_defect (I : V → E → Prop) [DecidableRel I] (root : V) :
    Defect I (charge root) root (fun _ => false) := by
  classical
  intro v
  unfold ParityConstraint parity charge
  simp [bit]

theorem transport_defect (I : V → E → Prop) [DecidableRel I] (c : V → ZMod 2)
    {x y : V} {e : E} (hxy : x ≠ y)
    (hI : ∀ v, I v e ↔ v = x ∨ v = y) {a : Assignment E}
    (ha : Defect I c x a) : Defect I c y (flip a e) := by
  intro v
  by_cases hx : v = x
  · subst v
    rw [(parity_flip_law I c x e a).1 ((hI x).2 (Or.inl rfl)),ha x]
    simp [hxy]
  · by_cases hy : v = y
    · subst v
      rw [(parity_flip_law I c y e a).1 ((hI y).2 (Or.inr rfl)),ha y]
      simp [hx]
    · rw [(parity_flip_law I c v e a).2 (fun h => (hI v).1 h |>.elim hx hy),ha v]
      simp [hx,hy]

inductive Reach (I : V → E → Prop) (root : V) : V → Prop
  | self : Reach I root root
  | step {x y : V} (e : E) : Reach I root x → x ≠ y →
      (∀ v, I v e ↔ v = x ∨ v = y) → Reach I root y

theorem defect_at_reachable (I : V → E → Prop) [DecidableRel I] (root r : V)
    (h : Reach I root r) : ∃ a, Defect I (charge root) r a := by
  induction h with
  | self => exact ⟨fun _ => false, zero_single_defect I root⟩
  | step e _ hxy hI ih =>
    obtain ⟨a,ha⟩ := ih
    exact ⟨flip a e, transport_defect I _ hxy hI ha⟩

theorem proper_subsystem_sat (I : V → E → Prop) [DecidableRel I]
    (root : V) (hconn : ∀ r, Reach I root r)
    (S : Finset V) (hS : S.card < Fintype.card V) :
    ∃ a, ∀ v ∈ S, ParityConstraint I (charge root) v a := by
  classical
  have hn : S ≠ Finset.univ := by intro h; rw [h,Finset.card_univ] at hS; omega
  have hmiss : ∃ r : V, r ∉ S := by
    by_contra h
    apply hn
    exact Finset.eq_univ_of_forall fun r => by
      by_contra hr
      exact h ⟨r,hr⟩
  obtain ⟨r,hr⟩ := hmiss
  obtain ⟨a,ha⟩ := defect_at_reachable I root r (hconn r)
  exact ⟨a,fun v hv => (ha v).2 (fun h => hr (h ▸ hv))⟩

theorem connected_odd_parity_width (I : V → E → Prop) [DecidableRel I]
    (root : V) (hconn : ∀ r, Reach I root r) {k w : Nat}
    (hk : 1 ≤ k) (hcard : k < Fintype.card V)
    (hexp : ∀ S : Finset V, k < S.card → S.card ≤ 2*k →
      ∀ F : Finset E, (∀ e, Boundary I S e → e ∈ F) → w < F.card) :
    ¬ Derivation (ParityConstraint I (charge root)) w (fun _ => False) := by
  exact no_narrow_semantic_refutation hk (flip_implies_repair (parity_flip_law I (charge root)))
    (fun S hs => proper_subsystem_sat I root hconn S (lt_of_le_of_lt hs hcard)) hexp

end PNPAbove.WP37

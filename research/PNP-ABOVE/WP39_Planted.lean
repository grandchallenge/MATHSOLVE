import PNPAbove.WP37Complete
import Mathlib.Data.Finset.Option

namespace PNPAbove.WP39
open WP37
universe u v
variable {V : Type u} {E : Type v} [DecidableEq V] [DecidableEq E]
set_option linter.unusedSectionVars false

def liftAssignment (b : Bool) (a : Assignment E) : Assignment (Option E)
  | none => b
  | some e => a e

def restrictAssignment (a : Assignment (Option E)) : Assignment E :=
  fun e => a (some e)

/-- On the false branch the original constraints remain; on the true
branch every variable is pinned to the explicitly supplied assignment.
The optional final constraint selects the false branch when requested. -/
def planted (P : V → Predicate E) (p : Assignment E) (pinFalse : Bool) :
    Option (Sum V E) → Predicate (Option E)
  | none, a => pinFalse = true → a none = false
  | some (.inl v), a => a none = true ∨ P v (restrictAssignment a)
  | some (.inr e), a => a none = false ∨ a (some e) = p e

theorem lift_restrict (b : Bool) (a : Assignment E) :
    restrictAssignment (liftAssignment b a) = a := rfl

theorem planted_true_model (P : V → Predicate E) (p : Assignment E) :
    ∀ c, planted P p false c (liftAssignment true p) := by
  intro c
  cases c with
  | none => simp [planted]
  | some c => cases c <;> simp [planted,liftAssignment]

theorem planted_model_iff (P : V → Predicate E) (p : Assignment E)
    (hP : ¬ ∃ a, ∀ v, P v a) (a : Assignment (Option E)) :
    (∀ c, planted P p false c a) ↔ a = liftAssignment true p := by
  constructor
  · intro h
    have hb : a none = true := by
      cases h0 : a none with
      | true => rfl
      | false =>
        exfalso
        apply hP
        refine ⟨restrictAssignment a,fun v => ?_⟩
        exact (h (some (.inl v))).resolve_left (by simp [h0])
    funext e
    cases e with
    | none => exact hb
    | some e => exact (h (some (.inr e))).resolve_left (by simp [hb])
  · rintro rfl
    exact planted_true_model P p

theorem planted_false_unsat (P : V → Predicate E) (p : Assignment E)
    (hP : ¬ ∃ a, ∀ v, P v a) :
    ¬ ∃ a, ∀ c, planted P p true c a := by
  rintro ⟨a,h⟩
  apply hP
  have hb : a none = false := h none rfl
  exact ⟨restrictAssignment a,fun v => (h (some (.inl v))).resolve_left (by simp [hb])⟩

theorem restrict_support (Q : Predicate (Option E)) (F : Finset (Option E))
    (h : Depends Q F) :
    Depends (fun a => Q (liftAssignment false a)) (Finset.eraseNone F) := by
  intro a b hab
  apply h
  intro e he
  cases e with
  | none => rfl
  | some e => exact hab e (Finset.mem_eraseNone.mpr he)

theorem planted_derivation_restrict (P : V → Predicate E) (p : Assignment E)
    (v0 : V) (pinFalse : Bool) (w : Nat) (Q : Predicate (Option E))
    (h : Derivation (planted P p pinFalse) w Q) :
    Derivation P w (fun a => Q (liftAssignment false a)) := by
  induction h with
  | initial c Q F hd hw h =>
    have hs := restrict_support Q F hd
    have hb := le_trans (Finset.card_eraseNone_le F) hw
    cases c with
    | none =>
      exact .initial v0 _ _ hs hb (fun a _ => h _ (by simp [planted,liftAssignment]))
    | some c =>
      cases c with
      | inl v =>
        exact .initial v _ _ hs hb (fun a ha => h _ (Or.inr ha))
      | inr e =>
        exact .initial v0 _ _ hs hb (fun a _ => h _ (Or.inl rfl))
  | @combine Q R U F hQ hR hd hw h ihQ ihR =>
    exact .combine _ ihQ ihR (restrict_support U F hd)
      (le_trans (Finset.card_eraseNone_le F) hw) (fun a => h (liftAssignment false a))

theorem planted_forced_selector_width (P : V → Predicate E) (p : Assignment E)
    (v0 : V) (w : Nat) (hW : ¬ Derivation P w (fun _ => False)) :
    ¬ Derivation (planted P p false) w (fun a => a none = true) := by
  intro h
  have hr := planted_derivation_restrict P p v0 false w _ h
  have he : (fun a : Assignment E => liftAssignment false a none = true) = (fun _ => False) := by
    funext a
    simp [liftAssignment]
  rw [he] at hr
  exact hW hr

theorem planted_wrong_branch_width (P : V → Predicate E) (p : Assignment E)
    (v0 : V) (w : Nat) (hW : ¬ Derivation P w (fun _ => False)) :
    ¬ Derivation (planted P p true) w (fun _ => False) := by
  intro h
  exact hW (planted_derivation_restrict P p v0 true w _ h)

/-- The planted pin constraint is not affine: toggling the selector
sometimes changes truth, sometimes preserves truth. -/
theorem planted_not_flipLaw (P : V → Predicate E) (p : Assignment E) (e : E) :
    ¬ ∃ I : Option (Sum V E) → Option E → Prop,
      FlipLaw I (planted P p false) := by
  rintro ⟨I,hI⟩
  let c : Option (Sum V E) := some (.inr e)
  have hgood := hI c none (liftAssignment false p)
  have hbad := hI c none (liftAssignment false (WP37.flip p e))
  by_cases hi : I c none
  · have hh := hgood.1 hi
    simp [c,planted,liftAssignment,WP37.flip] at hh
  · have hh := hbad.2 hi
    simp [c,planted,liftAssignment,WP37.flip] at hh

def plantedInc (I : V → E → Prop) (pinFalse : Bool) :
    Option (Sum V E) → Option E → Prop
  | none, none => pinFalse = true
  | none, some _ => False
  | some (.inl _), none => True
  | some (.inl v), some e => I v e
  | some (.inr _), none => True
  | some (.inr f), some e => e = f

theorem restrict_flip_none (a : Assignment (Option E)) :
    restrictAssignment (WP37.flip a none) = restrictAssignment a := by
  funext e
  simp [restrictAssignment,WP37.flip]

theorem restrict_flip_some (a : Assignment (Option E)) (e : E) :
    restrictAssignment (WP37.flip a (some e)) = WP37.flip (restrictAssignment a) e := by
  funext f
  simp [restrictAssignment,WP37.flip]

/-- The weaker one-way repair property survives gating and planting. -/
theorem planted_repairLaw (I : V → E → Prop) (P : V → Predicate E)
    (hP : RepairLaw I P) (p : Assignment E) (pinFalse : Bool) :
    RepairLaw (plantedInc I pinFalse) (planted P p pinFalse) := by
  intro c e a
  cases c with
  | none =>
    cases e with
    | none =>
      cases pinFalse <;> cases h : a none <;>
        simp [plantedInc,planted,WP37.flip,h]
    | some e => simp [plantedInc,planted,WP37.flip]
  | some c =>
    cases c with
    | inl v =>
      cases e with
      | none =>
        simp only [plantedInc,planted,restrict_flip_none]
        cases h : a none <;> simp [WP37.flip,h]
      | some e =>
        have hp := hP v e (restrictAssignment a)
        simp only [plantedInc,planted,restrict_flip_some]
        have hsel : WP37.flip a (some e) none = a none := by simp [WP37.flip]
        rw [hsel]
        constructor
        · intro hi hn
          exact Or.inr (hp.1 hi (fun h => hn (Or.inr h)))
        · intro hi
          rw [hp.2 hi]
    | inr f =>
      cases e with
      | none =>
        cases h : a none <;> simp [plantedInc,planted,WP37.flip,h]
      | some e =>
        by_cases h : e = f
        · subst e
          cases ha : a none <;> cases hb : a (some f) <;> cases hc : p f <;>
            simp [plantedInc,planted,WP37.flip,ha,hb,hc]
        · simp [plantedInc,planted,WP37.flip,h,Ne.symm h]

variable [Fintype V]

theorem complete_planted_unique (root : V) (p : Assignment (V × V)) :
    ∀ a, (∀ c, planted (ParityConstraint completeInc (charge root)) p false c a)
      ↔ a = liftAssignment true p :=
  planted_model_iff _ p (complete_unsat root)

theorem complete_planted_width (root : V) (p : Assignment (V × V)) (k : Nat)
    (hk : 1 ≤ k) (hN : 3*k ≤ Fintype.card V) :
    (¬ Derivation (planted (ParityConstraint completeInc (charge root)) p false)
        (k*k) (fun a => a none = true)) ∧
    (¬ Derivation (planted (ParityConstraint completeInc (charge root)) p true)
        (k*k) (fun _ => False)) :=
  ⟨planted_forced_selector_width _ p root _ (complete_quadratic_width root k hk hN),
   planted_wrong_branch_width _ p root _ (complete_quadratic_width root k hk hN)⟩

end PNPAbove.WP39

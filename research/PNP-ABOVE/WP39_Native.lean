import PNPAbove.WP39Planted
import PNPAbove.WP37Transfer
import MIPRE.Foundations.SAT.Rename

namespace PNPAbove.WP39
open WP37 MIPRE MIPRE.SAT MIPRE.Cost
abbrev Edges (q : Nat) := Fin (2^q) × Fin (2^q)
abbrev Constraints (q : Nat) := Option (Sum (Fin (2^q)) (Edges q))

def index {q : Nat} : Option (Edges q) → Nat
  | none => 0
  | some e => edgeIndex e + 1

theorem index_injective (q : Nat) : Function.Injective (@index q) := by
  intro e f h
  cases e <;> cases f
  · rfl
  · simp [index] at h
  · simp [index] at h
  · congr 1
    apply edgeIndex_injective (2^q)
    simpa [index] using h

def readNative (q : Nat) (a : Assignment Nat) : Assignment (Option (Edges q)) :=
  fun e => a (index e)

noncomputable def writeNative (q : Nat) (a : Assignment (Option (Edges q))) : Assignment Nat :=
  fun i => if h : ∃ e : Option (Edges q), index e = i then a (Classical.choose h) else false

theorem read_write (q : Nat) (a : Assignment (Option (Edges q))) :
    readNative q (writeNative q a) = a := by
  classical
  funext e
  have h : ∃ f : Option (Edges q), index f = index e := ⟨e,rfl⟩
  have he := index_injective q (Classical.choose_spec h)
  simp [readNative,writeNative,h,he]

def nativeConstraint (q : Nat) (root : Fin (2^q)) (pinFalse : Bool) :
    Constraints q → Fml
  | none => if pinFalse then .not (.inp 0) else .const true
  | some (.inl v) => .or (.inp 0) ((WP37.nativeConstraint q root v).rename Nat.succ)
  | some (.inr e) => .or (.not (.inp 0)) (.not (.inp (index (some e))))

theorem nativeConstraint_eval (q : Nat) (root : Fin (2^q)) (pinFalse : Bool)
    (c : Constraints q) (a : Assignment Nat) :
    (nativeConstraint q root pinFalse c).eval a = true ↔
      planted (ParityConstraint completeInc (charge root)) (fun _ => false)
        pinFalse c (readNative q a) := by
  cases c with
  | none =>
    cases pinFalse <;> simp [nativeConstraint,planted,readNative,index,Fml.eval]
  | some c =>
    cases c with
    | inl v =>
      simp only [nativeConstraint,Fml.eval,Bool.or_eq_true,Fml.eval_rename,planted,
        readNative,index]
      rw [WP37.nativeConstraint_eval]
      rfl
    | inr e =>
      simp [nativeConstraint,Fml.eval,planted,readNative,index]

def nativeFormula (q : Nat) (root : Fin (2^q)) (pinFalse : Bool)
    (cs : List (Constraints q)) : Fml :=
  cs.foldr (fun c f => .and (nativeConstraint q root pinFalse c) f) (.const true)

theorem nativeFormula_eval (q : Nat) (root : Fin (2^q)) (pinFalse : Bool)
    (cs : List (Constraints q)) (a : Assignment Nat) :
    (nativeFormula q root pinFalse cs).eval a = true ↔
      ∀ c ∈ cs, planted (ParityConstraint completeInc (charge root)) (fun _ => false)
        pinFalse c (readNative q a) := by
  induction cs with
  | nil => simp [nativeFormula,Fml.eval]
  | cons c cs ih =>
    change ((nativeConstraint q root pinFalse c).eval a &&
      (nativeFormula q root pinFalse cs).eval a) = true ↔ _
    simp [Bool.and_eq_true,nativeConstraint_eval,ih]

def plantedBits : Assignment Nat := fun i => decide (i = 0)

theorem read_plantedBits (q : Nat) :
    readNative q plantedBits = liftAssignment true (fun _ => false) := by
  funext e
  cases e <;> simp [readNative,plantedBits,index,liftAssignment]

theorem native_plantedBits_satisfies (q : Nat) (root : Fin (2^q))
    (cs : List (Constraints q)) :
    (nativeFormula q root false cs).eval plantedBits = true := by
  rw [nativeFormula_eval,read_plantedBits]
  exact fun c _ => planted_true_model _ _ c

noncomputable def fullNative (q : Nat) (root : Fin (2^q)) (pinFalse : Bool) : Fml :=
  nativeFormula q root pinFalse Finset.univ.toList

theorem fullNative_model_iff (q : Nat) (root : Fin (2^q)) (a : Assignment Nat) :
    (fullNative q root false).eval a = true ↔
      readNative q a = readNative q plantedBits := by
  rw [fullNative,nativeFormula_eval,read_plantedBits]
  simpa using complete_planted_unique root (fun _ => false) (readNative q a)

theorem fullNative_satisfies (q : Nat) (root : Fin (2^q)) :
    (fullNative q root false).eval plantedBits = true :=
  native_plantedBits_satisfies q root _

theorem fullNative_wrong_branch_unsat (q : Nat) (root : Fin (2^q)) :
    ¬ ∃ a : Assignment Nat, (fullNative q root true).eval a = true := by
  rintro ⟨a,ha⟩
  apply planted_false_unsat (ParityConstraint completeInc (charge root)) (fun _ => false)
    (complete_unsat root)
  refine ⟨readNative q a,?_⟩
  have h := (nativeFormula_eval q root true _ a).1 ha
  exact fun c => h c (by simp)

def supportPreimage (q : Nat) (F : Finset Nat) : Finset (Option (Edges q)) :=
  Finset.univ.filter fun e => index e ∈ F

theorem supportPreimage_card (q : Nat) (F : Finset Nat) :
    (supportPreimage q F).card ≤ F.card := by
  classical
  have hh : (supportPreimage q F).image index ⊆ F := by
    intro x hx
    obtain ⟨e,he,rfl⟩ := Finset.mem_image.mp hx
    exact (Finset.mem_filter.mp he).2
  rw [← Finset.card_image_of_injective (supportPreimage q F) (index_injective q)]
  exact Finset.card_le_card hh

theorem writeNative_support (q : Nat) (Q : Predicate Nat) (F : Finset Nat)
    (h : Depends Q F) :
    Depends (fun a => Q (writeNative q a)) (supportPreimage q F) := by
  classical
  intro a b hab
  apply h
  intro i hi
  unfold writeNative
  split
  · rename_i he
    exact hab _ (by simp [supportPreimage,Classical.choose_spec he,hi])
  · rfl

theorem native_derivation_pullback (q : Nat) (P : Constraints q → Predicate Nat)
    (w : Nat) (Q : Predicate Nat) (h : Derivation P w Q) :
    Derivation (fun c a => P c (writeNative q a)) w (fun a => Q (writeNative q a)) := by
  induction h with
  | initial c Q F hd hw h =>
    exact .initial c _ _ (writeNative_support q Q F hd)
      (le_trans (supportPreimage_card q F) hw) (fun a => h (writeNative q a))
  | @combine Q R U F hQ hR hd hw h ihQ ihR =>
    exact .combine _ ihQ ihR (writeNative_support q U F hd)
      (le_trans (supportPreimage_card q F) hw) (fun a => h (writeNative q a))

theorem native_pullback_constraints (q : Nat) (root : Fin (2^q)) (pinFalse : Bool) :
    (fun c a => (nativeConstraint q root pinFalse c).eval (writeNative q a) = true) =
      planted (ParityConstraint completeInc (charge root)) (fun _ => false) pinFalse := by
  funext c a
  apply propext
  rw [nativeConstraint_eval,read_write]

theorem native_wrong_branch_width (q : Nat) (root : Fin (2^q)) (k : Nat)
    (hk : 1 ≤ k) (hN : 3*k ≤ 2^q) :
    ¬ Derivation (fun c a => (nativeConstraint q root true c).eval a = true)
        (k*k) (fun _ => False) := by
  intro h
  have hp := native_derivation_pullback q _ _ _ h
  rw [native_pullback_constraints] at hp
  exact (complete_planted_width root (fun _ => false) k hk (by simpa using hN)).2 hp

theorem native_forced_selector_width (q : Nat) (root : Fin (2^q)) (k : Nat)
    (hk : 1 ≤ k) (hN : 3*k ≤ 2^q) :
    ¬ Derivation (fun c a => (nativeConstraint q root false c).eval a = true)
        (k*k) (fun a => a 0 = true) := by
  intro h
  have hp := native_derivation_pullback q _ _ _ h
  rw [native_pullback_constraints] at hp
  have he : (fun a : Assignment (Option (Edges q)) => writeNative q a 0 = true) =
      (fun a => a none = true) := by
    funext a
    have hr := congrFun (read_write q a) none
    exact congrArg (fun b : Bool => b = true) hr
  rw [he] at hp
  exact (complete_planted_width root (fun _ => false) k hk (by simpa using hN)).1 hp

end PNPAbove.WP39

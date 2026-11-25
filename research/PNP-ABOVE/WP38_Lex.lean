import PNPAbove.WP38Greedy

namespace PNPAbove.WP38
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun

def choices (D : PolyTimeFun Data Bool) : List Nat → Fml → BitStr
  | [], _ => []
  | i::xs, f =>
    let b := choose D f i
    b :: choices D xs (.and f (lit i b))

theorem choices_fold (D : PolyTimeFun Data Bool) (xs : List Nat) (s : State) :
    (xs.foldl (step D) s).2.reverse = s.2.reverse ++ choices D xs s.1 := by
  induction xs generalizing s with
  | nil => simp [choices]
  | cons i xs ih =>
    rw [List.foldl_cons,ih]
    simp [step,choices,List.reverse_cons,List.append_assoc]

theorem search_choices (D : PolyTimeFun Data Bool) (xs : List Nat) (f : Fml) :
    searchP D (xs,f) = choices D xs f := by
  rw [searchP_correct,run,choices_fold]
  rfl

/-- Weak descending lexicographic preference on finite bit strings.
true is preferred to false; unequal lengths need not be comparable. -/
inductive Preferred : BitStr → BitStr → Prop
  | nil : Preferred [] []
  | strict (xs ys : BitStr) : Preferred (true::xs) (false::ys)
  | tail (b : Bool) {xs ys : BitStr} : Preferred xs ys → Preferred (b::xs) (b::ys)

theorem preferred_refl (xs : BitStr) : Preferred xs xs := by
  induction xs with
  | nil => exact .nil
  | cons x xs ih => exact .tail x ih

theorem preferred_antisymm {xs ys : BitStr} (h : Preferred xs ys)
    (h' : Preferred ys xs) : xs = ys := by
  induction h with
  | nil => rfl
  | strict xs ys => cases h'
  | tail b h ih =>
    cases h' with
    | tail _ h' => exact congrArg (List.cons b) (ih h')

/-- Every model is lexicographically dominated by greedy choices. The
proof uses satisfiability only at a feasible prefix. -/
theorem choices_preferred (D : PolyTimeFun Data Bool)
    (hD : Correct D) (xs : List Nat) (f : Fml)
    (a : Nat → Bool) (ha : f.eval a = true) :
    Preferred (choices D xs f) (xs.map a) := by
  induction xs generalizing f with
  | nil => exact .nil
  | cons i xs ih =>
    change Preferred (choose D f i :: choices D xs (.and f (lit i (choose D f i))))
      (a i :: xs.map a)
    cases hb : choose D f i <;> cases hi : a i
    · exact .tail false (ih _ ((pin_eval _ _ _ _).mpr ⟨ha,hi⟩))
    · have hs : Sat (.and f (.inp i)) := ⟨a,by simp [Fml.eval,ha,hi]⟩
      have ht := (hD _).mpr hs
      exact False.elim (Bool.noConfusion (hb.symm.trans ht))
    · exact .strict _ _
    · exact .tail true (ih _ ((pin_eval _ _ _ _).mpr ⟨ha,hi⟩))

theorem search_preferred (D : PolyTimeFun Data Bool)
    (hD : Correct D) (xs : List Nat) (f : Fml) (a : Nat → Bool)
    (ha : f.eval a = true) :
    Preferred (searchP D (xs,f)) (xs.map a) := by
  rw [search_choices]
  exact choices_preferred D hD _ _ _ ha

def CanonicalWitness (xs : List Nat) (f : Fml) (bs : BitStr) : Prop :=
  (∃ a : Nat → Bool, f.eval a = true ∧ bs = xs.map a) ∧
  ∀ a : Nat → Bool, f.eval a = true → Preferred bs (xs.map a)

theorem canonical_unique (xs : List Nat) (f : Fml) {bs cs : BitStr}
    (hb : CanonicalWitness xs f bs) (hc : CanonicalWitness xs f cs) : bs = cs := by
  obtain ⟨a,ha,he⟩ := hb.1
  obtain ⟨b,hb',he'⟩ := hc.1
  apply preferred_antisymm
  · rw [he']
    exact hb.2 b hb'
  · rw [he]
    exact hc.2 a ha

theorem search_canonical (D : PolyTimeFun Data Bool)
    (hD : Correct D) (xs : List Nat) (f : Fml) (hf : Sat f) :
    CanonicalWitness xs f (searchP D (xs,f)) :=
  ⟨search_model D hD xs f hf,search_preferred D hD xs f⟩

end PNPAbove.WP38

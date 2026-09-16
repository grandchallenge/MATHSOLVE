import MathSolve.RSICCC.Stage

/-!
# RSI-CCC M1: direct Cartesian-closed structure

This file develops the Kripke exponential for the direct stage-indexed model.
The construction is intentionally explicit: an element of `B^A` at stage `n`
is a coherent family of maps at every stage `m ≤ n`.
-/

namespace MathSolve.RSICCC

universe u

/-- Restrict a stage value along an arbitrary proof `m ≤ n`. -/
def restrictLE (A : StageObj.{u}) {m n : Nat} (h : m ≤ n) : A.carrier n → A.carrier m :=
  match h with
  | .refl => fun x => x
  | .step h' => fun x => restrictLE A h' (A.restrict _ x)

@[simp] theorem restrictLE_refl (A : StageObj.{u}) (n : Nat) (x : A.carrier n) :
    restrictLE A (Nat.le_refl n) x = x := rfl

@[simp] theorem restrictLE_succ (A : StageObj.{u}) (n : Nat) (x : A.carrier (n + 1)) :
    restrictLE A (Nat.le_succ n) x = A.restrict n x := rfl

/-- Restriction along inequalities composes. -/
theorem restrictLE_trans (A : StageObj.{u}) {l m n : Nat}
    (h₁ : l ≤ m) (h₂ : m ≤ n) (x : A.carrier n) :
    restrictLE A h₁ (restrictLE A h₂ x) = restrictLE A (h₁.trans h₂) x := by
  induction h₂ with
  | refl => rfl
  | @step n h₂ ih =>
      simpa [restrictLE] using ih (A.restrict n x)

/-- One-step restriction after an arbitrary restriction path is the same as
the composite path. -/
theorem restrict_restrictLE (A : StageObj.{u}) {m n : Nat}
    (h : m + 1 ≤ n) (x : A.carrier n) :
    A.restrict m (restrictLE A h x) =
      restrictLE A ((Nat.le_succ m).trans h) x := by
  simpa using restrictLE_trans A (Nat.le_succ m) h x

/-- A coherent Kripke family representing an exponential element at stage `n`. -/
structure ExpCarrier (A B : StageObj.{u}) (n : Nat) where
  map : (m : Nat) → m ≤ n → A.carrier m → B.carrier m
  natural : ∀ m (h : m + 1 ≤ n) x,
    B.restrict m (map (m + 1) h x) =
      map m ((Nat.le_succ m).trans h) (A.restrict m x)

/-- Equality of exponential elements is determined by their stage maps;
naturality witnesses are propositions and hence proof-irrelevant. -/
@[ext] theorem ExpCarrier.ext {A B : StageObj.{u}} {n : Nat}
    {f g : ExpCarrier A B n}
    (h : ∀ m (hm : m ≤ n) a, f.map m hm a = g.map m hm a) : f = g := by
  cases f with
  | mk fmap fnat =>
      cases g with
      | mk gmap gnat =>
          have hm : fmap = gmap := by
            funext m hm a
            exact h m hm a
          cases hm
          rfl

/-- Forget the top stage of a Kripke exponential element. -/
def expRestrict (A B : StageObj.{u}) (n : Nat) :
    ExpCarrier A B (n + 1) → ExpCarrier A B n := fun e =>
  {
    map := fun m h => e.map m (h.trans (Nat.le_succ n))
    natural := by
      intro m h x
      simpa using e.natural m (h.trans (Nat.le_succ n)) x
  }

/-- The direct Kripke exponential object. -/
def exponential (A B : StageObj.{u}) : StageObj.{u} where
  carrier n := ExpCarrier A B n
  restrict n := expRestrict A B n

/-- Evaluation of a Kripke exponential at the current stage. -/
def eval (A B : StageObj.{u}) : Hom (prod (exponential A B) A) B where
  app n x := x.1.map n (Nat.le_refl n) x.2
  natural n x := by
    simpa [prod, exponential, expRestrict] using
      x.1.natural n (Nat.le_refl (n + 1)) x.2

/-- Build the exponential element induced by a morphism `X × A ⟶ B` and a
value of `X` at the current stage. -/
def curryElem {X A B : StageObj.{u}} (f : Hom (prod X A) B)
    (n : Nat) (x : X.carrier n) : ExpCarrier A B n where
  map m h a := f.app m (restrictLE X h x, a)
  natural m h a := by
    have hf := f.natural m (restrictLE X h x, a)
    have hr := restrict_restrictLE X h x
    simpa [prod, hr] using hf

/-- Currying for the direct Kripke exponential. -/
def curry {X A B : StageObj.{u}} (f : Hom (prod X A) B) : Hom X (exponential A B) where
  app n x := curryElem f n x
  natural n x := by
    apply ExpCarrier.ext
    intro m hm a
    change f.app m (restrictLE X (hm.trans (Nat.le_succ n)) x, a) =
      f.app m (restrictLE X hm (X.restrict n x), a)
    have hr := (restrictLE_trans X hm (Nat.le_succ n) x).symm
    simpa using congrArg (fun y => f.app m (y, a)) hr

/-- Beta law for the explicit evaluation/currying construction. -/
@[simp] theorem eval_curry {X A B : StageObj.{u}} (f : Hom (prod X A) B)
    (n : Nat) (x : X.carrier n) (a : A.carrier n) :
    (eval A B).app n ((curry f).app n x, a) = f.app n (x, a) := by
  rfl

/-- Terminal stage object. -/
def terminal : StageObj.{u} where
  carrier _ := PUnit
  restrict _ _ := PUnit.unit

/-- Unique displayed map into the terminal object. -/
def terminate (A : StageObj.{u}) : Hom A terminal where
  app _ _ := PUnit.unit
  natural _ _ := rfl

end MathSolve.RSICCC

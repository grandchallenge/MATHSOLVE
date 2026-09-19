import MathSolve.RSICCC.Stage

/-!
# RSI-CCC M1: direct Cartesian-closed structure

The Kripke exponential at stage `n` is a coherent family of maps at every
stage `m ≤ n`. Because `StageObj` carries arbitrary restriction maps and their
functor laws explicitly, the construction stays direct and proof-local.
-/

namespace MathSolve.RSICCC

universe u

/-- A coherent Kripke family representing an exponential element at stage `n`. -/
structure ExpCarrier (A B : StageObj.{u}) (n : Nat) where
  map : (m : Nat) → m ≤ n → A.carrier m → B.carrier m
  natural : ∀ {l m} (h₁ : l ≤ m) (h₂ : m ≤ n) x,
    B.restrict h₁ (map m h₂ x) =
      map l (h₁.trans h₂) (A.restrict h₁ x)

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

/-- Restrict a Kripke exponential element to an earlier observation stage. -/
def expRestrict {A B : StageObj.{u}} {m n : Nat} (h : m ≤ n)
    (e : ExpCarrier A B n) : ExpCarrier A B m where
  map l hl := e.map l (hl.trans h)
  natural h₁ h₂ x := by
    simpa using e.natural h₁ (h₂.trans h) x

/-- The direct Kripke exponential object. -/
def exponential (A B : StageObj.{u}) : StageObj.{u} where
  carrier n := ExpCarrier A B n
  restrict h e := expRestrict h e
  restrict_refl n e := by
    apply ExpCarrier.ext
    intro m hm a
    rfl
  restrict_trans h₁ h₂ e := by
    apply ExpCarrier.ext
    intro l hl a
    rfl

/-- Evaluation of a Kripke exponential at the current stage. -/
def eval (A B : StageObj.{u}) : Hom (prod (exponential A B) A) B where
  app n x := x.1.map n (Nat.le_refl n) x.2
  natural h x := by
    simpa [prod, exponential, expRestrict] using
      x.1.natural h (Nat.le_refl _) x.2

/-- Build the exponential element induced by `f : X × A ⟶ B` and a value of
`X` at stage `n`. -/
def curryElem {X A B : StageObj.{u}} (f : Hom (prod X A) B)
    (n : Nat) (x : X.carrier n) : ExpCarrier A B n where
  map m h a := f.app m (X.restrict h x, a)
  natural h₁ h₂ a := by
    calc
      B.restrict h₁ (f.app _ (X.restrict h₂ x, a))
          = f.app _
              (X.restrict h₁ (X.restrict h₂ x), A.restrict h₁ a) := by
                simpa [prod] using f.natural h₁ (X.restrict h₂ x, a)
      _ = f.app _ (X.restrict (h₁.trans h₂) x, A.restrict h₁ a) := by
            rw [X.restrict_trans h₁ h₂ x]

/-- Currying for the direct Kripke exponential. -/
def curry {X A B : StageObj.{u}} (f : Hom (prod X A) B) : Hom X (exponential A B) where
  app n x := curryElem f n x
  natural h x := by
    apply ExpCarrier.ext
    intro l hl a
    change f.app l (X.restrict (hl.trans h) x, a) =
      f.app l (X.restrict hl (X.restrict h x), a)
    rw [X.restrict_trans hl h x]

/-- Beta law for evaluation after currying. -/
@[simp] theorem eval_curry {X A B : StageObj.{u}} (f : Hom (prod X A) B)
    (n : Nat) (x : X.carrier n) (a : A.carrier n) :
    (eval A B).app n ((curry f).app n x, a) = f.app n (x, a) := by
  change f.app n (X.restrict (Nat.le_refl n) x, a) = f.app n (x, a)
  rw [X.restrict_refl n x]

/-- Eta law for the explicit Kripke exponential. -/
@[simp] theorem curry_eval (A B : StageObj.{u}) (n : Nat)
    (e : (exponential A B).carrier n) :
    (curry (eval A B)).app n e = e := by
  apply ExpCarrier.ext
  intro m hm a
  rfl

/-- Terminal stage object. -/
def terminal : StageObj.{u} where
  carrier _ := PUnit
  restrict _ _ := PUnit.unit
  restrict_refl _ _ := rfl
  restrict_trans _ _ _ := rfl

/-- Unique map into the terminal object. -/
def terminate (A : StageObj.{u}) : Hom A terminal where
  app _ _ := PUnit.unit
  natural _ _ := rfl

end MathSolve.RSICCC

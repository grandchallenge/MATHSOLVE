import MathSolve.RSICCC.Stage

/-!
# RSI-CCC M1: direct Cartesian-closed structure

This file develops the Kripke exponential for the direct stage-indexed model.
An element of `B^A` at stage `n` is represented recursively by its current
stage map together with the coherent element visible one stage earlier.
-/

namespace MathSolve.RSICCC

universe u

/-- Recursive carrier of the Kripke exponential. At stage zero it contains a
map `A₀ → B₀`. At a successor stage it contains the current map, the complete
previous-stage exponential element, and the one-step naturality law. -/
inductive ExpCarrier (A B : StageObj.{u}) : Nat → Type u
  | zero (top : A.carrier 0 → B.carrier 0) : ExpCarrier A B 0
  | succ {n : Nat}
      (top : A.carrier (n + 1) → B.carrier (n + 1))
      (prev : ExpCarrier A B n)
      (natural : ∀ a, B.restrict n (top a) = current prev (A.restrict n a)) :
      ExpCarrier A B (n + 1)
where
  /-- Current-stage map represented by an exponential element. -/
  current : {n : Nat} → ExpCarrier A B n → A.carrier n → B.carrier n
    | 0, zero f => f
    | _ + 1, succ f _ _ => f

namespace ExpCarrier

/-- Forget the current top stage. -/
def previous {A B : StageObj.{u}} {n : Nat} :
    ExpCarrier A B (n + 1) → ExpCarrier A B n
  | .succ _ prev _ => prev

/-- One-step naturality equation exposed independently of the constructor. -/
theorem naturality {A B : StageObj.{u}} {n : Nat}
    (e : ExpCarrier A B (n + 1)) (a : A.carrier (n + 1)) :
    B.restrict n (current e a) = current (previous e) (A.restrict n a) := by
  cases e with
  | succ _ _ h => exact h a

end ExpCarrier

/-- The direct Kripke exponential object. -/
def exponential (A B : StageObj.{u}) : StageObj.{u} where
  carrier n := ExpCarrier A B n
  restrict _ e := ExpCarrier.previous e

/-- Evaluation of a Kripke exponential at the current stage. -/
def eval (A B : StageObj.{u}) : Hom (prod (exponential A B) A) B where
  app _ x := ExpCarrier.current x.1 x.2
  natural n x := ExpCarrier.naturality x.1 x.2

/-- Build the exponential element induced by `f : X × A ⟶ B` and a value of
`X` at a stage. The recursive predecessor is obtained by restricting `x`. -/
def curryElem {X A B : StageObj.{u}} (f : Hom (prod X A) B) :
    (n : Nat) → X.carrier n → ExpCarrier A B n
  | 0, x => .zero (fun a => f.app 0 (x, a))
  | n + 1, x =>
      .succ
        (fun a => f.app (n + 1) (x, a))
        (curryElem f n (X.restrict n x))
        (by
          intro a
          simpa [prod, curryElem] using f.natural n (x, a))

/-- Currying for the direct Kripke exponential. -/
def curry {X A B : StageObj.{u}} (f : Hom (prod X A) B) : Hom X (exponential A B) where
  app n x := curryElem f n x
  natural _ _ := rfl

/-- Beta law for evaluation after currying. -/
@[simp] theorem eval_curry {X A B : StageObj.{u}} (f : Hom (prod X A) B)
    (n : Nat) (x : X.carrier n) (a : A.carrier n) :
    (eval A B).app n ((curry f).app n x, a) = f.app n (x, a) := by
  cases n <;> rfl

/-- Currying evaluation reconstructs every exponential element. -/
theorem curry_eval_elem (A B : StageObj.{u}) :
    ∀ n (e : ExpCarrier A B n), curryElem (eval A B) n e = e := by
  intro n e
  cases e with
  | zero top => rfl
  | @succ n top prev natural =>
      simp only [curryElem, eval, ExpCarrier.current, exponential]
      rw [curry_eval_elem A B n prev]

/-- Eta law at every stage of the explicit exponential. -/
@[simp] theorem curry_eval (A B : StageObj.{u}) (n : Nat)
    (e : (exponential A B).carrier n) :
    (curry (eval A B)).app n e = e :=
  curry_eval_elem A B n e

/-- Terminal stage object. -/
def terminal : StageObj.{u} where
  carrier _ := PUnit
  restrict _ _ := PUnit.unit

/-- Unique displayed map into the terminal object. -/
def terminate (A : StageObj.{u}) : Hom A terminal where
  app _ _ := PUnit.unit
  natural _ _ := rfl

end MathSolve.RSICCC

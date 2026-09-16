import Mathlib

/-!
# RSI-CCC M1: direct stage-indexed guarded substrate

The ambient object is presented as a contravariant stage family with explicit
restriction along every inequality. This is equivalent to presenting a
presheaf over the natural-number stage order and makes the Kripke exponential
construction direct and inspectable.

Frozen upstream formal-object SHA-256:
`1fca7a5e5bba2f4b59ccf9288a6a01129652091f86071c7be70022ea076d0edc`.
-/

namespace MathSolve.RSICCC

universe u

/-- A stage-indexed presheaf object. Restriction is functorial by construction
laws retained explicitly in the proof surface. -/
structure StageObj where
  carrier : Nat → Type u
  restrict : {m n : Nat} → m ≤ n → carrier n → carrier m
  restrict_refl : ∀ n x, restrict (Nat.le_refl n) x = x
  restrict_trans : ∀ {l m n} (h₁ : l ≤ m) (h₂ : m ≤ n) x,
    restrict h₁ (restrict h₂ x) = restrict (h₁.trans h₂) x

/-- A natural transformation between stage-indexed objects. -/
structure Hom (A B : StageObj.{u}) where
  app : (n : Nat) → A.carrier n → B.carrier n
  natural : ∀ {m n} (h : m ≤ n) x,
    B.restrict h (app n x) = app m (A.restrict h x)

namespace Hom

/-- Identity natural transformation. -/
def id (A : StageObj.{u}) : Hom A A where
  app _ x := x
  natural _ _ := rfl

/-- Composition of natural transformations. -/
def comp {A B C : StageObj.{u}} (g : Hom B C) (f : Hom A B) : Hom A C where
  app n x := g.app n (f.app n x)
  natural h x := by
    rw [g.natural h (f.app _ x)]
    rw [f.natural h x]

end Hom

/-- Stagewise binary product. -/
def prod (A B : StageObj.{u}) : StageObj.{u} where
  carrier n := A.carrier n × B.carrier n
  restrict h x := (A.restrict h x.1, B.restrict h x.2)
  restrict_refl n x := by
    apply Prod.ext
    · exact A.restrict_refl n x.1
    · exact B.restrict_refl n x.2
  restrict_trans h₁ h₂ x := by
    apply Prod.ext
    · exact A.restrict_trans h₁ h₂ x.1
    · exact B.restrict_trans h₁ h₂ x.2

/-- First product projection. -/
def fst (A B : StageObj.{u}) : Hom (prod A B) A where
  app _ x := x.1
  natural _ _ := rfl

/-- Second product projection. -/
def snd (A B : StageObj.{u}) : Hom (prod A B) B where
  app _ x := x.2
  natural _ _ := rfl

/-- Pair two morphisms into the stagewise product. -/
def pair {X A B : StageObj.{u}} (f : Hom X A) (g : Hom X B) : Hom X (prod A B) where
  app n x := (f.app n x, g.app n x)
  natural h x := by
    apply Prod.ext
    · exact f.natural h x
    · exact g.natural h x

@[simp] theorem fst_pair {X A B : StageObj.{u}} (f : Hom X A) (g : Hom X B)
    (n : Nat) (x : X.carrier n) :
    (fst A B).app n ((pair f g).app n x) = f.app n x := rfl

@[simp] theorem snd_pair {X A B : StageObj.{u}} (f : Hom X A) (g : Hom X B)
    (n : Nat) (x : X.carrier n) :
    (snd A B).app n ((pair f g).app n x) = g.app n x := rfl

/-- Carrier of the guarded later modality. -/
def laterCarrier (A : StageObj.{u}) : Nat → Type u
  | 0 => PUnit
  | n + 1 => A.carrier n

/-- Restriction for `Later`. A positive stage restriction is delegated one
stage down to the underlying presheaf. -/
def laterRestrict (A : StageObj.{u}) :
    {m n : Nat} → m ≤ n → laterCarrier A n → laterCarrier A m
  | 0, _, _, _ => PUnit.unit
  | _ + 1, 0, h, _ => by omega
  | m + 1, n + 1, h, x => A.restrict (Nat.succ_le_succ_iff.mp h) x

/-- The later modality: stage zero is trivial and every positive stage sees
one stage less of the underlying object. -/
def later (A : StageObj.{u}) : StageObj.{u} where
  carrier := laterCarrier A
  restrict := laterRestrict A
  restrict_refl := by
    intro n x
    cases n with
    | zero => rfl
    | succ n => simpa [laterRestrict] using A.restrict_refl n x
  restrict_trans := by
    intro l m n h₁ h₂ x
    cases l with
    | zero => rfl
    | succ l =>
        cases m with
        | zero => omega
        | succ m =>
            cases n with
            | zero => omega
            | succ n =>
                simpa [laterRestrict] using
                  A.restrict_trans
                    (Nat.succ_le_succ_iff.mp h₁)
                    (Nat.succ_le_succ_iff.mp h₂) x

/-- Stagewise component of `next : A ⟶ Later A`. -/
def nextApp (A : StageObj.{u}) : (n : Nat) → A.carrier n → (later A).carrier n
  | 0, _ => PUnit.unit
  | n + 1, x => A.restrict (Nat.le_succ n) x

/-- The canonical natural transformation into `Later`. -/
def next (A : StageObj.{u}) : Hom A (later A) where
  app := nextApp A
  natural := by
    intro m n h x
    cases m with
    | zero => rfl
    | succ m =>
        cases n with
        | zero => omega
        | succ n =>
            let h' : m ≤ n := Nat.succ_le_succ_iff.mp h
            change A.restrict h' (A.restrict (Nat.le_succ n) x) =
              A.restrict (Nat.le_succ m) (A.restrict h x)
            calc
              A.restrict h' (A.restrict (Nat.le_succ n) x)
                  = A.restrict (h'.trans (Nat.le_succ n)) x :=
                      A.restrict_trans h' (Nat.le_succ n) x
              _ = A.restrict ((Nat.le_succ m).trans h) x := by rfl
              _ = A.restrict (Nat.le_succ m) (A.restrict h x) := by
                    symm
                    exact A.restrict_trans (Nat.le_succ m) h x

/-- A coherent global section of a stage object. -/
structure Section (A : StageObj.{u}) where
  component : (n : Nat) → A.carrier n
  coherent : ∀ {m n} (h : m ≤ n), A.restrict h (component n) = component m

namespace Section

/-- Natural transformations map coherent sections to coherent sections. -/
def map {A B : StageObj.{u}} (f : Hom A B) (s : Section A) : Section B where
  component n := f.app n (s.component n)
  coherent h := by
    rw [f.natural h]
    rw [s.coherent h]

end Section

/-- Stagewise guarded fixed-point approximation for `f : Later A ⟶ A`. -/
def gfixAt {A : StageObj.{u}} (f : Hom (later A) A) : (n : Nat) → A.carrier n
  | 0 => f.app 0 PUnit.unit
  | n + 1 => f.app (n + 1) (gfixAt f n)

/-- One-step coherence of the guarded fixed-point approximants. -/
theorem gfixAt_step {A : StageObj.{u}} (f : Hom (later A) A) :
    ∀ n, A.restrict (Nat.le_succ n) (gfixAt f (n + 1)) = gfixAt f n := by
  intro n
  induction n with
  | zero =>
      simpa [gfixAt, later, laterRestrict] using
        f.natural (Nat.le_succ 0) (gfixAt f 0)
  | succ n ih =>
      have h := f.natural (Nat.le_succ (n + 1)) (gfixAt f (n + 1))
      calc
        A.restrict (Nat.le_succ (n + 1)) (gfixAt f (n + 1 + 1))
            = f.app (n + 1)
                ((later A).restrict (Nat.le_succ (n + 1)) (gfixAt f (n + 1))) := by
                  simpa [gfixAt] using h
        _ = f.app (n + 1)
              (A.restrict (Nat.le_succ n) (gfixAt f (n + 1))) := rfl
        _ = f.app (n + 1) (gfixAt f n) := by rw [ih]
        _ = gfixAt f (n + 1) := rfl

/-- Coherence along every stage restriction. -/
theorem gfixAt_coherent {A : StageObj.{u}} (f : Hom (later A) A)
    {m n : Nat} (h : m ≤ n) :
    A.restrict h (gfixAt f n) = gfixAt f m := by
  induction h with
  | refl => exact A.restrict_refl _ _
  | @step n h ih =>
      calc
        A.restrict (Nat.step h) (gfixAt f (n + 1))
            = A.restrict h
                (A.restrict (Nat.le_succ n) (gfixAt f (n + 1))) := by
                  simpa using
                    (A.restrict_trans h (Nat.le_succ n) (gfixAt f (n + 1))).symm
        _ = A.restrict h (gfixAt f n) := by rw [gfixAt_step f n]
        _ = gfixAt f _ := ih

/-- The guarded fixed point as a coherent stagewise section. -/
def gfixSection {A : StageObj.{u}} (f : Hom (later A) A) : Section A where
  component := gfixAt f
  coherent h := gfixAt_coherent f h

/-- Stage-zero unfold law. -/
@[simp] theorem gfix_zero {A : StageObj.{u}} (f : Hom (later A) A) :
    (gfixSection f).component 0 = f.app 0 PUnit.unit := rfl

/-- Successor-stage guarded unfold law. -/
@[simp] theorem gfix_succ {A : StageObj.{u}} (f : Hom (later A) A) (n : Nat) :
    (gfixSection f).component (n + 1) =
      f.app (n + 1) ((gfixSection f).component n) := rfl

end MathSolve.RSICCC

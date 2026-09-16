import Mathlib

/-!
# RSI-CCC M1: direct stage-indexed guarded substrate

This file implements the first theorem-first tranche for `RSI-CCC-001`.
It deliberately stays below the later Kripke-exponential, reflection,
refinement, and admission layers.

The frozen upstream formal object is identified by SHA-256
`1fca7a5e5bba2f4b59ccf9288a6a01129652091f86071c7be70022ea076d0edc`.
-/

namespace MathSolve.RSICCC

universe u

/-- A direct presentation of an object of the topos-of-trees base used by M1:
a family of stage-indexed carriers with one-step restriction maps. -/
structure StageObj where
  carrier : Nat → Type u
  restrict : (n : Nat) → carrier (n + 1) → carrier n

/-- A morphism is a stagewise map commuting with one-step restriction. -/
structure Hom (A B : StageObj.{u}) where
  app : (n : Nat) → A.carrier n → B.carrier n
  natural : ∀ n x, B.restrict n (app (n + 1) x) = app n (A.restrict n x)

namespace Hom

/-- Identity natural transformation. -/
def id (A : StageObj.{u}) : Hom A A where
  app _ x := x
  natural _ _ := rfl

/-- Composition of natural transformations. -/
def comp {A B C : StageObj.{u}} (g : Hom B C) (f : Hom A B) : Hom A C where
  app n x := g.app n (f.app n x)
  natural n x := by
    rw [g.natural n (f.app (n + 1) x)]
    rw [f.natural n x]

end Hom

/-- Stagewise binary product. -/
def prod (A B : StageObj.{u}) : StageObj.{u} where
  carrier n := A.carrier n × B.carrier n
  restrict n x := (A.restrict n x.1, B.restrict n x.2)

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
  natural n x := by
    apply Prod.ext
    · exact f.natural n x
    · exact g.natural n x

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

/-- Restriction map for the guarded later modality. -/
def laterRestrict (A : StageObj.{u}) :
    (n : Nat) → laterCarrier A (n + 1) → laterCarrier A n
  | 0, _ => PUnit.unit
  | n + 1, x => A.restrict n x

/-- The later modality: stage zero is trivial and every successor stage sees
one stage less of the underlying object. -/
def later (A : StageObj.{u}) : StageObj.{u} where
  carrier := laterCarrier A
  restrict := laterRestrict A

/-- Stagewise component of `next : A ⟶ Later A`. -/
def nextApp (A : StageObj.{u}) : (n : Nat) → A.carrier n → (later A).carrier n
  | 0, _ => PUnit.unit
  | n + 1, x => A.restrict n x

/-- The canonical natural transformation into `Later`. -/
def next (A : StageObj.{u}) : Hom A (later A) where
  app := nextApp A
  natural n x := by
    cases n <;> rfl

/-- A coherent global section of a stage object. -/
structure Section (A : StageObj.{u}) where
  at : (n : Nat) → A.carrier n
  coherent : ∀ n, A.restrict n (at (n + 1)) = at n

/-- Stagewise guarded fixed-point approximation for `f : Later A ⟶ A`. -/
def gfixAt {A : StageObj.{u}} (f : Hom (later A) A) : (n : Nat) → A.carrier n
  | 0 => f.app 0 PUnit.unit
  | n + 1 => f.app (n + 1) (gfixAt f n)

/-- The guarded fixed-point approximants form a coherent section. -/
theorem gfixAt_coherent {A : StageObj.{u}} (f : Hom (later A) A) :
    ∀ n, A.restrict n (gfixAt f (n + 1)) = gfixAt f n := by
  intro n
  induction n with
  | zero =>
      simpa [gfixAt, later, laterRestrict] using f.natural 0 (gfixAt f 0)
  | succ n ih =>
      simpa [gfixAt, later, laterRestrict, ih] using
        f.natural (n + 1) (gfixAt f (n + 1))

/-- The guarded fixed point as a coherent stagewise section. -/
def gfixSection {A : StageObj.{u}} (f : Hom (later A) A) : Section A where
  at := gfixAt f
  coherent := gfixAt_coherent f

/-- Stage-zero unfold law. -/
@[simp] theorem gfix_zero {A : StageObj.{u}} (f : Hom (later A) A) :
    (gfixSection f).at 0 = f.app 0 PUnit.unit := rfl

/-- Successor-stage guarded unfold law. -/
@[simp] theorem gfix_succ {A : StageObj.{u}} (f : Hom (later A) A) (n : Nat) :
    (gfixSection f).at (n + 1) = f.app (n + 1) ((gfixSection f).at n) := rfl

end MathSolve.RSICCC

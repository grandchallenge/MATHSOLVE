/-
Copyright 2026 The Formal Conjectures Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-/

/- Source-extracted from google-deepmind/formal-conjectures at
85f863718beeec7b58a3a1926ee92e3472bc2020, blob
9b85fd453afcfa95c6572e2a98d214d50f7e8caa.
Exact predicates and right-hand-side propositions, with import and
declaration wrappers adapted to MATHSOLVE's pinned Mathlib.
This is not an import or compilation of the full upstream package. -/
import Mathlib

open Set
namespace Erdos602

def IsMonochromatic {α : Type*} (f : α → Fin 2) (A : Set α) : Prop :=
  ∀ x ∈ A, ∀ y ∈ A, f x = f y

/-- A family `(A_i)_{i ∈ I}` of subsets of `α` has **Property B** if there exists
a 2-colouring `f : α → Fin 2` such that no `A_i` is monochromatic. -/
def HasPropertyB {α : Type*} (I : Type*) (A : I → Set α) : Prop :=
  ∃ f : α → Fin 2, ∀ i, ¬IsMonochromatic f (A i)

def CountableIndexTarget : Prop :=
    ∀ {α : Type*} (A : ℕ → Set α),
      (∀ i, (A i).Countable ∧ (A i).Infinite) →
      (∀ i j, i ≠ j → (A i ∩ A j).Finite) →
      (∀ i j, i ≠ j → Set.ncard (A i ∩ A j) ≠ 1) →
      HasPropertyB ℕ A

def UnrestrictedTarget : Prop :=
    ∀ {α : Type*} {I : Type*} (A : I → Set α),
      (∀ i, (A i).Countable ∧ (A i).Infinite) →
      (∀ i j, i ≠ j → (A i ∩ A j).Finite) →
      (∀ i j, i ≠ j → Set.ncard (A i ∩ A j) ≠ 1) →
      HasPropertyB I A

end Erdos602

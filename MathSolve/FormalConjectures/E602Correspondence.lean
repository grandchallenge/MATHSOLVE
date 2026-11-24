import MathSolve.FormalConjectures.E602SourceExtract
import MathSolve.Erdos.E602SetBridge

/-! Kernel-checked correspondence with the source-locked extracted
FormalConjectures predicates and propositions. The original package
uses Lean 4.27.0; this is an adapted import in MATHSOLVE 4.29.1,
not an upstream build or a proof of the unrestricted proposition. -/

namespace MathSolve.Erdos602
universe u v

theorem monochromatic_source_eq {X : Type v} (f : X → Fin 2) (A : Set X) :
    IsMonochromatic f A = _root_.Erdos602.IsMonochromatic f A := rfl

theorem propertyB_source_eq {X : Type v} (I : Type u) (A : I → Set X) :
    HasPropertyB I A = _root_.Erdos602.HasPropertyB I A := rfl

def UnrestrictedTarget : Prop :=
  ∀ {X : Type v} {I : Type u} (A : I → Set X),
    (∀ i, (A i).Countable ∧ (A i).Infinite) →
    (∀ i j, i ≠ j → (A i ∩ A j).Finite) →
    (∀ i j, i ≠ j → Set.ncard (A i ∩ A j) ≠ 1) →
    HasPropertyB I A

theorem unrestricted_source_eq :
    UnrestrictedTarget.{u,v} = _root_.Erdos602.UnrestrictedTarget := rfl

/-- The precise extracted right-hand side of the upstream countable_index
variant follows from the stronger Bernstein lemma. -/
theorem source_countable_index :
    _root_.Erdos602.CountableIndexTarget := by
  intro X A hMembers _hInter _hNoSingleton
  exact bernstein_nat A (fun i => (hMembers i).2)

/-- The logical answer wrapper, without the upstream answer elaborator. -/
theorem source_countable_index_true_iff :
    True ↔ _root_.Erdos602.CountableIndexTarget :=
  ⟨fun _ => source_countable_index, fun _ => trivial⟩

#print axioms monochromatic_source_eq
#print axioms propertyB_source_eq
#print axioms unrestricted_source_eq
#print axioms source_countable_index
#print axioms source_countable_index_true_iff

end MathSolve.Erdos602

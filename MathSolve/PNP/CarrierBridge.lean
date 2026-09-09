/-!
# PNP Boolean decision problem / binary language carrier bridge

This file proves only the carrier-level bridge used by `PNP-BRIDGE-001`.
It does not define or identify the complexity classes `P` or `NP`.
-/

namespace MathSolve.PNP

abbrev DecisionProblem := List Bool → Bool
abbrev BinaryLanguage := List Bool → Prop
abbrev ComplexityClass := DecisionProblem → Prop
abbrev LanguageClass := BinaryLanguage → Prop

/-- The language accepted by a total Boolean-valued decision problem. -/
def languageOf (decision : DecisionProblem) : BinaryLanguage :=
  fun input => decision input = true

/-- Transport a class of Boolean decision problems to its class of true-preimage languages. -/
def languageClassOf (problems : ComplexityClass) : LanguageClass :=
  fun language => ∃ decision, problems decision ∧ language = languageOf decision

theorem mem_languageOf_iff (decision : DecisionProblem) (input : List Bool) :
    languageOf decision input ↔ decision input = true :=
  by rfl

/-- A Boolean decision problem is determined by its true-preimage language. -/
theorem languageOf_injective : Function.Injective languageOf := by
  intro left right h
  funext input
  cases hleft : left input <;> cases hright : right input <;> try rfl
  all_goals
    have hpoint := congrFun h input
    simp [languageOf, hleft, hright] at hpoint

/-- Transport through `languageOf` preserves and reflects class equality. -/
theorem languageClassOf_eq_iff (left right : ComplexityClass) :
    languageClassOf left = languageClassOf right ↔ left = right := by
  constructor
  · intro h
    ext decision
    constructor
    · intro hleft
      have himage : languageClassOf left (languageOf decision) := ⟨decision, hleft, rfl⟩
      rw [h] at himage
      rcases himage with ⟨other, hright, hcarrier⟩
      have : other = decision := languageOf_injective hcarrier.symm
      simpa [this] using hright
    · intro hright
      have himage : languageClassOf right (languageOf decision) := ⟨decision, hright, rfl⟩
      rw [← h] at himage
      rcases himage with ⟨other, hleft, hcarrier⟩
      have : other = decision := languageOf_injective hcarrier.symm
      simpa [this] using hleft
  · exact congrArg languageClassOf

/-- In particular, transport preserves and reflects class inequality. -/
theorem languageClassOf_ne_iff (left right : ComplexityClass) :
    languageClassOf left ≠ languageClassOf right ↔ left ≠ right := by
  constructor
  · intro transported original
    exact transported ((languageClassOf_eq_iff left right).2 original)
  · intro original transported
    exact original ((languageClassOf_eq_iff left right).1 transported)

end MathSolve.PNP

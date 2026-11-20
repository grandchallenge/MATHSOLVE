import PNPAbove.WP24CNF

/-!
Concrete exact Lean tests of SAT instance dependence. Both simple
instances have the same question/answer alphabet. Only the formula
differs. The resulting quantum-value promises genuinely differ.
-/

namespace PNPAbove.WP24
open MIPRE MIPRE.SAT

/-- A contradictory formula in the original pinned formula syntax. -/
def impossible : SAT.Fml := .and (.inp 0) (.not (.inp 0))

/-- A tautological formula in the same original syntax. -/
def possible : SAT.Fml := .or (.inp 0) (.not (.inp 0))

theorem impossible_unsat : ¬ Satisfiable 1 impossible := by
  rintro ⟨w, hw⟩
  have hbit : bitsAt w 0 = w ⟨0, by decide⟩ := bitsAt_fin w ⟨0, by decide⟩
  cases h : w ⟨0, by decide⟩ <;>
    simp [impossible, SAT.Fml.eval, hbit] at hw

theorem possible_sat : Satisfiable 1 possible := by
  refine ⟨fun _ => true, ?_⟩
  simp [possible, SAT.Fml.eval, bitsAt]

/-- Original quantum strategy value 0 for this negative input. -/
theorem impossible_quantum_zero :
    MIPRE.quantumValue (satGame 1 impossible).toGame = 0 :=
  quantum_zero_of_unsat 1 impossible impossible_unsat

/-- Original quantum strategy value 1 for this positive input. -/
theorem possible_quantum_one :
    MIPRE.quantumValue (satGame 1 possible).toGame = 1 :=
  quantum_one_of_sat 1 possible possible_sat

/-- Strict native nonlocal-value distinction between SAT and UNSAT inputs:
the fixed Bell verifier of WP23A was index-invariant; this game is not. -/
theorem sat_instance_changes_quantum_value :
    MIPRE.quantumValue (satGame 1 impossible).toGame ≠
      MIPRE.quantumValue (satGame 1 possible).toGame := by
  rw [impossible_quantum_zero, possible_quantum_one]
  norm_num

end PNPAbove.WP24

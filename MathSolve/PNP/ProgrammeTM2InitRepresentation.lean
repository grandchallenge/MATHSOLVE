import MathSolve.PNP.ProgrammeTM2InitRun

/-!
# Reverse initialization representation

The exact linear initialization run ends at a run-mode configuration that
represents the native Programme initial configuration cell-for-cell.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- ListBlank input cells use none beyond the explicit list. -/
theorem programmeTM2_map_some_getI (bits : List Bool) (n : Nat) :
    (bits.map some).getI n = bits[n]? := by
  rw [List.getI_eq_getElem?_getD, List.getElem?_map]
  cases bits[n]? <;> rfl

/-- The empty explicit input side is blank at every offset. -/
theorem programmeTM2_emptyOption_getI (n : Nat) :
    ([] : List (Option Bool)).getI n = none := by
  rw [List.getI_eq_getElem?_getD]
  rfl

/-- The empty explicit work side is blank at every offset. -/
theorem programmeTM2_emptyWork_getI (M : ProgrammeMachine) (n : Nat) :
    ([] : List M.Symbol).getI n = M.blank := by
  rw [List.getI_eq_getElem?_getD]
  rfl

theorem programmeTM2ReadyInitCfg_represents (M : ProgrammeMachine)
    (input : List Bool) :
    ProgrammeTM2Represents M input (M.init input)
      (programmeTM2ReadyInitCfg M input) := by
  refine ⟨rfl, rfl, rfl, ?_, ?_⟩
  · intro offset
    cases offset with
    | ofNat n =>
        cases n with
        | zero =>
            cases input <;>
              simp [programmeTM2InputTape, programmeTM2ReadyInitCfg,
                programmeTM2InitStacks, ProgrammeMachine.init,
                programmeInputRead, Turing.Tape.nth,
                programmeTM2_emptyOption_getI] <;> rfl
        | succ n =>
            cases input with
            | nil =>
                simp [programmeTM2InputTape, programmeTM2ReadyInitCfg,
                  programmeTM2InitStacks, ProgrammeMachine.init,
                  programmeInputRead, Turing.Tape.nth, Turing.ListBlank.nth_mk,
                  programmeTM2_map_some_getI, programmeTM2_emptyOption_getI] <;> rfl
            | cons bit tail =>
                simp [programmeTM2InputTape, programmeTM2ReadyInitCfg,
                  programmeTM2InitStacks, ProgrammeMachine.init,
                  programmeInputRead, Turing.Tape.nth, Turing.ListBlank.nth_mk,
                  programmeTM2_map_some_getI, programmeTM2_emptyOption_getI] <;> omega
    | negSucc n =>
        simp [programmeTM2InputTape, programmeTM2ReadyInitCfg,
          programmeTM2InitStacks, ProgrammeMachine.init,
          programmeInputRead, Turing.Tape.nth,
          programmeTM2_emptyOption_getI] <;> rfl
  · intro tape offset
    cases offset with
    | ofNat n =>
        cases n <;>
          simp [programmeTM2WorkTape, programmeTM2ReadyInitCfg,
            programmeTM2InitStacks, programmeTM2InitialState,
            ProgrammeMachine.init, Turing.Tape.nth, Turing.ListBlank.nth_mk,
            programmeTM2_emptyWork_getI] <;> rfl
    | negSucc n =>
        simp [programmeTM2WorkTape, programmeTM2ReadyInitCfg,
          programmeTM2InitStacks, programmeTM2InitialState,
          ProgrammeMachine.init, Turing.Tape.nth, Turing.ListBlank.nth_mk,
          programmeTM2_emptyWork_getI] <;> rfl

#print axioms programmeTM2_map_some_getI
#print axioms programmeTM2_emptyOption_getI
#print axioms programmeTM2_emptyWork_getI
#print axioms programmeTM2ReadyInitCfg_represents

end

end MathSolve.PNP

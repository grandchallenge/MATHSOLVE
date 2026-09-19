import MathSolve.PNP.ProgrammeTM2InitRun

/-!
# Reverse initialization representation

The exact linear initialization run ends at a run-mode configuration that
represents the native Programme initial configuration cell-for-cell.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

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
                programmeInputRead, Turing.Tape.nth]
        | succ n =>
            cases input <;>
              simp [programmeTM2InputTape, programmeTM2ReadyInitCfg,
                programmeTM2InitStacks, ProgrammeMachine.init,
                programmeInputRead, Turing.Tape.nth, Turing.ListBlank.nth_mk]
    | negSucc n =>
        simp [programmeTM2InputTape, programmeTM2ReadyInitCfg,
          programmeTM2InitStacks, ProgrammeMachine.init,
          programmeInputRead, Turing.Tape.nth]
  · intro tape offset
    cases offset with
    | ofNat n =>
        cases n <;>
          simp [programmeTM2WorkTape, programmeTM2ReadyInitCfg,
            programmeTM2InitStacks, ProgrammeMachine.init,
            Turing.Tape.nth, Turing.ListBlank.nth_mk]
    | negSucc n =>
        simp [programmeTM2WorkTape, programmeTM2ReadyInitCfg,
          programmeTM2InitStacks, ProgrammeMachine.init,
          Turing.Tape.nth, Turing.ListBlank.nth_mk]

#print axioms programmeTM2ReadyInitCfg_represents

end

end MathSolve.PNP

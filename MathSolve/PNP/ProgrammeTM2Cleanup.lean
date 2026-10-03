import MathSolve.PNP.ProgrammeTM2RunInvariant

/-!
# Canonical terminal cleanup for the reverse Programme-to-TM2 compiler

After the simulated Programme reaches accept/reject, the concrete FinTM2 clears
all auxiliary tape stacks and emits exactly one Boolean on the designated output
stack.  This file fixes a closed-form cleanup state and proves the local cleanup
transitions used by the quantitative terminal run.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Explicit heterogeneous stack family during terminal cleanup. -/
def programmeTM2CleanupStacks (M : ProgrammeMachine)
    (raw temp : List Bool)
    (inputLeft inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    ∀ k : ProgrammeTM2Stack M.workTapeCount,
      List (programmeTM2StackAlphabet M k)
  | .rawInput => raw
  | .inputTemp => temp
  | .inputLeft => inputLeft
  | .inputRight => inputRight
  | .workLeft tape => workLeft tape
  | .workRight tape => workRight tape
  | .output => output

/-- Closed-form cleanup configuration carrying one fixed terminal control. -/
def programmeTM2CleanupCfg (M : ProgrammeMachine)
    (mode : ProgrammeTM2Mode M.workTapeCount)
    (base : ProgrammeTM2State M)
    (raw temp : List Bool)
    (inputLeft inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).Cfg where
  l := some mode
  var := { base with mode := mode }
  stk := programmeTM2CleanupStacks M raw temp inputLeft inputRight
    workLeft workRight output

/-- Cleaning one raw-input cell stays in the raw cleanup mode. -/
theorem programmeTM2_step_cleanRaw_cons (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (bit : Bool) (raw temp : List Bool)
    (inputLeft inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanRaw base
          (bit :: raw) temp inputLeft inputRight workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M .cleanRaw base
          raw temp inputLeft inputRight workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

/-- The blank raw-input pop advances to temporary-stack cleanup. -/
theorem programmeTM2_step_cleanRaw_nil (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (temp : List Bool)
    (inputLeft inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanRaw base
          [] temp inputLeft inputRight workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M .cleanTemp base
          [] temp inputLeft inputRight workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

theorem programmeTM2_step_cleanTemp_cons (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (bit : Bool) (temp : List Bool)
    (inputLeft inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanTemp base
          [] (bit :: temp) inputLeft inputRight workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M .cleanTemp base
          [] temp inputLeft inputRight workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

theorem programmeTM2_step_cleanTemp_nil (M : ProgrammeMachine)
    (base : ProgrammeTM2State M)
    (inputLeft inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanTemp base
          [] [] inputLeft inputRight workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M .cleanInputLeft base
          [] [] inputLeft inputRight workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

theorem programmeTM2_step_cleanInputLeft_cons (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (symbol : Option Bool)
    (inputLeft inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanInputLeft base
          [] [] (symbol :: inputLeft) inputRight workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M .cleanInputLeft base
          [] [] inputLeft inputRight workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

theorem programmeTM2_step_cleanInputLeft_nil (M : ProgrammeMachine)
    (base : ProgrammeTM2State M)
    (inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanInputLeft base
          [] [] [] inputRight workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M .cleanInputRight base
          [] [] [] inputRight workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

theorem programmeTM2_step_cleanInputRight_cons (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (symbol : Option Bool)
    (inputRight : List (Option Bool))
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanInputRight base
          [] [] [] (symbol :: inputRight) workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M .cleanInputRight base
          [] [] [] inputRight workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

/-- One work-left cleanup pop consumes one stored work symbol. -/
theorem programmeTM2_step_cleanWorkLeft_cons (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (tape : Fin M.workTapeCount)
    (symbol : M.Symbol) (left : List M.Symbol)
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool)
    (hleft : workLeft tape = symbol :: left) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M (.cleanWorkLeft tape) base
          [] [] [] [] workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M (.cleanWorkLeft tape) base
          [] [] [] [] (Function.update workLeft tape left) workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  rw [hleft]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

/-- One work-right cleanup pop consumes one stored work symbol. -/
theorem programmeTM2_step_cleanWorkRight_cons (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (tape : Fin M.workTapeCount)
    (symbol : M.Symbol) (right : List M.Symbol)
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool)
    (hright : workRight tape = symbol :: right) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
          [] [] [] [] workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
          [] [] [] [] workLeft (Function.update workRight tape right) output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  rw [hright]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

/-- With no work tapes, the empty input-right cleanup goes directly to emit. -/
theorem programmeTM2_step_cleanInputRight_nil_noWork
    (M : ProgrammeMachine) (hzero : M.workTapeCount = 0)
    (base : ProgrammeTM2State M)
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanInputRight base
          [] [] [] [] workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M
          (.emit (programmeTM2TerminalResult M base)) base
          [] [] [] [] workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  simp [programmeTM2FirstWorkOrEmit, hzero]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

/-- Emit mode resets local state, writes one Boolean output, and halts. -/
theorem programmeTM2_step_emit_halt (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (result : Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M (.emit result) base
          [] [] [] [] (fun _ => []) (fun _ => []) []) =
      some (Turing.haltList (programmeTM2Machine M) [result]) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks, Turing.haltList]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

#print axioms programmeTM2_step_cleanRaw_cons
#print axioms programmeTM2_step_cleanRaw_nil
#print axioms programmeTM2_step_cleanTemp_cons
#print axioms programmeTM2_step_cleanTemp_nil
#print axioms programmeTM2_step_cleanInputLeft_cons
#print axioms programmeTM2_step_cleanInputLeft_nil
#print axioms programmeTM2_step_cleanInputRight_cons
#print axioms programmeTM2_step_cleanWorkLeft_cons
#print axioms programmeTM2_step_cleanWorkRight_cons
#print axioms programmeTM2_step_cleanInputRight_nil_noWork
#print axioms programmeTM2_step_emit_halt

end

end MathSolve.PNP

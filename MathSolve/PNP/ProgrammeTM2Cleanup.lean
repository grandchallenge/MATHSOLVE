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


/-- The blank input-right pop advances to the first work cleanup mode, or emit
when there are no work tapes. -/
theorem programmeTM2_step_cleanInputRight_nil (M : ProgrammeMachine)
    (base : ProgrammeTM2State M)
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanInputRight base
          [] [] [] [] workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M
          (programmeTM2FirstWorkOrEmit M base) base
          [] [] [] [] workLeft workRight output) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux, programmeTM2CleanupCfg,
    programmeTM2CleanupStacks]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2CleanupStacks, Function.update] <;> rfl

/-- The blank left-work pop advances to right-work cleanup for the same tape. -/
theorem programmeTM2_step_cleanWorkLeft_nil (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (tape : Fin M.workTapeCount)
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) (hleft : workLeft tape = []) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M (.cleanWorkLeft tape) base
          [] [] [] [] workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
          [] [] [] [] workLeft workRight output) := by
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

/-- The blank right-work pop advances to the next work tape or emit. -/
theorem programmeTM2_step_cleanWorkRight_nil (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (tape : Fin M.workTapeCount)
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) (hright : workRight tape = []) :
    (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
          [] [] [] [] workLeft workRight output) =
      some
        (programmeTM2CleanupCfg M
          (programmeTM2NextWorkOrEmit M tape base) base
          [] [] [] [] workLeft workRight output) := by
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

/-- Clear the raw-input stack in exactly one transition per stored cell plus
one blank-detection transition. -/
theorem programmeTM2_cleanRaw_run (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) :
    ∀ (raw temp : List Bool)
      (inputLeft inputRight : List (Option Bool))
      (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
      (output : List Bool),
      Nonempty
        (StateTransition.EvalsToInTime
          (programmeTM2Machine M).step
          (programmeTM2CleanupCfg M .cleanRaw base
            raw temp inputLeft inputRight workLeft workRight output)
          (some
            (programmeTM2CleanupCfg M .cleanTemp base
              [] temp inputLeft inputRight workLeft workRight output))
          (raw.length + 1)) := by
  intro raw
  induction raw with
  | nil =>
      intro temp inputLeft inputRight workLeft workRight output
      exact ⟨programmeTM2_one_step_in_time
        (programmeTM2_step_cleanRaw_nil M base temp
          inputLeft inputRight workLeft workRight output)⟩
  | cons bit raw ih =>
      intro temp inputLeft inputRight workLeft workRight output
      have hone := programmeTM2_one_step_in_time
        (programmeTM2_step_cleanRaw_cons M base bit raw temp
          inputLeft inputRight workLeft workRight output)
      rcases ih temp inputLeft inputRight workLeft workRight output with ⟨hrest⟩
      refine ⟨?_⟩
      simpa [Nat.add_assoc] using
        StateTransition.EvalsToInTime.trans
          (programmeTM2Machine M).step
          1 (raw.length + 1)
          (programmeTM2CleanupCfg M .cleanRaw base
            (bit :: raw) temp inputLeft inputRight workLeft workRight output)
          (programmeTM2CleanupCfg M .cleanRaw base
            raw temp inputLeft inputRight workLeft workRight output)
          (some (programmeTM2CleanupCfg M .cleanTemp base
            [] temp inputLeft inputRight workLeft workRight output))
          hone hrest

theorem programmeTM2_cleanTemp_run (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) :
    ∀ (temp : List Bool)
      (inputLeft inputRight : List (Option Bool))
      (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
      (output : List Bool),
      Nonempty
        (StateTransition.EvalsToInTime
          (programmeTM2Machine M).step
          (programmeTM2CleanupCfg M .cleanTemp base
            [] temp inputLeft inputRight workLeft workRight output)
          (some
            (programmeTM2CleanupCfg M .cleanInputLeft base
              [] [] inputLeft inputRight workLeft workRight output))
          (temp.length + 1)) := by
  intro temp
  induction temp with
  | nil =>
      intro inputLeft inputRight workLeft workRight output
      exact ⟨programmeTM2_one_step_in_time
        (programmeTM2_step_cleanTemp_nil M base
          inputLeft inputRight workLeft workRight output)⟩
  | cons bit temp ih =>
      intro inputLeft inputRight workLeft workRight output
      have hone := programmeTM2_one_step_in_time
        (programmeTM2_step_cleanTemp_cons M base bit temp
          inputLeft inputRight workLeft workRight output)
      rcases ih inputLeft inputRight workLeft workRight output with ⟨hrest⟩
      refine ⟨?_⟩
      simpa [Nat.add_assoc] using
        StateTransition.EvalsToInTime.trans
          (programmeTM2Machine M).step
          1 (temp.length + 1)
          (programmeTM2CleanupCfg M .cleanTemp base
            [] (bit :: temp) inputLeft inputRight workLeft workRight output)
          (programmeTM2CleanupCfg M .cleanTemp base
            [] temp inputLeft inputRight workLeft workRight output)
          (some (programmeTM2CleanupCfg M .cleanInputLeft base
            [] [] inputLeft inputRight workLeft workRight output))
          hone hrest

theorem programmeTM2_cleanInputLeft_run (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) :
    ∀ (inputLeft inputRight : List (Option Bool))
      (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
      (output : List Bool),
      Nonempty
        (StateTransition.EvalsToInTime
          (programmeTM2Machine M).step
          (programmeTM2CleanupCfg M .cleanInputLeft base
            [] [] inputLeft inputRight workLeft workRight output)
          (some
            (programmeTM2CleanupCfg M .cleanInputRight base
              [] [] [] inputRight workLeft workRight output))
          (inputLeft.length + 1)) := by
  intro inputLeft
  induction inputLeft with
  | nil =>
      intro inputRight workLeft workRight output
      exact ⟨programmeTM2_one_step_in_time
        (programmeTM2_step_cleanInputLeft_nil M base
          inputRight workLeft workRight output)⟩
  | cons symbol inputLeft ih =>
      intro inputRight workLeft workRight output
      have hone := programmeTM2_one_step_in_time
        (programmeTM2_step_cleanInputLeft_cons M base symbol inputLeft
          inputRight workLeft workRight output)
      rcases ih inputRight workLeft workRight output with ⟨hrest⟩
      refine ⟨?_⟩
      simpa [Nat.add_assoc] using
        StateTransition.EvalsToInTime.trans
          (programmeTM2Machine M).step
          1 (inputLeft.length + 1)
          (programmeTM2CleanupCfg M .cleanInputLeft base
            [] [] (symbol :: inputLeft) inputRight workLeft workRight output)
          (programmeTM2CleanupCfg M .cleanInputLeft base
            [] [] inputLeft inputRight workLeft workRight output)
          (some (programmeTM2CleanupCfg M .cleanInputRight base
            [] [] [] inputRight workLeft workRight output))
          hone hrest

theorem programmeTM2_cleanInputRight_run (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) :
    ∀ (inputRight : List (Option Bool))
      (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
      (output : List Bool),
      Nonempty
        (StateTransition.EvalsToInTime
          (programmeTM2Machine M).step
          (programmeTM2CleanupCfg M .cleanInputRight base
            [] [] [] inputRight workLeft workRight output)
          (some
            (programmeTM2CleanupCfg M
              (programmeTM2FirstWorkOrEmit M base) base
              [] [] [] [] workLeft workRight output))
          (inputRight.length + 1)) := by
  intro inputRight
  induction inputRight with
  | nil =>
      intro workLeft workRight output
      exact ⟨programmeTM2_one_step_in_time
        (programmeTM2_step_cleanInputRight_nil M base workLeft workRight output)⟩
  | cons symbol inputRight ih =>
      intro workLeft workRight output
      have hone := programmeTM2_one_step_in_time
        (programmeTM2_step_cleanInputRight_cons M base symbol inputRight
          workLeft workRight output)
      rcases ih workLeft workRight output with ⟨hrest⟩
      refine ⟨?_⟩
      simpa [Nat.add_assoc] using
        StateTransition.EvalsToInTime.trans
          (programmeTM2Machine M).step
          1 (inputRight.length + 1)
          (programmeTM2CleanupCfg M .cleanInputRight base
            [] [] [] (symbol :: inputRight) workLeft workRight output)
          (programmeTM2CleanupCfg M .cleanInputRight base
            [] [] [] inputRight workLeft workRight output)
          (some (programmeTM2CleanupCfg M
            (programmeTM2FirstWorkOrEmit M base) base
            [] [] [] [] workLeft workRight output))
          hone hrest

/-- Clear one selected work-left stack. -/
theorem programmeTM2_cleanWorkLeft_run (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (tape : Fin M.workTapeCount)
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    Nonempty
      (StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M (.cleanWorkLeft tape) base
          [] [] [] [] workLeft workRight output)
        (some
          (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
            [] [] [] [] (Function.update workLeft tape [])
            workRight output))
        ((workLeft tape).length + 1)) := by
  generalize hleft : workLeft tape = left
  induction left generalizing workLeft with
  | nil =>
      have hnil : workLeft tape = [] := hleft
      have hone := programmeTM2_one_step_in_time
        (programmeTM2_step_cleanWorkLeft_nil M base tape
          workLeft workRight output hnil)
      refine ⟨?_⟩
      simpa [hnil] using hone
  | cons symbol left ih =>
      have hstep := programmeTM2_step_cleanWorkLeft_cons M base tape symbol left
        workLeft workRight output hleft
      have hone := programmeTM2_one_step_in_time hstep
      let nextLeft := Function.update workLeft tape left
      have hnext : nextLeft tape = left := by
        simp [nextLeft, Function.update]
      rcases ih nextLeft hnext with ⟨hrest⟩
      refine ⟨?_⟩
      have hrun :=
        StateTransition.EvalsToInTime.trans
          (programmeTM2Machine M).step
          1 (left.length + 1)
          (programmeTM2CleanupCfg M (.cleanWorkLeft tape) base
            [] [] [] [] workLeft workRight output)
          (programmeTM2CleanupCfg M (.cleanWorkLeft tape) base
            [] [] [] [] nextLeft workRight output)
          (some (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
            [] [] [] [] (Function.update nextLeft tape []) workRight output))
          hone hrest
      simpa [nextLeft, Function.update, hleft, Nat.add_assoc] using hrun

/-- Clear one selected work-right stack and advance to the machine's next
work/emit mode. -/
theorem programmeTM2_cleanWorkRight_run (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (tape : Fin M.workTapeCount)
    (workLeft workRight : Fin M.workTapeCount → List M.Symbol)
    (output : List Bool) :
    Nonempty
      (StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
          [] [] [] [] workLeft workRight output)
        (some
          (programmeTM2CleanupCfg M
            (programmeTM2NextWorkOrEmit M tape base) base
            [] [] [] [] workLeft (Function.update workRight tape []) output))
        ((workRight tape).length + 1)) := by
  generalize hright : workRight tape = right
  induction right generalizing workRight with
  | nil =>
      have hnil : workRight tape = [] := hright
      have hone := programmeTM2_one_step_in_time
        (programmeTM2_step_cleanWorkRight_nil M base tape
          workLeft workRight output hnil)
      refine ⟨?_⟩
      simpa [hnil] using hone
  | cons symbol right ih =>
      have hstep := programmeTM2_step_cleanWorkRight_cons M base tape symbol right
        workLeft workRight output hright
      have hone := programmeTM2_one_step_in_time hstep
      let nextRight := Function.update workRight tape right
      have hnext : nextRight tape = right := by
        simp [nextRight, Function.update]
      rcases ih nextRight hnext with ⟨hrest⟩
      refine ⟨?_⟩
      have hrun :=
        StateTransition.EvalsToInTime.trans
          (programmeTM2Machine M).step
          1 (right.length + 1)
          (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
            [] [] [] [] workLeft workRight output)
          (programmeTM2CleanupCfg M (.cleanWorkRight tape) base
            [] [] [] [] workLeft nextRight output)
          (some (programmeTM2CleanupCfg M
            (programmeTM2NextWorkOrEmit M tape base) base
            [] [] [] [] workLeft (Function.update nextRight tape []) output))
          hone hrest
      simpa [nextRight, Function.update, hright, Nat.add_assoc] using hrun

#print axioms programmeTM2_step_cleanInputRight_nil
#print axioms programmeTM2_step_cleanWorkLeft_nil
#print axioms programmeTM2_step_cleanWorkRight_nil
#print axioms programmeTM2_cleanRaw_run
#print axioms programmeTM2_cleanTemp_run
#print axioms programmeTM2_cleanInputLeft_run
#print axioms programmeTM2_cleanInputRight_run
#print axioms programmeTM2_cleanWorkLeft_run
#print axioms programmeTM2_cleanWorkRight_run

/-- Canonical work-stack map after all tape indices below `i` have been cleared. -/
def programmeTM2ClearWorkBefore {M : ProgrammeMachine}
    (work : Fin M.workTapeCount → List M.Symbol) (i : Nat) :
    Fin M.workTapeCount → List M.Symbol :=
  fun tape => if tape.1 < i then [] else work tape

/-- Cleanup mode corresponding to the next work-tape index. -/
def programmeTM2WorkCleanupMode (M : ProgrammeMachine)
    (base : ProgrammeTM2State M) (i : Nat) :
    ProgrammeTM2Mode M.workTapeCount :=
  if h : i < M.workTapeCount then
    .cleanWorkLeft ⟨i, h⟩
  else
    .emit (programmeTM2TerminalResult M base)

/-- Clearing the current index advances the canonical cleared-prefix map. -/
theorem programmeTM2ClearWorkBefore_update_current
    {M : ProgrammeMachine}
    (work : Fin M.workTapeCount → List M.Symbol)
    (i : Nat) (hi : i < M.workTapeCount) :
    Function.update (programmeTM2ClearWorkBefore work i) ⟨i, hi⟩ [] =
      programmeTM2ClearWorkBefore work (i + 1) := by
  funext tape
  by_cases heq : tape = ⟨i, hi⟩
  · subst tape
    simp [programmeTM2ClearWorkBefore, Function.update]
  · have hval : tape.1 ≠ i := by
      intro h
      apply heq
      apply Fin.ext
      exact h
    simp [programmeTM2ClearWorkBefore, Function.update, heq]
    by_cases hlt : tape.1 < i <;> simp [hlt]
    · omega
    · by_cases hnext : tape.1 < i + 1
      · omega
      · simp [hnext]

/-- At an in-range index, the canonical work-cleanup mode is the left stack
for exactly that tape. -/
theorem programmeTM2WorkCleanupMode_inRange
    (M : ProgrammeMachine) (base : ProgrammeTM2State M)
    (i : Nat) (hi : i < M.workTapeCount) :
    programmeTM2WorkCleanupMode M base i = .cleanWorkLeft ⟨i, hi⟩ := by
  simp [programmeTM2WorkCleanupMode, hi]

/-- The machine's successor after one right-work blank pop is exactly the
canonical cleanup mode for the next index. -/
theorem programmeTM2NextWorkOrEmit_eq_mode
    (M : ProgrammeMachine) (base : ProgrammeTM2State M)
    (i : Nat) (hi : i < M.workTapeCount) :
    programmeTM2NextWorkOrEmit M ⟨i, hi⟩ base =
      programmeTM2WorkCleanupMode M base (i + 1) := by
  unfold programmeTM2NextWorkOrEmit programmeTM2WorkCleanupMode
  by_cases hnext : i + 1 < M.workTapeCount
  · simp [hnext]
  · simp [hnext]

/-- At the terminal index `workTapeCount`, all canonical work stacks are empty. -/
theorem programmeTM2ClearWorkBefore_all
    {M : ProgrammeMachine}
    (work : Fin M.workTapeCount → List M.Symbol) :
    programmeTM2ClearWorkBefore work M.workTapeCount = fun _ => [] := by
  funext tape
  simp [programmeTM2ClearWorkBefore, tape.isLt]

#print axioms programmeTM2ClearWorkBefore_update_current
#print axioms programmeTM2NextWorkOrEmit_eq_mode
#print axioms programmeTM2ClearWorkBefore_all
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

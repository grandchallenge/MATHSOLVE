import MathSolve.PNP.ProgrammeTM2RunTransfer
import MathSolve.PNP.ProgrammeTM2Cleanup

/-!
# Terminal cleanup composition for the reverse Programme-to-TM2 compiler

A represented terminal Programme configuration first enters cleanup mode, then
clears every auxiliary stack, emits exactly one Boolean, and halts.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

theorem programmeTM2_step_terminal_accept
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (haccept : source.state = M.accept) :
    (programmeTM2Machine M).step target =
      some
        (programmeTM2CleanupCfg M .cleanRaw target.var
          (target.stk .rawInput) (target.stk .inputTemp)
          (target.stk .inputLeft) (target.stk .inputRight)
          (fun tape => target.stk (.workLeft tape))
          (fun tape => target.stk (.workRight tape))
          (target.stk .output)) := by
  rcases target with ⟨label, var, stk⟩
  have hlabel : label = some (.run) := hrep.1
  subst label
  have hmode : var.mode = .run := hrep.2.1
  have hcontrol : var.control = M.accept := hrep.2.2.1.trans haccept
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux]
  simp [hcontrol]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · simp [programmeTM2CleanupCfg, hmode]
  · simp [programmeTM2CleanupCfg]
  · intro k
    cases k <;> rfl

theorem programmeTM2_step_terminal_reject
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (haccept : source.state ≠ M.accept)
    (hreject : source.state = M.reject) :
    (programmeTM2Machine M).step target =
      some
        (programmeTM2CleanupCfg M .cleanRaw target.var
          (target.stk .rawInput) (target.stk .inputTemp)
          (target.stk .inputLeft) (target.stk .inputRight)
          (fun tape => target.stk (.workLeft tape))
          (fun tape => target.stk (.workRight tape))
          (target.stk .output)) := by
  rcases target with ⟨label, var, stk⟩
  have hlabel : label = some (.run) := hrep.1
  subst label
  have hmode : var.mode = .run := hrep.2.1
  have hcontrol : var.control = M.reject := hrep.2.2.1.trans hreject
  have hreject_ne_accept : M.reject ≠ M.accept := Ne.symm M.accept_ne_reject
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, Turing.TM2.stepAux]
  simp [hcontrol, hreject_ne_accept]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · simp [programmeTM2CleanupCfg, hmode]
  · simp [programmeTM2CleanupCfg]
  · intro k
    cases k <;> rfl

def programmeTM2CleanupBudget (M : ProgrammeMachine)
    (inputLength spent : Nat) : Nat :=
  inputLength + 2 * spent + 6 +
    2 * M.workTapeCount * (spent + 1)

theorem programmeTM2_cleanup_terminal
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    {spent : Nat} (hrep : ProgrammeTM2BoundedRepresents M input source target spent)
    (hnone : M.step input source = none)
    (result : Bool) (hout : M.output source = some result) :
    Nonempty
      (StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        target
        (some (Turing.haltList (programmeTM2Machine M) [result]))
        (programmeTM2CleanupBudget M input.length spent)) := by
  have hterminal := programmeTerminal_of_step_none M input source hnone
  have hentry :
      (programmeTM2Machine M).step target =
        some
          (programmeTM2CleanupCfg M .cleanRaw target.var
            [] [] (target.stk .inputLeft) (target.stk .inputRight)
            (fun tape => target.stk (.workLeft tape))
            (fun tape => target.stk (.workRight tape)) []) := by
    rcases hterminal with haccept | hreject
    · simpa [hrep.raw_empty, hrep.temp_empty, hrep.output_empty] using
        programmeTM2_step_terminal_accept hrep.represents haccept
    · have haccept : source.state ≠ M.accept := by
        intro h
        exact M.accept_ne_reject (h.symm.trans hreject)
      simpa [hrep.raw_empty, hrep.temp_empty, hrep.output_empty] using
        programmeTM2_step_terminal_reject hrep.represents haccept hreject
  have hone := programmeTM2_one_step_in_time hentry
  rcases programmeTM2_cleanRaw_run M target.var
      [] [] (target.stk .inputLeft) (target.stk .inputRight)
      (fun tape => target.stk (.workLeft tape))
      (fun tape => target.stk (.workRight tape)) [] with ⟨hraw⟩
  rcases programmeTM2_cleanTemp_run M target.var
      [] (target.stk .inputLeft) (target.stk .inputRight)
      (fun tape => target.stk (.workLeft tape))
      (fun tape => target.stk (.workRight tape)) [] with ⟨htemp⟩
  rcases programmeTM2_cleanInputLeft_run M target.var
      (target.stk .inputLeft) (target.stk .inputRight)
      (fun tape => target.stk (.workLeft tape))
      (fun tape => target.stk (.workRight tape)) [] with ⟨hleftRaw⟩
  have hleft :=
    programmeTM2_evalsToInTime_mono hleftRaw
      (Nat.add_le_add_right hrep.inputLeft_bound 1)
  rcases programmeTM2_cleanInputRight_run M target.var
      (target.stk .inputRight)
      (fun tape => target.stk (.workLeft tape))
      (fun tape => target.stk (.workRight tape)) [] with ⟨hrightRaw⟩
  have hright :=
    programmeTM2_evalsToInTime_mono hrightRaw
      (Nat.add_le_add_right hrep.inputRight_bound 1)
  rcases programmeTM2_cleanWork_run M target.var spent
      (fun tape => target.stk (.workLeft tape))
      (fun tape => target.stk (.workRight tape)) []
      hrep.workLeft_bound hrep.workRight_bound with ⟨hwork⟩
  have hresult :
      programmeTM2TerminalResult M target.var = result :=
    programmeTM2_terminalResult_eq hrep.represents result hout
  have hemit :=
    programmeTM2_one_step_in_time
      (programmeTM2_step_emit_halt M target.var result)
  have h12 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step 1 1
      target
      (programmeTM2CleanupCfg M .cleanRaw target.var
        [] [] (target.stk .inputLeft) (target.stk .inputRight)
        (fun tape => target.stk (.workLeft tape))
        (fun tape => target.stk (.workRight tape)) [])
      (some
        (programmeTM2CleanupCfg M .cleanTemp target.var
          [] [] (target.stk .inputLeft) (target.stk .inputRight)
          (fun tape => target.stk (.workLeft tape))
          (fun tape => target.stk (.workRight tape)) []))
      hone hraw
  have h123 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step 2 1
      target
      (programmeTM2CleanupCfg M .cleanTemp target.var
        [] [] (target.stk .inputLeft) (target.stk .inputRight)
        (fun tape => target.stk (.workLeft tape))
        (fun tape => target.stk (.workRight tape)) [])
      (some
        (programmeTM2CleanupCfg M .cleanInputLeft target.var
          [] [] (target.stk .inputLeft) (target.stk .inputRight)
          (fun tape => target.stk (.workLeft tape))
          (fun tape => target.stk (.workRight tape)) []))
      (by simpa using h12) htemp
  have h1234 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step 3 (spent + 1)
      target
      (programmeTM2CleanupCfg M .cleanInputLeft target.var
        [] [] (target.stk .inputLeft) (target.stk .inputRight)
        (fun tape => target.stk (.workLeft tape))
        (fun tape => target.stk (.workRight tape)) [])
      (some
        (programmeTM2CleanupCfg M .cleanInputRight target.var
          [] [] [] (target.stk .inputRight)
          (fun tape => target.stk (.workLeft tape))
          (fun tape => target.stk (.workRight tape)) []))
      (by simpa using h123) hleft
  have h12345 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (spent + 4) (input.length + spent + 1)
      target
      (programmeTM2CleanupCfg M .cleanInputRight target.var
        [] [] [] (target.stk .inputRight)
        (fun tape => target.stk (.workLeft tape))
        (fun tape => target.stk (.workRight tape)) [])
      (some
        (programmeTM2CleanupCfg M
          (programmeTM2FirstWorkOrEmit M target.var) target.var
          [] [] [] []
          (fun tape => target.stk (.workLeft tape))
          (fun tape => target.stk (.workRight tape)) []))
      (by simpa [Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using h1234)
      hright
  have h12345' :
      StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        target
        (some
          (programmeTM2CleanupCfg M
            (programmeTM2FirstWorkOrEmit M target.var) target.var
            [] [] [] []
            (fun tape => target.stk (.workLeft tape))
            (fun tape => target.stk (.workRight tape)) []))
        (input.length + 2 * spent + 5) :=
    programmeTM2_evalsToInTime_mono h12345 (by omega)
  have h123456 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (input.length + 2 * spent + 5)
      (2 * M.workTapeCount * (spent + 1))
      target
      (programmeTM2CleanupCfg M
        (programmeTM2FirstWorkOrEmit M target.var) target.var
        [] [] [] []
        (fun tape => target.stk (.workLeft tape))
        (fun tape => target.stk (.workRight tape)) [])
      (some
        (programmeTM2CleanupCfg M
          (.emit (programmeTM2TerminalResult M target.var)) target.var
          [] [] [] [] (fun _ => []) (fun _ => []) []))
      h12345' hwork
  have h123456Raw := h123456
  rw [hresult] at h123456Raw
  have h123456' :
      StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        target
        (some
          (programmeTM2CleanupCfg M
            (.emit result) target.var
            [] [] [] [] (fun _ => []) (fun _ => []) []))
        (input.length + 2 * spent + 5 +
          2 * M.workTapeCount * (spent + 1)) :=
    programmeTM2_evalsToInTime_mono h123456Raw (by omega)
  have hall :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (input.length + 2 * spent + 5 +
        2 * M.workTapeCount * (spent + 1)) 1
      target
      (programmeTM2CleanupCfg M
        (.emit result) target.var
        [] [] [] [] (fun _ => []) (fun _ => []) [])
      (some (Turing.haltList (programmeTM2Machine M) [result]))
      h123456' hemit
  refine ⟨?_⟩
  apply programmeTM2_evalsToInTime_mono hall
  unfold programmeTM2CleanupBudget
  omega

#print axioms programmeTM2_step_terminal_accept
#print axioms programmeTM2_step_terminal_reject
#print axioms programmeTM2_cleanup_terminal

end

end MathSolve.PNP

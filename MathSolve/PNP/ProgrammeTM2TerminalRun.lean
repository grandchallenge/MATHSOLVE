import MathSolve.PNP.ProgrammeTM2Cleanup

/-!
# Terminal entry and complete canonical cleanup for the reverse compiler

A represented terminal Programme configuration enters cleanup in one counted
TM2 step.  Cleanup then clears every auxiliary stack and emits exactly the
Programme Boolean result in the canonical mathlib `haltList` shape.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Re-express an arbitrary reverse configuration as an explicit cleanup
configuration with the same local state and heterogeneous stacks. -/
def programmeTM2CleanupFromTarget (M : ProgrammeMachine)
    (mode : ProgrammeTM2Mode M.workTapeCount)
    (target : (programmeTM2Machine M).Cfg) :
    (programmeTM2Machine M).Cfg :=
  programmeTM2CleanupCfg M mode target.var
    (target.stk .rawInput)
    (target.stk .inputTemp)
    (target.stk .inputLeft)
    (target.stk .inputRight)
    (fun tape => target.stk (.workLeft tape))
    (fun tape => target.stk (.workRight tape))
    (target.stk .output)

/-- A represented Programme terminal enters raw-stack cleanup in one TM2 step. -/
theorem programmeTM2_step_enter_cleanup
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M}
    {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (hterminal : source.state = M.accept ∨ source.state = M.reject) :
    (programmeTM2Machine M).step target =
      some (programmeTM2CleanupFromTarget M .cleanRaw target) := by
  rcases target with ⟨label, state, stacks⟩
  change label = some (.run) at hrep
  rcases hrep with ⟨hlabel, hmode, hcontrol, hinput, hwork⟩
  subst label
  change state.mode = .run at hmode
  change state.control = source.state at hcontrol
  rcases hterminal with haccept | hreject
  · have hstate : state.control = M.accept := hcontrol.trans haccept
    simp only [Turing.FinTM2.step, Turing.TM2.step]
    simp [programmeTM2Machine, programmeTM2Program, Turing.TM2.stepAux,
      hstate, programmeTM2CleanupFromTarget, programmeTM2CleanupCfg,
      programmeTM2CleanupStacks]
    apply congrArg some
    apply programmeTM2Cfg_ext
    · rfl
    · cases state
      simp_all
    · intro k
      cases k <;> rfl
  · have hstate : state.control = M.reject := hcontrol.trans hreject
    have hnotAccept : state.control ≠ M.accept := by
      rw [hstate]
      exact Ne.symm M.accept_ne_reject
    simp only [Turing.FinTM2.step, Turing.TM2.step]
    simp [programmeTM2Machine, programmeTM2Program, Turing.TM2.stepAux,
      hstate, hnotAccept, programmeTM2CleanupFromTarget,
      programmeTM2CleanupCfg, programmeTM2CleanupStacks]
    apply congrArg some
    apply programmeTM2Cfg_ext
    · rfl
    · cases state
      simp_all
    · intro k
      cases k <;> rfl

/-- The reverse simulator's terminal Boolean agrees exactly with the Programme
output convention on a represented terminal configuration. -/
theorem programmeTM2_terminalResult_eq_output
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M}
    {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (result : Bool)
    (hout : M.output source = some result) :
    programmeTM2TerminalResult M target.var = result := by
  have hcontrol : target.var.control = source.state := hrep.2.2.1
  unfold programmeTM2TerminalResult
  rw [hcontrol]
  by_cases haccept : source.state = M.accept
  · have hresult : result = true := by
      simpa [ProgrammeMachine.output, haccept] using Option.some.inj hout
    subst result
    simp [haccept]
  · have hreject : source.state = M.reject := by
      by_contra hne
      simp [ProgrammeMachine.output, haccept, hne] at hout
    have hresult : result = false := by
      simpa [ProgrammeMachine.output, haccept, hreject] using Option.some.inj hout
    subst result
    simp [haccept]

/-- Exact additive cleanup budget after a simulated run of `steps` source
transitions. -/
def programmeTM2CleanupRuntime (M : ProgrammeMachine)
    (inputLength steps : Nat) : Nat :=
  1 + 1 + 1 + (steps + 1) + (inputLength + steps + 1) +
    2 * M.workTapeCount * (steps + 1) + 1

/-- A bounded represented Programme terminal is cleaned to the exact canonical
one-bit mathlib halt configuration within the explicit cleanup budget. -/
theorem programmeTM2_terminal_cleanup_run
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M}
    {target : (programmeTM2Machine M).Cfg}
    {steps : Nat} (result : Bool)
    (hrep : ProgrammeTM2BoundedRepresents M input source target steps)
    (hterminal : source.state = M.accept ∨ source.state = M.reject)
    (hout : M.output source = some result) :
    Nonempty
      (StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        target
        (some (Turing.haltList (programmeTM2Machine M) [result]))
        (programmeTM2CleanupRuntime M input.length steps)) := by
  let inputLeft := target.stk .inputLeft
  let inputRight := target.stk .inputRight
  let workLeft : Fin M.workTapeCount → List M.Symbol :=
    fun tape => target.stk (.workLeft tape)
  let workRight : Fin M.workTapeCount → List M.Symbol :=
    fun tape => target.stk (.workRight tape)
  have hentryRaw :=
    programmeTM2_step_enter_cleanup hrep.represents hterminal
  have hentry :
      (programmeTM2Machine M).step target =
        some
          (programmeTM2CleanupCfg M .cleanRaw target.var
            [] [] inputLeft inputRight workLeft workRight []) := by
    simpa [programmeTM2CleanupFromTarget, inputLeft, inputRight,
      workLeft, workRight, hrep.raw_empty, hrep.temp_empty,
      hrep.output_empty] using hentryRaw
  have hentryTime := programmeTM2_one_step_in_time hentry
  rcases programmeTM2_cleanRaw_run M target.var
      [] [] inputLeft inputRight workLeft workRight [] with ⟨hraw⟩
  rcases programmeTM2_cleanTemp_run M target.var
      [] inputLeft inputRight workLeft workRight [] with ⟨htemp⟩
  rcases programmeTM2_cleanInputLeft_run M target.var
      inputLeft inputRight workLeft workRight [] with ⟨hileftRaw⟩
  have hileft :
      StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanInputLeft target.var
          [] [] inputLeft inputRight workLeft workRight [])
        (some
          (programmeTM2CleanupCfg M .cleanInputRight target.var
            [] [] [] inputRight workLeft workRight []))
        (steps + 1) := by
    exact programmeTM2_evalsToInTime_mono hileftRaw
      (Nat.add_le_add_right hrep.inputLeft_bound 1)
  rcases programmeTM2_cleanInputRight_run M target.var
      inputRight workLeft workRight [] with ⟨hirightRaw⟩
  have hiright :
      StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M .cleanInputRight target.var
          [] [] [] inputRight workLeft workRight [])
        (some
          (programmeTM2CleanupCfg M
            (programmeTM2FirstWorkOrEmit M target.var) target.var
            [] [] [] [] workLeft workRight []))
        (input.length + steps + 1) := by
    have hbound := Nat.add_le_add_right hrep.inputRight_bound 1
    exact programmeTM2_evalsToInTime_mono hirightRaw (by
      simpa [Nat.add_assoc] using hbound)
  have hworkLeft : ∀ tape, (workLeft tape).length ≤ steps := by
    intro tape
    exact hrep.workLeft_bound tape
  have hworkRight : ∀ tape, (workRight tape).length ≤ steps := by
    intro tape
    exact hrep.workRight_bound tape
  rcases programmeTM2_cleanWork_run M target.var steps
      workLeft workRight [] hworkLeft hworkRight with ⟨hwork⟩
  have hresult :=
    programmeTM2_terminalResult_eq_output hrep.represents result hout
  have hemitRaw :=
    programmeTM2_step_emit_halt M target.var
      (programmeTM2TerminalResult M target.var)
  have hemit :
      (programmeTM2Machine M).step
        (programmeTM2CleanupCfg M (.emit (programmeTM2TerminalResult M target.var))
          target.var [] [] [] [] (fun _ => []) (fun _ => []) []) =
        some (Turing.haltList (programmeTM2Machine M) [result]) := by
    simpa [hresult] using hemitRaw
  have hemitTime := programmeTM2_one_step_in_time hemit
  have h01 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      1 1 target
      (programmeTM2CleanupCfg M .cleanRaw target.var
        [] [] inputLeft inputRight workLeft workRight [])
      (some
        (programmeTM2CleanupCfg M .cleanTemp target.var
          [] [] inputLeft inputRight workLeft workRight []))
      hentryTime hraw
  have h02 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      2 1 target
      (programmeTM2CleanupCfg M .cleanTemp target.var
        [] [] inputLeft inputRight workLeft workRight [])
      (some
        (programmeTM2CleanupCfg M .cleanInputLeft target.var
          [] [] inputLeft inputRight workLeft workRight []))
      (by simpa using h01) htemp
  have h03 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      3 (steps + 1) target
      (programmeTM2CleanupCfg M .cleanInputLeft target.var
        [] [] inputLeft inputRight workLeft workRight [])
      (some
        (programmeTM2CleanupCfg M .cleanInputRight target.var
          [] [] [] inputRight workLeft workRight []))
      (by simpa using h02) hileft
  have h04 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (3 + (steps + 1)) (input.length + steps + 1) target
      (programmeTM2CleanupCfg M .cleanInputRight target.var
        [] [] [] inputRight workLeft workRight [])
      (some
        (programmeTM2CleanupCfg M
          (programmeTM2FirstWorkOrEmit M target.var) target.var
          [] [] [] [] workLeft workRight []))
      h03 hiright
  have h05 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (3 + (steps + 1) + (input.length + steps + 1))
      (2 * M.workTapeCount * (steps + 1))
      target
      (programmeTM2CleanupCfg M
        (programmeTM2FirstWorkOrEmit M target.var) target.var
        [] [] [] [] workLeft workRight [])
      (some
        (programmeTM2CleanupCfg M
          (.emit (programmeTM2TerminalResult M target.var)) target.var
          [] [] [] [] (fun _ => []) (fun _ => []) []))
      h04 hwork
  have h06 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (3 + (steps + 1) + (input.length + steps + 1) +
        2 * M.workTapeCount * (steps + 1))
      1 target
      (programmeTM2CleanupCfg M
        (.emit (programmeTM2TerminalResult M target.var)) target.var
        [] [] [] [] (fun _ => []) (fun _ => []) [])
      (some (Turing.haltList (programmeTM2Machine M) [result]))
      h05 hemitTime
  refine ⟨?_⟩
  simpa [programmeTM2CleanupRuntime, Nat.add_assoc] using h06

#print axioms programmeTM2_step_enter_cleanup
#print axioms programmeTM2_terminalResult_eq_output
#print axioms programmeTM2_terminal_cleanup_run

end

end MathSolve.PNP

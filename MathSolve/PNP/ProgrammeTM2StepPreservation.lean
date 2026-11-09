import MathSolve.PNP.ProgrammeTM2TapeEffects
import MathSolve.PNP.ProgrammeStep

/-!
# Preservation of the Programme/TM2 representation across one run step

The source-side arithmetic is separated from the simulator stack algebra:
input motion reindexes offsets, and a work action writes the scanned cell then
moves the head.  The final theorem composes these facts with the operational
normal form.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Tape-level input movement corresponding to one Programme head action. -/
def programmeTM2ApplyInputTape
    (move : HeadMove) (T : Turing.Tape (Option Bool)) :
    Turing.Tape (Option Bool) :=
  match move with
  | .left => T.move Turing.Dir.left
  | .stay => T
  | .right => T.move Turing.Dir.right

/-- Pointwise input representation is preserved when both source and target
heads take the same move. -/
theorem programmeTM2ApplyInputTape_nth_afterAction
    {M : ProgrammeMachine} (input : List Bool)
    (source : ProgrammeConfig M)
    (action : ProgrammeAction M.State M.Symbol M.workTapeCount)
    (T : Turing.Tape (Option Bool))
    (hrel : ∀ offset : Int,
      T.nth offset =
        programmeInputRead input (source.inputHead + offset))
    (offset : Int) :
    (programmeTM2ApplyInputTape action.inputMove T).nth offset =
      programmeInputRead input
        ((source.afterAction action).inputHead + offset) := by
  cases hmove : action.inputMove with
  | left =>
      change (T.move Turing.Dir.left).nth offset =
        programmeInputRead input ((source.afterAction action).inputHead + offset)
      rw [Turing.Tape.move_left_nth]
      rw [hrel (offset - 1)]
      apply congrArg (programmeInputRead input)
      simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply]
      omega
  | stay =>
      change T.nth offset =
        programmeInputRead input ((source.afterAction action).inputHead + offset)
      rw [hrel offset]
      apply congrArg (programmeInputRead input)
      simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply]
  | right =>
      change (T.move Turing.Dir.right).nth offset =
        programmeInputRead input ((source.afterAction action).inputHead + offset)
      rw [Turing.Tape.move_right_nth]
      rw [hrel (offset + 1)]
      apply congrArg (programmeInputRead input)
      simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply]
      omega

/-- Pointwise work-tape representation is preserved by the exact
write-then-move action. -/
theorem programmeTM2ApplyWorkTape_nth_afterAction
    {M : ProgrammeMachine}
    (source : ProgrammeConfig M)
    (action : ProgrammeAction M.State M.Symbol M.workTapeCount)
    (tape : Fin M.workTapeCount)
    (T : Turing.Tape M.Symbol)
    (hrel : ∀ offset : Int,
      T.nth offset =
        source.work tape (source.workHead tape + offset))
    (offset : Int) :
    (programmeTM2ApplyWorkTape M action tape T).nth offset =
      (source.afterAction action).work tape
        ((source.afterAction action).workHead tape + offset) := by
  cases hmove : action.workMove tape with
  | left =>
      simp only [programmeTM2ApplyWorkTape, hmove,
        Turing.Tape.move_left_nth, Turing.Tape.write_nth]
      by_cases hz : offset - 1 = 0
      · rw [if_pos hz]
        have hcoord :
            (source.workHead tape - 1) + offset =
              source.workHead tape := by omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          hcoord, Function.update]
      · rw [if_neg hz]
        rw [hrel (offset - 1)]
        have hcoord :
            (source.workHead tape - 1) + offset ≠
              source.workHead tape := by omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          Function.update, hcoord]
        congr 1
        omega
  | stay =>
      simp only [programmeTM2ApplyWorkTape, hmove,
        Turing.Tape.write_nth]
      by_cases hz : offset = 0
      · subst offset
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          Function.update]
      · rw [if_neg hz]
        rw [hrel offset]
        have hcoord :
            source.workHead tape + offset ≠ source.workHead tape := by
          omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          Function.update, hcoord]
  | right =>
      simp only [programmeTM2ApplyWorkTape, hmove,
        Turing.Tape.move_right_nth, Turing.Tape.write_nth]
      by_cases hz : offset + 1 = 0
      · rw [if_pos hz]
        have hcoord :
            (source.workHead tape + 1) + offset =
              source.workHead tape := by omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          hcoord, Function.update]
      · rw [if_neg hz]
        rw [hrel (offset + 1)]
        have hcoord :
            (source.workHead tape + 1) + offset ≠
              source.workHead tape := by omega
        simp [ProgrammeConfig.afterAction, hmove, HeadMove.apply,
          Function.update, hcoord]
        congr 1
        omega

/-- The configuration-level input tape is definitionally the raw state/stack
view used by the operational lemmas. -/
theorem programmeTM2InputTape_eq_of
    (M : ProgrammeMachine) (cfg : (programmeTM2Machine M).Cfg) :
    programmeTM2InputTape M cfg =
      programmeTM2InputTapeOf M cfg.var cfg.stk := by
  rfl

/-- The configuration-level work tape is definitionally the raw state/stack
view used by the operational lemmas. -/
theorem programmeTM2WorkTape_eq_of
    (M : ProgrammeMachine) (cfg : (programmeTM2Machine M).Cfg)
    (tape : Fin M.workTapeCount) :
    programmeTM2WorkTape M cfg tape =
      programmeTM2WorkTapeOf M cfg.var cfg.stk tape := by
  rfl

/-- Committing a frozen action changes only mode/control, not tape views. -/
theorem programmeTM2InputTapeOf_commitAction
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) :
    programmeTM2InputTapeOf M (s.commitAction M) stk =
      programmeTM2InputTapeOf M s stk := by
  rfl

theorem programmeTM2WorkTapeOf_commitAction
    (M : ProgrammeMachine) (s : ProgrammeTM2State M)
    (stk : ProgrammeTM2Stacks M) (tape : Fin M.workTapeCount) :
    programmeTM2WorkTapeOf M (s.commitAction M) stk tape =
      programmeTM2WorkTapeOf M s stk tape := by
  rfl

/-- Input tape carried by the pure run core after all work updates. -/
theorem programmeTM2RunCore_inputTape
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    programmeTM2InputTapeOf M
        (programmeTM2RunCore M target).1
        (programmeTM2RunCore M target).2 =
      programmeTM2ApplyInputTape
        (ProgrammeTM2State.snapshotAction M (target.var.snapshot M)).inputMove
        (programmeTM2InputTapeOf M target.var target.stk) := by
  unfold programmeTM2RunCore
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  let workResult :=
    programmeTM2WorkPhase M (programmeTM2WorkTapes M)
      inputState inputStacks
  change programmeTM2InputTapeOf M (workResult.1.commitAction M) workResult.2 =
    programmeTM2ApplyInputTape
      (ProgrammeTM2State.snapshotAction M snapped).inputMove
      (programmeTM2InputTapeOf M target.var target.stk)
  rw [programmeTM2InputTapeOf_commitAction]
  rw [programmeTM2WorkPhase_inputTape]
  have hinput :=
    programmeTM2AfterInput_inputTape M snapped target.stk (by rfl)
  simpa [programmeTM2ApplyInputTape,
    programmeTM2InputTapeOf_snapshot] using hinput

/-- Every work tape carried by the pure run core is its old tape after the
frozen Programme write/head movement. -/
theorem programmeTM2RunCore_workTape
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg)
    (tape : Fin M.workTapeCount) :
    programmeTM2WorkTapeOf M
        (programmeTM2RunCore M target).1
        (programmeTM2RunCore M target).2 tape =
      programmeTM2ApplyWorkTape M
        (ProgrammeTM2State.snapshotAction M (target.var.snapshot M))
        tape (programmeTM2WorkTapeOf M target.var target.stk tape) := by
  unfold programmeTM2RunCore
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  let workResult :=
    programmeTM2WorkPhase M (programmeTM2WorkTapes M)
      inputState inputStacks
  change programmeTM2WorkTapeOf M (workResult.1.commitAction M)
      workResult.2 tape =
    programmeTM2ApplyWorkTape M
      (ProgrammeTM2State.snapshotAction M snapped) tape
      (programmeTM2WorkTapeOf M target.var target.stk tape)
  rw [programmeTM2WorkTapeOf_commitAction]
  rw [programmeTM2WorkPhase_finRange_workTape]
  rw [programmeTM2AfterInput_snapshotAction M snapped target.stk]
  rw [programmeTM2AfterInput_workTape M snapped target.stk tape]
  rfl

/-- The pure run core commits exactly the frozen action's next control. -/
theorem programmeTM2RunCore_control
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    (programmeTM2RunCore M target).1.control =
      (ProgrammeTM2State.snapshotAction M (target.var.snapshot M)).nextState := by
  unfold programmeTM2RunCore
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  let workResult :=
    programmeTM2WorkPhase M (programmeTM2WorkTapes M)
      inputState inputStacks
  change (workResult.1.commitAction M).control =
    (ProgrammeTM2State.snapshotAction M snapped).nextState
  change (ProgrammeTM2State.snapshotAction M workResult.1).nextState =
    (ProgrammeTM2State.snapshotAction M snapped).nextState
  rw [programmeTM2WorkPhase_snapshotAction]
  rw [programmeTM2AfterInput_snapshotAction M snapped target.stk]

/-- The pure run core always returns to run mode. -/
theorem programmeTM2RunCore_mode
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    (programmeTM2RunCore M target).1.mode = .run := by
  unfold programmeTM2RunCore
  rfl

/-- One represented nonterminal Programme action is represented again after the
single counted TM2 run step. -/
theorem programmeTM2RunStepTarget_represents_afterAction
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target) :
    ProgrammeTM2Represents M input
      (source.afterAction (M.actionAt input source))
      (programmeTM2RunStepTarget M target) := by
  have haction :
      ProgrammeTM2State.snapshotAction M (target.var.snapshot M) =
        M.actionAt input source := by
    rw [programmeTM2_snapshotAction_snapshot]
    simpa [ProgrammeMachine.actionAt] using hrep.action_eq
  rw [programmeTM2RunStepTarget_eq_core]
  refine ⟨rfl, programmeTM2RunCore_mode M target, ?_, ?_, ?_⟩
  · rw [programmeTM2RunCore_control]
    rw [haction]
    rfl
  · intro offset
    rw [programmeTM2InputTape_eq_of]
    rw [programmeTM2RunCore_inputTape]
    rw [haction]
    apply programmeTM2ApplyInputTape_nth_afterAction
      input source (M.actionAt input source)
    intro oldOffset
    have hold := hrep.2.2.2.1 oldOffset
    simpa [programmeTM2InputTape_eq_of] using hold
  · intro tape offset
    rw [programmeTM2WorkTape_eq_of]
    rw [programmeTM2RunCore_workTape]
    rw [haction]
    apply programmeTM2ApplyWorkTape_nth_afterAction
      source (M.actionAt input source) tape
    intro oldOffset
    have hold := hrep.2.2.2.2 tape oldOffset
    simpa [programmeTM2WorkTape_eq_of] using hold

/-- One nonterminal Programme step and one counted TM2 step preserve the
representation relation. -/
theorem programmeTM2_step_preserves
    {M : ProgrammeMachine} {input : List Bool}
    {source source' : ProgrammeConfig M}
    {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target)
    (hstep : M.step input source = some source') :
    ∃ target',
      ProgrammeTM2Represents M input source' target' ∧
      (programmeTM2Machine M).step target = some target' := by
  have haccept : source.state ≠ M.accept := by
    intro h
    rw [M.step_eq_none_of_accept input source h] at hstep
    contradiction
  have hreject : source.state ≠ M.reject := by
    intro h
    rw [M.step_eq_none_of_reject input source h] at hstep
    contradiction
  have hsource :
      source' = source.afterAction (M.actionAt input source) := by
    have h := M.step_eq_some_afterAction input source haccept hreject
    rw [h] at hstep
    exact Option.some.inj hstep |>.symm
  let target' := programmeTM2RunStepTarget M target
  refine ⟨target', ?_, ?_⟩
  · subst source'
    exact programmeTM2RunStepTarget_represents_afterAction hrep
  · exact programmeTM2_step_run_nonterminal hrep haccept hreject

#print axioms programmeTM2InputTape_eq_of
#print axioms programmeTM2RunCore_inputTape
#print axioms programmeTM2RunCore_workTape
#print axioms programmeTM2RunCore_control
#print axioms programmeTM2RunStepTarget_represents_afterAction
#print axioms programmeTM2_step_preserves

#print axioms programmeTM2ApplyInputTape_nth_afterAction
#print axioms programmeTM2ApplyWorkTape_nth_afterAction

end

end MathSolve.PNP

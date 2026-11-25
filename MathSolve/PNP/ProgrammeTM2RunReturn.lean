import MathSolve.PNP.ProgrammeTM2StepSimulation

/-!
# Structural run-label return for the genuine reverse FinTM2 statement

Every branch through one complete reverse-simulator Programme transition
returns to the run label.  The proof is by induction on genuine TM2 Stmt trees
and the recursively enumerated work-tape family; it does not inspect a fixed
example input or assume a previously represented post-state.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Every reachable terminal leaf of this finite statement tree is a goto
for the run label.  A halt leaf is excluded. -/
def programmeTM2ReturnsToRun (M : ProgrammeMachine) :
    ProgrammeTM2Stmt M → Prop
  | .push _ _ next => programmeTM2ReturnsToRun M next
  | .peek _ _ next => programmeTM2ReturnsToRun M next
  | .pop _ _ next => programmeTM2ReturnsToRun M next
  | .load _ next => programmeTM2ReturnsToRun M next
  | .branch _ left right =>
      programmeTM2ReturnsToRun M left ∧ programmeTM2ReturnsToRun M right
  | .goto jump => ∀ state, jump state = .run
  | .halt => False

/-- Structural interpreter theorem: every such tree ends at the run label. -/
theorem programmeTM2_returnsToRun_stepAux_label
    (M : ProgrammeMachine) (stmt : ProgrammeTM2Stmt M) :
    programmeTM2ReturnsToRun M stmt →
      ∀ (state : ProgrammeTM2State M)
        (stacks : ∀ k, List (programmeTM2StackAlphabet M k)),
        (Turing.TM2.stepAux stmt state stacks).l = some (.run) := by
  induction stmt with
  | push k f next ih =>
      intro h state stacks
      exact ih h state (Function.update stacks k (f state :: stacks k))
  | peek k f next ih =>
      intro h state stacks
      exact ih h (f state (stacks k).head?) stacks
  | pop k f next ih =>
      intro h state stacks
      exact ih h (f state (stacks k).head?)
        (Function.update stacks k (stacks k).tail)
  | load f next ih =>
      intro h state stacks
      exact ih h (f state) stacks
  | branch f left right ihLeft ihRight =>
      intro h state stacks
      cases hf : f state with
      | false =>
          simpa [Turing.TM2.stepAux, hf] using ihRight h.2 state stacks
      | true =>
          simpa [Turing.TM2.stepAux, hf] using ihLeft h.1 state stacks
  | goto f =>
      intro h state stacks
      simpa [Turing.TM2.stepAux] using congrArg some (h state)
  | halt =>
      intro h state stacks
      exact False.elim h

/-- A write-and-head-motion statement preserves the always-return-to-run property. -/
theorem programmeTM2_returnsToRun_workMove (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount) (next : ProgrammeTM2Stmt M)
    (hnext : programmeTM2ReturnsToRun M next) :
    programmeTM2ReturnsToRun M (programmeTM2ApplyWorkMove M tape next) := by
  simp [programmeTM2ReturnsToRun, programmeTM2ApplyWorkMove, hnext]

/-- Every finite work-tape traversal preserves the run-label return property. -/
theorem programmeTM2_returnsToRun_workMoves (M : ProgrammeMachine)
    (tapes : List (Fin M.workTapeCount)) :
    ∀ next : ProgrammeTM2Stmt M,
      programmeTM2ReturnsToRun M next →
      programmeTM2ReturnsToRun M (programmeTM2ApplyWorkMoves M tapes next) := by
  induction tapes with
  | nil =>
      intro next hnext
      simpa [programmeTM2ApplyWorkMoves] using hnext
  | cons tape rest ih =>
      intro next hnext
      exact programmeTM2_returnsToRun_workMove M tape _ (ih next hnext)

/-- A left/right/stay input move also preserves the same structural guarantee. -/
theorem programmeTM2_returnsToRun_inputMove (M : ProgrammeMachine)
    (next : ProgrammeTM2Stmt M)
    (hnext : programmeTM2ReturnsToRun M next) :
    programmeTM2ReturnsToRun M (programmeTM2ApplyInputMove M next) := by
  simp [programmeTM2ReturnsToRun, programmeTM2ApplyInputMove, hnext]

/-- The entire genuine work-tape iteration and input move has no non-run exit. -/
theorem programmeTM2_runTransition_returnsToRun (M : ProgrammeMachine) :
    programmeTM2ReturnsToRun M (programmeTM2RunTransition M) := by
  unfold programmeTM2RunTransition
  change programmeTM2ReturnsToRun M
    (programmeTM2ApplyInputMove M
      (programmeTM2ApplyWorkMoves M (programmeTM2WorkTapes M)
        (.load (ProgrammeTM2State.commitAction M) (.goto fun _ => .run))))
  apply programmeTM2_returnsToRun_inputMove
  apply programmeTM2_returnsToRun_workMoves
  simp [programmeTM2ReturnsToRun]

/-- The actual, unmodified TM2.stepAux of any simulated nonterminal transition
returns to run mode, for every finite control and all stack contents. -/
theorem programmeTM2_runStepTarget_label (M : ProgrammeMachine)
    (target : (programmeTM2Machine M).Cfg) :
    (programmeTM2RunStepTarget M target).l = some (.run) := by
  exact programmeTM2_returnsToRun_stepAux_label M
    (programmeTM2RunTransition M)
    (programmeTM2_runTransition_returnsToRun M) target.var target.stk

#print axioms programmeTM2_runTransition_returnsToRun
#print axioms programmeTM2_runStepTarget_label

end
end MathSolve.PNP

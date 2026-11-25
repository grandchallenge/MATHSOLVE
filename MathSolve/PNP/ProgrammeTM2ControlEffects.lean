import MathSolve.PNP.ProgrammeTM2RunReturn

/-!
# Actual control preservation through the reverse FinTM2 statement

The nested TM2 interpreter modifies the scanned tape symbols during one outer
step, but it must retain the frozen source transition until commitAction.  The
proof develops structural preservation rules for actual TM2 statements.
-/
namespace MathSolve.PNP
noncomputable section
open Turing

/-- Every continuation commits the frozen Programme action regardless of
current stacks. -/
def programmeTM2CommitsFrozen (M : ProgrammeMachine)
    (stmt : ProgrammeTM2Stmt M) : Prop :=
  ∀ (state : ProgrammeTM2State M)
    (stackFamily : ∀ k, List (programmeTM2StackAlphabet M k)),
    (Turing.TM2.stepAux stmt state stackFamily).var.mode = .run ∧
    (Turing.TM2.stepAux stmt state stackFamily).var.control =
      (state.snapshotAction M).nextState

/-- Actual final local load commits the frozen transition. -/
theorem programmeTM2_commitsFrozen_base (M : ProgrammeMachine) :
    programmeTM2CommitsFrozen M
      (.load (ProgrammeTM2State.commitAction M) (.goto fun _ => .run)) := by
  intro state stackFamily
  constructor <;> rfl

/-- Push changes stacks only. -/
theorem programmeTM2_commitsFrozen_push (M : ProgrammeMachine)
    (k : ProgrammeTM2Stack M.workTapeCount)
    (fn : ProgrammeTM2State M → programmeTM2StackAlphabet M k)
    (next : ProgrammeTM2Stmt M) (h : programmeTM2CommitsFrozen M next) :
    programmeTM2CommitsFrozen M (.push k fn next) := by
  intro state stackFamily
  exact h state (Function.update stackFamily k (fn state :: stackFamily k))

/-- Local load preserves the frozen action if its state transform does. -/
theorem programmeTM2_commitsFrozen_load (M : ProgrammeMachine)
    (fn : ProgrammeTM2State M → ProgrammeTM2State M)
    (next : ProgrammeTM2Stmt M)
    (hsnapshot : ∀ state, (fn state).snapshotAction M = state.snapshotAction M)
    (h : programmeTM2CommitsFrozen M next) :
    programmeTM2CommitsFrozen M (.load fn next) := by
  intro state stackFamily
  have hnext := h (fn state) stackFamily
  exact ⟨hnext.1, by simpa [hsnapshot state] using hnext.2⟩

/-- A pop changes one stack and possibly scanned symbol, not the snapshot. -/
theorem programmeTM2_commitsFrozen_pop (M : ProgrammeMachine)
    (k : ProgrammeTM2Stack M.workTapeCount)
    (fn : ProgrammeTM2State M → Option (programmeTM2StackAlphabet M k) →
      ProgrammeTM2State M)
    (next : ProgrammeTM2Stmt M)
    (hsnapshot : ∀ state symbol,
      (fn state symbol).snapshotAction M = state.snapshotAction M)
    (h : programmeTM2CommitsFrozen M next) :
    programmeTM2CommitsFrozen M (.pop k fn next) := by
  intro state stackFamily
  have hnext := h (fn state (stackFamily k).head?)
    (Function.update stackFamily k (stackFamily k).tail)
  exact ⟨hnext.1, by simpa [hsnapshot state (stackFamily k).head?] using hnext.2⟩

/-- Both branches have the same control-commit property. -/
theorem programmeTM2_commitsFrozen_branch (M : ProgrammeMachine)
    (predicate : ProgrammeTM2State M → Bool)
    (left right : ProgrammeTM2Stmt M)
    (hl : programmeTM2CommitsFrozen M left)
    (hr : programmeTM2CommitsFrozen M right) :
    programmeTM2CommitsFrozen M (.branch predicate left right) := by
  intro state stackFamily
  cases hp : predicate state with
  | true => simpa [Turing.TM2.stepAux, hp] using hl state stackFamily
  | false => simpa [Turing.TM2.stepAux, hp] using hr state stackFamily

/-- Updating any scanned work symbol leaves the frozen action unchanged. -/
theorem programmeTM2_setWorkSymbol_preserves_action (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount) (symbol : M.Symbol)
    (state : ProgrammeTM2State M) :
    (state.setWorkSymbol M tape symbol).snapshotAction M =
      state.snapshotAction M := by
  rfl

/-- Updating input scan position also leaves the frozen action unchanged. -/
theorem programmeTM2_setInputSymbol_preserves_action (M : ProgrammeMachine)
    (state : ProgrammeTM2State M) (symbol : Option Bool) :
    ({ state with inputSymbol := symbol } : ProgrammeTM2State M).snapshotAction M =
      state.snapshotAction M := by
  rfl

/-- The nested push/pop/write branches of one work-tape update preserve the
frozen control until the continuation commits it. -/
theorem programmeTM2_commitsFrozen_workMove (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount) (next : ProgrammeTM2Stmt M)
    (h : programmeTM2CommitsFrozen M next) :
    programmeTM2CommitsFrozen M (programmeTM2ApplyWorkMove M tape next) := by
  unfold programmeTM2ApplyWorkMove
  apply programmeTM2_commitsFrozen_branch
  · apply programmeTM2_commitsFrozen_push
    apply programmeTM2_commitsFrozen_pop
    · intro state symbol
      exact programmeTM2_setWorkSymbol_preserves_action M tape
        (symbol.getD M.blank) state
    · exact h
  · apply programmeTM2_commitsFrozen_branch
    · apply programmeTM2_commitsFrozen_push
      apply programmeTM2_commitsFrozen_pop
      · intro state symbol
        exact programmeTM2_setWorkSymbol_preserves_action M tape
          (symbol.getD M.blank) state
      · exact h
    · apply programmeTM2_commitsFrozen_load
      · intro state
        exact programmeTM2_setWorkSymbol_preserves_action M tape
          ((ProgrammeTM2State.snapshotAction M state).write tape) state
      · exact h

/-- Fold the work-tape result over any finite list of machine work tapes. -/
theorem programmeTM2_commitsFrozen_workMoves (M : ProgrammeMachine)
    (tapes : List (Fin M.workTapeCount)) :
    ∀ next : ProgrammeTM2Stmt M,
      programmeTM2CommitsFrozen M next →
      programmeTM2CommitsFrozen M (programmeTM2ApplyWorkMoves M tapes next) := by
  induction tapes with
  | nil => intro next h; simpa [programmeTM2ApplyWorkMoves] using h
  | cons tape rest ih =>
      intro next h
      exact programmeTM2_commitsFrozen_workMove M tape _ (ih next h)

/-- Input movement modifies only scanned input and adjacent stacks. -/
theorem programmeTM2_commitsFrozen_inputMove (M : ProgrammeMachine)
    (next : ProgrammeTM2Stmt M)
    (h : programmeTM2CommitsFrozen M next) :
    programmeTM2CommitsFrozen M (programmeTM2ApplyInputMove M next) := by
  unfold programmeTM2ApplyInputMove
  apply programmeTM2_commitsFrozen_branch
  · apply programmeTM2_commitsFrozen_push
    apply programmeTM2_commitsFrozen_pop
    · intro state symbol
      exact programmeTM2_setInputSymbol_preserves_action M state
        (symbol.getD none)
    · exact h
  · apply programmeTM2_commitsFrozen_branch
    · apply programmeTM2_commitsFrozen_push
      apply programmeTM2_commitsFrozen_pop
      · intro state symbol
        exact programmeTM2_setInputSymbol_preserves_action M state
          (symbol.getD none)
      · exact h
    · exact h

/-- The literal complete run statement commits the next state selected
from the *pre-step* control and input/work scanned symbols. -/
theorem programmeTM2_runTransition_control (M : ProgrammeMachine)
    (state : ProgrammeTM2State M)
    (stackFamily : ∀ k, List (programmeTM2StackAlphabet M k)) :
    (Turing.TM2.stepAux (programmeTM2RunTransition M)
      state stackFamily).var.mode = .run ∧
    (Turing.TM2.stepAux (programmeTM2RunTransition M)
      state stackFamily).var.control =
      (M.transition state.control state.inputSymbol state.workSymbol).nextState := by
  have hbase := programmeTM2_commitsFrozen_base M
  have hwork := programmeTM2_commitsFrozen_workMoves M
    (programmeTM2WorkTapes M) _ hbase
  have hinput := programmeTM2_commitsFrozen_inputMove M _ hwork
  -- Snapshot intentionally selects the *fresh* source observation; it need
  -- not preserve old snapshot fields.  Apply the established continuation
  -- property after taking this real snapshot.
  have hresult := hinput (state.snapshot M) stackFamily
  simpa [programmeTM2RunTransition, ProgrammeTM2State.snapshotAction,
    ProgrammeTM2State.snapshot] using hresult

/-- The next source control state is the actual FinTM2 step target's control,
for any represented nonterminal source configuration. -/
theorem programmeTM2_runStepTarget_control
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (hrep : ProgrammeTM2Represents M input source target) :
    (programmeTM2RunStepTarget M target).var.mode = .run ∧
    (programmeTM2RunStepTarget M target).var.control =
      (M.actionAt input source).nextState := by
  have hresult := programmeTM2_runTransition_control M target.var target.stk
  simpa [programmeTM2RunStepTarget, ProgrammeMachine.actionAt,
    hrep.action_eq] using hresult

#print axioms programmeTM2_runTransition_control
#print axioms programmeTM2_runStepTarget_control
end
end MathSolve.PNP

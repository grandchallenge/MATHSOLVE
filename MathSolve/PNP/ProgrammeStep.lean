import MathSolve.PNP.ProgrammeMachine

/-!
# Exact one-step facts for Programme machines

These lemmas expose one nonterminal `ProgrammeMachine.step` as the deterministic
configuration update induced by its transition action.  They are the local
operational facts used by the TM2 simulation proof.
-/

namespace MathSolve.PNP

/-- Apply one already-computed Programme action to a configuration. -/
def ProgrammeConfig.afterAction {M : ProgrammeMachine}
    (cfg : ProgrammeConfig M)
    (action : ProgrammeAction M.State M.Symbol M.workTapeCount) :
    ProgrammeConfig M where
  state := action.nextState
  inputHead := action.inputMove.apply cfg.inputHead
  workHead := fun tape => (action.workMove tape).apply (cfg.workHead tape)
  work := fun tape =>
    Function.update (cfg.work tape) (cfg.workHead tape) (action.write tape)

/-- The action selected at one Programme configuration on a fixed input. -/
def ProgrammeMachine.actionAt (M : ProgrammeMachine) (input : List Bool)
    (cfg : ProgrammeConfig M) :
    ProgrammeAction M.State M.Symbol M.workTapeCount :=
  M.transition cfg.state
    (programmeInputRead input cfg.inputHead) cfg.readWork

/-- Every nonterminal Programme configuration takes exactly its selected action. -/
theorem ProgrammeMachine.step_eq_some_afterAction
    (M : ProgrammeMachine) (input : List Bool) (cfg : ProgrammeConfig M)
    (haccept : cfg.state ≠ M.accept) (hreject : cfg.state ≠ M.reject) :
    M.step input cfg = some (cfg.afterAction (M.actionAt input cfg)) := by
  simp [ProgrammeMachine.step, ProgrammeMachine.actionAt,
    ProgrammeConfig.afterAction, haccept, hreject]

/-- An accepting Programme configuration is terminal. -/
theorem ProgrammeMachine.step_eq_none_of_accept
    (M : ProgrammeMachine) (input : List Bool) (cfg : ProgrammeConfig M)
    (haccept : cfg.state = M.accept) :
    M.step input cfg = none := by
  simp [ProgrammeMachine.step, haccept]

/-- A rejecting Programme configuration is terminal. -/
theorem ProgrammeMachine.step_eq_none_of_reject
    (M : ProgrammeMachine) (input : List Bool) (cfg : ProgrammeConfig M)
    (hreject : cfg.state = M.reject) :
    M.step input cfg = none := by
  simp [ProgrammeMachine.step, hreject]

/-- Any terminal Programme configuration has no successor. -/
theorem ProgrammeMachine.step_eq_none_of_terminal
    (M : ProgrammeMachine) (input : List Bool) (cfg : ProgrammeConfig M)
    (hterminal : cfg.state = M.accept ∨ cfg.state = M.reject) :
    M.step input cfg = none := by
  rcases hterminal with h | h
  · exact M.step_eq_none_of_accept input cfg h
  · exact M.step_eq_none_of_reject input cfg h

#print axioms ProgrammeMachine.step_eq_some_afterAction
#print axioms ProgrammeMachine.step_eq_none_of_accept
#print axioms ProgrammeMachine.step_eq_none_of_reject
#print axioms ProgrammeMachine.step_eq_none_of_terminal

end MathSolve.PNP

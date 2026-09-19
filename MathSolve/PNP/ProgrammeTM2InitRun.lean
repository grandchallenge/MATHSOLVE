import MathSolve.PNP.ProgrammeTM2Representation

/-!
# Exact initialization run for the Programme-to-TM2 simulator

The reverse simulator normalizes the raw FinTM2 input in two linear passes:
first onto a temporary stack, then back into left-to-right input-tape order.
A final pop loads the scanned input cell and enters run mode.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Initialization-local state with only the transient input symbol changed. -/
def programmeTM2InitState (M : ProgrammeMachine) (symbol : Option Bool) :
    ProgrammeTM2State M :=
  { programmeTM2InitialState M with inputSymbol := symbol }

/-- Closed-form stack family used during reverse-simulator initialization. -/
def programmeTM2InitStacks (M : ProgrammeMachine)
    (raw temp : List Bool) (right : List (Option Bool)) :
    ∀ k : ProgrammeTM2Stack M.workTapeCount,
      List (programmeTM2StackAlphabet M k)
  | .rawInput => raw
  | .inputTemp => temp
  | .inputLeft => []
  | .inputRight => right
  | .workLeft _ => []
  | .workRight _ => []
  | .output => []

/-- Closed-form configuration for the two initialization labels. -/
def programmeTM2InitCfg (M : ProgrammeMachine)
    (label : ProgrammeTM2Mode M.workTapeCount) (symbol : Option Bool)
    (raw temp : List Bool) (right : List (Option Bool)) :
    (programmeTM2Machine M).Cfg where
  l := some label
  var := programmeTM2InitState M symbol
  stk := programmeTM2InitStacks M raw temp right

/-- The native FinTM2 input configuration is the closed-form first-pass state. -/
theorem programmeTM2_initList_eq_cfg (M : ProgrammeMachine) (input : List Bool) :
    Turing.initList (programmeTM2Machine M) input =
      programmeTM2InitCfg M .initToTemp none input [] [] := by
  rfl

/-- One nonempty first-pass step pops raw input and pushes it onto the temporary stack. -/
theorem programmeTM2_step_initToTemp_cons (M : ProgrammeMachine)
    (symbol : Option Bool) (bit : Bool) (raw temp : List Bool)
    (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToTemp symbol (bit :: raw) temp right) =
      some
        (programmeTM2InitCfg M .initToTemp (some bit) raw (bit :: temp) right) := by
  rfl

/-- The first blank pop ends the first pass and clears the transient symbol. -/
theorem programmeTM2_step_initToTemp_nil (M : ProgrammeMachine)
    (symbol : Option Bool) (temp : List Bool) (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToTemp symbol [] temp right) =
      some (programmeTM2InitCfg M .initToRight none [] temp right) := by
  rfl

/-- One nonempty second-pass step restores a Boolean cell to the right-of-head stack. -/
theorem programmeTM2_step_initToRight_cons (M : ProgrammeMachine)
    (symbol : Option Bool) (bit : Bool) (temp : List Bool)
    (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToRight symbol [] (bit :: temp) right) =
      some
        (programmeTM2InitCfg M .initToRight (some bit) [] temp (some bit :: right)) := by
  rfl

/-- The second blank pop ends the restoration pass. -/
theorem programmeTM2_step_initToRight_nil (M : ProgrammeMachine)
    (symbol : Option Bool) (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToRight symbol [] [] right) =
      some (programmeTM2InitCfg M .initFinish none [] [] right) := by
  rfl

/-- The final initialization step loads the scanned input cell and enters run mode. -/
theorem programmeTM2_step_initFinish (M : ProgrammeMachine)
    (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initFinish none [] [] right) =
      some
        { l := some (.run)
          var :=
            { programmeTM2InitialState M with
                mode := .run
                inputSymbol := right.head?.getD none }
          stk := programmeTM2InitStacks M [] [] right.tail } := by
  rfl

/-- Any exact one-step transition yields a one-step bounded evaluation witness. -/
theorem programmeTM2_one_step_in_time
    {M : ProgrammeMachine} {a b : (programmeTM2Machine M).Cfg}
    (h : (programmeTM2Machine M).step a = some b) :
    StateTransition.EvalsToInTime
      (programmeTM2Machine M).step a (some b) 1 := by
  exact
    { steps := 1
      evals_in_steps := by simpa using h
      steps_le_m := le_rfl }

#print axioms programmeTM2_initList_eq_cfg
#print axioms programmeTM2_step_initToTemp_cons
#print axioms programmeTM2_step_initToTemp_nil
#print axioms programmeTM2_step_initToRight_cons
#print axioms programmeTM2_step_initToRight_nil
#print axioms programmeTM2_step_initFinish
#print axioms programmeTM2_one_step_in_time

end

end MathSolve.PNP

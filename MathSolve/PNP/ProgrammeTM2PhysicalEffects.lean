import MathSolve.PNP.ProgrammeTM2ControlEffects
import MathSolve.PNP.ProgrammeTM2TapeOps

/-!
# Direct evaluation of the physical reverse FinTM2 statement

Unlike the abstract all-cell `afterAction_of_concrete_tape_effects` bridge,
these equations are proved by reducing the genuine `TM2.stepAux` constructor
interpreter, including *both* stack mutations and the scanned symbol update.
This is the critical local physical-semantics part of an unconditional reverse
simulation theorem.
-/

namespace MathSolve.PNP
noncomputable section
open Turing

/-- One leftward physical work-tape instruction has the exact native two-stack
state effect; the equation holds with an arbitrary continuation `next`. -/
theorem programmeTM2_workMove_left_exec (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount) (next : ProgrammeTM2Stmt M)
    (state : ProgrammeTM2State M)
    (stackFamily : ∀ k, List (programmeTM2StackAlphabet M k))
    (hleft : (state.snapshotAction M).workMove tape = .left) :
    Turing.TM2.stepAux (programmeTM2ApplyWorkMove M tape next)
      state stackFamily =
    Turing.TM2.stepAux next
      (state.setWorkSymbol M tape
        ((stackFamily (.workLeft tape)).head?.getD M.blank))
      (Function.update
        (Function.update stackFamily (.workRight tape)
          ((state.snapshotAction M).write tape :: stackFamily (.workRight tape)))
        (.workLeft tape) (stackFamily (.workLeft tape)).tail) := by
  simp [programmeTM2ApplyWorkMove, Turing.TM2.stepAux, hleft,
    ProgrammeTM2State.snapshotAction]

/-- The symmetric rightward work-tape instruction, including writes to the
old head and a pop from the right-hand stack. -/
theorem programmeTM2_workMove_right_exec (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount) (next : ProgrammeTM2Stmt M)
    (state : ProgrammeTM2State M)
    (stackFamily : ∀ k, List (programmeTM2StackAlphabet M k))
    (hright : (state.snapshotAction M).workMove tape = .right) :
    Turing.TM2.stepAux (programmeTM2ApplyWorkMove M tape next)
      state stackFamily =
    Turing.TM2.stepAux next
      (state.setWorkSymbol M tape
        ((stackFamily (.workRight tape)).head?.getD M.blank))
      (Function.update
        (Function.update stackFamily (.workLeft tape)
          ((state.snapshotAction M).write tape :: stackFamily (.workLeft tape)))
        (.workRight tape) (stackFamily (.workRight tape)).tail) := by
  have hnotleft : (state.snapshotAction M).workMove tape ≠ .left := by
    rw [hright]
    decide
  simp [programmeTM2ApplyWorkMove, Turing.TM2.stepAux,
    hright, hnotleft]

/-- A stationary head writes only its currently scanned work symbol, changing
no stack cells. -/
theorem programmeTM2_workMove_stay_exec (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount) (next : ProgrammeTM2Stmt M)
    (state : ProgrammeTM2State M)
    (stackFamily : ∀ k, List (programmeTM2StackAlphabet M k))
    (hstay : (state.snapshotAction M).workMove tape = .stay) :
    Turing.TM2.stepAux (programmeTM2ApplyWorkMove M tape next)
      state stackFamily =
    Turing.TM2.stepAux next
      (state.setWorkSymbol M tape ((state.snapshotAction M).write tape))
      stackFamily := by
  have hnotleft : (state.snapshotAction M).workMove tape ≠ .left := by
    rw [hstay]
    decide
  have hnotright : (state.snapshotAction M).workMove tape ≠ .right := by
    rw [hstay]
    decide
  simp [programmeTM2ApplyWorkMove, Turing.TM2.stepAux,
    hstay, hnotleft, hnotright]

/-- Concrete leftward immutable-input movement.  The saved pre-step input
symbol is pushed right while a scanned cell is popped on the left. -/
theorem programmeTM2_inputMove_left_exec (M : ProgrammeMachine)
    (next : ProgrammeTM2Stmt M)
    (state : ProgrammeTM2State M)
    (stackFamily : ∀ k, List (programmeTM2StackAlphabet M k))
    (hleft : (state.snapshotAction M).inputMove = .left) :
    Turing.TM2.stepAux (programmeTM2ApplyInputMove M next)
      state stackFamily =
    Turing.TM2.stepAux next
      { state with inputSymbol := (stackFamily .inputLeft).head?.getD none }
      (Function.update
        (Function.update stackFamily .inputRight
          (state.snapshotInputSymbol :: stackFamily .inputRight))
        .inputLeft (stackFamily .inputLeft).tail) := by
  simp [programmeTM2ApplyInputMove, Turing.TM2.stepAux,
    hleft]

/-- Concrete rightward immutable-input movement with the symmetric stacks. -/
theorem programmeTM2_inputMove_right_exec (M : ProgrammeMachine)
    (next : ProgrammeTM2Stmt M)
    (state : ProgrammeTM2State M)
    (stackFamily : ∀ k, List (programmeTM2StackAlphabet M k))
    (hright : (state.snapshotAction M).inputMove = .right) :
    Turing.TM2.stepAux (programmeTM2ApplyInputMove M next)
      state stackFamily =
    Turing.TM2.stepAux next
      { state with inputSymbol := (stackFamily .inputRight).head?.getD none }
      (Function.update
        (Function.update stackFamily .inputLeft
          (state.snapshotInputSymbol :: stackFamily .inputLeft))
        .inputRight (stackFamily .inputRight).tail) := by
  have hnotleft : (state.snapshotAction M).inputMove ≠ .left := by
    rw [hright]
    decide
  simp [programmeTM2ApplyInputMove, Turing.TM2.stepAux,
    hright, hnotleft]

/-- With a stationary immutable-input head no input stack or scanned symbol
is modified by the actual statement interpreter. -/
theorem programmeTM2_inputMove_stay_exec (M : ProgrammeMachine)
    (next : ProgrammeTM2Stmt M)
    (state : ProgrammeTM2State M)
    (stackFamily : ∀ k, List (programmeTM2StackAlphabet M k))
    (hstay : (state.snapshotAction M).inputMove = .stay) :
    Turing.TM2.stepAux (programmeTM2ApplyInputMove M next)
      state stackFamily =
    Turing.TM2.stepAux next state stackFamily := by
  have hnotleft : (state.snapshotAction M).inputMove ≠ .left := by
    rw [hstay]
    decide
  have hnotright : (state.snapshotAction M).inputMove ≠ .right := by
    rw [hstay]
    decide
  simp [programmeTM2ApplyInputMove, Turing.TM2.stepAux,
    hstay, hnotleft, hnotright]

#print axioms programmeTM2_workMove_left_exec
#print axioms programmeTM2_workMove_right_exec
#print axioms programmeTM2_workMove_stay_exec
#print axioms programmeTM2_inputMove_left_exec
#print axioms programmeTM2_inputMove_right_exec
#print axioms programmeTM2_inputMove_stay_exec
end
end MathSolve.PNP

import MathSolve.PNP.ProgrammeTM2StepSimulation
import MathSolve.PNP.ProgrammeTM2InitRun

/-!
# Operational normal form for one reverse Programme-to-TM2 run step

The reverse simulator executes one complete Programme transition inside one
finite TM2 statement tree.  These lemmas expose that tree as pure updates of
the simulator local state and heterogeneous stack family.  No machine semantics
are changed here.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

abbrev ProgrammeTM2Stacks (M : ProgrammeMachine) :=
  ∀ k : ProgrammeTM2Stack M.workTapeCount,
    List (programmeTM2StackAlphabet M k)

/-- State after applying only the frozen Programme input-head movement. -/
def programmeTM2AfterInputState (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    ProgrammeTM2State M :=
  match (ProgrammeTM2State.snapshotAction M s).inputMove with
  | .left =>
      { s with inputSymbol := (stk .inputLeft).head?.getD none }
  | .stay => s
  | .right =>
      { s with inputSymbol := (stk .inputRight).head?.getD none }

/-- Stack family after applying only the frozen Programme input-head movement. -/
def programmeTM2AfterInputStacks (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    ProgrammeTM2Stacks M :=
  match (ProgrammeTM2State.snapshotAction M s).inputMove with
  | .left =>
      Function.update
        (Function.update stk .inputRight
          (s.snapshotInputSymbol :: stk .inputRight))
        .inputLeft (stk .inputLeft).tail
  | .stay => stk
  | .right =>
      Function.update
        (Function.update stk .inputLeft
          (s.snapshotInputSymbol :: stk .inputLeft))
        .inputRight (stk .inputRight).tail

/-- State after applying one frozen Programme work-tape write/head movement. -/
def programmeTM2AfterWorkState (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    ProgrammeTM2State M :=
  let action := ProgrammeTM2State.snapshotAction M s
  match action.workMove tape with
  | .left =>
      s.setWorkSymbol M tape
        ((stk (.workLeft tape)).head?.getD M.blank)
  | .stay =>
      s.setWorkSymbol M tape (action.write tape)
  | .right =>
      s.setWorkSymbol M tape
        ((stk (.workRight tape)).head?.getD M.blank)

/-- Stack family after applying one frozen Programme work-tape write/head movement. -/
def programmeTM2AfterWorkStacks (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    ProgrammeTM2Stacks M :=
  let action := ProgrammeTM2State.snapshotAction M s
  match action.workMove tape with
  | .left =>
      Function.update
        (Function.update stk (.workRight tape)
          (action.write tape :: stk (.workRight tape)))
        (.workLeft tape) (stk (.workLeft tape)).tail
  | .stay => stk
  | .right =>
      Function.update
        (Function.update stk (.workLeft tape)
          (action.write tape :: stk (.workLeft tape)))
        (.workRight tape) (stk (.workRight tape)).tail

/-- Pure execution of the finite family of work-tape updates. -/
def programmeTM2WorkPhase (M : ProgrammeMachine) :
    List (Fin M.workTapeCount) →
      ProgrammeTM2State M → ProgrammeTM2Stacks M →
      ProgrammeTM2State M × ProgrammeTM2Stacks M
  | [], s, stk => (s, stk)
  | tape :: rest, s, stk =>
      programmeTM2WorkPhase M rest
        (programmeTM2AfterWorkState M tape s stk)
        (programmeTM2AfterWorkStacks M tape s stk)

/-- Exact normal form of the input-movement statement wrapper. -/
theorem programmeTM2_stepAux_applyInputMove
    (M : ProgrammeMachine) (next : ProgrammeTM2Stmt M)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    Turing.TM2.stepAux (programmeTM2ApplyInputMove M next) s stk =
      Turing.TM2.stepAux next
        (programmeTM2AfterInputState M s stk)
        (programmeTM2AfterInputStacks M s stk) := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).inputMove <;>
    simp [programmeTM2ApplyInputMove, programmeTM2AfterInputState,
      programmeTM2AfterInputStacks, hmove, Turing.TM2.stepAux,
      Function.update]

/-- Exact normal form of one work-tape statement wrapper. -/
theorem programmeTM2_stepAux_applyWorkMove
    (M : ProgrammeMachine) (tape : Fin M.workTapeCount)
    (next : ProgrammeTM2Stmt M)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    Turing.TM2.stepAux (programmeTM2ApplyWorkMove M tape next) s stk =
      Turing.TM2.stepAux next
        (programmeTM2AfterWorkState M tape s stk)
        (programmeTM2AfterWorkStacks M tape s stk) := by
  cases hmove : (ProgrammeTM2State.snapshotAction M s).workMove tape <;>
    simp [programmeTM2ApplyWorkMove, programmeTM2AfterWorkState,
      programmeTM2AfterWorkStacks, hmove, Turing.TM2.stepAux,
      ProgrammeTM2State.setWorkSymbol, Function.update]

/-- Exact normal form of the complete finite work-tape sequence. -/
theorem programmeTM2_stepAux_applyWorkMoves
    (M : ProgrammeMachine) (tapes : List (Fin M.workTapeCount))
    (next : ProgrammeTM2Stmt M)
    (s : ProgrammeTM2State M) (stk : ProgrammeTM2Stacks M) :
    Turing.TM2.stepAux
        (programmeTM2ApplyWorkMoves M tapes next) s stk =
      let result := programmeTM2WorkPhase M tapes s stk
      Turing.TM2.stepAux next result.1 result.2 := by
  induction tapes generalizing s stk with
  | nil =>
      rfl
  | cons tape rest ih =>
      rw [show programmeTM2ApplyWorkMoves M (tape :: rest) next =
          programmeTM2ApplyWorkMove M tape
            (programmeTM2ApplyWorkMoves M rest next) by rfl]
      rw [programmeTM2_stepAux_applyWorkMove]
      simpa [programmeTM2WorkPhase] using
        ih (programmeTM2AfterWorkState M tape s stk)
          (programmeTM2AfterWorkStacks M tape s stk)

/-- Pure result of the entire run statement, before wrapping it as a TM2 cfg. -/
def programmeTM2RunCore (M : ProgrammeMachine)
    (target : (programmeTM2Machine M).Cfg) :
    ProgrammeTM2State M × ProgrammeTM2Stacks M :=
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  let workResult :=
    programmeTM2WorkPhase M (programmeTM2WorkTapes M)
      inputState inputStacks
  (workResult.1.commitAction M, workResult.2)

/-- The existing reverse run-transition tree has the exact pure normal form. -/
theorem programmeTM2RunStepTarget_eq_core
    (M : ProgrammeMachine) (target : (programmeTM2Machine M).Cfg) :
    programmeTM2RunStepTarget M target =
      { l := some (.run)
        var := (programmeTM2RunCore M target).1
        stk := (programmeTM2RunCore M target).2 } := by
  unfold programmeTM2RunStepTarget programmeTM2RunTransition
  simp only [Turing.TM2.stepAux]
  let snapped := target.var.snapshot M
  let inputState := programmeTM2AfterInputState M snapped target.stk
  let inputStacks := programmeTM2AfterInputStacks M snapped target.stk
  let workResult :=
    programmeTM2WorkPhase M (programmeTM2WorkTapes M)
      inputState inputStacks
  calc
    Turing.TM2.stepAux
        (programmeTM2ApplyInputMove M
          (programmeTM2ApplyWorkMoves M (programmeTM2WorkTapes M)
            (.load (ProgrammeTM2State.commitAction M)
              (.goto fun _ => .run))))
        snapped target.stk =
      Turing.TM2.stepAux
        (programmeTM2ApplyWorkMoves M (programmeTM2WorkTapes M)
          (.load (ProgrammeTM2State.commitAction M)
            (.goto fun _ => .run)))
        inputState inputStacks := by
          exact programmeTM2_stepAux_applyInputMove M _ snapped target.stk
    _ =
      Turing.TM2.stepAux
        (.load (ProgrammeTM2State.commitAction M)
          (.goto fun _ => .run))
        workResult.1 workResult.2 := by
          exact programmeTM2_stepAux_applyWorkMoves M
            (programmeTM2WorkTapes M) _ inputState inputStacks
    _ =
      { l := some (.run)
        var := workResult.1.commitAction M
        stk := workResult.2 } := by
          rfl
    _ =
      { l := some (.run)
        var := (programmeTM2RunCore M target).1
        stk := (programmeTM2RunCore M target).2 } := by
          rfl

#print axioms programmeTM2_stepAux_applyInputMove
#print axioms programmeTM2_stepAux_applyWorkMove
#print axioms programmeTM2_stepAux_applyWorkMoves
#print axioms programmeTM2RunStepTarget_eq_core

end

end MathSolve.PNP

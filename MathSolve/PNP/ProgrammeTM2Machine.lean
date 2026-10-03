import MathSolve.PNP.ProgrammeTM2Types

/-!
# Concrete Programme-to-TM2 machine

This file constructs the finite mathlib `FinTM2` used by the reverse half of
`PNP-BRIDGE-MODEL-001`.

Each two-way Programme tape is represented by two TM2 stacks plus the scanned
cell in finite local state.  One TM2 step executes the whole finite Programme
transition tree.  Input normalization and terminal cleanup are separate linear
phases.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

abbrev ProgrammeTM2Stmt (M : ProgrammeMachine) :=
  Turing.TM2.Stmt (programmeTM2StackAlphabet M)
    (ProgrammeTM2Mode M.workTapeCount) (ProgrammeTM2State M)

/-- Update one scanned work symbol in finite simulator state. -/
def ProgrammeTM2State.setWorkSymbol (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) (tape : Fin M.workTapeCount)
    (symbol : M.Symbol) : ProgrammeTM2State M :=
  { s with workSymbol := Function.update s.workSymbol tape symbol }

/-- Commit the frozen Programme action after all simulated head/tape updates. -/
def ProgrammeTM2State.commitAction (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) : ProgrammeTM2State M :=
  { s with
      mode := .run
      control := (ProgrammeTM2State.snapshotAction M s).nextState }

/-- Boolean result encoded by a terminal Programme control state. -/
def programmeTM2TerminalResult (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) : Bool :=
  decide (s.control = M.accept)

/-- Initialization pass 1: reverse the raw Boolean input onto a temporary stack. -/
def programmeTM2InitToTemp (M : ProgrammeMachine) : ProgrammeTM2Stmt M :=
  .pop .rawInput
    (fun s bit => { s with inputSymbol := bit })
    (.branch (fun s => s.inputSymbol.isSome)
      (.push .inputTemp (fun s => s.inputSymbol.getD false)
        (.goto fun _ => .initToTemp))
      (.goto fun _ => .initToRight))

/-- Initialization pass 2: restore input order onto the explicit right-of-head stack. -/
def programmeTM2InitToRight (M : ProgrammeMachine) : ProgrammeTM2Stmt M :=
  .pop .inputTemp
    (fun s bit => { s with inputSymbol := bit })
    (.branch (fun s => s.inputSymbol.isSome)
      (.push .inputRight (fun s => some (s.inputSymbol.getD false))
        (.goto fun _ => .initToRight))
      (.goto fun _ => .initFinish))

/-- Initialization pass 3: load input position zero into the scanned-cell state. -/
def programmeTM2InitFinish (M : ProgrammeMachine) : ProgrammeTM2Stmt M :=
  .pop .inputRight
    (fun s symbol =>
      { s with
          mode := .run
          inputSymbol := symbol.getD none })
    (.goto fun _ => .run)

/-- Apply the frozen Programme input-head movement. -/
def programmeTM2ApplyInputMove (M : ProgrammeMachine)
    (next : ProgrammeTM2Stmt M) : ProgrammeTM2Stmt M :=
  .branch
    (fun s => decide ((ProgrammeTM2State.snapshotAction M s).inputMove = .left))
    (.push .inputRight (fun s => s.snapshotInputSymbol)
      (.pop .inputLeft
        (fun s symbol => { s with inputSymbol := symbol.getD none })
        next))
    (.branch
      (fun s => decide ((ProgrammeTM2State.snapshotAction M s).inputMove = .right))
      (.push .inputLeft (fun s => s.snapshotInputSymbol)
        (.pop .inputRight
          (fun s symbol => { s with inputSymbol := symbol.getD none })
          next))
      next)

/-- Apply the frozen write/head move for one Programme work tape. -/
def programmeTM2ApplyWorkMove (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount) (next : ProgrammeTM2Stmt M) :
    ProgrammeTM2Stmt M :=
  .branch
    (fun s =>
      decide ((ProgrammeTM2State.snapshotAction M s).workMove tape = .left))
    (.push (.workRight tape)
      (fun s => (ProgrammeTM2State.snapshotAction M s).write tape)
      (.pop (.workLeft tape)
        (fun s symbol => s.setWorkSymbol M tape (symbol.getD M.blank))
        next))
    (.branch
      (fun s =>
        decide ((ProgrammeTM2State.snapshotAction M s).workMove tape = .right))
      (.push (.workLeft tape)
        (fun s => (ProgrammeTM2State.snapshotAction M s).write tape)
        (.pop (.workRight tape)
          (fun s symbol => s.setWorkSymbol M tape (symbol.getD M.blank))
          next))
      (.load
        (fun s =>
          s.setWorkSymbol M tape
            ((ProgrammeTM2State.snapshotAction M s).write tape))
        next))

/-- Sequence the finite family of work-tape updates inside one TM2 statement. -/
def programmeTM2ApplyWorkMoves (M : ProgrammeMachine) :
    List (Fin M.workTapeCount) → ProgrammeTM2Stmt M → ProgrammeTM2Stmt M
  | [], next => next
  | tape :: rest, next =>
      programmeTM2ApplyWorkMove M tape
        (programmeTM2ApplyWorkMoves M rest next)

/-- Canonical finite enumeration of Programme work tapes. -/
def programmeTM2WorkTapes (M : ProgrammeMachine) :
    List (Fin M.workTapeCount) :=
  List.finRange M.workTapeCount

/-- One complete nonterminal Programme transition, executed inside one TM2 step. -/
def programmeTM2RunTransition (M : ProgrammeMachine) : ProgrammeTM2Stmt M :=
  .load (ProgrammeTM2State.snapshot M)
    (programmeTM2ApplyInputMove M
      (programmeTM2ApplyWorkMoves M (programmeTM2WorkTapes M)
        (.load (ProgrammeTM2State.commitAction M)
          (.goto fun _ => .run))))

/-- First cleanup mode after the input-side stacks are empty. -/
def programmeTM2FirstWorkOrEmit (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) : ProgrammeTM2Mode M.workTapeCount :=
  if h : 0 < M.workTapeCount then
    .cleanWorkLeft ⟨0, h⟩
  else
    .emit (programmeTM2TerminalResult M s)

/-- Cleanup successor after finishing one right work stack. -/
def programmeTM2NextWorkOrEmit (M : ProgrammeMachine)
    (tape : Fin M.workTapeCount) (s : ProgrammeTM2State M) :
    ProgrammeTM2Mode M.workTapeCount :=
  if h : tape.1 + 1 < M.workTapeCount then
    .cleanWorkLeft ⟨tape.1 + 1, h⟩
  else
    .emit (programmeTM2TerminalResult M s)

/-- Total reverse-simulator program. -/
def programmeTM2Program (M : ProgrammeMachine) :
    ProgrammeTM2Mode M.workTapeCount → ProgrammeTM2Stmt M
  | .initToTemp => programmeTM2InitToTemp M
  | .initToRight => programmeTM2InitToRight M
  | .initFinish => programmeTM2InitFinish M
  | .run =>
      .branch (fun s => decide (s.control = M.accept))
        (.load (fun s => { s with mode := .cleanRaw })
          (.goto fun _ => .cleanRaw))
        (.branch (fun s => decide (s.control = M.reject))
          (.load (fun s => { s with mode := .cleanRaw })
            (.goto fun _ => .cleanRaw))
          (programmeTM2RunTransition M))
  | .cleanRaw =>
      .pop .rawInput
        (fun s symbol =>
          { s with
              mode := match symbol with
                | none => .cleanTemp
                | some _ => .cleanRaw })
        (.goto fun s => s.mode)
  | .cleanTemp =>
      .pop .inputTemp
        (fun s symbol =>
          { s with
              mode := match symbol with
                | none => .cleanInputLeft
                | some _ => .cleanTemp })
        (.goto fun s => s.mode)
  | .cleanInputLeft =>
      .pop .inputLeft
        (fun s symbol =>
          { s with
              mode := match symbol with
                | none => .cleanInputRight
                | some _ => .cleanInputLeft })
        (.goto fun s => s.mode)
  | .cleanInputRight =>
      .pop .inputRight
        (fun s symbol =>
          { s with
              mode := match symbol with
                | none => programmeTM2FirstWorkOrEmit M s
                | some _ => .cleanInputRight })
        (.goto fun s => s.mode)
  | .cleanWorkLeft tape =>
      .pop (.workLeft tape)
        (fun s symbol =>
          { s with
              mode := match symbol with
                | none => .cleanWorkRight tape
                | some _ => .cleanWorkLeft tape })
        (.goto fun s => s.mode)
  | .cleanWorkRight tape =>
      .pop (.workRight tape)
        (fun s symbol =>
          { s with
              mode := match symbol with
                | none => programmeTM2NextWorkOrEmit M tape s
                | some _ => .cleanWorkRight tape })
        (.goto fun s => s.mode)
  | .emit result =>
      .load (fun _ => programmeTM2InitialState M)
        (.push .output (fun _ => result) .halt)

/-- Concrete finite TM2 that simulates one locked Programme machine. -/
def programmeTM2Machine (M : ProgrammeMachine) : Turing.FinTM2 where
  K := ProgrammeTM2Stack M.workTapeCount
  k₀ := .rawInput
  k₁ := .output
  Γ := programmeTM2StackAlphabet M
  Λ := ProgrammeTM2Mode M.workTapeCount
  main := .initToTemp
  σ := ProgrammeTM2State M
  initialState := programmeTM2InitialState M
  m := programmeTM2Program M

/-- Boolean input/output alphabet equivalences for the concrete reverse machine. -/
def programmeTM2Aux (M : ProgrammeMachine) : Turing.TM2ComputableAux Bool Bool where
  tm := programmeTM2Machine M
  inputAlphabet := Equiv.refl Bool
  outputAlphabet := Equiv.refl Bool

#print axioms programmeTM2Machine
#print axioms programmeTM2Aux

end

end MathSolve.PNP

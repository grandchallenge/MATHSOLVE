import MathSolve.PNP.ModelBridge
import Mathlib.Tactic

/-!
# Programme-to-TM2 simulator finite types

This file fixes only the finite carrier types for the reverse machine-model
compiler.  It does not yet define a transition program or claim a simulation.

The reverse representation uses two stacks per two-way tape.  The currently
scanned input/work symbols live in finite TM2 local state; left/right stacks
store the cells on either side.  A separate raw-input and temporary stack
support linear initialization from the pinned FinTM2 input convention.
-/

namespace MathSolve.PNP

noncomputable section

/-- Heterogeneous TM2 stacks used by the reverse Programme simulator. -/
inductive ProgrammeTM2Stack (workTapeCount : Nat) where
  | rawInput
  | inputTemp
  | inputLeft
  | inputRight
  | workLeft (tape : Fin workTapeCount)
  | workRight (tape : Fin workTapeCount)
  | output
  deriving DecidableEq, Fintype, Repr

/-- Stack alphabet of the reverse simulator.

The raw input/output stacks remain Boolean so the bundled FinTM2 can expose the
identity Boolean input/output alphabet.  Auxiliary input stacks use
`Option Bool` so blank displacement is represented explicitly. -/
def programmeTM2StackAlphabet (M : ProgrammeMachine) :
    ProgrammeTM2Stack M.workTapeCount → Type
  | .rawInput => Bool
  | .inputTemp => Bool
  | .inputLeft => Option Bool
  | .inputRight => Option Bool
  | .workLeft _ => M.Symbol
  | .workRight _ => M.Symbol
  | .output => Bool

noncomputable instance programmeTM2StackAlphabetFintype
    (M : ProgrammeMachine) (k : ProgrammeTM2Stack M.workTapeCount) :
    Fintype (programmeTM2StackAlphabet M k) := by
  cases k <;> simp [programmeTM2StackAlphabet] <;> infer_instance

noncomputable instance programmeTM2StackAlphabetDecidableEq
    (M : ProgrammeMachine) (k : ProgrammeTM2Stack M.workTapeCount) :
    DecidableEq (programmeTM2StackAlphabet M k) :=
  Classical.decEq _

/-- Control phase of the reverse simulator.

Cleanup labels are represented in local state first; the concrete finite TM2
program may later split these into labels if that gives a simpler termination
proof. -/
inductive ProgrammeTM2Mode (workTapeCount : Nat) where
  | initToTemp
  | initToRight
  | initFinish
  | run
  | cleanRaw
  | cleanTemp
  | cleanInputLeft
  | cleanInputRight
  | cleanWorkLeft (tape : Fin workTapeCount)
  | cleanWorkRight (tape : Fin workTapeCount)
  | emit (result : Bool)
  deriving DecidableEq, Fintype, Repr

/-- Finite local state of the reverse simulator.

The `snapshot*` fields freeze the Programme configuration observed at the
start of one simulated transition.  This lets the finite TM2 statement tree
recompute every component of `M.transition` while mutating the next scanned
symbols, without storing a function-valued `ProgrammeAction` in state. -/
structure ProgrammeTM2State (M : ProgrammeMachine) where
  mode : ProgrammeTM2Mode M.workTapeCount
  control : M.State
  inputSymbol : Option Bool
  workSymbol : Fin M.workTapeCount → M.Symbol
  snapshotControl : M.State
  snapshotInputSymbol : Option Bool
  snapshotWorkSymbol : Fin M.workTapeCount → M.Symbol

noncomputable instance programmeTM2StateFintype (M : ProgrammeMachine) :
    Fintype (ProgrammeTM2State M) := by
  classical
  let e :
      ProgrammeTM2State M ≃
        ProgrammeTM2Mode M.workTapeCount ×
        M.State × Option Bool ×
        (Fin M.workTapeCount → M.Symbol) ×
        M.State × Option Bool ×
        (Fin M.workTapeCount → M.Symbol) :=
    { toFun := fun s =>
        (s.mode, s.control, s.inputSymbol, s.workSymbol,
          s.snapshotControl, s.snapshotInputSymbol, s.snapshotWorkSymbol)
      invFun := fun s =>
        { mode := s.1
          control := s.2.1
          inputSymbol := s.2.2.1
          workSymbol := s.2.2.2.1
          snapshotControl := s.2.2.2.2.1
          snapshotInputSymbol := s.2.2.2.2.2.1
          snapshotWorkSymbol := s.2.2.2.2.2.2 }
      left_inv := by intro s; cases s; rfl
      right_inv := by intro s; rcases s with ⟨a,b,c,d,e,f,g⟩; rfl }
  exact Fintype.ofEquiv _ e.symm

noncomputable instance programmeTM2StateDecidableEq (M : ProgrammeMachine) :
    DecidableEq (ProgrammeTM2State M) :=
  Classical.decEq _

/-- Canonical local state before reverse-simulator initialization starts. -/
def programmeTM2InitialState (M : ProgrammeMachine) : ProgrammeTM2State M where
  mode := .initToTemp
  control := M.start
  inputSymbol := none
  workSymbol := fun _ => M.blank
  snapshotControl := M.start
  snapshotInputSymbol := none
  snapshotWorkSymbol := fun _ => M.blank

/-- Freeze the current simulated Programme observation before applying one
Programme transition. -/
def ProgrammeTM2State.snapshot (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) : ProgrammeTM2State M :=
  { s with
    snapshotControl := s.control
    snapshotInputSymbol := s.inputSymbol
    snapshotWorkSymbol := s.workSymbol }

/-- The exact Programme action selected from the frozen observation. -/
def ProgrammeTM2State.snapshotAction (M : ProgrammeMachine)
    (s : ProgrammeTM2State M) :
    ProgrammeAction M.State M.Symbol M.workTapeCount :=
  M.transition s.snapshotControl s.snapshotInputSymbol s.snapshotWorkSymbol

#print axioms programmeTM2StateFintype
#print axioms programmeTM2StateDecidableEq

end

end MathSolve.PNP

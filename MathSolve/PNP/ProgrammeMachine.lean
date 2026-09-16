import MathSolve.PNP.PolyBoundBridge
import Mathlib

/-!
# PNP locked Programme deterministic multitape machine

This file fixes a native Lean target for the machine model named by the protected
P-versus-NP machine-and-encoding lock.

The concrete standard variant is:

* one read-only two-way input tape over `Option Bool`, where `none` is blank;
* finitely many two-way work tapes over one finite alphabet with a distinguished blank;
* finite deterministic control;
* one transition reads the input head and all work heads, writes all work heads,
  moves every head by at most one cell, and changes control state;
* accepting and rejecting control states are terminal;
* one transition application is one Programme cost unit;
* every work tape is initially blank and every head starts at integer position zero.

The input carrier remains exactly `List Bool`. Extending the input tape by blank
cells does not alter encoded input length, which remains `input.length`.

Runtime uses the same `Turing.EvalsToInTime` step counter used by the pinned
`FinTM2` interface. This keeps the later simulation theorem about machine steps,
not about a second ad-hoc evaluator.

This file defines the target and generic polynomial-time decider interface. It
does not by itself claim equivalence to mathlib `FinTM2`; that is the separate
simulation obligation in `PNP-BRIDGE-MODEL-001`.
-/

namespace MathSolve.PNP

/-- One-cell head motion for the locked Programme machine. -/
inductive HeadMove where
  | left
  | stay
  | right
  deriving DecidableEq, Repr

/-- Apply one head motion to a two-way integer tape coordinate. -/
def HeadMove.apply : HeadMove → Int → Int
  | .left, p => p - 1
  | .stay, p => p
  | .right, p => p + 1

/-- The result of one deterministic Programme transition. -/
structure ProgrammeAction (State Symbol : Type) (workTapeCount : Nat) where
  nextState : State
  inputMove : HeadMove
  write : Fin workTapeCount → Symbol
  workMove : Fin workTapeCount → HeadMove

/--
A finite deterministic Programme machine with a read-only binary input tape and
finitely many mutable work tapes.
-/
structure ProgrammeMachine where
  State : Type
  [stateFintype : Fintype State]
  [stateDecidableEq : DecidableEq State]
  Symbol : Type
  [symbolFintype : Fintype Symbol]
  [symbolDecidableEq : DecidableEq Symbol]
  blank : Symbol
  workTapeCount : Nat
  start : State
  accept : State
  reject : State
  accept_ne_reject : accept ≠ reject
  transition :
    State → Option Bool → (Fin workTapeCount → Symbol) →
      ProgrammeAction State Symbol workTapeCount

attribute [instance] ProgrammeMachine.stateFintype
attribute [instance] ProgrammeMachine.stateDecidableEq
attribute [instance] ProgrammeMachine.symbolFintype
attribute [instance] ProgrammeMachine.symbolDecidableEq

/-- Operational configuration of a locked Programme machine. -/
structure ProgrammeConfig (M : ProgrammeMachine) where
  state : M.State
  inputHead : Int
  workHead : Fin M.workTapeCount → Int
  work : Fin M.workTapeCount → Int → M.Symbol

/-- Read the immutable binary input tape; every cell outside the finite input is blank. -/
def programmeInputRead (input : List Bool) (position : Int) : Option Bool :=
  if h : 0 ≤ position then input.get? position.toNat else none

/-- Initial Programme configuration for an exact finite binary input. -/
def ProgrammeMachine.init (M : ProgrammeMachine) (input : List Bool) : ProgrammeConfig M where
  state := M.start
  inputHead := 0
  workHead := fun _ => 0
  work := fun _ _ => M.blank

/-- Read all mutable work-tape head cells. -/
def ProgrammeConfig.readWork {M : ProgrammeMachine} (cfg : ProgrammeConfig M) :
    Fin M.workTapeCount → M.Symbol :=
  fun tape => cfg.work tape (cfg.workHead tape)

/-- Boolean output convention of a terminal Programme configuration. -/
def ProgrammeMachine.output (M : ProgrammeMachine) (cfg : ProgrammeConfig M) : Option Bool :=
  if cfg.state = M.accept then some true
  else if cfg.state = M.reject then some false
  else none

/-- Accept and reject are the only terminal control states. -/
def ProgrammeMachine.isTerminal (M : ProgrammeMachine) (state : M.State) : Bool :=
  decide (state = M.accept ∨ state = M.reject)

/-- One locked Programme transition. Terminal configurations have no successor. -/
def ProgrammeMachine.step (M : ProgrammeMachine) (input : List Bool) :
    ProgrammeConfig M → Option (ProgrammeConfig M)
  | cfg =>
      if hterm : cfg.state = M.accept ∨ cfg.state = M.reject then none
      else
        let action := M.transition cfg.state
          (programmeInputRead input cfg.inputHead) cfg.readWork
        some {
          state := action.nextState
          inputHead := action.inputMove.apply cfg.inputHead
          workHead := fun tape => (action.workMove tape).apply (cfg.workHead tape)
          work := fun tape =>
            Function.update (cfg.work tape) (cfg.workHead tape) (action.write tape)
        }

/--
`RunsInTime M input result bound` means that the exact Programme transition
relation reaches an accepting/rejecting terminal configuration with `result` in
at most `bound` transition applications. The quantitative witness is mathlib's
`Turing.EvalsToInTime`, matching the imported TM2 step-accounting interface.
-/
def ProgrammeMachine.RunsInTime (M : ProgrammeMachine) (input : List Bool)
    (result : Bool) (bound : Nat) : Prop :=
  ∃ cfg : ProgrammeConfig M,
    Turing.EvalsToInTime (M.step input) (M.init input) (some cfg) bound ∧
    M.step input cfg = none ∧
    M.output cfg = some result

/-- A machine-specific runtime majorant and total-correctness witness for a decision function. -/
structure ProgrammeDecider (decision : List Bool → Bool) where
  machine : ProgrammeMachine
  runtime : BinaryRuntimeCost
  outputs : ∀ input, machine.RunsInTime input (decision input) (runtime input)

/-- The protected Programme polynomial-time class presentation on Boolean decision functions. -/
def ProgrammeComputableInPolyTime (decision : List Bool → Bool) : Prop :=
  ∃ decider : ProgrammeDecider decision, ProgrammePolynomialBound decider.runtime

/-- Uniformity is structural: one finite Programme machine witnesses every input length. -/
theorem programmePolyTime_uniform {decision : List Bool → Bool}
    (h : ProgrammeComputableInPolyTime decision) :
    ∃ M : ProgrammeMachine, ∀ input, ∃ bound,
      M.RunsInTime input (decision input) bound := by
  rcases h with ⟨decider, _⟩
  exact ⟨decider.machine, fun input => ⟨decider.runtime input, decider.outputs input⟩⟩

/-- A reached accepting state cannot simultaneously be the rejecting state. -/
theorem ProgrammeMachine.accept_not_reject (M : ProgrammeMachine) :
    M.accept ≠ M.reject :=
  M.accept_ne_reject

#print axioms programmePolyTime_uniform
#print axioms ProgrammeMachine.accept_not_reject

end MathSolve.PNP

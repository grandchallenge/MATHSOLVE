import MathSolve.PNP.ProgrammeTM2Machine

/-!
# Representation invariant for the reverse Programme-to-TM2 simulator

The reverse simulator stores each two-way Programme tape as two finite TM2
stacks plus the currently scanned symbol in finite local state.  These
definitions expose that storage as mathlib `Tape` objects, so head moves and
writes can be proved with the standard `Tape.move_*_nth` and
`Tape.write_nth` lemmas.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- The Programme blank gives its finite work alphabet a canonical tape blank. -/
instance programmeMachineSymbolInhabited (M : ProgrammeMachine) :
    Inhabited M.Symbol :=
  ⟨M.blank⟩

/-- Two reverse-simulator input stacks plus the scanned symbol, viewed as one
two-way tape. -/
def programmeTM2InputTape (M : ProgrammeMachine)
    (cfg : (programmeTM2Machine M).Cfg) : Turing.Tape (Option Bool) where
  head := cfg.var.inputSymbol
  left := Turing.ListBlank.mk (cfg.stk (.inputLeft))
  right := Turing.ListBlank.mk (cfg.stk (.inputRight))

/-- The two reverse-simulator stacks for one Programme work tape plus its
scanned symbol, viewed as one two-way tape. -/
def programmeTM2WorkTape (M : ProgrammeMachine)
    (cfg : (programmeTM2Machine M).Cfg) (tape : Fin M.workTapeCount) :
    Turing.Tape M.Symbol where
  head := cfg.var.workSymbol tape
  left := Turing.ListBlank.mk (cfg.stk (.workLeft tape))
  right := Turing.ListBlank.mk (cfg.stk (.workRight tape))

/-- A run-mode reverse-simulator configuration represents a Programme
configuration when all tape cells agree relative to the Programme head
coordinates. -/
def ProgrammeTM2Represents (M : ProgrammeMachine) (input : List Bool)
    (source : ProgrammeConfig M) (target : (programmeTM2Machine M).Cfg) : Prop :=
  target.l = some (.run) ∧
  target.var.mode = .run ∧
  target.var.control = source.state ∧
  (∀ offset : Int,
    (programmeTM2InputTape M target).nth offset =
      programmeInputRead input (source.inputHead + offset)) ∧
  (∀ tape : Fin M.workTapeCount, ∀ offset : Int,
    (programmeTM2WorkTape M target tape).nth offset =
      source.work tape (source.workHead tape + offset))

/-- The scanned input symbol of a represented target is exactly the source
input read. -/
theorem ProgrammeTM2Represents.input_head
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (h : ProgrammeTM2Represents M input source target) :
    target.var.inputSymbol = programmeInputRead input source.inputHead := by
  have hzero := h.2.2.2.1 (0 : Int)
  simpa [programmeTM2InputTape] using hzero

/-- Every scanned work symbol of a represented target is exactly the source
work-tape read. -/
theorem ProgrammeTM2Represents.work_head
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (h : ProgrammeTM2Represents M input source target)
    (tape : Fin M.workTapeCount) :
    target.var.workSymbol tape = source.readWork tape := by
  have hzero := h.2.2.2.2 tape (0 : Int)
  simpa [programmeTM2WorkTape, ProgrammeConfig.readWork] using hzero

/-- The finite local observation in a represented reverse target matches the
Programme transition observation exactly. -/
theorem ProgrammeTM2Represents.action_eq
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target : (programmeTM2Machine M).Cfg}
    (h : ProgrammeTM2Represents M input source target) :
    M.transition target.var.control target.var.inputSymbol target.var.workSymbol =
      M.actionAt input source := by
  rw [h.2.2.1]
  rw [h.input_head]
  apply congrArg (fun readWork =>
    M.transition source.state (programmeInputRead input source.inputHead) readWork)
  funext tape
  exact h.work_head tape

#print axioms ProgrammeTM2Represents.input_head
#print axioms ProgrammeTM2Represents.work_head
#print axioms ProgrammeTM2Represents.action_eq

end

end MathSolve.PNP

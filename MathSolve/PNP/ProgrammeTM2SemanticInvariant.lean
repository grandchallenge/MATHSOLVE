import MathSolve.PNP.ProgrammeTM2StepSimulation
import Mathlib.Tactic

/-!
# Full-tape semantics for the reverse Programme-to-TM2 simulator

The core proof interface is the actual integer-addressed tape invariant, not
merely equality of the currently scanned symbol.  These lemmas establish that
moving an immutable input tape and writing/moving arbitrary work tapes preserve
*every* cell of the Programme representation, for every signed offset.

The final theorem reduces one genuine TM2 run transition to four concrete,
checkable stepAux effects: next label, next control, input tape move and all
work-tape write/moves.  It does not assume a post-state representation.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Actual left, stay, or right tape movement specified by a Programme action. -/
def programmeTM2TapeMove {α : Type*} [Inhabited α]
    (movement : HeadMove) (tape : Turing.Tape α) : Turing.Tape α :=
  match movement with
  | .left => tape.move .left
  | .stay => tape
  | .right => tape.move .right

/-- Arbitrary signed-offset read alignment is preserved under all head moves. -/
theorem programmeTM2_tape_move_alignment
    {α : Type*} [Inhabited α]
    (tape : Turing.Tape α) (cells : Int → α) (head : Int)
    (h : ∀ offset : Int, tape.nth offset = cells (head + offset))
    (movement : HeadMove) (offset : Int) :
    (programmeTM2TapeMove movement tape).nth offset =
      cells (movement.apply head + offset) := by
  cases movement with
  | left =>
      calc
        _ = tape.nth (offset - 1) := Tape.move_left_nth _ _
        _ = cells (head + (offset - 1)) := h _
        _ = cells ((head - 1) + offset) := by congr 1; omega
  | stay =>
      simpa [programmeTM2TapeMove, HeadMove.apply] using h offset
  | right =>
      calc
        _ = tape.nth (offset + 1) := Tape.move_right_nth _ _
        _ = cells (head + (offset + 1)) := h _
        _ = cells ((head + 1) + offset) := by congr 1; omega

/-- Writing precisely the scanned work cell preserves all other signed offsets. -/
theorem programmeTM2_tape_write_alignment
    {α : Type*} [Inhabited α]
    (tape : Turing.Tape α) (cells : Int → α) (head : Int)
    (h : ∀ offset : Int, tape.nth offset = cells (head + offset))
    (symbol : α) (offset : Int) :
    (tape.write symbol).nth offset =
      (Function.update cells head symbol) (head + offset) := by
  rw [Tape.write_nth]
  by_cases hz : offset = 0
  · subst offset
    simp
  · have hne : head + offset ≠ head := by omega
    simp [hz, hne, Function.update, h offset]

/-- Writing the old work head and moving to the next head exactly realizes the
Programme's entire integer-indexed work-tape transition. -/
theorem programmeTM2_tape_write_move_alignment
    {α : Type*} [Inhabited α]
    (tape : Turing.Tape α) (cells : Int → α) (head : Int)
    (h : ∀ offset : Int, tape.nth offset = cells (head + offset))
    (symbol : α) (movement : HeadMove) (offset : Int) :
    (programmeTM2TapeMove movement (tape.write symbol)).nth offset =
      (Function.update cells head symbol) (movement.apply head + offset) := by
  exact programmeTM2_tape_move_alignment
    (tape.write symbol) (Function.update cells head symbol) head
    (programmeTM2_tape_write_alignment tape cells head h symbol)
    movement offset

/-- Exact semantic bridge: if the concrete TM2 statement produces the specified
label, control and physical tape operations, *all* cells of the source's new
configuration are represented.  In particular this does not use an assumed
representation of the target configuration. -/
theorem ProgrammeTM2Represents.afterAction_of_concrete_tape_effects
    {M : ProgrammeMachine} {input : List Bool}
    {source : ProgrammeConfig M} {target target' : (programmeTM2Machine M).Cfg}
    (action : ProgrammeAction M.State M.Symbol M.workTapeCount)
    (hrep : ProgrammeTM2Represents M input source target)
    (hlabel : target'.l = some (.run))
    (hmode : target'.var.mode = .run)
    (hcontrol : target'.var.control = action.nextState)
    (hinput : programmeTM2InputTape M target' =
      programmeTM2TapeMove action.inputMove (programmeTM2InputTape M target))
    (hwork : ∀ tape : Fin M.workTapeCount,
      programmeTM2WorkTape M target' tape =
        programmeTM2TapeMove (action.workMove tape)
          ((programmeTM2WorkTape M target tape).write (action.write tape))) :
    ProgrammeTM2Represents M input (source.afterAction action) target' := by
  rcases hrep with ⟨_, _, _, hinputOld, hworkOld⟩
  refine ⟨hlabel, hmode, hcontrol, ?_, ?_⟩
  · intro offset
    rw [hinput]
    change (programmeTM2TapeMove action.inputMove
      (programmeTM2InputTape M target)).nth offset =
      programmeInputRead input (action.inputMove.apply source.inputHead + offset)
    exact programmeTM2_tape_move_alignment
      (programmeTM2InputTape M target) (programmeInputRead input)
      source.inputHead hinputOld action.inputMove offset
  · intro tape offset
    rw [hwork tape]
    change (programmeTM2TapeMove (action.workMove tape)
      ((programmeTM2WorkTape M target tape).write (action.write tape))).nth offset =
      (Function.update (source.work tape) (source.workHead tape) (action.write tape))
        ((action.workMove tape).apply (source.workHead tape) + offset)
    exact programmeTM2_tape_write_move_alignment
      (programmeTM2WorkTape M target tape) (source.work tape)
      (source.workHead tape) (hworkOld tape)
      (action.write tape) (action.workMove tape) offset

#print axioms programmeTM2_tape_move_alignment
#print axioms programmeTM2_tape_write_alignment
#print axioms programmeTM2_tape_write_move_alignment
#print axioms ProgrammeTM2Represents.afterAction_of_concrete_tape_effects

end
end MathSolve.PNP

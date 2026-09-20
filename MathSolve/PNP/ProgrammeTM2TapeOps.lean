import MathSolve.PNP.ProgrammeTM2Representation

/-!
# Tape algebra for the Programme-to-TM2 simulator

These lemmas identify the left/right stack operations used by the reverse
simulator with the standard two-way tape write and move operations.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- A two-stack plus scanned-cell presentation of the Programme input tape. -/
def programmeTM2InputTapeRaw
    (symbol : Option Bool) (left right : List (Option Bool)) :
    Turing.Tape (Option Bool) where
  head := symbol
  left := Turing.ListBlank.mk left
  right := Turing.ListBlank.mk right

/-- A two-stack plus scanned-cell presentation of one Programme work tape. -/
def programmeTM2WorkTapeRaw {M : ProgrammeMachine}
    (symbol : M.Symbol) (left right : List M.Symbol) :
    Turing.Tape M.Symbol where
  head := symbol
  left := Turing.ListBlank.mk left
  right := Turing.ListBlank.mk right

theorem programmeTM2InputTapeRaw_move_left
    (symbol : Option Bool) (left right : List (Option Bool)) :
    programmeTM2InputTapeRaw (left.head?.getD none) left.tail (symbol :: right) =
      (programmeTM2InputTapeRaw symbol left right).move Turing.Dir.left := by
  cases left <;>
    simp [programmeTM2InputTapeRaw, Turing.Tape.move]

theorem programmeTM2InputTapeRaw_move_right
    (symbol : Option Bool) (left right : List (Option Bool)) :
    programmeTM2InputTapeRaw (right.head?.getD none) (symbol :: left) right.tail =
      (programmeTM2InputTapeRaw symbol left right).move Turing.Dir.right := by
  cases right <;>
    simp [programmeTM2InputTapeRaw, Turing.Tape.move]

theorem programmeTM2WorkTapeRaw_write_move_left
    {M : ProgrammeMachine} (symbol write : M.Symbol)
    (left right : List M.Symbol) :
    programmeTM2WorkTapeRaw (M := M) (left.head?.getD M.blank)
        left.tail (write :: right) =
      ((programmeTM2WorkTapeRaw (M := M) symbol left right).write write).move
        Turing.Dir.left := by
  cases left <;>
    simp [programmeTM2WorkTapeRaw, Turing.Tape.write, Turing.Tape.move]

theorem programmeTM2WorkTapeRaw_write_move_right
    {M : ProgrammeMachine} (symbol write : M.Symbol)
    (left right : List M.Symbol) :
    programmeTM2WorkTapeRaw (M := M) (right.head?.getD M.blank)
        (write :: left) right.tail =
      ((programmeTM2WorkTapeRaw (M := M) symbol left right).write write).move
        Turing.Dir.right := by
  cases right <;>
    simp [programmeTM2WorkTapeRaw, Turing.Tape.write, Turing.Tape.move]

theorem programmeTM2WorkTapeRaw_write_stay
    {M : ProgrammeMachine} (symbol write : M.Symbol)
    (left right : List M.Symbol) :
    programmeTM2WorkTapeRaw (M := M) write left right =
      (programmeTM2WorkTapeRaw (M := M) symbol left right).write write := by
  rfl

#print axioms programmeTM2InputTapeRaw_move_left
#print axioms programmeTM2InputTapeRaw_move_right
#print axioms programmeTM2WorkTapeRaw_write_move_left
#print axioms programmeTM2WorkTapeRaw_write_move_right
#print axioms programmeTM2WorkTapeRaw_write_stay

end

end MathSolve.PNP

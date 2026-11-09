import MathSolve.PNP.TM2Provenance
import Mathlib.Tactic

/-!
# Structural Programme cost of one finite-TM2 machine step

A mathlib `TM2.step` executes `stepAux` recursively through one finite
statement tree.  The concrete Programme compiler executes the same syntax one
primitive at a time, with `push` requiring two transitions and every other
primitive requiring one.

This file records the exact structural cost and a machine-wide finite bound.
It does not yet assert the simulation theorem.
-/

namespace MathSolve.PNP

noncomputable section

open Turing
open scoped BigOperators

/-- Number of Programme transitions used to traverse one TM2 statement path.

For a branch, only one child executes, so the structural bound uses the maximum
of the two child costs. -/
def tm2ProgrammeStatementCost {K : Type} {Γ : K → Type} {Λ σ : Type} :
    Turing.TM2.Stmt Γ Λ σ → Nat
  | .push _ _ next => 2 + tm2ProgrammeStatementCost next
  | .peek _ _ next => 1 + tm2ProgrammeStatementCost next
  | .pop _ _ next => 1 + tm2ProgrammeStatementCost next
  | .load _ next => 1 + tm2ProgrammeStatementCost next
  | .branch _ trueStmt falseStmt =>
      1 + max (tm2ProgrammeStatementCost trueStmt)
        (tm2ProgrammeStatementCost falseStmt)
  | .goto _ => 1
  | .halt => 1

/-- Every statement traversal consumes at least one Programme transition. -/
theorem tm2ProgrammeStatementCost_pos {K : Type} {Γ : K → Type} {Λ σ : Type}
    (stmt : Turing.TM2.Stmt Γ Λ σ) :
    0 < tm2ProgrammeStatementCost stmt := by
  induction stmt with
  | push _ _ _ ih => simp [tm2ProgrammeStatementCost]
  | peek _ _ _ ih => simp [tm2ProgrammeStatementCost]
  | pop _ _ _ ih => simp [tm2ProgrammeStatementCost]
  | load _ _ ih => simp [tm2ProgrammeStatementCost]
  | branch _ _ _ ih₁ ih₂ => simp [tm2ProgrammeStatementCost]
  | goto => simp [tm2ProgrammeStatementCost]
  | halt => simp [tm2ProgrammeStatementCost]

/-- Finite machine-wide target transition factor: sum the positive structural
costs of every coded statement occurrence.  The sum is intentionally a coarse
bound; finiteness and monotonicity matter more than minimizing the constant. -/
def tm2ProgrammeStepFactor (tm : Turing.FinTM2) : Nat :=
  ∑ code : TM2StatementCode tm,
    tm2ProgrammeStatementCost code.2.1

/-- Every accessible coded statement is bounded by the machine-wide factor. -/
theorem tm2ProgrammeStatementCost_le_stepFactor
    (tm : Turing.FinTM2)
    (code : TM2StatementCode tm) :
    tm2ProgrammeStatementCost code.2.1 ≤ tm2ProgrammeStepFactor tm := by
  classical
  unfold tm2ProgrammeStepFactor
  exact Finset.single_le_sum
    (s := Finset.univ)
    (f := fun c : TM2StatementCode tm =>
      tm2ProgrammeStatementCost c.2.1)
    (fun _ _ => Nat.zero_le _)
    (Finset.mem_univ code)

/-- In particular, every label root is bounded by the same fixed factor. -/
theorem tm2ProgrammeRootCost_le_stepFactor
    (tm : Turing.FinTM2) (label : tm.Λ) :
    tm2ProgrammeStatementCost (tm.m label) ≤ tm2ProgrammeStepFactor tm := by
  simpa [TM2StatementCode.root] using
    tm2ProgrammeStatementCost_le_stepFactor tm
      (TM2StatementCode.root tm label)

#print axioms tm2ProgrammeStatementCost_pos
#print axioms tm2ProgrammeStatementCost_le_stepFactor
#print axioms tm2ProgrammeRootCost_le_stepFactor

end

end MathSolve.PNP

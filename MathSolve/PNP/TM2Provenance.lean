import Mathlib.Computability.TuringMachine.Computable
import Mathlib.Data.Fintype.Sigma
import Mathlib.Data.Fintype.Sum

/-!
# Finite provenance alphabet for `FinTM2`

A `FinTM2` requires the input stack alphabet to be finite, but its other stack
carrier types are not globally required to be `Fintype`. A correct simulation
into the protected Programme machine therefore must not assume that every
`Γ k` is finite.

For a fixed finite program, every symbol written to a non-input stack is
produced by one syntactic `push` occurrence applied to one finite internal
state. We can therefore represent a generated symbol by provenance:

* the finite label under which the statement occurrence lives;
* the finite accessible subtree occurrence itself; and
* the finite source internal state at which that push was executed.

Original input symbols are represented directly by their Boolean input bit.
The resulting token type is finite regardless of the ambient `Γ k` carriers.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/--
A finite code for a statement occurrence: a function label plus one subtree of
that label's finite statement tree.
-/
def TM2StatementCode (tm : Turing.FinTM2) :=
  Σ label : tm.Λ,
    {stmt : Turing.TM2.Stmt tm.Γ tm.Λ tm.σ //
      stmt ∈ Turing.TM2.stmts₁ (tm.m label)}

noncomputable instance tm2StatementOccurrenceFintype (tm : Turing.FinTM2)
    (label : tm.Λ) :
    Fintype {stmt : Turing.TM2.Stmt tm.Γ tm.Λ tm.σ //
      stmt ∈ Turing.TM2.stmts₁ (tm.m label)} :=
  Fintype.ofFinite _

noncomputable instance tm2StatementCodeFintype (tm : Turing.FinTM2) :
    Fintype (TM2StatementCode tm) := by
  letI : Fintype tm.Λ := tm.ΛFin
  letI : ∀ label : tm.Λ,
      Fintype {stmt : Turing.TM2.Stmt tm.Γ tm.Λ tm.σ //
        stmt ∈ Turing.TM2.stmts₁ (tm.m label)} :=
    fun label => tm2StatementOccurrenceFintype tm label
  unfold TM2StatementCode
  exact Sigma.instFintype

/-- The root statement of any finite label has a canonical occurrence code. -/
def TM2StatementCode.root (tm : Turing.FinTM2) (label : tm.Λ) :
    TM2StatementCode tm :=
  ⟨label, ⟨tm.m label, Turing.TM2.stmts₁_self⟩⟩

/-- Every subtree of an accessible occurrence is accessible under the same label. -/
theorem TM2StatementCode.subtree_mem (tm : Turing.FinTM2)
    (code : TM2StatementCode tm)
    {stmt : Turing.TM2.Stmt tm.Γ tm.Λ tm.σ}
    (hstmt : stmt ∈ Turing.TM2.stmts₁ code.2.1) :
    stmt ∈ Turing.TM2.stmts₁ (tm.m code.1) := by
  exact (Turing.TM2.stmts₁_trans code.2.2) hstmt

/-- Descend from an occurrence to any one of its finite statement subtrees. -/
def TM2StatementCode.descend (tm : Turing.FinTM2)
    (code : TM2StatementCode tm)
    (stmt : Turing.TM2.Stmt tm.Γ tm.Λ tm.σ)
    (hstmt : stmt ∈ Turing.TM2.stmts₁ code.2.1) :
    TM2StatementCode tm :=
  ⟨code.1, ⟨stmt, TM2StatementCode.subtree_mem tm code hstmt⟩⟩

/--
Finite tape-cell provenance token.

`Sum.inl bit` denotes an original input-alphabet symbol. `Sum.inr (code, state)`
denotes the value generated when the coded statement occurrence executed its
`push` function at `state`. Validity for a particular stack is imposed by the
simulation relation; including invalid combinations here only makes the target
transition function total and does not enlarge the related source states.
-/
def TM2ProvenanceToken (tm : Turing.FinTM2) :=
  Bool ⊕ (TM2StatementCode tm × tm.σ)

noncomputable instance tm2ProvenanceTokenFintype (tm : Turing.FinTM2) :
    Fintype (TM2ProvenanceToken tm) := by
  letI : Fintype (TM2StatementCode tm) := tm2StatementCodeFintype tm
  letI : Fintype tm.σ := tm.σFin
  unfold TM2ProvenanceToken
  infer_instance

noncomputable instance tm2ProvenanceTokenDecidableEq (tm : Turing.FinTM2) :
    DecidableEq (TM2ProvenanceToken tm) :=
  Classical.decEq _

/-- Add one distinguished blank symbol for the Programme tape alphabet. -/
abbrev TM2ProgrammeSymbol (tm : Turing.FinTM2) := Option (TM2ProvenanceToken tm)

noncomputable instance tm2ProgrammeSymbolFintype (tm : Turing.FinTM2) :
    Fintype (TM2ProgrammeSymbol tm) := by
  letI : Fintype (TM2ProvenanceToken tm) := tm2ProvenanceTokenFintype tm
  unfold TM2ProgrammeSymbol
  infer_instance

noncomputable instance tm2ProgrammeSymbolDecidableEq (tm : Turing.FinTM2) :
    DecidableEq (TM2ProgrammeSymbol tm) :=
  Classical.decEq _

/-- The distinguished Programme blank is not a provenance-bearing source symbol. -/
def tm2ProgrammeBlank (tm : Turing.FinTM2) : TM2ProgrammeSymbol tm := none

#print axioms TM2StatementCode.subtree_mem

end

end MathSolve.PNP

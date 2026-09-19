import MathSolve.PNP.ModelBridge
import MathSolve.PNP.TM2Provenance

/-!
# Exact `FinTM2` stack representation on Programme work tapes

This file gives the relational stack invariant used by the finite-TM2 to
Programme compiler.  Raw internal `Γ k` values are related to finite provenance
tokens; a whole source stack is related pointwise to a finite token list; and
that token list is embedded contiguously on one two-way Programme work tape.

The relation is intentionally partial on provenance tokens.  Tokens that do not
correspond to the source stack index are invalid and can be routed to a rejecting
sink by the total target transition function.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Semantic value denoted by one finite provenance token on source stack `k`. -/
def TM2TokenDenotes {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    (token : TM2ProvenanceToken source.tm) (value : source.tm.Γ k) : Prop :=
  match token with
  | .inl bit =>
      ∃ h : source.tm.k₀ = k,
        value = h ▸ source.inputAlphabet.invFun bit
  | .inr generated =>
      let code := generated.1
      let state := generated.2
      match code.2.1 with
      | .push k' valueFn _ =>
          ∃ h : k' = k, value = h ▸ valueFn state
      | _ => False

/-- Original input bits denote exactly the corresponding source input symbols. -/
theorem tm2TokenDenotes_input {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (bit : Bool) :
    TM2TokenDenotes source source.tm.k₀ (.inl bit)
      (source.inputAlphabet.invFun bit) := by
  exact ⟨rfl, rfl⟩

/-- Pointwise denotation relation between finite provenance tokens and one raw TM2 stack. -/
inductive TM2TokenListDenotes {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K) :
    List (TM2ProvenanceToken source.tm) → List (source.tm.Γ k) → Prop
  | nil : TM2TokenListDenotes source k [] []
  | cons {token value tokens values} :
      TM2TokenDenotes source k token value →
      TM2TokenListDenotes source k tokens values →
      TM2TokenListDenotes source k (token :: tokens) (value :: values)

/-- Related token/source stacks have exactly the same length. -/
theorem TM2TokenListDenotes.length_eq {decision : List Bool → Bool}
    {source : ImportedTM2Witness decision} {k : source.tm.K}
    {tokens : List (TM2ProvenanceToken source.tm)} {values : List (source.tm.Γ k)}
    (h : TM2TokenListDenotes source k tokens values) :
    tokens.length = values.length := by
  induction h with
  | nil => rfl
  | cons _ _ ih => simp [ih]

/-- The exact imported binary input stack has a finite provenance representation. -/
theorem inputTokenList_denotes {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    TM2TokenListDenotes source source.tm.k₀
      (input.map Sum.inl)
      (input.map source.inputAlphabet.invFun) := by
  induction input with
  | nil => exact .nil
  | cons bit rest ih =>
      exact .cons (tm2TokenDenotes_input source bit) ih

/--
Embed a finite provenance stack on a two-way Programme tape.

The source stack head is at `head`; increasing integer coordinates enumerate the
remaining stack cells.  Every cell outside the finite represented segment is
blank.
-/
def embedTM2TokenStack {tm : Turing.FinTM2}
    (tokens : List (TM2ProvenanceToken tm)) (head : Int) :
    Int → TM2ProgrammeSymbol tm :=
  fun position =>
    let offset := position - head
    if 0 ≤ offset then tokens[offset.toNat]? else none

/-- Exact source-stack/Programme-tape representation invariant. -/
def TM2StackRepresented {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    (tape : Int → TM2ProgrammeSymbol source.tm) (head : Int)
    (stack : List (source.tm.Γ k)) : Prop :=
  ∃ tokens : List (TM2ProvenanceToken source.tm),
    TM2TokenListDenotes source k tokens stack ∧
    tape = embedTM2TokenStack tokens head

/-- The empty source stack is represented by an everywhere-blank work tape. -/
theorem emptyTM2StackRepresented {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K) (head : Int) :
    TM2StackRepresented source k (embedTM2TokenStack [] head) head [] := by
  exact ⟨[], .nil, rfl⟩

/-- The exact imported input list is represented by its Boolean provenance tokens. -/
theorem inputTM2StackRepresented {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) (head : Int) :
    TM2StackRepresented source source.tm.k₀
      (embedTM2TokenStack (input.map Sum.inl) head) head
      (input.map source.inputAlphabet.invFun) := by
  exact ⟨input.map Sum.inl, inputTokenList_denotes source input, rfl⟩

#print axioms TM2TokenListDenotes.length_eq
#print axioms inputTokenList_denotes
#print axioms emptyTM2StackRepresented
#print axioms inputTM2StackRepresented

end

end MathSolve.PNP

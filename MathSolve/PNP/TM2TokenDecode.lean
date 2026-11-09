import MathSolve.PNP.TM2StackEncoding

/-!
# Deterministic decoding of finite TM2 provenance tokens

`TM2ProvenanceToken` is the finite alphabet used by the Programme-side
simulation of a fixed imported `FinTM2`.  This file turns the relational
`TM2TokenDenotes` invariant into a deterministic partial decoder at a selected
source stack.

The decoder is intentionally partial: a token generated for a different source
stack, or a provenance code whose statement is not a `push`, is invalid at that
stack.  Validity is supplied by the simulation invariant.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Decode one finite provenance token at source stack `k`. -/
def tm2TokenValue? {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    (token : TM2ProvenanceToken source.tm) : Option (source.tm.Γ k) :=
  match token with
  | .inl bit =>
      if h : source.tm.k₀ = k then
        some (h ▸ source.inputAlphabet.invFun bit)
      else
        none
  | .inr generated =>
      let code := generated.1
      let state := generated.2
      match code.2.1 with
      | .push k' valueFn _ =>
          if h : k' = k then
            some (h ▸ valueFn state)
          else
            none
      | _ => none

/-- Original input provenance decodes exactly on the designated input stack. -/
theorem tm2TokenValue?_input {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (bit : Bool) :
    tm2TokenValue? source source.tm.k₀ (.inl bit) =
      some (source.inputAlphabet.invFun bit) := by
  simp [tm2TokenValue?]

/-- Every relationally valid token is accepted by the deterministic decoder. -/
theorem tm2TokenValue?_eq_some_of_denotes {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    (token : TM2ProvenanceToken source.tm) (value : source.tm.Γ k)
    (hdenotes : TM2TokenDenotes source k token value) :
    tm2TokenValue? source k token = some value := by
  cases token with
  | inl bit =>
      rcases hdenotes with ⟨h, rfl⟩
      simp [tm2TokenValue?, h]
  | inr generated =>
      rcases generated with ⟨code, state⟩
      dsimp [TM2TokenDenotes] at hdenotes
      generalize hstmt : code.2.1 = stmt at hdenotes ⊢
      cases stmt with
      | push k' valueFn next =>
          rcases hdenotes with ⟨h, rfl⟩
          simp [tm2TokenValue?, hstmt, h]
      | peek => simp [hstmt] at hdenotes
      | pop => simp [hstmt] at hdenotes
      | load => simp [hstmt] at hdenotes
      | branch => simp [hstmt] at hdenotes
      | goto => simp [hstmt] at hdenotes
      | halt => simp [hstmt] at hdenotes

/-- A represented nonempty stack exposes its source head through the decoder. -/
theorem TM2TokenListDenotes.head_decode {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    {token : TM2ProvenanceToken source.tm} {tokens : List (TM2ProvenanceToken source.tm)}
    {value : source.tm.Γ k} {values : List (source.tm.Γ k)}
    (h : TM2TokenListDenotes source k (token :: tokens) (value :: values)) :
    tm2TokenValue? source k token = some value := by
  cases h with
  | cons hhead _ =>
      exact tm2TokenValue?_eq_some_of_denotes source k token value hhead

#print axioms tm2TokenValue?_input
#print axioms tm2TokenValue?_eq_some_of_denotes
#print axioms TM2TokenListDenotes.head_decode

end

end MathSolve.PNP

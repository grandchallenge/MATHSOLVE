import MathSolve.PNP.TM2TokenDecode

/-!
# Elementary operations on represented TM2 stacks

These lemmas expose the head cell of the exact provenance-stack representation.
They are the local invariant facts used by the concrete Programme compiler for
`peek`, `pop`, and output inspection.
-/

namespace MathSolve.PNP

noncomputable section

/-- A token list denoting a nonempty source stack is itself nonempty, with a
head token denoting the source head value. -/
theorem TM2TokenListDenotes.exists_head {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    {tokens : List (TM2ProvenanceToken source.tm)}
    {value : source.tm.Γ k} {values : List (source.tm.Γ k)}
    (h : TM2TokenListDenotes source k tokens (value :: values)) :
    ∃ token rest,
      tokens = token :: rest ∧
      TM2TokenDenotes source k token value := by
  cases h with
  | cons hhead _ =>
      exact ⟨_, _, rfl, hhead⟩

/-- The exact embedding exposes the first provenance token at its designated head. -/
@[simp] theorem embedTM2TokenStack_head {tm : Turing.FinTM2}
    (token : TM2ProvenanceToken tm)
    (tokens : List (TM2ProvenanceToken tm)) (head : Int) :
    embedTM2TokenStack (token :: tokens) head head = some token := by
  simp [embedTM2TokenStack]

/-- The exact empty-stack embedding is blank at its designated head. -/
@[simp] theorem embedTM2TokenStack_empty_head {tm : Turing.FinTM2} (head : Int) :
    embedTM2TokenStack ([] : List (TM2ProvenanceToken tm)) head head = none := by
  simp [embedTM2TokenStack]

/-- A represented empty source stack is blank at the represented head. -/
theorem TM2StackRepresented.empty_head {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    (tape : Int → TM2ProgrammeSymbol source.tm) (head : Int)
    (h : TM2StackRepresented source k tape head []) :
    tape head = none := by
  rcases h with ⟨tokens, htokens, rfl⟩
  cases htokens
  simp

/-- A represented nonempty source stack exposes a provenance token whose
deterministic decoder is exactly the source head value. -/
theorem TM2StackRepresented.head_decode {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (k : source.tm.K)
    (tape : Int → TM2ProgrammeSymbol source.tm) (head : Int)
    (value : source.tm.Γ k) (values : List (source.tm.Γ k))
    (h : TM2StackRepresented source k tape head (value :: values)) :
    ∃ token : TM2ProvenanceToken source.tm,
      tape head = some token ∧
      tm2TokenValue? source k token = some value := by
  rcases h with ⟨tokens, htokens, rfl⟩
  rcases TM2TokenListDenotes.exists_head source k htokens with
    ⟨token, rest, rfl, hhead⟩
  refine ⟨token, ?_, ?_⟩
  · simp
  · exact tm2TokenValue?_eq_some_of_denotes source k token value hhead

#print axioms TM2TokenListDenotes.exists_head
#print axioms embedTM2TokenStack_head
#print axioms embedTM2TokenStack_empty_head
#print axioms TM2StackRepresented.empty_head
#print axioms TM2StackRepresented.head_decode

end

end MathSolve.PNP

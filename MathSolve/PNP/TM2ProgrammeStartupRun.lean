import MathSolve.PNP.TM2ProgrammeStartupStep
import MathSolve.PNP.TM2ProgrammeInitialization

/-!
# Closed-form startup configurations for the forward TM2 compiler

The copy phase writes input provenance tokens from coordinate zero toward the
right.  The rewind phase returns both the immutable input head and the selected
work head to zero before entering the imported TM2 root.
-/

namespace MathSolve.PNP

noncomputable section

/-- Appending one token to the represented finite segment is exactly one write
at the first blank coordinate to its right. -/
theorem embedTM2TokenStack_append_singleton {tm : Turing.FinTM2}
    (tokens : List (TM2ProvenanceToken tm))
    (token : TM2ProvenanceToken tm) :
    Function.update (embedTM2TokenStack tokens 0)
        (tokens.length : Int) (some token) =
      embedTM2TokenStack (tokens ++ [token]) 0 := by
  funext position
  by_cases hp : position = (tokens.length : Int)
  · subst position
    simp [Function.update, embedTM2TokenStack]
  · by_cases hnonneg : 0 ≤ position
    · have hcast : (position.toNat : Int) = position :=
        Int.toNat_of_nonneg hnonneg
      have hne : position.toNat ≠ tokens.length := by
        intro h
        apply hp
        rw [← hcast, h]
      by_cases hlt : position.toNat < tokens.length
      · simp [Function.update, hp, embedTM2TokenStack, hnonneg,
          List.getElem?_append, hlt]
      · have hgt : tokens.length < position.toNat := by
          omega
        simp [Function.update, hp, embedTM2TokenStack, hnonneg,
          List.getElem?_append, hlt, hgt]
    · simp [Function.update, hp, embedTM2TokenStack, hnonneg]

/-- Closed form after a finite prefix has been copied, before the first blank
input cell switches the machine into rewind mode. -/
def tm2ProgrammeCopyConfig {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (prefix : List Bool) :
    ProgrammeConfig (tm2ProgrammeMachine source) where
  state := tm2ControlCopy source
  inputHead := (prefix.length : Int)
  workHead := fun tape =>
    if tape = tm2TapeEquiv source source.tm.k₀
    then (prefix.length : Int)
    else 0
  work := tm2ProgrammeReadyWork source prefix

/-- One copy action extends the closed-form copied prefix by exactly one bit. -/
theorem tm2ProgrammeCopyConfig_after_bit {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (prefix : List Bool) (bit : Bool) :
    (tm2ProgrammeCopyConfig source prefix).afterAction
        (tm2CopyBitAction source bit
          (tm2ProgrammeCopyConfig source prefix).readWork) =
      tm2ProgrammeCopyConfig source (prefix ++ [bit]) := by
  ext tape position <;>
    simp [tm2ProgrammeCopyConfig, ProgrammeConfig.afterAction,
      tm2CopyBitAction, tm2ProgrammeReadyWork, tm2MoveSelected,
      tm2WriteSelected, ProgrammeConfig.readWork, HeadMove.apply,
      embedTM2TokenStack_append_singleton, Function.update_eq_self]
  by_cases htape : tape = tm2TapeEquiv source source.tm.k₀
  · subst tape
    simp [tm2ProgrammeCopyConfig, ProgrammeConfig.afterAction,
      tm2CopyBitAction, tm2ProgrammeReadyWork, tm2MoveSelected,
      tm2WriteSelected, ProgrammeConfig.readWork, HeadMove.apply,
      embedTM2TokenStack_append_singleton]
  · simp [tm2ProgrammeCopyConfig, ProgrammeConfig.afterAction,
      tm2CopyBitAction, tm2ProgrammeReadyWork, tm2MoveSelected,
      tm2WriteSelected, ProgrammeConfig.readWork, HeadMove.apply,
      htape, Function.update_eq_self]

#print axioms embedTM2TokenStack_append_singleton
#print axioms tm2ProgrammeCopyConfig_after_bit

end

end MathSolve.PNP

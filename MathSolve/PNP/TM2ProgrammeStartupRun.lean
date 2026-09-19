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

/-- The zero-length copy configuration is the native Programme initial
configuration; the input argument affects reads, not stored configuration data. -/
theorem tm2ProgrammeCopyConfig_nil_eq_init {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    tm2ProgrammeCopyConfig source [] =
      (tm2ProgrammeMachine source).init input := by
  ext tape position <;>
    simp [tm2ProgrammeCopyConfig, ProgrammeMachine.init,
      tm2ProgrammeReadyWork, embedTM2TokenStack]

/-- Reading at the first position after a copied prefix returns the next input bit. -/
theorem programmeInputRead_append_head
    (prefix rest : List Bool) (bit : Bool) :
    programmeInputRead (prefix ++ bit :: rest) (prefix.length : Int) =
      some bit := by
  simp [programmeInputRead, List.getElem?_append]

/-- Copying an arbitrary remaining suffix reaches the closed-form full copied
configuration in exactly one Programme transition per remaining input bit. -/
theorem tm2Programme_copy_run_aux {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    ∀ (done todo : List Bool),
      input = done ++ todo →
      Nonempty
        (StateTransition.EvalsToInTime
          ((tm2ProgrammeMachine source).step input)
          (tm2ProgrammeCopyConfig source done)
          (some (tm2ProgrammeCopyConfig source input))
          todo.length) := by
  intro done todo hinput
  induction todo generalizing done with
  | nil =>
      subst input
      simpa using
        (StateTransition.EvalsToInTime.refl
          ((tm2ProgrammeMachine source).step (done ++ []))
          (tm2ProgrammeCopyConfig source done))
  | cons bit rest ih =>
      have hread :
          programmeInputRead input (done.length : Int) = some bit := by
        rw [hinput]
        exact programmeInputRead_append_head done rest bit
      have hstepRaw :=
        tm2ProgrammeMachine_step_copy_some source input
          (tm2ProgrammeCopyConfig source done) bit rfl hread
      have hstep :
          (tm2ProgrammeMachine source).step input
              (tm2ProgrammeCopyConfig source done) =
            some (tm2ProgrammeCopyConfig source (done ++ [bit])) := by
        rw [tm2ProgrammeCopyConfig_after_bit] at hstepRaw
        exact hstepRaw
      have hinput' :
          input = (done ++ [bit]) ++ rest := by
        simpa [List.append_assoc] using hinput
      rcases ih (done ++ [bit]) hinput' with ⟨hrest⟩
      have hone := programme_one_step_in_time hstep
      refine ⟨?_⟩
      simpa using
        StateTransition.EvalsToInTime.trans
          ((tm2ProgrammeMachine source).step input)
          1 rest.length
          (tm2ProgrammeCopyConfig source done)
          (tm2ProgrammeCopyConfig source (done ++ [bit]))
          (some (tm2ProgrammeCopyConfig source input))
          hone hrest

/-- Starting from the native Programme initial configuration, the exact input is
copied in `input.length` transitions. -/
theorem tm2Programme_copy_run {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    Nonempty
      (StateTransition.EvalsToInTime
        ((tm2ProgrammeMachine source).step input)
        ((tm2ProgrammeMachine source).init input)
        (some (tm2ProgrammeCopyConfig source input))
        input.length) := by
  rcases tm2Programme_copy_run_aux source input [] input (by simp) with ⟨hcopy⟩
  refine ⟨?_⟩
  simpa [tm2ProgrammeCopyConfig_nil_eq_init] using hcopy

#print axioms embedTM2TokenStack_append_singleton
#print axioms tm2ProgrammeCopyConfig_after_bit
#print axioms tm2ProgrammeCopyConfig_nil_eq_init
#print axioms programmeInputRead_append_head
#print axioms tm2Programme_copy_run_aux
#print axioms tm2Programme_copy_run

end

end MathSolve.PNP

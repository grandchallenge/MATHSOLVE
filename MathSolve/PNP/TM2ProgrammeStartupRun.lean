import MathSolve.PNP.TM2ProgrammeStartupStep
import MathSolve.PNP.TM2ProgrammeInitialization

/-!
# Closed-form startup copy execution for the forward TM2 compiler

The copy phase writes input provenance tokens from coordinate zero toward the
right.  This file proves its exact closed form and exact linear transition count.
The rewind phase is handled separately.
-/

namespace MathSolve.PNP

noncomputable section

/-- Fieldwise extensionality for Programme configurations. -/
theorem programmeConfig_ext {M : ProgrammeMachine}
    {a b : ProgrammeConfig M}
    (hstate : a.state = b.state)
    (hinput : a.inputHead = b.inputHead)
    (hhead : a.workHead = b.workHead)
    (hwork : a.work = b.work) :
    a = b := by
  cases a with
  | mk astate ainput ahead awork =>
      cases b with
      | mk bstate binput bhead bwork =>
          cases hstate
          cases hinput
          cases hhead
          cases hwork
          rfl

/-- The empty provenance embedding at head zero is the everywhere-blank tape. -/
theorem embedTM2TokenStack_nil_zero {tm : Turing.FinTM2} :
    embedTM2TokenStack ([] : List (TM2ProvenanceToken tm)) 0 =
      (fun _ => none) := by
  funext position
  simp [embedTM2TokenStack]

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
      · have hgt : tokens.length < position.toNat := by omega
        have hsub : position.toNat - tokens.length ≠ 0 := by omega
        simp [Function.update, hp, embedTM2TokenStack, hnonneg,
          List.getElem?_append, hlt, hsub]
    · simp [Function.update, hp, embedTM2TokenStack, hnonneg]

/-- Closed form after a finite initial segment has been copied, before the first
blank input cell switches the machine into rewind mode. -/
def tm2ProgrammeCopyConfig {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (copied : List Bool) :
    ProgrammeConfig (tm2ProgrammeMachine source) where
  state := tm2ControlCopy source
  inputHead := (copied.length : Int)
  workHead := fun tape =>
    if tape = tm2TapeEquiv source source.tm.k₀
    then (copied.length : Int)
    else 0
  work := tm2ProgrammeReadyWork source copied

/-- One copy action extends the closed-form copied segment by exactly one bit. -/
theorem tm2ProgrammeCopyConfig_after_bit {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision)
    (copied : List Bool) (bit : Bool) :
    (tm2ProgrammeCopyConfig source copied).afterAction
        (tm2CopyBitAction source bit
          (tm2ProgrammeCopyConfig source copied).readWork) =
      tm2ProgrammeCopyConfig source (copied ++ [bit]) := by
  apply programmeConfig_ext
  · rfl
  · simp [tm2ProgrammeCopyConfig, ProgrammeConfig.afterAction,
      tm2CopyBitAction, HeadMove.apply]
  · funext tape
    by_cases htape : tape = tm2TapeEquiv source source.tm.k₀
    · subst tape
      simp [tm2ProgrammeCopyConfig, ProgrammeConfig.afterAction,
        tm2CopyBitAction, tm2MoveSelected, HeadMove.apply]
    · simp only [tm2ProgrammeCopyConfig, ProgrammeConfig.afterAction,
        tm2CopyBitAction, tm2MoveSelected]
      rw [Function.update_of_ne htape, if_neg htape]
      rfl
  · funext tape position
    by_cases htape : tape = tm2TapeEquiv source source.tm.k₀
    · subst tape
      change
        Function.update
            (embedTM2TokenStack (copied.map Sum.inl) 0)
            (if tm2TapeEquiv source source.tm.k₀ =
                tm2TapeEquiv source source.tm.k₀
             then (copied.length : Int) else 0)
            (some (.inl bit)) position =
          embedTM2TokenStack ((copied ++ [bit]).map Sum.inl) 0 position
      rw [if_pos rfl]
      simpa [List.map_append] using
        congrFun
          (embedTM2TokenStack_append_singleton
            (copied.map Sum.inl) (.inl bit))
          position
    · simp only [tm2ProgrammeCopyConfig, ProgrammeConfig.afterAction,
        tm2CopyBitAction, tm2ProgrammeReadyWork, tm2WriteSelected,
        ProgrammeConfig.readWork]
      rw [if_neg htape, Function.update_of_ne htape]
      exact congrFun (Function.update_eq_self (fun _ : Int => none) 0) position

/-- The zero-length copy configuration is the native Programme initial
configuration; the input argument affects reads, not stored configuration data. -/
theorem tm2ProgrammeCopyConfig_nil_eq_init {decision : List Bool → Bool}
    (source : ImportedTM2Witness decision) (input : List Bool) :
    tm2ProgrammeCopyConfig source [] =
      (tm2ProgrammeMachine source).init input := by
  apply programmeConfig_ext
  · rfl
  · rfl
  · funext tape
    simp [tm2ProgrammeCopyConfig, ProgrammeMachine.init]
  · funext tape position
    by_cases htape : tape = tm2TapeEquiv source source.tm.k₀
    · subst tape
      change embedTM2TokenStack [] 0 position = tm2ProgrammeBlank source.tm
      rw [congrFun (embedTM2TokenStack_nil_zero (tm := source.tm)) position]
      rfl
    · change
        (if tape = tm2TapeEquiv source source.tm.k₀
         then embedTM2TokenStack [] 0 else fun _ => none) position =
          tm2ProgrammeBlank source.tm
      rw [if_neg htape]
      rfl

/-- Reading at the first position after a copied segment returns the next input bit. -/
theorem programmeInputRead_append_head
    (copied rest : List Bool) (bit : Bool) :
    programmeInputRead (copied ++ bit :: rest) (copied.length : Int) =
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
      refine ⟨?_⟩
      simpa using
        (StateTransition.EvalsToInTime.refl
          ((tm2ProgrammeMachine source).step done)
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
  rw [tm2ProgrammeCopyConfig_nil_eq_init source input] at hcopy
  exact hcopy

#print axioms programmeConfig_ext
#print axioms embedTM2TokenStack_nil_zero
#print axioms embedTM2TokenStack_append_singleton
#print axioms tm2ProgrammeCopyConfig_after_bit
#print axioms tm2ProgrammeCopyConfig_nil_eq_init
#print axioms programmeInputRead_append_head
#print axioms tm2Programme_copy_run_aux
#print axioms tm2Programme_copy_run

end

end MathSolve.PNP

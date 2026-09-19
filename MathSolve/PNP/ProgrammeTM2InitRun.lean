import MathSolve.PNP.ProgrammeTM2Representation

/-!
# Exact initialization run for the Programme-to-TM2 simulator

The reverse simulator normalizes the raw FinTM2 input in two linear passes:
first onto a temporary stack, then back into left-to-right input-tape order.
A final pop loads the scanned input cell and enters run mode.
-/

namespace MathSolve.PNP

noncomputable section

open Turing

/-- Initialization-local state with only the transient input symbol changed. -/
def programmeTM2InitState (M : ProgrammeMachine) (symbol : Option Bool) :
    ProgrammeTM2State M :=
  { programmeTM2InitialState M with inputSymbol := symbol }

/-- Closed-form stack family used during reverse-simulator initialization. -/
def programmeTM2InitStacks (M : ProgrammeMachine)
    (raw temp : List Bool) (right : List (Option Bool)) :
    ∀ k : ProgrammeTM2Stack M.workTapeCount,
      List (programmeTM2StackAlphabet M k)
  | .rawInput => raw
  | .inputTemp => temp
  | .inputLeft => []
  | .inputRight => right
  | .workLeft _ => []
  | .workRight _ => []
  | .output => []

@[simp] theorem programmeTM2InitStacks_raw (M : ProgrammeMachine)
    (raw temp : List Bool) (right : List (Option Bool)) :
    programmeTM2InitStacks M raw temp right .rawInput = raw := rfl

@[simp] theorem programmeTM2InitStacks_temp (M : ProgrammeMachine)
    (raw temp : List Bool) (right : List (Option Bool)) :
    programmeTM2InitStacks M raw temp right .inputTemp = temp := rfl

@[simp] theorem programmeTM2InitStacks_right (M : ProgrammeMachine)
    (raw temp : List Bool) (right : List (Option Bool)) :
    programmeTM2InitStacks M raw temp right .inputRight = right := rfl

/-- Closed-form configuration for the two initialization labels. -/
def programmeTM2InitCfg (M : ProgrammeMachine)
    (label : ProgrammeTM2Mode M.workTapeCount) (symbol : Option Bool)
    (raw temp : List Bool) (right : List (Option Bool)) :
    (programmeTM2Machine M).Cfg where
  l := some label
  var := programmeTM2InitState M symbol
  stk := programmeTM2InitStacks M raw temp right

/-- Fieldwise extensionality for heterogeneous TM2 configurations. -/
theorem programmeTM2Cfg_ext
    {K : Type} {Γ : K → Type} {Λ σ : Type}
    {a b : Turing.TM2.Cfg Γ Λ σ}
    (hl : a.l = b.l) (hv : a.var = b.var)
    (hs : ∀ k, a.stk k = b.stk k) : a = b := by
  cases a with
  | mk al av astk =>
      cases b with
      | mk bl bv bstk =>
          simp only at hl hv hs
          cases hl
          cases hv
          congr
          funext k
          exact hs k

theorem programmeTM2InitStacks_update_raw (M : ProgrammeMachine)
    (raw raw' temp : List Bool) (right : List (Option Bool)) :
    Function.update (programmeTM2InitStacks M raw temp right) .rawInput raw' =
      programmeTM2InitStacks M raw' temp right := by
  funext k
  cases k <;> simp [programmeTM2InitStacks, Function.update]

theorem programmeTM2InitStacks_update_temp (M : ProgrammeMachine)
    (raw temp temp' : List Bool) (right : List (Option Bool)) :
    Function.update (programmeTM2InitStacks M raw temp right) .inputTemp temp' =
      programmeTM2InitStacks M raw temp' right := by
  funext k
  cases k <;> simp [programmeTM2InitStacks, Function.update]

theorem programmeTM2InitStacks_update_right (M : ProgrammeMachine)
    (raw temp : List Bool) (right right' : List (Option Bool)) :
    Function.update (programmeTM2InitStacks M raw temp right) .inputRight right' =
      programmeTM2InitStacks M raw temp right' := by
  funext k
  cases k <;> simp [programmeTM2InitStacks, Function.update]

/-- The native FinTM2 input configuration is the closed-form first-pass state. -/
theorem programmeTM2_initList_eq_cfg (M : ProgrammeMachine) (input : List Bool) :
    Turing.initList (programmeTM2Machine M) input =
      programmeTM2InitCfg M .initToTemp none input [] [] := by
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;>
      simp [Turing.initList, programmeTM2Machine, programmeTM2InitCfg,
        programmeTM2InitState, programmeTM2InitStacks] <;> rfl
  
/-- One nonempty first-pass step pops raw input and pushes it onto the temporary stack. -/
theorem programmeTM2_step_initToTemp_cons (M : ProgrammeMachine)
    (symbol : Option Bool) (bit : Bool) (raw temp : List Bool)
    (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToTemp symbol (bit :: raw) temp right) =
      some
        (programmeTM2InitCfg M .initToTemp (some bit) raw (bit :: temp) right) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, programmeTM2InitToTemp, Turing.TM2.stepAux,
    programmeTM2InitCfg, programmeTM2InitState, programmeTM2InitStacks_raw,
    programmeTM2InitStacks_temp]
  rw [List.head?_cons, Option.isSome_some, Bool.cond_true,
    List.tail_cons, Option.getD_some]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2InitStacks, Function.update] <;> rfl

/-- The first blank pop ends the first pass and clears the transient symbol. -/
theorem programmeTM2_step_initToTemp_nil (M : ProgrammeMachine)
    (symbol : Option Bool) (temp : List Bool) (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToTemp symbol [] temp right) =
      some (programmeTM2InitCfg M .initToRight none [] temp right) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, programmeTM2InitToTemp, Turing.TM2.stepAux,
    programmeTM2InitCfg, programmeTM2InitState, programmeTM2InitStacks_raw]
  rw [List.head?_nil, Option.isSome_none, Bool.cond_false, List.tail_nil]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2InitStacks, Function.update] <;> rfl

/-- One nonempty second-pass step restores a Boolean cell to the right-of-head stack. -/
theorem programmeTM2_step_initToRight_cons (M : ProgrammeMachine)
    (symbol : Option Bool) (bit : Bool) (temp : List Bool)
    (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToRight symbol [] (bit :: temp) right) =
      some
        (programmeTM2InitCfg M .initToRight (some bit) [] temp (some bit :: right)) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, programmeTM2InitToRight, Turing.TM2.stepAux,
    programmeTM2InitCfg, programmeTM2InitState, programmeTM2InitStacks_temp,
    programmeTM2InitStacks_right]
  rw [List.head?_cons, Option.isSome_some, Bool.cond_true,
    List.tail_cons, Option.getD_some]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2InitStacks, Function.update] <;> rfl

/-- The second blank pop ends the restoration pass. -/
theorem programmeTM2_step_initToRight_nil (M : ProgrammeMachine)
    (symbol : Option Bool) (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToRight symbol [] [] right) =
      some (programmeTM2InitCfg M .initFinish none [] [] right) := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, programmeTM2InitToRight, Turing.TM2.stepAux,
    programmeTM2InitCfg, programmeTM2InitState, programmeTM2InitStacks_temp]
  rw [List.head?_nil, Option.isSome_none, Bool.cond_false, List.tail_nil]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2InitStacks, Function.update] <;> rfl

/-- The final initialization step loads the scanned input cell and enters run mode. -/
theorem programmeTM2_step_initFinish (M : ProgrammeMachine)
    (right : List (Option Bool)) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initFinish none [] [] right) =
      some
        { l := some (.run)
          var :=
            { programmeTM2InitialState M with
                mode := .run
                inputSymbol := right.head?.getD none }
          stk := programmeTM2InitStacks M [] [] right.tail } := by
  simp only [Turing.FinTM2.step, Turing.TM2.step, programmeTM2Machine,
    programmeTM2Program, programmeTM2InitFinish, Turing.TM2.stepAux,
    programmeTM2InitCfg, programmeTM2InitState, programmeTM2InitStacks_right]
  apply congrArg some
  apply programmeTM2Cfg_ext
  · rfl
  · rfl
  · intro k
    cases k <;> simp [programmeTM2InitStacks, Function.update] <;> rfl

/-- Any exact one-step transition yields a one-step bounded evaluation witness. -/
def programmeTM2_one_step_in_time
    {M : ProgrammeMachine} {a b : (programmeTM2Machine M).Cfg}
    (h : (programmeTM2Machine M).step a = some b) :
    StateTransition.EvalsToInTime
      (programmeTM2Machine M).step a (some b) 1 := by
  exact
    { steps := 1
      evals_in_steps := by simpa using h
      steps_le_m := le_rfl }

/-- Enlarge an existing step bound without changing the witnessed execution. -/
def programmeTM2_evalsToInTime_mono
    {σ : Type} {step : σ → Option σ} {a : σ} {b : Option σ}
    {m n : Nat} (h : StateTransition.EvalsToInTime step a b m)
    (hmn : m ≤ n) : StateTransition.EvalsToInTime step a b n :=
  { h.toEvalsTo with steps_le_m := le_trans h.steps_le_m hmn }

/-- The complete first normalization pass takes exactly one step per input
cell plus one blank-detection step. -/
theorem programmeTM2_initToTemp_run (M : ProgrammeMachine) :
    ∀ (raw temp : List Bool) (symbol : Option Bool)
      (right : List (Option Bool)),
      Nonempty
        (StateTransition.EvalsToInTime
          (programmeTM2Machine M).step
          (programmeTM2InitCfg M .initToTemp symbol raw temp right)
          (some
            (programmeTM2InitCfg M .initToRight none []
              (raw.reverse ++ temp) right))
          (raw.length + 1)) := by
  intro raw
  induction raw with
  | nil =>
      intro temp symbol right
      refine ⟨?_⟩
      simpa using
        programmeTM2_one_step_in_time
          (programmeTM2_step_initToTemp_nil M symbol temp right)
  | cons bit raw ih =>
      intro temp symbol right
      have hstep :=
        programmeTM2_step_initToTemp_cons M symbol bit raw temp right
      have hone := programmeTM2_one_step_in_time hstep
      rcases ih (bit :: temp) (some bit) right with ⟨hrest⟩
      refine ⟨?_⟩
      have hrun :=
        StateTransition.EvalsToInTime.trans
          (programmeTM2Machine M).step
          1 (raw.length + 1)
          (programmeTM2InitCfg M .initToTemp symbol (bit :: raw) temp right)
          (programmeTM2InitCfg M .initToTemp (some bit) raw (bit :: temp) right)
          (some
            (programmeTM2InitCfg M .initToRight none []
              (raw.reverse ++ bit :: temp) right))
          hone hrest
      simpa [List.reverse_cons, List.append_assoc, Nat.add_assoc] using hrun

/-- The complete second normalization pass takes exactly one step per temporary
cell plus one blank-detection step. -/
theorem programmeTM2_initToRight_run (M : ProgrammeMachine) :
    ∀ (temp : List Bool) (right : List (Option Bool)) (symbol : Option Bool),
      Nonempty
        (StateTransition.EvalsToInTime
          (programmeTM2Machine M).step
          (programmeTM2InitCfg M .initToRight symbol [] temp right)
          (some
            (programmeTM2InitCfg M .initFinish none [] []
              (temp.reverse.map some ++ right)))
          (temp.length + 1)) := by
  intro temp
  induction temp with
  | nil =>
      intro right symbol
      refine ⟨?_⟩
      simpa using
        programmeTM2_one_step_in_time
          (programmeTM2_step_initToRight_nil M symbol right)
  | cons bit temp ih =>
      intro right symbol
      have hstep :=
        programmeTM2_step_initToRight_cons M symbol bit temp right
      have hone := programmeTM2_one_step_in_time hstep
      rcases ih (some bit :: right) (some bit) with ⟨hrest⟩
      refine ⟨?_⟩
      have hrun :=
        StateTransition.EvalsToInTime.trans
          (programmeTM2Machine M).step
          1 (temp.length + 1)
          (programmeTM2InitCfg M .initToRight symbol [] (bit :: temp) right)
          (programmeTM2InitCfg M .initToRight (some bit) [] temp (some bit :: right))
          (some
            (programmeTM2InitCfg M .initFinish none [] []
              (temp.reverse.map some ++ some bit :: right)))
          hone hrest
      simpa [List.reverse_cons, List.map_append, List.append_assoc,
        Nat.add_assoc] using hrun

/-- Canonical run-mode configuration reached after the two initialization passes. -/
def programmeTM2ReadyInitCfg (M : ProgrammeMachine) (input : List Bool) :
    (programmeTM2Machine M).Cfg where
  l := some (.run)
  var :=
    { programmeTM2InitialState M with
        mode := .run
        inputSymbol := input.head? }
  stk := programmeTM2InitStacks M [] [] (input.tail.map some)

/-- Loading the first restored cell yields the canonical run-mode input representation. -/
theorem programmeTM2_step_initFinish_input (M : ProgrammeMachine) (input : List Bool) :
    (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initFinish none [] [] (input.map some)) =
      some (programmeTM2ReadyInitCfg M input) := by
  rw [programmeTM2_step_initFinish]
  cases input <;>
    rfl

/-- Reverse-simulator initialization is exactly linear: 2*n + 3 FinTM2 steps. -/
theorem programmeTM2_initialization_run (M : ProgrammeMachine) (input : List Bool) :
    Nonempty
      (StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (Turing.initList (programmeTM2Machine M) input)
        (some (programmeTM2ReadyInitCfg M input))
        (2 * input.length + 3)) := by
  rcases programmeTM2_initToTemp_run M input [] none [] with ⟨hfirstRaw⟩
  have hfirst :
      StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToTemp none input [] [])
        (some (programmeTM2InitCfg M .initToRight none [] input.reverse []))
        (input.length + 1) := by
    simpa using hfirstRaw
  rcases programmeTM2_initToRight_run M input.reverse [] none with ⟨hsecondRaw⟩
  have hsecond :
      StateTransition.EvalsToInTime
        (programmeTM2Machine M).step
        (programmeTM2InitCfg M .initToRight none [] input.reverse [])
        (some (programmeTM2InitCfg M .initFinish none [] [] (input.map some)))
        (input.length + 1) := by
    simpa using hsecondRaw
  have hlast :=
    programmeTM2_one_step_in_time
      (programmeTM2_step_initFinish_input M input)
  have h12 :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (input.length + 1) (input.length + 1)
      (programmeTM2InitCfg M .initToTemp none input [] [])
      (programmeTM2InitCfg M .initToRight none [] input.reverse [])
      (some (programmeTM2InitCfg M .initFinish none [] [] (input.map some)))
      hfirst hsecond
  have hall :=
    StateTransition.EvalsToInTime.trans
      (programmeTM2Machine M).step
      (input.length + 1 + (input.length + 1)) 1
      (programmeTM2InitCfg M .initToTemp none input [] [])
      (programmeTM2InitCfg M .initFinish none [] [] (input.map some))
      (some (programmeTM2ReadyInitCfg M input))
      h12 hlast
  rw [programmeTM2_initList_eq_cfg M input]
  exact ⟨programmeTM2_evalsToInTime_mono hall (by omega)⟩

#print axioms programmeTM2_initList_eq_cfg
#print axioms programmeTM2_step_initToTemp_cons
#print axioms programmeTM2_step_initToTemp_nil
#print axioms programmeTM2_step_initToRight_cons
#print axioms programmeTM2_step_initToRight_nil
#print axioms programmeTM2_step_initFinish
#print axioms programmeTM2_initToTemp_run
#print axioms programmeTM2_initToRight_run
#print axioms programmeTM2_step_initFinish_input
#print axioms programmeTM2_initialization_run
#print axioms programmeTM2_one_step_in_time

end

end MathSolve.PNP

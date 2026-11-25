import MathSolve.PNP.ProgrammeTM2RunSimulation

/-! A deliberately conservative affine storage bound on native finite stacks. -/
namespace MathSolve.PNP
noncomputable section

abbrev ReverseStacks (M : ProgrammeMachine) :=
  ∀ k : ProgrammeTM2Stack M.workTapeCount, List (programmeTM2StackAlphabet M k)

def ReverseStackBound (M : ProgrammeMachine) (S : ReverseStacks M) (b : Nat) : Prop :=
  ∀ k, (S k).length ≤ b

theorem reverseStackBound_update (M : ProgrammeMachine) (S : ReverseStacks M)
    (b : Nat) (k : ProgrammeTM2Stack M.workTapeCount)
    (v : List (programmeTM2StackAlphabet M k))
    (h : ReverseStackBound M S b) (hv : v.length ≤ b) :
    ReverseStackBound M (Function.update S k v) b := by
  intro j
  by_cases he : j = k
  · subst j; simpa using hv
  · simpa [Function.update_of_ne he] using h j

theorem reverseStackBound_mono (M : ProgrammeMachine) (S : ReverseStacks M)
    (a b : Nat) (h : ReverseStackBound M S a) (hab : a ≤ b) : ReverseStackBound M S b :=
  fun k => (h k).trans hab

private theorem reverseCons_bound {α : Type*} (x : α) (xs : List α) (b : Nat)
    (h : xs.length ≤ b) : (x :: xs).length ≤ b + 1 := by
  exact Nat.succ_le_succ h

private theorem reverseTail_bound {α : Type*} (xs : List α) (b : Nat)
    (h : xs.length ≤ b) : xs.tail.length ≤ b + 1 := by
  cases xs <;> simp_all <;> omega

/-- Both stack mutations of a single work move grow the uniform length bound by at most one. -/
theorem reverseWorkUpdate_bound (M : ProgrammeMachine) (c : ReverseCfg M)
    (k : Fin M.workTapeCount) (b : Nat) (hb : ReverseStackBound M c.stk b) :
    ReverseStackBound M (reverseWorkUpdate M k c).stk (b+1) := by
  have hb' := reverseStackBound_mono M c.stk b (b+1) hb (by omega)
  cases h : (c.var.snapshotAction M).workMove k with
  | left =>
    simp only [reverseWorkUpdate, h]
    exact reverseStackBound_update M _ (b+1) (.workLeft k) _
      (reverseStackBound_update M c.stk (b+1) (.workRight k) _ hb'
        (reverseCons_bound _ _ b (hb (.workRight k))))
      (reverseTail_bound _ b (hb (.workLeft k)))
  | right =>
    simp only [reverseWorkUpdate, h]
    exact reverseStackBound_update M _ (b+1) (.workRight k) _
      (reverseStackBound_update M c.stk (b+1) (.workLeft k) _ hb'
        (reverseCons_bound _ _ b (hb (.workLeft k))))
      (reverseTail_bound _ b (hb (.workRight k)))
  | stay => simpa only [reverseWorkUpdate, h] using hb'

theorem reverseInputUpdate_bound (M : ProgrammeMachine) (c : ReverseCfg M)
    (b : Nat) (hb : ReverseStackBound M c.stk b) :
    ReverseStackBound M (reverseInputUpdate M c).stk (b+1) := by
  have hb' := reverseStackBound_mono M c.stk b (b+1) hb (by omega)
  cases h : (c.var.snapshotAction M).inputMove with
  | left =>
    simp only [reverseInputUpdate, h]
    exact reverseStackBound_update M _ (b+1) .inputLeft _
      (reverseStackBound_update M c.stk (b+1) .inputRight _ hb'
        (reverseCons_bound _ _ b (hb .inputRight)))
      (reverseTail_bound _ b (hb .inputLeft))
  | right =>
    simp only [reverseInputUpdate, h]
    exact reverseStackBound_update M _ (b+1) .inputRight _
      (reverseStackBound_update M c.stk (b+1) .inputLeft _ hb'
        (reverseCons_bound _ _ b (hb .inputLeft)))
      (reverseTail_bound _ b (hb .inputRight))
  | stay => simpa only [reverseInputUpdate, h] using hb'

theorem reverseWorkFold_bound (M : ProgrammeMachine) (ks : List (Fin M.workTapeCount))
    (c : ReverseCfg M) (b : Nat) (hb : ReverseStackBound M c.stk b) :
    ReverseStackBound M (reverseWorkFold M ks c).stk (b + ks.length) := by
  induction ks generalizing c b with
  | nil => simpa [reverseWorkFold] using hb
  | cons k ks ih =>
    have h := ih (reverseWorkUpdate M k c) (b+1) (reverseWorkUpdate_bound M c k b hb)
    simpa [reverseWorkFold, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using h

theorem reverseRunPhysical_bound (M : ProgrammeMachine) (c : ReverseCfg M)
    (b : Nat) (hb : ReverseStackBound M c.stk b) :
    ReverseStackBound M (reverseRunPhysical M c).stk (b + (M.workTapeCount+1)) := by
  let snap : ReverseCfg M := { c with var := c.var.snapshot M }
  have h := reverseWorkFold_bound M (programmeTM2WorkTapes M) (reverseInputUpdate M snap)
    (b+1) (reverseInputUpdate_bound M snap b hb)
  simpa [reverseRunPhysical, snap, programmeTM2WorkTapes, Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using h

theorem reverseWorkUpdate_output (M : ProgrammeMachine) (k : Fin M.workTapeCount) (c : ReverseCfg M) :
    (reverseWorkUpdate M k c).stk .output = c.stk .output := by
  cases h : (c.var.snapshotAction M).workMove k <;> simp [reverseWorkUpdate, h, Function.update_of_ne]

theorem reverseInputUpdate_output (M : ProgrammeMachine) (c : ReverseCfg M) :
    (reverseInputUpdate M c).stk .output = c.stk .output := by
  cases h : (c.var.snapshotAction M).inputMove <;> simp [reverseInputUpdate, h, Function.update_of_ne]

theorem reverseWorkFold_output (M : ProgrammeMachine) (ks : List (Fin M.workTapeCount)) (c : ReverseCfg M) :
    (reverseWorkFold M ks c).stk .output = c.stk .output := by
  induction ks generalizing c with
  | nil => rfl
  | cons k ks ih => simp only [reverseWorkFold, ih, reverseWorkUpdate_output]

theorem reverseRunPhysical_output (M : ProgrammeMachine) (c : ReverseCfg M) :
    (reverseRunPhysical M c).stk .output = c.stk .output := by
  simp [reverseRunPhysical, reverseWorkFold_output, reverseInputUpdate_output]

/-- Exact arbitrary iteration with a physical size bound and untouched output stack. -/
theorem programmeTM2_simulates_iterate_budget (M : ProgrammeMachine) (input : List Bool) :
    ∀ (n : Nat) (source source' : ProgrammeConfig M) (target : ReverseCfg M) (b : Nat),
      ProgrammeTM2Represents M input source target → ReverseStackBound M target.stk b →
      target.stk .output = [] → ((flip bind (M.step input))^[n]) (some source) = some source' →
      ∃ target', ProgrammeTM2Represents M input source' target' ∧
        ((flip bind (programmeTM2Machine M).step)^[n]) (some target) = some target' ∧
        ReverseStackBound M target'.stk (b+(M.workTapeCount+1)*n) ∧ target'.stk .output = [] := by
  intro n
  induction n with
  | zero =>
    intro source source' target b hrep hb ho hs
    simp only [Function.iterate_zero_apply] at hs
    cases Option.some.inj hs
    exact ⟨target, hrep, rfl, by simpa using hb, ho⟩
  | succ n ih =>
    intro source source' target b hrep hb ho hs
    rw [Function.iterate_succ_apply'] at hs
    generalize hm : ((flip bind (M.step input))^[n]) (some source) = mid at hs
    cases mid with
    | none => simp [flip] at hs
    | some middle =>
      have hstep : M.step input middle = some source' := by simpa using hs
      rcases ih source middle target b hrep hb ho hm with ⟨tm, hrm, htm, hbm, hom⟩
      have ha : middle.state ≠ M.accept := by
        intro h; rw [M.step_eq_none_of_accept input middle h] at hstep; contradiction
      have hr : middle.state ≠ M.reject := by
        intro h; rw [M.step_eq_none_of_reject input middle h] at hstep; contradiction
      have ht := programmeTM2_step_run_nonterminal hrm ha hr
      have hnew := programmeTM2_runStepTarget_represents hrm
      have he := Option.some.inj ((M.step_eq_some_afterAction input middle ha hr).symm.trans hstep)
      subst source'
      refine ⟨programmeTM2RunStepTarget M tm, hnew, ?_, ?_, ?_⟩
      · rw [Function.iterate_succ_apply', htm]; simpa using ht
      · rw [reverseRunPhysical_exec]
        simpa [Nat.mul_succ, Nat.add_assoc] using reverseRunPhysical_bound M tm _ hbm
      · rw [reverseRunPhysical_exec, reverseRunPhysical_output, hom]

/-- The canonical normalized input has no output and every stack has length at most n. -/
theorem programmeTM2ReadyInitCfg_budget (M : ProgrammeMachine) (input : List Bool) :
    ReverseStackBound M (programmeTM2ReadyInitCfg M input).stk input.length ∧
      (programmeTM2ReadyInitCfg M input).stk .output = [] := by
  refine ⟨?_,rfl⟩
  intro k
  cases k <;> first | (change 0 ≤ input.length; exact Nat.zero_le _) |
    (change (input.tail.map some).length ≤ input.length; rw [List.length_map, List.length_tail]; omega)

/-- A bounded source execution from initialization arrives at the represented
terminal (or intermediate) state with every physical stack still bounded. -/
theorem programmeTM2_simulates_from_init_budget {M : ProgrammeMachine} {input : List Bool}
    {source' : ProgrammeConfig M} {bound : Nat}
    (hrun : StateTransition.EvalsToInTime (M.step input) (M.init input) (some source') bound) :
    ∃ target', ProgrammeTM2Represents M input source' target' ∧
      Nonempty (StateTransition.EvalsToInTime (programmeTM2Machine M).step
        (Turing.initList (programmeTM2Machine M) input) (some target') (2*input.length+3+bound)) ∧
      ReverseStackBound M target'.stk (input.length+(M.workTapeCount+1)*bound) ∧ target'.stk .output = [] := by
  have hb := programmeTM2ReadyInitCfg_budget M input
  rcases programmeTM2_simulates_iterate_budget M input hrun.steps (M.init input) source'
      (programmeTM2ReadyInitCfg M input) input.length (programmeTM2ReadyInitCfg_represents M input)
      hb.1 hb.2 hrun.evals_in_steps with ⟨target', hrep, hs, hbound, ho⟩
  have ht : StateTransition.EvalsToInTime (programmeTM2Machine M).step
      (programmeTM2ReadyInitCfg M input) (some target') bound :=
    { steps := hrun.steps, evals_in_steps := hs, steps_le_m := hrun.steps_le_m }
  rcases programmeTM2_initialization_run M input with ⟨hi⟩
  refine ⟨target', hrep, ⟨?_⟩, ?_, ho⟩
  · simpa only [Nat.add_comm bound (2 * input.length + 3)] using
      (StateTransition.EvalsToInTime.trans (programmeTM2Machine M).step
        (2*input.length+3) bound _ _ _ hi ht)
  · apply reverseStackBound_mono M _ _ _ hbound
    exact Nat.add_le_add_left (Nat.mul_le_mul_left _ hrun.steps_le_m) _

#print axioms reverseRunPhysical_bound
#print axioms programmeTM2_simulates_iterate_budget
#print axioms programmeTM2_simulates_from_init_budget
end
end MathSolve.PNP

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

/-- Both stack mutations of a single work move grow the uniform length bound by at most one. -/
theorem reverseWorkUpdate_bound (M : ProgrammeMachine) (c : ReverseCfg M)
    (k : Fin M.workTapeCount) (b : Nat) (hb : ReverseStackBound M c.stk b) :
    ReverseStackBound M (reverseWorkUpdate M k c).stk (b+1) := by
  have hb' := reverseStackBound_mono M c.stk b (b+1) hb (by omega)
  cases h : (c.var.snapshotAction M).workMove k with
  | left =>
    simp only [reverseWorkUpdate, h]
    apply reverseStackBound_update
    · apply reverseStackBound_update M _ _ _ _ hb'
      simp only [List.length_cons]; have := hb (.workRight k); omega
    · have ht := (show (c.stk (.workLeft k)).tail.length ≤ (c.stk (.workLeft k)).length by rw [List.length_tail]; omega); have := hb (.workLeft k); omega
  | right =>
    simp only [reverseWorkUpdate, h]
    apply reverseStackBound_update
    · apply reverseStackBound_update M _ _ _ _ hb'
      simp only [List.length_cons]; have := hb (.workLeft k); omega
    · have ht := (show (c.stk (.workRight k)).tail.length ≤ (c.stk (.workRight k)).length by rw [List.length_tail]; omega); have := hb (.workRight k); omega
  | stay => simpa only [reverseWorkUpdate, h] using hb'

theorem reverseInputUpdate_bound (M : ProgrammeMachine) (c : ReverseCfg M)
    (b : Nat) (hb : ReverseStackBound M c.stk b) :
    ReverseStackBound M (reverseInputUpdate M c).stk (b+1) := by
  have hb' := reverseStackBound_mono M c.stk b (b+1) hb (by omega)
  cases h : (c.var.snapshotAction M).inputMove with
  | left =>
    simp only [reverseInputUpdate, h]
    apply reverseStackBound_update
    · apply reverseStackBound_update M _ _ _ _ hb'
      simp only [List.length_cons]; have := hb .inputRight; omega
    · have ht := (show (c.stk .inputLeft).tail.length ≤ (c.stk .inputLeft).length by rw [List.length_tail]; omega); have := hb .inputLeft; omega
  | right =>
    simp only [reverseInputUpdate, h]
    apply reverseStackBound_update
    · apply reverseStackBound_update M _ _ _ _ hb'
      simp only [List.length_cons]; have := hb .inputLeft; omega
    · have ht := (show (c.stk .inputRight).tail.length ≤ (c.stk .inputRight).length by rw [List.length_tail]; omega); have := hb .inputRight; omega
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

end
end MathSolve.PNP

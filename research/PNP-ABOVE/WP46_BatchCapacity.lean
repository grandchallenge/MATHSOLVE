import PNPAbove.WP45Selector

namespace PNPAbove.WP46
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun Polynomial

variable {α β γ : Type} [SizedEncoding α] [SizedEncoding β] [SizedEncoding γ]

/-- Binary advice is charged as program text, and conversion to a unary
clock is charged as execution. -/
def budgetPrefix : Prog :=
  .elim 0 .nil (.cons (Prog.callVar 0 Prog.toUnaryProg) (.var 1))

theorem budgetPrefix_scoped : budgetPrefix.WellScoped 1 := by
  exact ⟨by decide,trivial,Prog.callVar_wellScoped (by decide) Prog.toUnaryProg_wellScoped,by simp [Prog.WellScoped]⟩

theorem budgetPrefix_runs (B : Nat) (x : Data) :
    ∃ t ≤ (Nat.size B + 2) * ((B+1)*(4*B+14)+7*esize B+8*B+90)
          + esize B + x.size + 5,
      budgetPrefix.Runs (.cons (encode B) x) (.cons (Data.ofNat B) x) t := by
  obtain ⟨s,hs,hr⟩ := Prog.toUnaryProg_runs B
  have hcall := Prog.callVar_eval (env := [encode B,x,.cons (encode B) x])
    (i := 0) Prog.toUnaryProg_wellScoped (v := encode B) (by simp) hr
  have hvar := Eval.var_of_get (env := [encode B,x,.cons (encode B) x]) (i := 1)
    (v := x) (by simp)
  refine ⟨_,?_,Eval.elim_cons (i := 0) (n := .nil) (by simp)
    (Eval.cons hcall hvar)⟩
  change (esize B+1+s+1)+(x.size+1)+1+1 ≤ _
  omega

noncomputable def budgetCore (A : PolyTimeFun (Unary × α) β) : Prog :=
  .let_ budgetPrefix A.code

noncomputable def fixedBudget (A : PolyTimeFun (Unary × α) β) (B : Nat) : Prog :=
  hardcode (budgetCore A) (encode B)

theorem budgetCore_scoped (A : PolyTimeFun (Unary × α) β) :
    (budgetCore A).WellScoped 1 :=
  ⟨budgetPrefix_scoped,A.closed.mono (by omega) A.code⟩

theorem fixedBudget_scoped (A : PolyTimeFun (Unary × α) β) (B : Nat) :
    (fixedBudget A B).WellScoped 1 :=
  hardcode_wellScoped (budgetCore_scoped A) _

theorem fixedBudget_size (A : PolyTimeFun (Unary × α) β) (B : Nat) :
    esize (fixedBudget A B) = esize (budgetCore A) + esize B + 35 :=
  hardcode_size _ _

theorem binary_size_le (B : Nat) : Nat.size B ≤ B :=
  Nat.size_le.mpr B.lt_two_pow_self

theorem binary_power_le (B : Nat) : 2^Nat.size B ≤ 2*(B+1) := by
  cases h : Nat.size B with
  | zero => simp; omega
  | succ n =>
    have hn : n < Nat.size B := by omega
    have hp := Nat.lt_size.mp hn
    rw [pow_succ]
    omega

theorem encoded_binary_power_le (B : Nat) :
    2^(esize B) ≤ 32*(B+1)^4 := by
  calc
    2^(esize B) ≤ 2^(4*Nat.size B+1) :=
      Nat.pow_le_pow_right (by decide) (esize_nat_le B)
    _ = 2*(2^Nat.size B)^4 := by
      rw [pow_succ,Nat.mul_comm 4 (Nat.size B),pow_mul]
      ring
    _ ≤ 2*(2*(B+1))^4 := Nat.mul_le_mul_left _
      (Nat.pow_le_pow_left (binary_power_le B) 4)
    _ = _ := by ring

noncomputable def conversionBound : Polynomial Nat :=
  (X+2)*((X+1)*(4*X+14)+7*(4*X+1)+8*X+90)

noncomputable def executionBound (A : PolyTimeFun (Unary × α) β) : Polynomial Nat :=
  conversionBound + A.timeBound.comp (2*X+2) + 8*X+12

theorem conversion_bound (B S : Nat) (h : B ≤ S) :
    (Nat.size B+2)*((B+1)*(4*B+14)+7*esize B+8*B+90) ≤
      conversionBound.eval S := by
  have hs := (binary_size_le B).trans h
  have he : esize B ≤ 4*S+1 := by
    have := esize_nat_le B
    omega
  simp [conversionBound]
  apply Nat.mul_le_mul (by omega)
  have hm : (B+1)*(4*B+14) ≤ (S+1)*(4*S+14) :=
    Nat.mul_le_mul (by omega) (by omega)
  omega

theorem fixedBudget_runs (A : PolyTimeFun (Unary × α) β) (B : Nat) (a : α) :
    ∃ t, (fixedBudget A B).Runs (encode a) (encode (A (unary B,a))) t ∧
      t+1 ≤ (executionBound A).eval (B+esize a) := by
  obtain ⟨s,hs,hr⟩ := budgetPrefix_runs B (encode a)
  obtain ⟨t,ht,ha⟩ := A.computes (unary B,a)
  have hx : encode (unary B,a) = Data.cons (Data.ofNat B) (encode a) := by
    rw [encode_prod,encode_unary]
  rw [hx] at ha
  have hcore : (budgetCore A).Runs (.cons (encode B) (encode a))
      (encode (A (unary B,a))) (s+t+1) :=
    Eval.let_ hr (Eval.append_of_wellScoped ha A.closed [Data.cons (encode B) (encode a)])
  refine ⟨s+t+1+esize B+esize a+3,hardcode_time (budgetCore_scoped A) hcore,?_⟩
  let S := B+esize a
  have hS : B ≤ S := by dsimp [S]; omega
  have hb := conversion_bound B S hS
  have hu : esize (unary B,a) ≤ 2*S+2 := by
    rw [esize_prod]
    have h : esize (unary B) = 2*B+1 := by
      change (encode (unary B) : Data).size = _
      rw [encode_unary,Data.size_ofNat]
    rw [h]; dsimp [S]; omega
  have htime := ht.trans (polynomial_eval_mono A.timeBound hu)
  have hcode := esize_nat_le B
  have hbits := binary_size_le B
  change s ≤ _ + esize B + esize a + 5 at hs
  change s+t+1+esize B+esize a+3+1 ≤ (executionBound A).eval S
  simp only [executionBound,Polynomial.eval_add,Polynomial.eval_mul,Polynomial.eval_comp,
    Polynomial.eval_X,Polynomial.eval_ofNat]
  dsimp [S] at *
  omega

noncomputable def weightedBound (A : PolyTimeFun (Unary × α) β) : Polynomial Nat :=
  C (2^(esize (budgetCore A)+35)*32) * (X+1)^4 * executionBound A

theorem fixedBudget_weighted (A : PolyTimeFun (Unary × α) β) (B : Nat) (a : α) :
    ∃ t, (fixedBudget A B).Runs (encode a) (encode (A (unary B,a))) t ∧
      2^(esize (fixedBudget A B))*(t+1) ≤ (weightedBound A).eval (B+esize a) := by
  obtain ⟨t,hr,ht⟩ := fixedBudget_runs A B a
  refine ⟨t,hr,?_⟩
  rw [fixedBudget_size,show esize (budgetCore A)+esize B+35 =
    (esize (budgetCore A)+35)+esize B by omega,pow_add]
  have he := encoded_binary_power_le B
  have hp : (B+1)^4 ≤ (B+esize a+1)^4 := Nat.pow_le_pow_left (by omega) _
  have hh := Nat.mul_le_mul_left 32 hp
  simp only [weightedBound,Polynomial.eval_mul,Polynomial.eval_C,Polynomial.eval_pow,
    Polynomial.eval_add,Polynomial.eval_X,Polynomial.eval_one]
  calc
    2^(esize (budgetCore A)+35)*2^(esize B)*(t+1)
        ≤ (2^(esize (budgetCore A)+35)*(32*(B+esize a+1)^4))*
          (executionBound A).eval (B+esize a) :=
      Nat.mul_le_mul (Nat.mul_le_mul_left _ (he.trans hh)) ht
    _ = _ := by ring

def LocalCheap (V : PolyTimeFun (α × BitStr) Bool) (B : Nat) (a : α) : Prop :=
  ∃ c : Prog, ∃ w : BitStr, ∃ t : Nat,
    c.WellScoped 1 ∧ c.Runs (encode a) (encode w) t ∧
    V (a,w) = true ∧ 2^(esize c)*(t+1) ≤ B

def BatchGood (V : PolyTimeFun (α × BitStr) Bool)
    (xs : List α) (ws : List BitStr) : Prop :=
  List.Forall₂ (fun a w => V (a,w) = true) xs ws

noncomputable def batchP (V : PolyTimeFun (α × BitStr) Bool) :
    PolyTimeFun (Unary × List α) (List BitStr) :=
  (mapWith ((WP45.budgetSelector selfClockedUniversal V).comp (snd.pair fst))).comp
    (snd.pair fst)

theorem batchP_correct (V : PolyTimeFun (α × BitStr) Bool) (u : Unary) (xs : List α) :
    batchP V (u,xs) = xs.map (fun a => WP45.budgetSelector selfClockedUniversal V (u,a)) := rfl

theorem batchP_good (V : PolyTimeFun (α × BitStr) Bool) (B : Nat) (xs : List α)
    (h : ∀ a ∈ xs, LocalCheap V B a) :
    BatchGood V xs (batchP V (unary B,xs)) := by
  rw [batchP_correct]
  unfold BatchGood
  induction xs with
  | nil => exact .nil
  | cons a xs ih =>
    apply List.Forall₂.cons
    · obtain ⟨c,w,t,_,hr,hv,hb⟩ := h a (by simp)
      have hp : 0 < 2^(esize c) := by positivity
      have hc := (Nat.le_mul_of_pos_right (2^(esize c)) (by omega : 0 < t+1)).trans hb
      have ht := (Nat.le_mul_of_pos_left (t+1) hp).trans hb
      apply WP45.budgetSelector_complete selfClockedUniversal V _ _ c w t _ _ hr hv
      · simpa using hc
      · simp; omega
    · exact ih (fun a ha => h a (by simp [ha]))

theorem batch_weighted_bound (V : PolyTimeFun (α × BitStr) Bool) :
    ∃ q : Polynomial Nat, ∀ (B : Nat) (xs : List α),
      (∀ a ∈ xs, LocalCheap V B a) →
      ∃ c : Prog, ∃ ws : List BitStr, ∃ t : Nat,
        c.WellScoped 1 ∧ c.Runs (encode xs) (encode ws) t ∧ BatchGood V xs ws ∧
          2^(esize c)*(t+1) ≤ q.eval (B+esize xs) := by
  refine ⟨weightedBound (batchP V),?_⟩
  intro B xs h
  obtain ⟨t,hr,ht⟩ := fixedBudget_weighted (batchP V) B xs
  exact ⟨_,_,t,fixedBudget_scoped _ _,hr,batchP_good V B xs h,ht⟩

noncomputable def jointP (V : PolyTimeFun (α × BitStr) Bool)
    (D : PolyTimeFun γ (List α)) (J : PolyTimeFun (γ × List BitStr) BitStr) :
    PolyTimeFun (Unary × γ) BitStr :=
  J.comp (snd.pair ((batchP V).comp (fst.pair (D.comp snd))))

theorem jointP_correct (V : PolyTimeFun (α × BitStr) Bool)
    (D : PolyTimeFun γ (List α)) (J : PolyTimeFun (γ × List BitStr) BitStr)
    (u : Unary) (x : γ) :
    jointP V D J (u,x) = J (x,batchP V (u,D x)) := rfl

theorem decomposable_weighted_bound (V : PolyTimeFun (α × BitStr) Bool)
    (W : PolyTimeFun (γ × BitStr) Bool)
    (D : PolyTimeFun γ (List α)) (J : PolyTimeFun (γ × List BitStr) BitStr)
    (lift : ∀ x ws, BatchGood V (D x) ws → W (x,J (x,ws)) = true) :
    ∃ q : Polynomial Nat, ∀ (B : Nat) (x : γ),
      (∀ a ∈ D x, LocalCheap V B a) →
      LocalCheap W (q.eval (B+esize x)) x := by
  refine ⟨weightedBound (jointP V D J),?_⟩
  intro B x h
  obtain ⟨t,hr,ht⟩ := fixedBudget_weighted (jointP V D J) B x
  refine ⟨_,_,t,fixedBudget_scoped _ _,hr,?_,ht⟩
  rw [jointP_correct]
  exact lift x _ (batchP_good V B (D x) h)

/-- A joint obstruction exceeding the polynomial assembly allowance
forces an obstruction in at least one component. -/
theorem decomposable_bad_component (V : PolyTimeFun (α × BitStr) Bool)
    (W : PolyTimeFun (γ × BitStr) Bool)
    (D : PolyTimeFun γ (List α)) (J : PolyTimeFun (γ × List BitStr) BitStr)
    (lift : ∀ x ws, BatchGood V (D x) ws → W (x,J (x,ws)) = true) :
    ∃ q : Polynomial Nat, ∀ (B : Nat) (x : γ),
      ¬ LocalCheap W (q.eval (B+esize x)) x →
      ∃ a ∈ D x, ¬ LocalCheap V B a := by
  classical
  obtain ⟨q,hq⟩ := decomposable_weighted_bound V W D J lift
  refine ⟨q,?_⟩
  intro B x hb
  by_contra hn
  apply hb
  apply hq
  intro a ha
  by_contra hf
  exact hn ⟨a,ha,hf⟩

/-- Even nonuniform, instance-specific cheap components suffice to
construct one uniform polynomial solver for the joint relation. -/
theorem polynomial_decomposition_solves (V : PolyTimeFun (α × BitStr) Bool)
    (W : PolyTimeFun (γ × BitStr) Bool)
    (D : PolyTimeFun γ (List α)) (J : PolyTimeFun (γ × List BitStr) BitStr)
    (lift : ∀ x ws, BatchGood V (D x) ws → W (x,J (x,ws)) = true)
    (p : Polynomial Nat)
    (h : ∀ x, WP45.HasWitness W x →
      ∀ a ∈ D x, LocalCheap V (p.eval (esize x)) a) :
    ∃ S : PolyTimeFun γ BitStr, WP45.Solves W S := by
  obtain ⟨q,hq⟩ := decomposable_weighted_bound V W D J lift
  apply (WP45.weightedBound_iff_solver_native W).1
  refine ⟨q.comp (p+X),?_⟩
  intro x hx
  change LocalCheap W ((q.comp (p+X)).eval (esize x)) x
  simpa only [Polynomial.eval_comp,Polynomial.eval_add,Polynomial.eval_X]
    using hq (p.eval (esize x)) x (h x hx)

end PNPAbove.WP46

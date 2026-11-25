import PNPAbove.WP12

namespace PNPAbove.WP13
open MIPRE MIPRE.Cost MIPRE.CL

/-- A nine-level presentation: identity at level one and eight empty stages. -/
def trivialStages : (k : Nat) → CLFun 𝔽₂ (Fin 9) k
  | 0 => .zero
  | k + 1 => .cons ∅ 0 (fun _ => trivialStages k)

def diagonalCL : CLFun 𝔽₂ (Fin 9) 9 :=
  .cons Finset.univ (RegLinear.id Finset.univ) (fun _ => trivialStages 8)

theorem trivialStages_exactlyOn (k : Nat) :
    (trivialStages k).ExactlyOn ∅ := by
  induction k with
  | zero => rfl
  | succ k ih => exact ⟨by simp, fun _ => by simpa [trivialStages] using ih⟩

theorem diagonalCL_exactlyOn : diagonalCL.ExactlyOn Finset.univ := by
  exact ⟨Finset.Subset.refl _, fun _ => by
    simpa [diagonalCL] using trivialStages_exactlyOn 8⟩


/-- Empty later levels contribute no value to any marginal. -/
theorem trivialStages_truncate_zero (k j : Nat) (x : Fin 9 → 𝔽₂) :
    ((trivialStages k).truncate j).eval x = 0 := by
  induction j generalizing k with
  | zero => simp
  | succ j ih =>
      cases k with
      | zero => simp [trivialStages]
      | succ k => simp [trivialStages, ih]

/-- Empty later levels have zero maps and empty factors. -/
theorem trivialStages_map_zero (k j : Nat) (u y : Fin 9 → 𝔽₂) :
    ((trivialStages k).mapOfPrefix j u) y = 0 := by
  induction j generalizing k with
  | zero => cases k <;> simp [trivialStages]
  | succ j ih => cases k <;> simp [trivialStages, ih]

theorem trivialStages_factor_empty (k j : Nat) (u : Fin 9 → 𝔽₂) :
    (trivialStages k).factorOfPrefix j u = ∅ := by
  induction j generalizing k with
  | zero => cases k <;> rfl
  | succ j ih => cases k <;> simp [trivialStages, ih]

/-- The nondegenerate first stage is identity, every other stage contributes zero. -/
theorem diagonalCL_truncate (j : Nat) (hj : 1 ≤ j) (x : Fin 9 → 𝔽₂) :
    (diagonalCL.truncate j).eval x = x := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : j ≠ 0)
  simp [diagonalCL, RegLinear.id_apply]

theorem diagonalCL_map_first (u y : Fin 9 → 𝔽₂) :
    (diagonalCL.mapOfPrefix 0 u) y = y := by
  simp [diagonalCL, RegLinear.id]

theorem diagonalCL_map_later (j : Nat) (hj : 1 ≤ j)
    (u y : Fin 9 → 𝔽₂) :
    (diagonalCL.mapOfPrefix j u) y = 0 := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : j ≠ 0)
  simp [diagonalCL, trivialStages_map_zero]

theorem diagonalCL_factor_first (u : Fin 9 → 𝔽₂) :
    diagonalCL.factorOfPrefix 0 u = Finset.univ := by
  rfl

theorem diagonalCL_factor_later (j : Nat) (hj : 1 ≤ j)
    (u : Fin 9 → 𝔽₂) :
    diagonalCL.factorOfPrefix j u = ∅ := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : j ≠ 0)
  simp [diagonalCL, trivialStages_factor_empty]

/-- Normalization lemmas for the finite binary query tags and legal nine stages. -/
@[simp] theorem bits_0 : Nat.bits (0:Nat) = [] := by decide
@[simp] theorem bits_1 : Nat.bits (1:Nat) = [true] := by decide
@[simp] theorem bits_2 : Nat.bits (2:Nat) = [false, true] := by decide
@[simp] theorem bits_3 : Nat.bits (3:Nat) = [true, true] := by decide
@[simp] theorem bits_4 : Nat.bits (4:Nat) = [false, false, true] := by decide
@[simp] theorem bits_5 : Nat.bits (5:Nat) = [true, false, true] := by decide
@[simp] theorem bits_6 : Nat.bits (6:Nat) = [false, true, true] := by decide
@[simp] theorem bits_7 : Nat.bits (7:Nat) = [true, true, true] := by decide
@[simp] theorem bits_8 : Nat.bits (8:Nat) = [false, false, false, true] := by decide
@[simp] theorem bits_9 : Nat.bits (9:Nat) = [true, false, false, true] := by decide

/-- The source program's canonical bit-string query outputs. -/
def zeroBits : Data := encode (List.replicate 9 false : BitStr)
def oneBits : Data := encode (List.replicate 9 true : BitStr)

def selectStageOne (yes no : Prog) : Prog :=
  .elim 0 no (.elim 0 no (.elim 3 yes no))

def readStageAt (idx : Nat) (yes no : Prog) : Prog :=
  .elim idx no (.elim 1 no (selectStageOne yes no))

/-- In the success branch the `rest3` field at index 5 is `cons u y`;
read the field `y` without copying the rest of the unbounded input. -/
def copyLinearArgument : Prog := .elim 5 .nil (.var 1)

/-- When the kind is marginal, `rest` at index 5 is
`cons player (cons j (cons z nil))`; copy the query `z`. -/
def copyMarginalArgument : Prog :=
  .elim 5 .nil (.elim 1 .nil (.elim 1 .nil (.var 0)))

/-- One closed source program answering the four true MIPRE sampler queries.
Unexpected raw/malformed queries still halt without an extra decoder. -/
def samplerProg : Prog :=
  .elim 0 .nil
    (.elim 1 .nil
      (.elim 0 (.const (encode (9 : Nat)))
        (.elim 0
          (readStageAt 3 copyLinearArgument (.const zeroBits))
          (.elim 3 copyMarginalArgument
            (readStageAt 7 (.const oneBits) (.const zeroBits))))))

/-- Loop freedom ensures halting for every raw query, not only canonical ones. -/
theorem samplerProg_loopFree : WP11.LoopFree samplerProg := by
  simp [samplerProg, readStageAt, selectStageOne, copyLinearArgument,
    copyMarginalArgument, WP11.LoopFree]

theorem samplerProg_closed : samplerProg.WellScoped 1 := by
  simp [samplerProg, readStageAt, selectStageOne, copyLinearArgument,
    copyMarginalArgument, Prog.WellScoped]

theorem samplerProg_halts_raw (d : Data) :
    ∃ r t, Eval [d] samplerProg r t :=
  WP11.loopfree_terminates _ samplerProg_loopFree [d]




theorem eval_dimension (n : Nat) :
    WP12.evalValue samplerProg [encode (n, Sampler.Query.dimension)] =
      encode (9 : Nat) := by
  rfl

theorem eval_marginal (n : Nat) (w : Player) (j : Nat) (z : BitStr) :
    WP12.evalValue samplerProg [encode (n, Sampler.Query.marginal w j z)] =
      encode z := by
  simp [samplerProg, readStageAt, selectStageOne, copyMarginalArgument, copyLinearArgument,
    WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode, Data.ofList, Data.ofBool]

theorem eval_linear_first (n : Nat) (w : Player) (u y : BitStr) :
    WP12.evalValue samplerProg [encode (n, Sampler.Query.linear w 1 u y)] =
      encode y := by
  simp [samplerProg, readStageAt, selectStageOne, copyMarginalArgument, copyLinearArgument,
    WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode, Data.ofList, Data.ofBool]

theorem eval_linear_later (n : Nat) (w : Player) (j : Nat) (u y : BitStr)
    (hj : 2 ≤ j) (h9 : j ≤ 9) :
    WP12.evalValue samplerProg [encode (n, Sampler.Query.linear w j u y)] =
      zeroBits := by
  interval_cases j <;> simp [samplerProg, readStageAt, selectStageOne, copyMarginalArgument,
    copyLinearArgument, WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
    Data.ofList, Data.ofBool, zeroBits]

theorem eval_factor_first (n : Nat) (w : Player) (u : BitStr) :
    WP12.evalValue samplerProg [encode (n, Sampler.Query.factor w 1 u)] =
      oneBits := by
  simp [samplerProg, readStageAt, selectStageOne, copyMarginalArgument, copyLinearArgument,
    WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode, Data.ofList, Data.ofBool]

theorem eval_factor_later (n : Nat) (w : Player) (j : Nat) (u : BitStr)
    (hj : 2 ≤ j) (h9 : j ≤ 9) :
    WP12.evalValue samplerProg [encode (n, Sampler.Query.factor w j u)] =
      zeroBits := by
  interval_cases j <;> simp [samplerProg, readStageAt, selectStageOne, copyMarginalArgument,
    copyLinearArgument, WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
    Data.ofList, Data.ofBool, zeroBits]


/-- Canonical bit-string results for the two extremal factor spaces. -/
theorem toBits_zero9 : toBits (0 : Fin 9 → 𝔽₂) =
    List.replicate 9 false := by decide

theorem indicator_univ9 : indicatorBits (Finset.univ : Finset (Fin 9)) =
    List.replicate 9 true := by decide

theorem indicator_empty9 : indicatorBits (∅ : Finset (Fin 9)) =
    List.replicate 9 false := by decide

/-- Completeness of the independent structural evaluator is the actual
source `Eval` relation for this loop-free program. -/
theorem source_runs {d r : Data}
    (h : WP12.evalValue samplerProg [d] = r) :
    ∃ t, samplerProg.Runs d r t := by
  obtain ⟨t, ht⟩ := WP12.evalValue_sound samplerProg [d] samplerProg_loopFree
  exact ⟨t, h ▸ ht⟩

/-- Nine-dimensional, nine-level *diagonal identity* sampler: Alice and Bob
both receive the same nine-bit uniform seed; this is not a zero-output sampler. -/
def sampler9 : Sampler 9 where
  prog := samplerProg
  closed := samplerProg_closed
  dim := fun _ => 9
  cl := fun _ _ => diagonalCL
  cl_exactlyOn := fun _ _ => diagonalCL_exactlyOn
  runs_dimension := fun n => source_runs (eval_dimension n)
  runs_marginal := by
    intro n w j z hj h9 hz
    have hval : toBits ((diagonalCL.truncate j).eval (ofBits 9 z)) = z := by
      rw [diagonalCL_truncate j hj]
      exact toBits_ofBits hz
    simpa only [hval] using (source_runs (eval_marginal n w j z))
  runs_linear := by
    intro n w j u y hj h9 hu hy
    by_cases h1 : j = 1
    · subst j
      have hval : toBits ((diagonalCL.mapOfPrefix 0 (ofBits 9 u)) (ofBits 9 y)) = y := by
        rw [diagonalCL_map_first]
        exact toBits_ofBits hy
      simpa only [Nat.reduceSub, hval] using
        (source_runs (eval_linear_first n w u y))
    · have hj2 : 2 ≤ j := by omega
      have hval : toBits ((diagonalCL.mapOfPrefix (j - 1) (ofBits 9 u)) (ofBits 9 y)) =
          List.replicate 9 false := by
        rw [diagonalCL_map_later (j - 1) (by omega)]
        exact toBits_zero9
      simpa only [hval, zeroBits] using
        (source_runs (eval_linear_later n w j u y hj2 h9))
  runs_factor := by
    intro n w j u hj h9 hu
    by_cases h1 : j = 1
    · subst j
      have hval : indicatorBits (diagonalCL.factorOfPrefix 0 (ofBits 9 u)) =
          List.replicate 9 true := by
        rw [diagonalCL_factor_first]
        exact indicator_univ9
      simpa only [Nat.reduceSub, hval, oneBits] using
        (source_runs (eval_factor_first n w u))
    · have hj2 : 2 ≤ j := by omega
      have hval : indicatorBits (diagonalCL.factorOfPrefix (j - 1) (ofBits 9 u)) =
          List.replicate 9 false := by
        rw [diagonalCL_factor_later (j - 1) (by omega)]
        exact indicator_empty9
      simpa only [hval, zeroBits] using
        (source_runs (eval_factor_later n w j u hj2 h9))
  halts := fun n d => by
    obtain ⟨r,t,ht⟩ := samplerProg_halts_raw (.cons (encode n) d)
    exact ⟨r,t,ht⟩

/-- The source is genuinely seed-preserving and not zero-output. -/
theorem diagonalCL_eval (x : Fin 9 → 𝔽₂) : diagonalCL.eval x = x := by
  have h := diagonalCL_truncate 9 (by omega) x
  simpa only [CLFun.truncate_self] using h

theorem sampler9_nonconstant (n : Nat) :
    (sampler9.cl n .alice).eval (0 : Fin 9 → 𝔽₂) ≠
    (sampler9.cl n .alice).eval (1 : Fin 9 → 𝔽₂) := by
  change diagonalCL.eval 0 ≠ diagonalCL.eval 1
  rw [diagonalCL_eval, diagonalCL_eval]
  intro h
  have h0 := congrFun h (0 : Fin 9)
  exact (by decide : (0 : 𝔽₂) ≠ 1) h0

/-- The admitted all-typed acceptance theorem supplies the source verifier's
length side condition, with no additional parser or trust assumption. -/
def verifier9 : Verifier 9 where
  sampler := sampler9
  decider := WP08.identityDecider
  accepts_length := by
    intro n x y a b h
    have ht := (WP12.accepts_iff_typed_spec n x y a b).mp h
    exact ⟨ht.2.1, ht.2.2.1⟩


/-! ### Source-native polynomial time from the exact read-only syntax tree -/
/-- Bounded-depth inspect/return syntax. Unlike generic `Prog`, this tree
cannot allocate unbounded intermediate structures or iterate. -/
def ReadTree : Prog → Prop
  | .var _ | .nil | .const _ => True
  | .elim _ l r => ReadTree l ∧ ReadTree r
  | _ => False

/-- Maximum path cost, with one possible raw-subtree copy at a leaf. -/
def staticSteps : Prog → Nat
  | .var _ | .nil => 1
  | .const d => d.size
  | .elim _ l r => 1 + max (staticSteps l) (staticSteps r)
  | _ => 0

theorem samplerProg_readTree : ReadTree samplerProg := by
  simp [samplerProg, readStageAt, selectStageOne, copyLinearArgument,
    copyMarginalArgument, ReadTree]

/-- Every environment value remains bounded through a source `elim` step. -/
theorem env_get_size_le (B : Nat) (hB : 1 ≤ B) :
    ∀ (env : Env), (∀ d, d ∈ env → d.size ≤ B) → ∀ i, (env.get i).size ≤ B := by
  intro env
  induction env with
  | nil =>
      intro _ i
      simpa [Env.get] using hB
  | cons a env ih =>
      intro h i
      cases i with
      | zero => exact h a (by simp)
      | succ i =>
          have he : ∀ d, d ∈ env → d.size ≤ B := by
            intro d hd
            exact h d (by simp [hd])
          simpa using ih he i

/-- Actual upstream evaluation, not a simulated time surrogate: each leaf
copies at most one environment value; the syntactic inspection depth is fixed. -/
theorem readTree_eval_bound (B : Nat) (hB : 1 ≤ B) :
    ∀ {env : Env} {p : Prog} {r : Data} {t : Nat},
      Eval env p r t → ReadTree p →
      (∀ d, d ∈ env → d.size ≤ B) →
      t ≤ staticSteps p * (B + 1) := by
  intro env p r t he
  induction he with
  | var env i =>
      intro hp henv
      have hx := env_get_size_le B hB env henv i
      simp only [staticSteps, one_mul]
      omega
  | nil env =>
      intro hp henv
      simp [staticSteps]
  | const env d =>
      intro hp henv
      simp only [staticSteps]
      have h1 : 1 ≤ B + 1 := by omega
      exact Nat.le_mul_of_pos_right d.size h1
  | cons he1 he2 ih1 ih2 =>
      intro hp henv
      cases hp
  | elim_nil hget he ih =>
      rename_i env0 ii pn pc rr tt
      intro hp henv
      have ht := ih hp.1 henv
      simp only [staticSteps]
      have hmul := Nat.mul_le_mul_right (B + 1)
        (Nat.le_max_left (staticSteps pn) (staticSteps pc))
      simp only [Nat.add_mul, one_mul]
      omega
  | elim_cons hget he ih =>
      rename_i e ii pn pc a b rr tt
      intro hp henv
      have hwhole : (Data.cons a b).size ≤ B := by
        rw [← hget]
        exact env_get_size_le B hB e henv _
      have henv' : ∀ d, d ∈ (a :: b :: e) → d.size ≤ B := by
        intro d hd
        simp only [List.mem_cons] at hd
        rcases hd with rfl | rfl | hmem
        · simp only [Data.size_cons] at hwhole
          omega
        · simp only [Data.size_cons] at hwhole
          omega
        · exact henv d hmem
      have ht := ih hp.2 henv'
      simp only [staticSteps]
      have hmul := Nat.mul_le_mul_right (B + 1)
        (Nat.le_max_right (staticSteps pn) (staticSteps pc))
      simp only [Nat.add_mul, one_mul]
      omega
  | let_ he1 he2 ih1 ih2 =>
      intro hp henv
      cases hp
  | loop_nil he ih =>
      intro hp henv
      cases hp
  | loop_stop he ih =>
      intro hp henv
      cases hp
  | loop_step he1 he2 ih1 ih2 =>
      intro hp henv
      cases hp


/-- Full source-native time bound for every raw tail, not merely canonical
query inputs. The coefficient depends only on the canonical index's bit size. -/
theorem sampler9_timeBoundAt (n : Nat) :
    sampler9.TimeBoundAt n (staticSteps samplerProg * (esize n + 2)) 1 := by
  intro d
  obtain ⟨r,t,hr⟩ := samplerProg_halts_raw (.cons (encode n) d)
  have hinput : 1 ≤ (Data.cons (encode n) d).size := Data.size_pos _
  have hc := readTree_eval_bound _ hinput hr samplerProg_readTree
    (by
      intro x hx
      simp only [List.mem_singleton] at hx
      subst x
      rfl)
  have hsize : (Data.cons (encode n) d).size + 1 ≤
      (esize n + 2) * (d.size + 1) := by
    simp only [Data.size_cons, esize]
    nlinarith [Nat.zero_le ((encode n).size * d.size)]
  have hmul := Nat.mul_le_mul_left (staticSteps samplerProg) hsize
  refine ⟨r,t,?_,hr⟩
  simp only [pow_one]
  calc
    t ≤ staticSteps samplerProg * ((Data.cons (encode n) d).size + 1) := hc
    _ ≤ staticSteps samplerProg * ((esize n + 2) * (d.size + 1)) := hmul
    _ = (staticSteps samplerProg * (esize n + 2)) * (d.size + 1) := by ring

/-- The original bounded decider inherits WP11's fixed 89-cost theorem. -/
theorem decider9_timeBoundAt (n : Nat) :
    WP08.identityDecider.TimeBoundAt n 89 0 := by
  intro d
  obtain ⟨r,t,ht,hrun⟩ := WP11.identityDecider_uniform_fuel (.cons (encode n) d)
  have heval := WP09.runFuel_sound _ _ _ _ _ hrun
  have hcost : t ≤ 89 := by
    simpa only [show WP11.staticCost WP08.identityDeciderProg = 89 from by decide] using ht
  exact ⟨r,t,by simpa using hcost,heval⟩

#guard staticSteps samplerProg == 47
#guard sampler9.size == 723
#guard WP08.identityDecider.size == 145459


/-- Explicit polynomial-time condition at every valid index. The output-size
clause is not inferred from a spurious input-independent time bound. -/
def boundLam : Nat := verifier9.size + 10

theorem size_le_index (n : Nat) : Nat.size n ≤ n :=
  Nat.size_le.mpr (Nat.lt_two_pow_self (n := n))

theorem sampler_coefficient_le_pow (n : Nat) (hn : 2 ≤ n) :
    staticSteps samplerProg * (esize n + 2) ≤ n ^ 10 := by
  have hbit : esize n ≤ 4 * n + 1 := by
    have hs := esize_nat_le n
    have hnsize := size_le_index n
    omega
  have hpow9 : 512 ≤ n ^ 9 := by
    simpa only [show (2:Nat)^9 = 512 from by decide] using
      (Nat.pow_le_pow_left hn 9)
  have hcoef : staticSteps samplerProg = 47 := by decide
  rw [hcoef]
  calc
    47 * (esize n + 2) ≤ 47 * (4 * n + 3) := by omega
    _ ≤ 512 * n := by omega
    _ ≤ n ^ 9 * n := Nat.mul_le_mul_right n hpow9
    _ = n ^ 10 := by ring

/-- The actual nine-level verifier meets the source's exact quantitative
`IsBounded` interface at a single explicit (large) finite lambda. -/
theorem verifier9_isBounded : verifier9.IsBounded boundLam := by
  have hLam : 10 ≤ boundLam := by
    dsimp [boundLam]
    omega
  constructor
  · intro n hn
    have hpow : n ^ 10 ≤ n ^ boundLam :=
      Nat.pow_le_pow_right (by omega : 1 ≤ n) hLam
    have hpow9 : 512 ≤ n ^ 9 := by
      simpa only [show (2:Nat)^9 = 512 from by decide] using
        (Nat.pow_le_pow_left hn 9)
    have h512 : 512 ≤ n ^ boundLam := by
      have h10 : 512 ≤ n ^ 10 := by
        calc
          512 ≤ 512 * n := by omega
          _ ≤ n ^ 9 * n := Nat.mul_le_mul_right n hpow9
          _ = n ^ 10 := by ring
      omega
    refine ⟨?_, ?_, ?_⟩
    · change 9 ≤ n ^ boundLam
      omega
    · change sampler9.TimeBoundAt n (n ^ boundLam) boundLam
      apply Sampler.TimeBoundAt.mono (sampler9_timeBoundAt n)
      · exact (sampler_coefficient_le_pow n hn).trans hpow
      · omega
    · change WP08.identityDecider.TimeBoundAt n (n ^ boundLam) boundLam
      apply Decider.TimeBoundAt.mono (decider9_timeBoundAt n)
      · omega
      · omega
  · dsimp only [boundLam]
    omega


/-- Both players receive the *same* full uniform seed through the source
CL interface. This proves a genuine nine-bit question distribution, but it
is not a hardness construction. -/
theorem sampler9_seed_exact (n : Nat) (w : Player) (x : Fin 9 → 𝔽₂) :
    (sampler9.cl n w).eval x = x := diagonalCL_eval x

/-- The admitted typed parser rules make this a synchronous verifier. -/
theorem verifier9_synchronous (n : Nat) : verifier9.IsSynchronousAt n := by
  intro x a b hab hacc
  have ht := (WP12.accepts_iff_typed_spec n x x a b).mp hacc
  exact hab (ht.2.2.2.1.trans ht.2.2.2.2.symm)

/-- Explicit limitation: all legitimate nine-bit question pairs accept
empty answers at every positive index. It is a valid reference verifier,
not evidence of a computationally hard game. -/
theorem verifier9_accepts_empty (n : Nat) (hn : n ≠ 0)
    (x y : Fin 9 → 𝔽₂) :
    verifier9.decider.Accepts n (toBits x) (toBits y) [] [] := by
  exact (WP12.accepts_iff_typed_spec n (toBits x) (toBits y) [] []).mpr
    ⟨hn, length_toBits x, length_toBits y, rfl, rfl⟩

end PNPAbove.WP13

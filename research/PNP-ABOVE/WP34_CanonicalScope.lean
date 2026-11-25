import PNPAbove.WP33Budget
import MIPRE.Foundations.Cost.BinaryCompare

namespace PNPAbove.WP34
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun
open Polynomial

/-- The least initial segment containing every input variable. No variables
are allocated, and its natural-number representation is binary. -/
def scope : Fml → Nat
  | .inp i => i+1
  | .const _ => 0
  | .and f g => max (scope f) (scope g)
  | .or f g => max (scope f) (scope g)
  | .not f => scope f

theorem scope_le_iff (f : Fml) (m : Nat) : scope f ≤ m ↔ f.InputsLt m := by
  induction f with
  | inp i => simp [scope, Fml.InputsLt]
  | const b => simp [scope, Fml.InputsLt]
  | and f g ihf ihg => simp [scope, Fml.InputsLt, ihf, ihg]
  | or f g ihf ihg => simp [scope, Fml.InputsLt, ihf, ihg]
  | not f ih => simpa [scope, Fml.InputsLt] using ih

def step (s : Nat) (nd : Fml.Node) : Nat :=
  match nd with
  | .inp i => max s (i+1)
  | _ => s

noncomputable def inputStepProgram : PolyTimeFun (Nat × Nat) Nat :=
  PolyTimeFun.ite
    (PolyTimeFun.leNat.comp (fst.pair (PolyTimeFun.inc.comp snd)))
    (PolyTimeFun.inc.comp snd) fst

theorem inputStep_correct (s i : Nat) : inputStepProgram (s,i) = max s (i+1) := by
  change (if decide (s ≤ i+1) then i+1 else s) = max s (i+1)
  simp only [decide_eq_true_eq]
  split_ifs with h
  · exact (Nat.max_eq_right h).symm
  · exact (Nat.max_eq_left (by omega)).symm

noncomputable def stepProgram : PolyTimeFun (Nat × Fml.Node) Nat :=
  MIPRE.SAT.PolyTimeFun.casesNode inputStepProgram fst
    (PolyTimeFun.id Nat) (PolyTimeFun.id Nat) (PolyTimeFun.id Nat)

theorem stepProgram_correct (s : Nat) (nd : Fml.Node) :
    stepProgram (s,nd) = step s nd := by
  cases nd with
  | inp i => exact inputStep_correct s i
  | const b => rfl
  | and => rfl
  | or => rfl
  | not => rfl

theorem step_encoding_bound (s : Nat) (nd : Fml.Node) :
    esize (stepProgram (s, nd)) ≤ esize s + (X + C 4 : Polynomial Nat).eval (esize nd) := by
  rw [stepProgram_correct]
  cases nd with
  | inp i =>
    simp only [step, Polynomial.eval_add, Polynomial.eval_X, Polynomial.eval_C, esize_node_inp]
    by_cases h : s ≤ i+1
    · rw [Nat.max_eq_right h]
      have hh := esize_succ_le i
      omega
    · rw [Nat.max_eq_left (by omega)]
      omega
  | const b => simp [step]
  | and => simp [step]
  | or => simp [step]
  | not => simp [step]

theorem rpn_scope (f : Fml) (s : Nat) :
    f.rpn.foldl step s = max s (scope f) := by
  induction f generalizing s with
  | inp i => rfl
  | const b => simp [Fml.rpn, step, scope]
  | and f g ihf ihg =>
    simp [Fml.rpn, List.foldl_append, ihf, ihg, step, scope, max_assoc]
  | or f g ihf ihg =>
    simp [Fml.rpn, List.foldl_append, ihf, ihg, step, scope, max_assoc]
  | not f ih =>
    simp [Fml.rpn, List.foldl_append, ih, step, scope]

/-- Actual fixed, polynomial-time original Cost.Prog for canonical scope. -/
noncomputable def scopeProgram : PolyTimeFun Fml Nat :=
  (PolyTimeFun.foldlAdd stepProgram (X + C 4) step_encoding_bound).comp
    (Fml.rpnF.pair (PolyTimeFun.const (0 : Nat)))

theorem scopeProgram_correct (f : Fml) : scopeProgram f = scope f := by
  simp only [scopeProgram, comp_apply, pair_apply, Fml.rpnF_apply,
    const_apply, foldlAdd_apply, stepProgram_correct]
  rw [rpn_scope, Nat.zero_max]

theorem scopeProgram_polytime (f : Fml) :
    ∃ t ≤ scopeProgram.timeBound.eval (esize f),
      scopeProgram.code.Runs (encode f) (encode (scope f)) t := by
  simpa only [scopeProgram_correct] using scopeProgram.computes f

theorem scope_le_source_power (f : Fml) : scope f ≤ 2 ^ esize f := by
  induction f with
  | inp i =>
    have hh : i < 2 ^ esize i := Nat.size_le.mp (size_le_esize_nat i)
    have hs : esize i ≤ esize (Fml.inp i) := by
      change esize i ≤ esize ([Fml.Node.inp i] : List Fml.Node)
      rw [esize_list_cons, esize_node_inp]
      omega
    exact (Nat.succ_le_of_lt hh).trans (Nat.pow_le_pow_right (by decide) hs)
  | const b => simp [scope]
  | and f g ihf ihg =>
    rw [scope, Nat.max_le, esize_and_fml]
    exact ⟨ihf.trans (Nat.pow_le_pow_right (by decide) (by omega)),
      ihg.trans (Nat.pow_le_pow_right (by decide) (by omega))⟩
  | or f g ihf ihg =>
    rw [scope, Nat.max_le, esize_or_fml]
    exact ⟨ihf.trans (Nat.pow_le_pow_right (by decide) (by omega)),
      ihg.trans (Nat.pow_le_pow_right (by decide) (by omega))⟩
  | not f ih =>
    rw [scope, esize_not_fml]
    exact ih.trans (Nat.pow_le_pow_right (by decide) (by omega))

theorem scope_le_index (f : Fml) : scope f ≤ WP28B.formulaIndex f :=
  (scope_le_source_power f).trans (WP28B2.formulaIndex_numeric_exponential_lower f)

theorem satisfiable_iff_global (f : Fml) (m : Nat) (hscope : f.InputsLt m) :
    WP24.Satisfiable m f ↔ ∃ w : Nat → Bool, f.eval w = true := by
  constructor
  · rintro ⟨w, hw⟩
    exact ⟨WP24.bitsAt w, hw⟩
  · rintro ⟨w, hw⟩
    refine ⟨fun i => w i.val, ?_⟩
    rw [← Fml.eval_congr_of_inputsLt hscope w (WP24.bitsAt (fun i : Fin m => w i.val))]
    · exact hw
    · intro i hi
      simp [WP24.bitsAt, hi]

theorem scope_sat_iff (f : Fml) (m : Nat) (hscope : f.InputsLt m) :
    WP24.Satisfiable (scope f) f ↔ WP24.Satisfiable m f := by
  rw [satisfiable_iff_global f _ ((scope_le_iff f _).mp le_rfl),
    satisfiable_iff_global f m hscope]

/-- Normalizer computes padded formula and its exact minimal initial scope. -/
noncomputable def paddedFormulaProgram (r : Nat) : PolyTimeFun WP29.Enc3CNF Fml :=
  (WP32.padTrueProgram r).comp WP29.formulaProgram

noncomputable def normalizeProgram (r : Nat) : PolyTimeFun WP29.Enc3CNF (Fml × Nat) :=
  (PolyTimeFun.id Fml).pair scopeProgram |>.comp (paddedFormulaProgram r)

theorem normalizeProgram_correct (r : Nat) (cs : WP29.Enc3CNF) :
    normalizeProgram r cs =
      (WP32.padTrue r (WP29.formula cs), scope (WP32.padTrue r (WP29.formula cs))) := by
  simp [normalizeProgram, paddedFormulaProgram, WP32.padTrueProgram_correct,
    WP29.formulaProgram_correct, scopeProgram_correct]

theorem normalizeProgram_polytime (r : Nat) (cs : WP29.Enc3CNF) :
    ∃ t ≤ (normalizeProgram r).timeBound.eval (esize cs),
      (normalizeProgram r).code.Runs (encode cs) (encode (normalizeProgram r cs)) t :=
  (normalizeProgram r).computes cs

theorem canonical_budget (G : GapCompression) (U : Cost.UniversalMachine)
    (f : Fml) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam) :
    scope f ≤ (2 ^ WP28B.formulaIndex f) ^ lam := by
  have hpos : 0 < lam := by have := hB.two_le; omega
  exact (scope_le_index f).trans ((Nat.le_of_lt Nat.lt_two_pow_self).trans (Nat.le_pow hpos))


/-- The actual source compressor has its full native promise for every
formula above the fixed threshold, with no external variable budget. -/
theorem canonical_compressed_yes
    (G : GapCompression) (U : Cost.UniversalMachine) (f : Fml) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hk : G.C₀ ≤ WP28B.formulaIndex f)
    (hsat : ∃ w : Nat → Bool, f.eval w = true) :
    (WP30.fixedCompressed G U lam).HasPerfectPCC
      (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) := by
  exact WP28C.powerCompressedPCC_of_sat G U f (scope f) lam hB hk
    (canonical_budget G U f lam hB)
    ((satisfiable_iff_global f _ ((scope_le_iff f _).mp le_rfl)).mpr hsat)

theorem canonical_compressed_no
    (G : GapCompression) (U : Cost.UniversalMachine) (f : Fml) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hk : G.C₀ ≤ WP28B.formulaIndex f)
    (hunsat : ¬ ∃ w : Nat → Bool, f.eval w = true) :
    (WP30.fixedCompressed G U lam).valStar
      (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) ≤ (1/2 : Real) := by
  exact WP28C.powerCompressedSoundness_of_unsat G U f (scope f) lam hB hk
    ((scope_le_iff f _).mp le_rfl)
    (fun h => hunsat ((satisfiable_iff_global f _ ((scope_le_iff f _).mp le_rfl)).mp h))

/-- SAT is exactly perfect PCC for valid indices above threshold, not
merely implied by PCC; the opposite case has a genuine quantum gap. -/
theorem canonical_pcc_iff_sat
    (G : GapCompression) (U : Cost.UniversalMachine) (f : Fml) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hk : G.C₀ ≤ WP28B.formulaIndex f) :
    (WP30.fixedCompressed G U lam).HasPerfectPCC
      (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) ↔
      ∃ w : Nat → Bool, f.eval w = true := by
  constructor
  · intro hp
    by_contra h
    have hs := canonical_compressed_no G U f lam hB hk h
    have hv := (WP30.fixedCompressed G U lam).valStar_eq_one_of_hasPerfectPCC hp
    rw [hv] at hs
    norm_num at hs
  · exact canonical_compressed_yes G U f lam hB hk

theorem canonical_gap_iff_unsat
    (G : GapCompression) (U : Cost.UniversalMachine) (f : Fml) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hk : G.C₀ ≤ WP28B.formulaIndex f) :
    (WP30.fixedCompressed G U lam).valStar
      (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) ≤ (1/2 : Real) ↔
      ¬ ∃ w : Nat → Bool, f.eval w = true := by
  constructor
  · intro hg hs
    have hp := canonical_compressed_yes G U f lam hB hk hs
    have hv := (WP30.fixedCompressed G U lam).valStar_eq_one_of_hasPerfectPCC hp
    rw [hv] at hg
    norm_num at hg
  · exact canonical_compressed_no G U f lam hB hk

/-- The WP32 classical transfer now needs no ambient variable budget.
The same original polynomial source program handles every finite 3CNF. -/
theorem budget_free_classical_transfer
    (G : GapCompression) (U : Cost.UniversalMachine)
    (oracle : PolyTimeFun Nat Bool) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hyes : ∀ k, (WP30.fixedCompressed G U lam).HasPerfectPCC k
      (G.bound.eval (k + lam)) → oracle k = true)
    (hno : ∀ k, (WP30.fixedCompressed G U lam).valStar k
      (G.bound.eval (k + lam)) ≤ (1/2 : Real) → oracle k = false)
    {m : Nat} (cs : List (SAT.Clause3 (Fin m))) :
    WP32.normalizedClassicalProgram G.C₀ oracle (WP29.fromOriginal3CNF cs) = true ↔
      ∃ w : Fin m → Bool, (WP24.threeCNFSet cs).Sat w := by
  let f := WP32.padTrue G.C₀ (WP29.formula (WP29.fromOriginal3CNF cs))
  let k := WP28B.formulaIndex f
  have hk : G.C₀ ≤ k := by
    simpa only [WP32.normalizedIndex_correct] using
      WP32.normalizedIndex_threshold G.C₀ (WP29.fromOriginal3CNF cs)
  have hscope : f.InputsLt m :=
    (WP32.padTrue_inputs G.C₀ m _).mpr (WP29.original3CNF_scoped cs)
  have hequiv : (∃ w : Nat → Bool, f.eval w = true) ↔
      ∃ w : Fin m → Bool, (WP24.threeCNFSet cs).Sat w := by
    rw [← satisfiable_iff_global f m hscope, WP32.padTrue_sat]
    exact exists_congr (fun w => (WP29.originalFinite3CNF_sat_iff cs w).symm)
  have horacle : oracle k = true ↔ ∃ w : Nat → Bool, f.eval w = true := by
    constructor
    · intro ht
      by_contra hu
      have hf := hno k (canonical_compressed_no G U f lam hB hk hu)
      rw [hf] at ht
      contradiction
    · intro hs
      exact hyes k (canonical_compressed_yes G U f lam hB hk hs)
  change oracle (WP32.normalizedIndexProgram G.C₀ (WP29.fromOriginal3CNF cs)) = true ↔ _
  rw [WP32.normalizedIndex_correct]
  exact horacle.trans hequiv

/-- An original polynomial-time solver on encoded formula data gives a
polynomial-time solver for the restricted, valid-index compressed promise.
This uses the exact source decoder, not expanded game enumeration. -/
noncomputable def decodedSolver (satSolver : PolyTimeFun Data Bool) : PolyTimeFun Nat Bool :=
  satSolver.comp WP28B.decodeDataProgram

theorem decodedSolver_correct
    (G : GapCompression) (U : Cost.UniversalMachine)
    (satSolver : PolyTimeFun Data Bool)
    (hsatSolver : ∀ f : Fml, satSolver (encode f) = true ↔ ∃ w : Nat → Bool, f.eval w = true)
    (f : Fml) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hk : G.C₀ ≤ WP28B.formulaIndex f) :
    (decodedSolver satSolver (WP28B.formulaIndex f) = true ↔
      (WP30.fixedCompressed G U lam).HasPerfectPCC
        (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam))) ∧
    (decodedSolver satSolver (WP28B.formulaIndex f) = false ↔
      (WP30.fixedCompressed G U lam).valStar
        (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) ≤ (1/2 : Real)) := by
  have hd : WP28B.decodeDataProgram (WP28B.formulaIndex f) = encode f := by
    simpa only [WP28B.formulaIndexProgram_correct] using WP28B.formulaIndex_decode f
  have ht : decodedSolver satSolver (WP28B.formulaIndex f) = true ↔
      ∃ w : Nat → Bool, f.eval w = true := by
    change satSolver (WP28B.decodeDataProgram (WP28B.formulaIndex f)) = true ↔ _
    rw [hd]
    exact hsatSolver f
  refine ⟨ht.trans (canonical_pcc_iff_sat G U f lam hB hk).symm, ?_⟩
  rw [canonical_gap_iff_unsat G U f lam hB hk, ← ht]
  cases decodedSolver satSolver (WP28B.formulaIndex f) <;> simp


/-- Only the genuine valid formula-index promise, not arbitrary integer indices. -/
def SolvesValidPromise (G : GapCompression) (U : Cost.UniversalMachine)
    (lam : Nat) (oracle : PolyTimeFun Nat Bool) : Prop :=
  ∀ f : Fml, G.C₀ ≤ WP28B.formulaIndex f →
    ((WP30.fixedCompressed G U lam).HasPerfectPCC
        (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) →
          oracle (WP28B.formulaIndex f) = true) ∧
    ((WP30.fixedCompressed G U lam).valStar
        (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) ≤ (1/2 : Real) →
          oracle (WP28B.formulaIndex f) = false)

def SolvesFormulaDataSAT (satSolver : PolyTimeFun Data Bool) : Prop :=
  ∀ f : Fml, satSolver (encode f) = true ↔ ∃ w : Nat → Bool, f.eval w = true

/-- Finite lookup is a fixed source program; table size may depend on the
fixed threshold, never the input. Binary comparisons avoid unary search. -/
noncomputable def finiteTable (labels : Nat → Bool) : (r : Nat) → PolyTimeFun Nat Bool
  | 0 => PolyTimeFun.const false
  | r+1 =>
    PolyTimeFun.ite
      (PolyTimeFun.leNat.comp ((PolyTimeFun.id Nat).pair (PolyTimeFun.const r)))
      (PolyTimeFun.ite
        (PolyTimeFun.leNat.comp ((PolyTimeFun.const r).pair (PolyTimeFun.id Nat)))
        (PolyTimeFun.const (labels r))
        (finiteTable labels r))
      (PolyTimeFun.const false)

theorem finiteTable_correct (labels : Nat → Bool) (r n : Nat) (h : n < r) :
    finiteTable labels r n = labels n := by
  induction r with
  | zero => omega
  | succ r ih =>
    have hle : n ≤ r := by omega
    change (if decide (n ≤ r) then
      (if decide (r ≤ n) then labels r else finiteTable labels r n) else false) = labels n
    simp only [decide_eq_true_eq, ite_eq_left hle]
    split_ifs with hge
    · have heq : r = n := by omega
      rw [heq]
    · exact ih (by omega)

/-- Mathematical labels for the finitely many fixed exceptional indices.
No algorithm for general SAT is postulated or implemented here. -/
noncomputable def indexSATLabel (k : Nat) : Bool := by
  classical
  exact if ∃ f : Fml, WP28B.formulaIndex f = k ∧
    ∃ w : Nat → Bool, f.eval w = true then true else false

theorem indexSATLabel_correct (f : Fml) :
    indexSATLabel (WP28B.formulaIndex f) = true ↔
      ∃ w : Nat → Bool, f.eval w = true := by
  classical
  unfold indexSATLabel
  simp only [ite_eq_left_iff, Bool.false_eq_true, imp_false, not_not]
  constructor
  · rintro ⟨g, hg, hs⟩
    have heq := WP28B.formulaIndex_injective hg
    simpa only [heq] using hs
  · intro hs
    exact ⟨f, rfl, hs⟩

/-- Extend a restricted promise solver across the finitely many indices below
the fixed threshold. Only those finitely many SAT labels enter its code. -/
noncomputable def thresholdExtendedSolver (r : Nat)
    (oracle : PolyTimeFun Nat Bool) : PolyTimeFun Nat Bool :=
  PolyTimeFun.ite
    (PolyTimeFun.leNat.comp ((PolyTimeFun.const r).pair (PolyTimeFun.id Nat)))
    oracle (finiteTable indexSATLabel r)

theorem thresholdExtendedSolver_correct
    (G : GapCompression) (U : Cost.UniversalMachine) (lam : Nat)
    (oracle : PolyTimeFun Nat Bool)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (ho : SolvesValidPromise G U lam oracle) (f : Fml) :
    thresholdExtendedSolver G.C₀ oracle (WP28B.formulaIndex f) = true ↔
      ∃ w : Nat → Bool, f.eval w = true := by
  let k := WP28B.formulaIndex f
  change (if decide (G.C₀ ≤ k) then oracle k else finiteTable indexSATLabel G.C₀ k) =
    true ↔ _
  simp only [decide_eq_true_eq]
  split_ifs with hk
  · constructor
    · intro ht
      by_contra hu
      have hf := (ho f hk).2 (canonical_compressed_no G U f lam hB hk hu)
      change oracle k = false at hf
      rw [hf] at ht
      contradiction
    · intro hs
      exact (ho f hk).1 (canonical_compressed_yes G U f lam hB hk hs)
  · rw [finiteTable_correct indexSATLabel _ _ (by omega)]
    exact indexSATLabel_correct f

/-- Exact source-polynomial reduction equivalence, restricted to genuine
formula indices. It does not assert an efficient solver exists. -/
theorem valid_promise_polytime_iff_formula_SAT
    (G : GapCompression) (U : Cost.UniversalMachine) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam) :
    (∃ oracle : PolyTimeFun Nat Bool, SolvesValidPromise G U lam oracle) ↔
      ∃ satSolver : PolyTimeFun Data Bool, SolvesFormulaDataSAT satSolver := by
  constructor
  · rintro ⟨oracle, ho⟩
    refine ⟨(thresholdExtendedSolver G.C₀ oracle).comp WP28B.indexDataProgram, ?_⟩
    intro f
    change thresholdExtendedSolver G.C₀ oracle
      (WP28B.indexDataProgram (encode f)) = true ↔ _
    rw [WP28B.indexDataProgram_correct]
    exact thresholdExtendedSolver_correct G U lam oracle hB ho f
  · rintro ⟨satSolver, hs⟩
    refine ⟨decodedSolver satSolver, ?_⟩
    intro f hk
    have hh := decodedSolver_correct G U satSolver hs f lam hB hk
    exact ⟨hh.1.mpr, hh.2.mpr⟩


/-- Padding does not introduce any active variables. -/
theorem scope_padTrue (r : Nat) (f : Fml) : scope (WP32.padTrue r f) = scope f := by
  induction r with
  | zero => rfl
  | succ r ih => simp [WP32.padTrue, scope, ih]

/-- The computed normalization pair is a scoped SAT-equivalent instance
for every original finite 3CNF, including arbitrary unused Fin variables. -/
theorem normalized_pair_sat (r : Nat) {m : Nat} (cs : List (SAT.Clause3 (Fin m))) :
    let p := normalizeProgram r (WP29.fromOriginal3CNF cs)
    p.1.InputsLt p.2 ∧
      (WP24.Satisfiable p.2 p.1 ↔
        ∃ w : Fin m → Bool, (WP24.threeCNFSet cs).Sat w) := by
  dsimp only
  rw [normalizeProgram_correct]
  let f := WP32.padTrue r (WP29.formula (WP29.fromOriginal3CNF cs))
  change f.InputsLt (scope f) ∧ (WP24.Satisfiable (scope f) f ↔ _)
  have hscope : f.InputsLt m :=
    (WP32.padTrue_inputs r m _).mpr (WP29.original3CNF_scoped cs)
  refine ⟨(scope_le_iff f _).mp le_rfl, ?_⟩
  rw [scope_sat_iff f m hscope, WP32.padTrue_sat]
  exact exists_congr (fun w => (WP29.originalFinite3CNF_sat_iff cs w).symm)

/-- The computed scope fits the exact native answer budget, without
expanding either the scope or the index to a unary representation. -/
theorem normalized_pair_budget (G : GapCompression) (U : Cost.UniversalMachine)
    (lam : Nat) (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (cs : WP29.Enc3CNF) :
    (normalizeProgram G.C₀ cs).2 ≤
      (2 ^ WP32.normalizedIndexProgram G.C₀ cs) ^ lam := by
  rw [normalizeProgram_correct, WP32.normalizedIndex_correct]
  exact canonical_budget G U _ lam hB

/-- Full source-polynomial SAT transfer on original 3CNF using only the
restricted valid-index promise, no global oracle condition. -/
theorem valid_promise_classical_transfer
    (G : GapCompression) (U : Cost.UniversalMachine)
    (oracle : PolyTimeFun Nat Bool) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (ho : SolvesValidPromise G U lam oracle)
    {m : Nat} (cs : List (SAT.Clause3 (Fin m))) :
    WP32.normalizedClassicalProgram G.C₀ oracle (WP29.fromOriginal3CNF cs) = true ↔
      ∃ w : Fin m → Bool, (WP24.threeCNFSet cs).Sat w := by
  let f := WP32.padTrue G.C₀ (WP29.formula (WP29.fromOriginal3CNF cs))
  let k := WP28B.formulaIndex f
  have hk : G.C₀ ≤ k := by
    simpa only [WP32.normalizedIndex_correct] using
      WP32.normalizedIndex_threshold G.C₀ (WP29.fromOriginal3CNF cs)
  have hscope : f.InputsLt m :=
    (WP32.padTrue_inputs G.C₀ m _).mpr (WP29.original3CNF_scoped cs)
  have hequiv : (∃ w : Nat → Bool, f.eval w = true) ↔
      ∃ w : Fin m → Bool, (WP24.threeCNFSet cs).Sat w := by
    rw [← satisfiable_iff_global f m hscope, WP32.padTrue_sat]
    exact exists_congr (fun w => (WP29.originalFinite3CNF_sat_iff cs w).symm)
  have ht : oracle k = true ↔ ∃ w : Nat → Bool, f.eval w = true := by
    constructor
    · intro h
      by_contra hu
      have hf := (ho f hk).2 (canonical_compressed_no G U f lam hB hk hu)
      change oracle k = false at hf
      rw [hf] at h
      contradiction
    · intro hs
      exact (ho f hk).1 (canonical_compressed_yes G U f lam hB hk hs)
  change oracle (WP32.normalizedIndexProgram G.C₀ (WP29.fromOriginal3CNF cs)) = true ↔ _
  rw [WP32.normalizedIndex_correct]
  exact ht.trans hequiv

/-- The two nonexistence assertions are equivalent for these exact
source-polynomial machine types. No independent lower bound is supplied. -/
theorem valid_promise_lower_bound_iff_formula_SAT
    (G : GapCompression) (U : Cost.UniversalMachine) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam) :
    (¬ ∃ oracle : PolyTimeFun Nat Bool, SolvesValidPromise G U lam oracle) ↔
      ¬ ∃ satSolver : PolyTimeFun Data Bool, SolvesFormulaDataSAT satSolver :=
  not_congr (valid_promise_polytime_iff_formula_SAT G U lam hB)

end PNPAbove.WP34

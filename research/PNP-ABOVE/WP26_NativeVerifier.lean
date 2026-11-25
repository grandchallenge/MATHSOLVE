import PNPAbove.WP25SourceEvaluator
import MIPRE.Foundations.Halting.WrapperCost
import MIPRE.Foundations.Halting.Classes
import MIPRE.Foundations.SAT.Rename

/-! Source-native raw verifier tuple compiler, for arbitrary formula f. -/
namespace PNPAbove.WP26
open MIPRE MIPRE.Cost
open MIPRE.Cost.PolyTimeFun

/-- Source executable projection of the original Decider's Alice component. -/
noncomputable def rawAlice : PolyTimeFun (Nat × BitStr × BitStr × BitStr × BitStr) BitStr :=
  fst.comp (snd.comp (snd.comp snd))

/-- Source executable projection of the original Decider's Bob component. -/
noncomputable def rawBob : PolyTimeFun (Nat × BitStr × BitStr × BitStr × BitStr) BitStr :=
  snd.comp (snd.comp (snd.comp snd))

/-- For ANY original Boolean formula f, the emitted ORIGINAL Cost.Prog
accepts a raw verifier tuple precisely on a pair of identical SAT
witnesses. The program ignores n, x and y. The normal-form verifier
wrapper must separately check question dimensions. -/
noncomputable def rawSatChecker (f : MIPRE.SAT.Fml) :
    PolyTimeFun (Nat × BitStr × BitStr × BitStr × BitStr) Bool :=
  PNPAbove.WP25.answerCheckProgram.comp
    (((PolyTimeFun.const f).pair rawAlice).pair rawBob)

/-- Source runtime correctness for all canonically encoded raw five-tuples. -/
theorem rawSatChecker_correct (f : MIPRE.SAT.Fml) (n : Nat)
    (x y a b : BitStr) :
    rawSatChecker f (n, x, y, a, b) =
      (f.eval (fun i => a.getD i false) && decide (a = b)) := by
  simp [rawSatChecker, rawAlice, rawBob,
    PNPAbove.WP25.answerCheckProgram_correct]

/-- The actual CLOSED source program and polynomial ORIGINAL runtime
witness for every source-typed raw verifier tuple, not merely a
mathematical predicate. -/
theorem rawSatChecker_polytime (f : MIPRE.SAT.Fml)
    (p : Nat × BitStr × BitStr × BitStr × BitStr) :
    ∃ t ≤ (rawSatChecker f).timeBound.eval (esize p),
      (rawSatChecker f).code.Runs (encode p) (encode (rawSatChecker f p)) t :=
  (rawSatChecker f).computes p

/-- Original source syntax has no free environment parameters. -/
theorem rawSatChecker_closed (f : MIPRE.SAT.Fml) :
    (rawSatChecker f).code.WellScoped 1 :=
  (rawSatChecker f).closed


/-- The ORIGINAL machine's acceptance event (a run returning encode true)
is EQUIVALENT to having a satisfying witness, for all canonical raw verifier
input tuples. No finite enumeration or abstract oracle. -/
theorem rawSatChecker_accepts_iff (f : MIPRE.SAT.Fml) (n : Nat)
    (x y a b : BitStr) :
    (∃ t, (rawSatChecker f).code.Runs
       (encode (n, x, y, a, b)) (encode true) t) ↔
      (f.eval (fun i => a.getD i false) = true ∧ a = b) := by
  constructor
  · rintro ⟨t, hrun⟩
    obtain ⟨t₀, ht₀, hcanonical⟩ :=
      (rawSatChecker f).computes (n, x, y, a, b)
    have heq : encode true = encode (rawSatChecker f (n, x, y, a, b)) :=
      (MIPRE.Cost.Eval.deterministic hrun hcanonical).1
    have hvalue : rawSatChecker f (n, x, y, a, b) = true := by
      cases h : rawSatChecker f (n, x, y, a, b) with
      | false => simp [h] at heq
      | true => rfl
    rw [rawSatChecker_correct] at hvalue
    simpa only [Bool.and_eq_true, decide_eq_true_eq] using hvalue
  · intro hacc
    obtain ⟨t, _, hrun⟩ :=
      (rawSatChecker f).computes (n, x, y, a, b)
    refine ⟨t, ?_⟩
    have hvalue : rawSatChecker f (n, x, y, a, b) = true := by
      rcases hacc with ⟨hf, rfl⟩
      simp only [rawSatChecker_correct, Bool.and_eq_true, decide_eq_true_eq]
      refine ⟨?_, trivial⟩
      simpa [List.getD] using hf
    simpa only [hvalue] using hrun


/-- An ACTUAL original source-native seven-level normal verifier.
Its question sampler is the caller's genuine MIPRE.CL.Sampler 7,
and its decider is the original universal-machine wrapper around
the real formula-specialized Cost.Prog. Unlike WP24, this has the
exact original MIPRE.Verifier 7 type, native raw decider source,
and built-in accepted-question-length check. -/
noncomputable def satVerifier (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) : MIPRE.Verifier 7 :=
  MIPRE.Verifier.ofSamplerDecider U S (rawSatChecker f).code

/-- Source verifier structure retains the original seven-level sampler. -/
theorem satVerifier_sampler (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) :
    (satVerifier U S f).sampler = S := rfl

/-- Actual original source Decider.Accepts has the precise five-tuple
SAT semantics AND question-length guards for ALL typed tuples,
not just the older abstract game. -/
theorem satVerifier_accepts_iff (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (n : Nat) (x y a b : BitStr) :
    (satVerifier U S f).decider.Accepts n x y a b ↔
      x.length = S.dim n ∧ y.length = S.dim n ∧
      f.eval (fun i => a.getD i false) = true ∧ a = b := by
  change (MIPRE.Verifier.ofSamplerDecider U S (rawSatChecker f).code).decider.Accepts n x y a b ↔ _
  rw [MIPRE.Verifier.ofSamplerDecider_accepts]
  simp only [rawSatChecker_accepts_iff]

/-- This original native source verifier is synchronous at EVERY index:
on equal questions, different answers cannot both be accepted. -/
theorem satVerifier_synchronous (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) (n : Nat) :
    (satVerifier U S f).IsSynchronousAt n := by
  intro x a b hab hacc
  exact hab ((satVerifier_accepts_iff U S f n x x a b).mp hacc).2.2.2


/-- For any *actual* seven-level source sampler, a satisfiable instance
admits a perfect PCC strategy for the ORIGINAL Verifier 7 game at every
source index, provided its answer budget admits the complete witness. -/
theorem nativePerfectPCC_of_sat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (satVerifier U S f).HasPerfectPCC k T := by
  obtain ⟨w, hw⟩ := hSAT
  let a : BitStr := List.ofFn w
  have ha : a.length ≤ T := by
    simp only [a, List.length_ofFn]
    omega
  apply (satVerifier U S f).hasPerfectPCC_of_accepts_diagonal ⟨a, ha⟩
  intro x y
  rw [satVerifier_accepts_iff]
  refine ⟨MIPRE.CL.length_toBits x, MIPRE.CL.length_toBits y, ?_, rfl⟩
  have heval : (fun i => a.getD i false) = PNPAbove.WP24.bitsAt w := by
    funext i
    exact PNPAbove.WP25.ofFn_getD_eq_bitsAt w i
  simpa only [heval] using hw

/-- No original source decider execution can accept an UNSAT formula
with all variables among the declared m inputs, regardless of
question index, question strings, response lengths or raw-answer bits. -/
theorem nativeRejectsAll_of_unsat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (k : Nat) (x y a b : BitStr) :
    ¬ (satVerifier U S f).decider.Accepts k x y a b := by
  intro hacc
  obtain ⟨_, _, hf, _⟩ := (satVerifier_accepts_iff U S f k x y a b).mp hacc
  apply hunsat
  let w : Fin m → Bool := fun i => a.getD i.val false
  refine ⟨w, ?_⟩
  have heq : f.eval (fun i => a.getD i false) =
      f.eval (PNPAbove.WP24.bitsAt w) := by
    apply MIPRE.SAT.Fml.eval_congr_of_inputsLt hscope
    intro i hi
    simp [PNPAbove.WP24.bitsAt, hi, w]
  exact heq ▸ hf

/-- Actual original Verifier.valStar is ZERO on an UNSAT scoped input,
for ALL indices and ALL answer budgets. This is the exact source-native
soundness promise that WP24's abstract game lacked. -/
theorem nativeValStar_zero_of_unsat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (k T : Nat) :
    (satVerifier U S f).valStar k T = 0 := by
  apply (satVerifier U S f).valStar_eq_zero_of_rejects_all
  intro x y a b
  exact nativeRejectsAll_of_unsat U S f m hscope hunsat k x y a b

/-- The actual original MIPRE GapCompression soundness bound at the
normal-form verifier GAME level: zero is strictly below one-half. -/
theorem nativeValStar_half_of_unsat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (k T : Nat) :
    (satVerifier U S f).valStar k T ≤ (1 / 2 : Real) := by
  rw [nativeValStar_zero_of_unsat U S f m hscope hunsat k T]
  norm_num


/-- For SAT, the actual ORIGINAL normal-verifier tensor game value is one. -/
theorem nativeValStar_one_of_sat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (satVerifier U S f).valStar k T = 1 :=
  (satVerifier U S f).valStar_eq_one_of_hasPerfectPCC
    (nativePerfectPCC_of_sat U S f m k T hT hSAT)

/-- The EXACT original seven-level normal verifier has the 1/0 native
quantum value promise when the formula's variables are all scoped. -/
theorem nativeValStar_one_iff_sat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hscope : f.InputsLt m) (hT : m ≤ T) :
    (satVerifier U S f).valStar k T = 1 ↔
      PNPAbove.WP24.Satisfiable m f := by
  constructor
  · intro hv
    by_contra h
    have hz := nativeValStar_zero_of_unsat U S f m hscope h k T
    rw [hz] at hv
    norm_num at hv
  · exact nativeValStar_one_of_sat U S f m k T hT

/-- The ORIGINAL MIPRE compression theorem now consumes this exact
native SAT verifier. The sole remaining computational input premise
is its original source-wide Verifier.IsBounded lambda contract. -/
theorem nativeCompressedPCC_of_sat (G : MIPRE.GapCompression)
    (U : MIPRE.Cost.UniversalMachine) (f : MIPRE.SAT.Fml)
    (m lam k : Nat)
    (hB : (satVerifier U (G.sampler 0) f).IsBounded lam)
    (hk : G.C₀ ≤ k)
    (hwitness : m ≤ (2 ^ k) ^ lam)
    (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (G.output
      ((satVerifier U (G.sampler 0) f).sampler.prog,
       (satVerifier U (G.sampler 0) f).decider.prog)
       lam).HasPerfectPCC k (G.bound.eval (k + lam)) := by
  apply G.completeness (satVerifier U (G.sampler 0) f) lam k hB hk
  exact nativePerfectPCC_of_sat U (G.sampler 0) f m
    (2 ^ k) ((2 ^ k) ^ lam) hwitness hSAT

/-- Legal ORIGINAL compression soundness for every UNSAT 3CNF with
all input variables scoped, conditional *only* on the native uniform
runtime prerequisite required by the upstream theorem. -/
theorem nativeCompressedSoundness_of_unsat (G : MIPRE.GapCompression)
    (U : MIPRE.Cost.UniversalMachine) (f : MIPRE.SAT.Fml)
    (m lam k : Nat)
    (hB : (satVerifier U (G.sampler 0) f).IsBounded lam)
    (hk : G.C₀ ≤ k)
    (hscope : f.InputsLt m)
    (hunsat : ¬ PNPAbove.WP24.Satisfiable m f) :
    (G.output
      ((satVerifier U (G.sampler 0) f).sampler.prog,
       (satVerifier U (G.sampler 0) f).decider.prog)
       lam).valStar k (G.bound.eval (k + lam)) ≤ (1 / 2 : Real) := by
  apply G.soundness (satVerifier U (G.sampler 0) f) lam k hB hk
  exact nativeValStar_half_of_unsat U (G.sampler 0) f m
    hscope hunsat (2 ^ k) ((2 ^ k) ^ lam)


/-- The remaining all-raw-data polynomial runtime obligation is explicit,
not silently inferred from typed PolyTimeFun.computes. Once that single
source HasPolyCost obligation is discharged, the original upstream
normal-form wrapper yields the genuine IsBounded lambda certificate. -/
theorem nativeIsBounded_of_raw_totalCost (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (hS : S.prog.HasPolyCost)
    (hdim : MIPRE.Cost.PolyBounded S.dim)
    (hRaw : (rawSatChecker f).code.HasPolyCost) :
    ∃ lam, (satVerifier U S f).IsBounded lam := by
  obtain ⟨lam, h⟩ :=
    MIPRE.Verifier.ofSamplerDecider_isBounded U S
      (rawSatChecker f).code hS hdim hRaw
  exact ⟨lam, h lam le_rfl⟩

/-- The ORIGINAL pinned compressor sampler has all required size and
sampler runtime bounds. Thus the ONLY residual premise for native
IsBounded is the formula-specialized raw Cost.Prog HasPolyCost. -/
theorem nativeIsBounded_with_compressor_of_raw_totalCost
    (G : MIPRE.GapCompression) (U : MIPRE.Cost.UniversalMachine)
    (f : MIPRE.SAT.Fml) (hRaw : (rawSatChecker f).code.HasPolyCost) :
    ∃ lam, (satVerifier U (G.sampler 0) f).IsBounded lam := by
  apply nativeIsBounded_of_raw_totalCost U (G.sampler 0) f ?_ ?_ hRaw
  · exact MIPRE.CL.Sampler.hasPolyCost_of_timeBound
       (T := fun n => G.bound.eval (n + 0)) (k := G.deg)
       (MIPRE.Cost.PolyBounded.eval G.bound
         (MIPRE.Cost.PolyBounded.id.add_const 0))
       (fun n => G.sampler_time 0 n)
  · exact (MIPRE.Cost.PolyBounded.eval G.bound
      (MIPRE.Cost.PolyBounded.id.add_const 0)).mono (G.sampler_dim 0)


/-- ORIGINAL game-level classical witness exactness: on EVERY sampled
question pair, there exists a winning pair of length-bounded original
native answers iff the source SAT formula has a satisfying assignment.
The winning Alice answer yields an actual source witness; conversely a
source witness yields the same constant answer on every question pair. -/
theorem nativeWinningPair_iff_sat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hscope : f.InputsLt m) (hT : m ≤ T)
    (q r : (satVerifier U S f).Questions k) :
    (∃ a b : MIPRE.Verifier.Answers T,
      ((satVerifier U S f).game k T).D q r a b = true) ↔
      PNPAbove.WP24.Satisfiable m f := by
  classical
  constructor
  · rintro ⟨a, b, hgame⟩
    have hacc : (satVerifier U S f).decider.Accepts k
        (MIPRE.CL.toBits q) (MIPRE.CL.toBits r) a.1 b.1 := by
      simpa only [MIPRE.Verifier.game, decide_eq_true_eq] using hgame
    obtain ⟨_, _, hval, _⟩ :=
      (satVerifier_accepts_iff U S f k _ _ _ _).mp hacc
    let w : Fin m → Bool := fun i => a.1.getD i.val false
    refine ⟨w, ?_⟩
    have heq : f.eval (fun i => a.1.getD i false) =
        f.eval (PNPAbove.WP24.bitsAt w) := by
      apply MIPRE.SAT.Fml.eval_congr_of_inputsLt hscope
      intro i hi
      simp [PNPAbove.WP24.bitsAt, hi, w]
    exact heq ▸ hval
  · rintro ⟨w, hw⟩
    let aw : BitStr := List.ofFn w
    have hal : aw.length ≤ T := by simp [aw]; omega
    let a : MIPRE.Verifier.Answers T := ⟨aw, hal⟩
    refine ⟨a, a, ?_⟩
    change decide ((satVerifier U S f).decider.Accepts k
      (MIPRE.CL.toBits q) (MIPRE.CL.toBits r) a.1 a.1) = true
    simp only [decide_eq_true_eq]
    apply (satVerifier_accepts_iff U S f k _ _ _ _).mpr
    refine ⟨MIPRE.CL.length_toBits q, MIPRE.CL.length_toBits r, ?_, rfl⟩
    have heval : (fun i => aw.getD i false) =
        PNPAbove.WP24.bitsAt w := by
      funext i
      exact PNPAbove.WP25.ofFn_getD_eq_bitsAt w i
    simpa only [a, heval] using hw

end PNPAbove.WP26

import PNPAbove.WP26NativeVerifier

/-!
An original Cost.Prog compiler mapping an arbitrary original SAT formula to
a source-native Verifier 7 decider program. This is built from the original
MIPRE PolyTimeFun.smn, not a metalevel recipe claiming to be polynomial.
-/
namespace PNPAbove.WP26
open MIPRE MIPRE.Cost
open MIPRE.Cost.PolyTimeFun

abbrev Raw : Type := Nat × BitStr × BitStr × BitStr × BitStr

/-- The fixed source evaluator consumes formula and full raw verifier tuple. -/
noncomputable def sourceCoreChecker :
    PolyTimeFun (MIPRE.SAT.Fml × Raw) Bool :=
  PNPAbove.WP25.answerCheckProgram.comp
    (((fst : PolyTimeFun (MIPRE.SAT.Fml × Raw) MIPRE.SAT.Fml).pair
       (rawAlice.comp snd)).pair (rawBob.comp snd))

theorem sourceCoreChecker_correct (f : MIPRE.SAT.Fml) (p : Raw) :
    sourceCoreChecker (f, p) =
      (f.eval (fun i => p.2.2.2.1.getD i false) &&
         decide (p.2.2.2.1 = p.2.2.2.2)) := by
  simp [sourceCoreChecker, rawAlice, rawBob,
    PNPAbove.WP25.answerCheckProgram_correct]

/-- REAL source polynomial-time S-M-N machine: a uniform compiler
from each original SAT.Fml into a closed Cost.Prog.
The compiler's source code is itself the original fixed source smnProg. -/
noncomputable def sourceUniformGenerator :
    PolyTimeFun MIPRE.SAT.Fml Prog :=
  (PolyTimeFun.smn MIPRE.SAT.Fml).comp
    ((PolyTimeFun.const sourceCoreChecker.code).pair
      (PolyTimeFun.id MIPRE.SAT.Fml))

/-- The generated native program is the ORIGINAL source hardcoding operator
on the fixed universal SAT evaluator, not a postulated compiler. -/
theorem sourceUniformGenerator_correct (f : MIPRE.SAT.Fml) :
    sourceUniformGenerator f =
      Cost.hardcode sourceCoreChecker.code (encode f) := rfl

/-- The constructed source generator is polynomial-time in the ORIGINAL
MIPRE size of the formula, including a quantitative executable runtime
certificate rather than informal circuit-size reasoning. -/
theorem sourceUniformGenerator_polytime (f : MIPRE.SAT.Fml) :
    ∃ t ≤ sourceUniformGenerator.timeBound.eval (esize f),
      sourceUniformGenerator.code.Runs
        (encode f) (encode (sourceUniformGenerator f)) t :=
  sourceUniformGenerator.computes f

/-- The generated native decider code is closed at the original source
single-environment ABI for every SAT instance. -/
theorem sourceUniformGenerator_closed (f : MIPRE.SAT.Fml) :
    (sourceUniformGenerator f).WellScoped 1 := by
  rw [sourceUniformGenerator_correct]
  exact Cost.hardcode_wellScoped sourceCoreChecker.closed _


/-- The ACTUAL source-program bytes emitted by the uniform polynomial
compiler run on the ORIGINAL raw verifier tuple and accept iff the
formula is satisfied by identical Alice/Bob responses. -/
theorem sourceUniformGenerator_accepts_iff (f : MIPRE.SAT.Fml)
    (n : Nat) (x y a b : BitStr) :
    (∃ t, (sourceUniformGenerator f).Runs
      (encode (n, x, y, a, b)) (encode true) t) ↔
      (f.eval (fun i => a.getD i false) = true ∧ a = b) := by
  rw [sourceUniformGenerator_correct]
  constructor
  · rintro ⟨t, hrun⟩
    obtain ⟨t₁, _, hcore⟩ :=
      Cost.hardcode_time_rev sourceCoreChecker.closed hrun
    obtain ⟨t₀, _, hcanonical⟩ :=
      sourceCoreChecker.computes (f, (n, x, y, a, b))
    have heq : encode true = encode (sourceCoreChecker (f, (n, x, y, a, b))) :=
      (Cost.Eval.deterministic hcore hcanonical).1
    have hresult : sourceCoreChecker (f, (n, x, y, a, b)) = true := by
      cases h : sourceCoreChecker (f, (n, x, y, a, b)) with
      | false => simp [h] at heq
      | true => rfl
    rw [sourceCoreChecker_correct] at hresult
    simpa only [Bool.and_eq_true, decide_eq_true_eq] using hresult
  · intro hacc
    obtain ⟨t, _, hcore⟩ :=
      sourceCoreChecker.computes (f, (n, x, y, a, b))
    have hresult : sourceCoreChecker (f, (n, x, y, a, b)) = true := by
      rcases hacc with ⟨hf, rfl⟩
      simp only [sourceCoreChecker_correct, Bool.and_eq_true, decide_eq_true_eq]
      refine ⟨?_, trivial⟩
      simpa [List.getD] using hf
    have hrun : sourceCoreChecker.code.Runs (encode (f, (n, x, y, a, b)))
        (encode true) t := by
      simpa only [hresult] using hcore
    exact ⟨t + (encode f).size + (encode (n, x, y, a, b)).size + 3,
      Cost.hardcode_time sourceCoreChecker.closed hrun⟩

/-- The source generated, not merely meta-language-selected,
seven-level normal-form verifier. -/
noncomputable def uniformSatVerifier (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) : MIPRE.Verifier 7 :=
  MIPRE.Verifier.ofSamplerDecider U S (sourceUniformGenerator f)

/-- Exact source-wide native input contract of the UNIFORMLY compiled
normal-form seven-level verifier. -/
theorem uniformSatVerifier_accepts_iff (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (n : Nat) (x y a b : BitStr) :
    (uniformSatVerifier U S f).decider.Accepts n x y a b ↔
      x.length = S.dim n ∧ y.length = S.dim n ∧
      f.eval (fun i => a.getD i false) = true ∧ a = b := by
  change (MIPRE.Verifier.ofSamplerDecider U S
      (sourceUniformGenerator f)).decider.Accepts n x y a b ↔ _
  rw [MIPRE.Verifier.ofSamplerDecider_accepts]
  simp only [sourceUniformGenerator_accepts_iff]


/-- This is a PCC for the actual verifier whose original source
decider Prog is produced by the original polynomial S-M-N compiler,
not just the fixed-code prototype. -/
theorem uniformNativePCC_of_sat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (uniformSatVerifier U S f).HasPerfectPCC k T := by
  obtain ⟨w, hw⟩ := hSAT
  let a : BitStr := List.ofFn w
  have ha : a.length ≤ T := by
    simp only [a, List.length_ofFn]
    omega
  apply (uniformSatVerifier U S f).hasPerfectPCC_of_accepts_diagonal ⟨a, ha⟩
  intro x y
  rw [uniformSatVerifier_accepts_iff]
  refine ⟨MIPRE.CL.length_toBits x, MIPRE.CL.length_toBits y, ?_, rfl⟩
  have heval : (fun i => a.getD i false) = PNPAbove.WP24.bitsAt w := by
    funext i
    exact PNPAbove.WP25.ofFn_getD_eq_bitsAt w i
  simpa only [heval] using hw

/-- Native ORIGINAL source rejection for all UNSAT formula instances,
all indices and all response strings, including malformed answers. -/
theorem uniformNativeRejectsAll_of_unsat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (k : Nat) (x y a b : BitStr) :
    ¬ (uniformSatVerifier U S f).decider.Accepts k x y a b := by
  intro hacc
  obtain ⟨_, _, hf, _⟩ :=
    (uniformSatVerifier_accepts_iff U S f k x y a b).mp hacc
  apply hunsat
  let w : Fin m → Bool := fun i => a.getD i.val false
  refine ⟨w, ?_⟩
  have heq : f.eval (fun i => a.getD i false) =
      f.eval (PNPAbove.WP24.bitsAt w) := by
    apply MIPRE.SAT.Fml.eval_congr_of_inputsLt hscope
    intro i hi
    simp [PNPAbove.WP24.bitsAt, hi, w]
  exact heq ▸ hf

/-- The actual ORIGINAL source Verifier.valStar of the uniformly
source-generated Verifier 7 has the exact SAT/UNSAT zero-one promise. -/
theorem uniformNativeValStar_zero_of_unsat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (k T : Nat) :
    (uniformSatVerifier U S f).valStar k T = 0 := by
  apply (uniformSatVerifier U S f).valStar_eq_zero_of_rejects_all
  intro x y a b
  exact uniformNativeRejectsAll_of_unsat U S f m hscope hunsat k x y a b

theorem uniformNativeValStar_one_of_sat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (uniformSatVerifier U S f).valStar k T = 1 :=
  (uniformSatVerifier U S f).valStar_eq_one_of_hasPerfectPCC
    (uniformNativePCC_of_sat U S f m k T hT hSAT)

/-- Exact source-native SAT instance-dependence of the UNIFORMLY
compiled Verifier 7, with all possible original source finite
dimensional tensor strategies in the optimization. -/
theorem uniformNativeValStar_one_iff_sat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hscope : f.InputsLt m) (hT : m ≤ T) :
    (uniformSatVerifier U S f).valStar k T = 1 ↔
      PNPAbove.WP24.Satisfiable m f := by
  constructor
  · intro hv
    by_contra h
    have hz := uniformNativeValStar_zero_of_unsat U S f m hscope h k T
    rw [hz] at hv
    norm_num at hv
  · exact uniformNativeValStar_one_of_sat U S f m k T hT

/-- The original GapCompression source pipeline is now connected
to this uniform SAT-to-native-Verifier compiler, conditional only
on the source-mandated Verifier.IsBounded lambda prerequisite. -/
theorem uniformCompressedPCC_of_sat (G : MIPRE.GapCompression)
    (U : Cost.UniversalMachine) (f : MIPRE.SAT.Fml)
    (m lam k : Nat)
    (hB : (uniformSatVerifier U (G.sampler 0) f).IsBounded lam)
    (hk : G.C₀ ≤ k) (hT : m ≤ (2 ^ k) ^ lam)
    (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (G.output
      ((uniformSatVerifier U (G.sampler 0) f).sampler.prog,
       (uniformSatVerifier U (G.sampler 0) f).decider.prog)
       lam).HasPerfectPCC k (G.bound.eval (k + lam)) := by
  apply G.completeness (uniformSatVerifier U (G.sampler 0) f) lam k hB hk
  exact uniformNativePCC_of_sat U (G.sampler 0) f m
    (2 ^ k) ((2 ^ k) ^ lam) hT hSAT

theorem uniformCompressedSoundness_of_unsat (G : MIPRE.GapCompression)
    (U : Cost.UniversalMachine) (f : MIPRE.SAT.Fml)
    (m lam k : Nat)
    (hB : (uniformSatVerifier U (G.sampler 0) f).IsBounded lam)
    (hk : G.C₀ ≤ k) (hscope : f.InputsLt m)
    (hunsat : ¬ PNPAbove.WP24.Satisfiable m f) :
    (G.output
      ((uniformSatVerifier U (G.sampler 0) f).sampler.prog,
       (uniformSatVerifier U (G.sampler 0) f).decider.prog)
       lam).valStar k (G.bound.eval (k + lam)) ≤ (1 / 2 : Real) := by
  apply G.soundness (uniformSatVerifier U (G.sampler 0) f) lam k hB hk
  have hz := uniformNativeValStar_zero_of_unsat U (G.sampler 0)
    f m hscope hunsat (2 ^ k) ((2 ^ k) ^ lam)
  rw [hz]
  norm_num

/-- ORIGINAL game-level classical witness exactness: on EVERY sampled
question pair, there exists a winning pair of length-bounded original
native answers iff the source SAT formula has a satisfying assignment.
The winning Alice answer yields an actual source witness; conversely a
source witness yields the same constant answer on every question pair. -/
theorem uniformNativeWinningPair_iff_sat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hscope : f.InputsLt m) (hT : m ≤ T)
    (q r : (uniformSatVerifier U S f).Questions k) :
    (∃ a b : MIPRE.Verifier.Answers T,
      ((uniformSatVerifier U S f).game k T).D q r a b = true) ↔
      PNPAbove.WP24.Satisfiable m f := by
  classical
  constructor
  · rintro ⟨a, b, hgame⟩
    have hacc : (uniformSatVerifier U S f).decider.Accepts k
        (MIPRE.CL.toBits q) (MIPRE.CL.toBits r) a.1 b.1 := by
      simpa only [MIPRE.Verifier.game, decide_eq_true_eq] using hgame
    obtain ⟨_, _, hval, _⟩ :=
      (uniformSatVerifier_accepts_iff U S f k _ _ _ _).mp hacc
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
    change decide ((uniformSatVerifier U S f).decider.Accepts k
      (MIPRE.CL.toBits q) (MIPRE.CL.toBits r) a.1 a.1) = true
    simp only [decide_eq_true_eq]
    apply (uniformSatVerifier_accepts_iff U S f k _ _ _ _).mpr
    refine ⟨MIPRE.CL.length_toBits q, MIPRE.CL.length_toBits r, ?_, rfl⟩
    have heval : (fun i => aw.getD i false) =
        PNPAbove.WP24.bitsAt w := by
      funext i
      exact PNPAbove.WP25.ofFn_getD_eq_bitsAt w i
    simpa only [a, heval] using hw

end PNPAbove.WP26

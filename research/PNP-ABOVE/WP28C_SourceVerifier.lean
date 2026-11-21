import PNPAbove.WP28CPower

/-! Real native source PowerIndex verifier and fixed numeric source exponent. -/

namespace PNPAbove.WP28C
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun
open Polynomial

/-- Original source verifier runtime is polynomial on EVERY raw input,
with a fixed, source-computed polynomial and NO formula parameter.
This is a bona fide upstream Prog.HasPolyCost proof, not the typed
PolyTimeFun-computes theorem misapplied to malformed inputs. -/
theorem powerIndexedRawChecker_hasPolyCost : powerIndexedRawChecker.code.HasPolyCost := by
  have hB : PolyCost
      (fun n d => powerIndexedRawChecker.timeBound.eval
        ((Data.cons (encode n) d).size)) :=
    PolyCost.poly powerIndexedRawChecker.timeBound PNPAbove.WP28B2.raw_input_size_PolyCost
  apply Prog.hasPolyCost_of_polyCost hB
  intro n d
  obtain ⟨t, ht, hrun⟩ :=
    powerIndexedRawChecker.computes (Data.cons (encode n) d)
  refine ⟨encode (powerIndexedRawChecker (Data.cons (encode n) d)), t, ht, ?_⟩
  simpa only [encode_data] using hrun

/-- ORIGINAL native seven-level verifier with FIXED programme code
independent of arbitrary SAT instance f. The source question sampler
is a real upstream CL.Sampler 7, with exact question-length wrapper. -/
noncomputable def powerIndexedVerifier
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7) :
    MIPRE.Verifier 7 :=
  MIPRE.Verifier.ofSamplerDecider U S powerIndexedRawChecker.code

/-- Native ORIGINAL source Decider.Accepts has the exact
SAT indexed instance predicate, including the required question-length
checks for every original well-formed native input. -/
theorem powerIndexedVerifier_accepts_iff
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (x y a b : BitStr) :
    (powerIndexedVerifier U S).decider.Accepts
       (2 ^ PNPAbove.WP28B.formulaIndex f) x y a b ↔
      x.length = S.dim (2 ^ PNPAbove.WP28B.formulaIndex f) ∧
      y.length = S.dim (2 ^ PNPAbove.WP28B.formulaIndex f) ∧
      f.eval (fun i => a.getD i false) = true ∧ a = b := by
  change (MIPRE.Verifier.ofSamplerDecider U S
    powerIndexedRawChecker.code).decider.Accepts _ x y a b ↔ _
  rw [MIPRE.Verifier.ofSamplerDecider_accepts]
  constructor
  · rintro ⟨hx, hy, t, ht⟩
    refine ⟨hx, hy, ?_⟩
    obtain ⟨t₀, _, hcanon⟩ := powerIndexedRawChecker.computes
      (encode (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b))
    have hcanon' : powerIndexedRawChecker.code.Runs
        (encode (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b))
        (encode (powerIndexedRawChecker (encode
          (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b)))) t₀ := by
      simpa only [encode_data] using hcanon
    have heq : encode true =
        encode (powerIndexedRawChecker (encode
          (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b))) :=
      (Cost.Eval.deterministic ht hcanon').1
    have htruth : powerIndexedRawChecker (encode
        (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b)) = true := by
      cases hv : powerIndexedRawChecker (encode
        (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b)) with
      | false => simp [hv] at heq
      | true => rfl
    rw [powerIndexedRawChecker_correct] at htruth
    simpa only [Bool.and_eq_true, decide_eq_true_eq] using htruth
  · rintro ⟨hx, hy, hSAT, heq⟩
    refine ⟨hx, hy, ?_⟩
    obtain ⟨t, _, hrun⟩ := powerIndexedRawChecker.computes
      (encode (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b))
    have hv : powerIndexedRawChecker (encode
        (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b)) = true := by
      rw [powerIndexedRawChecker_correct]
      simp only [Bool.and_eq_true, decide_eq_true_eq]
      exact ⟨hSAT, heq⟩
    refine ⟨t, ?_⟩
    simpa only [encode_data, hv] using hrun

/-- The standard source sampler from the genuine upstream compressor,
combined with the NEW source HasPolyCost, yields ONE FIXED native
Verifier.IsBounded lambda for ALL 2^k encoded SAT formulas. -/
theorem powerIndexedVerifier_exists_uniform_lam
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine) :
    ∃ lam, (powerIndexedVerifier U (G.sampler 0)).IsBounded lam := by
  have hs : (G.sampler 0).prog.HasPolyCost :=
    MIPRE.CL.Sampler.hasPolyCost_of_timeBound
      (T := fun n => G.bound.eval (n + 0)) (k := G.deg)
      (PolyBounded.eval G.bound (PolyBounded.id.add_const 0))
      (fun n => G.sampler_time 0 n)
  have hdim : PolyBounded (G.sampler 0).dim :=
    (PolyBounded.eval G.bound (PolyBounded.id.add_const 0)).mono
      (G.sampler_dim 0)
  obtain ⟨lam, hlam⟩ :=
    MIPRE.Verifier.ofSamplerDecider_isBounded
      U (G.sampler 0) powerIndexedRawChecker.code
      hs hdim powerIndexedRawChecker_hasPolyCost
  exact ⟨lam, hlam lam le_rfl⟩

end PNPAbove.WP28C

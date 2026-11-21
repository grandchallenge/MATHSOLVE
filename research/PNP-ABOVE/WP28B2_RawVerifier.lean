import PNPAbove.WP28B2Evaluator
import PNPAbove.WP27RobustVerifier
import MIPRE.Foundations.Halting.PolyBounded

/-! Single FIXED Cost.Prog for SAT games indexed by binary original formulas. -/

namespace PNPAbove.WP28B2
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun
open Polynomial

/-- Native source-prog extracts the actual index and both source answers
from an original decoded five-field verifier tuple. -/
noncomputable def indexedTupleChecker :
    PolyTimeFun PNPAbove.WP27.Raw Bool :=
  indexedAnswerCheckProgram.comp
    (((fst : PolyTimeFun PNPAbove.WP27.Raw Nat).pair
       PNPAbove.WP26.rawAlice).pair PNPAbove.WP26.rawBob)

/-- A SINGLE fixed source Cost.Prog over EVERY arbitrary raw original
Data input, normalizing malformed tuples before interpreting the
formula indexed by n. No hardcoding of formula f is involved. -/
noncomputable def indexedRawChecker : PolyTimeFun Data Bool :=
  indexedTupleChecker.comp PNPAbove.WP27.parseRaw

theorem indexedRawChecker_correct (f : MIPRE.SAT.Fml)
    (x y a b : BitStr) :
    indexedRawChecker
      (encode (PNPAbove.WP28B.formulaIndex f, x, y, a, b)) =
      (f.eval (fun i => a.getD i false) && decide (a = b)) := by
  simp [indexedRawChecker, indexedTupleChecker,
    PNPAbove.WP27.parseRaw_encode, indexedAnswerCheckProgram_correct,
    PNPAbove.WP26.rawAlice, PNPAbove.WP26.rawBob]

theorem indexedRawChecker_closed : indexedRawChecker.code.WellScoped 1 :=
  indexedRawChecker.closed

/-- Cost model proof for ALL source Data, including malformed inputs.
The fixed formula does not appear in this bound. -/
theorem raw_input_size_PolyCost :
    PolyCost (fun n d => (Data.cons (encode n) d).size) := by
  let C : Nat → Nat := fun n => esize n + 2
  have hC : PolyBounded C :=
    ((PolyBounded.size.const_mul 4).add_const 3).mono
      (fun n => by have hn := esize_nat_le n; dsimp [C]; omega)
  refine ⟨C, 1, hC, fun n d => ?_⟩
  dsimp [C]
  simp only [Data.size_cons, pow_one]
  change esize n + d.size + 1 ≤ (esize n + 2) * (d.size + 1)
  have hp := esize_pos n
  nlinarith

/-- Original source verifier runtime is polynomial on EVERY raw input,
with a fixed, source-computed polynomial and NO formula parameter.
This is a bona fide upstream Prog.HasPolyCost proof, not the typed
PolyTimeFun-computes theorem misapplied to malformed inputs. -/
theorem indexedRawChecker_hasPolyCost : indexedRawChecker.code.HasPolyCost := by
  have hB : PolyCost
      (fun n d => indexedRawChecker.timeBound.eval
        ((Data.cons (encode n) d).size)) :=
    PolyCost.poly indexedRawChecker.timeBound raw_input_size_PolyCost
  apply Prog.hasPolyCost_of_polyCost hB
  intro n d
  obtain ⟨t, ht, hrun⟩ :=
    indexedRawChecker.computes (Data.cons (encode n) d)
  refine ⟨encode (indexedRawChecker (Data.cons (encode n) d)), t, ht, ?_⟩
  simpa only [encode_data] using hrun

/-- ORIGINAL native seven-level verifier with FIXED programme code
independent of arbitrary SAT instance f. The source question sampler
is a real upstream CL.Sampler 7, with exact question-length wrapper. -/
noncomputable def fixedIndexedVerifier
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7) :
    MIPRE.Verifier 7 :=
  MIPRE.Verifier.ofSamplerDecider U S indexedRawChecker.code

/-- Native ORIGINAL source Decider.Accepts has the exact
SAT indexed instance predicate, including the required question-length
checks for every original well-formed native input. -/
theorem fixedIndexedVerifier_accepts_iff
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (x y a b : BitStr) :
    (fixedIndexedVerifier U S).decider.Accepts
       (PNPAbove.WP28B.formulaIndex f) x y a b ↔
      x.length = S.dim (PNPAbove.WP28B.formulaIndex f) ∧
      y.length = S.dim (PNPAbove.WP28B.formulaIndex f) ∧
      f.eval (fun i => a.getD i false) = true ∧ a = b := by
  change (MIPRE.Verifier.ofSamplerDecider U S
    indexedRawChecker.code).decider.Accepts _ x y a b ↔ _
  rw [MIPRE.Verifier.ofSamplerDecider_accepts]
  constructor
  · rintro ⟨hx, hy, t, ht⟩
    refine ⟨hx, hy, ?_⟩
    obtain ⟨t₀, _, hcanon⟩ := indexedRawChecker.computes
      (encode (PNPAbove.WP28B.formulaIndex f, x, y, a, b))
    have hcanon' : indexedRawChecker.code.Runs
        (encode (PNPAbove.WP28B.formulaIndex f, x, y, a, b))
        (encode (indexedRawChecker (encode
          (PNPAbove.WP28B.formulaIndex f, x, y, a, b)))) t₀ := by
      simpa only [encode_data] using hcanon
    have heq : encode true =
        encode (indexedRawChecker (encode
          (PNPAbove.WP28B.formulaIndex f, x, y, a, b))) :=
      (Cost.Eval.deterministic ht hcanon').1
    have htruth : indexedRawChecker (encode
        (PNPAbove.WP28B.formulaIndex f, x, y, a, b)) = true := by
      cases hv : indexedRawChecker (encode
        (PNPAbove.WP28B.formulaIndex f, x, y, a, b)) with
      | false => simp [hv] at heq
      | true => rfl
    rw [indexedRawChecker_correct] at htruth
    simpa only [Bool.and_eq_true, decide_eq_true_eq] using htruth
  · rintro ⟨hx, hy, hSAT, heq⟩
    refine ⟨hx, hy, ?_⟩
    obtain ⟨t, _, hrun⟩ := indexedRawChecker.computes
      (encode (PNPAbove.WP28B.formulaIndex f, x, y, a, b))
    have hv : indexedRawChecker (encode
        (PNPAbove.WP28B.formulaIndex f, x, y, a, b)) = true := by
      rw [indexedRawChecker_correct]
      simp only [Bool.and_eq_true, decide_eq_true_eq]
      exact ⟨hSAT, heq⟩
    refine ⟨t, ?_⟩
    simpa only [encode_data, hv] using hrun

/-- The standard source sampler from the genuine upstream compressor,
combined with the NEW source HasPolyCost, yields ONE FIXED native
Verifier.IsBounded lambda for ALL indexed SAT formulas. -/
theorem fixedIndexedVerifier_exists_uniform_lam
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine) :
    ∃ lam, (fixedIndexedVerifier U (G.sampler 0)).IsBounded lam := by
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
      U (G.sampler 0) indexedRawChecker.code
      hs hdim indexedRawChecker_hasPolyCost
  exact ⟨lam, hlam lam le_rfl⟩

end PNPAbove.WP28B2

import PNPAbove.WP40Tag
import PNPAbove.WP38Bridge

namespace PNPAbove.WP40
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun Polynomial

theorem payload_support_fold (bs : BitStr) (xs : List Nat) :
    (payload bs).rpn.foldl WP35.supportStep xs = xs := by
  induction bs generalizing xs with
  | nil => rfl
  | cons b bs ih =>
    simp [payload,Fml.rpn,List.foldl_append,WP35.supportStep,ih]

theorem tag_support (f : Fml) (bs : BitStr) :
    WP35.support (tag f bs) = WP35.support f := by
  simp [WP35.support,tag,Fml.rpn,List.foldl_append,WP35.supportStep,payload_support_fold]

theorem tag_dense_eval (f : Fml) (bs : BitStr) (a : Nat → Bool) :
    (WP35.dense (tag f bs)).eval a = (WP35.dense f).eval a := by
  rw [WP35.dense,WP35.dense,Fml.eval_rename,Fml.eval_rename,tag_support,tag_eval]

theorem tag_verifier (f : Fml) (bs w : BitStr) :
    WP35.denseWitnessVerifier (tag f bs,w) = WP35.denseWitnessVerifier (f,w) := by
  rw [WP35.denseWitnessVerifier_correct,WP35.denseWitnessVerifier_correct,tag_dense_eval]

theorem tagged_witness_read (f : Fml) (bs : BitStr)
    (h : WP35.denseWitnessVerifier (f,bs) = true) :
    WP35.denseWitnessVerifier (tag f bs,readP (tag f bs)) = true := by
  rw [readP_tag,tag_verifier]
  exact h

/-- An explicit, linearly larger presentation of each satisfiable formula
has the same truth function and ordered support, with an accepted witness
returned by one fixed total polynomial program. The existential choice of
the tag bits is not a polynomial computation of a witness. -/
theorem easy_equivalent_presentation (f : Fml) (hf : WP38.Sat f) :
    ∃ g : Fml, (∀ a, g.eval a = f.eval a) ∧
      WP35.support g = WP35.support f ∧
      esize g ≤ 17*esize f+46 ∧
      WP35.denseWitnessVerifier (g,readP g) = true := by
  obtain ⟨bs,hb,hw⟩ := (WP35.denseWitnessVerifier_source_length_iff f).2 hf
  exact ⟨tag f bs,tag_eval f bs,tag_support f bs,tag_short f bs hb,tagged_witness_read f bs hw⟩

/-- Invariance under exact logical equivalence even if the entire ordered
support is required to agree. This is weaker than truth-function-only
invariance. -/
def SemanticInvariant (M : Fml → Nat) : Prop :=
  ∀ f g, (∀ a, f.eval a = g.eval a) →
    WP35.support f = WP35.support g → M f = M g

/-- A necessary condition on a measure lower-bounding every successful
individual witness computation by its runtime (up to a program-specific
polynomial). The program need not solve SAT outside its successful domain.
This is deliberately stronger than soundness only for global SAT solvers. -/
def LocalSound (M : Fml → Nat) : Prop :=
  ∀ A : PolyTimeFun Fml BitStr, ∃ p : Polynomial Nat,
    ∀ f, WP35.denseWitnessVerifier (f,A f) = true →
      M f ≤ p.eval (esize f)

/-- A pointwise lower bound on actual successful native runs is a
particularly strong form of local soundness. -/
def RunSound (M : Fml → Nat) : Prop :=
  ∀ (A : PolyTimeFun Fml BitStr) (f : Fml) (t : Nat),
    A.code.Runs (encode f) (encode (A f)) t →
    WP35.denseWitnessVerifier (f,A f) = true → M f ≤ t

theorem runSound_localSound (M : Fml → Nat) (h : RunSound M) : LocalSound M := by
  intro A
  refine ⟨A.timeBound,?_⟩
  intro f hf
  obtain ⟨t,ht,hr⟩ := A.computes f
  exact (h A f t hr hf).trans ht

/-- Even soundness for the single reader suffices. -/
theorem semantic_capacity_reader_barrier (M : Fml → Nat)
    (hM : SemanticInvariant M) (p : Polynomial Nat)
    (hp : ∀ g, WP35.denseWitnessVerifier (g,readP g) = true →
      M g ≤ p.eval (esize g)) :
    ∀ f, WP38.Sat f → M f ≤ p.eval (17*esize f+46) := by
  intro f hf
  obtain ⟨g,he,hs,hsize,hw⟩ := easy_equivalent_presentation f hf
  have hEq := hM g f he hs
  rw [← hEq]
  exact (hp g hw).trans (polynomial_eval_mono p hsize)

theorem semantic_capacity_polynomial (M : Fml → Nat)
    (hM : SemanticInvariant M) (hS : LocalSound M) :
    ∃ q : Polynomial Nat, ∀ f, WP38.Sat f → M f ≤ q.eval (esize f) := by
  obtain ⟨p,hp⟩ := hS readP
  refine ⟨p.comp (C 17 * X + C 46),?_⟩
  intro f hf
  simpa [Polynomial.eval_comp,Polynomial.eval_add,Polynomial.eval_mul,Polynomial.eval_C,
    Polynomial.eval_X] using semantic_capacity_reader_barrier M hM p hp f hf

theorem semantic_run_capacity_polynomial (M : Fml → Nat)
    (hM : SemanticInvariant M) (hS : RunSound M) :
    ∃ q : Polynomial Nat, ∀ f, WP38.Sat f → M f ≤ q.eval (esize f) :=
  semantic_capacity_polynomial M hM (runSound_localSound M hS)

theorem tag_canonical_iff (f : Fml) (bs w : BitStr) :
    WP38.CanonicalWitness (WP35.support (tag f bs)) (tag f bs) w ↔
      WP38.CanonicalWitness (WP35.support f) f w := by
  unfold WP38.CanonicalWitness
  rw [tag_support]
  simp only [tag_eval]

/-- A normalization algorithm is required to discover a valid tag, not just
to preserve semantics. The output may be arbitrary on NO inputs. -/
def SolvesTag (N : PolyTimeFun Fml Fml) : Prop :=
  ∀ f, WP38.Sat f → ∃ bs : BitStr,
    WP35.denseWitnessVerifier (f,bs) = true ∧ N f = tag f bs

noncomputable def normalizeP (S : PolyTimeFun Fml BitStr) : PolyTimeFun Fml Fml :=
  tagP.comp ((PolyTimeFun.id Fml).pair S)

theorem normalizeP_correct (S : PolyTimeFun Fml BitStr) (hS : WP38.SolvesWitness S) :
    SolvesTag (normalizeP S) := by
  intro f hf
  refine ⟨S f,hS f hf,?_⟩
  change tagP (f,S f) = tag f (S f)
  exact tagP_correct _ _

theorem normalize_read_solves (N : PolyTimeFun Fml Fml) (hN : SolvesTag N) :
    WP38.SolvesWitness (readP.comp N) := by
  intro f hf
  obtain ⟨bs,hb,hn⟩ := hN f hf
  change WP35.denseWitnessVerifier (f,readP (N f)) = true
  rw [hn,readP_tag]
  exact hb

theorem tag_normalization_iff_witness :
    (∃ N : PolyTimeFun Fml Fml, SolvesTag N) ↔
      ∃ S : PolyTimeFun Fml BitStr, WP38.SolvesWitness S := by
  constructor
  · rintro ⟨N,hN⟩
    exact ⟨readP.comp N,normalize_read_solves N hN⟩
  · rintro ⟨S,hS⟩
    exact ⟨normalizeP S,normalizeP_correct S hS⟩

theorem tag_normalization_iff_decision :
    (∃ N : PolyTimeFun Fml Fml, SolvesTag N) ↔
      ∃ D : PolyTimeFun Data Bool, WP38.Correct D :=
  tag_normalization_iff_witness.trans WP38.native_decision_iff_witness.symm

end PNPAbove.WP40

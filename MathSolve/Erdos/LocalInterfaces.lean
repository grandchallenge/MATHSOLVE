import Mathlib

/-!
# Reusable exact interfaces related to Erdős 241 and 595

These are local mathematical lemmas, not proofs of the two open problems.
The finite additive-set API uses h-element multisets WITH repetition.
The graph API concerns bipartite edge layers, which are a restricted class
of triangle-free layers. No source-completion or MathCert is implied.
-/

namespace MathSolve.Erdos

/-- All h-element multisets from A have distinct integer sums. -/
def StrongBH (A : Finset ℕ) (h : ℕ) : Prop :=
  ∀ m n : Multiset ℕ,
    m.card = h → n.card = h →
    (∀ x ∈ m, x ∈ A) → (∀ x ∈ n, x ∈ A) →
    m.sum = n.sum → m = n

/-- All h-element multisets from A have distinct sums modulo M. -/
def StrongBHMod (A : Finset ℕ) (h M : ℕ) : Prop :=
  ∀ m n : Multiset ℕ,
    m.card = h → n.card = h →
    (∀ x ∈ m, x ∈ A) → (∀ x ∈ n, x ∈ A) →
    m.sum % M = n.sum % M → m = n

/-- Modular distinctness always implies integer distinctness, even for M=0. -/
theorem strongBH_of_mod (A : Finset ℕ) (h M : ℕ)
    (hm : StrongBHMod A h M) : StrongBH A h := by
  intro m n hmcard hncard hmA hnA heq
  apply hm m n hmcard hncard hmA hnA
  simp [heq]

/-- If all relevant sums lie below the modulus, no new collisions arise. -/
theorem strongBHMod_iff_of_sum_lt
    (A : Finset ℕ) (h M : ℕ)
    (hbound : ∀ m : Multiset ℕ, m.card = h →
      (∀ x ∈ m, x ∈ A) → m.sum < M) :
    StrongBHMod A h M ↔ StrongBH A h := by
  constructor
  · exact strongBH_of_mod A h M
  · intro hint m n hmcard hncard hmA hnA hmod
    apply hint m n hmcard hncard hmA hnA
    simpa [Nat.mod_eq_of_lt (hbound m hmcard hmA),
      Nat.mod_eq_of_lt (hbound n hncard hnA)] using hmod

/-- Two natural numbers with equal residues modulo M cannot differ by a
positive amount less than M. This is the local no-wrap arithmetic core. -/
theorem nat_mod_eq_of_close {a b M : ℕ}
    (hab : a ≤ b) (hgap : b - a < M)
    (hmod : a % M = b % M) : a = b := by
  omega

/-- An interval with diameter strictly less than M has injective reduction
modulo M, independent of where that interval starts. -/
theorem nat_mod_injective_on_interval
    {α : Type*} (f : α → ℕ) (lo hi M : ℕ)
    (hlo : ∀ x, lo ≤ f x)
    (hhi : ∀ x, f x ≤ hi)
    (hwidth : hi - lo < M) :
    Function.Injective (fun x => f x % M) ↔ Function.Injective f := by
  constructor
  · intro hmod x y hf
    apply hmod
    simp [hf]
  · intro hf x y hmod
    apply hf
    by_cases hxy : f x ≤ f y
    · apply nat_mod_eq_of_close hxy ?_ hmod
      have ha := hlo x
      have hb := hhi y
      omega
    · have hyx : f y ≤ f x := by omega
      apply Eq.symm
      apply nat_mod_eq_of_close hyx ?_ hmod.symm
      have ha := hlo y
      have hb := hhi x
      omega

/-- t edge-layers, each with a two-valued vertex colouring separating
    the endpoints of every edge it contains; the layers cover precisely E. -/
def HasBipartiteLayerCover {V : Type*}
    (E : V → V → Prop) (t : ℕ) : Prop :=
  ∃ H : Fin t → V → V → Prop,
    (∀ i, ∃ c : V → Bool,
      ∀ u v, H i u v → c u ≠ c v) ∧
    (∀ u v, E u v ↔ ∃ i, H i u v)

/-- A t-layer bipartite cover is equivalent to a separating t-bit
    vertex labelling. No symmetry or finite-cardinality assumption is needed. -/
theorem bipartiteLayerCover_iff_bitCode {V : Type*}
    (E : V → V → Prop) (t : ℕ) :
    HasBipartiteLayerCover E t ↔
      ∃ code : V → Fin t → Bool,
        ∀ u v, E u v → code u ≠ code v := by
  classical
  constructor
  · rintro ⟨H, hbits, hcover⟩
    let c : (i : Fin t) → V → Bool := fun i => Classical.choose (hbits i)
    have hc (i : Fin t) (u v : V) (h : H i u v) :
        c i u ≠ c i v := (Classical.choose_spec (hbits i)) u v h
    refine ⟨fun v i => c i v, ?_⟩
    intro u v huv heq
    obtain ⟨i, hi⟩ := (hcover u v).mp huv
    exact hc i u v hi (congrFun heq i)
  · rintro ⟨code, hproper⟩
    refine ⟨(fun i u v => E u v ∧ code u i ≠ code v i), ?_, ?_⟩
    · intro i
      refine ⟨(fun v => code v i), ?_⟩
      intro u v huv
      exact huv.2
    · intro u v
      constructor
      · intro huv
        have hne : code u ≠ code v := hproper u v huv
        have hi : ∃ i : Fin t, code u i ≠ code v i := by
          by_contra hnot
          push_neg at hnot
          apply hne
          funext i
          exact hnot i
        obtain ⟨i, hdiff⟩ := hi
        exact ⟨i, huv, hdiff⟩
      · rintro ⟨i, hi⟩
        exact hi.1

end MathSolve.Erdos

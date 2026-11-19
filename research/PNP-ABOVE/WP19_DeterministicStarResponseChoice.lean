import PNPAbove.WP18Value

namespace PNPAbove.WP19
open MIPRE MIPRE.CL MIPRE.Cost
open scoped Classical

variable {X A : Type*} [Fintype X] [Fintype A] [DecidableEq X] [DecidableEq A] [Nonempty A]

/-- Original game whose sampled bipartite question graph is one star together
with diagonal-only components disjoint from the star. -/
def StarMatching (G : SynchronousGame X A) (c : X) : Prop :=
  ∀ x y, G.μ x y ≠ 0 → x = c ∨ (x = y ∧ G.μ c x = 0)

/-- Choose a Bob answer on one spoke if there is an accepted answer. -/
noncomputable def spokeAnswer (G : SynchronousGame X A)
    (c : X) (a : A) (y : X) : A :=
  if h : ∃ b : A, G.D c y a b = true
  then Classical.choose h else Classical.choice inferInstance

theorem spokeAnswer_win (G : SynchronousGame X A)
    (c : X) (a b : A) (y : X)
    (h : G.D c y a b = true) :
    G.D c y a (spokeAnswer G c a y) = true := by
  unfold spokeAnswer
  split_ifs with hfound
  · exact Classical.choose_spec hfound
  · exact False.elim (hfound ⟨b, h⟩)

/-- A deterministic global choice indexed by the centre answer. Every isolated
diagonal question is assigned an accepted equal response if one exists. -/
noncomputable def starAnswer (G : SynchronousGame X A) (c : X)
    (a : A) (x : X) : A :=
  if x = c then a
  else if G.μ c x = 0 then WP17.chooseAnswer G x
  else spokeAnswer G c a x

theorem starAnswer_center (G : SynchronousGame X A) (c : X) (a : A) :
    starAnswer G c a c = a := by
  simp [starAnswer]

/-- Every accepted spoke wins under the centre-indexed deterministic assignment,
provided its source question pair is actually sampled. -/
theorem starAnswer_spoke_win (G : SynchronousGame X A) (c : X)
    (a b : A) (y : X)
    (hμ : G.μ c y ≠ 0) (hD : G.D c y a b = true) :
    G.D c y (starAnswer G c a c) (starAnswer G c a y) = true := by
  rw [starAnswer_center]
  by_cases hy : y = c
  · subst y
    have hab : a = b := by
      by_contra h
      have hf := G.synchronous c a b h
      rw [hf] at hD
      cases hD
    subst b
    simpa [starAnswer_center] using hD
  · have hspoke : starAnswer G c a y = spokeAnswer G c a y := by
      simp [starAnswer, hy, hμ]
    rw [hspoke]
    exact spokeAnswer_win G c a b y hD

/-- An isolated diagonal question can always use an accepted equal answer if
any such answer exists; synchronicity eliminates unequal accepted pairs. -/
theorem starAnswer_diag_win (G : SynchronousGame X A) (c : X)
    (v a b : A) (x : X) (hx : x ≠ c) (hμ : G.μ c x = 0)
    (hD : G.D x x a b = true) :
    G.D x x (starAnswer G c v x) (starAnswer G c v x) = true := by
  have hab : a = b := by
    by_contra h
    have hf := G.synchronous x a b h
    rw [hf] at hD
    cases hD
  have hf : WP17.feasible G x := ⟨a, by simpa [hab] using hD⟩
  simpa [starAnswer, hx, hμ] using WP17.chooseAnswer_spec G x hf

/-- Any accepted pair in the sampled star+isolated-matching graph can be
replaced by one deterministic global assignment, with its centre response
fixed to the observed Alice-centre answer. -/
theorem starAnswer_dominates_sampled (G : SynchronousGame X A) (c : X)
    (hstar : StarMatching G c) (x y : X) (v a b : A)
    (hμ : G.μ x y ≠ 0) (hD : G.D x y a b = true)
    (hv : x = c → v = a) :
    G.D x y (starAnswer G c v x) (starAnswer G c v y) = true := by
  rcases hstar x y hμ with hc | ⟨hxy,hzero⟩
  · subst x
    have hva : v = a := hv rfl
    subst v
    exact starAnswer_spoke_win G c a b y hμ hD
  · subst y
    by_cases hx : x = c
    · subst x
      exact False.elim (hμ hzero)
    · exact starAnswer_diag_win G c v a b x hx hzero hD

end PNPAbove.WP19

/-
Copyright 2026 The Formal Conjectures Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-/
import RequestProject.PublicationCertificate

namespace ProtectedSnapshot

open Cardinal Set

/-- A **3-uniform hypergraph** on vertex type `V` is a set of 3-element `Finset`s.
Each element of `edges` is a hyperedge, and `uniform` ensures each has exactly 3 vertices.

Note: Mathlib does not yet have a general hypergraph API; this fills that gap for the
3-uniform case relevant to Erdős problems 593 and 1177. -/
structure ThreeUniformHypergraph (V : Type) where
  /-- The set of hyperedges: each edge is a 3-element finset of vertices. -/
  edges : Set (Finset V)
  /-- Every hyperedge has exactly 3 vertices. -/
  uniform : ∀ e ∈ edges, e.card = 3

namespace ThreeUniformHypergraph

/-- A **proper coloring** of a 3-uniform hypergraph `H` by a color type `C` is a vertex
coloring such that no hyperedge is monochromatic (all three vertices receive the same color). -/
def IsProperColoring {V : Type} (H : ThreeUniformHypergraph V) {C : Type} (f : V → C) : Prop :=
  ∀ e ∈ H.edges, ∃ u ∈ e, ∃ v ∈ e, f u ≠ f v

/-- The **chromatic cardinal** of a 3-uniform hypergraph `H` is the infimum of cardinalities
of color types admitting a proper coloring.

In contrast to a `ℕ∞`-valued chromatic number, this `Cardinal`-valued definition distinguishes
between different infinite chromatic numbers (e.g., `ℵ₀` vs. `ℵ₁`). We work at `Type`
(universe 0) throughout to avoid universe metavariable issues. -/
noncomputable def chromaticCardinal {V : Type} (H : ThreeUniformHypergraph V) : Cardinal.{0} :=
  sInf {κ : Cardinal.{0} | ∃ (C : Type), #C = κ ∧ ∃ f : V → C, H.IsProperColoring f}

/-- A finite 3-uniform hypergraph `F` **appears** in `H` (as a sub-hypergraph) if there
exists an injective vertex map `φ : W → V` that sends every hyperedge of `F` to a hyperedge
of `H`. -/
def Appears {W V : Type} [DecidableEq V] (F : ThreeUniformHypergraph W)
    (H : ThreeUniformHypergraph V) : Prop :=
  ∃ φ : W → V, Function.Injective φ ∧ ∀ e ∈ F.edges, e.image φ ∈ H.edges

/-- A 3-uniform hypergraph `F` is **2-colorable** (has **Property B**) if there exists a
2-coloring of its vertices with no monochromatic edge.

This is the hypergraph analogue of bipartiteness for graphs: a graph is bipartite iff it
is 2-colorable as a graph. For 3-uniform hypergraphs, 2-colorability is a necessary condition
for being obligatory (every obligatory finite 3-uniform hypergraph is 2-colorable). -/
def IsTwoColorable {V : Type} (F : ThreeUniformHypergraph V) : Prop :=
  ∃ f : V → Fin 2, F.IsProperColoring f

end ThreeUniformHypergraph

/-- A finite 3-uniform hypergraph `F` on a `Fintype` vertex type is **obligatory** if it
appears in every 3-uniform hypergraph (on a `Type`-valued vertex set) whose chromatic
cardinal exceeds `ℵ₀`. -/
def IsObligatory {W : Type} [Fintype W] (F : ThreeUniformHypergraph W) : Prop :=
  ∀ (V : Type) [DecidableEq V] (H : ThreeUniformHypergraph V),
    ℵ₀ < H.chromaticCardinal → F.Appears H


end ProtectedSnapshot

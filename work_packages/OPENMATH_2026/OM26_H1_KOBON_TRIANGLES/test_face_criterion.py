#!/usr/bin/env python3
from __future__ import annotations
import random, unittest
from itertools import combinations
from pathlib import Path
import kobon_direct_oracle as oracle
import kobon_scorer as graph

ROOT=Path(__file__).resolve().parent

def graph_faces(lines):
    return {tuple(f["supporting_lines"]) for f in graph.score(lines)["faces"]}

class FaceCriterionTests(unittest.TestCase):
    def assert_same(self,lines): self.assertEqual(graph_faces(lines),set(oracle.direct_faces(lines)))
    def test_subdivided_triangle(self):
        lines=[(1,0,0),(0,1,0),(1,1,-2),(1,0,-1)]
        self.assert_same(lines); self.assertNotIn((0,1,2),set(oracle.direct_faces(lines)))
    def test_vertex_touch_does_not_kill_face(self):
        lines=[(1,0,0),(0,1,0),(1,1,-2),(1,1,0)]
        self.assert_same(lines); self.assertIn((0,1,2),set(oracle.direct_faces(lines)))
    def test_exhaustive_degenerate_pool(self):
        pool=[(1,0,0),(0,1,0),(1,-1,0),(1,1,0),(1,0,-2),(0,1,-2),(1,1,-2),(1,-1,-1)]
        for size in range(3,7):
            for subset in combinations(pool,size): self.assert_same(list(subset))
    def test_seeded_random_falsification(self):
        rng=random.Random(20260927)
        for n in range(3,9):
            accepted=0
            while accepted<60:
                lines=[]; seen=set()
                for _ in range(n):
                    for _attempt in range(100):
                        a=rng.randint(-6,6); b=rng.randint(-6,6); c=rng.randint(-10,10)
                        if a==0 and b==0: continue
                        line=oracle._normalize(a,b,c)
                        if line in seen: continue
                        seen.add(line); lines.append(line); break
                if len(lines)!=n: continue
                self.assert_same(lines); accepted+=1
    def test_locked_fixtures(self):
        for rel,expected in [
            ("baseline/solution.json",16),
            ("candidates/RG_STRUCTURED_FAMILY_058/solution.json",58),
            ("candidates/RD_LOCAL_MUTATION_086/solution.json",86),
        ]:
            lines,_=oracle.load_lines(ROOT/rel,18)
            self.assertEqual(len(oracle.direct_faces(lines)),expected)
            self.assertEqual(graph.score(lines)["triangles"],expected)
            self.assert_same(lines)
if __name__=="__main__": unittest.main()

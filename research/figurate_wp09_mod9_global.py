"""FIGURATE WP09: complete modulo-nine global Type B triple obstructions.

Mathematical theorem: for every k>=3 divisible by 3 and c=4 or 7
modulo 9, no positive-integer Type B triple exists, regardless of entries.
This is an all-triples, global impossibility statement, unlike WP09-001
which excludes only one specified triple.

Local table uses exact triple residue multisets with repetitions.
"""
from __future__ import annotations
import argparse
import json
from itertools import combinations_with_replacement

from research.figurate_census import polygonal


def residue_image(k: int, modulus: int = 9) -> tuple[int, ...]:
    if k < 3 or modulus < 2:
        raise ValueError("require order>=3 and modulus>=2")
    return tuple(sorted({polygonal(k, t) % modulus
                         for t in range(1, 2 * modulus + 1)}))


def first_local_triple(k: int, c: int, modulus: int = 9
                       ) -> tuple[int, int, int] | None:
    image = set(residue_image(k, modulus))
    for a, b, d in combinations_with_replacement(range(modulus), 3):
        if all((x*y+c) % modulus in image
               for x,y in ((a,b),(a,d),(b,d))):
            return a,b,d
    return None


def classification(modulus: int = 9) -> dict[int, tuple[int, ...]]:
    return {k%modulus: tuple(c for c in range(modulus)
                              if first_local_triple(k,c,modulus) is None)
            for k in range(modulus,2*modulus)}


def certificate(k: int, c: int, modulus: int = 9) -> dict:
    w=first_local_triple(k,c,modulus)
    return {"scheme":"FIGURATE-WP09-ODD-POWER-GLOBAL/1",
            "order":k,"offset":c,"modulus":modulus,
            "polygonal_residues":residue_image(k,modulus),
            "first_local_triple":w,
            "global_obstruction_by_modulus":w is None,
            "global_nonexistence_by_mod9_theorem":
                k%3==0 and c%9 in (4,7)}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--k",type=int)
    p.add_argument("--offset",type=int)
    p.add_argument("--modulus",type=int,default=9)
    args=p.parse_args()
    if (args.k is None)!=(args.offset is None):
        p.error("--k and --offset are required together")
    result=(classification(args.modulus) if args.k is None
            else certificate(args.k,args.offset,args.modulus))
    print(json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()

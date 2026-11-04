"""Exact degree-13 extension of verify_degree12.py; standard library only.

Run verify_degree12.py for degrees 1..12, then run this file for degree 13.
No floating-point arithmetic or numerical real-root test is used.
"""
from math import comb
from pathlib import Path
import json

from verify_degree12 import local_survivors


def main():
    rows = [local_survivors(13, k) for k in range(2, 13)]
    found = [(r["k"], s["q"], s["p"], s["v"])
             for r in rows for s in r["survivors"]]
    expected = [(2, 60, 13, 176), (2, 61, 13, 181),
                (2, 62, 13, 187), (2, 63, 13, 194),
                (2, 72, 14, 236), (2, 73, 14, 242),
                (2, 74, 14, 249), (3, 245, 86, 537)]
    assert found == expected, (found, expected)
    eliminations = []
    for k, q, p, v in found:
        if k == 2:
            if p == 13:
                allowed = {comb(13, 2) - 13}
            else:
                assert p == 14
                allowed = {comb(12, 2) + 2*12 - 14,
                           comb(11, 2) + 3*11 + 1 - 14}
            assert q not in allowed
            eliminations.append({"k": k, "q": q, "p": p,
                                 "reason": "small trace", "allowed_q": sorted(allowed)})
        else:
            assert k == 3
            # p=h2 and p+q=h3. Newton at indices 1 and 2 traps h1.
            lower = 13
            while 12*lower*lower < 26*p:
                lower += 1
            upper = (22*p*p) // (36*(p+q))
            assert lower > upper
            eliminations.append({"k": k, "q": q, "p": p,
                                 "reason": "inconsistent integer h1 interval",
                                 "h1_lower": lower, "h1_upper": upper})
    output = {"statement": "Q4.4 holds for every positive integer real-rooted degree-13 polynomial",
              "rows": rows, "survivors_before_final_elimination": found,
              "eliminations": eliminations, "survivors_after_final_elimination": []}
    path = Path(__file__).with_name("degree13_certificate.json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"rows": len(rows), "q_checked": sum(r["q_checked"] for r in rows),
                      "pairs_checked": sum(r["pairs_checked"] for r in rows),
                      "survivors": found, "all_excluded": True}, indent=2))


if __name__ == "__main__":
    main()

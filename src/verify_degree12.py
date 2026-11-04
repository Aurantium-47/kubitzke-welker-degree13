"""Exact finite certificate for Kubitzke--Welker Q4.4 in degrees 1..12.

Python 3.8+ standard library only; all comparisons use unbounded integers.
No floating-point root finding, coefficient-height cutoff, or numerical tolerance.
The accompanying degree12_proof.md proves that every possible counterexample
must survive these finite filters, including the whole unbounded tail.
"""
from math import comb, factorial
from pathlib import Path
import json


def kk(a, k):
    """Kruskal--Katona upper operator using the unique k-binomial expansion."""
    assert a >= 0 and k >= 1
    total, upper = 0, a + k
    for j in range(k, 0, -1):
        if a == 0:
            break
        lo, hi = j - 1, upper
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if comb(mid, j) <= a:
                lo = mid
            else:
                hi = mid
        n = lo
        assert comb(n, j) <= a < comb(n + 1, j)
        total += comb(n, j + 1) if n >= j + 1 else 0
        a -= comb(n, j)
        upper = n
    assert a == 0
    return total


def tail_cutoff(d, k):
    """Return N with rigorous all-n>=N tail certificate; see proof."""
    D = factorial(d) // factorial(d - k)
    n = k + 1
    while (d - k)**k * (factorial(k) * comb(n + 1, k))**(k + 1) > (
        D * (factorial(k + 1) * comb(n, k + 1))**k
    ):
        n += 1
    return n


def local_survivors(d, k):
    N = tail_cutoff(d, k)
    Q = comb(N, k)
    D = factorial(d) // factorial(d - k)
    left_factor = factorial(k + 1)**k * D
    right_factor = (d - k)**k * factorial(k)**(k + 1)
    passed_power, pairs_checked, survivors = 0, 0, []
    for q in range(1, Q):
        v = kk(q, k) + 1
        # Strict degree-sensitive inequality: equality already rules out failure.
        if v**k * left_factor >= right_factor * q**(k + 1):
            continue
        passed_power += 1
        # p=h_{k-1} >= C(d,k-1), and p < k(d-k)q/(d+1).
        max_p = (k * (d - k) * q - 1) // (d + 1)
        for p in range(comb(d, k - 1), max_p + 1):
            pairs_checked += 1
            c = p + q
            # Newton at index k, using h_{k+1} >= c+v.
            if c*c*k*(d - k) < p*(c + v)*(k + 1)*(d - k + 1):
                continue
            # Product of the preceding normalized-ratio inequalities.
            if p**k * (d - k + 1)**(k - 1) < (
                comb(d, k - 1) * k**(k - 1) * c**(k - 1)
            ):
                continue
            survivors.append({"q": q, "p": p, "v": v})
    return {"d": d, "k": k, "N": N, "Q": Q,
            "q_checked": Q - 1, "q_passing_power_bound": passed_power,
            "pairs_checked": pairs_checked, "survivors": survivors}


def main():
    assert kk(12, 2) == 11
    assert kk(61, 2) == 180
    rows = [local_survivors(d, k)
            for d in range(3, 13) for k in range(2, d)]
    found = [(r["d"], r["k"], s["q"], s["p"], s["v"])
             for r in rows for s in r["survivors"]]
    expected = [(11, 2, 41, 11, 95), (11, 2, 42, 11, 100),
                (12, 2, 50, 12, 131), (12, 2, 51, 12, 136),
                (12, 2, 52, 12, 142), (12, 2, 61, 13, 181),
                (12, 2, 62, 13, 187)]
    assert found == expected, (found, expected)
    # All surviving p=h1 equals d or d+1. The classical small-trace
    # classification restricts q=h2-h1 to the following exact values.
    for d, k, q, p, v in found:
        assert k == 2
        if p == d:
            allowed_q = {comb(d, 2) - d}
        elif p == d + 1:
            allowed_q = {
                comb(d - 1, 2) + 2*(d - 1) - (d + 1),
                comb(d - 2, 2) + 3*(d - 2) + 1 - (d + 1),
            }
        else:
            raise AssertionError("Unclassified trace")
        assert q not in allowed_q
    output = {"statement": "Q4.4 holds for every degree 1 <= d <= 12",
              "arithmetic": "Python arbitrary-precision integer arithmetic only",
              "rows": rows, "survivors_before_trace_classification": found,
              "survivors_after_trace_classification": []}
    path = Path(__file__).with_name("degree12_certificate.json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"rows": len(rows),
                      "q_checked": sum(r["q_checked"] for r in rows),
                      "pairs_checked": sum(r["pairs_checked"] for r in rows),
                      "survivors": found,
                      "trace_eliminated_all": True}, indent=2))


if __name__ == "__main__":
    main()

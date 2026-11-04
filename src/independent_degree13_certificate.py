"""Independent exact finite-tail audit of Q4.4 for actual degree 13.

No imports of the author's degree_bounds.py, check_local_pairs.py, or KK routine.
KK is tabulated independently by binomial blocks and Pascal's identity.
"""
from functools import lru_cache
from math import comb, factorial, prod
import json
from pathlib import Path


@lru_cache(maxsize=None)
def kk_table(k, limit):
    """Return K_k(a) for 0 <= a <= limit using binomial block recursion."""
    if k == 1:
        return [a*(a-1)//2 for a in range(limit+1)]
    if limit == 0:
        return [0]
    n = k
    while comb(n+1, k) <= limit:
        n += 1
    smaller = kk_table(k-1, comb(n, k-1)-1)
    values = [0] * (limit+1)
    for top in range(k, n+1):
        start = comb(top, k)
        end = min(comb(top+1, k), limit+1)
        leading = comb(top, k+1) if top > k else 0
        for a in range(start, end):
            values[a] = leading + smaller[a-start]
    return values


records = []
survivors = []
tested_q = 0
for d in [13]:
    for k in range(2, d):
        falling = prod(range(d-k+1, d+1))
        left_constant = factorial(k+1)**k * falling
        right_constant = (d-k)**k * factorial(k)**(k+1)
        N = k+1
        while (right_constant * comb(N+1, k)**(k+1)
               > left_constant * comb(N, k+1)**k):
            N += 1
        Q = comb(N, k)
        K = kk_table(k, Q-1)
        local = []
        bad_q_count = 0
        for q in range(1, Q):
            v = K[q]+1
            if left_constant * v**k >= right_constant * q**(k+1):
                continue  # Strict power bound excludes equality as well.
            bad_q_count += 1
            # Necessary integral range for p=h_{k-1}.
            lower = comb(d, k-1)
            upper = (k*(d-k)*q-1)//(d+1)
            for p in range(lower, upper+1):
                c = p+q
                # Newton at k, with the least possible failing g_{k+1}=v.
                if k*(d-k)*c*c < (k+1)*(d-k+1)*p*(c+v):
                    continue
                # Product of the preceding normalized ratio inequalities.
                if (p**k * (d-k+1)**(k-1)
                        < comb(d, k-1) * (k*c)**(k-1)):
                    continue
                local.append([q, p, v])
                survivors.append([d, k, q, p, v])
        tested_q += Q-1
        records.append(dict(d=d, k=k, N=N, Q=Q,
                            q_candidates=bad_q_count, local_pairs=local))
        print(f"d={d}, k={k}: N={N}, Q={Q}, surviving pairs={local}", flush=True)

expected = [[13,2,60,13,176], [13,2,61,13,181], [13,2,62,13,187],
            [13,2,63,13,194], [13,2,72,14,236], [13,2,73,14,242],
            [13,2,74,14,249], [13,3,245,86,537]]
assert survivors == expected, survivors

# Independent exact final elimination.
for d, k, q, p, v in survivors:
    if k == 2:
        if p == d:
            permitted_q = {comb(d, 2)-d}
        else:
            assert p == d+1
            permitted_q = {comb(d-1,2)+2*(d-1)-p,
                           comb(d-2,2)+3*(d-2)+1-p}
        assert q not in permitted_q
    else:
        assert [k,q,p,v] == [3,245,86,537]
        # Newton index 1 excludes h1 <= 13, index 2 excludes h1 >= 14.
        assert 12*13**2 < 26*p
        assert 36*(p+q)*14 > 22*p*p

out = Path(__file__).with_name("independent_degree13_certificate.json")
out.write_text(json.dumps(dict(max_degree=13, tested_q=tested_q,
                               surviving_pairs=survivors, records=records), indent=2)+"\n")
print(f"PASS: {tested_q:,} q values across {len(records)} (d,k) pairs; all eight degree-13 survivors excluded.")
print(f"Certificate: {out}")

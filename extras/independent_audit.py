"""Independent exact-arithmetic spot checks, not an exhaustive conjecture search."""
from fractions import Fraction
from math import comb, factorial
from random import Random


def upper_operator(a, k, shift=0):
    """shift=0: simplicial KK; shift=1: Macaulay."""
    answer, high = 0, None
    while a:
        low = k
        if high is None:
            high = k
            while comb(high, k) <= a:
                high *= 2
        while low < high:
            middle = (low + high + 1) // 2
            if comb(middle, k) <= a:
                low = middle
            else:
                high = middle - 1
        n = low
        a -= comb(n, k)
        answer += comb(n + shift, k + 1) if n + shift >= k + 1 else 0
        high, k = n - 1, k - 1
    return answer


def verify_transition(h, k):
    d = len(h) - 1
    a, b = h[k] - h[k - 1], h[k + 1] - h[k]
    if a <= 0 or b <= 0:
        return False
    # Raise to the kth power to remove all radicals, retaining exactness.
    lhs = factorial(k + 1)**k * b**k * (factorial(d) // factorial(d - k))
    rhs = (d - k)**k * (factorial(k) * a)**(k + 1)
    assert lhs < rhs
    assert h[k - 1] / h[k] < Fraction(k * (d - k), (k + 1) * (d - k + 1))
    assert h[k] < Fraction((k + 1) * (d - k + 1), d + 1) * a
    return True


for k in range(1, 16):
    for a in range(1, 5001):
        mac = upper_operator(a, k, 1)
        assert mac - a == upper_operator(a, k)
        assert factorial(k + 1)**k * mac**k >= (factorial(k) * a)**(k + 1)
print("75,000 exact Macaulay lower-bound and K=M-a checks passed.")

rng = Random(20261104)
transitions = 0
for _ in range(10000):
    d = rng.randrange(2, 17)
    ratios = sorted([Fraction(rng.randrange(1, 300), rng.randrange(1, 30))
                     for _ in range(d)], reverse=True)
    normalized = Fraction(1)
    h = [normalized]
    for i, ratio in enumerate(ratios, 1):
        normalized *= ratio
        h.append(normalized * comb(d, i))
    for k in range(1, d):
        transitions += verify_transition(h, k)
print(f"10,000 rational degree-Newton sequences; {transitions:,} positive transitions passed.")

family_checks = 0
for d in range(2, 15):
    for m in (1, 2, 3, 10, 100):
        h = [Fraction(comb(d, i) * m**i) for i in range(d + 1)]
        for k in range(1, d):
            family_checks += verify_transition(h, k)
print(f"{family_checks} exact binomial-family transitions passed.")

import sympy as sp
x = sp.symbols("x")
h = [1, 13, 74, 255, 570, 906, 1050, 894, 555, 245, 73, 13, 1]
d = len(h) - 1
slacks = [i*(d-i)*h[i]**2 - (i+1)*(d-i+1)*h[i-1]*h[i+1]
          for i in range(1, d)]
assert slacks == [83, 125, 68475, 450, 1260, 1764, 1260, 450, 75, 1475, 107]
assert all(s > 0 for s in slacks)
assert upper_operator(61, 2) == 180 < 181
p = sp.Poly(sum(v*x**i for i, v in enumerate(h)), x, domain=sp.QQ)
chain = [sp.Poly(q, x) for q in sp.sturm(p.as_expr(), x)]
signs_plus = [int(sp.sign(q.LC())) for q in chain]
signs_minus = [s*(-1)**q.degree() for s, q in zip(signs_plus, chain)]
variation = lambda signs: sum(a != b for a, b in zip(signs, signs[1:]))
assert [q.degree() for q in chain] == list(range(12, -1, -1))
assert variation(signs_minus) == 8 and variation(signs_plus) == 4
assert sp.gcd(p, p.diff()).degree() == 0
assert p.count_roots(-sp.oo, sp.oo) == 4
print("Degree-12 obstruction: Newton, KK, squarefreeness and four-real-root Sturm certificate passed.")

p5 = sp.Poly(1+6*x+12*x**2+12*x**3+6*x**4+x**5, x)
assert upper_operator(12, 2) == 11
assert p5.count_roots(-sp.oo, sp.oo) == 3
print("Degree-5 coefficient obstruction: K_2(12)=11; exactly three real roots.")

# Direct face-set verification of the small-trace construction.
from itertools import combinations


def ballot(n):
    return {ss for j in range(n // 2 + 1)
            for ss in combinations(range(1, n + 1), j)
            if all(x >= 2 * (i + 1) for i, x in enumerate(ss))}


def convolution(a, b):
    h = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            h[i + j] += x * y
    return h


face_examples = 0
for d in range(1, 19):
    for family in (1, 2, 3):
        if family == 3 and d < 2:
            continue
        if family == 1:
            h = [comb(d, i) for i in range(d + 1)]
        else:
            n = d - family + 1
            factor = [1, 2] if family == 2 else [1, 3, 1]
            h = convolution([comb(n, i) for i in range(n + 1)], factor)
        peak = next((i - 1 for i in range(1, d + 1) if h[i] <= h[i - 1]), d)
        g = [1] + [h[i] - h[i - 1] for i in range(1, peak + 1)]
        faces = ballot(d)
        if family > 1:
            faces |= {tuple((*face, d + 1)) for face in ballot(d - family + 1)}
        assert all(tuple(f[:i] + f[i + 1:]) in faces
                   for f in faces for i in range(len(f)))
        face_vector = [sum(len(f) == j for f in faces)
                       for j in range(1 + max(map(len, faces)))]
        assert face_vector == g, (d, family, g, face_vector)
        face_examples += 1
print(f"Small-trace constructions: {face_examples} full face-set checks in degrees 1–18 passed.")

h = [1, 13, 74, 255, 575, 921, 1075, 921, 575, 255, 74, 13, 1]
slacks = [i*(12-i)*h[i]**2 - (i+1)*(13-i)*h[i-1]*h[i+1]
          for i in range(1, 12)]
assert slacks == [83, 125, 53675, 11525, 18435, 38691,
                  18435, 11525, 53675, 125, 83]
p = sp.Poly(sum(v*x**i for i, v in enumerate(h)), x, domain=sp.QQ)
gamma = [1, 1, -2, 6, -20, 21, -3]
assert sp.expand(p.as_expr() - sum(g*x**j*(1+x)**(12-2*j)
                                 for j, g in enumerate(gamma))) == 0
assert sp.gcd(p, p.diff()).degree() == 0
assert p.count_roots(-sp.oo, sp.oo) == 2
print("Palindromic obstruction: strict Newton, gamma certificate and two-real-root count passed.")

"""Small, exact checks supplementing rather than replacing exhaustive replay."""
import importlib.util
from itertools import combinations
import json
from math import comb, factorial
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'src' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


submitted = module('verify_degree12')
interval = module('referee_degree12_alternative')


class ExactTests(unittest.TestCase):
    def test_kk_small_colex_face_counts(self):
        # Count all higher faces whose lower faces belong to the colex segment.
        # This finite-set definition is independent of the binomial algorithms.
        n = 7
        for k in range(1, 6):
            faces = sorted(combinations(range(n), k), key=lambda s: sum(1 << x for x in s))
            for q in range(len(faces) + 1):
                chosen = set(faces[:q])
                expected = sum(all(face in chosen for face in combinations(higher, k))
                               for higher in combinations(range(n), k + 1))
                self.assertEqual(submitted.kk(q, k), expected, (q, k))
                self.assertEqual(interval.upper(q, k), expected, (q, k))

    def test_known_operator_boundaries(self):
        self.assertEqual(submitted.kk(12, 2), 11)
        self.assertEqual(submitted.kk(61, 2), 180)
        self.assertEqual(submitted.kk(245, 3), 536)
        for k in range(1, 8):
            for n in range(k, 20):
                self.assertEqual(submitted.kk(comb(n, k), k), comb(n, k + 1))

    def test_cutoffs_and_strict_predecessors(self):
        for d in range(3, 14):
            for k in range(2, d):
                n = submitted.tail_cutoff(d, k)
                self.assertEqual(n, interval.cutoff(d, k))
                falling = factorial(d) // factorial(d-k)
                def good(m):
                    return (d-k)**k * (factorial(k)*comb(m+1, k))**(k+1) <= (
                        falling * (factorial(k+1)*comb(m, k+1))**k)
                self.assertTrue(good(n))
                if n > k+1:
                    self.assertFalse(good(n-1))
                # Samples guard implementation endpoints. Infinite coverage is a proof step.
                for m in (n+1, n+2, n+100):
                    self.assertTrue(good(m))

    def test_palindromic_newton_obstruction(self):
        h = [1,13,74,255,575,921,1075,921,575,255,74,13,1]
        self.assertEqual(h, h[::-1])
        slacks = [i*(12-i)*h[i]**2-(i+1)*(13-i)*h[i-1]*h[i+1]
                  for i in range(1,12)]
        self.assertEqual(slacks, [83,125,53675,11525,18435,38691,
                                  18435,11525,53675,125,83])
        self.assertGreater(min(slacks), 0)
        gamma = []
        for i in range(7):
            gamma.append(h[i] - sum(gamma[j]*comb(12-2*j, i-j) for j in range(i)))
        self.assertEqual(gamma, [1,1,-2,6,-20,21,-3])
        self.assertEqual(h[3]-h[2], 181)
        self.assertEqual(submitted.kk(h[2]-h[1], 2), 180)

    def test_final_degree13_contradiction(self):
        self.assertLess(12*13**2, 26*86)
        self.assertGreaterEqual(12*14**2, 26*86)
        self.assertGreater(36*331*14, 22*86**2)
        self.assertEqual((22*86**2)//(36*331), 13)

    def test_full_index_coverage_and_counts(self):
        rows = []
        for name in ('degree12_certificate.json', 'degree13_certificate.json'):
            obj = json.loads((ROOT/'certificates'/name).read_text())
            rows.extend(obj['rows'])
        self.assertEqual([(r['d'], r['k']) for r in rows],
                         [(d,k) for d in range(3,14) for k in range(2,d)])
        self.assertEqual(sum(r['q_checked'] for r in rows), 10445449)
        self.assertEqual(sum(r['pairs_checked'] for r in rows), 60581487)
        self.assertEqual(sum(len(r['survivors']) for r in rows), 15)
        self.assertTrue(all(r['q_checked'] == r['Q']-1 for r in rows))


if __name__ == '__main__':
    unittest.main()

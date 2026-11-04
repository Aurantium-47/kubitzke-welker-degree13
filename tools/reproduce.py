#!/usr/bin/env python3
"""Reproduce the complete exact certificate set without editing committed data."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
JOBS = [
    ('verify_degree12.py', 'degree12_certificate.json'),
    ('verify_degree13.py', 'degree13_certificate.json'),
    ('independent_degree_certificate.py', 'independent_degree_certificate.json'),
    ('independent_degree13_certificate.py', 'independent_degree13_certificate.json'),
    ('referee_degree12_alternative.py', 'referee_degree12_alternative.json'),
    ('referee_degree13_alternative.py', 'referee_degree13_alternative.json'),
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def release_files():
    for path in ROOT.rglob('*'):
        relative = path.relative_to(ROOT)
        if any(part in {'.git', 'build', '.venv', '__pycache__'} for part in relative.parts):
            continue
        if relative.as_posix() == 'SHA256SUMS' or path.suffix in {'.pyc', '.pyo'}:
            continue
        if relative.parts[0] == 'src' and path.suffix == '.json':
            continue  # Direct script invocations may create ignored local outputs.
        require(not path.is_symlink(), 'Unexpected symlink: ' + str(relative))
        if path.is_file():
            yield path


def verify_manifest():
    expected = {}
    for line in (ROOT / 'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        require(name not in expected, 'Duplicate manifest entry: ' + name)
        relative = Path(name)
        require(not relative.is_absolute() and '..' not in relative.parts,
                'Unsafe manifest path: ' + name)
        expected[name] = digest
    actual = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in release_files()}
    require(actual.keys() == expected.keys(),
            'Release file set differs: missing=%s, unexpected=%s' %
            (sorted(expected.keys() - actual.keys()), sorted(actual.keys() - expected.keys())))
    for name, digest in expected.items():
        require(actual[name] == digest, 'Checksum mismatch: ' + name)
    return len(expected)


def load(name):
    return json.loads((ROOT / 'certificates' / name).read_text(encoding='utf-8'))


def cross_check():
    count = 0
    total_q = total_pairs = 0
    for main_name, block_name, interval_name in [
        ('degree12_certificate.json', 'independent_degree_certificate.json',
         'referee_degree12_alternative.json'),
        ('degree13_certificate.json', 'independent_degree13_certificate.json',
         'referee_degree13_alternative.json'),
    ]:
        main, block, interval = load(main_name), load(block_name), load(interval_name)
        main_rows = {(r['d'], r['k']): r for r in main['rows']}
        block_rows = {(r['d'], r['k']): r for r in block['records']}
        interval_rows = {(r['d'], r['k']): r for r in interval['rows']}
        require(main_rows.keys() == block_rows.keys() == interval_rows.keys(),
                'Different index coverage: ' + main_name)
        for key, row in main_rows.items():
            b, i = block_rows[key], interval_rows[key]
            require((row['N'], row['Q']) == (b['N'], b['Q']) == (i['N'], i['Q']),
                    'Tail cutoff mismatch: ' + str(key))
            require(row['q_checked'] == row['Q'] - 1, 'Finite count mismatch: ' + str(key))
            require(row['q_passing_power_bound'] == b['q_candidates'],
                    'Power-filter count mismatch: ' + str(key))
            submitted = [[s['q'], s['p'], s['v']] for s in row['survivors']]
            quadratic = [s[2:] for s in i['survivors']]
            require(submitted == b['local_pairs'] == quadratic,
                    'Survivor mismatch: ' + str(key))
            count += 1
            total_q += row['q_checked']
            total_pairs += row['pairs_checked']
    require(count == 66 and total_q == 10445449 and total_pairs == 60581487,
            'Unexpected aggregate counts')
    return {'rows': count, 'finite_q_values': total_q, 'submitted_p_pairs': total_pairs}


def run_logged(command, cwd, log_path):
    start = time.perf_counter()
    with log_path.open('w', encoding='utf-8') as stream:
        result = subprocess.run(command, cwd=str(cwd), stdout=stream,
                                stderr=subprocess.STDOUT, check=False)
    require(result.returncode == 0, 'Command failed; see ' + str(log_path.relative_to(ROOT)))
    return round(time.perf_counter() - start, 3)


def main():
    if not __debug__ or sys.flags.optimize:
        raise SystemExit('Refusing optimized Python: assertions must be enabled; omit -O.')
    if sys.version_info < (3, 8):
        raise SystemExit('Python 3.8+ is required.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--quick', action='store_true',
                        help='Hashes and unit tests only; does not rerun enumeration')
    args = parser.parse_args()
    build = ROOT / 'build'
    build.mkdir(exist_ok=True)
    # Remove an old success receipt before any new check; failure cannot look like success.
    receipt = build / 'reproduction.json'
    if receipt.exists():
        receipt.unlink()
    manifest_count = verify_manifest()
    print('PASS: %d release-file checksums' % manifest_count, flush=True)
    seconds = run_logged([sys.executable, '-I', '-m', 'unittest', 'discover',
                          '-s', str(ROOT / 'tests'), '-v'], ROOT, build / 'unit-tests.log')
    print('PASS: exact unit tests (%.3fs)' % seconds, flush=True)
    rows = cross_check()
    print('PASS: stored three-way certificate consistency, 66 rows', flush=True)
    stages = []
    if not args.quick:
        with tempfile.TemporaryDirectory(prefix='q44-replay-') as directory:
            temp = Path(directory)
            for source in (ROOT / 'src').glob('*.py'):
                shutil.copyfile(source, temp / source.name)
            for script, output in JOBS:
                print('RUN: ' + script, flush=True)
                elapsed = run_logged([sys.executable, '-I', '-B', '-c',
                                      "import runpy, sys; sys.path.insert(0, '.'); "
                                      "runpy.run_path(sys.argv[1], run_name='__main__')", script], temp,
                                     build / (script[:-3] + '.log'))
                result = json.loads((temp / output).read_text(encoding='utf-8'))
                require(result == load(output), 'Regenerated certificate differs: ' + output)
                stages.append({'script': script, 'output': output, 'seconds': elapsed,
                               'complete_json_match': True})
                print('PASS: %s (%.3fs)' % (output, elapsed), flush=True)
    result = {'status': 'passed', 'mode': 'quick' if args.quick else 'full',
              'python': sys.version.split()[0], 'release_files': manifest_count,
              'unit_tests_seconds': seconds, 'certificate_consistency': rows,
              'enumeration_rerun': not args.quick, 'stages': stages,
              'note': 'Computational reproduction, not human peer review or formal proof checking.'}
    receipt.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print('PASS: %s; summary in build/reproduction.json' %
          ('quick checks only, enumeration NOT rerun' if args.quick else 'complete six-program replay'))


if __name__ == '__main__':
    main()

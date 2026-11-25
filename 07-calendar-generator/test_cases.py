# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('Thursday start',
  '3\n30\n',
  ['Mo Tu We Th Fr Sa Su\n          1  2  3  4\n', '26 27 28 29 30\n']),
 ('Monday four full weeks',
  '0\n28\n',
  [' 1  2  3  4  5  6  7\n', '22 23 24 25 26 27 28\n']),
 ('Sunday start 31 days', '6\n31\n', ['                   1\n', '30 31\n']),
 ('29 days', '0\n29\n', ['22 23 24 25 26 27 28\n29\n']),
 ('weekday out of range', '7\n30\n', ['Invalid weekday or month length']),
 ('invalid short month', '0\n27\n', ['Invalid weekday or month length']),
 ('negative weekday', '-1\n30\n', ['Invalid weekday or month length']),
 ('nonnumeric', 'Monday\n30\n', ['Invalid weekday or month length'])]

for name, data, expected in tests:
    result = subprocess.run(
        [sys.executable, str(solution)], input=data,
        text=True, capture_output=True, timeout=5)
    if result.returncode != 0:
        raise AssertionError(name + ': program crashed\n' + result.stderr)
    for line in expected:
        if line not in result.stdout:
            raise AssertionError(name + ': missing ' + repr(line)
                                 + '\nActual output:\n' + result.stdout)
    print('PASS:', name)
print(str(len(tests)) + ' tests passed')

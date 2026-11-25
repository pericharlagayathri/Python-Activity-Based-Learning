# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('priority and shortages',
  '10 8\n3\nNorth 2 6 5\nSouth 5 7 6\nEast 1 2 3\n',
  ['South allocated: [7, 6] unmet: [0, 0]\n'
   'North allocated: [3, 2] unmet: [3, 3]\n'
   'East allocated: [0, 0] unmet: [2, 3]\n'
   'Stock remaining: [0, 0]']),
 ('stable tie',
  '5 5\n2\nFirst 2 4 4\nSecond 2 4 4\n',
  ['First allocated: [4, 4] unmet: [0, 0]\n'
   'Second allocated: [1, 1] unmet: [3, 3]']),
 ('zero stock',
  '0 0\n1\nA 1 2 3\n',
  ['A allocated: [0, 0] unmet: [2, 3]', 'Stock remaining: [0, 0]']),
 ('surplus stock', '10 10\n1\nA 0 2 3\n', ['Stock remaining: [8, 7]']),
 ('negative stock', '-1 5\n1\n', ['Invalid stock or area count']),
 ('negative demand', '5 5\n1\nA 2 -1 2\n', ['Invalid area data']),
 ('duplicate names', '5 5\n2\nA 1 2 2\nA 2 2 2\n', ['Invalid area data']),
 ('wrong demand shape', '5 5\n1\nA 1 2\n', ['Invalid area data']),
 ('invalid count', '5 5\n0\n', ['Invalid stock or area count'])]

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

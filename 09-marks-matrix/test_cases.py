# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('matrix and tied toppers',
  '3 3\n80 30 70\n90 20 70\n50 40 60\n',
  ['Student 1 total: 180 average: 60.0 min: 30 max: 80',
   'Top students: [1, 2] total: 180',
   'Subject 2 total: 90 average: 30.0 min: 20 max: 40',
   'Low-average subjects: [2]']),
 ('single zero',
  '1 1\n0\n',
  ['Student 1 total: 0 average: 0.0 min: 0 max: 0',
   'Top students: [1] total: 0',
   'Low-average subjects: [1]']),
 ('40 boundary not low',
  '2 1\n30\n50\n',
  ['Subject 1 total: 80 average: 40.0', 'Low-average subjects: []']),
 ('maximum mark',
  '1 2\n100 100\n',
  ['total: 200 average: 100.0', 'Low-average subjects: []']),
 ('too high mark', '1 1\n101\n', ['Invalid marks matrix']),
 ('negative mark', '1 1\n-1\n', ['Invalid marks matrix']),
 ('ragged matrix', '2 2\n10 20\n30\n', ['Invalid marks matrix']),
 ('zero students', '0 2\n', ['Invalid matrix dimensions']),
 ('bad dimensions', 'x 2\n', ['Invalid matrix dimensions'])]

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

# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('exact thresholds',
  '15 20 8 40\nyes\n',
  ['Attendance: 75.0 %\nELIGIBLE\n']),
 ('all conditions fail',
  '14 20 6 35\nno\n',
  ['NOT ELIGIBLE',
   'attendance below 75%',
   'fewer than 8 completed labs',
   'internal marks below 40',
   'fees not cleared']),
 ('fully eligible',
  '20 20 10 100\nyes\n',
  ['Attendance: 100.0 %\nELIGIBLE\n']),
 ('below attendance boundary',
  '74 100 8 40\nyes\n',
  ['NOT ELIGIBLE', 'attendance below 75%']),
 ('zero held classes', '0 0 8 40\nyes\n', ['Invalid eligibility data']),
 ('attended exceeds held',
  '21 20 8 40\nyes\n',
  ['Invalid eligibility data']),
 ('invalid labs', '15 20 11 40\nyes\n', ['Invalid eligibility data']),
 ('invalid fee flag', '15 20 8 40\nmaybe\n', ['Invalid eligibility data']),
 ('nonnumeric input', 'x 20 8 40\nyes\n', ['Invalid eligibility data'])]

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

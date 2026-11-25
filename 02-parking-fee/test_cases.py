# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('overnight',
  '1 22 0\n2 2 30\ncar\nno\n',
  ['Duration (minutes): 270', 'Parking fee: Rs. 100']),
 ('one minute', '1 0 0\n1 0 1\nbike\nno\n', ['Parking fee: Rs. 10']),
 ('exact hour', '1 0 0\n1 1 0\ncar\nno\n', ['Parking fee: Rs. 20']),
 ('started next hour', '1 0 0\n1 1 1\ncar\nno\n', ['Parking fee: Rs. 40']),
 ('daily cap with penalty',
  '1 0 0\n2 0 0\ncar\nyes\n',
  ['Parking fee: Rs. 300']),
 ('two days plus minute',
  '1 0 0\n3 0 1\ntruck\nno\n',
  ['Parking fee: Rs. 840']),
 ('reverse interval',
  '1 12 0\n1 11 0\ncar\nno\n',
  ['Invalid parking data']),
 ('equal times', '1 12 0\n1 12 0\ncar\nno\n', ['Invalid parking data']),
 ('invalid hour', '1 24 0\n2 1 0\ncar\nno\n', ['Invalid parking data']),
 ('invalid category', '1 0 0\n1 1 0\nbus\nno\n', ['Invalid parking data']),
 ('invalid ticket flag',
  '1 0 0\n1 1 0\ncar\nmaybe\n',
  ['Invalid parking data']),
 ('nonnumeric time', 'x 0 0\n2 1 0\ncar\nno\n', ['Invalid parking data'])]

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

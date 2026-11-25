# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('compressible',
  'aaabbcccc\n',
  ['Encoded: a3b2c4',
   'Original length: 9',
   'Encoded length: 6',
   'Beneficial; characters saved: 3']),
 ('all distinct',
  'abc\n',
  ['Encoded: a1b1c1', 'Encoded length: 6', 'Not beneficial']),
 ('empty text',
  '\n',
  ['Encoded: \n',
   'Original length: 0',
   'Encoded length: 0',
   'Not beneficial']),
 ('one character', 'a\n', ['Encoded: a1', 'Not beneficial']),
 ('equal lengths',
  'aabb\n',
  ['Encoded: a2b2',
   'Original length: 4',
   'Encoded length: 4',
   'Not beneficial']),
 ('multi digit count',
  'aaaaaaaaaaaa\n',
  ['Encoded: a12', 'Beneficial; characters saved: 9']),
 ('spaces preserved',
  '   \n',
  ['Encoded:  3', 'Original length: 3', 'Encoded length: 2']),
 ('case sensitive', 'AaA\n', ['Encoded: A1a1A1']),
 ('digit characters',
  '11122\n',
  ['Encoded: 1322', 'Original length: 5', 'Encoded length: 4'])]

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

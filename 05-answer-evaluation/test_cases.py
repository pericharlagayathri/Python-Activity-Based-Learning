# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('mixed students',
  'ABCD\n3\nS1 ABCD\nS2 AB-D\nS3 DCBA\n',
  ['S1 correct: 4 incorrect: 0 unanswered: 0 score: 16',
   'S2 correct: 3 incorrect: 0 unanswered: 1 score: 12',
   'S3 correct: 0 incorrect: 4 unanswered: 0 score: -4']),
 ('all blank',
  'ABCD\n1\nS1 ----\n',
  ['correct: 0 incorrect: 0 unanswered: 4 score: 0']),
 ('mixed score',
  'ABCD\n1\nS1 AB-A\n',
  ['correct: 2 incorrect: 1 unanswered: 1 score: 7']),
 ('lowercase allowed', 'abcd\n1\nS1 abcd\n', ['score: 16']),
 ('invalid key', 'ABE\n1\n', ['Invalid key or student count']),
 ('wrong answer length', 'ABCD\n1\nS1 ABC\n', ['Invalid student record']),
 ('bad answer character', 'ABCD\n1\nS1 ABCX\n', ['Invalid student record']),
 ('duplicate ID',
  'A\n2\nS1 A\nS1 A\n',
  ['S1 correct: 1 incorrect: 0 unanswered: 0 score: 4',
   'Invalid student record'])]

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

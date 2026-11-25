# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('valid at minimum length', 'Abc123!x\n', ['Password: PASS\n']),
 ('several failures',
  'aaaAdmin\n',
  ['FAIL',
   'missing digit',
   'missing special character',
   'three consecutive identical characters',
   'prohibited substring: admin']),
 ('short password', 'Short1!\n', ['minimum length is 8']),
 ('empty password',
  '\n',
  ['minimum length is 8',
   'missing uppercase',
   'missing lowercase',
   'missing digit',
   'missing special character']),
 ('case insensitive banned word',
  'pAsSwOrD1!\n',
  ['prohibited substring: password']),
 ('missing uppercase', 'abc123!x\n', ['missing uppercase']),
 ('missing lowercase', 'ABC123!X\n', ['missing lowercase']),
 ('unsupported special', 'Abc123?x\n', ['missing special character']),
 ('two repeats allowed', 'Aabc11!x\n', ['Password: PASS\n']),
 ('three repeats rejected',
  'Abc111!x\n',
  ['three consecutive identical characters'])]

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

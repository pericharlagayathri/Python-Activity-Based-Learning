# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('normal diamond',
  '4\n',
  ['Pattern:\n   1\n  121\n 12321\n1234321\n 12321\n  121\n   1\n']),
 ('minimum dimension', '1\n', ['Pattern:\n1\n']),
 ('maximum dimension', '9\n', ['12345678987654321']),
 ('zero', '0\n', ['Invalid dimension']),
 ('too large', '10\n', ['Invalid dimension']),
 ('negative', '-2\n', ['Invalid dimension']),
 ('decimal', '2.5\n', ['Invalid dimension']),
 ('letters', 'abc\n', ['Invalid dimension'])]

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

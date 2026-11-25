# Standard-library checks; run with Python 3.
from pathlib import Path
import subprocess
import sys

solution = Path(__file__).with_name('solution.py')
tests = [('reconciliation',
  '3\nPens 20 10 12 18 25\nBooks 50 10 20 37 40\nFiles 10 0 2 10 5\n',
  ['Pens expected: 18 actual: 18 discrepancy: 0 replenish: 7',
   'Books expected: 40 actual: 37 discrepancy: -3 replenish: 3',
   'Files expected: 8 actual: 10 discrepancy: 2 replenish: 0',
   'Products with discrepancies: 2']),
 ('zero stock',
  '1\nA 0 0 0 0 0\n',
  ['A expected: 0 actual: 0 discrepancy: 0 replenish: 0']),
 ('dispatch all stock',
  '1\nA 5 2 7 0 4\n',
  ['expected: 0 actual: 0 discrepancy: 0 replenish: 4']),
 ('impossible dispatch', '1\nA 5 2 8 0 4\n', ['Invalid product data']),
 ('negative quantity', '1\nA -1 2 0 1 4\n', ['Invalid product data']),
 ('duplicate product',
  '2\nA 1 0 0 1 1\nA 1 0 0 1 1\n',
  ['Invalid product data']),
 ('missing field', '1\nA 1 2\n', ['Invalid product data']),
 ('invalid count', '0\n', ['Invalid product count'])]

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

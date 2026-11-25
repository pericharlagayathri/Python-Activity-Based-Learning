# Run all case-study checks from any working directory.
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
failed = 0
for folder in sorted(root.iterdir()):
    test_file = folder / 'test_cases.py'
    if folder.is_dir() and test_file.is_file():
        print('\n' + folder.name, flush=True)
        result = subprocess.run([sys.executable, str(test_file)])
        if result.returncode != 0:
            failed += 1
if failed:
    print('Failed case studies:', failed)
    sys.exit(1)
print('\nAll 10 case studies passed (90 tests).')

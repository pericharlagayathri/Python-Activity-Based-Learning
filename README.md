# Python Activity-Based Learning

**Name:** Pericharla Gayathri  
**Roll No:** 26000690  
**Section:** Section-2

## Selected case studies

1. [Case 14: Warehouse Inventory Reconciliation](01-warehouse-inventory/)
2. [Case 15: Smart Parking Fee Management](02-parking-fee/)
3. [Case 27: Advanced Numeric Pattern Generator](03-numeric-pattern/)
4. [Case 29: Password Policy Validation Engine](04-password-policy/)
5. [Case 31: String-Based Examination Answer Evaluation](05-answer-evaluation/)
6. [Case 35: Text Compression Using Character Runs](06-text-compression/)
7. [Case 37: Nested Loop Calendar Generator](07-calendar-generator/)
8. [Case 39: Multi-Stage Examination Eligibility System](08-examination-eligibility/)
9. [Case 42: Student Marks Matrix Analysis](09-marks-matrix/)
10. [Case 94: Disaster Relief Supply Allocation](10-relief-allocation/)

## Files

Each folder contains the ten required sections in `README.md`, the program
(`solution.py`), flowchart (`flowchart.png`), sample input (`demo_input.txt`),
interactive terminal output (`output.txt` and `output_screenshot.png`), and test cases with
results (`test_cases.py` and `test_results.txt`).

[Combined PDF: all 10 case studies](Python-Activity-Based-Learning-Complete.pdf)

The PDF shows the source code, sample input, test code, results, flowcharts and
output images in case-study order. All other repository files are also embedded
as PDF attachments, including the README files and original image files. The PDF
does not attach itself. Use a PDF reader with attachment support to extract them.

## Run

Python 3.8 or later is enough; no packages are needed for the programs or tests.
Run a program interactively:

```sh
python 01-warehouse-inventory/solution.py
```

Or use the supplied sample input in a shell that supports input redirection:

```sh
python 01-warehouse-inventory/solution.py < 01-warehouse-inventory/demo_input.txt
```

Run all checks:

```sh
python run_tests.py
```

There are 90 checks covering normal, boundary and invalid inputs. Results are in
`test_results.txt`. Automated checks use Python's standard library; the ten
solutions use only basic input/output, variables, operators, conditionals, loops,
strings, lists, nested lists, tuples and unpacking from the assigned syllabus.
All numerical rules not specified in the main assignment are stated explicitly
under Assumptions. Input prompts specify the expected fields.

Flowcharts use the reference repository's coloured standard symbols and labelled
branches. Output images use its dark terminal style, rendered from real
interactive sessions with sample input echoed. The PDF uses blue headings and
divider lines like the supplied reference PDF.

The supplied main assignment defines the requirements. The supplied second PDF
and [reference repository](https://github.com/emmanuelgotru/Python-Activity-Based-Learning)
were consulted for layout. The selected case numbers match the main assignment.

To submit, upload this folder's contents to your own repository named
`Python-Activity-Based-Learning`, including the combined PDF, and submit its link.

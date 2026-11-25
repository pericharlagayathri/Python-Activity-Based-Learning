# Case 39: Multi-Stage Examination Eligibility System
row = input('Attended held labs_completed internal_marks: ').split()
fees = input('Fees cleared (yes/no): ').strip().lower()
valid = len(row) == 4 and fees in ('yes', 'no')
for value in row:
    if not value.isascii() or not value.isdigit():
        valid = False
if valid:
    attended, held = int(row[0]), int(row[1])
    labs, marks = int(row[2]), int(row[3])
    if held == 0 or attended > held or labs > 10 or marks > 100:
        valid = False
if not valid:
    print('Invalid eligibility data')
else:
    reasons = []
    if attended * 100 < 75 * held:
        reasons.append('attendance below 75%')
    if labs < 8:
        reasons.append('fewer than 8 completed labs')
    if marks < 40:
        reasons.append('internal marks below 40')
    if fees != 'yes':
        reasons.append('fees not cleared')
    print('Attendance:', round(attended * 100 / held, 2), '%')
    if len(reasons) == 0:
        print('ELIGIBLE')
    else:
        print('NOT ELIGIBLE')
        for reason in reasons:
            print('-', reason)

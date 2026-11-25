# Case 42: Student Marks Matrix Analysis
size = input('Students subjects: ').split()
valid = len(size) == 2
for value in size:
    if not value.isascii() or not value.isdigit():
        valid = False
if valid:
    rows, columns = int(size[0]), int(size[1])
    if not 1 <= rows <= 30 or not 1 <= columns <= 10:
        valid = False
if not valid:
    print('Invalid matrix dimensions')
else:
    matrix = []
    for i in range(rows):
        data = input('Student marks: ').split()
        row_ok = len(data) == columns
        marks = []
        for value in data:
            if not value.isascii() or not value.isdigit():
                row_ok = False
            elif int(value) > 100:
                row_ok = False
            else:
                marks.append(int(value))
        if not row_ok:
            valid = False
        matrix.append(marks)
    if not valid:
        print('Invalid marks matrix')
    else:
        totals = []
        for i in range(rows):
            total = sum(matrix[i])
            totals.append(total)
            print('Student', i + 1, 'total:', total,
                  'average:', round(total / columns, 2),
                  'min:', min(matrix[i]), 'max:', max(matrix[i]))
        top = max(totals)
        toppers = []
        for i in range(rows):
            if totals[i] == top:
                toppers.append(i + 1)
        print('Top students:', toppers, 'total:', top)
        low = []
        for j in range(columns):
            subject = []
            for i in range(rows):
                subject.append(matrix[i][j])
            total = sum(subject)
            average = total / rows
            print('Subject', j + 1, 'total:', total,
                  'average:', round(average, 2),
                  'min:', min(subject), 'max:', max(subject))
            if total < 40 * rows:
                low.append(j + 1)
        print('Low-average subjects:', low)

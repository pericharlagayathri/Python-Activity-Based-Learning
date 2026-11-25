# Case 31: String-Based Examination Answer Evaluation
key = input('Answer key (A-D): ').strip().upper()
text = input('Number of students: ').strip()
valid = 1 <= len(key) <= 50
for ch in key:
    if ch not in 'ABCD':
        valid = False
if not text.isascii() or not text.isdigit() or not 1 <= int(text) <= 50:
    valid = False
if not valid:
    print('Invalid key or student count')
else:
    seen = []
    for i in range(int(text)):
        row = input('Student ID and answers (- for blank): ').split()
        row_ok = len(row) == 2
        if row_ok:
            sid, answers = row[0], row[1].upper()
            if sid in seen or len(answers) != len(key):
                row_ok = False
            for ch in answers:
                if ch not in 'ABCD-':
                    row_ok = False
        if not row_ok:
            print('Invalid student record')
        else:
            seen.append(sid)
            correct = wrong = blank = 0
            for j in range(len(key)):
                if answers[j] == '-':
                    blank += 1
                elif answers[j] == key[j]:
                    correct += 1
                else:
                    wrong += 1
            result = (sid, correct, wrong, blank, 4 * correct - wrong)
            sid, correct, wrong, blank, score = result
            print(sid, 'correct:', correct, 'incorrect:', wrong,
                  'unanswered:', blank, 'score:', score)

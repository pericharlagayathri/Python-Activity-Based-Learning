# Case 37: Nested Loop Calendar Generator
start_text = input('Starting weekday (Monday=0): ').strip()
days_text = input('Number of days (28-31): ').strip()
valid = True
for text in (start_text, days_text):
    if not text.isascii() or not text.isdigit():
        valid = False
if valid:
    start, days = int(start_text), int(days_text)
    if not 0 <= start <= 6 or days not in (28, 29, 30, 31):
        valid = False
if not valid:
    print('Invalid weekday or month length')
else:
    print('Calendar:')
    print('Mo Tu We Th Fr Sa Su')
    day = 1
    first_week = True
    while day <= days:
        line = ''
        for weekday in range(7):
            if first_week and weekday < start:
                line += '   '
            elif day <= days:
                line += str(day).rjust(2) + ' '
                day += 1
        print(line.rstrip())
        first_week = False

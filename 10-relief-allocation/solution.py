# Case 94: Disaster Relief Supply Allocation
stock_text = input('Available water food: ').split()
count_text = input('Number of areas: ').strip()
valid = len(stock_text) == 2
for value in stock_text:
    if not value.isascii() or not value.isdigit():
        valid = False
if not count_text.isascii() or not count_text.isdigit():
    valid = False
elif not 1 <= int(count_text) <= 50:
    valid = False
if not valid:
    print('Invalid stock or area count')
else:
    stock = [int(stock_text[0]), int(stock_text[1])]
    areas = []
    names = []
    for i in range(int(count_text)):
        row = input('Area urgency water_needed food_needed: ').split()
        row_ok = len(row) == 4
        if row_ok:
            for value in row[1:]:
                if not value.isascii() or not value.isdigit():
                    row_ok = False
        if row_ok and row[0] in names:
            row_ok = False
        if not row_ok:
            valid = False
        else:
            names.append(row[0])
            areas.append((row[0], int(row[1]), [int(row[2]), int(row[3])]))
    if not valid:
        print('Invalid area data')
    else:
        remaining = stock[:]
        queue = areas[:]
        while len(queue) > 0:
            best = 0
            for i in range(1, len(queue)):
                if queue[i][1] > queue[best][1]:
                    best = i
            name, urgency, needs = queue.pop(best)
            given = []
            unmet = []
            for i in range(2):
                amount = min(remaining[i], needs[i])
                remaining[i] -= amount
                given.append(amount)
                unmet.append(needs[i] - amount)
            print(name, 'allocated:', given, 'unmet:', unmet)
        print('Stock remaining:', remaining)

# Case 27: Advanced Numeric Pattern Generator
text = input('Dimension (1-9): ').strip()
if not text.isascii() or not text.isdigit() or not 1 <= int(text) <= 9:
    print('Invalid dimension')
else:
    n = int(text)
    print('Pattern:')
    for row in range(1, 2 * n):
        if row <= n:
            level = row
        else:
            level = 2 * n - row
        line = ' ' * (n - level)
        for number in range(1, level + 1):
            line += str(number)
        for number in range(level - 1, 0, -1):
            line += str(number)
        print(line)

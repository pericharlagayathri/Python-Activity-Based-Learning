# Case 35: Text Compression Using Character Runs
text = input('Text: ')
encoded = ''
if len(text) > 0:
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            encoded += current + str(count)
            current = ch
            count = 1
    encoded += current + str(count)
print('Encoded:', encoded)
print('Original length:', len(text))
print('Encoded length:', len(encoded))
if len(encoded) < len(text):
    print('Beneficial; characters saved:', len(text) - len(encoded))
else:
    print('Not beneficial')

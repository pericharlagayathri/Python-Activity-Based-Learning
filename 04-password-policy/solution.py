# Case 29: Password Policy Validation Engine
password = input('Password: ')
upper = lower = digit = special = False
errors = []
for ch in password:
    if 'A' <= ch <= 'Z':
        upper = True
    elif 'a' <= ch <= 'z':
        lower = True
    elif '0' <= ch <= '9':
        digit = True
    elif ch in '!@#$%':
        special = True
if len(password) < 8:
    errors.append('minimum length is 8')
if not upper:
    errors.append('missing uppercase')
if not lower:
    errors.append('missing lowercase')
if not digit:
    errors.append('missing digit')
if not special:
    errors.append('missing special character (!@#$%)')
for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        errors.append('three consecutive identical characters')
        break
for word in ('password', 'admin'):
    if word in password.lower():
        errors.append('prohibited substring: ' + word)
if len(errors) == 0:
    print('PASS')
else:
    print('FAIL')
    for error in errors:
        print('-', error)

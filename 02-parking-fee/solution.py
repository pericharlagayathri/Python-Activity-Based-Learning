# Case 15: Smart Parking Fee Management
start = input('Entry day hour minute: ').split()
end = input('Exit day hour minute: ').split()
vehicle = input('Vehicle (bike/car/truck): ').strip().lower()
lost = input('Lost ticket (yes/no): ').strip().lower()
valid = len(start) == 3 and len(end) == 3
for value in start + end:
    if not value.isascii() or not value.isdigit():
        valid = False
rate = 0
for name, price in [('bike', 10), ('car', 20), ('truck', 40)]:
    if vehicle == name:
        rate = price
if rate == 0 or lost not in ('yes', 'no'):
    valid = False
if valid:
    entry = (int(start[0]), int(start[1]), int(start[2]))
    exit_time = (int(end[0]), int(end[1]), int(end[2]))
    for day, hour, minute in (entry, exit_time):
        if day < 1 or hour > 23 or minute > 59:
            valid = False
    day, hour, minute = entry
    a = (day - 1) * 1440 + hour * 60 + minute
    day, hour, minute = exit_time
    b = (day - 1) * 1440 + hour * 60 + minute
    if b <= a:
        valid = False
if not valid:
    print('Invalid parking data')
else:
    duration = b - a
    full_days = duration // 1440
    remainder = duration % 1440
    hours = min(10, (remainder + 59) // 60)
    fee = (full_days * 10 + hours) * rate
    if lost == 'yes':
        fee += 100
    print('Duration (minutes):', duration)
    print('Parking fee: Rs.', fee)

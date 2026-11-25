# Case 14: Warehouse Inventory Reconciliation
text = input('Number of products: ').strip()
if not text.isascii() or not text.isdigit() or not 1 <= int(text) <= 50:
    print('Invalid product count')
else:
    products = []
    names = []
    valid = True
    for i in range(int(text)):
        row = input('Name opening incoming dispatched closing target: ').split()
        row_ok = len(row) == 6
        if row_ok:
            for value in row[1:]:
                if not value.isascii() or not value.isdigit():
                    row_ok = False
        if row_ok:
            name = row[0]
            opening, incoming = int(row[1]), int(row[2])
            dispatched, closing, target = int(row[3]), int(row[4]), int(row[5])
            if name in names or dispatched > opening + incoming:
                row_ok = False
        if not row_ok:
            valid = False
        else:
            names.append(name)
            products.append((name, opening, incoming, dispatched, closing, target))
    if not valid:
        print('Invalid product data')
    else:
        mismatches = 0
        for name, opening, incoming, dispatched, closing, target in products:
            expected = opening + incoming - dispatched
            difference = closing - expected
            refill = max(0, target - closing)
            if difference != 0:
                mismatches += 1
            print(name, 'expected:', expected, 'actual:', closing,
                  'discrepancy:', difference, 'replenish:', refill)
        print('Products with discrepancies:', mismatches)

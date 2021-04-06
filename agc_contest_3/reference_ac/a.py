S = input()
y, x = set(), set()
for c in S:
    if c == 'N' or c == 'S':
        y.add(c)
    else:
        x.add(c)

print(('No', 'Yes')[len(y) % 2 == 0 and len(x) % 2 == 0])

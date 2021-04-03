height, width = [int(e) for e in input().split()]
lst = []

for _ in range(height):
    pict = input()
    lst.append(pict)
    lst.append(pict)

print('\n'.join(lst))

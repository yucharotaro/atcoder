x, y = [int(n) for n in input().split()]
group = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]
if group[x] == group[y]:
    print("Yes")
else:
    print("No")

num = [*map(int, input())]

for i in range(2**3):
    total = num[0]
    op = []
    for j in range(len(num) - 1):
        if (i >> j) & 1:
            total += num[j + 1]
            op.append("+")
        else:
            total -= num[j + 1]
            op.append("-")
    if total == 7:
        print(num[0],
              op[0],
              num[1],
              op[1],
              num[2],
              op[2],
              num[3],
              "=7",
              sep="")
        exit()

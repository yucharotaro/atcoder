X = int(input())

if X > 1000:
    X %= 1000

for i in range(20):
    for j in range(20):
        for k in range(20):
            for l in range(20):
                for m in range(20):
                    for n in range(20):
                        ans = 100 * i + 101 * j + 102 * k + 103 * l \
                            + 104 * m + 105 * n
                        if ans > X:
                            break
                        if ans == X:
                            print(1)
                            exit()
print(0)

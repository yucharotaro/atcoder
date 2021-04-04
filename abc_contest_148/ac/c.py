a, b = map(int, input().split())

ans = a
i = 1
while True:
    if ans % b == 0:
        print(ans)
        exit()
    i += 1
    ans = a * i

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
ans = 0

while True:
    if r1 + c1 == r2 + c2:
        print(ans)
        exit()
    elif r1 - c1 == r2 - c2:
        print(ans)
        exit()
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(ans)
        exit()
    else:
        pass
    ans += 1

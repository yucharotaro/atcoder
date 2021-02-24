def isEven(x):
    return True if x % 2 == 0 else False


A, B, C = map(int, input().split())
cnt = 0

if A == B == C:
    if all([isEven(e) for e in [A, B, C]]):
        print(-1)
    else:
        print(0)
else:
    while all([isEven(e) for e in [A, B, C]]):
        half_A = A / 2
        half_B = B / 2
        half_C = C / 2
        A = half_B + half_C
        B = half_A + half_C
        C = half_A + half_B
        cnt += 1
    print(cnt)

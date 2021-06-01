N, M = map(int, input().split())

ac = [0 for _ in range(N)]
wa = [0 for _ in range(N)]
total_ac = 0
total_wa = 0

for _ in range(M):
    p, s = input().split()
    p = int(p)
    if s == "AC" and ac[p - 1] == 0:
        ac[p - 1] = 1
        total_ac += 1
        total_wa += wa[p - 1]
    elif s == "WA" and ac[p - 1] == 0:
        wa[p - 1] += 1
print(f"{total_ac} {total_wa}")

n = int(input())
s = list(input())
q = int(input())
Q = [list(map(int, input().split())) for _ in range(q)]

for t, a, b in Q:
    if t == 1:
        tmp = s[a - 1]
        s[a - 1] = s[b - 1]
        s[b - 1] = tmp
    elif t == 2:
        s = s[n:] + s[:n]

print("".join(s))

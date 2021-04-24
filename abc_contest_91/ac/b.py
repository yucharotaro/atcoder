n = int(input())
S = dict()
for _ in range(n):
    s = input()
    if s in S.keys():
        S[s] += 1
    else:
        S[s] = 1

m = int(input())
for _ in range(m):
    t = input()
    if t in S.keys():
        S[t] -= 1

print(max(0, max(S.values())))

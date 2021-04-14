n, m = map(int, input().split())
wa = [0] * n
problems = [0] * n
for _ in range(m):
    p, s = input().split()
    if s == "AC":
        problems[int(p) - 1] = 1
    elif s == "WA" and problems[int(p) - 1] != 1:
        wa[int(p) - 1] += 1

print(sum(problems), sum([i * j for i, j in zip(problems, wa)]))

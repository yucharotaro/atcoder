n, _ = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
print("".join(sorted(s)))

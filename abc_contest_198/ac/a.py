N = int(input())
ans = 0

a = [i for i in range(N)]
b = []

while len(b) - 1 != N - 1:
    if len(a) == 1:
        break

    b.append(a.pop())
    ans += 1

print(ans)

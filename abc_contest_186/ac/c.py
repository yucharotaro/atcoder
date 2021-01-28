N = int(input())

ans = N
for n in range(1, N + 1):
    if ("7" in str(n) or "7" in oct(n)):
        ans -= 1

print(ans)

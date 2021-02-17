n, k = map(int, input().split())

ans = 0
while True:
    if n == 1:
        ans += 1
        break
    elif n == 0:
        break
    n //= k
    ans += 1

print(ans)

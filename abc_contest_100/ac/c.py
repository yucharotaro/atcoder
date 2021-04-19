n = int(input())
a = list(map(int, input().split()))
cnt = 0

a = [e for e in a if e % 2 == 0]
for e in a:
    while e % 2 == 0:
        e //= 2
        cnt += 1

print(cnt)

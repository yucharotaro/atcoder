N = int(input())
A = list(map(int, input().split()))

cnt = 0
while True:
    A = sorted([a * 3 for a in A if a % 2 == 0])
    if len(A) > 0:
        A[-1] //= 6
        cnt += 1
    else:
        break

print(cnt)

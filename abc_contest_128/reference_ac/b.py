N = int(input())

arr = []
for i in range(N):
    s, p = input().split()
    p = int(p)
    arr.append((s, -p, i + 1))

arr.sort()
for s, p, i in arr:
    print(i)

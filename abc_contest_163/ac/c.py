N = int(input())
A = list(map(int, input().split()))
staff = [0] * N

for a in A:
    staff[a - 1] += 1

for p in staff:
    print(p)

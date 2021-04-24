n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = set([e for e in range(1, 1001)])
for i, j in zip(A, B):
    tmp = set([e for e in range(i, j + 1)])
    cnt = cnt & tmp

print(len(cnt))

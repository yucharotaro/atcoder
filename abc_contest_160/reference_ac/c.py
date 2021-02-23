import sys
read = sys.stdin.buffer.read

K, N = list(map(int, input().split()))
A = list(map(int, input().split()))
A.append(A[0] + K)
# print(len(A), len(A[1:]))
# print([y - x for x, y in zip(A, A[1:])])
gap = max(y - x for x, y in zip(A, A[1:]))
print(K - gap)

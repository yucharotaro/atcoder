import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, *A = map(int, read().split())

A.sort()
answer = sum(A[N::2])
print(answer)

def is_even(x):
    return False if x % 2 else True


N = int(input())
A = list(map(int, input().split()))

cnt = 0
while all(map(is_even, A)):
    A = [e / 2 for e in A]
    cnt += 1
print(cnt)

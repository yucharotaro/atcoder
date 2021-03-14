N, A, B = map(int, input().split())

c = N // (A + B)
y = N % (A + B)
if y >= A:
    print(c * A + A)
elif y < A:
    print(c * A + y)
else:
    print(c * A)

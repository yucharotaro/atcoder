A, B = map(int, input().split())
if abs(A - B) >= 2:
    x = max(A, B)
    print(2 * x - 1)
elif abs(A - B) < 2:
    print(A + B)

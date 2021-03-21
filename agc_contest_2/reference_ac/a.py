a, b = map(int, input().split())
if a * b <= 0:
    print('Zero')
elif b < 0 and ((b - a) + 1) % 2 == 1:
    print('Negative')
else:
    print('Positive')

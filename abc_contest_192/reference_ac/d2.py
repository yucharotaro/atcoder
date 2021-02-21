def f(x, mid):
    tmp = 0
    for i, e in enumerate(str(X)[::-1]):
        tmp += int(e) * (mid**i)
    print(f"tmp={tmp}")
    return tmp


X = input()
M = int(input())
d = max(map(int, str(X)))

left = 0
right = 10**60 + 1
print(f"left={left}, right={right}")
while right - left > 1:
    mid = (left + right) // 2
    print(f"mid={mid}")
    if f(X, mid) <= M:
        left = mid
    else:
        right = mid
    print(f"left={left}, right={right}")
print(left - d if left < 10**60 else 1)

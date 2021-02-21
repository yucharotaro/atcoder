a, b = input().split()
ab = int(a + b)

left = 0
right = ab + 1
while right - left > 1:
    mid = (left + right) // 2
    if mid**2 > ab:
        right = mid
    else:
        left = mid
print("Yes" if (left**2 == ab) or (right**2 == ab) else "No")

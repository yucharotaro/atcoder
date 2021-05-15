A, B, C = sorted(map(int, input().split()))
if C - B == B - A:
    print("Yes")
else:
    print("No")

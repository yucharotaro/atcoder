A, B, C, K = map(int, input().split())
unfair = 10**18

if abs(A - B) > unfair:
    print("Unfair")
    exit()

print(A - B if K % 2 == 0 else B - A)

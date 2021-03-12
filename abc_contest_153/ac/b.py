H, N = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]

print("Yes" if H <= sum(A) else "No")

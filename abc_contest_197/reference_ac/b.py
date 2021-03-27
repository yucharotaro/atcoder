H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
A = []
for h in range(H):
    A.append(input())

result = 0
for w in range(X, H):
    if A[w][Y] == ".":
        result += 1
    else:
        break

for w in range(X, -1, -1):
    if A[w][Y] == ".":
        result += 1
    else:
        break

for h in range(Y, W):
    if A[X][h] == ".":
        result += 1
    else:
        break

for h in range(Y, -1, -1):
    if A[X][h] == ".":
        result += 1
    else:
        break

print(result - 3)

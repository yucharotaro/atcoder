x, y = map(int, input().split())
A = [x]
while True:
    if A[-1] * 2 > y:
        break
    A.append(A[-1] * 2)

print(len(A))

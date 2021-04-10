x = int(input())
ans = [1]
for i in range(2, x):
    p = 2
    while i**p <= x:
        ans.append(i**p)
        p += 1
print(max(ans))

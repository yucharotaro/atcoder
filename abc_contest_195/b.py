A, B, W = map(int, input().split())

W = 1000 * W
min_m = 1000
max_m = 1

possible = False
ans = []
x = 0
while True:
    if A * x > W:
        break
    y = 0
    while True:
        f = (A * x) + (B * y)
        print(x, y, f)
        if f > W:
            break
        if f == W:
            possible = True
            ans.append(x + y)
        y += 1
    x += 1
print(ans)

#for i in range(A, B + 1):
#    if W % i == 0:
#        if min_m > W // i:
#            min_m = W // i
#            print(min_m)
#        if max_m < W // i:
#            max_m = W // i
#            print(max_m)
#        possible = True
ans = set(ans)
if possible:
    print(min(ans), max(ans))
else:
    print("UNSATISFIABLE")

N = int(input())

f = 0
s = 0
index = 0
for i in range(N):
    a = int(input())
    if a > f:
        index = i
        s = f
        f = a
    elif a > s:
        s = a

for i in range(N):
    if i == index:
        print(s)
    else:
        print(f)

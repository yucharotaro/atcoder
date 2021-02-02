n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

m = 0
aten = -99

for e in a:
    m += b[e - 1]
    if aten < n - 1 and abs(aten - e) == 1:
        m += c[aten - 1]
    aten = e
print(m)

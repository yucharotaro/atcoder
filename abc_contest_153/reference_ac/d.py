h = int(input())
a = 1
c = 0
while h:
    h //= 2
    c += a
    a *= 2
print(c)

H = int(input())

cnt = 0
loop = 1
while H != 1:
    H //= 2
    cnt += 2**loop
    loop += 1
print(cnt + 1)

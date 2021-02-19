H, W = list(map(int, input().split()))

odd_line = 0
even_line = 0

if H == 1 or W == 1:
    print(1)
    exit()

if W % 2 == 0:
    odd_line = even_line = W // 2
else:
    even_line = W // 2
    odd_line = even_line + 1

if H % 2 == 0:
    print(int(odd_line * (H / 2) + even_line * (H / 2)))
else:
    print(int((odd_line * (H // 2 + 1)) + (even_line * (H // 2))))

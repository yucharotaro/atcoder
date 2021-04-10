x = int(input())

w = x // 100
a = x % 100
if a <= w * 5:
    print(1)
else:
    print(0)

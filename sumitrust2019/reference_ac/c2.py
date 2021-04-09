X = int(input())

w = X // 100
amari = X % 100

if amari <= w * 5:
    print(1)
else:
    print(0)

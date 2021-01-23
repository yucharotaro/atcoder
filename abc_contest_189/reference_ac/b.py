N, X = map(int, input().split())
s = 0

for i in range(N):
    v, p = map(int, input().split())
    s += v * p
    # 浮動小数点の演算は一般に誤差を含みます。
    # 整数のみで計算できるように適切な式変形が必要です。
    if s > X * 100:
        print(i + 1)
        exit()

print(-1)

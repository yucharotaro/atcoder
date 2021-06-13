H, W = map(int, input().split())

# 入力の周囲を.で埋めて、(1,1)マスから確認していく。
x = ["." * (W + 2)]
for k in range(H):
    x.append("." + input() + ".")
x.append("." * (W + 2))

ans = []
for i in range(1, H + 1):
    b = []
    for k in range(1, W + 1):
        if x[i][k] == ".":
            sum = 0
            aa = x[i + 1][k - 1:k + 2].count("#") + x[i][k - 1:k + 2].count(
                "#") + x[i - 1][k - 1:k + 2].count("#")
            b.append(aa)
        else:
            b.append('#')

    ans.append(b)
for i in ans:
    print(''.join(map(str, i)))

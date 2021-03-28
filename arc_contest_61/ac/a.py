S = input()

ans = 0
for i in range(2**(len(S) - 1)):
    tmp = S[0]
    for j in range(len(S) - 1):
        # 順に右シフトして最下位ビットのフラグチェック
        if (i >> j) & 1:
            tmp += "+"
        tmp += S[j + 1]
    ans += sum(map(int, tmp.split("+")))

print(ans)

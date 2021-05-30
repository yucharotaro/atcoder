A, B, C, D = list(map(int, list(input())))
li = [B, C, D]

for i in range(8):
    exp = f"{A}"
    ans = A
    for j in range(3):
        if (i >> j) & 1:
            ans += li[j]
            exp += f"+{li[j]}"
        else:
            ans -= li[j]
            exp += f"-{li[j]}"
    if ans == 7:
        print(f"{exp}=7")
        exit()

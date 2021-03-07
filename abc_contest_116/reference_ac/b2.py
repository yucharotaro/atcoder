def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


i = 0
n = int(input())
while True:
    # Collatz problemtとして知られている問題。
    # 5 * 10^260以下ならnは4,2,1,4...と繰り返される。
    if n == 4 or n == 2 or n == 1:
        print(i + 4)
        break
    i += 1
    n = f(n)

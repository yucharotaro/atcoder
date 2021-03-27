def solve():
    from itertools import product

    N = int(input())
    A = [*map(int, input().split())]

    ans = float('INF')

    for _bit in product((True, False), repeat=N - 1):
        # A[-1]の右に常に区切り棒があることにすると、実装が楽
        bit = list(_bit) + [True]
        #print(f"bit={bit}")
        score = 0
        cur = 0
        for i in range(N):
            cur |= A[i]
            #print(f"cur={cur}")
            if bit[i]:
                #  区切り棒が来たら、今までORしたものをXORして、再びOR
                score ^= cur
                #print(f"score={score}")
                cur = 0
        ans = min(ans, score)
    print(ans)


solve()

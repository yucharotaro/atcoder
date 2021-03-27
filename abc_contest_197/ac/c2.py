def main():
    from itertools import product

    N = int(input())
    A = list(map(int, input().split()))

    ans = float("INF")

    for pair in product([1, 0], repeat=N - 1):
        sep = list(pair) + [1]
        _or = 0
        _xor = 0

        for i in range(N):
            _or |= A[i]
            if sep[i]:
                _xor ^= _or
                _or = 0
        ans = min(ans, _xor)

    print(ans)


main()

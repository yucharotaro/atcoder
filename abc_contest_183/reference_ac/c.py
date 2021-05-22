def main():
    from itertools import permutations

    n, k = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for perm in permutations(range(1, n)):
        now = 0
        p = 0
        for u in perm:
            now += g[p][u]
            p = u
        now += g[p][0]
        if now == k:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()

from itertools import permutations


def main():
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        t = list(map(int, input().split()))
        T.append(t)

    cnt = 0
    for pair in permutations(range(1, N), N - 1):
        total = T[0][pair[0]] + T[pair[-1]][0]
        for i in range(len(pair) - 1):
            total += T[pair[i]][pair[i + 1]]
        if total == K:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()

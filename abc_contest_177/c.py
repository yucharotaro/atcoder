from itertools import combinations


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans = 0
    m = 10**9 + 7
    # for i in range(n - 2):
    #     ans += pow((n - i - 1) * (a[i] * a[i + 1] + a[i] * a[-1]), 1, m) / 2
    # ans += pow(a[-2] * a[-1], 1, m)
    for pair in combinations(a_list, 2):
        ans += pow(pair[0] * pair[1], 1, 10**9 + 7)
    print(pow(ans, 1, m))


if __name__ == "__main__":
    main()

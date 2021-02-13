def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    m = 10**9 + 7
    s = pow(sum(a_list), 1, m)
    ans = 0

    for a in a_list:
        s -= a
        s %= m
        ans += (s * a) % m
    print(ans % m)


if __name__ == "__main__":
    main()

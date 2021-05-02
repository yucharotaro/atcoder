def main():
    n, m, *ls = map(int, open(0).read().split())
    ab = list(zip(ls[::2], ls[1::2]))
    ab.sort(key=lambda x: x[0])
    sum = 0
    ans = 0
    for i, j in ab:
        if sum + j < m:
            sum += j
            ans += i * j
        else:
            ans += (m - sum) * i
            break
    print(ans)


if __name__ == '__main__':
    main()

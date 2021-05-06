def main():
    N, *A = map(int, open(0).read().split())
    count = 0
    cur = 1
    while count < N:
        count += 1
        cur = A[cur - 1]
        if cur == 2:
            print(count)
            return
    print(-1)


if __name__ == '__main__':
    main()

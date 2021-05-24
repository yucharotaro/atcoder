def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    pre = [0 for _ in range(N)]
    for j in range(N):
        pre[B[C[j] - 1] - 1] += 1

    cnt = 0
    for i in range(N):
        cnt += pre[A[i] - 1]

    print(cnt)


if __name__ == "__main__":
    main()

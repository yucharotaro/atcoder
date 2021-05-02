def main():
    _ = int(input())
    A = [0] + list(map(int, input().split()))
    ans = sum(i == A[j] for i, j in enumerate(A[1:], 1)) // 2
    print(ans)


if __name__ == "__main__":
    main()

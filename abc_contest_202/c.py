def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    set_B = set(B)
    C = list(map(int, input().split()))
    set_C = set(C)

    cnt = 0
    for i in range(N):
        if A[i] not in set_B:
            continue
        for c in set_C:
            if A[i] == B[c - 1]:
                cnt += C.count(c)
    print(cnt)


if __name__ == "__main__":
    main()

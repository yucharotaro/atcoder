N, A, B = map(int, input().split())

print(
    sum([
        i for i in range(1, N + 1)
        if (sum(map(int, str(i))) >= A and (sum(map(int, str(i))) <= B))
    ]))

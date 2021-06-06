import sys


def dfs(before_v, v, graph, seen):
    seen[v] = 1

    for next_v in graph[v]:
        if seen[next_v] == 1:
            continue
        if before_v == next_v:
            continue
        dfs(v, next_v, graph, seen)


sys.setrecursionlimit(100000)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A - 1].append(B - 1)

ans = 0
for n in range(N):
    seen = [0 for _ in range(N)]
    dfs(-1, n, graph, seen)
    ans += sum(seen)
print(ans)

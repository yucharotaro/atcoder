from collections import deque


def bfs(u):
    global N
    global tree
    dist = [-1] * N
    dist[u] = 0
    #print(dist)
    q = deque()
    q.append(u)

    while q:
        u = q.popleft()
        #print("u=", u)
        for v in tree[u]:
            #print("v=", v)
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
        #print(dist)
    max_dist = max(dist)

    return dist.index(max_dist), max_dist


N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    tree[u].append(v)
    tree[v].append(u)

# 任意の頂点から各頂点までの最短距離を調べ、最も最短距離が大きい頂点を求める。
u, _ = bfs(0)
# 最も最短距離が大きかった頂点から各頂点までの最短距離を調べ、
# 最短距離が最も大きい頂点までの距離が木の直径(E)となる。
_, E = bfs(u)

print(E + 1)

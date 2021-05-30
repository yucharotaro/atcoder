N, K = map(int, input().split())

friends = dict()
for _ in range(N):
    A, B = map(int, input().split())
    if A in friends:
        friends[A] += B
    else:
        friends[A] = B

friends = dict(sorted(friends.items(), key=lambda x: x[0]))
v = 0
while K > 0:
    #print(f"K = {K}, v = {v}, friends = {friends}")
    if len(friends) > 0:
        nv = next(iter(friends))
        if nv > K + v:
            v += K
            K = 0
        else:
            K -= nv - v
            v += nv - v
            K += friends.pop(nv)
    else:
        v += K
        K = 0

print(v)

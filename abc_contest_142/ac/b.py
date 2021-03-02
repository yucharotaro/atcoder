N, K = map(int, input().split())
hn = list(map(int, input().split()))

print(len(list(h for h in hn if h >= K)))

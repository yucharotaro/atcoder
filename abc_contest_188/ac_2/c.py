n = int(input())
a_list = list(map(int, input().split()))

mid = (2**n // 2)
p1 = max(a_list[:mid])
p2 = max(a_list[mid:])
loser = min(p1, p2)

print(a_list.index(loser) + 1)
